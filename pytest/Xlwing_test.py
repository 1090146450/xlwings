import xlwings as xl
import win32
# 创建Excel程序  visible程序是否可见运行 add_book是否创建文件博
with xl.App(visible=False, add_book=False) as app:
    #     创建新的工作蒲
    book = app.books.add()
    # 创建sheet表
    sheets1 = book.sheets.add(name="第一个表单123")
    # 表格内容居中
    sheets1.range('A1:ck3000').api.HorizontalAlignment = -4108
    #     向表插入数据  也可以插入表格[1,2,3]从A1-C1插入123 (在使用的时候需要将（）换成=等号) 如果是sheets1.range("A1").options(transpose=True)是将列表从
    # A1到A3上
    sheets1.range("A1").value = "=MIN(A2:A3)"
    aaa = sheets1.range("A2")
    # aaa.api.Broders(9).LineStyle = 1
    sht=book.api.Font.ColorIndex=3
    # 保存表
    book.save("C:/Users/Administrator/Desktop/DV/123.xlsx")
