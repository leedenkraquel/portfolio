from os import listdir
from parse_md import parse_md
from projects.projects import create_project_cards

###
# Name: page.py
# Auhtor(s): Leeden Raquel
# Description: generates a string that represents the html for the home page. The home page should
#  display a header with my name followed by a preview of my projects and essays
###

def create_home_page ():
    project_files = listdir("projects/")

    home_page = '''
        <h1 class="centered">Leeden Raquel</h1>
        <p class="centered about_body">Software Developer</p>
        <div class="hr"></div>
        <h2>Projects</h2>
        <div class="project_section">
    '''
    
    home_page += ''.join(create_project_cards("", project_files)[:3])

    home_page += '''
        </div>
        <div class="hr"></div>
        <h2>Essays</h2>
        <div class="hr"></div>
    '''
    return home_page