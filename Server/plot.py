import matplotlib.pyplot as plt
#from Tkinter import *
#Tk()

class Plot():
	def __init__(self, makePlot=False):
		if makePlot == True:
			#self.plt = plt
			plt.ion()
			self.makeGraph = True
			self.fig = plt.figure()
			self.ax = self.fig.add_subplot(111)
			self.ax.cla()
			self.ax.set_title('Node Localization')
			self.ax.set_xlabel('X Distance (in meters)')
			self.ax.set_ylabel('Y Distance (in meters)')
		else:
			#self.makeGraph = False
			return False

	def closeGraph(self):
		if self.fig:
			self.fig.close()

	def plotGraph(self, nodes, loc):
		self.ax.cla() #clears axis
		#self.ax.clf() #clears figure
		minX = min(x[1][2] for x in nodes)
		minY = min(y[1][3] for y in nodes)
		maxX = max(x[1][2] for x in nodes)
		maxY = max(y[1][3] for y in nodes)
		axisOffset = max(rssi[1][0] for rssi in nodes)

		plt.axis([minX - axisOffset, maxX + axisOffset, minY - axisOffset, maxY + axisOffset])
		for circle in nodes:
			x = circle[1][2]
			y = circle[1][3]
			rad = circle[1][0]
			name = "Node"

			if (circle[0]):
				name = circle[0]

			self.ax.annotate(name, xy=(x,y+.20),horizontalalignment='center',size=8)
			self.ax.add_patch(plt.Circle((x,y),radius=.05, color='k', fill=True))
			self.ax.add_patch(plt.Circle((x,y),radius=rad, color='k', fill=False))

		self.ax.add_patch(plt.Circle((loc.x, loc.y),radius=.06, color='b', fill=True))

		self.fig.canvas.draw()
		#plt.show()



