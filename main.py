# -*- coding: utf-8 -*- 

import sys


def main(fir_num, sec_num):

	fn = int(fir_num.replace(',',''))
	sn = int(sec_num.replace(',',''))

	answer = fn * sn
	print (answer)

if __name__ == "__main__":
	if(len(sys.argv) != 3):
		print ("##### ERROR: Please provide a first and second number to multiply")
		print ("***** Example: python main.py 2 3")
		print ("Exiting...")
		sys.exit()
	fir_num = sys.argv[1]
	sec_num = sys.argv[2]
	main(fir_num, sec_num)