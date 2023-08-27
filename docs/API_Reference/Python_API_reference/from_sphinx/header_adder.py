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



    