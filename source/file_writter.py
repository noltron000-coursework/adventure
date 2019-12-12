import os

class FileWritter:
	def __init__(self, story):
		self.story = story
		self.dir = input('What folder-name do you want your output files to be in? ')
		if self.dir == '':
			self.dir = 'story'
		if os.path.isdir(f'./{self.dir}'):
			raise # ValueError('This folder already exists! Please try again.')

		else:
			os.mkdir(f'./{self.dir}')
			os.mkdir(f'./{self.dir}/pages')

	def main(self):
		story = self.story
		self.write_cover()
		self.write_event(story.root)

	def write_cover(self):
		story = self.story
		markdown = (
			f'{story.title.title()}\n'
			f'{len(story.title) * "="}\n\n'
			f'{story.subtitle.title()}\n'
			f'{len(story.subtitle) * "-"}\n\n'
			f'> {story.synopsis}\n\n'
			'---\n\n'
			'### [*click here to start reading*]'
			f'(./pages/{id(story.root)}.md)\n'
		)

		# then create the file
		with open(f'./{self.dir}/START.md', 'w+') as file:
			file.write(markdown)

	def write_event(self, event):
		# compile event path
		event_path = f'./{self.dir}/pages/{id(event)}.md'
		# check if the compiled markdown file exists.
		if os.path.isfile(event_path):
			return

		# first create the list of options.
		option_list = ''
		for index, choice in enumerate(event.choices):
			outcome = event.outcomes[index]
			# compile event path
			outcome_path = f'./{id(outcome)}.md'
			option_list += f'1. [{choice}]({outcome_path})\n'

		if option_list != '':
			option_list = '\n---\n\n' + option_list

		# next compile the markdown
		markdown = (
			f'{event.content}\n'
			f'{option_list}'
		)

		# then create the file
		with open(event_path, 'w+') as file:
			file.write(markdown)

		# finally repeat for child events
		for outcome in event.outcomes:
			self.write_event(outcome)
