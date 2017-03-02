**Python Distance Program for ESP-07 modules and Windows Machine**

Python Script that runs on a windows machine to locate SPS networks (our ESP nodes), gets its mac address and RSSI signal,
convert the RSSI into a signal, then plot the nodes on a graph (the x and y position of the nodes are currently hardcoded)
Once graphed, it will take the distances of each node and run it through a trilateration program that returns an x and y
coordinate of where it thinks the laptop is in comparison to the nodes. Then it graphs this point along with the other nodes.

Things to note: distance.py uses a distance function gathered from real data and is not a physics derived equations
                trilat.py is borrowed from another python script for trilateration and is not 100% accurate
                Node positions and mac addresses are defined in definitions.py
