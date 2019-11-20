class networks():
    CPTs={}

    def __init__(self):
        pass       

    def initialiseNet(self, netID):
        if netID == "burglary":
            self.CPTs["B"]={"+b":0.001, "-b":0.999}
            self.CPTs["E"]={"+e":0.002, "-e":0.998}
            self.CPTs["A"]={"+a|+b+e":0.95, "-a|+b+e":0.05, 
                    "+a|+b-e":0.94, "-a|+b-e":0.06,
                    "+a|-b+e":0.29, "-a|-b+e":0.71,
                    "+a|-b-e":0.001, "-a|-b-e":0.999}
            self.CPTs["J"]={"+j|+a":0.90, "-j|+a":0.10, 
                    "+j|-a":0.05, "-j|-a":0.95}
            self.CPTs["M"]={"+m|+a":0.70, "-m|+a":0.30, 
                    "+m|-a":0.01, "-m|-a":0.99}
            self.CPTs["order"]=["B", "E", "A", "J", "M"]
            self.CPTs["parents"]={"B":None, "E":None, "A":"B,E", "J":"A", "M":"A"}

        elif netID == "sprinkler":
            self.CPTs["C"]={"+c":0.50, "-c":0.50}
            self.CPTs["S"]={"+s|+c":0.10, "-s|+c":0.90, 
                    "+s|-c":0.50, "-s|-c":0.50}
            self.CPTs["R"]={"+r|+c":0.80, "-r|+c":0.20, 
                    "+r|-c":0.20, "-r|-c":0.80}
            self.CPTs["W"]={"+w|+s+r":0.99, "-w|+s+r":0.01, 
                    "+w|+s-r":0.90, "-w|+s-r":0.10,
                    "+w|-s+r":0.90, "-w|-s+r":0.10,
                    "+w|-s-r":0.00, "-w|-s-r":1.00}
            self.CPTs["order"]=["C", "S", "R", "W"]
            self.CPTs["parents"]={"C":None, "S":"C", "R":"C", "W":"S,R"}
            
        elif netID == "disease":
            
            self.CPTs["D"] = {"+d": 0.1, "-d": 0.999}
            self.CPTs["T"] = {"+t|+d": 0.99, "-t|-d": 0.95,
                            "+t|-d": 0.01, "-t|+d": 0.05}

            self.CPTs["order"] = ["D", "T"]
            self.CPTs["parents"] = {"D": None, "T": "D"}

        else:
            print("UNKNOWN network="+str(netID))
            exit(0)

        return self.CPTs