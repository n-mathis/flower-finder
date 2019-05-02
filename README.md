# The Flower Finder Web App
## By: Alanna DeMuro, Isaiah Fujii Bresnihan, Lizzy Riffle, NaNa Mathis

### Flower Finder is a web application built by four computer science students for a class project. We use a ResNet34 machine learning model that accurately predicts (5% error rate) the flower type from an image that the user uploads. 

If you are interested in checking out the repository, here is some helpful information. 

## Setup folder: 
- The set up folder holds all the necessary files to get the web app running on an AWS ec2 instance. The README file included in that folder provides instructions on how to set it up, from our professor, Prof Z. You should only use this setup if you are in the CS121 class at Harvey Mudd College during Spring 2019.
<br> 
## App folder:
- The app folder stores the model we trained, our routing file, all of the data we are using to provide users with more information about the flowers, and the templates folder. 
	## - Templates folder: 
		- The templates folder holds all of our .html front-end code. Each page of the web app has its own
		html file. However, base.html is the file that extend across all of our files to ensure
		consistency. They hold the background color, the navigation, and thefooter. The rest of the file
		names correspond to the page names. For example, database.html refers to the Databse tab on the
		website. 
		
##Static folder: 
The static folder holds all of our .css files, images, and a JavaScript folder.
	##- css: 
		- This folder houses all of the .css styling files for our app. The stylesheet.css is the main
		stylesheet that sets the background, navigation bar, and most text on the website for all of the
		pages on the website. The rest of the file names correspond to the page names on our website. For
		example, identify.css is the style sheet for the Identify page and styles the identify.html file. 
	##- imgs:
		- We use this folder to hold all the images that are displayed on our website. For example, the 
		Database images and the About page images. 
	##- js:
		- main.js is used to display information on the displayResults.html page. 
