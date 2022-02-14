#! python3
# Digital clock

from time import strftime, sleep

while True:
    # strftime() prints fixed width

    # '\r' is a carriage return character.  It moves the cursor to the 
    # start of the *same current* line, so it will overwrite the same line 
    # (so multiple lines in Terminal are not written)

    # When end is set to something, the buffer is not flushed any more.
    # flush=True stops buffering and outputs immediately.

    print( strftime("%I:%M:%S %p") + '\r', end='', flush=True)

    sleep(1)
