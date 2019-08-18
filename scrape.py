from stackapi import StackAPI
SITE = StackAPI('stackoverflow')
tag = 'C++'
questions = SITE.fetch('questions', fromdate=1257136000, todate=1457222400, min=20, tagged=tag, sort='votes')
f = open("questions.csv", "a+")
# f.write("tag, link, other_tags\n")
for q in questions['items']:
	f.write(tag + ", " + q['link'] + ", ")
	for t in q['tags']:
		f.write(t + ";")
	f.write("\n")
f.close()
