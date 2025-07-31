# Import all tkinter functions for making GUI
from tkinter import *

# Import message box for showing error messages
import tkinter.messagebox as tmsg


# Create Calculator class to organize all calculator code
class Calculator():
    
    # Initialize method - runs when Calculator object is created
    def __init__(self, master):
        
        # Store the main window reference
        self.master = master
        
        # Set window title at top
        master.title("Calculator")
        
        # Set window size (width x height)
        master.geometry("300x400")
        
        # Optional: prevent window resizing
        # master.resizable(False, False)
        
        # Set main window background color to dark blue
        master.config(bg="#0f0f23")

        # Variable to store current expression (like "2+3")
        self.expression = ""
        
        # Special variable to show text in entry field
        self.input_text = StringVar()

        # Create frame container for input field
        input_frame = Frame(master, bd=3, relief=SUNKEN, bg="#1a1a2e")
        
        # Place input frame at top, fill horizontally, with padding
        input_frame.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)

        # Create text entry field for showing numbers and results
        input_field = Entry(input_frame, textvariable=self.input_text, justify=RIGHT, 
                          bg="#ecf0f1", width=21, font="Arial 18")
        
        # Place entry field in grid position 0,0 with padding
        input_field.grid(row=0, column=0, sticky="nsew", ipady=5)

        # Make input frame row 0 expand when window resizes
        input_frame.grid_rowconfigure(0, weight=1)
        
        # Make input frame column 0 expand when window resizes
        input_frame.grid_columnconfigure(0, weight=1)

        # Create frame container for all calculator buttons
        btns_frame = Frame(master, bg="#0f0f23")
        
        # Place button frame below input, fill remaining space
        btns_frame.pack(fill=BOTH, expand=True, padx=10, pady=5)

        # Make button rows 1-5 expand equally when window resizes
        for i in range(1, 6):  # rows 1-5 (buttons only)
            btns_frame.grid_rowconfigure(i, weight=1)
            
        # Make button columns 0-3 expand equally when window resizes
        for i in range(4):  # 4 columns
            btns_frame.grid_columnconfigure(i, weight=1)

        # List of all buttons with their text and grid positions
        # Format: (button_text, row_number, column_number)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('(',5,1),(')',5,2) 
        ]

        # Loop through each button in the list
        for (text, row, col) in buttons:
            
            # Check if current button is equals sign
            if text == '=':
                # Create green equals button that calls Calculate method
                button = Button(btns_frame, text=text, fg="white", bg="#00ff88", 
                              font=('Arial', 18, 'bold'), bd=0, relief=RIDGE,
                              command=self.Calculate)
                              
            # Check if current button is clear button
            elif text == 'C':
                # Create red clear button that calls Clear_input method
                button = Button(btns_frame, text=text, fg="white", bg="#ff3366", 
                              font=('Arial', 18, 'bold'), bd=0, relief=RIDGE,
                              command=self.Clear_input)
                              
            # Check if current button is an operator (+, -, *, /)
            elif text in ['+', '-', '*', '/','(',')']:
                # Create purple operator button that calls Button_click method
                button = Button(btns_frame, text=text, fg="white", bg="#9d4edd",
                              font=('Arial', 18, 'bold'), bd=0, relief=RIDGE,
                              command=lambda t=text: self.Button_click(t))
                              
            # All other buttons are numbers and decimal point
            else:
                # Create light gray number button that calls Button_click method
                button = Button(btns_frame, text=text, fg="#0f0f23", bg="#e0e1dd", 
                              font=('Arial', 18, 'bold'), bd=0, relief=RIDGE,
                              command=lambda t=text: self.Button_click(t))

            # Place button in grid at specified row and column position
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

    # Method that runs when number or operator button is clicked
    def Button_click(self, item):
        
        # Add clicked button text to current expression
        self.expression += str(item)
        
        # Update display to show new expression
        self.input_text.set(self.expression)

    # Method that runs when Clear button is clicked
    def Clear_input(self):
        
        # Reset expression to empty
        self.expression = ""
        
        # Clear the display
        self.input_text.set("")

    # Method that runs when equals button is clicked
    def Calculate(self):
        
        # Try to calculate the result (might fail with invalid input)
        try:
            # Use eval to calculate expression and convert to string
            result = str(eval(self.expression))
            
            # Show result in display
            self.input_text.set(result)
            
            # Save result as new expression for continued calculations
            self.expression = result
            
        # If calculation fails (like dividing by zero)
        except Exception as e:
            
            # Show error message popup
            tmsg.showerror("Error", "Invalid Input or Calculation Error")
            
            # Reset expression to empty
            self.expression = ""
            
            # Clear the display
            self.input_text.set("")


# Check if this file is being run directly (not imported)
if __name__ == '__main__':
    
    # Create main window
    root = Tk()
    
    # Create calculator object with main window
    my_calculator = Calculator(root)
    
    # Start the GUI event loop (keeps window open)
    root.mainloop()