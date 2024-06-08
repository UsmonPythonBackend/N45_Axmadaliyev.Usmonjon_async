import time
from datetime import datetime


def task_1():
    time.sleep(2)
    print("call 1")
    print("end task_1")

def task_2():
    time.sleep(2)
    print("call 2")
#    task_3()
    print("end task_2")

def task_3():
    time.sleep(2)
    print("call 3")
    print("end task_3")
#    task_6()


def task_4():
    time.sleep(2)
    print("call 4")
    print("end task_4")
#    task_5()


def task_5():
    time.sleep(3)
#    task_8()
    print("call 5")
    print("end task_5")

def task_6():
#    task_7()
    time.sleep(1)
    print("call 6")
    print("end task_6")


def task_7():
    time.sleep(2)
    print("call 7")
    print("end task_7")


def task_8():
    time.sleep(1)
    print("call 8")
    print("end task_8")


def task():
    print(datetime.now())
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
#    print(datetime.now())
    task_6()
    task_7()
    task_8()
    print(datetime.now())





if __name__ == "__main__":
    task()
