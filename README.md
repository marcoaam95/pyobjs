# **Pyobjs**

The objective of this repository is to implement a series of classes that allow us to emulate the structure notation of Javascript.

## **Object**

This class implements modifications of Python dictionaries to allow JS Object-like notation to assign an retrieve information.

### How to use

> **_NOTE:_**  When Object is printed, it returns formatted valid JSON string.


Creating a new object:
```python

from pyobjs import Object

obj = Object(name='John', surname='Smith', age=39)

print(obj)
```
```
{"name": "John", "surname": "Smith", "age": 39}
```

\
Item assignation and retrieval:
```python
obj['height'] = 175
obj.city = 'Boston'

print(obj['city'], obj.height)
```

```
Madrid 175
```

\
Nested elements:
```python
obj.dogs = [
    {'name': 'Maya', 'size': 'big', 'height': 100},
    {'name': 'Max', 'size': 'tiny', 'height': 40},
    {'name': 'Connor', 'size': 'mid', 'height': 60, 'awards': [('Mid Dog Award', '2019/08/21')]}
]

print(obj)
```
```
{"name": "John", "surname": "Smith", "age": 39, "height": 175, "city": "Madrid", "dogs": [{"name": "Maya", "size": "big", "height": 100}, {"name": "Max", "size": "tiny", "height": 35}, {"name": "Connor", "size": "mid", "height": 60, "awards": [("Mid Dog Award", "2019/08/21")]}]}
```

\
We also can get and modify nested attrs:
```python
# Modifying Max height to 35
obj.dogs[1].height = 35
print(obj.dogs[1])
```
```
{"name": "Max", "size": "tiny", "height": 35}
```


```python
# Get name of first dog
print(obj.dogs[0].name)
```
```
Maya
```



