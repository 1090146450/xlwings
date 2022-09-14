from BasePage import BasePage
import test_02

# 创建表1
bp = BasePage()
bp.add_sheets(["03_SYS_MEMOPY", "02_SQI", "01_FPS", "00_CPU"])
bt = bp.book.sheets
# 在表中填写数据
CPU_A1 = [["", "TOTAL", "Cpu0", "Cpu1", "Cpu2"],
          ["MIN", "=MIN(B5:B999999)", "=MIN(C5:C999999)", "=MIN(E5:E999999)", "=MIN(E5:E999999)"],
          ["MAN", "=MAX(B5:B999999)", "=MAX(C5:C999999)", "=MAX(D5:D999999)", "=MAX(E5:E999999)"],
          [" ", "TOTAL", "Cpu0", "Cpu1", "Cpu2"]]
bp.add_cell(bt[0], "A1", CPU_A1)
# 修改表数据居中
bp.cell_Center(bt[0])
# 修改表格列宽
bp.cell_wide(bt[0], "A1", 32)
# 修改表格外边框
bp.cell_Line(bt[0], "A1:E4")
# x修改表底色
bp.cell_colo(bt[0], "A4:E4", (252, 228, 214))
bp.cell_colo(bt[0], "A1:E3")
# 添加数据
bp.add_cell(bt[0],"A5",test_02.Cup_A,transpose=True)

# 表2
name = ["A1:B5", "I1:J5"]
dms0 = ["A1:B1", "I1:J1", "A1", "I1"]
FPS_1 = [[["dms0", "", "MIN", "MAX", ">25"],
          [" ", "FPS", "=MIN(B6:B999999)", "=MAX(B6:B999999)", "=COUNTIF(B6:B999999,\">25\")"]],
         [["oms1", "", "MIN", "MAX", ">25"],
          [" ", "FPS", "=MIN(J6:J999999)", "=MAX(J6:J999999)", "=COUNTIF(J6:J999999,\">25\")"]]]
# 单元格居中
bp.cell_Center(bt[1])
for i in range(0, 2):
    # 修改单元格宽度
    bp.cell_wide(bt[1], dms0[i + 2], 26)
    # 填入数据
    if i == 0:
        bp.add_cell(bt[1], name[i], FPS_1[0], transpose=True)
    else:
        bp.add_cell(bt[1], name[i], FPS_1[1], transpose=True)
    # 修改颜色
    bp.cell_colo(bt[1], name[i])
    # 合并单元格
    bp.cell_merge(bt[1], dms0[i])
    # 设置边框
    bp.cell_Line(bt[1], name[i])

# 表3
sqi_date = [["", "sqi_value", "sqi_level"],
            ["MIN", "=MIN(B4:B1000000)", "=MIN(C4:C1000000)"],
            ["MAX", "=MAX(B4:B1000001)", "=MAX(C4:C1000001)"]]
sqi = "A1:C3"
# 设置单元格宽度
bp.cell_wide(bt[2], "A1", 32)
# 添加数据
bp.add_cell(bt[2], sqi, sqi_date)
# 修改颜色
bp.cell_colo(bt[2], sqi)
# 设置边框
bp.cell_Line(bt[2], sqi)
# 单元格居中
bp.cell_Center(bt[2])

# 表4
SYS_date = [["", "Total", "Free", "Avai", "Cach"],
            ["MIN", "=MIN(B4:B1000000)", "=MIN(C4:B1000000)", "=MIN(D4:B1000000)", "=MIN(E4:B1000000)"],
            ["MAX", "=MAX(B4:B1000001)", "=MAX(C4:B1000001)", "=MAX(D4:B1000001)", "=MAX(E4:B1000001)"]]
SYS = "A1:E3"
# 设置单元格宽度
bp.cell_wide(bt[3], "A1", 25)
bp.cell_wide(bt[3], "B1:E1", 14)
# 添加数据
bp.add_cell(bt[3], SYS, SYS_date)
# 修改颜色
bp.cell_colo(bt[3], SYS)
# 设置边框
bp.cell_Line(bt[3], SYS)
# 单元格居中
bp.cell_Center(bt[3])
# 退出
bp.quit()
