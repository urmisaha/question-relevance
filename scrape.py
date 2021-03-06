from stackapi import StackAPI
import sys
import pymongo
SITE = StackAPI('stackoverflow')
tag = sys.argv[1]
tags = tag.split()

filename = ""

for tag in tags:
	filename += tag + "_"

filename = filename[0:len(filename)-1]
tag_name = filename

filename += ".csv"
c = 0
f = open("extracted_questions/"+filename, "w+")
print("Fetching questions...")
f.write("question_id, tag, link, tags, accepted_answer\n")

fetched_questions = []

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.stackapi
collec_ques = db.questions

for tag in tags:
	questions = SITE.fetch('questions', fromdate=1257136000, todate=1457222400, min=20, tagged=tag, sort='votes', order='desc')
	collec_ques.insert_many(questions['items'])
	for q in questions['items']:
		for t in tags:
			if t in q['tags']:
				flag = 1
			else:
				flag = 0
		if flag == 0:
			continue
		question_id = q['question_id']
		row = ''
		if question_id not in fetched_questions:
			fetched_questions.append(question_id)
			row = (str(question_id) + "," + tag_name + ", " + q['link'] + ", ")
			for t in q['tags']:
				row += t + ";"
			row = row[0:len(row)-1] + ','
			try:
				answer_url = q['link'] + '/' + str(q['accepted_answer_id']) + '#' + str(q['accepted_answer_id'])
			except:
				continue
			f.write(row + answer_url + '\n')
			c += 1
print("Extracted " + str(c) + " questions and stored in " + filename)
f.close()