import sublime
import sublime_plugin


class ExpandWithoutChildren(sublime_plugin.TextCommand):
	def run(self, edit):
		for cursor_position in self.view.sel():
			region = self.view.word(cursor_position)
			word = self.view.substr(region)
			expanded_word = "<%s />" % word
			self.view.replace(edit, region, expanded_word);

		# @todo: move cursor before /> with multiples cursors
		# for new_position in self.view.sel():
		# 	new_position = cursor_position
		# 	new_position.a -= 2 
		# 	new_position.b -= 2 
		# 	# self.view.sel().clear();
		# 	self.view.sel().add(new_position);

