
import csv
import json

csv_data = csv.reader(open('twitter_test.csv', 'rb'), delimiter=',')

tweets = []
next(csv_data, None)
for row in csv_data:
    t = {'uname':row[0],'content':row[1],
        'loc':{'x':row[2],'y':row[3]}}
    tweets.append(t)

with open('output.json', 'w') as outfile:
    json.dump(tweets, outfile,indent=4, sort_keys=True)
