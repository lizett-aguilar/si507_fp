Lizett Aguilar  
SI 507  
Final Project  
11/29/24  

This project allows the user to obtain information about National Park Service (NPS) sites in the state of California. 

The project uses the following libraries: json, requests, secret, and networkx. The user should obtain their NPS api key here https://www.nps.gov/subjects/developer/get-started.htm
and replace the api_key variable with their own before running the program.

The project obtains data from the NPS API. An API key is required to do an API call. The end user can obtain their
own api key here: https://www.nps.gov/subjects/developer/get-started.htm

When the user runs the program they are asked to input the name of a California NPS site to obtain more information on it. 
The program gives them a list of the sites which they can copy and paste from. 

On the backend, the program has done an API call to the NPS API and saved the site information locally. 
The program obtains the information for the site the user has input and returns the site's description, website address, and a list of activities available at the site. 
The graph component is composed of nodes (the sites) and edges (activities available at each site). 
The nodes are connected by the activities the sites share in common. The network component offers the users
site recommendations based on these shared edges and provides the name of the park which is most similar to the park the user inquired about. 
Similarity in this case is determined by the most number of shared activities. 

After providing this information, the user can continue to obtain more site information and recommendations until they enter "quit" to end the program. 

