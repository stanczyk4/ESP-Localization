from definitions import *

class circle(object):
    def __init__(self,mac,x,y,r):
        self.mac = mac
        self.x = x
        self.y = y
        self.r = r
    def __str__(self):
        return str(self.mac)+"\nX:"+str(self.x)+"\nY:"+str(self.y)+"\nR:"+str(self.r)

def identify(new):

    # List of all circles
    circles = []

    # Loop through all nodes that were discovered in the latest scan
    for node in range(len(new)):
        # For each one, loop through the list of node locations
        for j in range(len(locations)):
            # Compare the BSSID of the current node to the BSSID of the current location item
            if new[node].keys()[0] == locations.keys()[j]:
                # If they match, associate the X and Y locations with the signal strength
                x = locations.values()[j][0]
                y = locations.values()[j][1]
                r = new[node].values()[0]
                mac = new[node].keys()[0]

                # Associate the values into a circle object
                newCircle = circle(mac,x,y,r)

                #print newCircle
                
                # Append to list
                circles.append(newCircle)

    return circles