class Test():
    name = 'test1'  # 类属性

    def __init__(self):
        self.name = 'test2'  # 实例属性
        name = 'test3'  # name只是局部变量，函数调用完后会被销毁,只能在init函数内部访问
        print(self.name)


if __name__ == '__main__':
    t = Test()
    print(t.name)  # output：test2 ，由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
    print(Test.name)  # output：test1，类属性也可以通过类名.类属性访问
