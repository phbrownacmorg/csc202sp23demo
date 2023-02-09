# Program to open a graphics window and draw nothing, correctly.
from graphics import *
import math
from typing import cast
from quit_button import makeButton, inButton

def makeHead(r: float, color: str) -> Circle:
    head: Circle = Circle(Point(0, 0), r)
    head.setFill(color)
    head.setOutline(color)
    return head

def makeMouseEar(x_sign: int, r: float, color: str) -> GraphicsObject:
    angle: float = 55 # angle from horizontal in degrees
    scale: float = 1.3
    x_offset: float = x_sign * scale * r * math.cos(math.radians(angle))
    y_offset: float = scale * r * math.sin(math.radians(angle))
    ear: Circle = Circle(Point(x_offset, y_offset), r * 0.6)
    ear.setFill(color)
    ear.setOutline(color)
    return ear

def makeEye(x_sign: int, r: float, color: str) -> GraphicsObject:
    angle: float = 50
    x_offset: float = x_sign * r * math.cos(math.radians(angle))
    y_offset: float = r * math.sin(math.radians(angle))
    topPt: Point = Point(x_offset, y_offset)
    x_offset = x_sign * r * 0.1
    bottomPt: Point = Point(x_offset, 0)
    eye: Oval = Oval(topPt, bottomPt)
    eye.setFill(color)
    return eye

def makeNose(r: float) -> GraphicsObject:
    y_dist: float = r * 0.25
    bottom: Point = Point(0, -y_dist)
    left: Point = Point(-y_dist * 0.5, 0)
    right: Point = Point(y_dist * 0.5, 0)
    nose: Polygon = Polygon(bottom, left, right)
    nose.setFill('black')
    return nose

def makeMouthLine(x_sign: int, r: float) -> Line:
    angle: float = 20 # Angle below vertical in degrees
    y_below: float = r * -0.3
    inPt: Point = Point(0, y_below)
    scale: float = 0.4
    out_x: float = x_sign * r * math.cos(math.radians(angle)) * scale
    out_y: float = y_below - r * math.sin(math.radians(angle)) * scale
    outPt: Point = Point(out_x, out_y)
    return Line(inPt, outPt)

def makeWhisker(x_sign: int, y_val: int, r: float) -> Line:
    angle: float = y_val * 10
    in_scale: float = 0.8
    out_scale: float = 1.8
    x: float = x_sign * in_scale * r * math.cos(math.radians(angle))
    y: float = in_scale * r * math.sin(math.radians(angle))
    inPt: Point = Point(x, y)
    x = x_sign * out_scale * r * math.cos(math.radians(angle))
    y = out_scale * r * math.sin(math.radians(angle))
    outPt: Point = Point(x, y)
    return Line(inPt, outPt)

def makeCatEar(x_sign: int, r: float, color: str) -> GraphicsObject:
    centralAngle: float = 55 # angle from horizontal in degrees
    widthAngle: float = 20
    outer_scale: float = 1.5

    x = x_sign * outer_scale * r * math.cos(math.radians(centralAngle))
    y = outer_scale * r * math.sin(math.radians(centralAngle))
    tip: Point = Point(x, y)
    x = x_sign * r * math.cos(math.radians(centralAngle + widthAngle))
    y = r * math.sin(math.radians(centralAngle + widthAngle))
    base1: Point = Point(x, y)
    x = x_sign * r * math.cos(math.radians(centralAngle - widthAngle))
    y = r * math.sin(math.radians(centralAngle - widthAngle))
    base2: Point = Point(x, y)
    ear: Polygon = Polygon(tip, base1, base2)
    ear.setFill(color)
    ear.setOutline(color)
    return ear

# Define an animal as a list of GraphicsObjects, all of which
# move together.  It always starts at the origin.
def makeMouse(r: float) -> list[GraphicsObject]:
    color: str = 'gray30'
    animal: list[GraphicsObject] = []
    animal.append(makeHead(r, color))

    # Make ears
    for x_sign in [-1, 1]:
        animal.append(makeMouseEar(x_sign, r, color))

    # Ears and eyes aren't interleaved to ensure the right order in the list
    for x_sign in [-1, 1]: 
        animal.append(makeEye(x_sign, r, 'black'))

    # Nose
    #nose = Circle(Point(0, 0), r * 0.1)
    #nose.setFill('black')
    animal.append(makeNose(r))

    # Mouth
    for x_sign in [-1, 1]:
        animal.append(makeMouthLine(x_sign, r))

    for x_sign in [-1, 1]:
        for y_val in [-1, 0, 1]:
            animal.append(makeWhisker(x_sign, y_val, r))

    return animal

def makeCat(r: float) -> list[GraphicsObject]:
    # Pre:
    assert r > 0, "makeCat: r must be positive"
    cat: list[GraphicsObject] = []
    color: str = 'orange'
    cat.append(makeHead(r, color))

    for x_sign in [-1, 1]:
        cat.append(makeCatEar(x_sign, r, color))

    for x_sign in [-1, 1]:
        cat.append(makeEye(x_sign, r, 'green'))

    cat.append(makeNose(r))
    for x_sign in [-1, 1]:
        cat.append(makeMouthLine(x_sign, r))

    for x_sign in [-1, 1]:
        for y_val in [-1, 0, 1]:
            cat.append(makeWhisker(x_sign, y_val, r))

    # Post: 
    assert len(cat) == 14 # and they're all the correct things for a cat
    return cat

def drawAnimal(animal: list[GraphicsObject], win: GraphWin) -> None:
    # Pre: none
    for part in animal:
        part.draw(win)
    # Post: (side effect) all the GraphicsObjects on the ANIMAL list are drawn

def animalCenter(animal: list[GraphicsObject]) -> Point:
    # Pre:
    assert (len(animal) > 0) and \
        (isinstance(animal[0], Circle) or isinstance(animal[0], Oval) \
            or isinstance(animal[0], Rectangle))
    return cast(Circle, animal[0]).getCenter()
    # Post: return value is a Point at the center of animal[0]

def moveAnimal(animal: list[GraphicsObject], dx: float, dy: float) -> None:
    # Pre: dx and dy need to be something we can add with
    assert (not math.isnan(dx)) and (not math.isnan(dy))
    for part in animal:
        part.move(dx, dy)
    # Post: (side effect)
    # All the items in the ANIMAL list have been moved by (dx, dy)

def main(args: list[str]) -> int:
    # Create and open a window to draw in
    win: GraphWin = GraphWin('Graphics window', 800, 800)
    win.setCoords(-1, -1, 1, 1)

    quitButton: Rectangle = makeButton(Point(-1, 1), Point(-.9, .9), 'Quit', win)

    mouse: list[GraphicsObject] = makeMouse(0.05)
    drawAnimal(mouse, win)

    cat: list[GraphicsObject] = makeCat(0.125)
    moveAnimal(cat, 2, 2) # Put the cat out
    drawAnimal(cat, win)

    label: Text = Text(Point(0, 0.9), 'Mouse click: (none)')
    label.draw(win)

    click: Point = cast(Point, win.getMouse())
    dist: float = 4 # More than the largest dimension of the screen

    while (not inButton(quitButton, click)) and \
        (dist > cat[0].getRadius()):        
        label.setText('Mouse click: Point({0:0.3f}, {1:0.3f})'.format(click.getX(), click.getY()))

        # Mouse jumps to the click
        mousePos: Point = animalCenter(mouse)
        moveAnimal(mouse, click.getX() - mousePos.getX(),
                    click.getY() - mousePos.getY())

        # Cat jumps to where the mouse just was
        catPos: Point = animalCenter(cat)
        moveAnimal(cat, mousePos.getX() - catPos.getX(),
                    mousePos.getY() - catPos.getY())

        # Update dist
        dist = math.dist((mousePos.getX(), mousePos.getY()),
                            (catPos.getX(), catPos.getY()))
        click = cast(Point, win.getMouse())

    # Close the window when clicked on
    #win.getMouse() # Wait for a mouse click
    win.close()

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)