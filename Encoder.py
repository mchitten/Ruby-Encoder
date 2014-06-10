import sublime, sublime_plugin

class EncoderInsertCommand(sublime_plugin.TextCommand):
  def run(self, edit, encoding):
    self.view.insert(edit, 0, "# encoding: " + encoding + "\n\n")

class EncoderCommand(sublime_plugin.EventListener):
  def __init__(self):
    self.settings = sublime.load_settings('Encoder.sublime-settings')

  def on_pre_save(self, view):
    file_ext = view.file_name()[-3:]
    encoding = self.settings.get('encoding')
    if (not view.substr(view.line(0)) == "# encoding: " + encoding) and (file_ext in self.settings.get('ruby_extensions')):
      view.run_command('encoder_insert', { 'encoding': encoding })
