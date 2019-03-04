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
import numpy as np
import os

MUSABOX = []
MUSABOX.append('\
<svg xmlns:dc="http://purl.org/dc/elements/1.1/"\n \
  xmlns:cc="http://creativecommons.org/ns#"\n \
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n \
  xmlns:svg="http://www.w3.org/2000/svg"\n \
  xmlns="http://www.w3.org/2000/svg"\n \
  xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"\n \
  xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"\n'
  + '   width="' + str(100) +'"\n \
  height="100">\n \
  <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />\n \
</svg>')


# *****************************************************************************
# Write File
# *****************************************************************************
f = open ("images/MUSA-BOXTEST.svg", "w")

for item in MUSABOX:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass


f.close()

# os.chdir("images")
# os.chdir("../")
