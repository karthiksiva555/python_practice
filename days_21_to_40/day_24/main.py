from days_21_to_40.day_24.file_manager import FileManager

file_manager = FileManager()

def show_file():
    print(file_manager.read_file_context_manager())

# show contents of my_file.txt
print(file_manager.read_file_manual_close())
show_file()

# write contents into my_file.txt
file_manager.write_to_file("Tech is awesome!")
show_file()

# append content to my_file.txt
file_manager.append_to_file("Python is the most popular language in AI.")
show_file()

# create new file and write contents into it
FileManager.create_and_write_to_file("new_file.txt", "Everyday learning is one step closer to success.")
# write some content again and make sure write works with an existing file as well.
FileManager.create_and_write_to_file("new_file.txt", "Reading books is powerful.")
file_manager.read_file_context_manager("new_file.txt")
