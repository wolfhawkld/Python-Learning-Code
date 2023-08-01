'''遍历当前文件夹所有MOV文件
   根据其文件创建日期重新命名该文件
   实现文件名唯一（解决大疆无人机换卡后文件命名重复问题）'''

import os
import time
# 递归遍历当前文件夹内所有同类后缀文件
def scan_files(suffix):
    cwd = os.getcwd()
    os.chdir(cwd) #更改当前路径
    #print(cwd)
    for root, dirs, files in os.walk(cwd):  # 遍历所有目录，包括自身
        for file in files:  # 遍历文件，抓取指定文件
            #stamp_file(file)
            if file.endswith(suffix):
                #print(root + file)
                stamp_file(root, file)

    

# 根据文件创建日期重命名该文件
def stamp_file(file_path, file_name):
    ctime = get_file_date(file_path, file_name)
    cl_time = time.localtime(ctime)
    stamp = time.strftime("%Y%m%d%H%M%S", cl_time) 
    print(stamp)
    new_name = file_name[:4] + stamp + file_name[4:]
    print(new_name)
    os.rename(file_path + '\\' + file_name, file_path + '\\' + new_name)


# 获取文件创建日期
def get_file_date(file_path, file_name):
    return os.path.getctime(file_path + '\\' + file_name)


scan_files('MOV')
