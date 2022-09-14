#!/usr/bin/env python3
import imaplib
import ssl
import email.message
import email.charset
import time

tls_context = ssl.create_default_context()

server = imaplib.IMAP4('imap.mydomain.com')
server.starttls(ssl_context=tls_context)
server.login('email@mydomain.com', 'password')
# Select mailbox
server.select("INBOX.Drafts")
# Create message
new_message = email.message.Message()
new_message["From"] = "Your name <sender@mydomain.com>"
new_message["To"] = "Name of Recipient <recpient@mydomain.com>"
new_message["Subject"] = "Your subject"
new_message.set_payload("""
This is your message.
It can have multiple lines and
contain special characters: äöü.
""")
# Fix special characters by setting the same encoding we'll use later to encode the message
new_message.set_charset(email.charset.Charset("utf-8"))
encoded_message = str(new_message).encode("utf-8")
server.append('INBOX.Drafts', '', imaplib.Time2Internaldate(time.time()), encoded_message)
# Cleanup
server.close()