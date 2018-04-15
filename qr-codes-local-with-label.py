#!/usr/bin/python
#generates qr codes using python-qrcode module
#pass file with data as arguement, delimited by line-breaks

import sys
import qrcode

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

def qr_gen(data, count):
        qr = qrcode.QRCode(
            version=6,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=12,
            border=6,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        img.save(str(count) + '.' + data + '.png')
        qr.clear()

def add_label_to_qr(data, count):
	font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 20)
	imagename = str(count) + '.' + data + '.png'
	data = imagename.rstrip('.png')
	img = Image.open(imagename)
	if img.mode != "RGB":
		img = img.convert("RGB")
	draw = ImageDraw.Draw(img)
	draw.text((65,40), text=data, fill=(0,0,0), font=font)
	img.save(imagename)

def iterate_data(filename, count=0):
	f = open(filename)
	contents = f.readlines()
	for i in contents:
		count += 1
		data = i.strip('\n')
		qr_gen(data, count)
		add_label_to_qr(data, count)

def main():
	if len(sys.argv) < 2:
		print "You need to pass filename containing data as argument!"
		sys.exit(1)
	else:
		iterate_data(sys.argv[1])


if __name__ == "__main__":
	main()

