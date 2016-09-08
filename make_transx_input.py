# download data from Fendl 3.1b
import os
import argparse

def get_save_path():
	parser = argparse.ArgumentParser(description=
		'Downloads Fendl3.1b data for neutrons (MATXS) and creates a TRANSX input.')
	parser.add_argument('-s', nargs='?', type=str, default='$HOME/fendl3.1b/',
		help='path to save downloaded data', required=False)
	parser.add_argument('-d', nargs='?', type=str, 
		default='https://www-nds.iaea.org/fendl/data/neutron/fendl31b-neutron-matxs.zip', 
		help='URL to the data, default is Fendl3.1 data', required=False)


def main():
	# get the path to download and save
	# path to fendl https://www-nds.iaea.org/fendl/
	parser = argparse.ArgumentParser(description=
		'Downloads Fendl3.1b data for neutrons (MATXS) and creates a TRANSX input.')
	parser.add_argument('-s', nargs='?', type=str, default='$HOME/fendl3.1b/',
		help='path to save downloaded data', required=False)
	parser.add_argument('-d', nargs='?', type=str, 
		default='https://www-nds.iaea.org/fendl/data/neutron/fendl31b-neutron-matxs.zip', 
		help='URL to the data, default is Fendl3.1 data', required=False)
	# download and extract data
	
	# read files and create input
	




if __name__ == "__main__":
	main()
