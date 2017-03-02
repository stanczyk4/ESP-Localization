import math

def calculate_distance(signal_strength):
    est_dist = math.pow(math.e,(int(signal_strength) + 42.849) / -10.693)
    return est_dist