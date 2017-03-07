import matplotlib.pyplot as plt

def drawCircles(circles,predictedPosition):
    minX = min(i.x for i in circles)
    minY = min(i.y for i in circles)
    maxX = max(i.x for i in circles)
    maxY = max(i.y for i in circles)
    axisOffset = max(i.r for i in circles)
    #axisOffset = 2;

    # Figure setup
    fig=plt.figure(1)
    plt.axis([minX - axisOffset, maxX + axisOffset, minY - axisOffset, maxY + axisOffset])
    ax=fig.add_subplot(1,1,1)
    ax.cla()
    ax.set_title('Node Localization')
    ax.set_xlabel('X Distance (in meters)')
    ax.set_ylabel('Y Distance (in meters)')
    plt.ion()
    plt.show()
    
    # Otherwise draw the predicted position on the graph
    # Draw the found nodes and their estimated distances

    for circle in circles:
        x = circle.x
        y = circle.y
        rad = circle.r
        name = "Node"
        if (circle.name):
            name = circle.name
        ax.add_patch(plt.Circle((x,y),radius=rad, color='k', fill=False))
        ax.add_patch(plt.Circle((x,y),radius=.05, color='k', fill=True))
        ax.annotate(name, xy=(x,y+.25),horizontalalignment='center',size=8)
    
    ax.add_patch(plt.Circle((predictedPosition.x, predictedPosition.y),radius=.06, color='b', fill=True))
    # Show plot
    plt.draw()
    plt.show()

