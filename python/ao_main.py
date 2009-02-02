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

import time
import Aspyct

temperature = 0.0

def setTemperature(t):
    global temperature
    temperature = t
    
def adviceIn(cd):
    global temperature
    print "Temperature was %f" % temperature
    
def adviceOut(cd):
    global temperature
    print "Temperature changed to %f" % temperature
    
Aspyct.atCall(setTemperature, adviceIn)
Aspyct.atReturn(setTemperature, adviceOut)

while True:
    ret = raw_input("Enter new temperature (x to exit): ")
    if ret == "x":
        quit()
        
    setTemperature(float(ret))
        
