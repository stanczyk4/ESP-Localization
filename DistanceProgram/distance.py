import math

# This function takes a signal strength and returns a distance estimate
# This is the only function that should be changed if a new method of calculating distance is found
def calculate_distance(signal_strength):
    est_dist = math.pow(math.e,(int(signal_strength) + 42.849) / -10.693)
    return est_dist

# This function converts a list of dictionaries from 
# {BSSID:signal_strength} to {BSSID:distance}
def convert(nodes):
    distanceList = []
    for node in nodes:
        x = calculate_distance(node.values()[0])
        dic = {node.keys()[0]:x}
        distanceList.append(dic)
    return distanceList