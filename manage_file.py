import os


def check_file_name(folder_path):
	"""The goal is to check if the files in a folder have a certain name
	
	Returns : A bool 
	"""
	#load 
	files = os.listdir(folder_path)
	for f in files:
		number_of_files = 0
		#Index of the first character of f
		idn = -1
		#Check if file name contains "_"
		if "_" in f:
			idn = int(f.split("_")[0])
			print(f"Error: file name is incorrect {f}")
			#Get the id of the rasbery pi
		if idn < 0 | idn > 29:
			print(f"Error: file name is incorrect {f}")
		else:
			number_of_files += 1
	return number_of_files == len(files)

def main():
	i = input("Choose 0 for annotations folder or 1 for audios folder (1/0) : ")
	folder_path = ""
	if int(i) == 0 :
		folder_path = '4/annotations/'
	elif int(i) == 1:
		folder_path = '4/audios/'
	#
	if check_file_name(folder_path):
		print("Correct")
	

main()
