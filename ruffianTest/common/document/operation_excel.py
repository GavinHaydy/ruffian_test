import xlrd


class OperationExcel:
    def __init__(self, path, sheet_name):
        self.workbook = xlrd.open_workbook(path)
        self.sheet = self.workbook.sheet_by_name(sheet_name)

    def get_value(self, row, col):
        sheet_value = self.sheet.cell_value(row-1, col-1)
        return sheet_value

    def get_values(self, start_row, end_row, start_col, end_col):
        results = []
        if start_row < end_row and start_col < end_col:
            for item in range(start_row-1, end_row):
                results.append(self.sheet.row_values(item, start_col-1, end_col))
        elif start_row < end_row and start_col == end_col:
            results.append(self.sheet.col_values(start_col-1, start_row-1, end_row))
        elif start_row == end_row and start_col < end_col:
            results.append(self.sheet.row_values(start_row-1, start_col-1, end_col))
        elif start_row == end_row and start_col == end_col:
            results = self.get_value(start_row, start_col)
        else:
            results = '参数错误'
        return results


if __name__ == '__main__':
    s = OperationExcel('/home/bugpz/文档/快快/测试用例快快V2.6.1.xlsx','快快V2.6.1').get_values(4,5,1,0)
    print(s)