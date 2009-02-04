## aspyctGAME ##
#
# Test the Aspyct module in the context of a small game
# Copyright (C) 2008,2009  Philippe Chretien
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# You will find the latest version of this code at the following address:
# http://github.com/pchretien
#
# You can contact me at the following email address:
# philippe.chretien@gmail.com

import Aspyct

class Position:
    x = 0
    y = 0
    
position = Position()
board = [[0,0,0],[0,1,0],[0,0,0]]

def up():
    global position
    position.y = position.y - 1
    
def down():
    global position
    position.y = position.y + 1
    
def left():
    global position
    position.x = position.x - 1
    
def right():
    global position
    position.x = position.x + 1


def callUp(cd):
    global position, board    
    if position.y == 0:
        return True
    
def callDown(cd):
    global position, board
    if position.y == len(board)-1:
        return True
    
def callLeft(cd):
    global position, board
    if position.x == 0:
        return True
    
def callRight(cd):
    global position, board
    if position.x == len(board[0])-1:
        return True
    
def returnMove(cd):
    global position, board    
    if board[position.y][position.x] == 1:
        print "Boum!"
        quit()
    else:
        print "Ouf :)"
        
def avoidMove(cd):
    print "Invalid move!"
    
def exitMove(cd):
    print "( %d, %d)" % (position.x, position.y)
    print board
             
    
Aspyct.atCall(up, callUp)
Aspyct.atCall(down, callDown)
Aspyct.atCall(left, callLeft)
Aspyct.atCall(right, callRight)

Aspyct.atReturn(up, returnMove)
Aspyct.atReturn(down, returnMove)
Aspyct.atReturn(left, returnMove)
Aspyct.atReturn(right, returnMove)

Aspyct.atAvoid(up, avoidMove)
Aspyct.atAvoid(down, avoidMove)
Aspyct.atAvoid(left, avoidMove)
Aspyct.atAvoid(right, avoidMove)

Aspyct.atExit(up, exitMove)
Aspyct.atExit(down, exitMove)
Aspyct.atExit(left, exitMove)
Aspyct.atExit(right, exitMove)

while True:
    dir = raw_input("Where do you want to go today?  ")
    dir = dir.strip().lower()
    if dir == "exit":
        quit()
        
    if dir == "help":
        print "COMMAND   DESCRIPTION"
        print "up        Move one tile up."
        print "down      Move one tile down."
        print "left      Move one tile left."
        print "right     Move one tile right."
        print "exit      Exit the program."
        print "help      Display this help."
        
    if dir == "up":
        up()
    if dir == "down":
        down()
    if dir == "left":
        left()
    if dir == "right":
        right()
        
