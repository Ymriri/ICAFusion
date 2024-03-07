# -*- coding: utf-8 -*-
"""
@since      :2024/3/5 21:45
@Author    :Ymri

""" 

import os

from pandas import DataFrame
 
class DataClear(object):
    def __init__(self,file_path):
        self.file_path = file_path
    def read_RGB_data(self):
        ret_list = []
        with open(self.file_path, 'r') as f:
            # 手动一行一行读取，然后截取
            while True:
                line = f.readline()
                if "---end---" in line:
                    print("---end---")
                    break 
                # 找到一个开始标志
                if "----------epoch" in line:
                    resolution = str(line).replace("----------epoch","").replace("------------","").replace(":","").split()
                    ret_data = {
                        "rgb": resolution[0], # rgb 
                        "ther": resolution[1],  # 热成像
                        "data":[]
                    }
                    temp_data = []
                    # 开始读一轮的数据
                    while True:
                        line = f.readline()
                        # 读到一轮的结束
                        if "labels saved to" in line:
                            break
                        if "all        1013" in line:
                            # 提取一行
                            temp_line = line.split()
                            temp_data.append(temp_line[5])
                            pass 
                        if "person" in line:
                            temp_line = line.split()
                            temp_data.append(temp_line[5])
                            # 提取person
                            pass
                        if "car" in line:
                            temp_line = line.split()
                            temp_data.append(temp_line[5])
                            # 提取car
                            pass
                        # 分辨率 all 的mp50 person 的mp50 car的mp50    all mp50
                    ret_data["data"] = temp_data
                    ret_list.append(ret_data)
        self.data_list = ret_list
        return ret_list
    def save(self,file_path:str):
        data = {'RGB': [], 'Ther': [], 'all': [], 'person': [], 'car': []}
        data_list = self.data_list 
        for item in data_list:
            data['RGB'].append(float(item['rgb']))
            data['Ther'].append(float(item['ther']))
            data['all'].append(float(item['data'][0]))
            data['person'].append(float(item['data'][1]))
            data['car'].append(float(item['data'][2]))
        df = DataFrame.from_dict(data)
        # print(df)
        df.to_excel(file_path)

if __name__ == "__main__":
    temp = DataClear("/Users/ym/ICAFusion/dataClear/rgb_th_4.log")
    temp.read_RGB_data()
    temp.save("/Users/ym/ICAFusion/dataClear/rgb_th_4.xlsx")