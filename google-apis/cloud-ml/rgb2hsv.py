from PIL import Image
import colorsys
import glob

with open("skintones.txt", "w") as pixeldata:
	for filename in glob.glob("*.bmp"):
		im = Image.open(filename)
		print(im)

		r,g,b = im.split()
		Hdat = []
		Sdat = []
		Vdat = []
		for r, g, b in zip(r.getdata(), g.getdata(), b.getdata()):
			h, s, v = colorsys.rgb_to_hsv(r / 255., g / 255., b / 255.)
			Hdat.append(int(h * 99.))
			Sdat.append(int(s * 99.))
			Vdat.append(int(v * 99.))
		
		im_hsv = list(zip(Hdat, Sdat, Vdat))
		for pixel in im_hsv:
			pixeldata.write("%d,%d,%d\n" % (pixel[0], pixel[1], pixel[2]))
