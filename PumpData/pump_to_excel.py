# -*- encoding=utf-8 -*-

import re
import os
import codecs
import xlwt

# Global Params Start.
FILE_SUFFIX = '.cs'
PUMP_RE = '/SFDC'
ROOT_PATH = 'C:\\Users\\da.long\\source\\Workspaces\\MFP_Merck'
RESULT = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = RESULT.add_sheet('SFDC_API_Worklist', cell_overwrite_ok=True)
sheet.write(0, 0, 'API')
sheet.write(0, 1, 'cs_file')
sheet.write(0, 2, 'line')
n = 1
# Global Params End.


# Get a specified suffix file list from ROOT_PATH.
def get_all_files(root_path):
    name_list = []
    for root, dirs, files in os.walk(root_path):  # 遍历所有目录，包括自身
        for file in files:  # 遍历文件，抓取指定文件
            pre, suf = os.path.splitext(file)
            if suf == FILE_SUFFIX:
                name_list.append(os.path.join(root, file))
    # print(name_list.__len__())
    return name_list


# Reguar Expression match.
def find_re(line, line_num, file_name):
    line_list = []

    pattern = re.compile('"/SFDC.*?"', re.S)
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
def pump_file(file):
    ret_list = []

    file_obj = codecs.open(file, 'r', 'utf-8')
    i = 1
    while True:
        line = file_obj.readline()  # 只读取一行内容
        if not line:    # 判断是否读取到内容
            break
        line_match_list = find_re(line, i, file)
        i += 1
        if line_match_list is not None:
            ret_list.extend(line_match_list)
    # print(ret_list)
    file_obj.close()

    return ret_list


# If a file's content matches PUMP_RE, then save the result into excel.
def save_to_excel(ret_list):
    for item in ret_list:
        api_name = item['api_name']
        file_name = item['file_name']
        line = item['line']

        global n
        sheet.write(n, 0, api_name)
        sheet.write(n, 1, file_name)
        sheet.write(n, 2, line)
        n = n + 1


def test():
    pump_file('C:\\Users\\da.long\\source\\Workspaces\\MFP_Merck\\test.cs')


def main():
    file_list = get_all_files(ROOT_PATH)
    # test()
    for file in file_list:
        ret_list = pump_file(file)
        if ret_list is not None:
            save_to_excel(ret_list)
    return


if __name__ == '__main__':
    main()

RESULT.save(u'SFDC_API_Worklist.xls')


