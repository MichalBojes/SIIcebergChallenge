import json

with open('test.json') as test:
    test_data = json.load(test)
    for p in test_data:
        print('Id: ' + p['id'])
        print('')

with open('train.json') as test:
    train_data = json.load(test)
    for p in test_data['people']:
        print('Id: ' + p['id'])
        print('')