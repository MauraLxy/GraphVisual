# GraphVisual
The purpose of this project is to visualise research graph data with *Gephi* and *Observable*. The procedures are:  
1. Use the "case" code to convert data to GML file because Gephi doesn't support JSON. (How to convert? See **A1**)  
2. Import the GML file to Gephi to modify the layout. (How to modify? See **A2**)  
3. Export a JSON file from Gephi and import the JSON file to https://observablehq.com/d/41773913ab3e2d19 or copy the codes in main.js to your Observable notebook to get the visualisation.  

---
**A1-Converting**  
Since the data are in different formats, three common cases are chosen to visualise.  
  
*case1*: JSON-formatted data like sample1: 
```json
{"nodes": [{"n_source": "A", "n_type": "Researcher", "n_PID": "A", "count": "1", "id": 1}, 
          {"n_source": "B", "n_type": "Organisation", "n_PID": "B", "count": "2", "id": 2}], 
"links": [{"rel_count": "1", "source": 1, "target": 2}, {"rel_count": "2", "source": 1, "target": 3}]}   
```
  
*case2*: JSON-formatted data like sample2: 
```json
{"nodes": {"datasets": [{"authors_list": "A", "datacite_type": "dataset", "doi": "1", "key": "/1", "publication_year": "1001", "title": "A1"}], 
          "grants":[{"end_year": "2", "funder": "B", "grant_id": "2", "key": "/2", "start_year": "1002", "title": "B2"}]}, 
"relationships": {"researcher-dataset":[{"from": "/5", "to": "/1"}], "researcher-grant":[{"from": "/5", "to": "/2"}]}}   
```
  
*case3*: Retrieve data from neo4j which are several Records:  
```record
<Record 
a = <Node element_id='1' properties={'type': 'researcher', 'key': '/1'}> 
r = <Relationship element_id='10' nodes=(<Node element_id='1' properties={'type': 'researcher', 'key': '/1'}>, 
                                         <Node element_id='2' properties={'type': 'publication', 'key': '/2'}>)> 
b = <Node element_id='2' properties={'type': 'publication', 'key': '/2'}>
>
```
  
*What you need to do for converting*:  
  1.1 Find which case matches your data and replace the sample file with your JSON file (case1 and case2) or implement the user file (case3).   
  1.2 Run the corresponding python file to generate a GML file. (command: e.g. "python case2-convert.py")  
  
---

**A2-Modifying**   
You can either follow the word version instructions here or try https://1drv.ms/p/s!AvFj9wFogEtIjGI2RaHH4I80-0eZ for the diagram version instructions.  
  2.1. Open Graph File... (meta.gml), change the graph type from "Directed" to "Undirected", click "OK".  
  2.2 Change the node color by clicking the "partition" under the *palette icon* in the appearance(top left), choose "type" and "Apply".  
  2.3 (case1 only) Change the node size by clicking the "Ranking" under the *circles icon* next to the *palette icon*, set the "min" to "10" and the "max" to "60", choose "size" and "Apply".  
  2.4 From "Layout" (bottom left column), choose "Force Atlas", change the "Repulsion strength" to 2000, tick the "Adjust by Sizes" and "Stop".  
  2.5 If the layout of the nodes is not satisfactory, you can manually drag the node to a better position.  
  2.6 (optional) Get the degree of each node by clicking the "Run" next to the "Average Degree" (right column).  
  
---
**Showcase**  
case1 - https://observablehq.com/d/066b0f5d94fe57ba  
case2 - https://observablehq.com/d/534134752c6a29d8  
case3 - https://observablehq.com/d/41773913ab3e2d19  
