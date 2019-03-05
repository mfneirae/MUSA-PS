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
# *****************************************************************************
# SVG for page
# *****************************************************************************
def createbox(ID,EST,EFT,CODE,DURATION,LST,LFT,ATTRIBUTES,OPERATIONS):
    MUSABOX = []
    MUSABOXWB = []
    MUSABOX.append('\
    <svg xmlns:dc="http://purl.org/dc/elements/1.1/"\n \
      xmlns:cc="http://creativecommons.org/ns#"\n \
      xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n \
      xmlns:svg="http://www.w3.org/2000/svg"\n \
      xmlns="http://www.w3.org/2000/svg"\n \
      xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"\n \
      xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"\n \
      viewBox="0 0 211 221" \n \
      version="1.1" \n \
      sodipodi:docname="MUSA-BOX.svg" \n \
      width="210.96037" \n \
      height="220.96036"> \n \
      <g \n \
         inkscape:label="Layer 1" \n \
         inkscape:groupmode="layer" \n \
         id="layer1" \n \
         transform="translate(0.00112024,26.467552)"> \n \
    <!-- ID BOX --> \n \
         <rect \n \
           id="ID-0001" \n \
           width="210" \n \
           height="20" \n \
           x="0.47907066" \n \
           y="-25.98737" /> \n \
         <text \n \
           id="IDTEXT-0001" \n \
           y="-12" \n \
           transform="translate(100)"> \n \
           <tspan x="0" text-anchor="middle"> \n' \
    + str(ID) + '\n ' \
    + '         </tspan> \n \
        </text> \n \
    <!-- EARLY START TIME BOX -->  \n \
         <rect \n \
            id="EST-0001" \n \
            width="70" \n \
            height="20" \n \
            x="0.47907066" \n \
            y="-5.9873705" \n \
            /> \n \
         <text \n \
            id="ESTTEXT-0001" \n \
            y="10" \n \
            transform="translate(33)"> \n \
            <tspan x="0" text-anchor="middle"> \n' \
     + str(EST) + '\n ' \
     + '         </tspan> \n \
         </text> \n \
    <!-- EARLY FINISH TIME BOX -->  \n \
         <rect \n \
            id="EFT-0001" \n \
            width="70" \n \
            height="20" \n \
            x="0.47906977" \n \
            y="14.01263"/> \n \
          <text \n \
             id="EFTTEXT-0001" \n \
             y="30" \n \
             transform="translate(33)"> \n \
             <tspan x="0%" text-anchor="middle"> \n' \
      + str(EFT) + '\n ' \
      + '         </tspan> \n \
          </text> \n \
    <!-- CODE BOX -->  \n \
          <rect \n \
             id="CODE-0001" \n \
             width="70" \n \
             height="20" \n \
             x="70.479073" \n \
             y="-5.9873705" \n \
             /> \n \
         <text \n \
            id="CODETEXT-0001" \n \
            y="10" \n \
            transform="translate(33)"> \n \
            <tspan x="33.3%" text-anchor="middle"> \n' \
     + str(CODE) + '\n ' \
     + '         </tspan> \n \
         </text> \n \
    <!-- DURATION -->  \n \
         <rect \n \
            id="DURATION-0001" \n \
            width="70" \n \
            height="20" \n \
            x="70.479073" \n \
            y="14.01263" \n \
            /> \n \
          <text \n \
             id="DURATIONTEXT-0001" \n \
             y="30" \n \
             transform="translate(33)"> \n \
             <tspan x="33.3%" text-anchor="middle"> \n' \
      + str(DURATION) + '\n ' \
      + '         </tspan> \n \
          </text> \n \
    <!-- LATE START TIME -->  \n \
          <rect \n \
             id="LST-0001" \n \
             width="70" \n \
             height="20" \n \
             x="140.47906" \n \
             y="-5.9873743" \n \
             /> \n \
         <text \n \
            id="LSTTEXT-0001" \n \
            y="10" \n \
            transform="translate(33)"> \n \
            <tspan x="66.6%" text-anchor="middle"> \n' \
     + str(LST) + '\n ' \
     + '         </tspan> \n \
         </text> \n \
    <!-- LATE FINISH TIME -->  \n \
         <rect \n \
            id="LFT-0001" \n \
            width="70" \n \
            height="20" \n \
            x="140.47903" \n \
            y="14.012629" \n \
            /> \n \
        <text \n \
           id="LFTTEXT-0001" \n \
           y="30" \n \
           transform="translate(33)"> \n \
           <tspan x="66.6%" text-anchor="middle"> \n' \
    + str(LST) + '\n ' \
    + '         </tspan> \n \
        </text>  \n \
    <!-- ATTRIBUTES BOX -->  \n \
        <rect  \n \
           id="ATTRIBUTES-0001" \n \
           width="210" \n \
           height="80" \n \
           x="0.47906977" \n \
           y="34.01263" /> \n \
         <text \n \
            id="ATTRIBUTESTEXT-0001" \n \
            y="60" \n \
            transform="translate(0)"> \n \
            <tspan x="10" text-anchor="start"> \n' \
     + str(ATTRIBUTES) + '\n ' \
     + '         </tspan> \n \
         </text> \n \
        <rect \n \
           id="OPERATIONS-0001" \n \
           width="210" \n \
           height="80" \n \
           x="0.47906214" \n \
           y="114.01263" /> \n \
       <text \n \
          id="OPERATIONSTEXT-0001" \n \
          y="140" \n \
          transform="translate(0)"> \n \
          <tspan x="10" text-anchor="start"> \n' \
   + str(OPERATIONS) + '\n ' \
   + '         </tspan> \n \
          <tspan x="10" y="160" text-anchor="start"> \n' \
   + str(OPERATIONS) + '\n ' \
   + '         </tspan> \n \
          <tspan x="10" y="180" text-anchor="start"> \n' \
   + str(OPERATIONS) + '\n ' \
   + '         </tspan> \n \
        </text> \n \
       </g> \n '\
       +'</svg>')
# *****************************************************************************
# Withe background
# *****************************************************************************
    MUSABOXWB.append('\
  <svg xmlns:dc="http://purl.org/dc/elements/1.1/"\n \
    xmlns:cc="http://creativecommons.org/ns#"\n \
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n \
    xmlns:svg="http://www.w3.org/2000/svg"\n \
    xmlns="http://www.w3.org/2000/svg"\n \
    xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"\n \
    xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"\n \
    viewBox="0 0 211 221" \n \
    version="1.1" \n \
    sodipodi:docname="MUSA-BOX.svg" \n \
    width="210.96037" \n \
    height="220.96036"> \n \
    <g \n \
       inkscape:label="Layer 1" \n \
       inkscape:groupmode="layer" \n \
       id="layer1" \n \
       transform="translate(0.00112024,26.467552)"> \n \
  <!-- ID BOX --> \n \
       <rect \n \
         fill="none" \n \
         stroke="black" \n \
         id="ID-0001" \n \
         width="210" \n \
         height="20" \n \
         x="0.47907066" \n \
         y="-25.98737" /> \n \
       <text \n \
         id="IDTEXT-0001" \n \
         y="-12" \n \
         transform="translate(100)"> \n \
         <tspan x="0" text-anchor="middle"> \n' \
  + str(ID) + '\n ' \
  + '         </tspan> \n \
      </text> \n \
  <!-- EARLY START TIME BOX -->  \n \
       <rect \n \
         fill="none" \n \
         stroke="black" \n \
          id="EST-0001" \n \
          width="70" \n \
          height="20" \n \
          x="0.47907066" \n \
          y="-5.9873705" \n \
          /> \n \
       <text \n \
          id="ESTTEXT-0001" \n \
          y="10" \n \
          transform="translate(33)"> \n \
          <tspan x="0" text-anchor="middle"> \n' \
   + str(EST) + '\n ' \
   + '         </tspan> \n \
       </text> \n \
  <!-- EARLY FINISH TIME BOX -->  \n \
       <rect \n \
         fill="none" \n \
         stroke="black" \n \
          id="EFT-0001" \n \
          width="70" \n \
          height="20" \n \
          x="0.47906977" \n \
          y="14.01263"/> \n \
        <text \n \
           id="EFTTEXT-0001" \n \
           y="30" \n \
           transform="translate(33)"> \n \
           <tspan x="0%" text-anchor="middle"> \n' \
    + str(EFT) + '\n ' \
    + '         </tspan> \n \
        </text> \n \
  <!-- CODE BOX -->  \n \
        <rect \n \
           fill="none" \n \
           stroke="black" \n \
           id="CODE-0001" \n \
           width="70" \n \
           height="20" \n \
           x="70.479073" \n \
           y="-5.9873705" \n \
           /> \n \
       <text \n \
          id="CODETEXT-0001" \n \
          y="10" \n \
          transform="translate(33)"> \n \
          <tspan x="33.3%" text-anchor="middle"> \n' \
   + str(CODE) + '\n ' \
   + '         </tspan> \n \
       </text> \n \
  <!-- DURATION -->  \n \
       <rect \n \
         fill="none" \n \
         stroke="black" \n \
          id="DURATION-0001" \n \
          width="70" \n \
          height="20" \n \
          x="70.479073" \n \
          y="14.01263" \n \
          /> \n \
        <text \n \
           id="DURATIONTEXT-0001" \n \
           y="30" \n \
           transform="translate(33)"> \n \
           <tspan x="33.3%" text-anchor="middle"> \n' \
    + str(DURATION) + '\n ' \
    + '         </tspan> \n \
        </text> \n \
  <!-- LATE START TIME -->  \n \
        <rect \n \
           fill="none" \n \
           stroke="black" \n \
           id="LST-0001" \n \
           width="70" \n \
           height="20" \n \
           x="140.47906" \n \
           y="-5.9873743" \n \
           /> \n \
       <text \n \
          id="LSTTEXT-0001" \n \
          y="10" \n \
          transform="translate(33)"> \n \
          <tspan x="66.6%" text-anchor="middle"> \n' \
   + str(LST) + '\n ' \
   + '         </tspan> \n \
       </text> \n \
  <!-- LATE FINISH TIME -->  \n \
       <rect \n \
         fill="none" \n \
         stroke="black" \n \
          id="LFT-0001" \n \
          width="70" \n \
          height="20" \n \
          x="140.47903" \n \
          y="14.012629" \n \
          /> \n \
      <text \n \
         id="LFTTEXT-0001" \n \
         y="30" \n \
         transform="translate(33)"> \n \
         <tspan x="66.6%" text-anchor="middle"> \n' \
  + str(LST) + '\n ' \
  + '         </tspan> \n \
      </text>  \n \
  <!-- ATTRIBUTES BOX -->  \n \
      <rect  \n \
         fill="none" \n \
         stroke="black" \n \
         id="ATTRIBUTES-0001" \n \
         width="210" \n \
         height="80" \n \
         x="0.47906977" \n \
         y="34.01263" /> \n \
       <text \n \
          id="ATTRIBUTESTEXT-0001" \n \
          y="60" \n \
          transform="translate(0)"> \n \
          <tspan x="10" text-anchor="start"> \n' \
   + str(ATTRIBUTES) + '\n ' \
   + '         </tspan> \n \
       </text> \n \
      <rect \n \
         fill="none" \n \
         stroke="black" \n \
         id="OPERATIONS-0001" \n \
         width="210" \n \
         height="80" \n \
         x="0.47906214" \n \
         y="114.01263" /> \n \
     <text \n \
        id="OPERATIONSTEXT-0001" \n \
        y="140" \n \
        transform="translate(0)"> \n \
        <tspan x="10" text-anchor="start"> \n' \
 + str(OPERATIONS) + '\n ' \
 + '         </tspan> \n \
        <tspan x="10" y="160" text-anchor="start"> \n' \
 + str(OPERATIONS) + '\n ' \
 + '         </tspan> \n \
        <tspan x="10" y="180" text-anchor="start"> \n' \
 + str(OPERATIONS) + '\n ' \
 + '         </tspan> \n \
      </text> \n \
     </g> \n '\
     +'</svg>')
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

    f = open ("images/MUSA-BOXTESTWB.svg", "w")
    for item in MUSABOXWB:
        try:
            f.write(item)
        except UnicodeEncodeError:
            pass
    f.close()
