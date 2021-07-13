import os
import sys

mylist = [".zip", ".rar", ".gz", ".tar", ".pem"]
directory = "./"
binary_file_list = []
file_size_list = []
exclude_dir = set([".git"])
max_file_size_allowed = 10485760
max_file_size_allowed_MB = 10
for root, subdirectories, files in os.walk(directory):
	subdirectories[:] = [d for d in subdirectories if d not in exclude_dir]
	for file in files:
		if any(file.endswith(s) for s in mylist):
			binary_file_list.append(os.path.join(root, file))
		if os.path.getsize(os.path.join(root, file))>max_file_size_allowed:
			file_size_list.append(os.path.join(root, file))
if binary_file_list and file_size_list:
	print("Below Files are Binaries:")
	for file in binary_file_list:
		print(file)
	print("\nBelow Files are more than "+str(max_file_size_allowed_MB)+" MB:")
	for file in file_size_list:
		print(file)
	print("\nCommit includes binary files and files are bigger than 10 MB in size. Please re-commit correct file.")
	sys.exit()
elif binary_file_list:
	print("Below Files are Binaries:")
	for file in binary_file_list:
		print(file)
	print("\nCommit includes binary files. Please re-commit correct file.")
	sys.exit()
elif file_size_list:
	print("Below Files are more than "+str(max_file_size_allowed_MB)+" MB:")
	for file in file_size_list:
		print(file)
	print("\nFiles are bigger than "+str(max_file_size_allowed_MB)+" MB. Please re-commit correct file.")
	sys.exit()
else:
	print("All Files in commit looks good.")
