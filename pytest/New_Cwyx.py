import xlwings as xl


class open_xlsx:
    with xl.App(visible=False, add_book=False) as app:
        # 关闭提示信息加快运行速度
        app.display_alerts = False
        # 新建工作蒲
        book = app.books.add()
        SYS_MEMORY = book.sheets.add("03_SYS_MEMORY")
        SQI = book.sheets.add("02_SQI")
        FPS = book.sheets.add("01_FPS")
        CPU = book.sheets.add("00_CPU")
        CPU.range("A1").column_width = 32
        CPU.range("A1:ck3000").api.HorizontalAlignment = -4108
        B1 = ["TOTAL", "Cpu0", "Cpu1", "Cpu2"]
        CPU.range("B1").value = B1
        A2 = ["MIN", "=MIN(B5:B999999)", "=MIN(C5:C999999)", "=MIN(E5:E999999)", "=MIN(E5:E999999)"]
        CPU.range("A2").value = A2
        A3 = ["MAN", "=MAX(B5:B999999)", "=MAX(C5:C999999)", "=MAX(D5:D999999)", "=MAX(E5:E999999)"]
        CPU.range("A3").value = A3
        B4 = ["TOTAL", "Cpu0", "Cpu1", "Cpu2"]
        CPU.range("B4").value = B4
        ae13 = CPU.range("A1:E3")
        ae13.color = (226, 239, 218)
        for b_id in range(7, 13):
            ae13.api.Borders(b_id).LineStyle = 1
        # 表01FTP
        FPS.range("A1:B1").api.Merge()
        Fps_a5 = ["dms0", "", "MIN", "MAX", ">25"]
        FPS.range("A1:A5").options(transpose=True).value = Fps_a5
        Fps_a1 = FPS.range("A1")
        Fps_a1.column_width = 26
        FPS.range("A1:ck3000").api.HorizontalAlignment = -4108
        Fps_b2 = ["FPS", "=MIN(B6:B999999)", "=MAX(B6:B999999)", "=COUNTIF(B6:B999999,\">25\")"]
        FPS.range("B2:B5").options(transpose=True).value = Fps_b2
        Fps_a1b5 = FPS.range("A1:B5")
        Fps_a1b5.color = (226, 239, 218)
        for b_id in range(7, 13):
            Fps_a1b5.api.Borders(b_id).LineStyle = 1
        # 第二块
        FPS.range("I1:J1").api.Merge()
        Fps_i5 = ["oms1", "", "MIN", "MAX", ">25"]
        FPS.range("i1:i5").options(transpose=True).value = Fps_i5
        Fps_i1 = FPS.range("i1")
        Fps_i1.column_width = 26
        Fps_j2 = ["FPS", "=MIN(B6:B999999)", "=MAX(B6:B999999)", "=COUNTIF(B6:B999999,\">25\")"]
        FPS.range("j2:j5").options(transpose=True).value = Fps_j2
        Fps_i1j5 = FPS.range("i1:j5")
        Fps_i1j5.color = (226, 239, 218)
        for b_id in range(7, 13):
            Fps_i1j5.api.Borders(b_id).LineStyle = 1
        book.save("D:/迅雷下载/1.xlsx")
