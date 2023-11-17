# Tic-Tac-Toe
Tic-Tac-Toe

This is a small Python game resembling the popular Tic-Tac-Toe game. 

It was built in Python and the GUI was done using the <Tkinter> module. The whole code is written in a simple manner which makes it easy to understand and read even for somebody who has never coded before.

Enough with the talking, go on and look at my small interactive game:)

## Create Standalone Executable

pip install pyinstaller
cd Desktop
pyinstaller --onefile --windowed --icon=icontictactoe.ico tictactoe.py

"""
!!using command prompt!!
=> --onefile because we only want one executable
=> --windowed because we don`t want a console to be opened
=> icontictactoe.ico is our desired icon for the final executable, which must be in the same location as the tictactoe.py is, and it must be in an ico/exe format
"""
