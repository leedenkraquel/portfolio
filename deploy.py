from os import listdir
from parse_md import parse_md

# Projects portion
project_html = open("./projects/index.html", "w")
project_files = listdir("./projects")

projects = []
for file_name in project_files:
	if ".md" in file_name:
		projects.append(file_name)

project_body = '<div class="project_body">'

for project in projects:
        project_obj = parse_md("./projects/" + project)
        project_name = project[:-3]
        project_body = project_body + '''
        <div class="project_card_outer">
            <a href="''' + project_name + '''.html"> 
                <div class="project_card_inner">
                    <p class="title">''' + project_obj.get_title() + '''</p>
                    <p class="date">''' + project_obj.get_date() + '''</p>
                    <img class="cover_image" src="../''' + project_obj.get_image() + '''" />
                    <p class="summary">''' + project_obj.get_summary() + '''</p>
                </div>
            </a>
        </div>'''

        subproject_html = open("./projects/" + project_name + ".html", "w")
        subproject_html.write("<head><link rel='stylesheet' href='substyles.css'/><link rel='stylesheet' href='../styles.css' /></head>")
        subproject_html.write("<body id='project_page'>")
        subproject_html.write("<div id='nav_bar'></div>")
        subproject_html.write(project_obj.to_html())
        subproject_html.write("</body>")

project_body = project_body + '</div>'

# Essays portion
essay_html = open("./essays/inex.html", "w")
essay_files = listdir("./essays")

essays = []
for file_name in essay_files:
	if ".md" in file_name:
		essays.append(file_name)

# Default index head and tail sections
index_head = '''
<!DOCTYPE html>
<html>
<!--The header section of the code-->
<head>
<link rel="stylesheet" href="../styles.css"/>
<link rel="stylesheet" href="substyles.css"/>
<!--The title appears in the tab-->
<title>Leeden</title>
<!--favicon-->
<link rel="icon" type="image/x-icon" href="https://img.icons8.com/ios-filled/2x/full-screen.png"/>
<script src="../scripts.js"></script>
<!--import Google icons-->
<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
</head>

<!-- The body section of the code-->
<body>

    <div id="body_style">
        <!--Navigation Bar-->
        <div id="nav_bar"></div>

        <!--Side Navigation Menu-->
        <div id="side_nav"></div>

        <!--Main Body-->
        <div id="site_body">
            <div>'''
index_tail = '''
            </div>
        </div>

        <!--Footer-->
        <div id="footer"></div>
    </div>

</body>
</html>'''

# Import bodies to htmls files
project_html.write(index_head)
project_html.write(project_body)
project_html.write(index_tail)
