''' 
This code is to convert a JSON file formatting like "sample2-meta" to a GML file.
The future graph is expected to have nodes with different colors according to its type but the same sizes.
Before executing this, you need to add your JSON file in the same directory to replace "sample2-meta.json".
'''
# Import modules
import json
import networkx as nx

# Load the JSON data from file
with open('sample2-meta.json', 'r') as s2:
    data = json.load(s2)

# Create a networkx graph object
graph = nx.Graph()

# Add nodes
for node in data['nodes']['datasets']:
    id = node['key']
    name = node['title']
    graph.add_node(id, type='Dataset', name=name)

for node in data['nodes']['grants']:
    id = node['key']
    name = node['title']
    graph.add_node(id, type='Grant', name=name)

for node in data['nodes']['organisations']:
    id = node['key']
    name = node['name']
    graph.add_node(id, type='Organisation', name=name)

for node in data['nodes']['publications']:
    id = node['key']
    name = node['title']
    graph.add_node(id, type='Publication', name=name)

for node in data['nodes']['researchers']:
    id = node['key']
    name = node['full_name']
    graph.add_node(id, type='Researcher', name=name)

# Add edges
for key in data["relationships"]:
    for edge in data["relationships"][key]:
        graph.add_edge(edge['to'], edge['from'])

# Write graph to GML file
nx.write_gml(graph, 'meta.gml')

# Print the message
print('The meta.gml has been generated.')