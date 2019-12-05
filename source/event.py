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
		self.choices = []  # remains empty if theres no choices.
		self.outcomes = []

		# The story ends here if this is true.
		# You can only try again or quit.
		self.terminal = False

		# See if the user has already visited this event.
		# It is possible that the user has returned,
		# and that new options are available to them.
		self.visited = False

	def __repr__(self):
		'''
		Represents what is seen by the user.
		Specifically, this outputs a string including:
		- the main content of the event
		- a numbered-list of available choices
		'''
		option_list = ''
		for index, choice in enumerate(choices):
			index += 1
			option_list += f'{index}. {choice}\n'

		return (
			f'{self.content}\n'
			f'{option_list}\n'
		)

	def create(self):
		pass
