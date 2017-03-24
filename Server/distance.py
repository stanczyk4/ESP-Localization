import math

def calcDistance(RSSI):
	return math.pow(math.e,(int(RSSI) + 42.849) / -10.693)
