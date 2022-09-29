import re
import xlwings

Cup_A, Cup_B, Cup_C, Cup_D, Cup_E = [], [], [], [], []

app = xlwings.App(visible=True, add_book=False)
book = app.books.add()
sheet = book.sheets.add()
sheet.range("A1").value = "你好"
sheet.name = "123"
book.save("./name1.xlsx")
book.close()
app.quit()
# with open("C:/Users/AN/Desktop/123.txt", mode="r", encoding="UTF-8") as op:
#     while True:
#         a = op.readline()
#         if "CPU OCCUPY" in a:
#             Cup_A.append(a[12:20])
#             if "Total" in a[73:83]:
#                 Cup_B.append(a[80:83])
#             if "Cpu0" in a[84:93]:
#                 Cup_C.append(a[90:93])
#             if "Cpu2" in a[101:114]:
#                 Cup_E.append(a[110:113])
#             if "Cpu1" in a[94:103]:
#                 Cup_D.append(a[100:103])
#
#         if a == "":
#             break
# def link():
#     filepath = "../teraterm.log"
#     txt = open(filepath, mode="r", encoding="UTF-8").read()
#     result = ""
#     Cpu = re.findall(r"oms1 RUNNING:(\s+\d+) fps", txt)
#     Sqi = re.findall(r"sqi_value.(\d+\.\d+).", txt)
#     Sqi_1=[]
#     if Sqi:
#         Sqi_1 += re.findall(r"....-..-.. (\d\d:\d\d\:\d\d)\.", txt)
#     result = result + "\n".join(Cpu)
#     fileResult = open("../sql.txt", mode="a", encoding="UTF-8")
#     fileResult.write(result)
#     print(len(Sqi),len(Sqi_1))
# Sqi, Sqi_1 = [], []
#
#
# def Test():
#     a = [[], [], [], []]
#     for i in range(0, 4):
#         for x in range(0, 10):
#             a[i].append(x)
#     return a


# b = "[Thu Sep 15 19:45:31.032 2022] [2022-06-09 00:00:06.255488][invo_alg_fid.h           ][WRN] FaceIdFeature[0]::load(/tmp/sense/faceid/faceid0.db) ..."
# MEMOPY_00 = []
# a_time = "(\d\d\d\d-\d\d-\d\d.\d\d:\d\d:\d\d)"
# print(re.split(a_time, b))
# if "SYS MEMORY" in b:
#     MEMOPY_02 = [["Total", "Free", "Avai", "Cach"],
#                  ["Total\[(\d+\.?\d+?)MB\]", "Free\[(\d+\.?\d+?)MB\]", "Avai\[(\d+\.?\d+?)MB\]", "Cach\[(\d+\.?\d+?)MB\]"]]
#     for x in range(0, 4):
#         if MEMOPY_02[0][x] in b:
#             MEMOPY_00 += re.findall(MEMOPY_02[1][x], b)
#         else:
#             MEMOPY_00.append("")
# print(MEMOPY_00)
# #
