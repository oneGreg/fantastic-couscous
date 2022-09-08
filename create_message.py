#inspired by https://gist.github.com/jeremykdev/a489d95e628b8217429c53624f225b50

# Prototype to create an eml file using python

import os
import uuid
from email import generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# where to write the output file
directory = "./out"

#fromAddress, toAddress, subject, body

fromAddress = "jane@example.com"
toAddress = "joe@example.com"
subject = "test"
body = "Hello email!"

def create_message():
    msg = MIMEMultipart()
    msg["To"] = toAddress
    msg["From"] = fromAddress
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    return msg

def write_eml_file(msg):
    os.chdir(directory)
    filename = str(uuid.uuid4()) + ".eml"

    with open(filename, 'w') as file:
        emlGenerator = generator.Generator(file)
        emlGenerator.flatten(msg)

def main():
    msg = create_message()
    write_eml_file(msg)
    

if __name__ == "__main__":
    main()