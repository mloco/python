from subprocess import call

import csv
with open('asins.csv', 'rt', encoding='utf8') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		commandUrl = 'webkit2png https://read.amazon.com/kp/kshare?asin=' + str(row[0]) + ' -C --clipwidth=50 --clipheight=50'
		call(commandUrl, shell=True)
		#print(commandUrl)
		print(', '.join(row))






#call('webkit2png https://read.amazon.com/kp/kshare?asin=B00BATEIEO', shell=True)