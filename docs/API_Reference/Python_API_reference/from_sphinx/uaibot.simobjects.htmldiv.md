--- 
layout: default
title: uaibot.simobjects.htmldiv
parent: uaibot.simobjects
grand_parent: Python API reference
--- 

# uaibot.simobjects.htmldiv module

<a id="module-uaibot.simobjects.htmldiv"></a>

### *class* uaibot.simobjects.htmldiv.HTMLDiv(name='', html_text='Text', style='')

Bases: `object`

A HTML div that is used to display a text into the scenario canvas.

## Parameters

name
: The object’s name.
  (default: ‘genHTMLDiv’).

html_text
: The html string.
  (default: ‘Text’).

style
: CSS style string  (example: ‘position:absolute;top:200px,right:100px’).
  (default: ‘Text’).

#### add_ani_frame(time, html_text=None, style=None)

#### gen_code()

Generate code for injection.

#### *property* html_text

The HTML string representing the text. HTML markup is allowed here.

#### *property* name

The name of the object.

#### set_ani_frame(html_text=None, style=None)

#### *property* style

The CSS style string.
