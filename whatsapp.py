import pywhatkit
import datetime

# Variables
phone_numer = '+34691737022'
message = 'Write the message here'
time_hour = datetime.datetime.now().hour
time_minute = datetime.datetime.now().minute + 1
waiting_time_to_send = 10
close_tab = True
waiting_time_to_close = 2
pywhatkit.sendwhatmsg(phone_numer, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
