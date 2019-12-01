import pandas as pd
from networks import networks
from parsing import parsing

class read_cpts_from_csv():
    def __init__(self,net):
        self.net = net

    def read_cpts(self):
        variables = []
        conditions = []
        var_nosign = []
        cond_no_sign = []
        new_cond = []
        df = pd.read_csv('lucas0_train.csv')
        for node in self.net["order"]:
            keylist = list(self.net[node].keys())
            for cond_prob in range(len(keylist)):
                variable, condition = parsing().parse_querry(keylist[cond_prob])
                variables.append(variable)
                conditions.append(condition)
                var_nosign.append(variable[1:].upper())
                if condition==None:
                    cond_no_sign.append(None)
                else:
                    cond_no_sign.append(parsing().parse_evidence(condition))
        new_cond = cond_no_sign

        for i in range(len(cond_no_sign)):
            if cond_no_sign[i] is not None:
                for k in range(len(cond_no_sign[i])):
                    result = conditions[i].find(cond_no_sign[i][k])
                    new_cond[i][k]=conditions[i][result-1]+cond_no_sign[i][k]
                    # print(result,conditions[i],cond_no_sign[i][k])
            print(var_nosign[i],variables[i],conditions[i])

            # if  cond_no_sign[i] == variables[i]:
            #     cond_no_sign[i] = None
            # print(var_nosign[i], variables[i],cond_no_sign[i])
            # print(cond_no_sign[i],cond_no_sign[i])
        
        # for i in range(len(variables)):





if __name__ == '__main__':
    read_cpts_from_csv(networks().initialiseNet("cancer")).read_cpts()