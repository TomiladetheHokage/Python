import os


current_dir = os.getcwd()
print('current directory is: ',current_dir)

lyric_file = os.path.abspath("lyric")
print("the file path for lyric is: ", lyric_file)

files_and_directories = os.listdir()
print("files and dir: ", files_and_directories)