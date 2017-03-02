locations = {'5E:CF:7F:D1:75:2A':[1,1], '5E:CF:7F:D1:78:FE':[2,3]}

class circle(object):
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
    def __str__(self):
        return "X:"+str(self.x)+"\nY:"+str(self.y)+"\nR:"+str(self.r)

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

                # Associate the values into a circle object
                newCircle = circle(x,y,r)

                print newCircle
                
                # Append to list
                circles.append(newCircle)

    return circles