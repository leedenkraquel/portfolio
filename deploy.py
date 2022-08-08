from about.about import create_about_me_page
from home import create_home_page
import sys
from page import create_page
from home import create_home_page
from about.about import create_about_me_page
###
# Name: deploy.py
# Author(s): Leeden Raquel
# Description: used by github actions to recreate all static html pages in the website
#  whenever a commit is made
###

create_page("index.html", create_home_page(), ["home.css"])
create_page("essays/index.html", "<p>essays page</p>")
create_page("about/index.html", create_about_me_page(), ["about.css"])