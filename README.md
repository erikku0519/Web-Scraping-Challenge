# Web Scraping Challenge

In this exercise, I guilt an web application that scrapes data from five different websites to gather data related to the Mission to Mars and ultimately displays the information in a single HTML webpage, with following steps along the way:<br>

PART 1: Logic for Web App: Initial Scrapping: mission_to_mars.ipynb<br>
* NASA Mars News Site was used to collect the latest New Title and Paragraph Text.(br>
* JPL Featured Space Image Page was used along with Splinter to scrape jpg image file.<br>
* Mars Weather Twitter account was used to scrape latest Mars weather tweets.<br>
* Mars Fact Website was used along with Pandas to gather the facts table about Mars<br>
* USGS Astrogeology site was used to get the images of 4 hemispheres of Mars<br>
<br>


PART 2: Web App: Application and MongoDB<br>

Step 1: Convert mission_to_mars.ipynb to scrape_mars.py to put all the scarapped ata into a single Python dictionary.<br>
Step 2: Use /scrape route to import Python script and enable scrapping of data<br>
Step 3: Use PyMongo to create a new database and collection to store the scrapped data.<br>
Step 4: Create a root 

PART 3: Front End: HTML and BootStrap<br>

* Create an HTML file (index.html) for client-facing webpage. 
