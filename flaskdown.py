#!/usr/bin/env python3
import markdown
import codecs
from flask import Flask, render_template, Markup

app = Flask(__name__)

@app.route('/content/<mdfile>')
def render_md(mdfile: str) -> str:
    '''
    Renders a markdown file with the given filename.

    :param mdfile: name of markdown file wihout .md
    :returns: string with rendered html of markdown file with content.html
    '''
    mdfile_name = mdfile + '.md'
    input_file = codecs.open(mdfile_name, mode='r', encoding='utf-8')
    text = input_file.read()
    content = Markup(markdown.markdown(text))
    return render_template('content.html', **locals())

@app.route('/')
def render_index() -> str:
    return render_md('index')

if __name__ == '__main__':
    app.run()
