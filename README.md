# Horse Hangman


## Overview

[Embarr Equestrian Testimonials](https://embarr-equestrian-testimonials.herokuapp.com/) is a site page that allows clients/ visitors to post a review/ testimonial on services provided by Embarr Equestrian.


### The Site 



<div><h2>
Site Mockup
</h2></div>


## Flowchart


## Database Entity Diagram


## User Experience

Goals:



First Time User:


Returning/ Regular Visitor: 




## Features 



### Features Left to Implement
       

## Frameworks & Languages Used
- Django
- Python

Python Packages:

-
- OS: modules provide numerous tools to deal with filenames, paths, directories


## Frameworks, Libaries and technologies used

- [Git/ Github](https://github.com/) - Git/Github was used for version control, storage and deployment of the project.
- [Heroku](https://www.heroku.com/) - Heroku was used to deploy and create the terminal application.
- [Techsini](https://techsini.com/multi-mockup) - This was used for the mockup image in the overview.


## Testing Conducted 

### Usability testing 


### Bugs




### Content 

I reviewed all content on the site for:
- Grammar and spelling mistakes
- Hangman pictures are placed properly with proper sizes & displaying as expected
- Instructions are clear and contain correct information
- Verified all text/ headings are displaying correctly


### Validation

I ran all the Python Code through [PEP8](http://pep8online.com/)


## Lighthouse

Lighthouse was used to test Performance, Best Practices, Accessibility and SEO on Desktop.

<img src=images/lighthouse.JPG>


## Credits

Python Code inspired and adapted from the following tutorials and sources:

- https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman

- https://inventwithpython.com/invent4thed/chapter8.html

- https://www.w3schools.com/python/default.asp

- https://www.youtube.com/watch?v=pFvSb7cb_Us

- https://note.nkmk.me/en/python-textwrap-wrap-fill-shorten/

- https://www.sololearn.com/Discuss/1582033/how-to-check-if-input-is-empty-in-python

- Code Institute - Blog 

Flowchart created in:

- https://app.diagrams.net/


### Content

All content was written by the project owner.


### Readme 

- I used the 
[Markdown cheat sheet](https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md) and the [love running template ](https://github.com/Code-Institute-Solutions/readme-template )to help put together my readme.


### Acknowledgments




# Deployment

The site was deployed to Heroku. 

The steps to deploy are as follows: 

- Log in to Heroku or create an account
- On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App
- You must enter a unique app name
- Next select your region
- Click on the Create App button
- The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
- Click Reveal Config Vars and enter port into the Key box and 8000 into the Value box and click the Add button
- Scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
- Repeat step 8 to add node.js. o Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order
- Go to the top of the page and choose the Deploy tab
- Select Github as the deployment method
- Confirm you want to connect to GitHub
- Search for the repository name and click the connect button
- Scroll to the bottom of the deploy page and select the preferred deployment type
- Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

  - On submission the project is forked in Github, by forking the project a copy of the original repository is made that can be viewed without affecting the original repository by following these steps: In the GitHub repository, locate the settings, above this is the option to 'fork', select this to create a copy

  - Cloning a repository: When you create a repository on GitHub.com, it exists as a remote repository. You can clone your repository to create a local copy on your computer and sync between the two locations. It makes it easier to fix merge conflicts, add or remove files, and push larger commits. 

The live link can be found here - https://horse-hangman.herokuapp.com/ 