last_id = 0

# class Note:                              #this are bulding blocks for the program NO PRINT
#     def __init__(self, message):
#         self.message = message 
#         global last_id # the only time global has a use case is only when you want to track one use case
#         last_id += 1 # the next note will never have the value of the prior note
#         self.id = last_id

#     def __repr__(self):
#         return f"{self.id}|{self.message}"
#     def update_note(self): # all methods begin with def and has self
#         new_message = input ("What is the new message?\n> ")
#         self.message = new_message

# # a_note = Note ("Hello world")


# a_note = Note("Hello World") # Dot notation, you ise the class obj, then the value that it is stored in  in this case id
# print(a_note.id)
# print(a_note.message)



class Menu:   
    def __init__(self):
        self.notes = []

    def new_note(self, message):
        self.notes.append(Note(message))

    def _find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
            return None
    def update_message(self, note_id, message):
            note = self._find_note(note_id)
            if note:
                note.message = message
            return True
            return False

nb = Notebook()

# nb.new_note("This is a note")
# print(nb.notes)
# nb.update_message(1, "This is an updated note")
# print(nb.notes)





 # nb = Notebook()

# nb.new_note("this is a note")
# nb.new_note("this is note two")

# for nt in nb.notes:
#     print(nt.id, nt.message)
