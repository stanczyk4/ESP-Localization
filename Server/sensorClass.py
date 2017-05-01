import time

#local library
import trilat
import distance

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

    def removeOldSensors(self):
        self.list[self.sensorIndex].clearOld()

    def addNewSensor(self, packet, db):
        self.list[self.sensorIndex].replaceData(packet.MAC_Beacon, packet.Rssi, db)

    def listSensorItems(self):
        return self.list[self.sensorIndex].data_dict.items()

    def sensorListLength(self):
        return len(self.list[self.sensorIndex].data_dict.items())

    def sensorTrilat(self):
        return trilat.trilat2D(self.list[self.sensorIndex].data_dict)


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
        if (RSSI < -65):
            return
        db.execute('SELECT X FROM node WHERE MAC=?',(MAC,))
        X = db.fetchone()[0]
        db.execute('SELECT Y FROM node WHERE MAC=?',(MAC,))
        Y = db.fetchone()[0]
        db.execute('SELECT Z FROM node WHERE MAC=?',(MAC,))
        Z = db.fetchone()[0]

        est_dist = distance.calcDistance(RSSI)

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
