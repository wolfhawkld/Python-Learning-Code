# -*- encoding=utf-8 -*-

import re
import os
import codecs
import xlwt

# Global Params Start.
RESULT = xlwt.Workbook(encoding='utf-8', style_compression=0)
row_num = 1
# Global Params End.


# Create excel sheet head on demand.
def create_excel_sheet(sheet_name, columns):
    sheet = RESULT.add_sheet(sheet_name, cell_overwrite_ok=True)
    i = 0
    for item in columns:
        sheet.write(0, i, item)
        i += 1
    return sheet


# Get a specified suffix file list from ROOT_PATH.
def get_all_files(root_path, file_suffix):
    name_list = []
    for root, dirs, files in os.walk(root_path):  # 遍历所有目录，包括自身
        for file in files:  # 遍历文件，抓取指定文件
            pre, suf = os.path.splitext(file)
            for item in file_suffix:
                if suf == item:
                    name_list.append(os.path.join(root, file))
    print(name_list.__len__())
    return name_list

def get_col_name(line,):
    return 

# Get a table list from sql script file.
def get_all_tables(in_file, pump_re):
    name_list = []
    col_list = []
    table_cols_list = []
    ret_cols_list = []
    file_obj = codecs.open(in_file, 'r', 'utf-8')
    
    # for i, line in enumerate(file_obj):
    #     lineno = i + 1
    #     if line.find(pump_re) != -1:    # 判断是否是表名所在行，是则取出表名
    #         tn = find_table_name(line)
    #         name_list.append(tn)
    #                                     # 动态获取该表所有列名
    #         next_line = file_obj.seek(lineno)
    #         if next_line.find('PRIMARY') == -1:
    #             col_list.append(get_col_name(next_line))
    #         else:
    #             break


    i = 1
    while True:
        line = file_obj.readline()  # 只读取一行内容
        if not line:    # 判断是否读取到内容
            break
        line_str = line.strip()
        if line_str.find(pump_re) != -1:
            tn = find_table_name(line_str)
            name_list.append(tn)
        if line_str.startswith('['):
            col_str = re.findall(r'\[.*?\]', line_str)[0]
            col_list.append(col_str.strip('[').strip(']'))
        if line_str.startswith(')'):
            table_cols_list.append(col_list)
            col_list = []
        i += 1
    for i in table_cols_list:
        if len(i) == 0:
            continue
        else:
            ret_cols_list.append(i)
    print(ret_cols_list)
    # table_cols_list = [i for i in table_cols_list if i != '[break]']
    # print(table_cols_list)

    return name_list, ret_cols_list


# Get table name.
def find_table_name(line):
    tableObj = re.findall(r'\[.*?\]', line)[1]
    ret = tableObj.strip('[').strip(']')
    #print(ret)
    return ret


# Reguar Expression match.
def find_re(line, line_num, file_name, pump_re):
    line_list = []

    pattern = re.compile(pump_re, re.S)
    api_list = re.findall(pattern, line)
    for item in api_list:
        if item is not None:
            line_list.append({
                'api_name': item[2:].split('"')[0],
                'file_name': file_name,
                'line': line_num
            })
    if line_list.__len__() > 0:
        # print(line_list)
        return line_list
    else:
        return


# Read a file, find if there is matched pattern in file, and return the result.
def pump_file(file, pump_re):
    ret_list = []

    file_obj = codecs.open(file, 'r', 'utf-8')
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
    return ret_list


def pump_dir(file_list):
    ret_list = []
    for item in file_list:
        ret_list.append({'file_name': item})
    return ret_list


# Save the result into excel.
def append_excel_data(ret_list, columns, sheet):
    global row_num
    col_num = 0

    for item in ret_list:
        for col in columns:
            sheet.write(row_num, col_num, item[col])
            col_num += 1
        col_num = 0
        row_num += 1


def save_excel_file(file_name):
    RESULT.save(file_name)

'''
def test():
    pump_file('C:\\Users\\da.long\\source\\Workspaces\\MFP_Merck\\test.cs')


def main():
    file_list = get_all_files(ROOT_PATH)
    # test()

    # All sheet heads:
    sheet = create_excel_sheet(EXCEL_SHEET_NAME, EXCEL_COLUMNS)
    for file in file_list:
        ret_list = pump_file(file)
        if ret_list is not None:
            print(ret_list)
            save_to_excel(ret_list, EXCEL_COLUMNS, sheet)
    return


if __name__ == '__main__':
    main()

RESULT.save(EXCEL_FILE_NAME)
'''

