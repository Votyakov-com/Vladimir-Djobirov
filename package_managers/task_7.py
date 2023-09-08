import wikipedia

array_of_title = wikipedia.search('Computer program')

page = wikipedia.page(array_of_title[0])
print(page.title)
print(page.url)
print(page.summary)
print(page.content)

links = page.links
print(links)
