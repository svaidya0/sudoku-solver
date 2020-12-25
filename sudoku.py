class Sudoku:
    def __init__(self, rows):
        self.rows = rows

    def cols(self, n):
        # Method for fast access of the columns of the sudoku
        col = [self.rows[i][n] for i in range(9)]
        return col

    def box(self, a, b):
        # Method for fast access of the boxes of the sudoku
        m = a - a%3
        n = b - b%3

        box = list()
        for j in range(3):
            for k in range(3):
                box.append(self.rows[m+j][n+k])
        
        return box

    def cpy(self):
        # Faster alternative to deepcopy function
        row_copy = [[r for r in row] for row in self.rows]
        return row_copy

    # Method to check inital entry
    def correctEntry(self):
        numbers = [1,2,3,4,5,6,7,8,9]
        for j in range(9):
            if not all([(self.rows[j]).count(i) < 2 for i in numbers]): return False
            elif not all([(self.cols(j)).count(i) < 2 for i in numbers]): return False 
            elif not all([( self.box( j, (j*3)%9 ) ).count(i) < 2 for i in numbers]): return False
            else: continue
        return True

    # Checks whether sudoku solution is correct
    def isCorrect(self):
        numbers = [1,2,3,4,5,6,7,8,9]
        for j in range(9):
            if not all([i in self.rows[j] for i in numbers]): return False
            elif not all([i in self.cols(j) for i in numbers]): return False
            elif not all([i in self.box( j, (j*3)%9 ) for i in numbers]): return False
            else: continue
        return True

def solveSudoku(sudoku):
    numbers = [1,2,3,4,5,6,7,8,9]
    s = Sudoku(sudoku)

    for i in range(9):
        for j in range(9):
            #Finds squares that are empty
            if s.rows[i][j] == 0:
                #Tries all possible numbers from 1 to 9
                for n in numbers:
                    if (n not in s.rows[i]) and (n not in s.cols(j)) and (n not in s.box(i,j)):
                        try:
                            temp = Sudoku(s.cpy())
                            temp.rows[i][j] = n
                            s = Sudoku(solveSudoku(temp.rows))
                        except:
                            del temp
                            #Goes on to try the next number
                            continue
                
                #If none of the numbers from 1 to 9 work then something is wrong so algorithm backtracks
                if s.rows[i][j] == 0:
                    raise Exception
    
    #At this point all squares should be filled
    return s.rows

def userInput():
    
    grid = list()
    numbers = range(10)

    for i in range(9):
        # Loop to restart current iteration in case of problem with input
        while True:
            try:
                row = input("Enter Row "  + str(i+1) + ": ").split()
                
                # Checks than the input had 9 entries
                if len(row) != 9: raise Exception
                
                # Turns inputs into integers and makes sure all integers are within bounds
                for j in range(9):
                    row[j] = int(row[j])
                    if row[j] not in numbers:
                        raise Exception
                grid.append(row)
                break
            
            except:
                print("ERROR: Please try again")
                pass
    
    # Checks that input is correct
    test = Sudoku(grid)
    if not test.correctEntry():
        print("\nLooks like your input is incorrect! Please try again:\n")
        grid = userInput()
    del test
    
    return grid

def main():

    print("\nSudoku Solver v0.3.0 \n \nEnter your sudoku row by row. For blank spaces enter '0'. \n")
    print("Here's an example: \n ")
    print("Enter Row 4: 5 1 0 8 9 6 3 2 0")
    print("\nNow follow the prompts to enter your sudoku: \n")

    print("Checking your input\n")
    grid = userInput()

    try:
        print("\nSolving your sudoku")
        ans = solveSudoku(grid)
        
        print("\nSolution: \n")
        for rows in ans:
            print(rows)
        
        a = Sudoku(ans)
        if not a.isCorrect():
            print("Sorry, this solution is not correct! \nPlease check you entered your sudoku correctly, if you are sure you have entered correctly then you may have found a bug! \n You can report this to svaidya0 on github along with sudoku you were trying to solve. \nThank you :)")
        else:
            print("\nThank you for using my Sudoku Solver!")
    except:
        print("There was an error trying to solve the sudoku! \nPlease check you entered your sudoku correctly, if you are sure you have entered correctly then you may have found a bug! \n Would very much appreciate if you report this to svaidya0 on github along with sudoku you were trying to solve. \n Thank you :) ")

main()