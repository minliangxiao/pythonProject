import  unittest
from my_calculaor import  my_adder
'''
 主要学习unittest的用法 启动这个小案例在终端输入python -m unittest


'''

class TestMyAdder(unittest.TestCase):
    # 类后面跟参数 表示继承
    def test_positive_with_positive(self):
        # self可以取到父类立main的东西
        self.assertEqual(my_adder(5,3),8);
    def test_negative_with_positive(self):
        self.assertEqual(my_adder(5,3),7);
