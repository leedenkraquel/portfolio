from os import listdir
from parse_md import parse_md
from datetime import datetime

###
# Name: projects.py
# Author(s): Leeden Raquel
# Description: generates a string that represents the html for the projects page.
###

def create_projects_page (directory):
    project_page = '<div class="project_page">'
    project_files = listdir("projects/")
    project_page += ''.join(create_project_cards(directory, project_files))
    project_page += "</div>"
    return project_page

def create_project_cards (directory, project_files):
    project_cards = []
    for project in project_files:
        if ".md" in project:
            project_obj = parse_md("projects/" + project)
            project_card = '<a class="project_link" href="' + directory + project[:-3] + '.html"><div class="project_card">'
            project_card += '<p class="title">' + project_obj.get_title() + '</p>'
            project_card += '<p class="date">' + project_obj.get_date() + '</p>'
            project_card += '<img class="cover_image" src="' + '../' * directory.count("/") + project_obj.get_image() + '" />'
            project_card += '<p class="summary">' + project_obj.get_summary() + '</p>'
            project_card += '</div></a>'
            project_cards.append((project_obj.get_date(), project_card))
    
    project_cards = sorted(project_cards ,reverse = True)
    return list(list(zip(*project_cards))[1])