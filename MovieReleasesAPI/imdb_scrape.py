from bs4 import BeautifulSoup
import requests


def scrape():
    movie_list = []
    base_url = 'https://www.imdb.com/calendar/?region=pt'

    # Request URL and Beautiful Parser
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # all dates are contained in a h4 tag
    all_dates = soup.find_all('h4')
    # get all the unordered list that contain the list of movies
    list_of_movies = soup.find('div', {'id': 'main'}).find_all('ul')

    # the response will be in a json format
    construct_response = []

    for date, ultag in zip(all_dates, list_of_movies):
        dates_dict = {}
        dates_dict['date'] = date.text
        construct_response.append(dates_dict)

    return construct_response


if __name__ == "__main__":
    print(scrape())
