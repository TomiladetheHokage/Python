import os
#
destination_dir = os.path.join(os.getcwd(), "test1")
if not os.path.exists(destination_dir):
    os.mkdir(destination_dir)
#
src_file = os.path.join(os.getcwd(), "sample", "file")
destination_dir = os.path.join(os.getcwd(), "test1", "file")

os.rename(src_file, destination_dir)

print(destination_dir)
#
