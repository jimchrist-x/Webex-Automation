import functions


if __name__ == '__main__':
	started = functions.start_time()
	functions.reset_log()
	print('Checking OS...')
	functions.write_log('Checking OS...')
	functions.check_os()
	print('Loading Files...')
	functions.write_log('Loading Files...')
	functions.write_log('Converting Schedule...')
	functions.convert_schedule('program.txt', 'key.txt')
	functions.write_log('Schedule Converted.')
	functions.write_log('Reading key...')
	schedule = functions.read_schedule('key.txt')
	functions.write_log('Key read successfully!')
	print('Done!')
	functions.write_log('Done!')
	usr_inpt = functions.user_inputs()
	#answer = str(input("Shutdown computer after program completion? (y\\n)"))
while 1:
		for elem in schedule[0]:
			if elem.split('#')[0] == functions.get_time()[0]:
				if elem.split('#')[1] == functions.get_time()[1]:
					functions.close_webex()
					functions.webex_start()
					functions.click('join.png', 0.9)
					functions.click('link.png', 0.9)
					functions.type_or_enter(elem.split('#')[3], "type")
					functions.click('name.png', 0.9)
					functions.type_or_enter(usr_inpt[0], "type")
					functions.click('email.png', 0.9)
					functions.type_or_enter(usr_inpt[1], "type")
					functions.click('Next.png', 0.9)
					functions.click('join_meeting.png', 0.9)
					functions.send_mail(usr_inpt[1], usr_inpt[2], usr_inpt[3], 'You just joined a meeting! Your name : {}'.format(usr_inpt[0]))
					while 1:
						if elem.split('#')[2] == functions.get_time()[1]:
							functions.write_log('Time reached')
							break
						else:
							continue
					functions.click('exit_meeting.png', 0.9)
					functions.click('exit_meeting1.png', 0.9)
					functions.click('leave_meeting1.png', 0.9)
					functions.click('leave_meeting2.png', 0.9)
					functions.click('leave_meeting.png', 0.9)
					functions.send_mail(usr_inpt[1], usr_inpt[2], usr_inpt[3], 'You just left a meeting! Your name : {}\n\nSession time: {} - {}'.format(usr_inpt[0], elem.split('#')[1], elem.split('#')[2]))
	#print('Program elapsed time: {} sec ({} min)'.format(functions.end_time() - started, round((functions.end_time() - started) / 60)))
	'''if answer.lower() == 'y':
                functions.shutdown(answer)
        else:
                continue'''
        
