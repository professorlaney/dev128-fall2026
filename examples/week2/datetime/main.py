from datetime import datetime

current_datetime = datetime.now()

print("Current date and time:", current_datetime)

print("Current date:", current_datetime.strftime("%m/%d/%Y"))
print("Current time:", current_datetime.strftime("%I:%M %p"))
