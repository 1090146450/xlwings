import re

Cup_A, Cup_B, Cup_C, Cup_D, Cup_E = [], [], [], [], []
Fps_A, Fps_B, Fps_C, Fps_D = [[], []], [[], []], [[], []], [[], []]
Sqi = [[], []]


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
                Fps_A[0].append(a[12:20])
                Fps_A[1] = Fps_A[1] + (re.findall(r"dms0 RUNNING: (\s+\d+) fps", a))
            if "oms1 RUNNING" in a:
                Fps_B[0].append(a[12:20])
                Fps_B[1] = Fps_B[1] + (re.findall(r"oms1 RUNNING: (\s+\d+) fps", a))
            if "oms2 RUNNING" in a:
                Fps_C[0].append(a[12:20])
                Fps_C[1].append(a[78:80])
            if "oms3 RUNNING" in a:
                Fps_D[0].append(a[12:20])
                Fps_D[1].append(a[78:80])
            Sqi_value = re.findall(r"sqi_value.(\d+\.\d+).", a)
            if Sqi_value:
                Sqi[0] += Sqi_value
                 
            if "sqi_value" in a:
                Sqi[0].append(a[12:20])
            if a == "":
                break
