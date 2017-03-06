import time
import scanner
import identify
import trilat
import plot
import distance

def main ():
    plotGraphs = True

    nodes = []
    # Returning list of dictionaries where each is {BSSID:RSSI}
    print("Hit ctrl+c to stop scanning...\nScanning Networks...")
    while len(nodes)<2:
        print("."),
        nodes = scanner.get_BSSI()

    # Calculates distances
    # Converts {BSSID:RSSI} to {BSSID:estimated distance}
    nodes = distance.convert(nodes)

    # Returns a list of circle objects (MAC,x,y,r)
    circles = identify.identify(nodes)

    for i in circles:
        print i
        print "\n"

    # If we don't have 2 or more nodes, the trilateration function will not work
    if (len(circles)<2):
        # Alert the user
        print("Need 2 or more nodes")

    else:
         # Try to predict a central position
        predictedPosition = trilat.trilat2D(circles)
        error = math.sqrt(predictedPosition.x**2 + predictedPosition.y**2)
        #print the predicated position and its error
        print "x: ", predictedPosition.x, "y: ", predictedPosition.y, "\nError in meters: ", error, "\n"

        if (plotGraphs == True):
            plot.drawCircles(circles, predictedPosition)

    input = raw_input("Enter 1 to re-run, else quit program: ")
    if (input == '1'):
        main()
    else:
        return

main()

