def desc(func):
  def inner(*args, **kwargs):
    print('do something before real func')
    func(args, kwargs)
    print('do something after real func')
  return inner

@desc
def realfunc(name, age):
  print('this is the real func', name, age)

realfunc('heelo', 22)


def auth(request, kargs):
  print('auth successful')
  print('request:', request)
  print('kargs:', kargs)

def log(request, kargs): 
  print('auth successful')
  print('log finished')
  print('kargs:', kargs)

def filter(auth, log):
  def outer(main_func):
    def wrapper(request, kargs):
      before_result = auth(request, kargs)
      main_func(request, kargs)
      after_result = log(request, kargs)
      
    return wrapper
  return outer

@filter(auth, log)
def func_business(name, age):
  print('real business code')

func_business('hello', 22)
