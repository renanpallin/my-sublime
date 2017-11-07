import sublime
import sublime_plugin


class ExpandWithoutChildren(sublime_plugin.TextCommand):
	def run(self, edit):
		position = self.view.sel()[0]
		region = self.view.word(position)
		word = self.view.substr(region)
		expanded_word = "<%s />" % word
		self.view.replace(edit, region, expanded_word);

		# @todo: Put cursor rigth before '/>'
		# self.view.sel().clear()
		# self.view.sel().add()
