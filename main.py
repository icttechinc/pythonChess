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
    class Board(object):
        def __init__(self,New_Board,Check,Mate,Valid_Move,Is_Checked):
    class Pieces:
        def __init(self,Captured,Capturing,Is_Turn,Is_Available):
        class Rook(object):
                def __init(self,Rmove):
        class Knight(object):
                def __init(self,Nmove):
        class Pawn(object):
                def __init(self,Pmove):
        class Bishop(object):
                def __init(self,Bmove):
        class Queen(object):
                def __init(self,Qmove):
        class King(object):
                def __init(self,Kmove):
elif Start == 2:
    print("Please restart program when ready")
else:
    print("Invalid answer")
