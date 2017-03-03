import matplotlib.pyplot as plt

def drawCircles(circles,predictedPosition):
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

    for circle in circles:
        x = circle.x
        y = circle.y
        rad = circle.r
        ax.add_patch(plt.Circle((x,y),radius=rad, color='k', fill=False))
        ax.add_patch(plt.Circle((x,y),radius=.05, color='k', fill=True))
    
    ax.add_patch(plt.Circle((predictedPosition.x, predictedPosition.y),radius=.06, color='b', fill=True))
    # Show plot
    plt.draw()
    plt.show()

