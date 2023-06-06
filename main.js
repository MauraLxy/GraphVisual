// Import ECharts
echarts = require('echarts')

// Import the JSON processed by Gephi 
meta = FileAttachment("meta.json").json()

// Create a container for visulisation
container = html`<div style="width:100%; height:750px;"/>`

// Format the nodes
nodes = meta.nodes.map((index) => ({
  id: meta.nodes.at(index).key,
  name: meta.nodes.at(index).attributes.name.replace("&#38;", "&"),
  label: meta.nodes.at(index).attributes.Degree,
  size: meta.nodes.at(index).attributes.size,
  x: meta.nodes.at(index).attributes.x,
  y: meta.nodes.at(index).attributes.y,
  category: getCategory(meta.nodes.at(index).attributes.type.toLowerCase())[0],
  color: getCategory(meta.nodes.at(index).attributes.type.toLowerCase())[1],
  borderColor: getCategory(meta.nodes.at(index).attributes.type.toLowerCase())[2]
  })
)

// Format the edges
function getLink(){
    var lks = []
    var keys = new Set()
    meta.edges.forEach(function (edge) {
        let link = {source: edge.source, target: edge.target};
        let key = link.source + "-" + link.target;
        let reversedKey = link.target + "-" + link.source;
        if (!keys.has(key) && !keys.has(reversedKey)) {
        lks.push(link);
        keys.add(key);
        }
    })
  return lks
}

// Format the category
categories = [
  {"name": "Researcher"},
  {"name": "Dataset"},
  {"name": "Organisation"},
  {"name": "Publication"},
  {"name": "Grant"}
]

// Set node categories, colors and border colors
function getCategory(type){
    switch (type) {
    case 'researcher':
      return [0,'RGB(99,204,158)','RGB(86,179,140)'];
    case 'dataset':
      return [1,'RGB(235,110,31)','RGB(184,74,3)'];
    case 'organisation':
      return [2, 'RGB(150,98,208)', 'RGB(101,66,142)'];
    case 'publication':
      return [3,'RGB(85,191,246)','RGB(75,169,220)'];
    case 'grant':
      return [4,'RGB(255,214,108)','RGB(249,200,82)'];
  }
}

// Set the option
option = ({
  // when the mouse is moved on the node, show the label
  tooltip: {},
  // set the default legend color, the order is inline with "categories" below.
  color: ['RGB(99,204,158)','RGB(235,110,31)','RGB(150,98,208)', 'RGB(85,191,246)', 'RGB(255,214,108)'],
  // categorize all nodes according to their types
  legend: [{
      data: categories.map(function (category) {
        return category.name;
      })
    }],
  // import the node data
  series: [
    {
      type: 'graph',
      layout: 'none',
      data: nodes.map((index) => ({
        // links connect two nodes by id
        id: nodes.at(index).id,
        // name is what will be shown beside the node, aka label
        name: nodes.at(index).name,
        // value will be shown on the label
        value: nodes.at(index).label,
        // set the size of each node
        symbolSize: nodes.at(index).size,
        // set the coordinates of each node
        x: nodes.at(index).x,
        y: nodes.at(index).y,
        // category is used to organize the legend 
        category: nodes.at(index).category,
        // set the color, border color and boder width of the node
        itemStyle: {
          color: nodes.at(index).color,
          borderColor: nodes.at(index).borderColor,
          borderWidth: 1
        }
      })),
      links: getLink(),
      categories: categories,
      // set the link color to be the same as its source node
      lineStyle: {
        color: 'source',
        curveness: 0.3
      },
      scaleLimit: {
        min: 0.4,
        max: 2
      },
      roam: true,
      draggable: true,
      //don't show the label
      label: {
        show: false,
        position: 'right',
        formatter: '{b}'
      }
    }
  ]
})

// Apply the option
echarts.init(container).setOption(option)