def filterSSID(ssid):
    ret = 0
    if not ssid.startswith("SPS"):
        ret = 1
    return ret

def filterSignalStrength(signal_strength):
    ret = 0
    if signal_strength < -60:
        ret = 1
    return ret