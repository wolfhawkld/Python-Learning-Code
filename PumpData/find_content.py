# -*- encoding=utf-8 -*-
import pump_to_excel

# Global Params Start.
FILE_SUFFIX_LIST = ['.cs']
# PUMP_RE = '.*?PostAPI.*?webApi.*?' #SFDC_API_Post
PUMP_RE = '"/SFDC.*?"' # SFDC_API
# PUMP_RE = '.*?GetAPI.*?webApi.*?' #SFDC_API_Get
ROOT_PATH = 'C:\\Users\\da.long\\source\\Workspaces\\OCE Wechat Demo'
EXCEL_FILE_NAME = u'SFDC_API.xls'
EXCEL_COLUMNS = ['api_name', 'file_name', 'line']
EXCEL_SHEET_NAME = 'SFDC_API'
# Global Params End.


def main():
    file_list = pump_to_excel.get_all_files(ROOT_PATH, FILE_SUFFIX_LIST)
    sheet = pump_to_excel.create_excel_sheet(EXCEL_SHEET_NAME, EXCEL_COLUMNS)
    for file in file_list:
        ret_list = pump_to_excel.pump_file(file, PUMP_RE)
        if ret_list is not None:
            pump_to_excel.append_excel_data(ret_list, EXCEL_COLUMNS, sheet)
    pump_to_excel.save_excel_file(EXCEL_FILE_NAME)


if __name__ == '__main__':
    main()
