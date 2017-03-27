import atexit
import time
import sys

#local libraries
import database
import server
import packet
import sensorClass
import plot

databaseFilePath = 'database.db'
serverIP = "127.0.0.1"
serverPORT = 5005
plotGraph = True

def programExit(db,serv,graph):
    graph.closeGraph()
    db.closeDatabase()
    serv.closeSocket()
    sys.exit()


def main():
    #create database object db to handle all database functionality
    db = database.Database(databaseFilePath)
    #create server object serv to handle all server operations
    serv = server.Server(serverIP, serverPORT)

    #create plot figure if plotGraph = True, otherwise set myGraph to False
    myGraph = plot.Plot(plotGraph)

    #register an OnExit function to close the database and server in case the program exits
    atexit.register(programExit, db, serv, myGraph)

    #start listening to packets in the background
    serv.listenForPackets()
    sensorData = sensorClass.SensorList()
 

    while True:
        #checks if we have a packet, if so, do something else loop again
        if not serv.queue.empty():
            newPacket = packet.Packet(serv.queue.get())
            newPacket.sortPacket()

            sensorData.getIndex(newPacket.MAC_Sensor)
            #Now index contains the correct sensor object

            # If we dont have a sensor data object for this sensor
            # Create a new one and append to the sensorData list
            sensorData.wasFound(newPacket.MAC_Sensor, db)

            # Clear out old data from beacons
            print "Cleaning expired data...\n"
            sensorData.removeOldSensors()

            # Add the new values
            print "Adding new data values...\n"
            sensorData.addNewSensor(newPacket, db.c)

            print sensorData.listSensorItems() 

            # Check if there are 3 or more beacons for this sensorData, if so, Trilaterate it
            if sensorData.sensorListLength() > 2:
                loc = sensorData.sensorTrilat()
                print "LOCATION:",loc
                if myGraph:
                    myGraph.plotGraph(sensorData.listSensorItems(), loc)


if __name__ == "__main__":
    main()
