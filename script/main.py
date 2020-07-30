
from modules.create_webdriver import create_webdriver

from modules.get_prices import get_prices
import time
from modules.grapher import plot_prices
from modules.helpers import check_raceday
import os
import sys

# select up to 5 drivers
# select a team

start_time = time.time()
wdir = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':

    if check_raceday():
        print("It's raceday or quali, no price change")

    else:

        webdriver = create_webdriver()
        webdriver.get("https://fantasy.formula1.com/team/1?week=3")

        credentials = {
            'username' : 'bstevensonssss@gmail.com',
            'password' : 'ferrari'
        }

        #Creates an account with given drivers
        try:
            get_prices(webdriver, credentials)
        except:
            print ("Unexpected error:", sys.exc_info()[0])
            raise
        print("--- %s seconds ---" % (time.time() - start_time))

        time.sleep(5)
        webdriver.close()

        plot_prices(wdir + "/modules/data/resources/constructor_prices.xlsx", drivers=False)

        plot_prices(wdir + "/modules/data/resources/driver_prices.xlsx", drivers=True)

