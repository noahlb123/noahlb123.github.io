import os
import json
import pandas as pd

cwd = os.path.dirname(os.path.realpath(__file__))
raw_text_dir = os.path.join(cwd, 'blog-raw-text')
blog_dir = os.path.join(cwd, 'blog')
files = os.listdir(raw_text_dir)

for_blog_html = []

#setup html template
template = open(os.path.join(cwd, 'template.html'), "r").read()
split_s = "var temp = `"
split_i = template.find(split_s) + len(split_s)
template = [template[0:split_i], template[split_i:len(template)]]

#create html file for each txt file in blog-raw-text
for file in files:
    raw = open(os.path.join(raw_text_dir, file), "r").read()

    #extract and reformat title
    split = raw.split('\n')
    title = split[0]
    date = split[2]
    safe_title = ''.join(c for c in title if c.isalpha() or c == ' ').replace(' ', '_') + '.html'
    for_blog_html.append([title, safe_title, date])

    with open(os.path.join(blog_dir, safe_title), "w") as f:
        text = ''.join([template[0], raw, template[1]])
        f.write(text)
        f.close()
'''
df = pd.DataFrame(data=for_blog_html)
df[2] = pd.to_datetime(df[2], format="%m/%d/%Y")
I need to zero pad my months and days in order to fix this ^
'''

#setup main blog templatee
blogTemplate = open(os.path.join(cwd, 'blog.html'), "r").read()
with open(os.path.join(cwd, 'blog.html'), "w") as f:
    #write new file
    split_s = "templateInput = ["
    start_line = blogTemplate.find(split_s) + len(split_s)
    end_line = blogTemplate.find('\n', start_line)
    f.write(blogTemplate[0:start_line - 1] + json.dumps(for_blog_html) + ';' + blogTemplate[end_line:len(blogTemplate)])
    f.close()
