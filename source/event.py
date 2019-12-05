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
		self.content = input(
			'Please input the event\'s content:\t'
		)

	def add_choices(self):
		'''
		==TODO==
		add docstring
		'''
		# WRITE new choices for item
		query = True
		while query:
			# ask user if they
			query = input(
				'Would you like to add a new choice? (y/n):\t'
			)

			# convert string to boolean
			if query.lower() == 'y':
				query = True
			else:
				query = False

			if query:
				# display choices thus far;
				# ask user if they want to add another choice
				# ==TODO==
				# self.add_choice()
				pass

		# CREATE an event for each choice
			event = Event()
			event.add_content()
			self.outcomes.append(event)

	def is_terminal(self):
		'''
		==TODO==
		add docstring
		'''
		return self.outcomes == []
