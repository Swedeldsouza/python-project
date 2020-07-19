#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import winsound
# Import Module
import os
#
# Here, I am Using Ubuntu
# that's why current function is working for me
# but if you are using any other operating system
# then, you need to customize below function as 
# your operating system supports.
#
# Check This Links
#
# http://askubuntu.com/questions/19906/beep-in-shell-script-not-working
# http://stackoverflow.com/questions/6537481/python-making-a-beep-noise
# http://stackoverflow.com/questions/16573051/python-sound-alarm-when-code-finishes
#
#
# Beep Creating Function
import winsound
import os
def beep(sec):
    frequency = 1500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


# Trigger Function
if __name__ == '__main__':
	beep(5)
