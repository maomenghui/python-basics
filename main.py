# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
import os
import time
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # 整除运算符 // 返回一个整数，取值是值最小的那个（5 除 2 = 2.5 取最小整数 2 ）负数就不好用了，取 - 3 也是取最小整数
    # print(-5 // 2)
    # 乘方（幂运算） **
    # print(2 ** 3)
    # 模运算 取余 %
    # print(5 % 3)

    # Python 常用函数
    # print(random())
    # print(math.sin(2))

    # 元组
    array = ('abcd', 786, 2.23, 'john', 70.2)
    arr = (99, 'ccc')
    # 当前下边和后面所有下标数据
    # print(array[2:])
    # print(array, arr)

    # 元字典
    # tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
    # 获取所有 key
    # print(tinydict.keys())
    # 获取所有 value
    # print(tinydict.values())
    # key 获取 value
    # print(tinydict.get('name'))

    # 数组
    fruits = ['apple', 'ba', 'tom']
    # 循环遍历
    # for fruit in fruits:
    #     print("当前字母：", fruit)

    # 循环使用 else 语句
    # for num in range(1, 10):
    #     for i in range(2, num):
    #         if num % i == 0:
    #             j = num / i
    #             print('%d 等于 %d * %d' % (num, i, j))
    #             break
    #         else:
    #             print(num, '这是一个质数')
    # 输入函数，接收的是字符串，计算需要转换
    # x = input('1输入的是')
    # y = input('2输入的是')
    # print("输入的是：", float(x) * float(y))

    # 输入计算 条件输出声音
    ''' name = input('请输入名称：')
    weight = float(input('请输入体重：'))
    speed = float(input('请输入速度：'))
    armor = float(input('请输入铠甲值：'))
    power_level = weight * speed - armor
    print(name, '战力值', power_level)

    if power_level > 100:
        os.system('start C:/Users/56359/Desktop/hands.mp3')
    else:
        os.system('start C:/Users/56359/Desktop/bgm.mp3') '''

    # **********
    # if elif else 使用
    # **********
    ''' apple = float(input('请输入购买的苹果数量'))
    if apple > 10:
        print('我要购买超过', apple)
    elif 5 <= apple < 10:
        print('我要购买5 - 10 苹果')
    else:
        print('购买5以内') '''

    # **********
    # 随机生成 1 - 7 的整数，实现一个自动生成乐谱小程序
    # **********
    ''' i = 1
    while i <= 7:
        i = random.randint(1, 7)
        path = 'start D:/BaiduNetdiskDownload/听书/' + str(i) + '.mp3'
        os.system(path)
        time.sleep(1 / random.randint(1, 2)) '''

    # **********
    # 猜音阶 1 - 7 输出猜了多少次
    # **********
    ''' node = random.randint(1, 7)
    os.system('start D:/BaiduNetdiskDownload/听书/' + str(node) + '.mp3')
    guess = -1
    i = 1
    while guess != node:
        guess = int(input("请输入刚刚听到的音符数字 1 - 7"))
        if guess > node:
            print('猜的大了一点哦')
        elif guess < node:
            print('猜的小了一点哦')
        else:
            print('你真是个小天才猜对啦')
            break
        i = i + 1
    print('一共猜了', i) '''

    # **********
    # 解数学公式（穷举法）  X4 * 693 = 4X * 396
    # x可以直接拼接在4上但是不美观， X4 如果是 24 = x(2) * 10 + 4，公式 int(str(x)+str(4)) * 693 == int(str(4)+str(x)) * 396
    # **********
    x = 1
    while x < 10:
        a = x * 10 + 8
        b = 8 * 10 + x
        print(a, b, a * 693, b * 396)
        if a * 693 == b * 396:
            print('X 的值是：', x)
        x = x + 1

    # **********
    # 解数学公式（穷举法）  XY * 693 = YX * 396
    # **********
    '''y = 1
    while y < 10:
        x = 1
        while x < 10:
            a = x * 10 + y
            b = y * 10 + x
            if a * 693 == b * 396:
                print('当Y等于=', y, 'X的值是：', x, 'XY * 693=', a * 693, 'YX * 396=', b * 396)
            x = x + 1
        y = y + 1 '''


if __name__ == '__main__':
    print_hi('PyCharm')
