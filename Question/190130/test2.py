# class Dele():
#     def __init__ (self, **kargs):
#         self.kargs = kargs

#     def gogo(self):
#         for k,v in self.kargs.items():
#             if(len(v) <= 5):
#                 del self.kargs[k]
#                 return self.kargs

# fruit = Dele(사과="apple",바나나="banana")
# print(fruit.gogo())

class Fruit:
    def __init__(self,**kwargs):
      self.kwargs = kwargs

    def delete(self):
      for i in self.kwargs:
          if len(self.kwargs.get(i)) > 5:
              print({i:self.kwargs.get(i)})

fruit ={"사과":"apple","바나나":"banana"}
f1=Fruit(**fruit)
f1.delete()