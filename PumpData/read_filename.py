# -*- encoding=utf-8 -*-
import pump_to_excel

FILE_SUFFIX_LIST = ['.txt', '.xlsx', '.xls']
EXCEL_FILE_NAME = u'file_name.xls'
EXCEL_COLUMNS = ['file_name']
EXCEL_SHEET_NAME = 'Data_File'
ROOT_PATH = 'C:\\Users\\da.long\\Documents\\Projects\\Upjohn\\Sample Data'


def main():
    file_list = pump_to_excel.get_all_files(ROOT_PATH, FILE_SUFFIX_LIST)
    ret_list = pump_to_excel.pump_dir(file_list)
    sheet = pump_to_excel.create_excel_sheet(EXCEL_SHEET_NAME, EXCEL_COLUMNS)
    pump_to_excel.append_excel_data(ret_list, EXCEL_COLUMNS, sheet)
    pump_to_excel.save_excel_file(EXCEL_FILE_NAME)


if __name__ == '__main__':
    main()
