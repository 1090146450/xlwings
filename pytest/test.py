with open("../teraterm.log", mode="r", encoding="UTF-8") as op:
    while True:
        a = op.readline()
        if "CPU OCCUPY" in a:
            print(a[11:20])
            if "Total" in a[73:83]:
                print(a[73:83])
            if "Cpu0" in a[84:93]:
                print(a[84:93])
            if "Cpu1" in a[94:103]:
                print(a[94:103])
            if "Cpu2" in a[104:113]:
                print(a[104:113])
        if a == "":
            break
