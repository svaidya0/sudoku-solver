class Sudoku:
    def __init__(self, rows):
        self.rows = rows
        
        #Constructs list for easy access of the columns of the sudoku
        cols = []
        for i in range(9):
            col = []
            for row in rows:
                col.append(row[i])
            cols.append(col)
        self.cols = cols

        # Constructs list for easy access of the boxes of the sudoku
        boxes = []
        temp = [0,3,6]
        for m in temp:
            for n in temp:
                box = []
                for j in range(3):
                    for k in range(3):
                        box.append(rows[m+j][n+k])
                boxes.append(box)
        self.boxes = boxes

    def cpy(self):
        # Faster alternative to deepcopy function
        row_copy = [[r for r in row] for row in self.rows]
        return row_copy

def solveSudoku(sudoku):
    numbers = [1,2,3,4,5,6,7,8,9]
    s = Sudoku(sudoku)

    for i in range(9):
        for j in range(9):
            #Finds squares that are empty
            if s.rows[i][j] == 0:
                #Tries all possible numbers from 1 to 9
                for n in numbers:
                    if (n not in s.rows[i]) and (n not in s.cols[j]) and (n not in s.boxes[ 3*int(i/3) + int(j/3) ]):
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

def main():

    print("\nSudoku Solver v1.0 \n \nEnter your sudoku row by row. For blank spaces enter '0'. \n")
    print("Here's an example: \n ")
    print("Enter Row 4: 5 1 0 8 9 6 3 2 0")
    print("\nNow follow the prompts to enter your sudoku: \n")

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
    
    try:
        ans = solveSudoku(grid)
    except:
        print("There was an error trying to solve the sudoku! \n Please check you entered your sudoku correctly, if you are sure you have entered correctly then you may have found a bug! \n Would very much appreciate if you report this to svaidya0 on github along with sudoku you were trying to solve. \n Thank you :) ")

    print("\nSolution: \n")
    for rows in ans:
        print(rows)
    
    print(" \n Thank you for using my Sudoku Solver!")

main()