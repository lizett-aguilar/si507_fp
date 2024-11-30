Lizett Aguilar
Readme file for Data Sources

Data Source: National Park Service API
Origin: https://www.nps.gov/subjects/developer/api-documentation.htm
Where to obtain API Key: https://www.nps.gov/subjects/developer/get-started.htm 
Format: Saved locally as a JSON file called: 'national_parks.json'

How to access the data: 
I created a function called get_national_park_site() which does an API call to the NPS API.
The data is initially structured as a dictionary and then saved to the json file. The following data is 
obtained from the api call: all NPS sites in the state of California, including their name, description, url, addresses, and activities.

The activities for the NPS sites are then pulled from the JSON file to create the network structure which the program 
uses to provide park recommendations. 

When the program is run, the user is provided the initial information for the site they've selected and the 
graph component is used to provide other park recommendations and the site it shares the most activities with. 

Brief explanation of local variables:
- 'parks': a list of NPS sites. Each NPS site has been initiated as a national_park_site class. Creating a class allows us to 
create self parameters which store each site's information, such as website and descriptions. 
- G : The network composed of nodes and edges. The network is undirected and each node represents a site. 
The nodes are connected by the activities they share in common with other nodes. 