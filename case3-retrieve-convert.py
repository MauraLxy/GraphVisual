''' 
This code is to retrieve data from neo4J database and transform it to a GML file.
The future graph is expected to have nodes with different colors according to its type but the same sizes.
Before executing this, you need to: 
1. Run "pip install neo4j" in the terminal to install neo4j 
2. Implement the user name, password and uri in "sample3-user.json"
'''
# Import modules
from neo4j import GraphDatabase
import networkx as nx
import json

# Read the user file and get the name, password and neo4j uri.
with open('sample3-user.json', 'r') as s3:
    data = json.load(s3)
user = data["username"]
password = data["password"]
uri = data["uri"]
driver = GraphDatabase.driver(uri, auth = (user, password))

# Create arrays to hold nodes and edges
nodes = []
edges = []

with driver.session() as session:
  
  # Retrieve data using cypher
  result = session.run("MATCH (a:researcher {orcid: '0000-0002-4259-9774'})-[r]-(b) RETURN a,r,b")

  # Add the connected nodes and edges
  for record in result:
    center = record['a']._properties
    connected = record['b']._properties
    start = record['r'].start_node._properties["key"]
    end = record['r'].end_node._properties["key"]
    relationship = {"source": start, "target": end}
    nodes.append(connected)
    edges.append(relationship)

  # Add the center researcher node
  nodes.append(center)

  # Create a graph
  graph = nx.Graph()

  # Create integer ids for each node
  count = 1
  map = {}
  for node in nodes:
    key = node['key']
    name = node.get('name') or node.get('full_name') or node.get('title')
    type = node['type']
    map[key] = count

    # Add the nodes to the graph
    graph.add_node(count, key=key, name=name, type=type)
    count+=1

  # Add the edges to the graph
  for edge in edges:
    source = map[edge['source']]
    target = map[edge['target']]
    graph.add_edge(source, target)

  # Generate the GML file
  nx.write_gml(graph, 'meta.gml')

# Print the message
print('The meta.gml has been generated.')