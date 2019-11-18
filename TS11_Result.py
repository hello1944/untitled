# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os
import csv
file_path = ' '  # 读取路径
np.set_printoptions(suppress=True)
for root, dirs, files in os.walk(file_path):
    for file in files:
        if file.endswith('_Result.txt'):  # 筛选result文件
            file_list_result=os.path.join(root,file)
            result_data = []  # 最终文件内容
            result_name = os.path.basename(file_list_result)[2:21]  # 读取编码
            result_time = os.path.basename(file_list_result)[22:36]  # 读取日期
            file_content = pd.read_csv(file_list_result, sep='\t', encoding='ANSI', header=0)  # 读取文件
            file_data1 = file_content['Judge']  # 读取判定项
            file_data1_1 = file_data1.dropna(axis=0, how='all', inplace=False)  # 删除读取判定项空值
            result_content1 = file_data1_1.values.tolist()  # 转化为数组
            f = open(file_list_result, 'r')     # 读取subrom判定
            result_subrom = f.readlines()
            for result_subrom in result_subrom:
                if "SubROM" in result_subrom:
                    result_subrom1 = result_subrom.strip()  # 删除读取判定项空值
                    result_data.append(result_name)   # 合并
                    result_data.append(result_time)   # 合并
                    result_data += result_content1   # 合并
                    result_data.append(result_subrom1)   # 合并
            with open('Result_Judge.csv', 'a+', newline='') as csvfile:   #输出
                writer = csv.writer(csvfile)
                writer.writerow(result_data)
