# download data from Fendl 3.1b
import os
import argparse as ap
import glob

def download_data(datapath):
	print('Downloading Fendl 3.1b data to ./data/')
	os.system("wget https://www-nds.iaea.org/fendl/data/neutron/fendl31b-neutron-matxs.zip")
	print('Extracting Data')
	os.system("unzip fendl31b-neutron-matxs.zip -d {}".format(datapath))
	os.system("rm fendl31b-neutron-matxs.zip")
	
def card1():
	c = "Fendl 3.1b Neutron Data\n"
	return(c)

def card2():
	
	#if 'IPRINT' in kwargs:
	#	IPRINT = kwargs['IPRINT']
	#else:
	#	IPRINT = 0
	#	print("Set Card 2 IPRINT to default value 0 (long)")
	#
	#if 'IOUT' in kwargs:
	#	IOUT = kwargs['IOUT']
	#else:
	#	IOUT = 0
	#	print("Set Card 2 IOUT to default value 0 (fido)")
		
	c = "idk what to do with this card yet\n"
	return c

def card3(datapath):
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
	NMIX = len(glob.glob1(datapath, "*.m"))

	# NREG - number of regions, assume 1
	NREG = 1
	
	# NMIXS = number of mix specifications
	NMIXS = NMIX + 0 # IDK what makes this > NMIX
	
	# NED = number of extra edits, always assume 7 for heat, kerma, dame, dpa,
	# t, he, and h
	NED = 7
	
	# NEDS = ????
	NEDS = NED + 0
	
	c = "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}\n".format(NGROUP, NL,
															NTABL, NUP,
															NTHG, NMIX,
															NREG, NMIXS,
															NED, NEDS)
	return c, NMIX
	
def card4(datapath):
	# For every .m file in the datapath, reads line 1 to get name
	c = ""
	names = []
	
	for filename in sorted(os.listdir(datapath)):
		# read line 1
		path = '{}/{}'.format(datapath, filename)
		f = open(path, 'r')
		line = f.readline()
		name = line.split('*')[1][9:].strip()
		c += name + " "
		names.append(name)
		f.close()
	
	c = c.rstrip() +"\n"
	return c, names
	
def card5():
	return "r1/\n"

def card6():
	# no card 6 in the samples?
	return ""
	
def card7(names):
	c = ""
	for i, mix in enumerate(names):
		c += "{} 1 {}/\n".format(i, mix)
	
	return c
	
def card8():
	HED = ['heat', 'kerma', 'dame', 'dpa', 't', 'he', 'h']
	c = '{0} {1} {2} {3} {4} {5} {6}\n'.format(HED[0], HED[1], HED[2], HED[3], 
											   HED[4], HED[5], HED[6])
	return c, HED

def card9(datapath, HED, n_TF, g_TF):
	c = ""

	for i, edit in enumerate(HED):
		
		# assume all mixes are used in heat with standard multiplier
		if edit == 'heat':
			# check if writing for neutron, gammas, or both
			if n_TF:
				c += '{} heat/\n'.format(i)
			if g_TF:
				c += '{} gheat/\n'.format(i)
		
		# assume all mixes are used in kerma with standard multiplier
		elif edit == 'kerma':
			# check if writing for neutron, gammas, or both
			if n_TF:
				c += '{} kerma/\n'.format(i)
			if g_TF:
				c += '{} gheat/\n'.format(i)
		
		# assume all mixes are used in dame with standard multiplier
		elif edit == 'kerma':
			c += '{} dame/\n'.format(i)
		
		# need to check files contain dame? but they all do
	
	for filename in sorted(os.listdir(datapath)):
		# read line 1
		path = '{}/{}'.format(datapath, filename)
		#f = open(path, 'r')
		 
	
	return ""

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
	datapath = './data/'
	
	# check if data folder already exist
	if os.path.isdir(datapath):	
		# if folder is empty download data
		if not os.listdir(datapath):		
			download_data(datapath)
		else:
			# assume data exists
			print("Data already exists in ./data/. Will not download.")
	else:
		# Folder does not exist so create folder
		os.system("mkdir data")
		# get data
		download_data(datapath)
		
	# Use neutron or gamma or both
	# set both to true for now
	n_TF = True
	g_TF = True
	
	### CREATE INPUT ###  
	# create a string for each card individually
	
	# card 1 - Title
	c1 = card1()
	
	# card 2 - Options
	## make optional card arguments, otherwise defaults?
	c2 = card2()
	
	# card 3 - Parameters
	# This has to be done after the rest maybe?
	c3, NMIX = card3(datapath)
	
	# card 4 - Mix Names
	c4, names = card4(datapath)
	
	c5 = card5()
	
	c6 = card6()
	
	c7 = card7(names)
	
	c8, HED = card8()
	
	c9 = card9(datapath, HED, n_TF, g_TF)
	
	total = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8
	#print(total)

if __name__ == "__main__":
	main()
