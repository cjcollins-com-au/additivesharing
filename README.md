## Additive sharing with 2 parties (Python)
Simple additive sharing (secure multiparty computation) example featuring Alice and Bob.

## Requirements

Requires python. 

Install websockets: $pip3 install websockets

(Install pip first if you don't already have it, on Linux this would be: $sudo apt install python3-pip)

Download all three files to the same directory.

## Usage

Run in terminal window on Windows / Linux / Mac.  Run in two separate terminal sessions, one for alice.py and one for bob.py. 

i.e:

(in terminal 1) $ python3 alice.py

(in terminal 2) $ python3 bob.py

These will then prompt for the respective values and proceed through the calculations, communicating via sockets to exchange any required values.

*Note - sssr.py is required and should be downloaded but is not run directly by the user; this is required by the Alice and Bob programs 
and provides the required socket/communication functions*

### Configuration Options
*These options are set in code - the variables involved are clearly indicated and located near the top of each source code file)*
* my_ip / my_port - IP address and port for each player.  Runs on localhost / 127.0.0.1 (same PC) by default.
* sleep_delay - in seconds, the time to pause between each processing step.  Increase to give you more time to see the process in action.
* random_max - the maximum integer value to use for generating random values.  Smaller values are more readable on screen.


## Notes

In this scenario with 2 parties, the original value from the other party can be inferred (although not directly exchanged) as the end result is 
known (...this is in fact the desired outcome) and each party knows their own value.   This won't happen with a 3 party setup but the 2 party 
setup here is a bit more understandable.
