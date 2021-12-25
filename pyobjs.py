from __future__ import annotations
from typing import Iterable
import json

class Object(dict):

    def __init__(self, **kwargs):

        super().__init__()

        for k, v in kwargs.items():
            v = Object.__assign_object(v)
            Object.__setattr__(self, k, v)

    @staticmethod
    def __assign_object(_value):

        if isinstance(_value, dict):
            # dictionaries are converted into object and processed recursively
            _value = Object(**_value)
            for k, v in _value.items():
                _value[k] = Object.__assign_object(v)

        elif type(_value) == str:
            # string is iterable but don't need to iterate recursively
            pass

        elif isinstance(_value, Iterable):

            # idx to use if needed
            v_range = range(0, len(_value)+1)

            for idx, item in zip(v_range, _value):

                # item assignation ecursively if needed
                item = Object.__assign_object(item)

                # distinct types of assignation depending of object type
                if type(_value) == list:
                    _value[idx] = item

                elif type(_value) == set:
                    _value.add(item)

        return _value

    def __getattr__(self, _key):
        '''
            Extends dictionary to get key:value pairs with attribute notation self._key
            Args:
                _key (str): attribute from which we want to get value.
            Return:
                Structure contained in attr or None if does not exist.
        '''
        return super().get(_key)

    def __setattr__(self, _key, _value):
        '''
            Sets a new key:value pair with _key:_value values. It performs the operations recursively.
            Args:
                _key (str): name of the new attr. If exists, old value is overriden.
                _value (Any): any structure to assign to attribute with name _key.
        '''
        _value = Object.__assign_object(_value)
        super().__setitem__(_key, _value)

    def __delattr__(self, _key):
        '''
            Deletes the attribute with name _key unbinding it from namespace.
            Args:
                _key (str): the attribute name we want to delete.
            Notes:
                1. If value of attribute _key is an Object, this function deletes recursively all its elements.
        '''
        super().__delitem__(_key)

    def __str__(self):
        return json.dumps(self)