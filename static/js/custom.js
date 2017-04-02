'use strict';

// var circle = [{'x': 50, 'y': 50, 'r': 40, 'stroke': 'green', 'stroke_width': 4, 'fill': 'yellow'}];
// var rect_ex1 = [{'width': 30, 'height': 10, 'fill': 'steelblue', 'stroke_width': 3}]

// var svg = d3.select('body')
//     .append('svg')
//     .attr('width', 100)
//     .attr('height', 100);

// var svg2 = d3.select('body')
//     .append('svg')
//     .attr('width', 400)
//     .attr('height', 180);

// svg.selectAll('.ex1')
//     .data(circle)
//     .enter()
//     .append('circle')
//     .attr({
//        'cx': function (d) { return d.x; },
//        'cy': function (d) { return d.y; },
//        'r': function (d) { return d.r; },
//        'stroke': function(d) { return d.stroke; },
//        'stroke-width': function(d) { return d.stroke_width; },
//         'fill': function(d) { return d.fill; }
//     });

// svg.selectAll('.ex1')
//     .data(rect_ex1)
//     .enter()
//     .append('rect')
//     .each(function(d) {
//         d3.select(this).attr({
//             width: d.width,
//             height: d.height,
//             fill: d.fill,
//             'stroke-width': d.stroke_width
//         });
//     });

// svg2.selectAll('.ex2')
//     .data(rect_ex2)
//     .enter()
//     .append('rect')
//     .each(function(d) {
//         d3.select(this).attr({
//             x: d.x,
//             y: d.y,
//             width: d.width,
//             height: d.height,
//             fill: d.fill,
//             stroke: d.stroke,
//             opacity: d.opacity,
//             'stroke_opacity': d.stroke_opacity
//         });
//     });


///// { DICTIONARY } /////

var svg3 = d3.select('body')
    .append('svg')
    .attr({
        'width': 400,
        'height': 180
    });

var rect_ex3 = {x: 50, y: 20, width: 150, height: 150};

svg3.append('rect')
    .attr('class', 'ex3_rect')
    .attr(rect_ex3);

// svg3.selectAll('.ex3_rect')
//     .data(rect_ex3)
//     .enter()
//     .append('rect')
//     .each(function(d) {
//         d3.select(this).attr({
//             class: 'ex3_rect',
//             x: d.x,
//             y: d.y,
//             width: d.width,
//             height: d.height
//         });
//     });


///// EASY /////

var svg4 = d3.select('body')
    .append('svg')
    .attr({
        width: 500,
        height: 210,
    });

svg4.append('rect')
    .attr({
        x: 10,
        y: 10,
        width: 50,
        height: 100,
    });

//// POLYGON with Data ////

var svg6 = d3.select('body')
    .append('svg')
    .attr({
        height: 210,
        width: 500,
    });

var points = [[100,10],[40,198],[190,78],[10,78],[160,198]];

svg6.append('polygon')
    .attr({
        'class': 'star',
        'points': points.join(' '),
    });

//// POLYLINE ////

var svg5 = d3.select('body')
    .append('svg')
    .attr({height: 200, width: 500});

svg5.append('polyline')
    .attr('class', 'polyline')
    .attr('points', '20,20 40,25 60,40 80,120 120,140 200,180');

//// PATH ////

var svg7 = d3.select('body')
    .append('svg')
    .attr({ height: 210, width: 400})

svg7.append('path')
    .attr('d', 'M 150 0 L 75 200 L 225 200 Z');