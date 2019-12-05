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
		for index, choice in enumerate(self.choices):
			option_list += f'{index + 1}. {choice}\n'

		return (
			f'{self.content}\n'
			f'{option_list}'
		)

	def add_content(self, parent = None, choice_index = None):
		'''
		This lets the user add string content to the event.

		==NOTE==
		This method should be called without parameters
		just once, only when it is used in Story.write().
		Otherwise, the parameters are needed to give
		the user more context to what they are writting.
		'''
		# ==READ==
		# The user should know the context of this function
		# pretty much as soon as its called, or they will be
		# asked to input information without knowing what for.
		print(
			f'\n{"-" * 47}\n'
		)

		if not (parent is None and choice_index is None):
			# Both choice & choice_index are needed for the user.
			choice = parent.choices[choice_index]

			# ==READ==
			# The user needs to see what they are adding to.
			# Here, they are adding an event's contents
			# in response to a choice that they added earlier.
			# Let them know exactly which choice that is.
			# The event's contents are visited again later;
			# it too might have choices of its own.
			print(parent)
			print(f'({choice_index + 1}. {choice})\n')

		# ==WRITE==
		# Once the user knows the context of this function,
		# they are given access to add a section to the story.
		self.content = input(
			'Please input the event\'s content:\t'
		)

	def add_choices(self):
		'''
		==TODO==
		add docstring
		'''
		print(
			f'\n{"-" * 47}\n'
		)
		# WRITE new choices for item
		query = True
		while query:
			print(self)
			# ask user if they want to add another choice
			query = input(
				'Would you like to add a new choice? (y/n):\t'
			)
			# convert string to boolean
			if query.lower() == 'y':
				query = True
			else:
				query = False

			if query:
				print(
					'Here are your choices thus far:\t'
					f'{self.choices}'
				)
				# ask user if they want to add another choice
				self.choices.append(input(
					'Please input the choice\'s content:\t'
				))

		# CREATE an event for each choice
		for choice_index, choice in enumerate(self.choices):
			event = Event()
			event.add_content(self, choice_index)
			self.outcomes.append(event)

		# CREATE choices for each event
		for event in self.outcomes:
			event.add_choices()

	def is_terminal(self):
		'''
		==TODO==
		add docstring
		'''
		return self.outcomes == []
