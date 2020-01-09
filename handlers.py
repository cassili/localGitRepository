class Handler(object):
	"""docstring for Handler"""
	def __init__(self, arg):
		super(Handler, self).__init__()
		self.arg = arg

	def callback(self, prefix, name, *args):
		method = getattr(self, prefix + name, None)
		if callable(method):
			return method(*args)

	def start(self, name):
		self.callback('start_', name)

	def end(self, name):
		self.callback('end_', name)

	def sub(self, name):
		def substitution(match):
			result = self.callback('sub_', name, match)
			if result is None:
				match.group(0)
				return result
		return substitution

class HTMLRenderer(Handler):
	"""docstring for HTMLRenderer"""
	def __init__(self, arg):
		super(HTMLRenderer, self).__init__()
		self.arg = arg
		
	def start_document(self):
		print '<html><head><title>...</title><body>'

	def end_document(self):
		print '</body></html>'

	def end_paragraph(self):
		print '</p>'

	def start_paragraph(self):
		print '<p>'

	def end_heading(self):
		print '</h2>'

	def start_heading(self):
		print '<h2>'

	def end_list(self):
		print '</ul>'

	def start_list(self):
		print '<ul>'

	def end_listitem(self):
		print '</li>'

	def start_listitem(self):
		print '<li>'

	def end_title(self):
		print '</h1>'

	def start_title(self):
		print '<h1>'

	def sub_emphasis(self, match):
		return '<em>{}</em>'.format(match.group(1))

	def sub_url(self, match):
		return '<a href = "{}">{}</a>'.format(match.group(0), match.group(1))

	def feed(self, data):
		print data





		