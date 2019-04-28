#
# #############################################################################
#       Copyright (c) 2019 mfneirae.com All Rights Reserved.
#
#                This work  is licensed under a Creative Commons
#       Attribution-NonCommercial - ShareAlike 4.0 International
#       License and MIT Licence.
#
#       by Manuel Neira Embus.
#
#       For more information write me to jai@mfneirae.com
#       Or visit my webpage at https://mfneirae.com/
# #############################################################################
#

def drawfiles():
    from svglib.svglib import svg2rlg
    from reportlab.graphics import renderPDF, renderPM
    drawing = svg2rlg("images/MUSA-BOXTESTWB.svg")
    renderPDF.drawToFile(drawing, "images/MUSA.pdf")
    renderPM.drawToFile(drawing, "images/MUSA.png", fmt="PNG")
