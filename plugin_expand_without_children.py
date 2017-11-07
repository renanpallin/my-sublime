import sublime
import sublime_plugin


class ExpandWithoutChildren(sublime_plugin.TextCommand):
	def run(self, edit):
		cursor_position = self.view.sel()[0]
		region = self.view.word(cursor_position)
		word = self.view.substr(region)
		expanded_word = "<%s />" % word
		self.view.replace(edit, region, expanded_word);

		new_position = self.view.sel()[0]
		new_position.a -= 2 
		new_position.b -= 2 
		self.view.sel().clear();
		self.view.sel().add(new_position);

