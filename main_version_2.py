import os
import time

os.chdir("D:\\git repos\\battery_notification_system")

from main_version_1 import *

if __name__ == "__main__":
    while(1):
        battery_percentage, battery_plug_in, battery_left = battery_details()
        notification = notification_gen(int(battery_percentage), str(battery_plug_in), str(battery_left))
        if int(battery_percentage) <=10 and str(battery_plug_in) == "False":
            notification.send()
        elif int(battery_percentage) >= 95 and str(battery_plug_in) == "True":
            notification.send()
        