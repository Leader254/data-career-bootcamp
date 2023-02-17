# Make sure you have installed request library via the cmd or via the vs code terminal so as it is simple to
# request for the names from the api 
# you can use the "pip install requests" as the command and install the library
import requests

# # Make a request to the API and retrieve the results
response = requests.get('https://randomuser.me/api/?results=100&gender=male')
results = response.json()['results']

# # Loop through the results and print the name and email of each male user
for i, result in enumerate(results):
    name = result['name']
    print(f"{i+1}. {name['title']}. {name['first']} {name['last']}")
#  The code prints the names of the 100 persons in the list who have the male label