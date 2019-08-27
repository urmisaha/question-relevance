## Scraping stackoverflow using API to get questions

**Our aim:** while a user tries to post a new question in a forum, we want a list of relevant questions which have already been asked on the platform and have been answered too. If that helps, then the user can select from the list, thus helping the user as well as reducing question redundancy in the platform.

> **StackAPI** is used to extract questions, which extracts questions posted in stackoverflow with one of its tags as the one provided as argument.

> **Installation**: pip install -r requirements.txt 

To extract questions for a particular tag, the tag should be provided as an argument to the file scrape.py

> Example: _python scrape.py c++_ will fetch questions with tag _c++_