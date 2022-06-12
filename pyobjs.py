from __future__ import annotations
from typing import Iterable
import json

class Object(dict):

    def __init__(self, **kwargs):

        super().__init__()

        for k, v in kwargs.items():
            Object.__setattr__(self, k, v)

    @staticmethod
    def is_iterable(_value):
        try:
            iter(_value)
            return True
        except TypeError:
            return False

    @staticmethod
    def is_mutable(_value):
        try:
            _value.__setitem__
            return True
        except AttributeError:
            return False

    @staticmethod
    def __assign_object(_value):

        if isinstance(_value, dict):
            # direct instances of dict are converted into object and processed recursively
            _value = Object(**_value)
            for k, v in _value.items():
                _value[k] = Object.__assign_object(v)

        elif type(_value) == str:
            # string is iterable but don't need to iterate recursively
            pass

        elif Object.is_iterable(_value) and Object.is_mutable(_value):
            # for iterable and mutable object we are going to check if they have more dict classes (or child) recursively

            for idx, item in enumerate(_value):
                # item assignation ecursively if needed
                _value[idx] = Object.__assign_object(item)

        return _value

    def __getattr__(self, _key):
        '''
            Extends dictionary to get key:value pairs with attribute notation self._key
            Args:
                _key (str): attribute from which we want to get value.
            Return:
                Structure contained in attr or None if does not exist.
        '''
        return self.__getitem__(_key)

    def __setattr__(self, _key, _value):
        '''
            Sets a new key:value pair with _key:_value values. It performs the operations recursively.
            Args:
                _key (str): name of the new attr. If exists, old value is overriden.
                _value (Any): any structure to assign to attribute with name _key.
        '''
        _value = Object.__assign_object(_value)
        self.__setitem__(_key, _value)

    def __delattr__(self, _key):
        '''
            Deletes the attribute with name _key unbinding it from namespace.
            Args:
                _key (str): the attribute name we want to delete.
            Notes:
                1. If value of attribute _key is an Object, this function deletes recursively all its elements.
        '''
        self.__delitem__(_key)


