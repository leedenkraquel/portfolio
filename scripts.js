// the nav bar is at the top of the screen and is used to navigate the different pages in the site
const navbar = `
<p id="logo">Portfolio</p>
<a id="nav_obj" class="site" href="https://www2.hawaii.edu/~leeden/contact/">Contact Me</a>
<a id="nav_obj" class="site" href="https://www2.hawaii.edu/~leeden/essays/">Essays</a>
<a id="nav_obj" class="site" href="https://www2.hawaii.edu/~leeden/projects/">Projects</a>
<a id="nav_obj" class="site" href="https://www2.hawaii.edu/~leeden/">Home</a>
<a id="nav_obj_mobile" class="material-icons" href="#" onclick="toggleSideMenu(); return false;">menu</a>`;
// the side nav bar is at the right side of the screen and is used to navigate the different pages in the site
const sidenav = `
<a id="side_nav_obj" href="https://www2.hawaii.edu/~leeden/">Home</a>
<a id="side_nav_obj" href="https://www2.hawaii.edu/~leeden/projects/">Projects</a>
<a id="side_nav_obj" href="https://www2.hawaii.edu/~leeden/essays/">Essays</a>
<a id="side_nav_obj" href="https://www2.hawaii.edu/~leeden/contact/">Contact Me</a>`;
// the footer is at the lowest part of the screen and displays the site map some social information and a neat quote
const footer = `
<div id="footer_col"><a id="sitemap" class="site" href="https://www2.hawaii.edu/~leeden/">Home</a>
    <a id="sitemap" class="site" href="https://www2.hawaii.edu/~leeden/projects/">Projects</a>
    <a id="sitemap" class="site" href="https://www2.hawaii.edu/~leeden/essays/">Essays</a>
    <a id="sitemap" class="site" href="https://www2.hawaii.edu/~leeden/contact/">Contact Me</a>
</div>
<div id="vert_rule"></div>
<div id="footer_col">
    <a id="social" class="material-icons" href="https://leedenkraquel.github.io/" target="_blank">account_circle</a>
    <a id="social" href="http://github.com/leedenkraquel" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/2048px-Octicons-mark-github.svg.png" class="invert" height="24px" />
    </a>
    <a id="social" href="http://linkedin.com/in/leeden-raquel" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/61/61109.png" class="invert" height="24px" />
    </a>
</div>
<div id="vert_rule"></div>
<div id="footer_col">
    <a>Quote</a>
</div>`;

// when a page is loaded run the on load function to draw overlay components
window.onload = function(event){onLoad();}
window.onpopstate = function(event){onLoad();}

/*
 * Name: onLoad
 * Author(s): Leeden Raquel
 * Inputs:
 *  None
 * Description: called when page loads in to draw the overlay components
 * Returns:
 *  None
 */
function onLoad() {
    const navbarDiv = document.getElementById('nav_bar');
    const sidenavDiv = document.getElementById('side_nav');
    const footerDiv = document.getElementById('footer');
    navbarDiv.innerHTML = navbar;
    sidenavDiv.innerHTML = sidenav;
    footerDiv.innerHTML = footer;
}
/*
 * Name: toggleSideMenu
 * Author(s): Leeden Raquel
 * Inputs:
 *  None
 * Description: toggles whether the side menu is being displayed
 * Returns:
 *  None
 */
function toggleSideMenu() {
    if (document.getElementById("nav_obj_mobile").innerHTML == "menu") {
        document.getElementById("nav_obj_mobile").innerHTML = "close";
        document.getElementById("side_nav").style.width = "200px";
        document.getElementById("nav_bar").style.paddingRight = "200px";
    } else {
        document.getElementById("nav_obj_mobile").innerHTML = "menu";
        document.getElementById("side_nav").style.width = "0px";
        document.getElementById("nav_bar").style.paddingRight = "50px";
    }
}
