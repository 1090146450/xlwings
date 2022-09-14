Cup_A, Cup_B, Cup_C, Cup_D, Cup_E = [], [], [], [], []
Fps_A, Fps_B, Fps_C, Fps_D= [], [], [], []

def Input():
    with open("../teraterm.log", mode="r", encoding="UTF-8") as op:
        while True:
            a = op.readline()
            if "CPU OCCUPY" in a:
                Cup_A.append(a[12:20])
                if "Total" in a[73:83]:
                    Cup_B.append(a[80:83])
                else:
                    Cup_B.append(" ")
                if "Cpu0" in a[84:93]:
                    Cup_C.append(a[90:93])
                else:
                    Cup_C.append(" ")
                if "Cpu1" in a[94:103]:
                    Cup_D.append(a[100:103])
                else:
                    Cup_D.append(" ")
                if "Cpu2" in a[104:113]:
                    Cup_E.append(a[110:113])
                else:
                    Cup_E.append(" ")
            if "dms0 RUNNING" in a:
                Fps_A.append(a[77:79])
            if "oms1 RUNNING" in a:
                Fps_B.append(a[77:79])
            if "oms2 RUNNING" in a:
                Fps_C.append(a[77:79])
            if "oms3 RUNNING" in a:
                Fps_D.append(a[77:79])
            if a == "":
                break


