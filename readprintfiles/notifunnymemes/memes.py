name_of_mydocument = 'poem.txt'
file_input = open(name_of_mydocument, 'r')

name_of_outputdocument = 'myoutputdocument.txt'
file_output = open(name_of_outputdocument, 'w')

whole_poem = file_input.read()
file_input.close()

file_output.write("This File is a Copy of the Poem\n\n")

file_output.write(whole_poem)

file_output.close()

