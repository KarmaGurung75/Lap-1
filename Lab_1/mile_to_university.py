'''You lives 4 mile aways from university. The bus drives at 25mph but spend 2 mins at each of the 10 stop on the ways.
How long will the bus journey take? alternatively, you could run to university. you jog the first mile at 7mph,
then run the next two at 15mph; before jogging the last at 7mph again,
will this be quicker or slower then the bus?
'''

mile_to_university=4
bus_meter=25
total_stop= 20  # min
total_time=((mile_to_university/bus_meter)*60)
total_bus_time=total_time+20
print("The total time take by the bus",total_bus_time)

first_mile=((1/7)*60)
second_mile=((2/15)*60)
third_mile=((1/7)*60)
total_running_time= first_mile+second_mile+third_mile
print("the total time taken by the jogging is",total_running_time)
if total_bus_time<total_running_time:
    print("The bus is faster than jogging")
else:
    print("By jogging is faster than bus")
