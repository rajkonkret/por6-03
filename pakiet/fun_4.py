def fun1():
    print("To jest fun1")

    def fun_2():
        print("To jest funkcja fun_2")

    return fun_2


print(fun1())
wiaderko = fun1()  # xFun1 = fun_2()
print(type(wiaderko))
wiaderko()   # fun2()
