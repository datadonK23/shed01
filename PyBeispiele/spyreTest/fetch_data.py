"""
Name: 
Purpose: Fetching my data from Strava
Author: Thomas Treml (datadonk23@gmail.com)
Date: 2015-05-11
"""

from stravalib import Client
from instance import hidden_conf

STORED_ACCESS_TOKEN = hidden_conf.get_access_token()
client = Client(access_token=STORED_ACCESS_TOKEN)

# My data
my_data = client.get_athlete() # athlete details
me = {}
me["id"] = my_data.id
me["name"] = my_data.firstname + " " + my_data.lastname
me["city"] = my_data.city
my_bikes = my_data.bikes
bikes = {}
for b in my_bikes:
    bike = {}
    bike[b.id] = b.name
    bikes.update(bike)
me["bikes"] = bikes
#print me

# Fetch activities
my_activities = client.get_activities(limit=5)
act = []
for a in my_activities:
    act.append(a)

last_id = act[0].id
last_activity = client.get_activity(last_id)

# Activity collection prototyp
my_activity = {}
if last_activity.type == "Ride":
    my_activity["time"] = last_activity.moving_time
    my_activity["distance"] = last_activity.distance
    my_activity["avg_speed"] = last_activity.average_speed
    my_activity["energy"] = last_activity.kilojoules
else:
    pass

print my_activity

