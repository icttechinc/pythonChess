Start = int(input("Start chess game? Answer 1 for yes and 2 for no"))
if Start == 1:
    print("  _____ _____ _____ _____ _____ _____ _____ _____ ")
    print(" |     |     |     |     |     |     |     |     |")
    print("8|  R  |  N  |  B  |  Q  |  K  |  B  |  N  |  R  |")
    print(" |_____|_____|_____|_____|_____|_____|_____|_____|")
    print(" |     |     |     |     |     |     |     |     |")
    print("7|  P  |  P  |  P  |  P  |  P  |  P  |  P  |  P  |")
    print(" |_____|_____|_____|_____|_____|_____|_____|_____|")
    print(" |     |     |     |     |     |     |     |     |")
    print("6|     |     |     |     |     |     |     |     |")
    print(" |_____|_____|_____|_____|_____|_____|_____|_____|")
    print(" |     |     |     |     |     |     |     |     |")
    print("5|     |     |     |     |     |     |     |     |")
    print(" |_____|_____|_____|_____|_____|_____|_____|_____|")
    print(" |     |     |     |     |     |     |     |     |")
    print("4|     |     |     |     |     |     |     |     |")
    print(" |_____|_____|_____|_____|_____|_____|_____|_____|")
    print(" |     |     |     |     |     |     |     |     |")
    print("3|     |     |     |     |     |     |     |     |")
    print(" |_____|_____|_____|_____|_____|_____|_____|_____|")
    print(" |     |     |     |     |     |     |     |     |")
    print("7|  P  |  P  |  P  |  P  |  P  |  P  |  P  |  P  |")
    print(" |_____|_____|_____|_____|_____|_____|_____|_____|")
    print(" |     |     |     |     |     |     |     |     |")
    print("8|  R  |  N  |  B  |  Q  |  K  |  B  |  N  |  R  |")
    print(" |_____|_____|_____|_____|_____|_____|_____|_____|")
    print("    a     b     c     d     e     f     g     h   ")
    class Board(object):                                                                #Board Code
        def __init__(self,nb,c,m,vm,ic):
    	    self.New_Board = nb
            self.Check = c
            self.Mate = m
            self.Valid_Move = vm
            self.Is_Checked = ic
    class Pieces:                                                                       #Pieces General Code
        def __init__ (self,ca,t,it,ia,b, m):
            self.captured = ca
            self.take = t
            self.Is_Turn = it
            self.Is_Available = ia
            self.block = b
            self.move = m
            if m == True:
                ia = False
                it = False
                b = False
                t = False
                c = False
                m = False
                print("Game Over")
            if c == True:
                if b == True:
                    ia = True
                if t == True:
                    ia = True
        class Rook(object):                                                             #Rook Code
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
        class Knight(object):                                                          #Knight Code
                def __init__ (self,c,x,y):
                    self.color = c
                    self.alive = True
                    self.x = x
                    self.y = y
               def move(self, dirx, diry):
                    if validMove(dirx,diry):
                        self.x= dirx
                        self.y= diry
        class Pawn(object):                                                             #Pawn Code
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
        class Bishop(object):                                                           #Bishop Code
                def __init__ (self,c,x,y):
                    self.color = c
                    self.alive = True
                    self.x = x
                    self.y = y
               def move(self, dirx, diry):
                    if validMove(dirx,diry):
                        self.x= dirx
                        self.y= diry
        class Queen(object):                                                            #Queen Code
                def __init__ (self,c,x,y):
                    self.color = c
                    self.alive = True
                    self.x = x
                    self.y = y
               def move(self, dirx, diry):
                    if validMove(dirx,diry):
                        self.x= dirx
                        self.y= diry
        class King(object):                                                             #King Code
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
