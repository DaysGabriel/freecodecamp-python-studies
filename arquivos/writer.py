#books from Tolkien
file_writer = open("books.txt", "w")
file_writer.write("The Hobbit   The Fellowship of the Ring  THe two towers  The return of the king\n")
#books from CS lewis
file_writer.write("The Lion, the witch and the wardrobe     Prince Caspian      The last battle")
file_writer.close()
#uploading the file content into 2 separeted strings
Tolkien = ""
Lewis = ""

file_reader = open("books.txt","r")
file_data = file_reader.read().split("\n")

Tolkien = file_data[0]
Lewis = file_data[1]

print(Tolkien)
print(Lewis)
