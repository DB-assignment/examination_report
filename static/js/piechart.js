/**
 * Pizza graphic
 */

//function to shorten document.getElementById
var $ = function(id){
  return document.getElementById(id);
}

//data from csv will be copied to rows variable
var rows ;

//async function to get data
d3.csv("GeneralElection2011.csv", function(error, data) {
  
  rows = data;
  initialise()
});

console.log(rows);

var initialise = function(){
        
  //Make an array of the constutuencies
  var places = rows.map(function(row) {
  
    return row.Constituency;
  });
  
  //populate the select list with the constituency names
  places.forEach( function(place) {
    
    var select = $("select");
    var option = document.createElement("option");
    option.setAttribute("value", place);
    
    var optionText = document.createTextNode(place);
    option.appendChild(optionText);
    
    select.appendChild(option);
    
  });	
}

//function to return the index (rows) of the desired constituency
var findIndex = function(name) {

  var index = rows.findIndex( function(row) {
    return row.Constituency == name;
  });
  
  return index;
};



//When the select list changes
$("select").onchange = function () {
  var conName = $("select").value;

  var conIndex = findIndex(conName);
  
  //change name in heading
  $("location").innerHTML = rows[conIndex].Constituency;

  //Use the conIndex to access the required row..
  console.log(rows[conIndex].NumSeats);




var dataset = [
  { label: 'Fianna Fail', count: Math.round(rows[conIndex].FFFirstPref) }, 
  { label: 'Fine Gael', count: Math.round(rows[conIndex].FGFirstPref) },
  { label: 'Labour', count: Math.round(rows[conIndex].LabFirstPref) },
  { label: 'Sinn Fein', count: Math.round(rows[conIndex].SFFirstPref) },
  { label: 'Others', count: Math.round(rows[conIndex].GreenFirstPref) }
];


var width = 500;
var height = 400;
var radius = 200;

//predefined category of 20 colours
var color = d3.scale.category20();

    //to delete extra charts
var chart = $('chart');
while(chart.hasChildNodes()){
  chart.removeChild(chart.firstChild);
}

//append an SVG and then append a 'g' (group) onto that
var svg = d3.select('#chart')
  .append('svg')
  .attr('width', width)
  .attr('height', height)
  .append('g')
  .attr('transform', 'translate(' + ((width-100) / 2) + 
  ',' + (height / 2) + ')');



var arc = d3.svg.arc()
  .outerRadius(radius);

var labelArc = d3.svg.arc()
  .outerRadius(radius- 40)
  .innerRadius(radius- 40);

var pie = d3.layout.pie()
  .value(function(d) { return d.count; })
  .sort(null);

var g = svg.selectAll('g')
  .data(pie(dataset))
  .enter().append('g');
  
g.append("path")
  .attr('d', arc)
  .attr("data-legend", function(d){return d.data.label})
  .attr("data-legend-pos", function(d, i){return i})
  .attr('fill', function(d, i) { 
    return color(d.data.label);
  });
  
g.append("text")
  .attr("transform", function(d) { return "translate(" + labelArc.centroid(d) + ")"; })
  .attr("dy", ".35em")
  .attr("class", "pieText")
  .text(function(d) { return d.data.count + "%"; });

d3.select('svg')
  .append("g")
  .attr("class", "legend")
  .attr("transform", "translate(400 ,50)")
  .style("font-size", "14px")
  .call(d3.legend);



}