import os
import sys
import pyautogui
import subprocess
import time
import smtplib
import base64
import datetime
import re
from getpass import getpass

def handle_error(err):
	print('An error occured!')
	write_log(err)
	time.sleep(5)
	sys.exit(1)


def user_inputs(): # User Inputs
	try:
		name = str(input("Type your name: "))
		write_log('User typed : ' + name)
		if name == '':
			print('Name is not valid')
			sys.exit(1)
			
		email = str(input("Type your email to recieve notifications (leave blank): "))
		if re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email):
			email_password = getpass('Type your email password : ')
			email_server = email.split('@')[1].split('.')[0]
			return [name, email, email_password, email_server]

		else:
			email = 'myemail@email.mail'
			return [name, email, None, 'email']
		
	except Exception as err:
		handle_error(err)


def webex_start(): # Starting webex
	try:
		subprocess.Popen('C:\\Users\\jimch\\AppData\\Local\\Programs\\Cisco Spark\\CiscoCollabHost.exe')
		write_log('Started Webex.')
		time.sleep(2)
	except Exception as err:
		handle_error(err)

def check_os(): # Checking wether os is linux or windows
	try:
		if os.name == 'nt':
			write_log('OS is Windows')
			return True
		if os.name == 'posix':
			write_log('OS is linux')
			print('Cisco Webex meetings aren\'t available on Linux Distributions.')
			sys.exit(1)
		else:
			write_log('Unknown OS')
			print('Your OS isn\'t compatible yet!')
			sys.exit(1)
	except Exception as err:
		handle_error(err)


def click(img, conf): # Function to click at the center of an image
	try:
		image = pyautogui.locateOnScreen('images\\' + img, confidence=conf)
		if image == None:
			print('Couldn\'t locate {} on screen'.format(img))
			time.sleep(1)
			return None
		center = pyautogui.center(image)
		x_coords, y_coords = center
		pyautogui.click(x_coords, y_coords)
		print('Clicking on {}  {}'.format(x_coords, y_coords))
		print("Clicking on x: {} y: {}".format(x_coords, y_coords))
		time.sleep(2)
	except Exception as err:
		handle_error(err)


def type_or_enter(msg, mode): # Function to type letters or just press enter
	try:
		if mode == 'type':
			pyautogui.write(msg)
			write_log('Typed:', msg)

		elif mode == 'enter':
			pyautogui.press("enter")
		else:
			print('Mode is invalid')
			sys.exit(1)
	except Exception as err:
		handle_error(err)


def send_mail(recipient, password, server, data): # Sending a notification email
	try:
		server_name = server.lower().split('.')[0]
		if server_name == 'gmail':
			mail_server = smtplib.SMTP('smtp.gmail.com', 587)
		elif server_name == 'yahoo':
			mail_server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
		elif server_name == 'zoho':
			mail_server = smtplib.SMTP('smtppro.zoho.eu', 587)
		elif server_name == 'outlook':
			mail_server = smtplib.SMTP('smtp.office365.com', 587)
		elif server_name == 'mail':
			mail_server = smtplib.SMTP('smtp.mail.com', 587)
		elif server_name == 'yandex':
			mail_server = smtplib.SMTP('smtp.yandex.com', 465)
		elif server_name == 'gmx':
			mail_server = smtplib.SMTP('smtp.gmx.com', 587)
		elif server_name == 'icloud':
			mail_server = smtplib.SMTP('smtp.mail.me.com', 587)
		elif server_name == 'email':
			return
		else:
			print('Mail server isn\'t supported')
			time.sleep(1)
			print('Supported servers : gmail, yahoo, zoho, outlook, mail, yandex, protonmail, gmx, icloud')
			sys.exit()

		mail_server.ehlo()
		mail_server.starttls()
		mail_server.login(str(recipient), str(password))
		content = "Subject: Webex Automator Mail\n\n{}".format(data)
		mail_server.sendmail(recipient, recipient, content)
		write_log('Sent an email')
		mail_server.close()

	except Exception as err:
		handle_error(err)

def convert_schedule(inputfile, outputfile): # Converting an input file to an output file using base64 encoding
	try:
		with open(inputfile, 'r') as file:
			read_file = file.read()
		with open(outputfile, 'w') as output:
			encode = base64.b64encode(read_file.encode())
			output.write(encode.decode())
	except Exception as err:
		handle_error(err)

def read_schedule(file):
	try:
		schedule = []
		with open(file, 'r') as file:
			for row in file:
				decoded = base64.b64decode(row).decode()
				schedule.append(decoded.split('\n'))
		return schedule
	except Exception as err:
		handle_error(err)


def get_time(): # This function returns a list containing the current day and time
	try:
		day = datetime.datetime.today().strftime("%A")
		hour = datetime.datetime.now().strftime("%H:%M")
		
		return [day, hour]
	except Exception as err:
		handle_error(err)
def close_webex(): # Closing Cisco Webex 
	try:
		subprocess.call("taskkill /f /im CiscoCollabHost.exe", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		write_log('Closed Webex.')
	except Exception as err:
		handle_error(err)
   
def shutdown(answer):# Shuts down computer
	try:
		write_log('User typed: {}'.format(answer))
		if answer.lower() == 'y':
			os.system('shutdown /t 30 /s')
			print('shuting computer down in : ')
			for num in range(30, 0, -1):
				print(num)
				time.sleep(1)
		if answer.lower() == 'n':
			sys.exit()
	except Exception as err:
		handle_error(err)
	
def start_time(): # Gets current time
	return round(time.time())
def end_time(): # Gets current time
	return round(time.time())

def write_log(data):
	try:
		with open('latest_log.log', 'a') as file:
			write = f'[{datetime.datetime.now()}]{str(data)}\n'
			file.write(write)
	except Exception as err:
		handle_error(err)
def reset_log():
	try:
		with open('latest_log.log', 'w') as file:
			print('Log resetted')
	except Exception as err:
		handle_error(err)



if __name__ == '__main__':
	print('This is not the main file. To start the program execute the run.py file')
	sys.exit(1)