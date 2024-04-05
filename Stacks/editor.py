"""
Class Implementation
The Editor class is designed to simulate a simple text editor with undo and redo functionalities, using
the concept of Stacks. Let's explore its components:

1. Initialization (__init__ method):

The editor starts with empty text (self.text).
Two lists, self.history_stack and self.redo_stack, 
are initialized to keep track of the changes for undo and redo operations, respectively.

2. Appending Text (append_text method):

Before appending new text, the current state of the text (self.text)
is saved onto the history_stack. This allows the undo operation
to revert to this prior state.

The new text is then appended to self.text.

3. Undoing Changes (undo method):

Checks if there is any text history in the history_stack.
If so, the current text is saved onto the redo_stack 
(allowing this action to be redone later) before reverting
self.text to the last saved state from history_stack.
If there's no history, it indicates that undoing is not possible.

4. Redoing Changes (redo method):

Checks if there is any redo history in the redo_stack.
If so, the current text is saved onto the history_stack 
(allowing this action to be undone later) before updating 
self.text to the last saved state from redo_stack.

If there's no redo history, it indicates that redoing is not possible.

5. Displaying the Text (display_text method):

Simply prints the current state of the text to the console.

"""

class Editor:
    def __init__(self):
        self.text = ""
        self.cursor_position = 0  # Initialize the cursor at the start of the text
        self.history_stack = []
        self.redo_stack = []

    def insert_text(self, text):
        self.history_stack.append(self.text)
        self.text = self.text[:self.cursor_position] + text + self.text[self.cursor_position:]
        # Update cursor position to the end of the inserted text
        self.cursor_position += len(text)

    def insert_text_at_position(self, text, position):
        self.history_stack.append(self.text)
        # Ensure the insertion position does not exceed the text length or go below 0
        position = max(0, min(position, len(self.text)))
        self.text = self.text[:position] + text + self.text[position:]

    def delete_text(self, length):
        self.history_stack.append(self.text)
        if length > 0:  # Delete text after the cursor
            end_position = min(len(self.text), self.cursor_position + length)
            self.text = self.text[:self.cursor_position] + self.text[end_position:]
        elif length < 0:  # Delete text before the cursor
            start_position = max(0, self.cursor_position + length)
            self.text = self.text[:start_position] + self.text[self.cursor_position:]
            self.cursor_position = start_position

    def move_cursor(self, position):
        # Ensure cursor position is within the boundaries of 'self.text'
        self.cursor_position = max(0, min(position, len(self.text)))

    def undo(self):
        if self.history_stack:
            self.redo_stack.append(self.text)
            self.text = self.history_stack.pop()
        else:
            print("Undo operation not possible. No history available.")

    def redo(self):
        if self.redo_stack:
            self.history_stack.append(self.text)
            self.text = self.redo_stack.pop()
        else:
            print("Redo operation not possible. No redo history available.")

    def display_text(self):
        print(self.text)
    
    def clear_text(self):
        self.history_stack.append(self.text)
        self.text = ""


editor = Editor()

editor = Editor()
editor.insert_text("Hello, CodeSignal users!")
editor.display_text()  # Output: "Hello, CodeSignal users!"
editor.move_cursor(7)  # Move cursor to a position after 'Hello,'
editor.delete_text(-5)  # Deletes "Hello"
editor.display_text()  # Output: ", CodeSignal users!"
editor.insert_text_at_position("Hello again", 0)  # Inserts text at the start
editor.display_text()  # Output: "Hello again, CodeSignal users!"