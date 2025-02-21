import os

cwd = os.path.dirname(os.path.realpath(__file__))
raw_text_dir = os.path.join(cwd, 'blog-raw-text')
blog_dir = os.path.join(cwd, 'blog')
files = os.listdir(raw_text_dir)

#setup html template
template = open(os.path.join(cwd, 'template.html'), "r").read()
split_s = "var temp = `"
split_i = template.find(split_s) + len(split_s)
template = [template[0:split_i], template[split_i:len(template)]]

#create html file for each txt file in blog-raw-text
for file in files:
    raw = open(os.path.join(raw_text_dir, file), "r").read()

    #extract and reformat title
    title = raw.split('\n')[0]
    title = ''.join(c for c in title if c.isalpha() or c == ' ')
    title = title.replace(' ', '_')

    with open(os.path.join(blog_dir, title + '.html'), "w") as f:
        text = ''.join([template[0], raw, template[1]])
        f.write(text)
        f.close()