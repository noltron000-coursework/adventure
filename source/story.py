from event import *

class Story:
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
			f'{self.title.upper()}\n'
			f'{self.subtitle}\n'
			f'{len(self.subtitle) * "-"}\n\n'
			f'{self.synopsis}\n'
		)

	def populate(self):
		'''
		==TODO==
		add docstring
		'''
		input(
			'===============================================\n'
			'        Welcome to Adventure Creator!\n'
			'This CLI tool will help you get started on your\n'
			'very own choose-your-own-adventure style story.\n'
			'         ~~PRESS ENTER TO CONTINUE~~\n'
			'===============================================\n'
		)

		self.title = input(
			'Please input the story\'s title:\t'
		)

		self.subtitle = input(
			'Please input the story\'s subtitle:\t'
		)

		self.synopsis = input(
			'Please input the story\'s synopsis:\t'
		)

		self.add_root()
		self.root.populate()

	def add_root(self, event = None):
		'''
		==TODO==
		add docstring
		'''
		if event is None:
			event = Event()
		if self.root is None:
			self.root = event
		else:
			raise ValueError('the root event already exists!')
