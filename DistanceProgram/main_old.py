import time
import scanner
import identify
import trilat
import plot
import matplotlib.pyplot as plt
import distance

def main ():
    plotGraphs = True
    nodes = []
    # Returning list of dictionaries where each is {BSSID:RSSI}
    print("Hit ctrl+c to stop scanning...\nScanning Networks...")
    while len(nodes)<2:
        print(".")
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
        print predictedPosition.x, predictedPosition.y
        if (plotGraphs == True):
            minX = min(i.x for i in circles)
            minY = min(i.y for i in circles)
            maxX = max(i.x for i in circles)
            maxY = max(i.y for i in circles)
            #axisOffset = max(i.r for i in circles)
            axisOffset = 2;
            # Figure setup
            fig=plt.figure(1)
            plt.axis([minX - axisOffset, maxX + axisOffset, minY - axisOffset, maxY + axisOffset])
            ax=fig.add_subplot(1,1,1)
            plt.ion()
            plt.show()
            ax.cla()
            # Otherwise draw the predicted position on the graph
            # Draw the found nodes and their estimated distances
            plot.drawCircles(plt, ax, circles)
            ax.add_patch(plt.Circle((predictedPosition.x, predictedPosition.y),radius=.05, color='b', fill=True))
            # Show the plot and print the predicted position
            plt.show()

    input = raw_input("Enter 1 to re-run, else quit program: ")
    if (input == '1'):
        main()
    else:
        return

main()

