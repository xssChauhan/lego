# lego
## Build your classes with minimum effort


Assigning values to `self` in from variables passed as arguments to `__init__` is generally a mundane and repeating task.
Lego helps you reduce the effor to a minimum by assigning the arguments to `self` automagically.


### Without lego

```python
class Planet:
  def __init__(self , name , position , boom = False):
    self.name = name
    self.position = position
    self.boom = boom

>> p = Planet("Earth" , 3)
>> p.name
'Earth'
>> p.position
3
>> p.boom
False
```



### With lego
```python
import lego

class Planet:
  @lego.assemble
  def __init__(self , name , position , boom = False):
    pass

>> p = Planet("Earth" , 3)
>> p.name
'Earth'
>> p.position
3
>> p.boom
False
```

lego does not stop you from customizing the `__init__` function.
```python
class Planet:
  @lego.assemble
  def __init__(self , name , position , boom = False):
    #All the assignments have been made
    self.distance = self.position * 1000

>> p = Planet("Earth" , 3)
>> p.name
'Earth'
>> p.position
3
>> p.boom
False
>> p.distance
3000
```

Inspired from this SO [answer](http://stackoverflow.com/a/1389216/5596800)
