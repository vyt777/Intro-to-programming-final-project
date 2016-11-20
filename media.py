import webbrowser

class Video():
	def __init__(self, title, description, image, video_url):
		self.title = title
		self.description = description
		self.image = image
		self.video = video_url
	def show_video(self):
		webbrowser.open(self.video)
		
