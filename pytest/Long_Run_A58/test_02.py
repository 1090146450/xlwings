import re
from Vlaue_book import Value_book

Cup_A, Fps_A,Sqi,MEMOPY = [], [[], [], [], []],[],[]


def Input():
    with open("../../teraterm.log", mode="r", encoding="UTF-8") as op:
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
                Cup_00=Value_book.Cpu_00(i,one_a)
                Fps_00=Value_book.Fps(i, one_a)
                Sqi_00=Value_book.Sqi(i,one_a)
                MEMOPY_00=Value_book.SyS_MEMOPY(i,one_a)
                if Cup_00:
                    Cup_A.append(Cup_00)
                # 这是第二个
                if  Fps_00!= [[], [], [], []]:
                    for x in range(0, 4):
                        if Fps_00[x]:
                            Fps_A[x].append(Fps_00[x])
            #     这是第三个
                if Sqi_00:
                    Sqi.append(Sqi_00)
            # 这是第四个
                if MEMOPY_00:
                    MEMOPY.append(MEMOPY_00)

            # Sqi_value = re.findall(r"sqi_value.(\d+\.\d+).", a)
            # if Sqi_value:
            #     Sqi[1] += Sqi_value
            #     Sqi[0] += re.findall(r"....-..-.. (\d\d:\d\d:\d\d)\.", a)
            if a == "":
                break
Input()
print(Fps_A)
