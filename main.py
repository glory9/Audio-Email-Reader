# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
from playsound import playsound

# These modules are imported to connect to/parse user email
import imaplib
import email

mail = imaplib.IMAP4_SSL('imap.gmail.com')

# Login with user email and password
while True:
    try:
        mail.login(input('Email address: '), input('Password: '))
        print('\nLogin successful...\n')
        break
    except:
        print('Invalid login credentials/Access disabled. Please try again/enable access.\n')
        continue
        
mail.list()
mail.select('inbox')

result, data = mail.uid('search', None, "ALL")
i = len(data[0].split())
j = 1

email_uid = data[0].split()[i - 7]
result, email_data = mail.uid('fetch', email_uid, '(RFC822)')
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
email_message = email.message_from_string(raw_email_string)

print('Parsing email...\n')
# this will loop through all the available multiparts in mail
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        # ignore attachments/html
        body = part.get_payload(decode=True)
        mytext = body.decode('utf-8').strip()
        
        # currently working on the code that goes here. this part 
        # filters the parsed text of unnecessary details like external 
        # link addresses/long URLs and repeated visual symbols.
        
        # lauguage is 'en' (English)
        myobj = gTTS(text=mytext, lang='en', slow=False)

        # Saving the converted audio in a mp3 file
        myobj.save("audio.mp3")

        print('Reading email...\n')
        # play recorded file
        playsound("UserDirectory\\audio.mp3")

    else:
        continue
