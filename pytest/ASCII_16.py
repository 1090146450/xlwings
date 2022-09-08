import glob

name = "C:/Users/Administrator/Desktop/DV/" + str(input("请输入LOG名称"))


def open_log():
    with open(name + ".zudslog", mode="r", encoding="utf-8") as t:
        while True:
            a = t.readline()
            if a:
                if "积极响应" in a:
                    b = ""
                    for i in range(0, len(a)):
                        if a[35 + i] != "[":
                            b = b + a[35 + i]
                        else:
                            break
                    c, i = "", 10
                    while True:
                        d = int(b[i] + b[i + 1], 16)
                        c = c + str(chr(d))
                        i = i + 3
                        if i + 1 >= len(b):
                            break

                    write_log(c + "\n")
            else:
                break


def write_log(txt):
    with open(name + ".txt", mode="a", encoding="utf-8") as t:
        t.write(txt)


def print_log():
    open_log()
    list_name = ["扩展诊断会话", "Boot软件版本号", "ECU名称", "ERP信息", "供应商ECU软件版本号", "系统供应商信息", "全部版本号",
                 "广汽ECU标定软件版本号", "广汽电子控制单元硬件版本号", "广汽电子控制单元软件版本号", "广汽总成零件号", "广汽零件号",
                 "应用程序版本号"]
    log_open = open(name + ".txt", mode="r", encoding="utf-8")
    read = log_open.readlines()
    for i in range(0, 13):
        print(list_name[i] + ":" + read[i], end="")


# 查询是否有该文件
if not glob.glob(name + ".zudslog"):
    print("输入文件不存在请重新运行")
else:
    print_log()
