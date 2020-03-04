def split(strng, sep, pos):
    strng = strng.split(sep)
    return sep.join(strng[:pos]), sep.join(strng[pos:])


class Parsing:

    def __init__(self):
        pass

    @staticmethod
    def parse_data(data):

        data = data.replace("P(", "").replace(")", "").split("|")
        if len(data) > 1:
            query = data[0].split()
            evidence = data[1].split(",")
        return query, evidence

    @staticmethod
    def parse_querry(data):
        data = data.split("|")
        # data = data.replace("|",",")
        # print(data, len(data),"!")
        if len(data) == 1:
            return data[0], None
        else:
            return data

    @staticmethod
    def parse_evidence(evidence):
        if evidence is None:
            return None
        else:
            new_evidence = evidence.replace(
                "+", ",").replace("-", ",")[1:].split(",")

            return new_evidence

    @staticmethod
    def parse_parents(parents):
        if parents is None:
            return None
        else:
            new_parents = parents.split(",")

            return new_parents
