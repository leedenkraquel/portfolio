from os import listdir;

# create an index.html file in this directory
file_html = open("index.html", "w")

files = listdir(".")
tests = []

for fileName in files:
	if ".md" in fileName:
		tests.append(fileName)

print(tests)

file_html.write('''
<html>
    <head>
    <title>Python</title>
    </head>
    <body>''')

for fileName in tests:
	file_html.write('<p>' + fileName + '</p>')

file_html.write('''
    </body>
</html>''')

file_html.close()
