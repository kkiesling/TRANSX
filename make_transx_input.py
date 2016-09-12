# download data from Fendl 3.1b
import os
import argparse as ap
import glob

def download_data(data_path):
	print('Downloading Fendl 3.1b data to ./data/')
	os.system("wget https://www-nds.iaea.org/fendl/data/neutron/fendl31b-neutron-matxs.zip")
	print('Extracting Data')
	os.system("unzip fendl31b-neutron-matxs.zip -d {}".format(data_path))
	os.system("rm fendl31b-neutron-matxs.zip")
	
def card1():
	c = "Fendl 3.1b Neutron Data\n"
	return(c)

def card2(**kwargs):
	
	if 'IPRINT' in kwargs:
		IPRINT = kwargs['IPRINT']
	else:
		IPRINT = 0
		print("Set Card 2 IPRINT to default value 0 (long)")
	
	if 'IOUT' in kwargs:
		IOUT = kwargs['IOUT']
	else:
		IOUT = 0
		print("Set Card 2 IOUT to default value 0 (fido)")

	
def card3(data_path):
	# NGROUP = ??? (-217 in others)
	NGROUP = -217
	
	# NL = ??
	NL = 6
	
	# NTABL = ??
	NTABL = 227
	
	# NUP = ??
	NUP = 0
	
	# NTHG = ??
	NTHG =0
	
	# NMIX = number of mixes (ie number of *.m files)
	NMIX = len(glob.glob1(data_path, "*.m"))
	
	# NREG - number of regions, assume 1
	NREG = 1
	
	# NMIXS = number of mix specifications
	NMIXS = NMIX + 0 # IDK what makes this > NMIX
	
	# NED = number of extra edits, always assume 7 for heat, kerma, dame, dpa,
	# t, he, and h
	NED = 7
	
	# NEDS = ????
	NEDS = NED + 0
	
	c3 = "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}\n".format(NGROUP, NL,
																 NTABL, NUP,
																 NTHG, NMIX,
																 NREG, NMIXS,
																 NED, NEDS)
	return c3
	
def card4(data_path):
	# For every .m file in the data_path, reads line 1 to get name
	c4 = ""
	
	for filename in sorted(os.listdir(data_path)):
		# read line 1
		path = '{}{}'.format(data_path, filename)
		f = open(path, 'r')
		line = f.readline()
		name = line.split('*')[1][9:].strip()
		c4 += name + " "
		f.close()
	
	c4 = c4.rstrip() +"\n"
	print(c4)
	return c4
	
def card5():
	pass

def card6():
	pass
	
def card7():
	pass
	
def card8():
	pass

def card9():
	pass

def card10():
	pass
	
def card11():
	pass
	
def main():
	### NEED TO MAKE THE OPTION TO CHOOSE NEUTRON, GAMMA, OR BOTH
	
	### PARSE COMMAND LINE ARGUMENTS ###
	# -p = photons
	# -n = neutrons
	# -iprint, -iout, iprob, iset, iform, itime, idecay, itrc, icoll, initf 
	# parser = ag.ArgumentParser(description='Creates TRANSX input file')
	# parser.add_argument('-n', nargs=0, default=False, type=bool)
	# parser.add_argument('-p', nargs=0, default=False, type=bool)
	# parser.add_argument('-iprint', nargs='?', default=0, type=int)
	# parser.add_argument('-iout', nargs='?', default=3, type=int)
	# parser.add_argument('-iprob', nargs='?', default=0, type=int)
	# #parser.add_argument('-iset', nargs='1', default=0, type=int)
	# parser.add_argument('-iform', nargs='?', default=1, type=int)
	# parser.add_argument('-itime', nargs='?', default=1, type=int)
	# parser.add_argument('-idecay', nargs='?', default=0, type=int)
	# parser.add_argument('-itrc', nargs='?', default=2, type=int)
	# parser.add_argument('-icoll', nargs='?', default=0, type=int)
	
	### DOWNLOAD & EXTRACT DATA ###
	data_path = './data/'
	
	# check if data folder already exist
	if os.path.isdir(data_path):	
		# if folder is empty download data
		if not os.listdir(data_path):		
			download_data(data_path)
		else:
			# assume data exists
			print("Data already exists in ./data/. Will not download.")
	else:
		# Folder does not exist so create folder
		os.system("mkdir data")
		# get data
		download_data(data_path)
		
	
	### CREATE INPUT ###  
	# create a string for each card individually
	
	# card 1 - Title
	c1 = card1()
	
	# card 2 - Options
	## make optional card arguments, otherwise defaults?
	
	# card 3 - Parameters
	# This has to be done after the rest maybe?
	c3 = card3(data_path)
	
	# card 4 - Mix Names
	c4 = card4(data_path)
	

if __name__ == "__main__":
	main()
