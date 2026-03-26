import os
import glob
import re

template_dir = r"c:\Users\FULL TEST\Desktop\PFM_Python\PFM\school\templates"
html_files = glob.glob(os.path.join(template_dir, "**/*.html"), recursive=True)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "{% load static %}" not in content:
        content = re.sub(r'(src|href)="assets/(.+?)"', r'\1="{% static \'assets/\2\' %}"', content)
        content = re.sub(r"(src|href)='assets/(.+?)'", r"\1='{% static \"assets/\2\" %}'", content)
        
        content = "{% load static %}\n" + content
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
print("Done")
