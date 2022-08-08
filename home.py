from os import listdir
from parse_md import parse_md

###
# Name: page.py
# Auhtor(s): Leeden Raquel
# Description: generates a string that represents the html for the home page. The home page should
#  display a header with my name followed by a preview of my projects and essays
###

def create_home_page ():
    project_directory = listdir("projects/")

    home_page = '''
        <h1 class="centered">Leeden Raquel</h1>
        <p class="centered about_body">Software Developer</p>
        <div class="hr"></div>
        <h2>Projects</h2>'''

    for project in project_directory:
        # parse each project md and display the name, date, and summary
        if ".md" in project:
            project_header = parse_about_project('projects/' + project)
            home_page += '<h3 class="title">' + project_header.get("title") + '</h3>'
            home_page += '<p class="date">' + project_header.get("date") + '</p>'
            home_page += '<p class="summary">' + project_header.get("summary") + '</p>'
            home_page += '<div><p class="labels">' + '</p><p class="labels">'.join(project_header.get("labels")) + '</p></div>'
            home_page += '<a class="link" href="projects' + project + '">View Work ></a>'

    home_page += '''<div class="hr"></div>
        <h2>Essays</h2>
        <div class="hr"></div>
    '''
    return home_page

def parse_about_project(directory):
    project = parse_md(directory)
    about_project = {
        "title": project.get_title(),
        "date": project.get_date(),
        "labels": project.get_labels(),
        "summary": project.get_summary(),
    }
    return about_project