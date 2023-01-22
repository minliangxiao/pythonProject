def printLearn(name):
    a = 1;
    print(name+str(a));
    b = input("input something");
    print(b)
    try:
        print(b)
    except:
        print()

class Test:
    def __init__(self):
        print(self)



if __name__ == '__main__':
    a = 1;
    printLearn('diaomao');
    locals();
    test = Test();
