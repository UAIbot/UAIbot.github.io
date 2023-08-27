---
layout: default
title: Example Home
nav_exclude: true
---

# How to generate the documentation relative to the Python API with Sphinx

Fist of all, you need to install Sphinx:
    
```bash
pip install sphinx
```
and install the sphinx-markdown-builder

```bash
pip install sphinx-markdown-builder
```

Then, you need to clone the UAIbotPy repository

```bash
git clone https://github.com/UAIbot/UAIbotPy.git
```

in the UAIbotPy folder you cloned, you need to create a folder called docs

```bash
mkdir docs
```
and then, get into the docs folder

```bash
cd docs
```

then, run the comand for the sphinx quickstart

```bash
sphinx-quickstart
``` 
Answer the questions acordingly to your preferences. Now go to the conf.py file and change the `extensions` variable to:

```python
 extensions = ['sphinx.ext.autodoc', 'sphinx_markdown_builder']
```
now go to the main folder

```bash
cd ..
```

and run the following command

```bash
sphinx-apidoc -o docs . --separate
```
now go back to the docs folder

```bash
cd docs
```

and run the following command

```bash
make markdown
```

now you can find the documentation files in the docs/_build/markdown folder, but those files are not compatible with Just the Docs theme. To make them compatible, you need to run the following python script in the same folder as the markdown files:

```python
import glob

for filename in glob.glob('*md'):
    f = open(filename, "r+")
    splited_filename = filename.split('.')
    metadata = ""
    if len(splited_filename) == 4:
        metadata = """--- 
layout: default
title: """+ filename[:-3] +"""
parent: """+ splited_filename[0] + '.' + splited_filename[1] +"""
grand_parent: Python API reference
--- """
        file_data = f.read() 
        f.seek(0, 0) 
        f.write(metadata + '\n' + '\n' + file_data)
        print(filename)
    if len(splited_filename) == 3:
        if "###" in open(filename).read():
            metadata = """---
layout: default
title: """+ filename[:-3] +"""
parent: Python API reference
---"""
            file_data = f.read()
            f.seek(0, 0)
            f.write(metadata + '\n' + '\n' + file_data)
            print(filename)
        else:
            metadata = """---
layout: default
title: """+ filename[:-3] +"""
has_children: true
parent: Python API reference
---"""
            file_data = f.read() 
            f.seek(0, 0)
            f.truncate(0)
            f.write(metadata)
            print(filename)
```

The script will add the metadata needed for the Just the Docs theme to work properly.

Now, you need to copy the markdown files to the documentation repository. Clone the documentation repository

```bash
git clone https://github.com/UAIbot/UAIbot.github.io.git
``` 

and copy the markdown files to the from_sphinx folder at the documentation repository

```bash
cp -r docs/_build/markdown/* /home/user/UAIbot.github.io/docs/API_Reference/Python_API_reference/from_sphinx
```

then run the following command to recreate the documentation

```bash
bundle exec jekyll serve
```

finally, push the changes to the documentation repository

```bash
git add .
git commit -m "created new python API reference"
git push
```
