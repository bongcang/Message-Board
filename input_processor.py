# input_processor.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# CONG-BANG TA
# CONGBANT@UCI.EDU
# 76664411
import ds_protocol as dsp


def Process():

    try:
        '''
        Checks the first letter for the command type and based on what the command is, will parse slightly differently
        If the first letter doesn't match any of the commands, throws an error
        '''
        userInput = input()

        command = userInput[0] #command is the first letter

        if command == "Q" or command == "q":
            command = dsp.QUIT
            return command, None

        elif command == "J" or command == "j":
            command = dsp.JOIN
            login_info = []
            userInput = userInput[3:]
            login_info.append(userInput[userInput.index(' ') + 1:userInput.index('-') - 1])
            userInput = userInput[userInput.index('-'):]
            login_info.append(userInput[userInput.index(' ') + 1:])
            return command, login_info

        elif command == "P" or command == "p":
            command = dsp.POST
            userInput = userInput[2:]
            return command, userInput

        elif command == "B" or command == "b":
            command = dsp.BIO
            userInput = userInput[2:]
            return command, userInput

        elif command == "L" or command == "l":
            command = dsp.LOCATION
            location = []
            userInput = userInput[3:]
            location.append(userInput[userInput.index(' ') + 1:userInput.index('-') - 1])
            userInput = userInput[userInput.index('-'):]
            location.append(userInput[userInput.index(' ') + 1:])

            return command, location

        elif command == "S" or command == "s":
            command = dsp.SONG
            track_data = []
            userInput = userInput[3:]
            track_data.append(userInput[userInput.index(' ') + 1:userInput.index('-') - 1])
            userInput = userInput[userInput.index('-'):]
            track_data.append(userInput[userInput.index(' ') + 1:])

            return command, track_data

    except ValueError:
        return dsp.ERROR, None
