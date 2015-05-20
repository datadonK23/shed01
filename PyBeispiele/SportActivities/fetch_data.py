"""
Name: 
Purpose: Fetching my data from Strava
Author: Thomas Treml (datadonk23@gmail.com)
Date: 2015-05-15
"""

import json, os, io
from datetime import datetime
from stravalib import Client
from instance import hidden_conf

# Import secret token
STORED_ACCESS_TOKEN = hidden_conf.get_access_token()
client = Client(access_token=STORED_ACCESS_TOKEN)

CYCLING_JSON = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "cycling_coll.json")
SWIMMING_JSON = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "swimming_coll.json")

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

# Fetch activities this year
my_activities = client.get_activities(after=datetime(2015, 1, 1)) #(limit=5)
act = []
for a in my_activities:
    act.append(a)

# Fetch every activity % make collections
cycling_collection = []
swimming_collection = []

for i in range(len(act)):
    print "fetching activity " + str(i)
    id = act[i].id
    activity = client.get_activity(id)

    # Activity collections
    if activity.type == "Ride":
        my_activity = {}
        my_activity["type"] = "cycling"
        my_activity["date"] = str(activity.start_date_local)
        my_activity["time"] = str(activity.moving_time)
        my_activity["distance"] = str(activity.distance)
        my_activity["avg_speed"] = str(activity.average_speed)
        my_activity["energy"] = str(activity.kilojoules)
        cycling_collection.append(my_activity)
    elif activity.type == "Swim":
        my_activity = {}
        my_activity["type"] = "swimming"
        my_activity["date"] = str(activity.start_date_local)
        my_activity["time"] = str(activity.moving_time)
        my_activity["distance"] = str(activity.distance)
        swimming_collection.append(my_activity)
    else:
        pass

# Store to json files
print "Write to files"

with io.open(CYCLING_JSON, "w", encoding="utf-8") as f:
    f.write(unicode(json.dumps(cycling_collection, ensure_ascii=False)))

with io.open(SWIMMING_JSON, "w", encoding="utf-8") as f:
    f.write(unicode(json.dumps(swimming_collection, ensure_ascii=False)))

print "Finished"
