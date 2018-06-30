# list1 = [1, 3, 5, 7, 100]
# print(list1)
# list2 = ['hello'] * 5
# print(list2)
# # 计算列表长度(元素个数)
# print(len(list1))
# # 下标(索引)运算
# print(list1[0])
# print(list1[4])
# # print(list1[5])  # IndexError: list index out of range
# print(list1[-1])
# print(list1[-3])
# list1[2] = 300
# print(list1)
# # 添加元素
# list1.append(200)
# list1.insert(1, 400)
# list1 += [1000, 2000]
# print(list1)
# print(len(list1))
# # 删除元素
# list1.remove(3)
# if 1234 in list1:
#   list1.remove(1234)
# del list1[0]
# print(list1)
# # 清空列表元素
# list1.clear()
# print(list1)

print('###################################')
	

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 循环遍历列表元素
for fruit in fruits:
  print(fruit.title(), end=' ')

print()
# 列表切片
fruits2 = fruits[1:4]
print(fruits2)
# fruit3 = fruits  # 没有复制列表只创建了新的引用
  # 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3)
fruits4 = fruits[-3:-1]
print(fruits4)
  # 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5)


print('###################################')

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)

