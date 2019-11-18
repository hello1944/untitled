# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os
import csv
file_path = 'H://2#EOL Data//2019//11//15//'  # 读取路径
np.set_printoptions(suppress=True)
for root, dirs, files in os.walk(file_path):
    for file in files:
        if file.endswith('_Result.txt'):  # 筛选result文件
            file_list_result=os.path.join(root,file)
            result_data = []  # 最终文件内容
            file_content_2 = pd.read_csv(file_list_result, sep='\t', encoding='ANSI', header=0)  # 读取文件
            file_data1_2 = file_content_2['Result']  # 读取result数值
            file_data1_1_2 = file_data1_2.dropna(axis=0, how='all', inplace=False)  # 删除读取判定项空值
            result_content1_2 = file_data1_1_2.values.tolist()  # 转化为数组
            result_content2_2 = result_content1_2[6:12]+result_content1_2[17:25]+result_content1_2[30:33]+result_content1_2[38:40]+result_content1_2[45:51]
            result_name = os.path.basename(file_list_result)[2:21]  # 读取编码
            result_time = os.path.basename(file_list_result)[22:36]  # 读取日期
            file_content = pd.read_csv(file_list_result, sep='\t', encoding='ANSI', header=0)  # 读取文件
            file_data1 = file_content['Judge']  # 读取判定项
            file_data1_1 = file_data1.dropna(axis=0, how='all', inplace=False)  # 删除读取判定项空值
            result_content1 = file_data1_1.values.tolist()  # 转化为数组
            result_content2 = result_content1[6:14]+result_content1[19:31]+result_content1[36:40]+result_content1[45:48]+result_content1[53:61]
            f = open(file_list_result, 'r')     # 读取subrom判定
            result_subrom = f.readlines()
            for result_subrom in result_subrom:
                if "SubROM" in result_subrom:
                    result_subrom1 = result_subrom.strip()  # 删除读取subrom核对项空值
                    result_data.append(result_name)
                    result_data.append(result_time)
                    result_data += result_content2_2   # 合并
                    result_data += result_content2   # 合并
                    result_data.append(result_subrom1)   # 合并
            with open('Result_data.csv', 'a+', newline='') as csvfile:   #输出
                writer = csv.writer(csvfile)
                writer.writerow(result_data)
for root, dirs, files in os.walk(file_path):
    for file in files:
        if file.endswith('_SubROM1.txt'):  # 筛选SubROM1文件
            file_list_subrom1=os.path.join(root,file)
            subrom_data = []  # subrom1文件内容
            result_name = os.path.basename(file_list_subrom1)[2:21]  # 读取编码
            result_time = os.path.basename(file_list_subrom1)[22:36]  # 读取日期
            file_content_subrom = pd.read_csv(file_list_subrom1, sep='\t', encoding='ANSI', header=0)  # 读取文件
            file_data_subrom_ml1 = file_content_subrom['ML Pressure(+)'].values.tolist() [0:13] # 读取ML+，转化数组
            file_data_subrom_ml2 = file_content_subrom['ML Pressure(-)'].values.tolist() [0:13] # 读取ML-，转化数组
            file_data_subrom_ss1 = file_content_subrom['SS Pressure(+)'].values.tolist() [1:10] # 读取ss+，转化数组
            file_data_subrom_ss2 = file_content_subrom['SS Pressure(-)'].values.tolist() [1:10] # 读取ss-，转化数组
            file_data_subrom_ps1 = file_content_subrom['PS Pressure(+)'].values.tolist() [1:10] # 读取ps+，转化数组
            file_data_subrom_ps2 = file_content_subrom['PS Pressure(-)'].values.tolist() [1:10] # 读取ps-，转化数组
            file_data_subrom_dc = file_content_subrom['DC Pressure(+)'].values.tolist() [4:16]# 读取dc，转化数组
            file_data_subrom_rc = file_content_subrom['RC Pressure(+)'].values.tolist() [15:16] # 读取rc，转化数组
            file_data_subrom_tc1 = file_content_subrom['TC Pressure(+)'].values.tolist() [2:12]# 读取tc+，转化数组
            file_data_subrom_tc2 = file_content_subrom['TC Pressure(-)'].values.tolist() [2:12] # 读取tc-，转化数组
            subrom_data1 = file_data_subrom_ml1+file_data_subrom_ml2+file_data_subrom_ss1+file_data_subrom_ss2+file_data_subrom_ps1+file_data_subrom_ps2+file_data_subrom_dc+file_data_subrom_rc+file_data_subrom_tc1+file_data_subrom_tc2
            subrom_data.append(result_name)
            subrom_data.append(result_time)
            subrom_data += subrom_data1
            with open('SubROM1_data.csv', 'a+', newline='') as csvfile:  # 输出
                writer = csv.writer(csvfile)
                writer.writerow(subrom_data)
resultdata = pd.read_csv("./Result_data.csv",header=None)
subrom1data = pd.read_csv("./SubROM1_data.csv",header=None)
ts11_data=pd.merge(subrom1data,resultdata,left_on = (0,1),right_on = (0,1))
ts11_data.to_csv('TS11_data.csv', mode='a', index=False, header=False)
os.remove("./SubROM1_data.csv")
os.remove("./Result_data.csv")
