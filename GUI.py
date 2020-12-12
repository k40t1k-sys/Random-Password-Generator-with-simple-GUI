import tkinter as tk
import pwd_gen as pwd

class App:
	def __init__(self, master):
		self.master = master
		master.title("Random Password Generator")

		password = str(pwd.gen_pwd())
		self.label1 = tk.Label(master, text=password)
		self.label1.pack(padx=10, pady=10)

		self.new_bttn = tk.Button(master, text="Generate New Password", command=self.new_pwd)
		self.new_bttn.pack(padx=60,pady=10)

		self.copy_bttn = tk.Button(master, text="Copy", command=self.copy)
		self.copy_bttn.pack(padx=10,pady=10)

		self.close_bttn = tk.Button(master, text="Close", command=master.quit)
		self.close_bttn.pack(padx=10,pady=10)

	def copy(self):
		self.master.clipboard_clear()
		self.master.clipboard_append(self.label1.cget("text"))

	def new_pwd(self):
		password = str(pwd.gen_pwd())
		self.label1.config(text=password)


root = tk.Tk()
app = App(root)
root.mainloop()
