import imaplib
import email
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(input('email address: '), input('password: '))
mail.list()
mail.select('inbox')

result, data = mail.uid('search', None, "ALL")
i = len(data[0].split())

email_uid = data[0].split()[i - 7]
result, email_data = mail.uid('fetch', email_uid, '(RFC822)')
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

# converts byte literal to string removing b''
email_message = email.message_from_string(raw_email_string)

# this will loop through all the available multiparts in mail
print('Parsing email...\n')
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        # ignore attachments/html
        body = part.get_payload(decode=True)
        print(body.decode('utf-8').strip())
        
        # code to connect to google text-to-speech API

    else:
        continue
