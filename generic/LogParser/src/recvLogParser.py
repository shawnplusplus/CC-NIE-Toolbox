#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""@package string
Copyright (C) 2015 University of Virginia. All rights reserved.

@file      recvLogParser.py
@author    Shawn Chen <sc7cq@virginia.edu>
@version   1.0
@date      June 27, 2015

@section   LICENSE

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation; either version 2 of the License, or（at your option）
any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
more details at http://www.gnu.org/copyleft/gpl.html

@brief     parses log files generated by VCMTPv3 receivers
@usage     python recvLogParser.py <logfile-to-read> <newfile-to-write>
"""


#import re
#import sys
import time
import datetime


# checks if the time elapse is more than 1 minute.
def checkTimeElapse(start, end):
    """Checks if the elapsed time is longer than 1 minute.

    Takes the start time and end time, checks if the elapsed time is longer
    than one minute. If so, returns True. Otherwise, returns False.

    Args:
        start: Start of the time, should be a time struct
        end  : End of the time, should be a time struct

    Returns:
        True : Elapsed time is longer than 1 minute.
        False: Elapsed time is shorter than 1 minute.
    """
    s = datetime.datetime.fromtimestamp(time.mktime(start))
    e = datetime.datetime.fromtimestamp(time.mktime(end))
    over_one_min = (e - s) > datetime.timedelta(minutes = 1)
    return over_one_min


# takes 2 command line arguments, first is log file name, second is new file to
# contain the parsed results.
"""
def main(filename, newfile):
    f = open(filename, 'r')
    w = open(newfile, 'w+')
    # parses the pattern but only takes the number
    sizes = re.findall(r'INFO:\s+(\d+)', f.read())
    for size in sizes:
        w.write(size + '\n')
    f.close()
    w.close()
"""


def main():
    start  = time.strptime("2015-06-26 09:23:05", "%Y-%m-%d %H:%M:%S")
    end    = time.strptime("2015-06-26 09:24:28", "%Y-%m-%d %H:%M:%S")
    status = checkTimeElapse(start, end)
    print "Longer than 1 minute:", status


if __name__ == "__main__":
    #main(sys.argv[1], sys.argv[2])
    main()
