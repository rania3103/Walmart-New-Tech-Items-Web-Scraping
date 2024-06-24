#!/usr/bin/env python3
from bs4 import BeautifulSoup
import pandas as pd

for i in range(1,10):
    if i == 2:
        continue
    # Load the HTML file
    with open(f'./html_files/index{i}.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all divs with the specified class
    divs = soup.find_all('div', class_='mb0 ph0-xl pt0-xl bb b--near-white w-25 pb3-m ph1')

    # Initialize lists to store the extracted data
    links = []
    items = []
    prices = []
    reviews = []
    ratings = []
    stat = []

    # Loop through each div and extract the required data
    for div in divs:
        # Extract the image link
        img_tag = div.find('img', class_='absolute top-0 left-0')
        link = img_tag['src'] if img_tag else ''
        
        # Extract the price from spans with class "f2"
        price_tag_f2 = div.find('span', class_='f2')
        price = price_tag_f2.text.strip() if price_tag_f2 else ''
        
        # Append '.' from spans with class "f6 f5-l"
        for span_f6 in div.find_all('span', class_='f6 f5-l'):
            price += '.' + span_f6.text.strip()
        
        # Extract the item description
        item_tag = div.find('span', class_='normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy')
        item = item_tag.text.strip() if item_tag else ''

        # Extract the number of reviews
        reviews_tag = div.find('span', class_= 'sans-serif gray f7')
        number_of_reviews = reviews_tag['data-value'] if reviews_tag else ''
        
        # Extract the rating
        ratings_tag = div.find('span', class_='black inline-flex mr1')
        rating = ratings_tag['data-value'] if ratings_tag else ''

        # Extract the inventory status
        status_tag = soup.find('div', {'data-automation-id': 'inventory-status'})
        status = status_tag.text.strip() if status_tag else ''
        
        # Append the extracted data to the lists
        links.append(link)
        items.append(item)
        prices.append(price)
        reviews.append(number_of_reviews)
        ratings.append(rating)
        stat.append(status)

    # Create a DataFrame from the extracted data
    data = {
        'Item': items,
        'Price': prices,
        'Rating':ratings,
        'Number_of_reviews':reviews,
        'Status':stat,
        'Image_link': links
    }

    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv(f'./csv_files/data{i}.csv', index=False, columns=['Item', 'Price', 'Rating', 'Number_of_reviews', 'Status', 'Image_link'])
