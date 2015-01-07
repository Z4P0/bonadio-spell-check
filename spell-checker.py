import requests
from bs4 import BeautifulSoup
from enchant.checker import SpellChecker

# with open("test.txt", "r") as myfile:
#     data = myfile.read()
# print(type(data))


BASE_URL = "http://www.bonadio.com/"


# our spellcheck library from pyenchant
chkr = SpellChecker("en_US")


# we generate a list of URLs to hit first
# we append a few ourselves, but progrmatically add most
pages = [
    BASE_URL,
    BASE_URL + "careers/why-bonadio",
    BASE_URL + "careers/bonadio-promise",
    BASE_URL + "careers/internships",
    # BASE_URL + "lol"
]

# these pages didn't load
broken_pages = []
all_links_ever = []

# give some feedback
print("Pages to scrape:")
print(pages)


# ============================================================
# ============================================================
# add article urls
#       https://www.bonadio.com/news-events/articles
#       https://www.bonadio.com/news-events/articles?field_author_or_authors_target_id=All&field_related_industries_tid=All&field_related_services_tid=All&name=&page=1
# ?field_author_or_authors_target_id=All&field_related_industries_tid=All&field_related_services_tid=All&name=&page=1
#       https://www.bonadio.com/our-people
#       https://www.bonadio.com/our-people?field_first_name_value=&field_last_name_value=&tid=All&tid_1=All&tid_2=All&page=10


# we pass a BeautifulSoup object
def spellcheck(soup):
    print("spellcheck")
    content = soup.find(id="main-left-sidebar")
    if content is not None:
        # print(soup.find(id="main-left-sidebar").get_text())
        text = soup.find(id="main-left-sidebar").find("div", {"class": "main"}).get_text(strip=True)
        # text = soup.find(id="main-left-sidebar")
        # text = text.find_all("div", {"class": "main"}).get_text(strip=True)
        # text = soup.find(id="main-left-sidebar").get_text(strip=True)
        chkr.set_text(text)
        for err in chkr:
            print("ERROR: " + err.word)

    else:
        print("no #main-left-sidebar")


# we pass a BeautifulSoup object
def check_for_links(soup):
    print("check_for_links")
    # for link in soup.find_all('a'):
    #     print(link.get('href'))


# the real deal
# ============================================================
# ============================================================


# go through all the pages
for index, page in enumerate(pages):
    # print(index, page)
    # request each page
    print("scrpaing page.." + page)
    response = requests.get(page)

    # use response.status_code to check if there is a broken link
    if response.status_code == 404 or response.status_code == 503:
        broken_pages.append(page)
    else:
        # we have a valid page (and content), so make our html soup
        soup = BeautifulSoup(response.text)
        # for each page we get the text content and spellcheck
        spellcheck(soup)
        check_for_links(soup)


# print(all_links_ever)


# output the file
# ============================================================

# output_file = open("text.html", "w")
# output_file.write(response.content)
# output_file.close()


# # output all links to a file
# output_file = open("links.txt", "w")
# for link in all_links_ever:
#     output_file.write("%s\n" % link)
# output_file.close()
