from PIL import Image
import csv
import os

path = '/a-images'
workingdir = os.listdir(os.getcwd())

with open('compatible.csv', 'wt', encoding='utf8') as csvfile:

	for filename in workingdir:

		if filename[-3:] == 'png':
			im = Image.open(filename)
			pix = im.load()
			colorVal = pix[1,1]

			asin = filename[25:-12]


			if colorVal[0] == 51:
				compat = False
			else:
				compat = True

			spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow([asin, str(compat)])


#readamazoncomkpkshareasinB010N7QO04-clipped.png
#readamazoncomkpkshareasinB00LFQMV4G-clipped.png