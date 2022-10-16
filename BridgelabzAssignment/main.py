# Python code to illustrate Sending mail from your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("sheikhnafisha95@gmail.com", "sheikh321")

sender = 'sheikhnafisha95@gmail.com'
receivers = ['mrinalrajput3@gmail.com', 'sudhasahu52@gmail.com']

# message to be sent
message = """From: From Person <sheikhnafisha95@gmail.com>
To: To Person <mrinalrajput3@gmail.com> and <sudhasahu52@gmail.com>

Subject: SMTP e-mail test

Hello, how are you???
This is to notify that tomorrow is holiday due to festival."""

# sending the mail
s.sendmail(sender, receivers, message)

# terminating the session
s.quit()
