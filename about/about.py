from os import listdir
from parse_md import parse_md

###
# Name: about.py
# Auhtor(s): Leeden Raquel
# Description: generates a string that represents the html for the about me page. The about me page
#  should show a resume about me, my skills, experience, and 
###

def create_about_me_page ():
    about_page = '''
        <img class="profile_picture" src="../images/profile-picture.jpg" alt="headshot" />
        <h1>About</h1>
        <p class="about_body">My name is Leeden. I am a student at the University of Hawaii at Manoa. I currently study Computer Science with a focus on Data Science and will be earning my B.S. in the upcoming Fall 2022 term. I have a passion for development in machine learning, application development, and software engineering. In my free time I enjoy playing tabletop games, cooking, and coding up fun projects.</p>
        <div class="hr"></div>
        <h2>Experience</h2>
        <div class="hr"></div>
        <h2>Skills</h2>
        <div class="hr"></div>
        <h2>Education</h2>
        <div class="hr"></div>
        <h2>Volunteering</h2>
        <div class="hr"></div>
        <h2>Awards</h2>
        <div class="hr"></div>
    '''
    return about_page
