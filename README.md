# Web-Scraping-Football-Match-Day-Data-with-BeautifulSoup
Overview

This Python script scrapes football match details from the Yallakora website for a given date. It extracts match results, team names, match times, and championship types, then saves the data into a CSV file.

Requirements

Ensure you have the following dependencies installed:

pip install requests beautifulsoup4 lxml

Usage

Run the script in a terminal or command prompt:

python script.py

Enter the desired date in the format M/D/YYYY when prompted.

The script fetches match details for that date and saves them in a CSV file.

Output

The data is stored in a file named web_scraping.csv 

The CSV file contains the following columns:

النتيجة (Match Result)

الموعد (Match Time)

الفريق الثانى (Team B)

الفريق الاول (Team A)

نوع البطولة (Championship Type)

Code Explanation

The script makes an HTTP request to Yallakora's match center page.

It parses the HTML response using BeautifulSoup.

It extracts relevant match data and stores it in a list of dictionaries.

The extracted data is saved in a tab-separated CSV file.

Notes

Ensure you have an active internet connection while running the script.

If no matches are found for the given date, the script will display a message.

The CSV file will be encoded in UTF-8 to support Arabic text.

License

This project is open-source and free to use. Modify it as needed for personal or educational purposes.

Author

Developed by Omar.
