# a4.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# CONG-BANG TA
# CONGBANT@UCI.EDU
# 76664411

import socket, input_processor
from OpenWeather import *
from LastFM import *
import ds_client as dsc
import ds_protocol as dsp
from ds_protocol import DSPProtocolError


def main() -> None:
    print("Hello! To start, please join by logging in or creating a profile by using the 'J' command and typing out your username and password.")
    print('Example: J -usr (username here) -pwd (password here)')

    HOST = "168.235.86.101"
    PORT = 3021
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    _dsp_conn = dsc.init(sock)
    openweather_apikey = '1bfa77f2ca7052bf2e2fb1ce35f4c644'
    lastfm_apikey = '80dba62e72a066fcd1c0ff02b6c8642e'

    try:
        while True:
            '''
            Gets user input to log into the server and lets the user know if it didn't work
            '''
            try:
                input = input_processor.Process()

                command = input[0]

                if command == "QUIT":
                    dsc.disconnect(_dsp_conn)
                    sock.close()
                    quit()

                elif command == dsp.ERROR:
                    print("Please enter a valid command.")

                elif command == dsp.JOIN:
                    username = input[1][0]
                    password = input[1][1]
                    res = dsc.join(_dsp_conn, username, password)
                    if res[0] == dsp.JOINED:
                        user = dsp.profile(HOST, username, password)
                        print(res[1])
                        break
                    else:
                        print(res[1])

                else:
                    print("Please enter a valid command")

            except TypeError:
                print("Please enter a valid command.")

        print()
        print("You can add a post by using the 'P' command and typing out what you want to say or add/change your bio "
              "with the 'B' command.")
        print("You can also add a location to your session using the 'L' command and using -cc and -zip for your "
              "country code and zipcode, respectively")
        print("A song that you like can be added to your profile as well using the 'S' command and using -name and "
              "-art for the name of the song and \nthe name of the artist\n")
        print("If you added a location, you can put the weather in your post/bio using @weather and can pull up your"
              " favorite song with @lastfm\n")

        while True:
            '''
            Gets user input to send a post, add/change their bio, add their location, or favorite song
            '''
            try:
                input = input_processor.Process()

                command = input[0]

                if command == dsp.QUIT:
                    dsc.disconnect(_dsp_conn)
                    sock.close()
                    quit()

                elif command == dsp.POST:
                    user.add_post(input[1])
                    msg = input[1]
                    if '@weather' in msg:
                        msg = location.transclude(msg)
                    if '@lastfm' in msg:
                        msg = song.transclude(msg)

                    dsc.send(HOST, PORT, username, password, msg)

                elif command == dsp.BIO:
                    user.add_bio(input[1])
                    msg = input[1]
                    if '@weather' in msg:
                        msg = location.transclude(msg)
                    if '@lastfm' in msg:
                        msg = song.transclude(msg)
                    dsc.send(HOST, PORT, username, password, "", msg)

                elif command == dsp.LOCATION:
                    location = OpenWeather()
                    user.add_location(input[1][0], input[1][1])
                    location.ccode = user.location[0]
                    location.zipcode = user.location[1]
                    location.set_apikey(openweather_apikey)
                    location.load_data()
                    print(f"Your current location has been set to '{location.city}'\n")

                elif command == dsp.SONG:
                    song = LastFM()
                    user.add_song(input[1][0], input[1][1])
                    song.track_name = input[1][0]
                    song.track_artist = input[1][1]
                    song.set_apikey(lastfm_apikey)
                    song.load_data()
                    print(f"Your current favorite song has been set to {user.song}\n")

                else:
                    print("Please enter a valid command")


            except TypeError:
                print("Please enter a valid command.")

            except UnboundLocalError:
                print("Please enter a location or song before trying to use the keywords.")

    except DSPProtocolError:
        print("An error occurred while attempting to connect.")


if __name__ == '__main__':
    main()