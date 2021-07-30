import os
import shutil

BASE_PATH = ('input_folder')
DESTINATION_PATH = ('output_folder')

target_extentions = ['.jpg', '.png']

file_counted = 0
target_counter = 0 
for folder, subfolders, r in os.walk(BASE_PATH):
	# print(folder, r)
	if folder and r:
		for item in r:
			file_counted+=1
			src = os.path.join( folder, item)
			dst = os.path.join(DESTINATION_PATH, item)
			# print('src', src)
			# print('dst', dst)

			if any(x in item for x in target_extentions):
				target_counter+=1 
				shutil.copyfile(src, dst)
				# shutil.move(src, dst)

print('Done..'+'\n'+f'{target_counter} of {file_counted} files have been copied')



