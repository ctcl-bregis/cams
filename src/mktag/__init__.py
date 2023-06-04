# CAMS Software - CTCL 2021-2023
# April 21, 2023 - May 12, 2023
# Purpose: ID tag vector image generator

import qrcode, json
from io import BytesIO
from reportlab.graphics import renderPDF, renderPM
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg

config_dir = "config/mktag/"

# Template
class doc:
    def __init__(self, tagfmt):
        with open(config_dir + "base_tags.json") as f:
            basetags = json.loads(f.read())
        
        if tagfmt in basetags["base_tags"]:
            self.tagfmt = tagfmt
        else:
            raise Exception
            
        
    def mktagdoc(self, data, pos, options):
        buf = BytesIO()
        pagesize = (72 * basetags["base_tags"][tagfmt]["docwidth"], 72 * basetags["base_tags"][tagfmt]["docheight"])
        c = canvas.Canvas(buf, pagesize = pagesize) 
        
        
        
        # Make the QR code
        qrecc = basetags["base_tags"][tagfmt]["qrecc"]
        
        if qrecc = "L":
            qrecc = qrcode.constants.ERROR_CORRECT_L
        elif qrecc = "M":
            qrecc = qrcode.constants.ERROR_CORRECT_M
        elif qrecc = "Q":
            qrecc = qrcode.constants.ERROR_CORRECT_Q
        elif qrecc = "H":
            qrecc = qrcode.constants.ERROR_CORRECT_H
        else:
            raise Exception("Invalid QR Code ECC value")
            
        qr = qrcode.make(data, image_factory =  qrcode.image.svg.SvgImage)
        
        
        tagpdf = buf.getvalue()
        
        return tagpdf
        
