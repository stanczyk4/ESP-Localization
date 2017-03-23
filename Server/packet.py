class Packet():
	def __init__(self, packet):
		self.packet = packet
		self.MAC_Sensor = ""
		self.MAC_Beacon = ""
		self.Rssi = ""

	def sortPacket(self):
		self.splitData = self.packet.split(',')
		self.MAC_Sensor = self.splitData[0]
		self.MAC_Beacon = self.splitData[1]
		self.Rssi = self.splitData[2]
