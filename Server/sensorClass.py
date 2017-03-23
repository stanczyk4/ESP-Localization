import math
import time

class SensorList():
    def __init__(self):
        self.list = []
        self.sensorIndex = 0
        self.found = False

    def getIndex(self, MAC):
        for i in range(len(self.list)):
            if self.list[i].mac == MAC:
                #this is the sensor data object we want
                self.sensorIndex = i
                self.found = True
                break

    def wasFound(self, MAC, db):
        if not(self.found):
            sensorID = db.searchIDfromMACinSensor(MAC)
            newSensor = SensorData(MAC, sensorID)
            self.list.append(newSensor)
            self.sensorIndex = len(self.list) - 1


class SensorData(object):
    def __init__(self,MAC,ID):
        self.mac = MAC
        self.name = ID
        self.data_dict = {}
    def findCombo(self,MAC_Beacon):
        ret = 0
        for beacon in self.data_dict.items():
            # beacon = (mac, [rssi,timestamp])
            if beacon[0] == MAC_Beacon:
                ret = 1
                break
        return ret
    def replaceData(self,MAC,RSSI,db):
        # If we are replacing data, we should already know if the combo exists
        # or not
        db.execute('SELECT X FROM node WHERE MAC=?',(MAC,))
        X = db.fetchone()[0]
        db.execute('SELECT Y FROM node WHERE MAC=?',(MAC,))
        Y = db.fetchone()[0]
        db.execute('SELECT Z FROM node WHERE MAC=?',(MAC,))
        Z = db.fetchone()[0]

        est_dist = math.pow(math.e,(int(RSSI) + 42.849) / -10.693)

        self.data_dict[MAC] = [est_dist,time.time(),X,Y,Z]

    def clearOld(self):
        for beacon in self.data_dict.items():
            if time.time() - beacon[1][1] > 2:
                del self.data_dict[beacon[0]]

    def __str__(self):
        st = str(self.mac)+","+str(self.name)+"\n\n"
        for i in self.data_dict:
            st = st+i+"\n"

        return st
