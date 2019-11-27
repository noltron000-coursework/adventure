class Story:
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
		# It is essentially the meta-data of the story.
		self.title = ''
		self.subtitle = ''
		self.synopsis = ''

		# The first event of the story.
		self.root = None

	def __repr__(self):
		'''
		Represents what is seen by the user.
		Specifically, this outputs a string containing:
		- the title of the story
		- the subtitle of the story
		- a synopsis of the story
		- the number of possible endings
		'''
		return (
			f'{self.title.uppercase()}\n'
			f'{self.subtitle}\n'
			f'{len(self.subtitle) * '-'}\n\n'
			f'{self.synopsis}\n'
		)
