import re
from Vlaue_book import Value_book

Cup_A, Fps_A = [], [[], [], [], []]
Sqi = [[], []]


def Input():
    with open("../teraterm.log", mode="r", encoding="UTF-8") as op:
        while True:
            # 每一行提取出来的数据
            a = op.readline()
            # 判断一行内是否为一条数据防止一行多条数据却取一条的值
            # 根据时间来进行拆分  时间的通配符为：".(\d\d\d\d-\d\d-\d\d.\d\d:\d\d:\d\d)"
            a_time = ".(\d\d\d\d-\d\d-\d\d.\d\d:\d\d:\d\d)"
            # 进行拆分成列表
            one_a = re.split(a_time, a)
            # 放入循环中，如果有几条数据则循环几次从而解决一行多条数据却提取一次值
            for i in range(int((len(one_a) - 1) / 2)):
                # 然后开始判断列表中是否含有想要取出的值
                # 这是第一个表格
                if Value_book.Cpu_00(i, one_a):
                    Cup_A.append(Value_book.Cpu_00(i, one_a))
                # 这是第二个
                if Value_book.Fps(i, one_a) != [[], [], [], []]:
                    for x in range(0, 4):
                        if Value_book.Fps(i, one_a)[x]:
                            Fps_A[x].append(Value_book.Fps(i, one_a)[x])


            # Sqi_value = re.findall(r"sqi_value.(\d+\.\d+).", a)
            # if Sqi_value:
            #     Sqi[1] += Sqi_value
            #     Sqi[0] += re.findall(r"....-..-.. (\d\d:\d\d:\d\d)\.", a)
            if a == "":
                break


Input()
print(Cup_A)
