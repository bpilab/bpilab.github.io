from scholarly import scholarly

# Retrieve the author's data, fill-in, and print
# Get an iterator for the author results
author = scholarly.search_author_id('plrdGDcAAAAJ') # Andy Woods
scholarly.pprint(author)

# Retrieve all the details for the author
author_details = scholarly.fill(author)
scholarly.pprint(author_details)

# Print the titles of the author's publications
publication_titles = [pub['bib']['title'] for pub in author_details['publications']]
print(publication_titles)
