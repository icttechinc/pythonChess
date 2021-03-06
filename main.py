Start = int(input("Start chess game? Answer 1 for yes and 2 for no"))
if Start == 1:
    print("  _____________ _____________ _____________ _____________ _____________ _____________ _____________ _____________ ")
    print(" |             |             |             |             |             |             |             |             |")
    print(" |             |             |             |             |             |             |             |             |") 
    print("8|      R      |      N      |      B      |      Q      |      K      |      B      |      N      |      R      |")
    print(" |             |             |             |             |             |             |             |             |")
    print(" |_____________|_____________|_____________|_____________|_____________|_____________|_____________|_____________|")
    print(" |             |             |             |             |             |             |             |             |")
    print(" |             |             |             |             |             |             |             |             |") 
    print("7|      P      |      P      |      P      |      P      |      P      |      P      |      P      |      P      |")
    print(" |             |             |             |             |             |             |             |             |")
    print(" |_____________|_____________|_____________|_____________|_____________|_____________|_____________|_____________|")
    print(" |             |             |             |             |             |             |             |             |")
    print(" |             |             |             |             |             |             |             |             |") 
    print("6|             |             |             |             |             |             |             |             |")
    print(" |             |             |             |             |             |             |             |             |")
    print(" |_____________|_____________|_____________|_____________|_____________|_____________|_____________|_____________|")
    print(" |             |             |             |             |             |             |             |             |")
    print(" |             |             |             |             |             |             |             |             |") 
    print("5|             |             |             |             |             |             |             |             |")
    print(" |             |             |             |             |             |             |             |             |")
    print(" |_____________|_____________|_____________|_____________|_____________|_____________|_____________|_____________|")
    print(" |             |             |             |             |             |             |             |             |")
    print(" |             |             |             |             |             |             |             |             |") 
    print("4|             |             |             |             |             |             |             |             |")
    print(" |             |             |             |             |             |             |             |             |")
    print(" |_____________|_____________|_____________|_____________|_____________|_____________|_____________|_____________|")
    print(" |             |             |             |             |             |             |             |             |")
    print(" |             |             |             |             |             |             |             |             |") 
    print("3|             |             |             |             |             |             |             |             |")
    print(" |             |             |             |             |             |             |             |             |")
    print(" |_____________|_____________|_____________|_____________|_____________|_____________|_____________|_____________|")
    print(" |             |             |             |             |             |             |             |             |")
    print(" |             |             |             |             |             |             |             |             |") 
    print("2|      P      |      P      |      P      |      P      |      P      |      P      |      P      |      P      |")
    print(" |             |             |             |             |             |             |             |             |")
    print(" |_____________|_____________|_____________|_____________|_____________|_____________|_____________|_____________|")
    print(" |             |             |             |             |             |             |             |             |")
    print(" |             |             |             |             |             |             |             |             |") 
    print("8|      R      |      N      |      B      |      Q      |      K      |      B      |      N      |      R      |")
    print(" |             |             |             |             |             |             |             |             |")
    print(" |_____________|_____________|_____________|_____________|_____________|_____________|_____________|_____________|")
    print("       a              b             c             d             e             f             g             h       ")
    class Board(object):                                                                    #Board Code
        def __init__(self,nb,ch,ma,vm,ic):
    	    self.New_Board = nb
            self.Check = ch
            self.Mate = ma
            self.Valid_Move = vm                    #Special Effects Could Be Added Here (Invaled Move)(Sound, Appereance, etc...)
            self.Is_Checked = ic
    class Pieces:                                                                           #Pieces General Code
        def __init__ (self,ca,ta,it,ia,bl,mo):
            self.captured = ca
            self.take = ta
            self.Is_Turn = it
            self.Is_Available = ia
            self.block = bl
            self.move = mo
            if ma == True:                          #Special Effects Could Be Added Here (Sound, Appereance, etc...)
                ia = False
                it = False
                bl = False
                ta = False
                ca = False
                mo = False
                print("Game Over")
            if ch == True:                          #Special Effects Could Be Added Here (Sound, Appereance, etc...)
                if bl == True:
                    ia = True
                if ta == True:
                    ia = True
            if nb == True:                          #Special Effects Could Be Added Here (Sound, Appereance, etc...)
                ta = False
                bl = False
                ca = False
                ia = True
                mo = True
        class Rook(object):                                                                 #Rook Code
                def __init__ (self,c,x,y):
                    self.color = c
                    self.alive = True
                    self.firstMove = True
                    self.x = x
                    self.y = y
                    if ca == True:
                        self.alive = False
               def move(self, dirx, diry):
                    if validMove(dirx,diry):
                        self.x= dirx
                        self.y= diry
        class Knight(object):                                                             #Knight Code
                def __init__ (self,c,x,y):
                    self.color = c
                    self.alive = True
                    self.x = x
                    self.y = y
                    if ca == True:
                        self.alive = False
               def move(self, dirx, diry):
                    if validMove(dirx,diry):
                        self.x= dirx
                        self.y= diry
        class Pawn(object):                                                               #Pawn Code
                def __init__ (self,c,x,y):
                    self.color = c
                    self.alive = True
                    self.firstMove = True
                    if self.firstMove == True:
                        self.enpassant = True
                    self.x = x
                    self.y = y
                    if ca == True:
                        self.alive = False
               def move(self, dirx, diry):
                    if validMove(dirx,diry):
                        self.x= dirx
                        self.y= diry
        class Bishop(object):                                                             #Bishop Code
                def __init__ (self,c,x,y):
                    self.color = c
                    self.alive = True
                    self.x = x
                    self.y = y
                    if ca == True:
                        self.alive = False
               def move(self, dirx, diry):
                    if validMove(dirx,diry):
                        self.x= dirx
                        self.y= diry
        class Queen(object):                                                                #Queen Code
                def __init__ (self,c,x,y):
                    self.color = c
                    self.alive = True
                    self.x = x
                    self.y = y
                    if ca == True:
                        self.alive = False
               def move(self, dirx, diry):
                    if validMove(dirx,diry):
                        self.x= dirx
                        self.y= diry
        class King(object):                                                                #King Code
                def __init__ (self,c,x,y):
                    self.color = c
                    self.alive = True
                    self.firstMove = True
                    self.x = x
                    self.y = y
               def move(self, dirx, diry):
                    if validMove(dirx,diry):
                        self.x= dirx
                        self.y= diry
elif Start == 2:
    print("Please restart program when ready")
else:
    print("Invalid answer")
