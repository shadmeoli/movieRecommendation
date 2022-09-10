# main library imports file
from BASE import  *

from . import *

# running the splash
def app_runner():
    try:
        entry = Home()
        return entry.run()
    except:
        print("Some error")