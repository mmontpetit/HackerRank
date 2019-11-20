import time

# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

def timeConversion(s):
    strt = time.strptime(s, '%I:%M:%S%p')
    return time.strftime('%H:%M:%S', strt)
    