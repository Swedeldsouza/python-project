import json
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt' 
records = [json.loads(line) for line in open(path)]