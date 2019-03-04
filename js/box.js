//
// #
// # #############################################################################
// #       Copyright (c) 2019 mfneirae.com All Rights Reserved.
// #
// #                This work  is licensed under a Creative Commons
// #       Attribution-NonCommercial - ShareAlike 4.0 International
// #       License and MIT Licence.
// #
// #       by Manuel Neira Embus.
// #
// #       For more information write me to jai@mfneirae.com
// #       Or visit my webpage at https://mfneirae.com/
// # #############################################################################
// #
// *****************************************************************************
// BLOBAL VARIABLES
// *****************************************************************************
var a;
var svgDoc;
var ID;
var IDTEXT;
var EST;
var EFT;
var CODE;
var LST;
var DURATION;
var LFT;
var ATTRIBUTES;
var ATTRIBUTESTEXT;
var OPERATIONS;
var OPERATIONSTEXT;
// *****************************************************************************
// START
// *****************************************************************************
window.onload=function() {
a = document.getElementById('svgObject');
svgDoc = a.contentDocument;
ID = svgDoc.getElementById("ID-0001");
IDTEXT = svgDoc.getElementById("IDTEXT-0001");
EST = svgDoc.getElementById("EST-0001");
EFT = svgDoc.getElementById("EFT-0001");
CODE = svgDoc.getElementById("CODE-0001");
LST = svgDoc.getElementById("LST-0001");
DURATION = svgDoc.getElementById("DURATION-0001");
LFT = svgDoc.getElementById("LFT-0001");
ATTRIBUTES = svgDoc.getElementById("ATTRIBUTES-0001");
ATTRIBUTESTEXT = svgDoc.getElementById("ATTRIBUTESTEXT-0001");
OPERATIONS = svgDoc.getElementById("OPERATIONS-0001");
OPERATIONSTEXT = svgDoc.getElementById("OPERATIONSTEXT-0001");
//Stroke
ID.setAttribute('stroke', 'black');
ID.setAttribute('stroke-width', '3');
EST.setAttribute('stroke', 'black');
EST.setAttribute('stroke-width', '3');
EFT.setAttribute('stroke', 'black');
EFT.setAttribute('stroke-width', '3');
CODE.setAttribute('stroke', 'black');
CODE.setAttribute('stroke-width', '3');
DURATION.setAttribute('stroke', 'black');
DURATION.setAttribute('stroke-width', '3');
LST.setAttribute('stroke', 'black');
LST.setAttribute('stroke-width', '3');
LFT.setAttribute('stroke', 'black');
LFT.setAttribute('stroke-width', '3');
ATTRIBUTES.setAttribute('stroke', 'black');
ATTRIBUTES.setAttribute('stroke-width', '3');
OPERATIONS.setAttribute('stroke', 'black');
OPERATIONS.setAttribute('stroke-width', '3');
//Fill
ID.setAttribute('fill', 'none');
EST.setAttribute('fill', 'none');
EFT.setAttribute('fill', 'none');
CODE.setAttribute('fill', 'none');
DURATION.setAttribute('fill', 'none');
LST.setAttribute('fill', 'none');
LFT.setAttribute('fill', 'none');
ATTRIBUTES.setAttribute('fill', 'none');
OPERATIONS.setAttribute('fill', 'none');
//Text
ATTRIBUTESTEXT.setAttribute('font-size', '8');
OPERATIONSTEXT.setAttribute('font-size', '8');
};
// *****************************************************************************
// MUSA-BOX
// *****************************************************************************

document.getElementById('svgObject').onmouseover = function() {mouseOver()};
document.getElementById('svgObject').onmouseout = function() {mouseOut()};

function mouseOver() {
  ID.setAttribute('fill', '#FFCB3F');
  IDTEXT.setAttribute('fill', '#2F5567');
}

function mouseOut() {
  ID.setAttribute('stroke', 'black');
  IDTEXT.setAttribute('fill', 'black');
  ID.setAttribute('fill', 'none');
}
