alright.
let's save some local HTML
i feel bad constatnly hitting the server like this
we're still debugging
almost getting to the nitty gritty

we have the text

$ brew install enchant  # used by pyenchant



request each pach of banadio.com
get the main content block of content, some #div-id
push the raw text content to an array
loop through that array and spell check each one
if it is incorrect then tell us what page it belong to, the url
add that url to a list that keeps track of all the pages and the errors

we spit out a txt file like this:
/article/title-of-article - 4 errors
"wgat", "thogh", "pcrincple", "adpl"

libs:
enchant       spellchecking - https://pythonhosted.org/pyenchant/api/enchant.html
requests
beautifulsoup4

might be useful:
pybloomfiltermmap
http://axiak.github.io/pybloomfiltermmap/
https://github.com/axiak/pybloomfiltermmap
lxml.cssselect
      http://lxml.de/cssselect.html
grequests
      pip install grequests
      https://github.com/kennethreitz/grequests
readability-lxml
      pip install readability-lxml
      https://pypi.python.org/pypi/readability-lxml

//*[@id="main-left-sidebar"]/div/div/div[2]/div[3]/div[125]/div/span/div/h4/a

shoutout to http://jakeaustwick.me/python-web-scraping-resource/
for being there

----------------------------------------

so we're spellchecking on every page
arrays:
pages_with_errors = []
page = {
  "url" = "/article/title-of-article",
  "errors" = [
      "wgat", "thogh", "pcrincple", "adpl"
  ]
}

definitely articles pages
      https://www.bonadio.com/news-events/articles
      https://www.bonadio.com/news-events/articles?field_author_or_authors_target_id=All&field_related_industries_tid=All&field_related_services_tid=All&name=&page=1
all the news stories are on one page
      https://www.bonadio.com/news-events/news
each person has a bio page
      https://www.bonadio.com/our-people
      https://www.bonadio.com/our-people?field_first_name_value=&field_last_name_value=&tid=All&tid_1=All&tid_2=All&page=10
services, 3 of them have subcategories
every industry served has a subcategory

specific pages:
https://www.bonadio.com/careers/why-bonadio
https://www.bonadio.com/careers/bonadio-promise
https://www.bonadio.com/careers/internships

code for paginated content

base_url = "http://some-url.com/something/?page=%s"
for url in [base_url % i for i in xrange(10)]:
    r = requests.get(url)



#node-542
 node node-page view-mode-full
