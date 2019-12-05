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
			print(
				f'{parent}\n'
				f'({choice_index + 1}. {choice})'
			)

		# ==WRITE==
		# Once the user knows the context of this function,
		# they are asked to add a section to the story.
		self.content = input(
			'Please input the event\'s content:\t'
		)

	def add_choices(self):
		'''
		==TODO==
		add docstring
		'''
		# ==READ==
		# The user should know the context of this function
		# pretty much as soon as its called, or they will be
		# asked to input information without knowing what for.
		print(
			f'\n{"-" * 47}\n'
		)

		# The `choice` here is needed to start the while loop.
		# It will be overwritten with a string later.
		# The string will be False if it is empty,
		# otherwise it is True because the user added data.
		choice = True
		# A loop is needed since an event can have many choices.
		while choice:
			# ==READ==
			# The user will be asked if they want to add
			# another `choice` option to the event.
			# Because they will be asked about it multiple times,
			# the loop's context should be repeatedly described
			# so that the user doesn't forget what they are doing.
			print(self)

			# ==WRITE==
			# Once the user knows the context of this function,
			# they are asked to add a `choice` to the event.
			choice = input(
				'Create a new choice for this event\n'
				'(you can leave this blank to skip):\t'
			)

			# Is `choice` left blank?
			if choice:
				self.choices.append(choice)

		# Once the loop finished, `self.choices` is populated.
		# If left empty, the event is considered terminal.
		# The for loop will end immediately in this case.
		for choice_index, choice in enumerate(self.choices):
			# Create a new outcome event for each choice.
			event = Event()
			# Add content to the outcome `event`.
			# The content branches off of the `choices` added here.
			event.add_content(self, choice_index)
			# The outcome `event` proceeds our `self`.
			self.outcomes.append(event)

		# Once each of the `events` are created,
		# they too can have `choices` of their own.
		# This recursively creates yet more `choices`,
		# and with those `choices` more `events`.
		for event in self.outcomes:
			event.add_choices()

	def is_terminal(self):
		'''
		==TODO==
		add docstring
		'''
		return self.outcomes == []
