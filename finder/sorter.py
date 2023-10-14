import math

def sort_by_distance(offices, longitude, latitude):
    def calculate_distance(office):
        office_longitude = office.longitude
        office_latitude = office.latitude
        dx = office_longitude - longitude
        dy = office_latitude - latitude
        distance = math.sqrt(dx ** 2 + dy ** 2)
        return distance

    sorted_offices = sorted(offices, key=calculate_distance)
    return sorted_offices
    
def sort_by_load(offices_loads, day, hour):
    offices_current_load = {}
    for office, office_loads in offices_loads.items():
        working_hour = []
        for load in office_loads:
            if load.hour not in working_hour:
                working_hour.append(load.hour)
        if hour in working_hour:
            for load in office_loads:
                if load.hour == hour and load.day == day:
                    offices_current_load[office] = load
        else:
            compare_result = compare_hour(hour, working_hour[1])
            if compare_result == 1 or compare_result == 0:
                for load in office_loads:
                    if load.hour == working_hour[1] and load.day == day:
                        offices_current_load[office] = load
            else:
                for load in office_loads:
                    if load.hour == working_hour[-1] and load.day == day:
                        offices_current_load[office] = load
    sorted_offices = sorted(offices_current_load, key=lambda x: offices_current_load[x].percentage)
    return sorted_offices
    
def compare_hour(hour_a, hour_b):
    hour_a = hour_a.split(':')
    hour_b = hour_b.split(':')
    
    if int(hour_a[0]) < int(hour_b[0]):
        return 1
    elif int(hour_a[0]) > int(hour_b[0]):
        return -1
    else:
        if int(hour_a[1]) < int(hour_b[1]):
            return 1
        elif int(hour_a[1]) > int(hour_b[1]):
            return -1
        else:
            return 0