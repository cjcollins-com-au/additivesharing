## Additive sharing with 2 parties (Python)
Simple additive sharing (secure multiparty computation) example featuring Alice and Bob.

## Requirements

Requires python. 

Install websockets: $pip3 install websockets

(Install pip first if you don't already have it, on Linux this would be: $sudo apt install python3-pip)

Download all files to the same directory.

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


## Disclaimer

This is based on process/formula provided as part of postgrad study; the end result is not hidden (in fact this is the desirable outcome) however
this means that the other parties orginal value can easily be inferred when there are only 2 parties.  This may be intended to scale up to a greater 
number of shares (a 2 party computation with Alice and Bob alone is perhaps naive) without parties being able to make that inference, but my 
maths skill isn't up to getting that to happen.
