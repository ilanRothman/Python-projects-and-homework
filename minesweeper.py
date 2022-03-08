"""
Student: Ilan Rothman
ID: 322061565
Assignment no. 6
Program: minesweeper.py
"""
import random
class MSSquare:
    """class for representing the squares in the board game"""
    def __init__(self,has_mine,hidden,neighbor_mines = 0):
        """
        Constructing the class

        Parameters
        ----------
        has_mine : Bool
            If square has a mine it will be True. else False
        hidden : Bool
            if square is hidden it will be True. else False
        neighbor_mines : int, optional
            The default is 0. will be added accordingly.
        Returns
        -------
        None.

        """
        self.__has_mine = has_mine
        self.__hidden = hidden
        self.__neighbor_mines = neighbor_mines
        
    @property
    def has_mine(self):
        """return True if is assigned to have a mine"""
        return self.__has_mine
        
    @has_mine.setter
    def has_mine(self, boolian):
        """if assgined for having a mine changes to True"""
        self.__has_mine = boolian
    @property
    def IsHidden(self):
        """return if Hidden or not"""
        return self.__hidden # True if hidden
    @IsHidden.setter
    def IsHidden(self,boolian):
        """if chosen to become visable turns hidden to False"""
        self.__hidden = boolian #now not hidden
    @property
    def NeighborMines(self):
        """return amount of neighbor mines"""
        return self.__neighbor_mines
    @NeighborMines.setter
    def NeighborMines(self,num):
        """when chosent to become visable will be assigned to amount of neighbour mines"""
        self.__neighbor_mines = num
        
        
def check_loose(square_lst):
    """If game is lost return True, False otherwise"""
    for row in square_lst:
        for square in row:
            if square.has_mine and not square.IsHidden:
                print("Sorry, you stepped on a mine, you Lost :(")
                return True
    return False

def check_win(square_lst):
    """if game is won return True, False otherwise"""
    win = True
    remaining = 0
    for row in square_lst:
        for square in row:
            if square.has_mine == False and square.IsHidden:
                remaining +=1
    if remaining > 0:
        win = False
        print(f"You have {remaining} squares left to find! good luck!")
    else:
        print("You Win!")
    return win
            
def create_mines(num,square_lst):
    """adding the mines to the board"""
    pairLst = []
    for pair in range(num):
        Done = False
        while not Done:
            x = random.randint(0,len(square_lst)-1)
            y = random.randint(0,len(square_lst)-1)
            if (x,y) not in pairLst:
                pairLst.append((x,y))
                Done = True
        for coordinate in pairLst: #setting the chosen squares to have a mine.
            square_lst[coordinate[0]][coordinate[1]].has_mine = True
            

def how_many_neighbormines(square_lst,row,col):
    """sets the amount of neighbor mines for the square"""
    counter = 0
    for i in range(row-1,row+2):
        for j in range(col-1,col+2 ):
            try:
                if square_lst[i][j].has_mine:
                    if i>=0 and j>=0: #making sure it's not on opsite side of board
                        counter +=1
            except IndexError:
                continue
    square_lst[row][col].NeighborMines = counter # setting
        
def set_board(square_lst):
    """prints opening board"""
    print("  "+"+---"*len(square_lst)+"+")
    for i in range(len(square_lst)):
        print(i+1,"|   "*len(square_lst)+"|")
        print("  "+"+---"*len(square_lst)+"+")
    return("    "+"   ".join([str(i+1) for i in range(len(square_lst))]))


def recsquare(board,row,col,lst):
    """recursive function to open squaers which have 0 neighbors"""
    if board[row][col].NeighborMines >=1:
        return 
    for i in range(row-1,row+2): # looping through all the neighbors
        for j in range(col-1,col+2 ):
                try:
                    if i>=0 and j>=0:
                        if board[i][j] not in lst: #not to check same square twice.
                            lst.append(board[i][j])
                            how_many_neighbormines(board,i,j)
                            board[i][j].IsHidden = False
                            recsquare(board,i,j,lst)
                except IndexError:
                    continue
        
def prntUpdatedBoard(square_lst,row,col):
    """prints updated board after every turn"""
    if square_lst[row][col].has_mine: #loosing option
        for r in square_lst:
            for square in r:
                if square.has_mine: # revieling mines
                    square.IsHidden = False 
    else: # not a mine
        square_lst[row][col].IsHidden = False             
        how_many_neighbormines(square_lst,row,col)
    if square_lst[row][col].NeighborMines == 0 and square_lst[row][col].has_mine == False: #recursive option
        recsquare(square_lst,row,col,[])
    row_count = 1
    print("  "+"+---"*len(square_lst)+"+") #top row
    for r in square_lst:
        print(row_count, end = " ")
        for square in r: # checking if hidden/has_mine/not hidden.
            if square.IsHidden:
                print("|   ",end = "")
            elif square.has_mine:
                print("| X ",end = "" )
            else:
                print(f"| {square.NeighborMines} ",end = "" )
        row_count+=1
        print("|")
        print("  "+"+---"*len(square_lst)+"+")
    print("    "+"   ".join([str(i+1) for i in range(len(square_lst))]))

        
        
def Make_board(x):
    """makes the game board"""
    square_lst = [[MSSquare(False,True) for col in range(x)]for row in range(x)]
    return square_lst

def main():
    """mindesqweeper game """
    print("Welcome to Minesweeper!")
    accepting = True
    while accepting:#accepting Board size
        try:
            Board_size = int(input("Please enter game board size between 4 and 9 (x): "))
            if Board_size > 9 or Board_size < 4:
                raise IndexError
            else: accepting = False
        except ValueError:
            print("Please enter an integer")
        except IndexError:
            print("Board size must be inbetween 4 and 9")
    accepting = True
    while accepting: #accepting number of mines.
        try:
            num_mines = int(input(f"Please choose the amount of mines(no more then {Board_size*2} and atleast 1):"))
        except ValueError:
            print("Please enter an integer")
        if type(num_mines) == int and num_mines > Board_size*2 or num_mines <=0 :
            print("Please enter correct amount of mines")
        else:
            accepting = False
        
    square_lst = Make_board(Board_size) #creating board
    create_mines(num_mines, square_lst) #creating mines
    print(set_board(square_lst))
    while check_loose(square_lst) == False  and check_win(square_lst)==False :
        try:
            x,y = input("Please enter the square coordinates to reveal with ',' separator (x,y): ").split(",")
            if int(x) > Board_size or int(y) > Board_size:
                raise IndexError
            prntUpdatedBoard(square_lst, int(y)-1, int(x)-1)
        except ValueError:
            print("Please enter two integers")
        except IndexError:
            print("Please enter coordinates in board range")
        
main()


        

        