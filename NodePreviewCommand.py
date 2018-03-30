import sublime
import sublime_plugin

import subprocess

"""
@todo:
Carregar algumas funções helpers, como:
const sum = (first, ...rest) =>
	(first.constructor === Array
		? first
		: [first, ...rest])
	.reduce((a, b) => a + b, 0);
"""

class NodePreviewCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for sel in self.view.sel():
			line = self.view.line(sel)

			js = self.view.substr(line).strip().split('\n')
			if not 'console' in js[-1]:
				js[-1] = "console.log({0})".format(js[-1])

			# print('js', )
			# cmd = ['node', '-e'] + [("console.log({0})".format(js) if not js.startswith('console') else js)]
			cmd = ['node', '-e'] + [';'.join(js)]

			print('---- exec', cmd)
			p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			out, err = p.communicate()
			if err is not None:
				print('ERROR:', err)
				# return

			print(out);

			self.view.insert(edit, line.end(), ' /* {0} */'.format((out if not err else err).decode().strip()))


