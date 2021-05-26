"""
Common mail chat v1.1

Credits:
	email, email.header, webbrowser, os, smtplib, imaplib
Developer:
	Time
Version:
	1.1
"""			
try:#<- To get the name from namefile
	nf = open("namefile","r")
	tmp_usrnm = str(nf.read())
except:
	tmp_usrnm = input("Your name: ")
	nf = open("namefile","w+")
	nf.close()
	nf = open("namefile","a")
	nf.write(tmp_usrnm)
	nf.close()
try:#<- To get the Email account credentials from the credfile
	creds = open("credfile","r")
	credis = str(creds.read())
	credis = credis.split("\n")
	gmail_user = credis[0]
	gmail_password = credis[1]
except:
	print("WARNING: No valid credfile found. (Re) enter the account credentials. It is expected that you use a new different common account")
	tmp_u = input("Email ID: ")
	tmp_p = input("Password: ")
	print("IMPORTANT: You may have to allow less secure apps to login under your account settings")
	creds = open("credfile","w+")
	creds.close()
	creds = open("credfile","a")
	cred_text = str(tmp_u + "\n" + tmp_p)
	creds.write(cred_text)
	creds.close()
	creds = open("credfile","r")
	credis = str(creds.read())
	credis = credis.split("\n")
	gmail_user = credis[0]
	gmail_password = credis[1]
	creds.close() 	
while True:#<- Main run
	import smtplib
	import os
	from datetime import datetime
	name_given = True
	def send_txt(name):#<- Function to send message with a name
		name_given = False
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)#<- Server setup
		server.ehlo()
		server.login(gmail_user,gmail_password)#<- Logging in
		sent_from = gmail_user
		to_1 = [gmail_user]
		email_text_sub = input("│\n│─Username: " + name + "\n" + "│─Message: ")
		if email_text_sub[1] == "$":
			os.system("rm impfile.tibunk")
		print("\nSending message...\n")
		now = datetime.now()
		time_crt = now.strftime("%d/%m/%Y %H:%M:%S")#<- Time format
		email_text = """\
		
	Time: %s
	Username: %s	
	Message: %s

		""" % (time_crt,name,email_text_sub)
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)#<- Another server setup
		server.ehlo()
		try:
			server.login(gmail_user,gmail_password)
		except:
			print("Incorrect password. Edit or delete the credfile to fix")	
		server.sendmail(sent_from,to_1,email_text)
		server.close()
		
	import imaplib
	from email.header import decode_header                             
	import email
	import webbrowser
	import os
	  
	print("\n[%s]Fetching messages...\n" % (gmail_user))  
	server ="imap.gmail.com"                     
	imap = imaplib.IMAP4_SSL(server)
	    
	imap.login(gmail_user,gmail_password)               
	  
	res, messages = imap.select('"[Gmail]/Sent Mail"')   
	  
	messages = int(messages[0])
	n = 8#<- Number of messages to fetch, the higher the number the more time taken to fetch
	txt_msg_data = []
	try:#<- To recieve a number of messages
		txt_msg_data = []
		for i in range(messages, messages - n, -1):
			res, msg = imap.fetch(str(i), "(RFC822)")     
			for response in msg:
				if isinstance(response, tuple):
					msg = email.message_from_bytes(response[1])
					msg_from = msg["From"]
					subject = msg["Subject"]
					msg_from = str(msg_from)
					msg_from = msg_from.replace("[","").replace("]","").replace(gmail_user,"")\
					.replace(gmail_user,"").replace("<","").replace(">","").replace("","")\
					.replace("	","")
					txt_msg_data.append(msg_from)
		
	except:
		pass
		
	txt_msg_data.reverse()
	for tmpmsg in txt_msg_data:
		new_data = tmpmsg.split("\n")
		for crrnt_msg in new_data:
			if "e" in crrnt_msg:
				print("│─" + crrnt_msg)
			else:
				print("│")	
	txt_msg_data.clear()																					
																				
	send_txt(tmp_usrnm)
	os.system("clear")