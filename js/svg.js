function wrap(text, width, height) {
  text.each(function(idx,elem) {
    var text = $(elem);
    text.attr("dy",height);
        var words = text.text().split(/\s+/).reverse(),
        word,
        line = [],
        lineNumber = 0,
        lineHeight = 1.1, // ems
        y = text.attr("y"),
        dy = parseFloat( text.attr("dy") ),
        tspan = text.text(null).append("tspan").attr("x", 0).attr("y", y).attr("dy", dy + "em");
    while (word = words.pop()) {
      line.push(word);
      tspan.text(line.join(" "));
      if (elem.getComputedTextLength() > width) {
        line.pop();
        tspan.text(line.join(" "));
        line = [word];
        tspan = text.append("tspan").attr("x", 0).attr("y", y).attr("dy", ++lineNumber * lineHeight + dy + "em").text(word);
      }
    }
  });
}
// *************************************************************
// NPI
// *************************************************************
var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
svg.setAttribute("viewBox", "0 0 211 220");
svg.setAttribute("width", "210.96037");
svg.setAttribute("height", "280.96036");
svg.setAttribute("class","boxbasic");

// *************************************************************
// Definitions
// *************************************************************
var strokewidth = 1;

// *************************************************************
// MUSA-BOX
// *************************************************************
var svgNS = svg.namespaceURI;

    // ID
    var rect = document.createElementNS(svgNS,'rect');
    rect.setAttribute('x',0.47906977);
    rect.setAttribute('y',-25.98737);
    rect.setAttribute('width',210);
    rect.setAttribute('height',20);
    rect.setAttribute('stroke-width',strokewidth);
    svg.appendChild(rect);
    // TIEMPO ESTIMADO
    var rect = document.createElementNS(svgNS,'rect');
    rect.setAttribute('x',0.47906977);
    rect.setAttribute('y',14.01263);
    rect.setAttribute('width',70);
    rect.setAttribute('height',20);
    rect.setAttribute('stroke-width',strokewidth);
    svg.appendChild(rect);
    // TIEMPO TARDIO INICIO
    var rect = document.createElementNS(svgNS,'rect');
    rect.setAttribute('x',70.479073);
    rect.setAttribute('y',14.01263);
    rect.setAttribute('width',70);
    rect.setAttribute('height',20);
    rect.setAttribute('stroke-width',strokewidth);
    svg.appendChild(rect);
    // TIEMPO TARDIO FINALIZACIÓN
    var rect = document.createElementNS(svgNS,'rect');
    rect.setAttribute('x',140.47903);
    rect.setAttribute('y',14.01263);
    rect.setAttribute('width',70);
    rect.setAttribute('height',20);
    rect.setAttribute('stroke-width',strokewidth);
    svg.appendChild(rect);
    // TIEMPO TEMPRANO FINALIZACIÓN
    var rect = document.createElementNS(svgNS,'rect');
    rect.setAttribute('x',140.47906);
    rect.setAttribute('y',-5.9873743);
    rect.setAttribute('width',70);
    rect.setAttribute('height',20);
    rect.setAttribute('stroke-width',strokewidth);
    svg.appendChild(rect);
    // TIEMPO TEMPRANO INICIO
    var rect = document.createElementNS(svgNS,'rect');
    rect.setAttribute('x',70.479073);
    rect.setAttribute('y',-5.9873705);
    rect.setAttribute('width',70);
    rect.setAttribute('height',20);
    rect.setAttribute('stroke-width',strokewidth);
    svg.appendChild(rect);
    // ALGO QUE NO RECUERDO :v Casilla 1
    var rect = document.createElementNS(svgNS,'rect');
    rect.setAttribute('x',0.47907066);
    rect.setAttribute('y',-5.9873705);
    rect.setAttribute('width',70);
    rect.setAttribute('height',20);
    rect.setAttribute('stroke-width',strokewidth);
    svg.appendChild(rect);

    // OPERACIONES
    var rect = document.createElementNS(svgNS,'rect');
    rect.setAttribute('x',0.47906214);
    rect.setAttribute('y',114.01263);
    rect.setAttribute('width',210);
    rect.setAttribute('height',80);
    rect.setAttribute('stroke-width',strokewidth);
    svg.appendChild(rect);
    // ATRIBUTOS
    var rect = document.createElementNS(svgNS,'rect');
    rect.setAttribute('x',0.47906977);
    rect.setAttribute('y',34.01263);
    rect.setAttribute('width',210);
    rect.setAttribute('height',80);
    rect.setAttribute('stroke-width',strokewidth);
    svg.appendChild(rect);

    document.body.appendChild(svg);
    var svg2 = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg2.setAttribute("viewBox", "0 0 211 220");
    svg2.setAttribute("width", "210.96037");
    svg2.setAttribute("height", "280.96036");

    var element = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    element.setAttributeNS(null, 'x', '50%');
    element.setAttributeNS(null, 'y', -11);
    element.setAttribute('textLength',100);
    element.setAttribute('fill',"red");
    element.setAttribute('font-size',10);

    var txt = document.createTextNode("Hello World");
    element.appendChild(txt);
    svg2.appendChild(element);


    document.body.appendChild(svg2);
