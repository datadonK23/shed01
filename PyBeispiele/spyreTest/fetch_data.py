"""
Name: 
Purpose: 
Author: Thomas Treml (datadonk23@gmail.com)
Date: 
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

my_activities = client.get_activities(limit=1)
result = my_activities.result_fetcher()

print me
print result