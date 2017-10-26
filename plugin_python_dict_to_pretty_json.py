import sublime
import sublime_plugin

class DictToJsonCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = sublime.Region(0, self.view.size())
		allTxt = self.view.substr(region)\
			.replace("True", "true")\
			.replace("False", "false")\
			.replace("'", '"')
			# @TODO: usar rexes e colocar na sintaxe {"$oid":"123"}
			# .replace("ObjectId.+\)", )
			# .replace("TimeStamp", )
		self.view.replace(edit, region, allTxt)
		self.view.run_command("pretty_json")
		self.view.set_syntax_file('Packages/JavaScript/JSON.sublime-syntax')