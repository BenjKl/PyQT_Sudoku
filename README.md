## PyQT_Sudoku
This is python program to solve sudoku puzzles with a GUI written in python+PyQt6.
Features:
* Numbers can be entered in GUI. 
    * Change active cell with cursor keys. 
    * Enter numbers or `Backspace` or zero to delete
    * Use "L" to lock fixed numbers
* Locked numbers are shown in bold (Not changed during reset)
* Wrong numbers are shown in red
* Allowed numbers based on the rules (row, column and block) are shown as small numbers
* *Candidates* (Unambiguous entries by looking at the allowed numbers for current row, column or block) are shown in blue (if selected in GUI)
* Undo/Redo stack (`Cmd+Z`, `Shift-Cmd+Z` on Mac)
* Generation shows number of *steps* during manual entry or iterations for the solver
* *Lock* fixes the entered numbers, so they are not deleted during reset
* *Step* Fill currently shown unambiguous candidates (if any).
* *Iterate* recursively fills all unambiguous candidates (if any)
* *Solve* solves the puzzle using a recursive algorithm (also explained here: [Youtube, Python Sudoku Solver - Computerphile](https://www.youtube.com/watch?v=G_UYXzGuqvM))
* *Reset* deletes all numbers which are not locked.
* *Next solution* cycles between solutions found by the recursive solver
* *Diagonal rule* activates the optional rule that in addition to the standard rules, numbers 1-9 are only allowed once in the two diagonals.
* *Show candidate* Activates candidates display in the grid (in blue)
* Puzzles can be saved/opened as .dat in json format

![Screenhot](https://github.com/BenjKl/PyQt_Sudoku/blob/main/screenshot.png?raw=true)

