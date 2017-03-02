#import matplotlib.pyplot as plt

def drawCircles(plt,ax,circles):

    for circle in circles:
        x = circle.center.x
        y = circle.center.y
        rad = circle.radius
        ax.add_patch(plt.Circle((x,y),radius=rad, color='k', fill=False))
        ax.add_patch(plt.Circle((x,y),radius=.01, color='k', fill=True))

    plt.draw()


