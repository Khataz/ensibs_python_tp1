import sys
import re

originalList = [17, 38, 10, 25, 72]

def function1(list):
    list.sort()
    return list

def function2(list):
    list.append(12)
    return list

def function3(list):
    list.reverse()
    return list

def function4(list):
    return list.index(17)

def function5(list):
    list.remove(38)
    return list

def function6(list):
    return list[1:3]

def function7(list):
    return list[:2]

def function8(list):
    return list[2:]

def function9(list):
    return list

def function10(list):
    return list[-1]

if __name__ == "__main__":
    print(function1(originalList.copy()))
    print(function2(originalList.copy()))
    print(function3(originalList.copy()))
    print(function4(originalList.copy()))
    print(function5(originalList.copy()))
    print(function6(originalList.copy()))
    print(function7(originalList.copy()))
    print(function8(originalList.copy()))
    print(function9(originalList.copy()))
    print(function10(originalList.copy()))
