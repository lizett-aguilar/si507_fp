import json
import requests
from secret import api_key
import networkx as nx

class national_park_site:
    def __init__(self, park):
        self.name = park['name']
        self.description = park['description']
        self.website = park['url']
        self.activities = park['activities']

#creating a dictionary of dictionaries for the national park information from the nps api. 
#For each national park in california, the key is the name of the park and the value is a dictionary of the park's information. 
#the following park information will be obtained from the nps api: park name, description, website, address, and activities.
def get_national_park_site():
    url = f"https://developer.nps.gov/api/v1/parks?stateCode=CA&api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    national_parks_dictionary = {}
    for park in data['data']:
        national_parks_dictionary[park['name']] = {
            'name': park['name'],
            'description': park['description'],
            'url': park['url'],
            'addresses': park['addresses'],
            'activities': [activity['name'] for activity in park['activities']]
        }
    #store the parks dictionary in a json file
    with open('national_parks.json', 'w') as f:
        json.dump(national_parks_dictionary, f)

#Use the networkx library to create a graph of the national parks in california, where the nodes are the park names and the edges are the activities that the parks have in common.
#wrap this in a function called create_park_graph that takes in a list of national park objects and returns a graph object.
def create_park_graph(parks):
    G = nx.Graph()
    for park in parks:
        G.add_node(park.name)
        for other_park in parks:
            if park != other_park:
                common_activities = set(park.activities) & set(other_park.activities)
                if common_activities:
                    G.add_edge(park.name, other_park.name, weight=len(common_activities))
    return G

'''using the graph G, write a function called park_recommendations that takes in a park name and returns a list of recommended parks to visit based on the activities that the parks have in common.'''
def get_park_recommendations(park_name, G):
    recommended_parks = []
    for park in G.neighbors(park_name):
        recommended_parks.append(park)
    print(f"\nIf you like this National Park Service (NPS) site, here are recommended parks based on shared activities: {recommended_parks}")

def get_most_similar_park(park_name, G):
    '''for the park_name, find the park that is most similar to it based on the weight of the edge between itself and the other parks. 
    print the name of the park and the set of common activities that the two parks have.'''
    most_similar_park = ''
    most_similar_park_weight = 0
    for park in G.neighbors(park_name):
        if G[park_name][park]['weight'] > most_similar_park_weight:
            most_similar_park = park
            most_similar_park_weight = G[park_name][park]['weight']
    print(f"\nThe park most similar to {park_name} is {most_similar_park} with {most_similar_park_weight} shared activities. You can get more information about {most_similar_park} by entering the park name.")

def input_prompt(parks, G: national_park_site):
    prompt = """ \n \n Please enter (copy and paste) the name of a Californian National Park Service (NPS) site which you would like more information for. \n 
    Here is a list of the NPS sites in California: Alcatraz Island, Cabrillo, California, Castle Mountains, Channel Islands, César E. Chávez, Death Valley, Devils Postpile, Eugene O'Neill, 
    Fort Point, Golden Gate, John Muir, Joshua Tree, Juan Bautista de Anza, Lassen Volcanic, Lava Beds, Manzanar, Mojave, Muir Woods, 
    Old Spanish, Pinnacles, Point Reyes, Pony Express, Port Chicago Naval Magazine, Presidio of San Francisco, Redwood, Rosie the Riveter WWII Home Front, 
    San Francisco Maritime, Santa Monica Mountains, Sequoia & Kings Canyon, Tule Lake, Whiskeytown, Yosemite" \n)
    Enter 'quit' to exit the program at anytime. \n """
    all_park_options = [park.name for park in parks]
    while True:
        chosen_park = input(prompt)
        if chosen_park == 'quit':
            return
        if chosen_park not in all_park_options:
            print('Please enter a valid park name.')
            return input_prompt(parks, G)
        elif chosen_park in all_park_options:
            #find the chosen park object from the list of park objects
            park = [park for park in parks if park.name == chosen_park][0]
            print(f'\nHere is information about national park site, {park.name}: \n DESCRIPTION: {park.description} \n WEBSITE: {park.website} \n ACTIVITIES AVAILABLE AT {park.name}:{park.activities}')
            get_park_recommendations(chosen_park, G)
            get_most_similar_park(chosen_park, G)
            return input_prompt(parks, G)

def main():
    get_national_park_site()
    #create an instance of the national_park class for each park in the national_parks.json file and store that as a list called parks
    with open('national_parks.json', 'r') as f:
        national_parks_dictionary = json.load(f)
        parks = [national_park_site(park) for park in national_parks_dictionary.values()]
    #remove park named 'Butterfield Overland] from the list of parks
    parks = [park for park in parks if park.name != 'Butterfield Overland']
    G = create_park_graph(parks)
    input_prompt(parks, G)

if __name__ == '__main__':
    main()