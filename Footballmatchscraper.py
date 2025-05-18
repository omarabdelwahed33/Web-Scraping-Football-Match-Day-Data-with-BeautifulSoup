import requests
from bs4 import BeautifulSoup
import csv

date = input("Please enter the date in this format M/D/YYYY : ")
url = f"https://www.yallakora.com/match-center/مركز-المباريات?date={date}#days"
page = requests.get(url)

def main(page):
    page.encoding = "utf-8"
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    matches_details = []

    championships = soup.find_all("div", {'class': 'matchCard'})

    def get_match_info(championship):
        championship_title = championship.find('div', {'class': 'title'}).find('h2').text.strip()
        all_matches = championship.find_all('div', {'class': 'item finish liItem'})

        for match in all_matches:
            team_A = match.find('div', {'class': 'teamA'}).find('p').text.strip()
            team_B = match.find('div', {'class': 'teamB'}).find('p').text.strip()

            # Updated score extraction
            match_result_div = match.find('div', {'class': 'MResult'})
            scores = match_result_div.find_all('span', {'class': 'score'})
            if len(scores) == 2:
                score_A = scores[0].text.strip()
                score_B = scores[1].text.strip()
                print_result = f'{score_A} - {score_B}'
            else:
                print_result = "N/A"

            match_time = match_result_div.find('span', {'class': 'time'}).text.strip()

            matches_details.append({
                'النتيجة': print_result,
                'الموعد': match_time,
                'الفريق الثانى': team_B,
                'الفريق الاول': team_A,
                'نوع البطولة': championship_title
            })

    for championship in championships:
        get_match_info(championship)

    if matches_details:
        keys = matches_details[0].keys()

        with open('C:/Users/DELL/Documents/web scrapinggg/web_scraping.csv', 'w', newline='', encoding="utf-8-sig") as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(matches_details)
            print("File created successfully!")
    else:
        print("No match details found for the given date.")

main(page)
