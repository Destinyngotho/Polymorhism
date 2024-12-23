class emp:
  __companyname="ABC" #private variable
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  def disp(self):
    print("My company name:",self.__companyname)
obj=emp('Destiny',100)
class emp:
  __companyname="ABC" #private variable
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  def __disp(self):
    print("My company name:",self.__companyname)

obj=emp("Destiny",100)
# print(obj.__companyname)
obj.disp()