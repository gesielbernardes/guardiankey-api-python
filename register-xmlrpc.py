
import base64
import os
from Crypto.Cipher import AES
import xmlrpclib


def register(email):
	guardianKeyXML='https://ws.guardiankey.net'
	
	keyb64 = base64.b64encode(os.urandom(32))
	ivb64  = base64.b64encode(os.urandom(16))
	notify_method = 'email'
	notify_data = base64.b64encode('{"smtp_method":"TLS","smtp_host":"smtp.example.foo","smtp_port":"587","smtp_user":"myuser","smtp_pass":"mypass"}')	
	proxy = xmlrpclib.ServerProxy(guardianKeyXML)
	hashid = proxy.register(email,keyb64,ivb64,notify_method,notify_data)
	
	
	return hashid,keyb64,ivb64


email = raw_input( "Enter the administrator e-mail:")
hashid,key,iv = register(email)

message = 'Put in your configuration this values:\n\
		   email: {}\n\
		   hashid: {}\n\
		   key: {}\n\
		   iv: {}\n'

print message.format(email,hashid,key,iv)


