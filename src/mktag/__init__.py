# CAMS Software
# CTCL 2021-2023
# ???, 2022 - March 27, 2023
# Purpose: App initialization

import qrcode
import json
from reportlab.graphics import renderPDF, renderPM
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg

class idtag:

     def __init__(self, data, bt):
         # Class object is initiated with the data to encode and a base_tags entry
         self.d = data
         self.t = bt
         
