from BasePage import BasePage
import test_02

test_02.Input()
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
bp.cell_Center(bt[0],name=("A1:E"+str(len(test_02.Cup_A)+6)))
# 修改表格列宽
bp.cell_wide(bt[0], "A1", 32)
# 修改表格外边框
bp.cell_Line(bt[0], "A1:E4")
# x修改表底色
bp.cell_colo(bt[0], "A4:E4", (252, 228, 214))
bp.cell_colo(bt[0], "A1:E3")
# 添加数据
bp.add_cell(bt[0], "A5", test_02.Cup_A)


# 表2
name = ["A1:H5"]
dms0 = ["A1:B1", "C1:D1", "E1:F1", "G1:H1", "A1", "I1"]
FPS_1 = [[["dms0", "", "MIN", "MAX", ">25"],
          [" ", "FPS", "=MIN(B6:B999999)", "=MAX(B6:B999999)", "=COUNTIF(B6:B999999,\">25\")"]],
         [["oms1", "", "MIN", "MAX", ">25"],
          [" ", "FPS", "=MIN(D6:D999999)", "=MAX(D6:D999999)", "=COUNTIF(D6:D999999,\">25\")"]],
         [["oms2", "", "MIN", "MAX", ">25"],
          [" ", "FPS", "=MIN(F6:F999999)", "=MAX(F6:F999999)", "=COUNTIF(F6:F999999,\">25\")"]],
         [["oms3", "", "MIN", "MAX", ">25"],
          [" ", "FPS", "=MIN(H6:H999999)", "=MAX(H6:H999999)", "=COUNTIF(H6:H999999,\">25\")"]]
         ]
# 单元格居中
bp.cell_Center(bt[1],name=("A1:H"+str(len(test_02.Fps_A[0])+6)))
for i in range(0, 4):
    # 修改单元格宽度
    bp.cell_wide(bt[1], dms0[i], 15)
    # 填入数据
    bp.add_cell(bt[1], dms0[i], FPS_1[i], transpose=True)
    # 修改颜色
    bp.cell_colo(bt[1], name[0])
    # 合并单元格
    bp.cell_merge(bt[1], dms0[i])
    # 设置边框
    bp.cell_Line(bt[1], name[0])
bp.add_cell(bt[1], "A6", test_02.Fps_A[0])
bp.add_cell(bt[1], "C6", test_02.Fps_A[1])
bp.add_cell(bt[1], "E6", test_02.Fps_A[2])
bp.add_cell(bt[1], "G6", test_02.Fps_A[3])

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
bp.cell_Center(bt[2],name="A1:C"+str(len(test_02.Sqi)+6))
# 填写数据
bp.add_cell(bt[2],"A4", test_02.Sqi)

# 表4
SYS_date = [["", "Total", "Free", "Avai", "Cach"],
            ["MIN", "=MIN(B4:B1000000)", "=MIN(C4:C1000000)", "=MIN(D4:D1000000)", "=MIN(E4:E1000000)"],
            ["MAX", "=MAX(B4:B1000001)", "=MAX(C4:C1000001)", "=MAX(D4:D1000001)", "=MAX(E4:E1000001)"]]
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
bp.cell_Center(bt[3],name="A1:E"+str(len(test_02.MEMOPY)+6))
# 添加数据
bp.add_cell(bt[3],"A4", test_02.MEMOPY)
# 退出
bp.quit()
