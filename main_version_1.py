import psutil
from notifypy import Notify
import os
import time

os.chdir("D:\\git repos\\battery_notification_system")


def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

def battery_details():
    battery = psutil.sensors_battery()
    return battery.percent,battery.power_plugged,convertTime(battery.secsleft)

def notification_gen(battery_percentage, battery_plug_in, battery_left):
    notification = Notify()
    notification.__init__(default_notification_application_name="Automation Walkers Services Ltd")
    notification.title = "Battery Notification"
    notification.audio = "./sounds/noti.wav"
    if battery_plug_in == "False":
        message = f"""Battery percentage -> {battery_percentage} %\nPower plugged in -> {battery_plug_in}\nBattery left -> {battery_left}"""
        if battery_percentage <= 10:
            notification.icon = "./icons/battery 1.png"
            message = f"""Battery percentage -> {battery_percentage} %\nBattery left -> {battery_left}\nPlease plug the charger!"""
        elif battery_percentage > 10 and battery_percentage <= 25:
            notification.icon = "./icons/battery 1.png"
        elif battery_percentage > 25 and battery_percentage <= 50:
            notification.icon = "./icons/battery 2.png"
        elif battery_percentage > 50 and battery_percentage <= 75:
            notification.icon = "./icons/battery 3.png"
        elif battery_percentage > 75 and battery_percentage <= 100:
            notification.icon = "./icons/battery 4.png"
    else:
        if battery_percentage > 95 and battery_percentage <= 100:
            notification.icon = "./icons/battery charging full.png"
            message = f"""Battery percentage -> {battery_percentage} %\nPlease plug out the charger!"""
        else:
            notification.icon = "./icons/battery charging.png"
            message = f"""Battery percentage -> {battery_percentage} %\nBattery is charging!"""

    notification.message = message
    return notification

if __name__ == "__main__":
    while(1):
        battery_percentage, battery_plug_in, battery_left = battery_details()
        notification = notification_gen(int(battery_percentage), str(battery_plug_in), str(battery_left))
        notification.send()
        time.sleep(1800)