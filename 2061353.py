from graphics import *

def circle(win, centre, radius, colour):
    c = Circle(centre, radius)
    c.setFill(colour)
    c.draw(win)
    return c


def rectangle2(win, tlPoint, brPoint, colour):
    r = Rectangle(tlPoint, brPoint)
    r.setFill(colour)
    r.draw(win)
    return r

def rectangle(win, tlPoint, brPoint, colour):
    r = Rectangle(tlPoint, brPoint)
    r.setFill(colour)
    r.setOutline("red")
    r.draw(win)
    return r


def triangle(win,point1,point2,point3,colour):
    t=Polygon(point1,point2,point3)
    t.setFill(colour)
    t.setOutline(colour)
    t.draw(win)


def brPoint(tlPoint, width, height):
    x = tlPoint.getX() + width
    y = tlPoint.getY() + height
    brPoint = Point(x, y)
    return brPoint

def centrePoint(tlPoint, radius):
    x = tlPoint.getX() + radius
    y = tlPoint.getY() + radius
    centre = Point(x, y)
    return centre


def patchB(win, colour, tlPoint):
    dimension = 100
    centre = centrePoint(tlPoint, 50)
    scale = 30
    r = rectangle2(win,tlPoint,brPoint(tlPoint,dimension,dimension),colour)



def patchF(win, colour, tlPoint):
    dimension = 100
    centre = centrePoint(tlPoint, 50)
    scale = 30
    r = rectangle2(win, tlPoint, brPoint(tlPoint, dimension, dimension), colour)



def patchP(win, colour, tlPoint):
    dimension = 100
    centre = centrePoint(tlPoint, 50)
    scale = 30
    r = rectangle2(win,tlPoint,brPoint(tlPoint,dimension,dimension),colour)




def grid(win, tlx, tly,colour): #function for one of the later patches.
    alternate=True
    scale=20
    p1=Point(tlx,tly)
    p2=Point(tlx + 100,tly + 100)
    rectangle2(win,p1,p2,"white")
    for y in range(tly,tly + 100,scale):
        for x in range(tlx,tlx + 100,scale):
            tl=Point(x,y)
            br=brPoint(tl,scale,scale)
            if alternate:
                rectangle2(win,tl,br,"white")
            else:
                rectangle2(win,tl,br,colour)

            alternate = not alternate

def circles(win, tlx, tly,colour):
    scale=20
    alt=True
    for y in range(tly,tly + 100,scale):
        for x in range (tlx,tlx + 100,scale): #tlx + 100 and tly + 100 allows it to jump no matter the screensize allowing patch to be drawn.
            radius=10
            centre=Point(x+10,y+10)
            if alt:
                circle(win,centre,radius,colour)
            else:
                pass
            alt = not alt

def triangles(win, tlx, tly,colour):
    screensize=100
    scale=20
    alt=True
    reverse=False
    for y in range(tly,tly + 100,scale):
        for x in range(tlx ,tlx + 100,scale):
            if reverse==False:  # have this for the second set of triangles.
                # so both triangles dont overdraw on eachother.
                tl=Point(x,y)
                p1=Point(x+10,y+10)
                p2=Point(x+20,y)
                p3=Point(x+20,y+20)

                if alt: # useage of the alt flag since traingles need to be drawn.
                    triangle(win,p1,p2,p3,"white")
                else:
                    pass
            else:
                t1=Point(x+10,y+10)
                t2=Point(x,y)
                t3=Point(x,y+20)
                if alt:
                    triangle(win, t1, t2, t3, "white")
                else:
                    pass

            alt = not alt
        reverse =not reverse

def penpatch(win,tlPoint,colour):
    tlx = int(tlPoint.getX())
    tly = int(tlPoint.getY())
    grid(win, tlx, tly,colour)
    circles(win, tlx, tly,colour)
    triangles(win, tlx, tly,"white")




def finalpatch(win, tlOffset,colour):
    alt= True
    screensize=100
    for y in range(0,100,10):
        tl=Point(tlOffset.getX(), tlOffset.getY()+y)
        br=Point(tlOffset.getX()+screensize,tlOffset.getY()+100)
        if alt:
            rectangle2(win,tl,br,"white")
        else:
            rectangle2(win,tl,br,colour)
        screensize-=10
        alt = not alt
# import math
def print10():
    print("-"*10)
def menu():
    print10()
    print("-- PATCHES COURSEWORK --")
    print10()
    print("What size patch do you want?")
    print("5- 500x500")
    print("7 -700x700")
    print10()
    return int(input("please select an option: "))
def main():
    selection = menu() #by using a menu i can limit user error
    if selection==5:
        screenSize=500
    elif selection == 7:
        screenSize=700
    else:
        print("invalid size")



    colours = ["red", "green", "blue", "purple", "orange", "cyan"]
    valid = []
    while len(valid)!=3:
        print("valid colours are red, green, blue, purple, orange, cyan")
        for i in range(3):
                c =input("please enter a colour")
                if c in colours:
                    valid.append(c)
                else:
                    print("invalid colour")
                    break
    validcolours=valid

    win = GraphWin("test", screenSize, screenSize)
    for y in range(0, screenSize, 100):
        for x in range(0, screenSize, 100):
            tlPoint = Point(x, y)
            if y == x:  # if alternateFlag:  #if y  == 0 or x == 0   #or x == 400 or y == 400:
                colour = colours[0]
                finalpatch(win, tlPoint,validcolours[0])

            elif y >= x:

                patchB(win, validcolours[1], tlPoint)
                if y == screenSize - 100 or x == 0:
                    pass
                else:
                    penpatch(win,tlPoint,validcolours[1])
            elif y <= x:
                colour = colours[2]
                patchP(win, validcolours[2], tlPoint)
                if y == 0 or x == screenSize - 100:
                    finalpatch(win,tlPoint,validcolours[2])
    win.getMouse()


main()



