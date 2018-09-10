# JSON	Python
# object	dict
# array	list
# string	str
# number (int / real)	int / float
# true / false	True / False
# null	None


# Python	JSON
# dict	object
# list, tuple	array
# str	string
# int, float, int- & float-derived Enums	number
# True / False	true / false
# None	null

# json模块主要有四个比较重要的函数，分别是：

# dump - 将Python对象按照JSON格式序列化到文件中
# dumps - 将Python对象处理成JSON格式的字符串
# load - 将文件中的JSON数据反序列化成对象
# loads - 将字符串的内容反序列化成Python对象

# import os

# print '***获取当前目录***'
# print os.getcwd()
# print os.path.abspath(os.path.dirname(__file__))

# print '***获取上级目录***'
# print os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# print os.path.abspath(os.path.dirname(os.getcwd()))
# print os.path.abspath(os.path.join(os.getcwd(), ".."))

# print '***获取上上级目录***'
# print os.path.abspath(os.path.join(os.getcwd(), "../.."))

import json
import os

def main():
    # 当前目录
    pwd = os.path.abspath(os.path.dirname(__file__))
    print(pwd)
    mydict = {
        'name': '李剑飞',
        'age': 28,
        'qq': 10010,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        path = pwd+'\data.json' 
        print(path)
        with open(path, 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)

    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()