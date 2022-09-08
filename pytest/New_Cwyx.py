import xlwings as xl


class open_xlsx:
    with xl.App(visible=False, add_book=False) as app:
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
        A2 = ["MIN", "=MIN(B5:B999999)", "=MIN(C5:C999999)", "=MIN(E5:E999999)"]
        CPU.range("A2").value = A2
        A3 = ["MIN", "=MIN(B5:B999999)", "=MIN(C5:C999999)", "=MIN(D5:D999999)", "=MIN(E5:E999999)"]
        CPU.range("A3").value = A3
        B4 = ["TOTAL", "Cpu0", "Cpu1", "Cpu2"]
        CPU.range("B4").value = B4
        ae13 = CPU.range("A1:E3")
        ae13.color = (226, 239, 218)
        ae13.api.Broders(9).LineStyle = 1
        # 表01

        book.save("C:/Users/Administrator/Desktop/DV/1.xlsx")
