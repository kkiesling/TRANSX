# download data from Fendl 3.1b
import os


def download_data(data_path):
	print('Downloading Fendl 3.1b data to ./data/')
	os.system("wget https://www-nds.iaea.org/fendl/data/neutron/fendl31b-neutron-matxs.zip")
	print('Extracting Data')
	os.system("unzip fendl31b-neutron-matxs.zip -d {}".format(data_path))
	os.system("rm fendl31b-neutron-matxs.zip")
	
	
def main():
	### DOWNLOAD DATA ###
	data_path = './data/'
	
	# check if data folder already exist
	if os.path.isdir(data_path):	
		# if folder is empty download data
		if not os.listdir(data_path):		
			download_data(data_path)
		else:
			# assume data exists
			print("Data already exists")
	else:
		# Folder does not exist so create folder
		os.system("mkdir data")
		# get data
		download_data(data_path)
		

if __name__ == "__main__":
	main()
