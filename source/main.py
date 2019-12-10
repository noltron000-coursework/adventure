from story import *
from file_writter import *

if __name__ == '__main__':
	story = Story()
	story.write()
	file_writter = FileWritter(story)
	file_writter.main()
