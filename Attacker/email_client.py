import smtplib
import poplib
from email import parser

def parse_id(obj):
	eid = ""
	start = end = 0
	for i in range(len(obj)):
		if obj[i] == '<': 
			start = i + 1
		if obj[i] == '>': 
			end = i
	return obj[start:end]

def send_mail(toaddrs):
	fromaddr = 'irritatingdoggo@gmail.com'
	password = 'annoyingdog'
	username = fromaddr
	
	content = "Your key is random"
	msg = "\r\n".join([
	  "From: " + fromaddr,
	  "To: " + toaddrs,
	  "Subject: Randomware Key",
	  "",
	  content
	  ])

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()

def parse_email(message):

	if message.is_multipart():
	    for part in message.walk():
	        ctype = part.get_content_type()
	        cdispo = str(part.get('Content-Disposition'))

	        # skip any text/plain (txt) attachments
	        if ctype == 'text/plain' and 'attachment' not in cdispo:
	            body = part.get_payload(decode=True)  # decode
	            break
	# not multipart - i.e. plain text, no attachments, keeping fingers crossed
	else:
	    body = message.get_payload(decode=True)
	return message['From'] , body.rstrip()

pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('irritatingdoggo@gmail.com')
pop_conn.pass_('annoyingdog')
#Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
# Concat message pieces:
messages = ["\n".join(mssg[1]) for mssg in messages]
#Parse message intom an email object:
messages = [parser.Parser().parsestr(mssg) for mssg in messages]
for message in messages:
	email_id, body = parse_email(message)
	if body == 'Shekar is a faggot': # Add a function to check gift card
		send_mail(parse_id(email_id))
pop_conn.quit()




