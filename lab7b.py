#!/usr/bin/env python3
# Student ID: clee259

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    sum = Time(0,0,0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    #[ insert python code here to check for minute and second 
    if sum.second > 59: # if second exceeds 60, add a value of one to minute then takeaway 60 from second
        sum.minute = sum.minute + 1
        sum.second = sum.second - 60
    #[ attribute here, and carry over when necessary
    if sum.minute > 59: # same as "if sum.secound > 59:", but in terms of hour
        sum.hour = sum.hour + 1
        sum.minute = sum.minute - 60
    return sum

def change_time(time, seconds):
    time.second += seconds
    if valid_time(time) != True:
        while time.second >= 60:
             time.second -= 60
             time.minute +=1
        while time.second < 0: # takeaway one minute and add 60 seconds if time.second is less than 0
            time.second += 60
            time.minute -= 1
        while time.minute >= 60:
             time.minute -= 60
             time.hour += 1
        while time.minute < 0: # takway one hour and add 60 minutes if time.minute is less than 0
            time.minute += 60
            time.hour -= 1
        ''' irrelevant as day parameter is absent...
        while time.hour >= 24:
            time.hour -= 24
        while time.hour < 0:
            time.hour += 24
        '''
    return None

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
