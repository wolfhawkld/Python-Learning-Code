'''目前仅支持SQL Server脚本语法'''
import pump_to_excel

# Global Params Start.
SCRIPT_FILE = 'CDM_DEV_20210222.sql'
# PUMP_RE = '.*?PostAPI.*?webApi.*?' #SFDC_API_Post
PUMP_RE = 'CREATE TABLE'
# PUMP_RE = '.*?GetAPI.*?webApi.*?' #SFDC_API_Get
ROOT_PATH = 'C:\\Users\\M293906\\Documents\\Project\\HK_CDM'
EXCEL_FILE_NAME = u'CDM_ER_Schema.xls'

# Global Params End.


# 读取本地sql脚本中的table
def read_script(file):
    file_obj = codecs.open(file, 'r', 'utf-8')
    EXCEL_SHEET_LIST.append(cache_object())
    i = 1
    while True:
        line = file_obj.readline()  # 只读取一行内容
        if not line:    # 判断是否读取到内容
            break
        line_match_list = find_re(line, i, file, pump_re)
        i += 1
        if line_match_list is not None:
            ret_list.extend(line_match_list)
    # print(ret_list)
    file_obj.close()
    return 0


# 解析table各个column并缓存至对象
def cache_object():
    col_list = []
    return col_list


# 将对象缓存的表及其column输出为excel的sheet页及列
def save_excel():
    return 0


def main():
    table_list, table_cols_list = pump_to_excel.get_all_tables(ROOT_PATH + '\\'+ SCRIPT_FILE, PUMP_RE)
    print(len(table_list))
    print(len(table_cols_list))
    dict_1 = {}
    """ zip打包用法,同时遍历两个list """
    for tab, cols in zip(table_list, table_cols_list):
        dict_1[tab] = cols 
    for (key,value) in dict_1.items():
        #print(key+':'+value)
        pump_to_excel.create_excel_sheet(key, value)
               
                # pump_to_excel.append_excel_data(ret_list, cols, sheet)
    pump_to_excel.save_excel_file(EXCEL_FILE_NAME)
    # for file in file_list:
    #     ret_list = pump_to_excel.pump_file(file, PUMP_RE)
    #     if ret_list is not None:
    #         pump_to_excel.append_excel_data(ret_list, EXCEL_COLUMNS, sheet)
    # pump_to_excel.save_excel_file(EXCEL_FILE_NAME)


if __name__ == '__main__':
    main()