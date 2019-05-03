# Introduction: 
   This page gives an overview of how the code is formatted for the
   Flower Finder project to help increase understanding and allow 
   anyone to add more functionalities if they please. We also created 
   this coding style guide to help the grutors of our project navigate 
   through the code more easily.

   The website code is mainly built with HTML and CSS. Python and 
   JavaScript are used to pass in information about the flowers and
   the prediction results. 

   If you are interested in helping to iterate on this project, please 
   git clone the code from GitHub at https://github.com/n-mathis/cs121 
   and submit a pull request with your changes. We will review the pull 
   requests and accept them if they align with our project goals, do 
   not have any unethical aspects, and works well with our existing code.

   To create this style guide, we consulted the Python style guide, 
   which can be found here: https://www.python.org/dev/peps/pep-0008/
    
   Thank you!

# Tabs vs Spaces:
   All Flower Finder code is formatted with four spaces.

# Indentation:
   All files have matching indentations where the head and body elements 
    are on the left most side and each element in between the tags are
    indented by one. Text for the website is on its own line and  
    div, p, and other tags are all in the same column as their closing 
    tags.

# Blank Lines:
   There are blank lines between different tags and elements so code 
    blocks and specific sections can be easily found. 
    ![](/static/img/indentation_blank_spaces.png)

# Line Breaks:
   When there are line breaks, the br element is one line above the next 
    div element and there is a blank line above the br element. 
   ![](/static/img/linebreak.png)
   
# Naming conventions:
   Flower Finder classes, methods, and functions are all named to 
    correspond with what they represent. For example, page title classes 
    for all pages are titled "page-title" and if the text styling is 
    different for a certain page they are titled "pagenamepage-title."

# Imports:
   Imports do not need to be on separate lines, but please separate 
    lines when possible. All imports are at the top of the file. The 
    order should be: 
        <ol>
            <li> Standard library imports </li>
            <li> Related third party imports </li>
            <li> Local application/library specific imports </li>
        </ol>

# Maximum line length:
   The maximum line length for Flower Finder code is 80 lines except for 
    instances where lines cannot be broken up, like URLs and calls to the 
    JavaScript and Python code.

# Images:
   All images are stored in the img folder under the static folder. 

   Alt labels must be used for this project to increase accessibility.  



