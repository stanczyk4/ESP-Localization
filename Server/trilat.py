import localization as lx
def trilat2D(nodes):
    mySolver = "LSE"
    P = lx.Project(mode='2D',solver=mySolver)

    for anchors in nodes.items():
        #add_anchor(ID, (x,y))
        P.add_anchor(anchors[0],(anchors[1][2],anchors[1][3]))

    t, label = P.add_target()
    for anchors in nodes.items():
        #add_measure(ID, distance)
        t.add_measure(anchors[0],anchors[1][0])

    P.solve()
    center = t.loc

    return center
