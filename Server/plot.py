'''import matplotlib.pyplot as plt

def PlotFunction(nodes, loc):
	plt.close('all')
	minX = min(x[1][2] for x in nodes)
	minY = min(y[1][3] for y in nodes)
	maxX = max(x[1][2] for x in nodes)
	maxY = max(y[1][3] for y in nodes)
	axisOffset = max(rssi[1][0] for rssi in nodes)

	fig = plt.figure(1)
	plt.axis([minX - axisOffset, maxX + axisOffset, minY - axisOffset, maxY + axisOffset])
	ax=fig.add_subplot(1,1,1)
	#ax.clf()
	ax.cla()
	ax.set_title('Node Localization')
	ax.set_xlabel('X Distance (in meters)')
	ax.set_ylabel('Y Distance (in meters)')
	plt.ion()

	for circle in nodes:
			x = circle[1][2]
			y = circle[1][3]
			rad = circle[1][0]
			name = "Node"

			if (circle[0]):
				name = circle[0]

			ax.annotate(name, xy=(x,y+.20),horizontalalignment='center',size=8)
			ax.add_patch(plt.Circle((x,y),radius=.05, color='k', fill=True))
			ax.add_patch(plt.Circle((x,y),radius=rad, color='k', fill=False))

	ax.add_patch(plt.Circle((loc.x, loc.y),radius=.06, color='b', fill=True))

	plt.draw()
	plt.show()

class Plot():
	def __init__(self, makePlot):
		if makePlot == True:
			#self.plt = plt
			self.makeGraph = True
			self.fig = plt.figure(1)
			self.ax = self.fig.add_subplot(1,1,1)
			plt.ion()
			self.ax.cla()

		else:
			#self.makeGraph = False
			return False

	def closeGraph(self):
		if self.fig:
			self.fig.close()

	def plotGraph(self, nodes, loc):
		self.ax.cla() #clears axis
		self.ax.set_title('Node Localization')
		self.ax.set_xlabel('X Distance (in meters)')
		self.ax.set_ylabel('Y Distance (in meters)')
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

		plt.draw()
		plt.show()
'''


