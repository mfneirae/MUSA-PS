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
import data
import musabox
import savepng

CODE = '0002'
CODEN = str(CODE)
data.importdata(CODEN)
musabox.createbox(data.ID,data.EST,data.EFT,CODE,data.DURATION,data.LST,data.LFT,data.ATTRIBUTES,data.OPERATIONS)

savepng.drawfiles()
