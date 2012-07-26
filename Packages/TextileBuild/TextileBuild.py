import sublime
import sublime_plugin
import textile
import os
import tempfile
import webbrowser

class TextileBuild(sublime_plugin.WindowCommand):
    def run(self):
        s = sublime.load_settings("TextileBuild.sublime-settings")
        output_html = s.get("output_html", False)
        open_html_in = s.get("open_html_in", "browser")
        use_css = s.get("use_css", True)
        charset = s.get("charset", "UTF-8")

        view = self.window.active_view()
        if not view:
            return
        file_name = view.file_name()
        if not file_name:
            return
        contents = view.substr(sublime.Region(0, view.size()))
        tx = textile.textile(contents)
        html = '<html><meta charset="' + charset + '">'
        if use_css:
            css = os.path.join(sublime.packages_path(), 'TextileBuild', 'textile.css')
            if (os.path.isfile(css)):
                styles = open(css, 'r').read()
                html += '<style>' + styles + '</style>'
        html += "<body>" + tx + "</body></html>"

        if output_html:
            html_name = os.path.splitext(file_name)[0]
            html_name = html_name + ".html"
            output = open(html_name, 'w')
        else:
            output = tempfile.NamedTemporaryFile(delete=False, suffix='.html')

        output.write(html.encode('UTF-8'))
        output.close()

        if open_html_in == "both":
            webbrowser.open("file://" + output.name)
            self.window.open_file(output.name)
        elif open_html_in == "sublime":
            self.window.open_file(output.name)
        else:
            webbrowser.open("file://" + output.name)
