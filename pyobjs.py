class Object(dict):

    def __init__(self, **kwargs):

        for k, v in kwargs.items():
            Object.__setattr__(self, k, v)

    def __repr__(self):
        '''
            Prints dictionary as a string.
        '''
        return ', '.join([f'{k}:{v}' for k, v in self.__dict__.items()])

    def __contains__(self, _value):
        '''
            Check if exists an attribute _value into the class.
            Args:
                _value (str) --> key to search for into attributes list.
        '''
        return _value in self.__dict__.keys()

    def __getitem__(self, _key):
        '''
            Same as __getattr__.
        '''
        return Object.__getattr__(self, _key)

    def __getattr__(self, _key):
        '''
            Returns value contained in _key attribute, else None.
            Args:
                _key (str): attribute from which we want to get value.
        '''
        ins_dict = self.__dict__
        x = ins_dict[_key] if _key in ins_dict.keys() else None
        return x

    def __setitem__(self, _key, _value):
        '''
            Same as __setattr__.
        '''
        Object.__setattr__(self, _key, _value)

    def __setattr__(self, _key, _value):
        '''
            Sets a new key:value pair with _key:_value values.
            Args:
                _key (str): name of the new attr. If exists, old value is overriden.
                _value (Any): any value to assign to attribute with name _key.
            Notes:
                1. If _value is of type 'dict', a new instance of Object (this class) is created as value of key:value pair.
        '''
        _value = Object(**_value) if isinstance(_value, dict) else _value
        self.__dict__[_key] = _value

    def __delitem__(self, _key):
        '''
            Same as __delattr__.
        '''
        Object.__delattr__(self, _key)

    def __delattr__(self, _key):
        '''
            Deletes the attribute with name _key unbinding it from namespace.
            Args:
                _key (str): the attribute name we want to delete.
            Notes:
                1. If value of attribute _key is an Object, this function deletes recursively all its elements.
        '''
        if _key in self:

            _item = self[_key]

            # if attr is an object we need to delte it recursively
            if isinstance(_item, Object):
                for k in list(_item.__dict__.keys()):
                    Object.__delattr__(_item, k)

            # Finally delete the main element, Object or not
            del self.__dict__[_key]

    def __del__(self):
        '''
            Deletes all attributes of the insatnce.
            Notes:
                1. Deletion consists of deleting all attributes individually and finally deleting the instance structure.
        '''
        ins_dict: dict = self.__dict__
        ins_items: list = list(ins_dict.items())

        # iterate each value and if is Object deletes it
        for attr, obj in ins_items:
            Object.__delattr__(self, attr)

        del self