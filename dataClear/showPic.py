import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from pandas import DataFrame

import pandas as pd

class ShowPic(object):
    def __init__(self,file_path:str):
        self.file_path = file_path
    
    def read_data(self):
        # 从excel表格读取数据
        data = pd.read_excel(self.file_path,names = ['RGB','Ther','all','person','car'])
        self.data =  data
        rgb =  list(map(lambda x: x * 640, data['RGB']))
        ther = list(map(lambda x: x * 480, data['Ther']))
        self.data['RGB'] = rgb
        self.data['Ther'] = ther
        
        print(data)

    def show(self):
        data = self.data
        fig = plt.figure()
        ax = Axes3D(fig)
        # ax = fig.add_subplot(111, projection='3d')
        x = data['RGB']
        y = data['Ther']
        z = data['all']
        # 颜色深度
        c = data['all'] 
        person = data['person']
        car = data['car']
         # s表明点的大小
        # ax.scatter(x, y, z, c=c, cmap='coolwarm', s=100)  渐变色
        ax.scatter(x, y, z, c=c, cmap='coolwarm', s=100)
        ax.scatter(x,y,car, c='r', marker='^')
        # person和all差不多，不显示
        # ax.scatter(x,y,person, c='r',marker='^') 
        ax.set_xlabel('RGB')
        ax.set_ylabel('Ther')
        ax.set_zlabel('all')
        plt.show()
    def save(self,file_path:str):
        data = self.data
        df = pd.DataFrame(data)
        df.to_csv(file_path)
        print("save to ",file_path)


if __name__ == "__main__":
    a = ShowPic("rgb_th_4.xlsx")
    a.read_data()
    a.show()
