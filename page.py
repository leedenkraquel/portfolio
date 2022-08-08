###
# Name: page.py
# Auhtor(s): Leeden Raquel
# Description: every page in the site is created by this script. It 
#  adds the navbar and the footer to each page
###

def write_header (page, directory, stylesheets):
    subdirectory = directory[:1 + directory.rfind("/")]
    page.write('''
        <head>
            <title>Leeden R | Portfolio</title>
            <link rel="stylesheet" href="''' + subdirectory + '''styles.css" />''')

    for stylesheet in stylesheets:
        page.write('<link rel="stylesheet" href="' + stylesheet + '" />')

    page.write('''
            <link rel="icon" type="image/x-icon" href="images/favicon.png" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        </head>
    ''')
    return page

def write_navbar (page):
    page.write('''
        <div class="navbar">
            <a class="menu_obj" href="#"><img class="inverted menu_button" src="images/menu.png" /></a>
            <a class="navbar_obj" href="/">Home</a>
            <a class="navbar_obj" href="/projects/">Projects</a>
            <a class="navbar_obj" href="/essays/">Essays</a>
            <a class="navbar_obj" href="/resume/">Resume</a>
        </div>
    ''')
    return page

def write_body (page, body):
    page.write('<div class="site_body">')
    page.write(body)
    page.write('</div>')
    return page

def write_footer (page):
    page.write('''
        <div class="footer">
            <div class="footer_col">
                <a class="sitemap_obj" href="/">Home</a>
                <a class="sitemap_obj" href="/projects/">Projects</a>
                <a class="sitemap_obj" href="/essays/">Essays</a>
                <a class="sitemap_obj" href="/resume/">Resume</a>
            </div>
            <div class="footer_col">
                <p>icons</p>
            </div>
            <div class="footer_col">
                <p>Quote</p>
            </div>
        </div>
    ''')
    return page

def create_page (directory, body, stylesheets = []):
    page_html = open(directory, "w")
    page_html = write_header(page_html, directory, stylesheets)
    page_html.write('<body>')
    page_html = write_navbar(page_html)
    page_html = write_body(page_html, body)
    page_html = write_footer(page_html)
    page_html.write('</body>')