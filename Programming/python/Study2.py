# wow=[1,2,3,4,5]

# print([(x,x**3) for x in wow])

# print([(x,3*x) for x in wow if x<4])

# print([(x,3*x) for x in wow if x>2])

# wow1=[1,2,3,4,5]
# wow2=[5,4,3,2,1]
# print([x*y for x in wow1 for y in wow2])
# print([wow1[i]+wow2[i] for i in range(len(wow1))])
# print([wow1[i]*wow2[i] for i in range(len(wow1))])

# def cube(x,y,z) : return x*y*z
# num1=[1,2,3]
# num2=[4,5,6]
# num3=[7,8,9]
# ss=list(map(cube,num1,num2,num3 ))
# print(ss)

# import functools
# sum = functools.reduce(lambda a,x : a+x, [0,1,2,3,4])
# print(sum)

# u = [0,1,2,3,4]
# t=sum(u)
# print(t)


# import functools
# def sum(seq):
#     def add(x,y):
#         return x+y
#     return functools.reduce(add  ,seq , 5)

# print(sum(range(1,11)))
# print(sum([]))


# import numpy as np 
# x = np.random.rand(10,)
# y = list(map(lambda v : v * 5, filter(lambda u : u % 2 , x)))    
# print(y)

# tpl = (1,2,3,4,5,6,7,8,9,10)
# tpl1 = tuple(filter(lambda x : x%2==0,tpl))

# print (tpl1)


# def even (item):
#     if item % 2 == 0:
#         return item**2
    
# lst=[i for i in range (1,11)]
# print(list(filter(lambda x : x is not None, list(map(even, lst)))))


