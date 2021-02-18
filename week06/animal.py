"""
这个类可以使用如下形式为动物园增加一只猫：
if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，
是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，
除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物
（同一个动物实例）不能被重复添加的功能。

"""
class Animal():
  def __init__(self,type,size,character):
      self.type=type
      self.size=size
      self.character=character

  def is_danger(self):
      if(self.size=='中' or self.size=='大') and self.type=='食肉' and self.character=='凶猛':
          self.danger =True
      else:
          self.danger=False

class Cat(Animal):
    voice='喵喵'
    def __init__(self,name,type,size,character):
        self.name=name
        super().__init__(type,size,character)
    @property
    def is_pet(self):
        return False if self.is_danger else True

class Dog(Animal):
    voice = '汪汪'

    def __init__(self, name, type, size, character):
        self.name = name
        super().__init__(type, size, character)
    @property
    def is_pet(self):
        return False if self.is_danger else True


class Zoo(object):
    def __init__(self,name):
        self.name=name
        self.zoo=set()
    def add_animal(self,animal):
        animal_class_name =animal.__class__.__name__

        if animal_class_name in self.zoo:
            print(f"存在{animal_class_name}")
        else:
            self.zoo.add(animal)
            print(self.zoo)



if __name__ =='__main__':
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)

    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    


