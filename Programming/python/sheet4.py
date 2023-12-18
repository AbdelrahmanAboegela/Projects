# class A:
#     aval=10
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def method1(self):
#         print("this is class a method")
#         self.w=1
        
# class B:
#     bval=20
#     def __init__(self,z):
#         self.z=z
#     def method1(self):
#         print("this is class b method")
#         z=self.z+B.bval
#         print(z)
# class C(A,B):
#     aval=30
#     def __init__(self,x,y,z,w):
#         A.__init__(self,x,y)
#         B.__init__(self,z)
#         self.w=w
#     def method1(self):
#         super().method1()
#         print(self.w)
#         A.method1(self)
#         B.method1(self)
#         A.aval=B.bval+C.aval
#         print(A.aval)
#         print(C.aval)
# obj=C(10,20,30,40)
# obj.method1()
        

# class A:
#     def f(self):
#         return self.g()
#     def g(self):
#         return 'A'
# class B(A):
#     def g(self):
#         return'B'
# a = A()
# b = B()
# print(a.f(),b.f())
# print(a.g(),b.g())

# class Shape:
#     def __init__(self):
#         self.area = 0

#     def get_area(self):
#         return self.area


# class Square(Shape):
#     def __init__(self, length):
#         super().__init__()
#         self.length = length
#         self.area = length ** 2

#     def get_area(self):
#         return self.area


# square = Square(10)
# print(square.get_area())  

# shape = Shape()
# print(shape.get_area())  

# class Jets:
#     def __init__ (self,name,country):
#         self.type = "Jet"
#         self.area = "Air"
#         self.name = name
#         self.origin = country
        
# # type your code below inside the new class
# class F14(Jets):
#     def __init__(self, *args):
#         super().__init__("F14", "USA")

    
# a=F14()
# print(a.origin)
# print(a.name)



# class Jets:
#     model = None
#     country = 0
    
#     def __init__ (self,name,country):
#         self.type = "Jet"
#         self.area = "Air"
#         self.name = name
#         self.origin = country
        
# # type your code below inside the new class
# class F14(Jets):
#     def __init__(self):
#         super().__init__("F14", "USA")
#         self.engine = 2
#         self.seat = 2
#         self.tail = 2

#     def set_engine(self, num):
#         self.engine = num

#     def set_seat(self, num):
#         self.seat = num

#     def set_tail(self, num):
#         self.tail = num

#     def set_speed(self, speed):
#         self.speed = speed
        
# f14 = F14()
# print(f14.name)    
# print(f14.origin)  
# print(f14.engine)
# print(f14.tail)
# print(f14.seat)
# f14.set_speed(1000)
# print(f14.speed)   


# class Jets:
#     model = None
#     country = 0
    
#     def __init__ (self, name, country):
#         self.type = "Jet"
#         self.area = "Air"
#         self.name = name
#         self.origin = country
        
# class AJS37(Jets):
#     def __init__(self):
#         super().__init__("AJS37", "Sweden")
        
# b = AJS37()
# print(b.name)  
# print(b.origin)  


# class Button:
#     def __init__(self, label):
#         self.label = label

#     def press(self):
#         print(f"Button {self.label} was pressed")

# class Keyboard:
#     def __init__(self, *buttons):
#         self.buttons = {i+1: button for i, button in enumerate(buttons)}

#     def press_button(self, position):
#         button = self.buttons.get(position)
#         if button:
#             button.press()

# button1 = Button("A")
# button2 = Button("B")
# button3 = Button("C")
# button4 = Button("0")
# button5 = Button("1")

# keyboard = Keyboard(button1, button2, button3, button4, button5)

# keyboard.press_button(1)  
# keyboard.press_button(2)  
# keyboard.press_button(3)  
# keyboard.press_button(4)  
# keyboard.press_button(5)  


# from abc import ABC, abstractmethod

# class Box(ABC):
#     def __init__(self):
#         self.items = []

#     @abstractmethod
#     def add(self, item):
#         pass

#     @abstractmethod
#     def empty(self):
#         pass

#     def count(self):
#         return len(self.items)

# class Item:
#     def __init__(self, name, value):
#         self.name = name
#         self.value = value

# class ListBox(Box):
#     def add(self, item):
#         self.items.append(item)

#     def empty(self):
#         items = self.items
#         self.items = []
#         return items

# class DictBox(Box):
#     def __init__(self):
#         super().__init__()
#         self.items = {}

#     def add(self, item):
#         self.items[item.name] = item

#     def empty(self):
#         items = [(name, value) for name, value in self.items.items()]
#         self.items = {}
#         return [Item(name, value) for name, value in items]



# box1 = ListBox()
# box2 = ListBox()
# box3 = DictBox()

# for i in range(20):
#     box1.add(Item(f"Item {i}", i))
# for i in range(9):
#     box2.add(Item(f"Item {i}", i))
# for i in range(5):
#     box3.add(Item(f"Item {i}", i))

# print(box1.count())
# print(box2.count())
# print(box3.count())

# def repack_boxes(*boxes):
#     items = []
#     for box in boxes:
#         items += box.empty()
#     num_items = len(items)
#     num_boxes = len(boxes)
#     items_per_box = num_items // num_boxes
#     remainder = num_items % num_boxes
#     box_index = 0
#     for i, item in enumerate(items):
#         if i % items_per_box == 0:
#             if remainder > 0:
#                 boxes[box_index].add(item)
#                 remainder -= 1
#             box_index = (box_index + 1) % num_boxes
#         boxes[box_index].add(item)
#     return boxes

# boxes = repack_boxes(box1, box2, box3)

# for box in boxes:
#     print(box.count())

# import abc

# class Box(abc.ABC):
#     def __init__(self):
#         self.items = []

#     @abc.abstractmethod
#     def add(self, *items):
#         pass

#     @abc.abstractmethod
#     def empty(self):
#         pass

#     def count(self):
#         return len(self.items)


# class Item:
#     def __init__(self, name, value):
#         self.name = name
#         self.value = value


# class ListBox(Box):
#     def add(self, *items):
#         for item in items:
#             self.items.append(item)

#     def empty(self):
#         items = self.items
#         self.items = []
#         return items


# class DictBox(Box):
#     def __init__(self):
#         self.items = {}

#     def add(self, *items):
#         for item in items:
#             self.items[item.name] = item

#     def empty(self):
#         items = list(self.items.values())
#         self.items = {}
#         return items


# def repack_boxes(*boxes):
#     all_items = []
#     for box in boxes:
#         all_items.extend(box.empty())

#     while all_items:
#         for box in boxes:
#             try:
#                 box.add(all_items.pop())
#             except IndexError:
#                 break


# box1 = ListBox()
# for i in range(20):
#     box1.add(Item(f'item{i}', i))

# box2 = ListBox()
# for i in range(9):
#     box2.add(Item(f'item{i+20}', i+20))

# box3 = DictBox()
# for i in range(5):
#     box3.add(Item(f'item{i+29}', i+29))

# repack_boxes(box1, box2, box3)

# print(box1.count())  
# print(box2.count())  
# print(box3.count())  

