from BasePage import BasePage

bp = BasePage()
bp.add_sheets([1, 2, 3])
sht = bp.book.sheets[1]
bp.cell_wide(sht, "A2", 12)
bp.cell_Center(sht)
bp.add_cell(sht, "A2", [[1, 2], [3, 4], [5, 6]])
print(sht)
bp.quit()
