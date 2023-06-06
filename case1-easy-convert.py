''' 
This code is to convert a JSON file formatting like "sample1-meta" to a GML file.
The future graph is expected to have nodes with different sizes according to its "count" and different colors according to its type.
Before executing this, you need to add your JSON file in the same directory to replace "sample1-meta.json".
'''
# Import modules
import json
import networkx as nx
import math

# Load the JSON data from file
with open('sample1-meta.json', 'r') as s1:
    data = json.load(s1)

# Create a networkx graph object
graph = nx.Graph()

# Add nodes
for node in data['nodes']:
    id = node['id']
    name = node['n_source']
    # The following two lines are to limit the size of node in case there're huge differences in the "count" values.
    count = int(node['count'])
    size = 10 * int(math.floor(math.log10(count)))
    type = node['n_type']
    graph.add_node(id, name=name, type=type, count=count, size=size)

# Add edges
for edge in data['links']:
    graph.add_edge(edge['source'], edge['target'])

# Write graph to GML file
nx.write_gml(graph, 'meta.gml')

# Print the message
print('The meta.gml has been generated.')