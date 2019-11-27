class Event:
	'''
	==TODO==
	add docstring
	'''

	def __init__():
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
		represents what is seen by the user.
		'''
		pass
