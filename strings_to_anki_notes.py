strings_to_file_lines = ['awhen considering a desorder you should consider {{c1::diagnoses}}{{c1::developmental causes}}{{c1::biological causes}}{{c1::social causes}}{{c1::psychological traits}}	', 'bwhen considering a desorder you should consider {{c1::diagnoses}}{{c1::developmental causes}}{{c1::biological causes}}{{c1::social causes}}{{c1::psychological traits}}	', 'cwhen considering a desorder you should consider {{c1::diagnoses}}{{c1::developmental causes}}{{c1::biological causes}}{{c1::social causes}}{{c1::psychological traits}}	']

def send_to_file (strings_to_file_lines):
	with open("to_be_imported.txt","w") as f:
		for n in strings_to_file_lines:
			f.write(n+'\t\n')

def insert_close_deletion(text_of_the_note, note_counter, close_delection_content):
	return text_of_the_note.replace(close_delection_content, '{{c' + str(note_counter) + '::'+close_delection_content + '}}')


def create_close_deletions(text_of_the_note, close_deletions):
	print(text_of_the_note, '\n', close_deletions)
	text_of_the_note = text_of_the_note[1:]
	note_counter = 0
	for i in close_deletions:
		if i[0] == 'n' or i == close_deletions[0]:
			note_counter +=1
		text_of_the_note = insert_close_deletion(text_of_the_note, note_counter, i[1:])
	print(text_of_the_note)
	return text_of_the_note

def file_to_text_and_close_deletions(file_name):
	list_of_notes = []
	with open(file_name) as f:
		content = f.readlines()

		text_of_the_note = ''
		close_deletions = []

		for line in content:
			if line[0] == 't':
				print('t found')
				if text_of_the_note != '' and close_deletions != []:
					list_of_notes.append(create_close_deletions(text_of_the_note, close_deletions))
					close_deletions = []
					text_of_the_note = ''
				text_of_the_note = line

			elif line[0] == 'n' or line[0] == 'c':
				print('n or c found')
				close_deletions.append(line[:-1])

			else:
				print("a line starts with an invalid line, the following line doesn't start with a t, b, nor c", '\n', line)

		if text_of_the_note != '' and close_deletions != []:
			list_of_notes.append(create_close_deletions(text_of_the_note, close_deletions))

	return list_of_notes

def main():
	list_of_notes = file_to_text_and_close_deletions('to_be_processed.txt')
	#t is for the text of the note
	#n if for new close deletion
	#c is for continue the close deletion
	send_to_file(list_of_notes)






def main_of_a_single_note():
	list_of_notes = file_to_text_and_close_deletions('to_be_processed.txt')
	#t is for the text of the note
	#n if for new close deletion
	#c is for continue the close deletion

	# for testing purposes
	text_of_the_note = 'tthis is a new note with this and this sharing a closed deletion and this as its own closed deletion'
	close_deletions = ['nwith this and', 'cthis sharing', 'nthis as']

	# turn into loop
	string_of_note = create_close_deletions(text_of_the_note, close_deletions)




	list_of_notes.append(string_of_note)
	send_to_file(list_of_notes)

main()