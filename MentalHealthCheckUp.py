def end_question():
	print('------------------------------------------------------')
	print('Are you good now? \n1: Yes, I am set now \n2: I think I need help with something else')
	ans = input('Pick a number (1 or 2): ')
	if ans == '1':
		print('------------------------------------------------------')
		print('I am glad you are okay! You can visit me again if you need help.')
		return '5'
	return '999'

print('Hi! I want to chat and check up how you are doing :) None of your responses will be recorded. We will just have a casual chat, so relax!')
name = input('What\'s your name?: ')
print('Nice to meet you, '+name+'!')
input('How was your day?: ')
input('How are you feeling at the moment?: ')
ans1 = input('Do you want to get something off your chest? rant? (Y/N): ')
if (ans1 == 'Y') or (ans1 == 'y'):
	input('Okay. I\'m all ears! Empty your mind: \n')
	print('That sounded like it was a load off your chest! Thanks for sharing with me.')
else:
	print('Okay, that is fine.')
ans2 = input('Are you in need of assistance? (Y/N): ')
if (ans2 == 'Y') or (ans2 == 'y'):
	num_help = '999'
	while num_help != '5':
		print('------------------------------------------------------')
		print('1: I need to talk to someone')
		print('2: I\'m overwhelmed and stressed')
		print('3: I\'m depressed and tired')
		print('4: I\'m anxious and scared')
		print('5: Actually I don\'t need help')
		num_help = input('What can I help you with? (type a number from above): ')
		if num_help == '1':
			print('------------------------------------------------------')
			print('Here are some resources I hope you find useful:')
			print('-')
			print('the National Suicide Prevention Lifeline is 800-273-8255 and their website is http://www.suicidepreventionlifeline.org/')
			print('-')
			print('the National Sexual Assault Hotline is safe and confidential; only the first six numbers will route the call (800)654-HOPE')
			print('-')
			print('the Crisis Text Line: text REASON to 741741 (free, confidential, and open 24/7')
			num_help = end_question()
		elif num_help == '2':
			print('------------------------------------------------------')
			print('It is okay to feel overwhelmed. Life gets crazy, and it is fine if you feel like there is a lot going on. Just breathe. Look at the things around you.')
			print('Some things you can do:\n-take a nice bath\n-journal\n-breathing exercises\n-drink warm tea\n-take a nap')
			print('Life gets overwhelming sometimes. Everyone needs a break every once in a while. You are doing amazing and I am proud of you.')
			num_help = end_question()
		elif num_help == '3':
			print('------------------------------------------------------')
			print('There are days when you will feel down or unmotivated. That is totally okay. Let\'s take things at a steady pace.')
			print('Remember that there are people out there who love you a lot. You are very important and your feelings are valid.')
			print('Your hard work will pay off. Everything you are doing matters, so do not give up!')
			print('It is important to take care of yourself.\n-get out of bed\n-take care of your personal hygiene\n-look out for your loved ones\n-take your medicine\n-seek help, talking about your problems will help')
			print('It\'s okay if doing these are hard. Let\'s tackle them, one thing at a time, one day at a time. You got this! I believe in you.')
			num_help = end_question()
		elif num_help == '4':
			print('------------------------------------------------------')
			print('Find out what caused you to feel this way.')
			print('You can try breathing exercises! Visit this thread of breathing exercises and anxiety reducing gifs: https://twitter.com/discoghouI/status/1272307242596020225?s=20')
			print('You can also try meditation! There are lots of guided meditation on youtube.')
			print('Also try washing your face, massaging your scalp, and listening to calm music.')
			num_help = end_question()
		else: 
			print('------------------------------------------------------')
			print('I am glad you are okay! You can visit me again if you need help.')
ans3 = input('Do you want ideas on stuff to do to feel better or to distract yourself? (Y/N): ')
if (ans3 == 'Y') or (ans3 == 'y'):
	print('Ok! Some ideas that might help include coloring, meditating, exercising, cleaning, and some self-care like showering/putting on a face mask.')
else:
	print('No problem. I hope I can be of more help in the future.')
print('Before you go, I wanted to give you some final reminders.')
print('You deserve to rest. You can do this. I am proud of you. Do not forget to eat, drink some water, take your medicine, and just breathe. Everything will be alright. I believe in you. Stay strong!')
print('Bye, '+name+'. Take care of yourself.')