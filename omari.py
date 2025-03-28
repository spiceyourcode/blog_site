import zoneinfo 
time=zoneinfo.available_timezones()


with open('timezones.txt', 'w') as file:
    time_in_srting=str(time)
    file.write(time_in_srting)
    print("operatiion done successfully")
