Cup_A, Cup_B, Cup_C, Cup_D, Cup_E = [], [], [], [], []


def Input():
    with open("../teraterm.log", mode="r", encoding="UTF-8") as op:
        while True:
            a = op.readline()
            if "CPU OCCUPY" in a:
                Cup_A.append(a[12:20])
                if "Total" in a[73:83]:
                    Cup_B.append(a[80:83])
                if "Cpu0" in a[84:93]:
                    Cup_C.append(a[90:93])
                if "Cpu1" in a[94:103]:
                    Cup_D.append(a[100:103])
                if "Cpu2" in a[104:113]:
                    Cup_E.append(a[110:113])
            if a == "":
                break


Input()
print(Cup_B, Cup_C, Cup_D, Cup_E)
