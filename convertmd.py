# convet markdown into html
import markdown as md
import sys

path = sys.argv[1]
fname = path.split("/")[-1].split(".")[0]
npath = "pages/{}.html".format(fname)

with open(path, 'r') as f:
    contents = f.read()
html = md.markdown(contents)

with open(npath, "w") as f:
    f.write(html)

print("file {} created".format(npath))
