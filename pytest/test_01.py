Cup_A, Cup_B, Cup_C, Cup_D, Cup_E = [], [], [], [], []
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
for i in range(0, 10000):
    Cup_A.append(i)
    Cup_B.append(i)
    Cup_C.append(i)
    Cup_D.append(i)
    Cup_E.append(i)
print(len(Cup_A), len(Cup_E), len(Cup_B), len(Cup_C), len(Cup_D))
