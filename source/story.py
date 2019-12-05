from event import *

class Story:
	'''
	A story points a reader to the first event.
	It also holds metadata, such as its title.

	Finally, it holds the function of impetus -- self.write().
	This thing sets off all the recursion within the Event.
	'''

	def __init__(self):
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

	def write(self):
		'''
		Write will ask the user for some basic metadata.
		Then, it will start the process of asking for all the
		other data and storylines that a good adventure needs.
		'''
		input(
			f'{"=" * 47}\n'
			'        Welcome to Adventure Creator!\n'
			'This CLI tool will help you get started on your\n'
			'very own choose-your-own-adventure style story.\n'
			'         ~~PRESS ENTER TO CONTINUE~~\n'
			f'{"=" * 47}\n'
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

		self.root = Event()
		self.root.add_content()
		self.root.add_choices()
