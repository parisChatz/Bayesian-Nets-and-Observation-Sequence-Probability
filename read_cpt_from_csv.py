import pandas as pd
from networks import networks
from parsing import parsing


class read_cpts_from_csv():
    def __init__(self, net):
        self.net = net
        self.df = pd.read_csv('lucas0_train.csv')
        self.row, self.col = self.df.shape
        self.df.replace(0, "-", inplace=True)
        self.df.replace(1, "+", inplace=True)
        self.df.columns = ['S', 'YF', 'AN', 'PP', 'G',
                           'AD', 'BED', 'CO', 'F', 'AL', 'CA', 'LC']

    def find_prob0(self, var_nosign, variables):
        sign = variables[0]
        count = self.df[var_nosign].value_counts()
        count = count[sign]
        return (count + 1) / (self.row + 2)

    def find_prob1(self, variables, conditions):
        sign = variables[0]
        cond_sign = conditions[0]
        kounter = 0
        kounter2 = 0
        for num, item in enumerate(self.df[variables[1:].upper()]):
            if item == sign and self.df[conditions[1:].upper()][num] == cond_sign:
                kounter += 1
            if self.df[conditions[1:].upper()][num] == cond_sign:
                kounter2 += 1
        return(kounter + 1) / (kounter2 + 2)

    def find_prob2(self, variables, new_cond=None):
        sign = variables[0]
        cond_sign1 = new_cond[0][0]
        cond_sign2 = new_cond[1][0]
        kounter = 0
        kounter2 = 0
        for num, item in enumerate(self.df[variables[1:].upper()]):
            if item == sign and self.df[new_cond[0][1:].upper()][num] == cond_sign1 and self.df[new_cond[1][1:].upper()][num] == cond_sign2:
                kounter += 1
            if self.df[new_cond[0][1:].upper()][num] == cond_sign1 and self.df[new_cond[1][1:].upper()][num] == cond_sign2:
                kounter2 += 1
        return(kounter + 1) / (kounter2 + 2)

    def read_cpts(self):
        variables = []
        conditions = []
        var_nosign = []
        cond_no_sign = []
        new_cond = []
        con = []
        for node in self.net["order"]:
            keylist = list(self.net[node].keys())
            for cond_prob in range(len(keylist)):
                variable, condition = parsing().parse_querry(
                    keylist[cond_prob])
                variables.append(variable)
                if condition is None:
                    conditions.append(None)
                else:
                    conditions.append(condition)
                var_nosign.append(variable[1:].upper())
                if condition is None:
                    cond_no_sign.append([None])
                else:
                    cond_no_sign.append(parsing().parse_evidence(condition))
        new_cond = cond_no_sign

        for i in range(len(cond_no_sign)):
            if cond_no_sign[i] is not None:
                for k in range(len(cond_no_sign[i])):
                    if conditions[i] != cond_no_sign[i][k]:
                        result = conditions[i].find(cond_no_sign[i][k])
                        new_cond[i][k] = conditions[i][result - 1] + \
                            cond_no_sign[i][k]
                    # print(result,conditions[i],cond_no_sign[i][k])

        for i in range(len(variables)):
            if conditions[i] is None:
                con.append(variables[i])
            elif conditions[i] is not None:
                con.append(variables[i] + "|" + conditions[i])

            # print(var_nosign[i],variables[i],len(new_cond[i]),conditions[i],con[i])

        size = len(var_nosign)
        for i in range(size):
            if conditions[i] is None:
                self.net[var_nosign[i]][con[i]] = self.find_prob0(
                    var_nosign[i], variables[i])
                # print(var_nosign[i],con[i],self.net[var_nosign[i]][variables[i]])
            elif len(new_cond[i]) == 1:
                self.net[var_nosign[i]][con[i]] = self.find_prob1(
                    variables[i], conditions[i])
                # print(var_nosign[i],con[i],self.net[var_nosign[i]][con[i]],len(new_cond[i]))
            elif len(new_cond[i]) == 2:
                self.net[var_nosign[i]][con[i]] = self.find_prob2(
                    variables[i], new_cond[i])
                # print(var_nosign[i],con[i],self.net[var_nosign[i]][con[i]],len(new_cond[i]))
        return self.net


if __name__ == '__main__':
    read_cpts_from_csv(networks().initialiseNet("cancer")).read_cpts()
