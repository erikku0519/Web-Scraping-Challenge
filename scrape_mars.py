
# Python Code for the Web App to scrape data and return a Library
#Import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time
from selenium import webdriver

# Define /Scrape function
def scrape():
    # Create a library that holds all the Mars' Data
    mars_library = {}

    #### PART 1: NASA Mars News ####
    # Initiate ChromeDriver
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Target URL
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Create a Beautiful Soup object
    html=browser.html
    soup=bs(html,"html.parser")

    # Latest News Title and Paragraph
    news_title = soup.find("div",class_="content_title").text
    news_paragraph = soup.find("div", class_="article_teaser_body").text
    print(f"Title: {news_title}")
    print(f"Para: {news_p}")

    # put infos into Library
    mars_library['news_title'] = news_title
    mars_library['news_paragraph'] = news_paragraph

    #### PART 2: JPL Mars Space Images ####

    # Target URL
    image_url= "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)

    # Create a Beautiful Soup object
    html=browser.html
    soup2=bs(html,"html.parser")

    # Featured Image
    image_url_route= soup2.find_all('a', class_='fancybox')[0].get('data-fancybox-href').strip()

    # Full Address
    featured_image_url="https://www.jpl.nasa.gov/"+image_url_route
    print(featured_image_url)

    # put infos into Library
    mars_library['featured_image_url'] = featured_image_url


    #### PART 3: Mars Weather ####

    # Target Twitter URL
    twitter_url="https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)

    # Create a Beautiful Soup object
    html=browser.html
    soup3=bs(html,"html.parser")

    # Latest Mars Weather Tweet
    mars_tweet=soup3.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].text
    print(mars_tweet)

    # put infos into Library
    mars_library['mars_weather'] = mars_weather

    #### PART 4: Mars Fact ####

    # Target URL
    url="https://space-facts.com/mars/"

    # Import URL to Panda
    table=pd.read_html(url)

    mars_fact_df=table[0]
    mars_fact_df.columns = ["Category", "Stats"]
    mars_fact_df.set_index(["Category"])

    # Exporting as HTML Table
    mars_fact_html = mars_fact_df.to_html()
    mars_fact_html = mars_fact_html.replace("\n", "")

    mars_fact_df.to_html('mars_fact_df.html')

    # Put infos into Library
    mars_library['mars_facts'] = mars_facts_df


    #### PART 5: Mars Hemispheres ####

    # Target URL
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    # Use splinter to loop through the 4 images and load them into a dictionary
    html = browser.html
    soup = bs(html, 'html.parser')
    mars_hemis=[]

    # loop through the four tags and load the data to the dictionary

    for i in range (4):
        time.sleep(5)
        images = browser.find_by_tag('h3')
        images[i].click()
        html = browser.html
        soup = bs(html, 'html.parser')
        partial = soup.find("img", class_="wide-image")["src"]
        img_title = soup.find("h2",class_="title").text
        img_url = 'https://astrogeology.usgs.gov'+ partial
        dictionary={"title":img_title,"img_url":img_url}
        mars_hemis.append(dictionary)
        browser.back()

    # Put infos into Library
    mars_library['hemisphere_image_urls']=mars_hemis


    # Return Library
    return mars_library
