---
layout: default
title: Example Home
nav_exclude: true
---

## How to generate the documentation relative to the JavaScript API with JSDocs

First, install jsdoc and jsdoc-to-markdown:

```bash
sudo npm install -g jsdoc
```

```bash
sudo npm install -g jsdoc-to-markdown
```

run the following command in the directory where the files are located:

```bash
for file in YOUR/PATH/HERE/UAIbotJS/*.js; do jsdoc2md "$file" >> "$file".md; done

```

Make a docs folder to contain the markdown files:

```bash
mkdir docs
```

run the following python script to convert the markdown files to the format that Jekyll expects:

```python
import glob
import re
import os


cwd = os.getcwd()
for filename in glob.glob('*md'):
    f = open(filename, "r+")
    content = f.read()
    if content == "" or "local" in filename:
        continue
    
    father_string = """---
layout: default
title: """+ str(filename.split(".")[0]).lower() +"""
has_children: true
parent: JavaScript API reference
---

"""
    mark_name = cwd + "/docs/" + str(filename.split(".")[0]).lower() + ".md"
    text_file = open(mark_name, "w")
    text_file.write(father_string)
    for i in range(1, len(re.split(r'\n## ', content))):
        s = re.split(r'\n## ', content)[i]
        s = s.rsplit("\n",3)[0]
        mark_name = cwd + "/docs/" + str(filename.split(".")[0]).lower() + "." + str(s.split('\n', 1)[0]).split()[0] + ".md"
        text_file = open(mark_name, "w")
        child_string = """---
layout: default
title: """+ str(filename.split(".")[0]).lower() + "." + str(s.split('\n', 1)[0]).split()[0] +"""
parent: """+ str(filename.split(".")[0]).lower() +"""
grand_parent: JavaScript API reference
---

"""     
        s = "## " + s
        s = child_string + s
        text_file.write(s)
```

You need to copy the markdown files to the documentation repository. Clone the documentation repository

```bash
git clone https://github.com/UAIbot/UAIbot.github.io.git
``` 

You can copy the docs folder contents to the YOUR/MACHINE/PATH/UAIbot.github.io/docs/API_Reference/JavaScript_API_reference/from_JSdocs folder in the main directory of the repository.

Finally, you can run the following command to update the website:

```bash
bundle exec jekyll serve
```