import time
import scanner
import identify
import trilat
import plot
import matplotlib.pyplot as plt
import distance

def main ():

    # Returning list of dictionaries where each is {BSSID:RSSI}
    nodes = scanner.get_BSSI()

    # Calculates distances
    # Converts {BSSID:RSSI} to {BSSID:estimated distance}
    nodes = distance.convert(nodes)

    # Returns a list of circle objects (MAC,x,y,r)
    circles = identify.identify(nodes)
    


    for i in circles:
        print i
        print "\n"

    # PASS CIRCLES LIST HERE

    # Figure setup
    fig=plt.figure(1)
    plt.axis([-5,10,-5,10])
    ax=fig.add_subplot(1,1,1)
    plt.ion()
    plt.show()
    ax.cla()

    # Draw the found nodes and their estimated distances
    plot.drawCircles(plt, ax, circles)
    
    # Try to predict a central position
    predictedPosition = trilat.trilat2D(circles)

    # If we don't have 2 or more nodes, the trilateration function will not work
    if (len(circles)<2):
        # Alert the user
        print("Need 2 or more nodes")
        raw_input("Press enter to continue...")
    # Otherwise draw the predicted position on the graph
    else:
        ax.add_patch(plt.Circle((predictedPosition.x, predictedPosition.y),radius=.05, color='b', fill=True))
    # Show the plot and print the predicted position
    plt.show()
    print predictedPosition.x, predictedPosition.y

    raw_input("Press enter to continue...")

main()

