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


    fig=plt.figure(1)
    plt.axis([-5,10,-5,10])
    ax=fig.add_subplot(1,1,1)
    plt.ion()
    plt.show()
    ax.cla()
    plot.drawCircles(plt, ax, circles)
    
    predictedPosition = trilat.trilat2D(circles)
    if (predictedPosition == -1):
        print("Need 2 or more nodes")
        raw_input("Press enter to continue...")

    ax.add_patch(plt.Circle((predictedPosition.x, predictedPosition.y),radius=.05, color='b', fill=True))
    plt.draw()
    print predictedPosition.x, predictedPosition.y

    raw_input("Press enter to continue...")

main()

