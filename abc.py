from tkinter import *
question_answers = {
    'Admission Process': 'The admission process involves appearing for the LPUNEST test, document verification, allotment, verification fee submission, joining classes, and maintaining 75% attendance.',
    'Courses Offered': 'Lovely Professional University offers a variety of courses including MCA, BCA, B.Tech, and Commerce.',
    'Fee Structure': 'The fee structure for the courses is as follows:\nMCA: Rs. 3,00,000\nBCA: Rs. 4,00,000\nB.Tech: Rs. 15,00,000\nCommerce: Rs. 2,00,000.',
    'Scholarships': 'Lovely Professional University provides scholarships based on category:\nCategory 1: Rs. 20,000\nCategory 2: Rs. 15,000\nCategory 3: Rs. 10,000.',
    'Contact Information': 'Lovely Professional University\nJalandhar-Delhi, G.T. Road,\nPhagwara, Punjab\n(INDIA) - 144411.\nTel: +91-1824-517000\nTel: +91-1824-404404.'
}

def send_message(message):
    display_message(message)

def display_message(message):
    text.configure(state=NORMAL)
    text.insert(END, "\n" + message)
    text.configure(state=DISABLED)

def handle_button_click(question):
    # Get the answer corresponding to the clicked question
    answer = question_answers.get(question)
    send_message(f"Bot: {answer}")

def handle_user_input():
    user_input = input_entry.get().strip().lower()  # Convert input to lowercase for case-insensitive matching
    if user_input.startswith('hi'):
        send_message("Bot: Hello there!")
    elif user_input == 'hi how are you?':
        send_message("Bot: I'm fine, thank you! How can I assist you?")
    elif user_input == 'hi i need information about admission':
        handle_button_click('Admission Process')
    elif user_input == 'hi what courses do you offer?':
        handle_button_click('Courses Offered')
    elif user_input == 'hi what is the fee structure?':
        handle_button_click('Fee Structure')
    elif user_input == 'hi do you provide scholarships?':
        handle_button_click('Scholarships')
    elif user_input == 'hi how can I contact you?':
        handle_button_click('Contact Information')
    else:
        send_message("Bot: Sorry, I didn't understand that.")

root = Tk()
root.title('College Admission Chatbot')

# Set minimum and maximum window size
root.minsize(600, 500)
root.maxsize(600, 500)

# Create frame for buttons
button_frame = Frame(root)
button_frame.grid(row=0, column=1, padx=5, pady=5, sticky='ne')

# Set the size of the message box
message_box_width = 50  # Adjust width as needed to maintain 500px ratio
message_box_height = 20  # Adjust height as needed to maintain 500px ratio

text = Text(root, bg='lightgrey', fg='black', wrap=WORD, height=message_box_height, width=message_box_width)
text.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
text.configure(state=DISABLED)

input_entry = Entry(root, width=40)
input_entry.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

send_button = Button(root, text='Send', command=handle_user_input)
send_button.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

# Create buttons for each question inside the frame
for i, question in enumerate(question_answers.keys()):
    button = Button(button_frame, text=question, width=20, command=lambda q=question: handle_button_click(q))
    button.grid(row=i, column=0, padx=5, pady=5, sticky='ew')

# Add image in the bottom-right corner
# robot_image = PhotoImage(file='robot.png')  # Change 'robot.png' to your image file path
# robot_label = Label(root, image=robot_image)
# robot_label.grid(row=1, column=2, padx=5, pady=5, sticky='se')

root.mainloop()