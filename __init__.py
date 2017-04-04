from functools import wraps
import inspect , itertools

def assemble(func):
	names , varargs , keywords , defaults = inspect.getargspec(func)
	@wraps(func)
	def wrapper(self , *args , **kargs):
		for name,arg in itertools.chain(zip(names[1:] , args) , kargs.items()):
			setattr(self,name , arg)
		if defaults:
			for name,default in zip(reversed(names),reversed(defaults)):
				if not hasattr(self,name):
					setattr(self , name , default)
		func(self , *args , **kargs)
	return wrapper