import time
import scanner
import identify
import trilat
import plot
import matplotlib.pyplot as plt

def main ():

    test, distances = scanner.get_BSSI()
    distances = sorted(distances)
    for i in range(0,10):
        # Wait
        time.sleep(3)

        # Save old test and distances
        oldTest = test
        oldDistances = distances

        # Scan again
        test, distances = scanner.get_BSSI()

        # Sort the list of distances
        distances = sorted(distances)
        circles = identify.identify(distances)

        # PASS CIRCLES LIST HERE


    fig=plt.figure(1)
    plt.axis([-6,6,-6,6])
    ax=fig.add_subplot(1,1,1)
    plt.ion()
    plt.show()
    ax.cla()

    finalPosition = trilat2D(circles);

    ax.add_patch(plt.Circle((finalPosition.x, finalPosition.y),radius=.01, color='b', fill=True))
    plt.draw()
    input("Press enter to continue...")

main()

