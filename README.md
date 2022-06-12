# Pyobjs

The objective of this repository is to implement a series of classes that allow us to emulate the structure notation of Javascript.

## Object

This class implements modifications of Python dictionaries to allow JS Object-like notation to assign an retreive information. It also works for recursive structures converting dictionaries (and child classes) into Object.

### Caveats
* You should take care about using this class with mutables types stored into tuple, as tuples are not mutables. As an example, this class can't create an `Object` class from a `dict` inside a `tuple` due its inmutability, so it avoid explore data into tuples.

### How to use

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
Boston 175
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
We can also get and modify nested attrs:
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



