class dog:
      def __init__(self,name,age):
        self.name=name
        self.age=age
      def makesound(self):
        print("Dog barking")
      def info(self):
        print("Dog name:",self.name)
        print("Dog age:",self.age)
class cat:
      def __init__(self,name,age):
        self.name=name
        self.age=age
      def makesound(self):
        print("MEOW MEOW")
      def info(self):
        print("cat name:",self.name)
        print("cat age:",self.age)

objdog=dog("Jimmy",7)
objcat=cat("Kate",6)

for i in (objcat,objdog):
  i.makesound()
  i.info()