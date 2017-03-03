#import matplotlib.pyplot as plt

def drawCircles(plt,ax,circles):

    for circle in circles:
        x = circle.x
        y = circle.y
        rad = circle.r
        ax.add_patch(plt.Circle((x,y),radius=rad, color='k', fill=False))
        ax.add_patch(plt.Circle((x,y),radius=.05, color='k', fill=True))

    plt.draw()


