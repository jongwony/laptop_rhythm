'use strict';

var width = 800,
    height = 600,
    radius = Math.min(width, height) / 2;

var color = d3.scale.category20()
    .domain(['active', 'deactive', 'remain']);

var arc = d3.arc()
    .outerRadius(radius - 10)
    .innerRadius(radius - 100);

var arcs = d3.pie()
    .sort(null)
    .value(function(d) { return d.delta; })( {{ data() }} );

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

var g = svg.selectAll(".arc")
    .data(arcs)
    .enter().append("g")
    .attr("class", "arc");

g.append('path')
    .attr('d', arc)
    .attr('data-legend', function(d) { return d.data.flag; })
    .attr('fill', function(d) { return color(d.data.flag); });

svg.append('g')
    .attr('class', 'legend')
    .attr('transform', 'translate(0, 0)')
    .call(d3.legend)

// g.append('text')
//     .attr('transform', function(d) { return 'translate(' + arc.centroid(d) + ')'; })
//     .attr('dy', '.35em')
//     .text(function(d) { return d.data.delta + '\r\n' + d.data.flag; });