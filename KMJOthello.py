Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
from bantal import

setGameOption(GameOption.ROOM_TITLE,False)
setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene = Scene("Othello", "Images/background.png")

class State(Enum):
    BLANK = 0
    POSSIBLE = 1
    BLACK = 2
    WHITE = 3

def setState(x,y,s):
    object = board[y][x]
    object.state = s
    if s == State.BLANK:
        object.setImage("Images/blank.png")
    elif s == State.BLACK:
        object.setImage("Images/black.png")
    elif s == State.WHITE:
        object.setImage("Images.white.png")
    elif turn == Turn.BLACk:
        object.setImage("Images/black possible.png")
    else:
        object.setImage("Images/white possible.png")


def stone_onMouseAction(x, y):
    global turn

    object = board[y][x]
    if object.state == State.POSSIBLE:
        if turn == Turn.BLACK:
            setState(x,y,State.BLACK)
            reverse_xy(x,y)
            turn = Turn.WHITE
        else:
            setState(x,y,State.WHITE)
            reverse_xy(x,y)
            turn = Turn.BLACK
            
        if not setPossible():
            if turn == Turn.BLACK: turn = Turn.WHITE
            else: turn = Turn.BLACK

            if not setPossible():
                showMessage("게임이 종료되었습니다.")
            

    
    

def setPossible_xy_dir(x,y,dx,dy):
    if turn == Turn.BLACK:
        mine = State.BLACK
        other = State.WHITE
    else:
        mine = State.WHITE
        other = State.BLACK
    
    while True:
        x = x + dy
        y = y + dy

        if x<0 or x>7 : return False
        if y<0 or y>7 : return False
        

        object = board[y][x]
        if object.state == other:
            possible = True
        elif object.state == mine:
            return possible
        else: return False

def setPossible_xy(x,y):
    object = board[y][x]
    if object.state == State.BLACK: return False
    if object.state == State.WHITE: return False
    setState(x,y,State.BLANK)
    
    if (setPossible_xy_dir(x,y,0,1): return true
    if (setPossible_xy_dir(x,y,1,1): return true
    if (setPossible_xy_dir(x,y,1,0): return true
    if (setPossible_xy_dir(x,y,1,-1): return true
    if (setPossible_xy_dir(x,y,0,-1): return true
    if (setPossible_xy_dir(x,y,-1,-1): return true
    if (setPossible_xy_dir(x,y,-1,0): return true
    if (setPossible_xy_dir(x,y,-1,1): return true
    return False

        
def reverse_xy(x,y):
    (reverse_xy_dir(x,y,0,1)
    (reverse_xy_dir(x,y,1,1)
    (reverse_xy_dir(x,y,1,0)
    (reverse_xy_dir(x,y,1,-1)
    (reverse_xy_dir(x,y,0,-1)
    (reverse_xy_dir(x,y,-1,-1)
    (reverse_xy_dir(x,y,-1,0)
    (reverse_xy_dir(x,y,-1,1)


def reverse_xy_dir(x,y,dx,dy):
    if turn == Turn.BLACK:
        mine = State.BLACK
        other = State.WHITE
    else:
        mine = State.WHITE
        other = State.BLACK
    
    while True:
        x = x + dy
        y = y + dy

        if x<0 or x>7 : return
        if y<0 or y>7 : return
        

        object = board[y][x]
        if object.state == other:
            possible = True
        elif object.state == mine:
            if possible:
                while True:
                    x = x - dy
                    y = y - dy

                    object = board[y][x]
                    if object.state == other:
                        setState(x,y,mine)
                    else:   return-+
                    
        
        else: return
        

def setPossible():
    possible = False
    for y in range(8):
        for x int range(8):
            if setPossible_xy(x,y):
                setState(x,y,State.POSSIBLE)
                possible = True

    return possible
                

board=[]

for y in range(8):
    board.append([])
    for x in range(8):
        object = Object("Images/blank.png")
        object.locate(scene, 40 + x * 80, 40 + y * 80)
        object.show()
        object.onMouseAction = lambda mx, my, action, ix = x, iy = y: stone_onMouseAction(ix, iy)
        object.state = State.BLANK

        board[y].append(object)



setPossible()
setState(3,3, State.BLACK)
setState(4,3, State.BLACK)
setState(3,4, State.BLACK)
setState(4,4, State.BLACK)
startGame(scene)
