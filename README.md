## Scraping stackoverflow using API to get questions

**Our aim:** while a user tries to post a new question in a forum, we want a list of relevant questions which have already been asked on the platform and have been answered too. If that helps, then the user can select from the list, thus helping the user as well as reducing question redundancy in the platform.

> **StackAPI** is used to extract questions, which extracts questions posted in stackoverflow with one of its tags as the one provided as argument.

> **Installation**: pip install -r requirements.txt 

To extract questions for a particular tag, the tag should be provided as an argument to the file scrape.py

> Example: _python scrape.py c++_ will fetch questions with tag _c++_

If the tag arguement contains multiple words, the entire entry is split into separate words and questions which contain all of these words as their tags are fetched.

The extracted questions are saved in the folder _extracted_questions_. A new file is generated with the name of the arguement provided by the user.

The extracted questions are saved in a csv format with the following columns:
> question_id, tag, link, tags, accepted_answer