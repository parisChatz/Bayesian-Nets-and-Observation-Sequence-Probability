class parsing():

    def __init__(self):
        pass

    def parse_data(self, data):

        data = data.replace("P(", "").replace(")", "").split("|")
        if len(data) > 1:
            query = data[0].split()
            evidence = data[1].split(",")
        return query, evidence
