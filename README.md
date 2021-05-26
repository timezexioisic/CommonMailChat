# Common Mail Chat 

CMC is a Python tool which allows you to chat in a terminal by sharing a spare Email account credentials. It only requires Python installed and an Email account dedicated to it. 

# Usage
## Email account
You will need to create an Email account and share the credentials with those you trust and want to chat with. WARNING: Do not share any personal information in any way with those you do not trust.
## Installation
You can enter the following commands:
```
git clone <link>
```
```
cd CommonMailChat
```
```
python cmc.py
```
# How it works
CMC uses smtplib along with imaplib to send and receive Email messages with the credentials the User has put, and it sends the mails to the same Email ID which contains time, username, and the message given by any user. It then collects all n number of mails sent through the account assuming it has been created for CMC and prints it. 

# License
You are allowed to edit and publish the source code wherever you want by linking the developer's GitHub inside the file.
