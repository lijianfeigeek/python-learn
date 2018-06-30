"""

Python的内置函数
	- 数学相关: abs / divmod / pow / round / min / max / sum
	- 序列相关: len / range / next / filter / map / sorted / slice / reversed
	- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
	- 数据结构: dict / list / set / tuple
	- 其他函数: all / any / id / input / open / print / type
"""

# abs() 函数返回数字的绝对值。
print("abs(-45) : ", abs(-45))

#  divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
print(divmod(7, 2))

# pow() 方法返回 xy（x的y次方） 的值。
print(pow(2,2))

# round() 方法返回浮点数x的四舍五入值。
print(round(80.23456, 2))
print(round(80.23456, 3))

# min() 方法返回给定参数的最小值，参数可以为序列。
print(min(80, 100, 1000))

# max() 方法返回给定参数的最大值，参数可以为序列。
print(max(80, 100, 1000))

# sum() 方法对系列进行求和计算。
print(sum([0,1,2]))
print(sum((2,3,4,),1))
print(sum([1,2,3,4],2))

# len() 方法返回对象（字符、列表、元组等）长度或项目个数。
print(len('lijianfei'))
print(len([1,2]))

# range() 函数可创建一个整数列表，一般用在 for 循环中。
# Python3.x 中 range() 函数返回的结果是一个整数序列的对象，而不是列表。

print(range(10))
print(range(1,11))
print(list(range(10)))
print(type(range(10)))
# print(help(range))

# next() 返回迭代器的下一个项目。
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break


# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# python2中返回的是过滤后的列表, 而python3中返回到是一个filter类
# filter类实现了__iter__和__next__方法, 可以看成是一个迭代器, 有惰性运算的特性, 相对python2提升了性能, 可以节约内存.
def is_odd(n):
    return n % 2 == 1
 
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(newlist))

# map() 会根据提供的函数对指定序列做映射。

def square(x):
  return x**2

print(list(map(square,range(1,6))))
print(list(map(lambda x: x ** 2, range(1,6))))# 使用 lambda 匿名函数
print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))# 提供了两个列表，对相同位置的列表数据进行相加

# sorted() 函数对所有可迭代的对象进行排序操作。
"""
sort 与 sorted 区别：

sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
"""
a = [5,7,6,3,4,1,2]
b = sorted(a)       # 保留原列表
print(a)
print(b)
print(sorted(a,reverse=True))

L=[('b',2),('a',1),('c',3),('d',4)]
# sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))   # 利用cmp函数
print(sorted(L, key=lambda x:x[1]))             # 利用key


# slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。

"""
class slice(stop)
class slice(start, stop[, step])
"""

myslice = slice(5)    # 设置截取5个元素的切片
print(myslice)

print(list(range(10)[myslice]))

# slice实现分片和列表的拷贝
alist = ['123', 'abc', 'good', 'hello', 'nice']  #定义一个列表
alist1 = alist[:]     #[:]分号左边表示从第0未开始，分号右边表示最后一位结束。
print(alist1)

# reversed()函数是返回序列seq的反向访问的迭代子。参数可以是列表，元组，字符串，不改变原对象。
l=[1,2,3,4,5]
print(list(reversed(l)))

str0 = '李剑飞飞剑李'
str1 = reversed(str0)

print(str(str1))
print(id(str0))
print(id(str1))
# if str==str1:
#   print('是回文')
# else:
#   print('不是回文')


# id() 函数用于获取对象的内存地址。

# str() 函数将对象转化为适于人阅读的形式。
dict_1 = {'runoob': 'runoob.com', 'google': 'google.com'}
print(str(dict_1))

# chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
print(chr(0x61))

# ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数

print(ord('a'))

# bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。

print(bool(1))
print(issubclass(bool,int))

# int() 函数用于将一个字符串或数字转换为整型。
print(int(3.6))

# float() 函数用于将整数和字符串转换成浮点数。
print(float(1))

# complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。。

# bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
print(bin(2))

# oct() 函数将一个整数转换成8进制字符串。
print(oct(10))

# hex() 函数用于将10进制整数转换成16进制，以字符串形式表示。
print(hex(255))

# all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。

# 元素除了是 0、空、FALSE 外都算 TRUE。

print(all(['a', 'b', 'c', 'd']))  # 列表list，元素都不为空或0)

print(all([0, 1,2, 3]))

# dict() 函数用于创建一个字典。
print(dict(a='a', b='b', t='t') )

# list() 方法用于将元组转换为列表。

# 注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。

aTuple = (123, 'xyz', 'zara', 'abc')
print(list(aTuple))


#  tuple() 函数将列表转换为元组。
print(tuple([1,2,3,4]))
print(tuple({1:2,3:4}) ) #针对字典 会返回字典的key组成的tuple


# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。

x = set('runoob')
y = set('google')

print(x)
print(y)
print(x&y) # 交集
print(x|y) # 并集
print(x-y) # 差集


# any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，


# open() 函数用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写。

# type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。

"""
isinstance() 与 type() 区别：

type() 不会认为子类是一种父类类型，不考虑继承关系。

isinstance() 会认为子类是一种父类类型，考虑继承关系。

如果要判断两个类型是否相同推荐使用 isinstance()。
"""

