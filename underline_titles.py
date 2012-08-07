import sublime, sublime_plugin

class UnderlineTitlesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		sel = view.sel()[0]
		string = '\n'
		title = view.line(sel) if sel.empty() else sel
		string += '#' * len(title)
		point = view.line(sel).end()
		view.insert(edit, point, string)

class UnderlineTitlesListener(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		sel = view.sel()[0]
		if '#' in view.substr(sel.a-1):
			row,col = view.rowcol(sel.a)
			prev_line = view.line(view.text_point(row-1,0))
			return [('Underline\tMarkdown','#' * (len(prev_line)-1))]