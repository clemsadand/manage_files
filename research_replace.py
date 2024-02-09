import os

#file_name = "4/annotations/4_aud4-2.svl"


def research_replace(file_name):
	f = open(file_name, "r")

	fnew = open("audio.txt", "w")

	for line in f.readlines():
		line = line.replace("Yes", "1")
		line = line.replace("No", "0")
		fnew.write(line)

	os.system("mv audio.txt "+file_name)

folder_path = "4/annotations/"

files = os.listdir(folder_path)

for f in files:
	research_replace(folder_path+f)
