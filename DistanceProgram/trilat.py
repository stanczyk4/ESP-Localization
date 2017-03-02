#!/usr/bin/env
# -*- coding:utf-8 -*-

from __future__ import division
import json
import math
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.2f')

#import turtle
import matplotlib.pyplot as plt

class base_station(object):
    def __init__(self, lat, lon, dist):
        self.lat = lat
        self.lon = lon
        self.dist = dist

class point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class circle(object):
    def __init__(self, point, radius):
        self.center = point
        self.radius = radius

class json_data(object):
    def __init__(self, circles, inner_points, center):
        self.circles = circles
        self.inner_points = inner_points
        self.center = center

def serialize_instance(obj):
    d = {}
    d.update(vars(obj))
    return d

def get_two_points_distance(p1, p2):
    return math.sqrt(pow((p1.x - p2.x), 2) + pow((p1.y - p2.y), 2))

def get_two_circles_intersecting_points(c1, c2):
    p1 = c1.center
    p2 = c2.center
    r1 = c1.radius
    r2 = c2.radius

    d = get_two_points_distance(p1, p2)
    # if to far away, or self contained - can't be done
    if d >= (r1 + r2) or d <= math.fabs(r1 -r2):
        return None

    a = (pow(r1, 2) - pow(r2, 2) + pow(d, 2)) / (2*d)
    h  = math.sqrt(pow(r1, 2) - pow(a, 2))
    x0 = p1.x + a*(p2.x - p1.x)/d
    y0 = p1.y + a*(p2.y - p1.y)/d
    rx = -(p2.y - p1.y) * (h/d)
    ry = -(p2.x - p1.x) * (h / d)
    return [point(x0+rx, y0-ry), point(x0-rx, y0+ry)]

def get_all_intersecting_points(circles):
    points = []
    num = len(circles)
    for i in range(num):
        j = i + 1
        for k in range(j, num):
            res = get_two_circles_intersecting_points(circles[i], circles[k])
            if res:
                points.extend(res)
    return points

def is_contained_in_circles(point, circles):
    for i in range(len(circles)):
        if (get_two_points_distance(point, circles[i].center) > (circles[i].radius)):
            return False
    return True

def get_polygon_center(points):
    center = point(0, 0)
    num = len(points)
    if num > 0:
        for i in range(num):
            center.x += points[i].x
            center.y += points[i].y
        center.x /= num
        center.y /= num
    return center

def drawCircles(plt,ax,circles):

    for circle in circles:
        x = circle.center.x
        y = circle.center.y
        rad = circle.radius
        ax.add_patch(plt.Circle((x,y),radius=rad, color='k', fill=False))
        ax.add_patch(plt.Circle((x,y),radius=.01, color='k', fill=True))

    plt.draw()



def trilat2D(circle_list):
    ############ Define Points Here ###################
    #p1 = point(0,0)
    #p2 = point(0,1)
    #p3 = point(1,0)
    #p4 = point(1,1)
    #c1 = circle(p1, 0.60)
    #c2 = circle(p2, 0.50)
    #c3 = circle(p3, 0.50)
    #c4 = circle(p4, 0.50)
    ###################################################
    #c1.center.x, c1.center.y, c1.radius  #class properties for above objects

    #create a list containing all the properties of our nodes, (center point and radius)
    #circle_list = [c1, c2, c3, c4]

    #magic math to get trilateration stuff
    inner_points = []
    for p in get_all_intersecting_points(circle_list):
        #including the line below will give a more accurate answer, but will cause an error if all the points dont intersect with each other
        #if is_contained_in_circles(p, circle_list):
            inner_points.append(p)

    # THIS IS THE OUTPUT WHERE IT THINKS THE ANSWER IS
    center = get_polygon_center(inner_points)
    print center.x, center.y #print to terminal the x and y

    #plot the answer on the plot
    #ax.add_patch(plt.Circle((center.x,center.y),radius=.01, color='b', fill=True))
    #plt.draw()


    #create json format for json data to write
    in_json = json_data([c1, c2, c3, c4], [p1, p2, p3, p4], center)
    out_json = json.dumps(in_json, sort_keys=True,
                     indent=4, default=serialize_instance)

    with open("data.json", 'w') as fw:
        fw.write(out_json)

    return center
