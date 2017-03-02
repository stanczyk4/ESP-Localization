import localization as lx

def trilat2D(circles):
    mySolver = "LSE"
    if len(circles == 2):
    	mySolver = "LSE_GC"
    elif len(circles < 2):
    	return -1

    P = lx.Project(mode="2D", solver=mySolver)
 	t, label = P.add_target()

    for anchors in circles:
    	P.add_anchor(anchors.mac, (anchor.x, anchor.y))
    	t.add_measure(anchors.mac, anchors.r)

    P.solve()
    center = t.loc

    return center
