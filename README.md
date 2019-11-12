## Scraping stackoverflow using API to get questions

**Our aim:** while a user tries to post a new question in a forum, we want a list of relevant questions which have already been asked on the platform and have been answered too. If that helps, then the user can select from the list, thus helping the user as well as reducing question redundancy in the platform.

> **StackAPI** is used to extract questions, which extracts questions posted in stackoverflow with one of its tags as the one provided as argument.

> **Installation**: pip install -r requirements.txt 

To **extract** questions for a particular tag, the tag should be provided as an argument to the file scrape.py

> Example: _python scrape.py c++_ will fetch questions with tag _c++_

If the tag arguement contains multiple words, the entire entry is split into separate words and questions which contain all of these words as their tags are fetched.

The extracted questions are saved in the folder _extracted_questions_. A new file is generated with the name of the arguement provided by the user.

The extracted questions are saved in a csv format with the following columns:
> question_id, tag, link, tags, accepted_answer

The scraped data is stored in mongodb. An example is shown below to describe the format:

```json
{
  "_id": ObjectId("5da5f437f4443ca75c2dc097"),
  "tags": [
    "java",
    "c++",
    "performance",
    "optimization",
    "branch-prediction"
  ],
  "owner": {
    "reputation": 313531,
    "user_id": 87234,
    "user_type": "registered",
    "accept_rate": 100,
    "profile_image": "https://i.stack.imgur.com/FkjBe.png?s=128&g=1",
    "display_name": "GManNickG",
    "link": "https://stackoverflow.com/users/87234/gmannickg"
  },
  "is_answered": true,
  "view_count": 1406174,
  "protected_date": 1399067470,
  "accepted_answer_id": 11227902,
  "answer_count": 23,
  "score": 23514,
  "last_activity_date": 1571096080,
  "creation_date": 1340805096,
  "last_edit_date": 1569980131,
  "question_id": 11227809,
  "link": "https://stackoverflow.com/questions/11227809/why-is-processing-a-sorted-array-faster-than-processing-an-unsorted-array",
  "title": "Why is processing a sorted array faster than processing an unsorted array?"
}
```

To **fetch** questions related to an input query, the query should be provided as an argument to the file query.py

> Example: _python query.py "what is c++"_ will fetch top voted questions with tag _c++_


