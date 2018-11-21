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
        movies_per_date = []
        list_of_lis = ultag.find_all('li')
        for litag in list_of_lis:
            movie = {}
            movie['name'] = litag.get_text(strip=True).split('(')[0]
            movie['url'] = 'https://www.imdb.com'+litag.a.get('href')
            movie['imdb_id'] = litag.a.get('href').split('/')[2]
            movies_per_date.append(movie)
        dates_dict['movies'] = movies_per_date
        construct_response.append(dates_dict)

    return construct_response


if __name__ == "__main__":
    print(scrape())
