import pandas as pd
from networks import networks

class read_cpts_from_csv():
    def __init__(self,net):
        self.net = net

    def read_cpts(self):

        df = pd.read_csv('lucas0_train.csv')

        for column in df.columns:
        	# print(column)
        	print (self.net["names"][column])


if __name__ == '__main__':
    read_cpts_from_csv(networks().initialiseNet("cancer")).read_cpts()