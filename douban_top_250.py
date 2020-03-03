import requests
from bs4 import BeautifulSoup as bs


def get_movie_info(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['User-Agent'] = user_agent

    response = requests.get(url, headers=header)
    # print(response)
    bs_info = bs(response.text, 'html.parser')

    for tags in bs_info.find_all('a', ):
        for node in tags.find_all('span', {'class': 'title'}):
            print(node.text)
            print(tags.get('href'))


def main():
    print("hello, word~")
    urls = tuple(
        f'https://movie.douban.com/top250?start={page * 25}' for page in range(10))

    for url in urls:
        get_movie_info(url)
    print("end")


if __name__ == "__main__":
    main()
