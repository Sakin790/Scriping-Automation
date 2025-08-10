import os

# os.mkdir("newFolder",)
#os.makedirs("parent/child/grandchild", exist_ok=True)
#os.remove(path)
#os.rmdir("empty_folder")  # Deletes 'empty_folder'
#os.removedirs("parent/child/grandchild")  # Removes empty directories up to 'parent'
#os.rename("old_name.txt", "new_name.txt")  # Renames file
#print(os.listdir("."))

"""
os.getcwdb()
"""
inx = os.listdir()
print(inx)
"""
stats = os.stat("file.txt")
print(stats.st_size)  # File size in bytes
print(stats.st_mtime)



os.chmod(path,mode)

"""