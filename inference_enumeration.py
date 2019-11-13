

class inf_by_enum:
    CPTs = {}

    def __init__(self):
        self.initialiseNet()

    def initialiseNet(self):
        self.CPTs["B"] = {"+b": 0.001, "-b": 0.999}
        self.CPTs["E"] = {"+e": 0.002, "-e": 0.998}
        self.CPTs["A"] = {"+a|+b+e": 0.95, "-a|+b+e": 0.05,
                          "+a|+b-e": 0.94, "-a|+b-e": 0.06,
                          "+a|-b+e": 0.29, "-a|-b+e": 0.71,
                          "+a|-b-e": 0.001, "-a|-b-e": 0.999}
        self.CPTs["J"] = {"+j|+a": 0.90, "-j|+a": 0.10,
                          "+j|-a": 0.05, "-j|-a": 0.95}
        self.CPTs["M"] = {"+m|+a": 0.70, "-m|+a": 0.30,
                          "+m|-a": 0.01, "-m|-a": 0.99}
        self.CPTs["order"] = ["B", "E", "A", "J", "M"]
        self.CPTs["parents"] = {"B": None,
                                "E": None, "A": "B,E", "J": "A", "M": "A"}
        print(self.CPTs["A"]["+b"])

    def normalize(self, probs):
        a = 1 / sum(probs)
        return a * probs


if __name__ == '__main__':
    inf_by_enum()
