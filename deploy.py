from page import create_page

###
# Name: deploy.py
# Author(s): Leeden Raquel
# Description: used by github actions to recreate all static html pages in the website
#  whenever a commit is made
###

create_page("index.html", "")