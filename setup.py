# pages
from App.signup import *
from App.login import *
from App.splashscreen import *


# running the splash
def app_runner():
    try:
        entry = SplashScreen()
        return entry.run()
    except:
        print("Some error")


if __name__ == '__main__':
    try:
        entry_point = app_runner()
        entry_point
    except:
        print("error")