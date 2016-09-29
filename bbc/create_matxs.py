# download data from Fendl 3.1b
import os

def main():

    datapath = "../data"
    for filename in sorted(os.listdir(datapath)):

        # move the text file to current directory and call it text
        path = '{}/{}'.format(datapath, filename)
        os.system("cp {} text".format(path))

        # get name of nuclide to call new matxs file
        f = open("text", 'r')
        line = f.readline()
        name = line.split('*')[1][9:].strip()
        f.close()

        # run bbc to get matx file
        os.system("bbc < makebbc")

        # move matx file to new name
        os.system("mv matx ../matxsdata/{}".format(name))

        # remove extra files created
        os.system("rm index text")

if __name__ == "__main__":
    main()
