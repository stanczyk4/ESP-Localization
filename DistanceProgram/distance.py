import math

def calculate_distance(signal_strength):
    est_dist = math.pow(math.e,(int(signal_strength) + 42.849) / -10.693)
    return est_dist

def convert(nodes):
    distanceList = []
    for node in nodes:
        x = calculate_distance(node.values()[0])
        dic = {node.keys()[0]:x}
        distanceList.append(dic)
    return distanceList