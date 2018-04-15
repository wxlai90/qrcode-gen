#!/usr/bin/python
#generates qr codes using python-qrcode module
#pass file with data as arguement, delimited by line-breaks

import sys
import qrcode #sudo apt install python-qrcode, pip install qrcode

def qr_gen(data, count):
        qr = qrcode.QRCode(
            version=6, #qrcode version
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=12,
            border=5, #change to 0 for no border
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        img.save(str(count) + "." + data + '.png')
        qr.clear()

def iterate_data(filename, count=0):
	f = open(filename)
	contents = f.readlines()
	for i in contents:
		count += 1
		qr_gen(i.strip('\n'), count)

def main():
	if len(sys.argv) < 2:
		print "You need to pass filename containing data as argument!"
		sys.exit(1)
	else:
		iterate_data(sys.argv[1])


if __name__ == "__main__":
	main()

