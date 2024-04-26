Simple additive sharing (secure multiparty computation) example featuring Alice and Bob.

Requires Python only; run in two separate terminal sessions, one for alice.py and one for bob.py. 

i.e:
(in terminal 1) $ python3 alice.py
(in terminal 2) $ python3 bob.py

These will then prompt for the respective values and proceed through the calculations, communicating via sockets to exchange any required values.

The programs have a configurable sleep time and also random value maximum which can be set in code towards the top of each program.
(The sleep time determines the delay between steps).

The IP address and port details are also configurable at the top of each program to run across a network (by default it runs on localhost - 127.0.0.1)


DISCLAIMER:

This is based on process/formula provided as part of postgrad study; the end result is not hidden (in fact this is the desirable outcome) however
this means that the other parties orginal value can easily be inferred when there are only 2 parties.  This may be intended to scale up to a greater 
number of shares (a 2 party computation with Alice and Bob alone is perhaps naive) without parties being able to make that inference, but my 
maths skill isn't up to getting that to happen.
