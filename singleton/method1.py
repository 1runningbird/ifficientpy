# coding: utf8

'''
use method:
from method1 import singleton

这种方式存在着相当大的弊端:
    1.还是有人会把_Singleton import 进去, 创建多个实例
'''
class _Singleton(object):
    def get_name(self):
        pass

singleton = _Singleton()
