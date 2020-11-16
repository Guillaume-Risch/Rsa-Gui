import json

my_dict = {'home': 'CHI', 'sport': 'NFL', 'playedStatus': 'UNPLAYED', 'away': 'SEA'}
json_dict = json.dumps(my_dict)
print(json_dict)