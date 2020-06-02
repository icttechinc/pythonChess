Start = int(input("Start chess game? Answer 1 for yes and 2 for no"))
if Start == 1:
    print("  ___ ___ ___ ___ ___ ___ ___ ___ ")
    print(" |   |   |   |   |   |   |   |   |")
    print("8| R | N | B | Q | K | B | N | R |")
    print(" |___|___|___|___|___|___|___|___|")
    print(" |   |   |   |   |   |   |   |   |")
    print("7| P | P | P | P | P | P | P | P |")
    print(" |___|___|___|___|___|___|___|___|")
    print(" |   |   |   |   |   |   |   |   |")
    print("6|   |   |   |   |   |   |   |   |")
    print(" |___|___|___|___|___|___|___|___|")
    print(" |   |   |   |   |   |   |   |   |")
    print("5|   |   |   |   |   |   |   |   |")
    print(" |___|___|___|___|___|___|___|___|")
    print(" |   |   |   |   |   |   |   |   |")
    print("4|   |   |   |   |   |   |   |   |")
    print(" |___|___|___|___|___|___|___|___|")
    print(" |   |   |   |   |   |   |   |   |")
    print("3|   |   |   |   |   |   |   |   |")
    print(" |___|___|___|___|___|___|___|___|")
    print(" |   |   |   |   |   |   |   |   |")
    print("2| P | P | P | P | P | P | P | P |")
    print(" |___|___|___|___|___|___|___|___|")
    print(" |   |   |   |   |   |   |   |   |")
    print("1| R | N | B | Q | K | B | N | R |")
    print(" |___|___|___|___|___|___|___|___|")
    print("   A   B   C   D   E   F   G   H  ")
    #The timer class and sound effect class will be added later
    #Special effects will also be added later
    class Board(object):                                                                #Board Code
        def __init__(self,nb,c,m,vm,ic):
    	   	self.New_Board = nb
            self.Check = c
            self.Mate = m
            self.Valid_Move = vm
            self.Is_Checked = ic
    class Pieces:                                                                       #Pieces General Code
        def __init__ (self,c,t,it,ia):
            self.captured = c
            self.take = t
            self.Is_Turn = it
            self.Is_Available = ia
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
                    self.firstMove = True
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
                    self.firstMove = True
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
                    self.firstMove = True
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
