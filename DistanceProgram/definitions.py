class nodeClass(object):
    def __init__(self,name,mac,x,y):
    	self.name = name
        self.mac = mac
        self.x = x
        self.y = y
        

nodeList = []

# Node 1
node1 = nodeClass("Node 1", '5E:CF:7F:D1:78:FE', 0, 0)
# Node 2
node2 = nodeClass("Node 2", '5E:CF:7F:D1:8F:87', 0, 0)
# Node 3
node3 = nodeClass("Node 3", '5E:CF:7F:D1:83:81', 0, 0)
# Node 4
node4 = nodeClass("Node 4", '5E:CF:7F:D1:75:2A', 0, 0)
# Node 5
node5 = nodeClass("Node 5", 'A2:20:A6:0D:0F:E8', 0, 0)
# Node 6
node6 = nodeClass("Node 6", 'A2:20:A6:0D:0F:B9', 0, 0)
# Node 7
#node7 = node("Node 7", '', 0, 0)
# Node 8
#node8 = node("Node 7", '', 0, 0)

nodeList.append(node1)
nodeList.append(node2)
nodeList.append(node3)
nodeList.append(node4)
nodeList.append(node5)
nodeList.append(node6)

locations = {}

for myNodes in nodeList:
    locations[myNodes.mac] = [myNodes.name,myNodes.x,myNodes.y]
