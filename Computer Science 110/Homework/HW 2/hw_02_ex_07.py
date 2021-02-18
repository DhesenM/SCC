# You look at the clock and it is exactly 2pm. You set an alarm to go off in 51
# hours. At what time does this alarm go off? (Hint: you could count on your
# fingers, but this is not what we're after. If you are tempted to count on your
# fingers, change the 51 to 5100.)

alarm_hours = 51
day_hours = 24
alarm_remaining_hours = 51 % day_hours   # Calculate the remaining hours
time = 14   # Set the time to 24-hour clock
time = (14 + alarm_remaining_hours) % day_hours
# Calculate the time in 24-hour clock
print("The alarm goes off at",str(time)+":00.")

# The alarm goes off at 17:00.
