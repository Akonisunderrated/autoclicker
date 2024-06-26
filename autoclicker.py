# AutoClicker V1.2 
# Last Updated: 05/June/2024
# Jorgen Eilertsen
# https://github.com/Akonisunderrated

import pyautogui
import time
from datetime import datetime

# Main clicker function. 
# Will click where ever the mouse pointer is. 
# Once every 1 minute for the amount of hours given.
def clicker(x):
    
    print('Countdown')
    print('5')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('Clicking')

    c = 0
    while c < x*60:
        pyautogui.click()
        c += 1
        
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print(c, ' at ', current_time)
        time.sleep(60)
    print('done at ', current_time)

# Simple run routine to allow for input to control hours runtime.
def run_routine():
    click_run_length_hours = float(input('Please input amount of hours to run : '))
    clicker(click_run_length_hours)
    rerun = input('run again? (y/n)')
    if rerun.lower() == 'n':
        return False
    elif rerun.lower() == 'y':
        return True
    else:
        raise ValueError('Unexpected answer. Please answer y or n')    


# Will only run if run as main script
if __name__ == '__main__':
    run=True
    while run:
        run = run_routine()