class Event:
	'''
	==TODO==
	add docstring
	'''

	def __init__(self):
		'''
		==TODO==
		add docstring
		'''
		# The content is long-form, unformatted text.
		# It is the main information presented to the user.
		self.content = ''

		# Different choices lead to different outcomes.
		# Their array index coorelates with one another.
		self.choices = [] # remains empty if theres no choices.
		self.outcomes = [] # empty if the event is terminal.

	def __repr__(self):
		'''
		Represents what is seen by the user.
		Specifically, this outputs a string including:
		- the main content of the event
		- a numbered-list of available choices
		'''
		option_list = ''
		for index, choice in enumerate(choices):
			option_list += f'{index + 1}. {choice}\n'

		return (
			f'{self.content}\n'
			f'{option_list}'
		)

	def add_content(self, parent = None, choice_index = None):
		'''
		==TODO==
		add docstring
		'''
		# READ description of parent/event (if any)
		# READ each&every choice option (if parent/event)
		if not (parent is None and choice_index is None):
			# display content text to user
			# display choice text to user
			pass

		# WRITE description of each&every child/outcome
		# REPEAT each&every time
		input(
			'\n'
			'-----------------------------------------------\n'
			'   You are creating a new event in the story.\n'
			'    An event is an overarching block or act,\n'
			' which is presented to the reader all at once.\n'
			'         ~~PRESS ENTER TO CONTINUE~~\n'
			'-----------------------------------------------\n'
		)

		self.content = input(
			'Please input the event\'s content:\t'
		)

	def add_choices(self):
		'''
		==TODO==
		add docstring
		'''
		query = True
		while query:
			query = input(
				'Would you like to add a new choice? (y/n):\t'
			)

			if query.lower() == 'y':
				query = True
			else:
				query = False

			if query:
				# ==TODO==
				# self.add_choice()
				pass

		for index, choice in enumerate(self.choices):
			print(f'{index + 1}', choice)
			event = Event()
			event.add_content()
			self.outcomes.append(event)

	def is_terminal(self):
		'''
		==TODO==
		add docstring
		'''
		return self.outcomes == []
