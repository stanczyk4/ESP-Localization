class nodeClass(object):
    def __init__(self,name,mac,x,y):
    	self.name = name
        self.mac = mac
        self.x = x
        self.y = y
        

nodeList = []

# Node 1
node1 = nodeClass("SPS:1", '5E:CF:7F:D1:78:FE', 0, 0)
# Node 2
node2 = nodeClass("SPS:2", '5E:CF:7F:D1:8F:87', 1, 2)
# Node 3
node3 = nodeClass("SPS:3", '5E:CF:7F:D1:83:81', 2, -1)
# Node 4
node4 = nodeClass("SPS:4", '5E:CF:7F:D1:75:2A', -1, 3)
# Node 5
node5 = nodeClass("SPS:5", 'A2:20:A6:0D:0F:E8', 0, 1)
# Node 6
node6 = nodeClass("SPS:6", 'A2:20:A6:0D:0F:B9', 1, 0)
# Node 7
#node7 = node("SPS:7", '', 0, 0)
# Node 8
#node8 = node("SPS:8", '', 0, 0)

nodeList.append(node1)
nodeList.append(node2)
nodeList.append(node3)
nodeList.append(node4)
nodeList.append(node5)
nodeList.append(node6)
#nodeList.append(node7)
#nodeList.append(node8)

#############LOOPING METHOD####################
locations = {}
for myNodes in nodeList:
    locations[myNodes.mac] = [myNodes.name,myNodes.x,myNodes.y]

#############ALTERNATE METHOD USING LESS MEMORY, but maybe more user input?#############
#to use this method comment out all the stuff above except class nodeClass
#locations = {}
# Node 1
#nodeX = nodeClass("SPS:1", '5E:CF:7F:D1:78:FE', 0, 0)
#locations.update({nodeX.mac:[nodeX.name,nodeX.x,nodeX.y]})
# Node 2
#nodeX = nodeClass("SPS:2", '5E:CF:7F:D1:8F:87', 0, 0)
#locations.update({nodeX.mac:[nodeX.name,nodeX.x,nodeX.y]})
# Node 3
#nodeX = nodeClass("SPS:3", '5E:CF:7F:D1:83:81', 0, 0)
#locations.update({nodeX.mac:[nodeX.name,nodeX.x,nodeX.y]})
# Node 4
#nodeX = nodeClass("SPS:4", '5E:CF:7F:D1:75:2A', 0, 0)
#locations.update({nodeX.mac:[nodeX.name,nodeX.x,nodeX.y]})
# Node 5
#nodeX = nodeClass("SPS:5", 'A2:20:A6:0D:0F:E8', 0, 0)
#locations.update({nodeX.mac:[nodeX.name,nodeX.x,nodeX.y]})
# Node 6
#nodeX = nodeClass("SPS:6", 'A2:20:A6:0D:0F:B9', 0, 0)
#locations.update({nodeX.mac:[nodeX.name,nodeX.x,nodeX.y]})
