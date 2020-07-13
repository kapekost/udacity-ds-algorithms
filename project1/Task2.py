"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
call_durations = {}
max_duration = {}
# max_duration["number"] = 0
# max_duration["duration"] = 0


def appendDuration(caller, duration):
    if (caller in call_durations):
        call_durations[caller] += duration
    else:
        call_durations[caller] = duration
    # if (max_duration["duration"] < call_durations[caller]):
    #     max_duration["number"] = caller
    #     max_duration["duration"] = call_durations[caller]


for call in calls:
    appendDuration(call[0], int(call[3]))
    appendDuration(call[1], int(call[3]))

max_call = max(call_durations, key=call_durations.get)

print("%s spent the longest time, %s seconds, on the phone during September 2016." %
      (max_call, call_durations[max_call]))
