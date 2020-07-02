import time
import json

# Open the settings json file

with open('Presets.json', 'r') as timers:
    settings_dict = timers.read()

# Load the newly opened settings json file into
# a variable for use as a dictionary

timer_presets = json.loads(settings_dict)

# Define a function called 'countdown' to be a timer
# that takes in an amount of time in seconds and counts
# down to to a stop time which is the amount of seconds
# passed into it plus the current time in seconds.

def countdown(count_time):

    # Get the current time in seconds and create a
    # stop time based on it and the amount of time
    # passed into the function by the user.

    current_time = time.time()
    stop_time = current_time + count_time
    while(time.time() < stop_time):

        # Print the amount of time left in the countdown in seconds
        # rounded to the nearest hundreth.

        print(f'[i] {round(stop_time - time.time(),2)} seconds left...')
        time.sleep(0.1)

    # Notify the user that the timer is done
    # and return them to the start function.

    print('[!] Timer done!')
    start()

# Define a function called 'presethelp' that when called
# prints help on how to use the json settings file
# as well as th rest of this program.

def presethelp():
    print('''
    \tSimple minute timers:
    \t\tEnter a number that will automatically become 
    \t\ta timer of that many minutes.
    \n\tCostom presets:
    \t\tEnter a time into the Timers.json file like so: 
    \t\t\t"name":{
    \t\t\t\t"name":"name", 
    \t\t\t\t"hours":1, 
    \t\t\t\t"minutes":30, 
    \t\t\t\t"seconds":0
    \t\t\t}
    \t\tAll values are needed, this creates a command, name, 
    \t\tthat when entered starts a 1:30:0 timer.
    \n\tEnter "new" to creat a new temporary timer
    \n\tEnter "help" to open this menu
    ''')
    start()

def start():

    # Start a loop to continually ask the user for input
    # until valid input is taken.

    while True:

        # Get user input to use later.

        usr_cmd = input('TIMER: ')

        # Loop through all of the preset dictionaries
        # and check if their name is the same as the 
        # command inputed by the user.

        for cmds in timer_presets['Timers']:
            if usr_cmd.lower() == cmds.lower():

                # Set the countdown equal to the amount of time
                # specified in the preset.

                hours = timer_presets['Timers'][usr_cmd]['hours']
                minutes = timer_presets['Timers'][usr_cmd]['minutes']
                seconds = timer_presets['Timers'][usr_cmd]['seconds']
                count_time = (hours * 60 * 60) + (minutes * 60) + seconds
                countdown(count_time)

        # Check if the user inputed the command to create a new
        # timer and if so allow them to create a new timer.

        if usr_cmd.lower() == 'new':

            # Get input for each unit of time and turn it all
            # to seconds to gie to the countdown function.

            hours = int(input('\tHOURS: '))
            minutes = int(input('\tMINUTES: '))
            seconds = int(input('\tSECONDS: '))
            count_time = (hours * 60 * 60) + (minutes * 60) + seconds
            countdown(count_time)

        # Check if the user entered the help command
        # and if so open help.
        
        elif usr_cmd.lower() == 'help':
            presethelp()

        # Check to see is the user's input was a digit and
        # if so creat a new timer of that many minutes.

        elif usr_cmd.isdigit() == True:

            # Turn the inputted minutes into seconds and
            # pass that through to the countdown function.

            count_time = int(usr_cmd) * 60
            countdown(count_time)

        # If none of the above if and elif statements wer true,
        # then notify the user that their command was invalid
        # and ask them to try again.

        else:
            print('[!] Invalid command...\n[>] Please try again.')

# Start the program by calling the start function

start()