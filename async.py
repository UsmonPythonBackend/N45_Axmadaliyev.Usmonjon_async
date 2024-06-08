import asyncio
from datetime import datetime

async def task1():
    await asyncio.sleep(1)
    print("Task 1 completed")
#    await task7()

async def task2():
#    await task5()
    await asyncio.sleep(3)
    print("Task 2 completed")


async def task3():
    await asyncio.sleep(5)
    print("Task 3 completed")

async def task4():
    await asyncio.sleep(11)
    print("Task 4 completed")
#    await task2()

async def task5():
    await asyncio.sleep(3)
    print("Task 5 completed")

async def task6():
    await asyncio.sleep(6)
    print("Task 6 completed")


async def task7():
    await asyncio.sleep(7)
    print("Task 7 completed")


async def task8():
    await asyncio.sleep(5)
    print("Task 8 completed")
#    await task1()

async def main():
#    await asyncio.gather(task1(), task2())
#    print("finished 1")
#    await asyncio.gather(task3(), task4())
#    print("finished 2")
#    await asyncio.gather(task5(), task6(), task7(), task8())
#    print("finished 3")
    await asyncio.gather(task1(), task2(), task3(), task4(), task5(), task6(), task7(), task8())

if __name__ == "__main__":
    print(datetime.now())
    asyncio.run(main())
    print(datetime.now())


#Xulosa : Sinxron dasturlashda biz quvvat kam sarflaymiz lekin vaqtda yutqazamiz, amallar berilgan ketma-ketlikda bajariladi. Sinxron dasturlashda misollar : telefonda qo'ng'iroq qilish, messenjerlarda xat yozish.
#Asinxron dasturlashda biz vaqtni kam sarflaymiz lekin quvvat ko'p talab qiladi, amallar barchasi bir vaqtni o'zida boshlanadi.Asinxron dasturlashda misollar : elektron pochta, hujjatlar bilan almashadigan onlayn platforma.