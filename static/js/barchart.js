
				var data; // a global to hold the json data
				var list; // a global to hold the list part from the data
				var xdomain; //global array to hold next 7 days of the week
				
				// Set the dimensions of the canvas / graph
				var margin = {top: 30, right: 20, bottom: 30, left: 50},
					width = 500 - margin.left - margin.right,
					height = 270 - margin.top - margin.bottom;
				
				//Set up ranges
				var x = d3.scale.ordinal()
					.rangeRoundBands([0, width], .1);
				
				var y = d3.scale.linear()
					.range([height, -10]);
				
				//set up axis
				var xAxis = d3.svg.axis()
					.scale(x)
					.orient("bottom");

				var yAxis = d3.svg.axis()
					.scale(y)
					.orient("left")
					
				
				//set up temperature SVG
				var tempChart = d3.select(".tempSvg")
					.attr("width", width + margin.left + margin.right)
					.attr("height", height + margin.top + margin.bottom)
				  .append("g")
					.attr("transform", "translate(" + margin.left + "," + margin.top + ")");
					
				//set up cloud SVG
				var cloudChart = d3.select(".cloudSvg")
					.attr("width", width + margin.left + margin.right)
					.attr("height", height + margin.top + margin.bottom)
				  .append("g")
					.attr("transform", "translate(" + margin.left + "," + margin.top + ")");
					
				//Work out day from unix timestamp
				 

				//Get Data
				var getData = function(url){
				
					//This function is a xhr callback for the json data
					d3.json(url, function(error, json) {
						  if (error) return console.warn(error);
						  data = json;	//assign to global
						  list=json.list;
						  
						  //extract days of the week from unix timestamp data
						  xdomain = list.map(function(d){
								var days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
								var day = new Date(d.dt * 1000).getDay();
								return days[day];
						});
						  
						  visualiseTemp();
						  visualiseClouds();
					});
				}

				 function visualiseTemp() {				
				 		
					x.domain(xdomain);
					y.domain([-10, 50]);
					
				
					//enter section
					var bar = tempChart.selectAll("g")
						.data(list)
							.enter().append("g")
							.attr("transform", function(d, i) { return "translate(" + x(xdomain[i]) + ",0)"; });
							
					bar.append("rect")
						.attr("y", function(d) { return y(d.temp.max); })
						.attr("height", function(d) { return height - y(d.temp.max); })
						.attr("width", x.rangeBand());
				
					bar.append("text")
							.attr("class", "barText")
							.attr("x", x.rangeBand() / 2)
							.attr("y", function(d) { return y(d.temp.max) + 3; })
							.attr("dy", ".75em")
							.text(function(d) { return d.temp.max; });
				
					//update section
					var bar = tempChart.selectAll("g")
						.data(list)
						
					bar.select("rect")
						.attr("y", function(d) { return y(d.temp.max); })
						.attr("height", function(d) { return height - y(d.temp.max); });
							
					bar.select("text")
						.attr("class", "barText")
						.attr("x", x.rangeBand() / 2)
						.attr("y", function(d) { return y(d.temp.max) + 3; })
						.attr("dy", ".75em")
						.text(function(d) { return d.temp.max; });
						
						
					//Draw the axes
					tempChart.append("g")
						.attr("class", "x axis")
						.attr("transform", "translate(0," + height + ")")
						.call(xAxis);
						
						
					yAxis.tickFormat(function(d) { return d + "°C"; });

					tempChart.append("g")
						.attr("class", "y axis")
						.call(yAxis)
					  .append("text")
						.attr("transform", "rotate(-90)")
						.attr("y", -40)
						.attr("dy", ".71em")
						.style("text-anchor", "end")
						.text("Degrees Celsius");
									
					//Change name of city in heading
					var cityName = data.city.name;
					document.getElementById("cityName").innerHTML = cityName;
			
				}
				
				function visualiseClouds() {				
					
					x.domain(xdomain);
					y.domain([0, 100]);
				
					//enter section
					var bar = cloudChart.selectAll("g")
						.data(list)
							.enter().append("g")
							.attr("transform", function(d, i) { return "translate(" + x(xdomain[i]) + ",0)"; })
							
						bar.append("rect")
							.attr("y", function(d) { return y(d.clouds); })
							.attr("height", function(d) { return height - y(d.clouds); })
							.attr("width", x.rangeBand());
							
						bar.append("text")
							.attr("class", "barText")
							.attr("x", x.rangeBand() / 2)
							.attr("y", function(d) { return y(d.clouds) + 3; })
							.attr("dy", ".75em")
							.text(function(d) { return d.clouds; });
					
					//update section
					var bar = cloudChart.selectAll("g")
						.data(list)
							
						bar.select("rect")
							.attr("y", function(d) { return y(d.clouds); })
							.attr("height", function(d) { return height - y(d.clouds); });
						  
						bar.select("text")
							.attr("class", "barText")
							.attr("x", x.rangeBand() / 2)
							.attr("y", function(d) { return y(d.clouds) + 3; })
							.attr("dy", ".75em")
							.text(function(d) { return d.clouds; });
							
					cloudChart.append("g")
						.attr("class", "x axis")
						.attr("transform", "translate(0," + height + ")")
						.call(xAxis);
						
						
					yAxis.tickFormat(function(d) { return d + "%"; });

					cloudChart.append("g")
						.attr("class", "y axis")
						.call(yAxis)
					  .append("text")
						.attr("transform", "rotate(-90)")
						.attr("y", -50)
						.attr("dy", ".71em")
						.style("text-anchor", "end")
						.text("Cloudiness");
				
					
					//Change name of city in heading
					var cityName = data.city.name;
					document.getElementById("cityName").innerHTML = cityName;
			
				}
					
				function changeCity()
				{
					//This function is called by the button to change city
					
					var city = document.getElementById("city").value;
					console.log("City name:" + city);
					
					//Build url for the new city
					var url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=" + city + "&mode=json&units=metric&cnt=7&appid=139534f48d889a380b62e96132eb44fd"
					getData(url);
				}
				
				//Starts visualisation when page loads the first time.. url is for Dublin
				var url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=Dublin,ireland&mode=json&units=metric&cnt=7&appid=139534f48d889a380b62e96132eb44fd"
				getData(url);
			
				//Date messing
				//d.date = new Date(data.unix_timestamp * 1000)
				var convertDate = function(d) {
					return new Date(d.dt * 1000);
				}