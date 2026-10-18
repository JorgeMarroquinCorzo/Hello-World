import tkinter as tk


def show_greeting():
  # Get the name from the input field
  name = entry.get()

  # print("Hello,", name + " Glad to have you here!")
  result_label.config(text=f"Hello, {name} Glad to have you here!")


# Create main window
root = tk.Tk()
root.title("Python Hello World GUI")
root.geometry("400x250")

#print("Hello " + "World!")
label1 = tk.Label(root, text="Hello World!", font=("Arial", 11))
label1.pack(pady=2)

# print("I love programming in Python.")
label2 = tk.Label(root, text="I love programming in Python.", font=("Arial", 11))
label2.pack(pady=2)

#print("I am learning", "how to write code.", sep="\n")
label3 = tk.Label(
    root, text="I am learning\nhow to write code.", font=("Arial", 11), justify="center"
)
label3.pack(pady=5) # pady = 5 means 5 pixels of vertical padding around the label

# Prompt for name (replacing input("Enter your name: "))
prompt_label = tk.Label(
    root, text="Enter your name:", font=("Arial", 11, "bold")
)
prompt_label.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 11), width=25)
entry.pack(pady=2)

# Button to submit and trigger the final print/greeting equivalent
submit_btn = tk.Button(root, text="Submit", command=show_greeting)
submit_btn.pack(pady=8)

# Label that displays the final greeting output
result_label = tk.Label(root, text="", font=("Arial", 11, "bold"))
result_label.pack(pady=5)

root.mainloop()


#print("Hello " + "World!")
#print("I love programming in Python.")
#print("I am learning", "how to write code.", sep="\n")
#name = input("Enter your name: ")
#print("Hello,", name + " Glad to have you here!")
