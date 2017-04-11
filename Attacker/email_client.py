import smtplib
from sys import argv

# Implement checks for command line input?

fromaddr = 'irritatingdoggo@gmail.com'
toaddrs  = argv[1]
content = "Your key is random"
msg = "\r\n".join([
  "From: " + fromaddr,
  "To: " + toaddrs,
  "Subject: Randomware Key",
  "",
  content
  ])
username = fromaddr
password = 'annoyingdog'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()