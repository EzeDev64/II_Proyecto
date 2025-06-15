#https://www.geeksforgeeks.org/modify-json-fields-using-python/
#https://www.geeksforgeeks.org/read-json-file-using-python/

import json

def read_file():
    with open('hall.json', 'r') as file:
        data = json.load(file)

    return data

def change_scores(score):
    keys = ['val1', 'val2', 'val3', 'val4', 'val5']

    with open('hall.json', 'r') as json_file:
        data = json.load(json_file)

    id = high_score(score,data,0,keys,len(data))

    print(id)
    if id == None:
        return
    
    field_key = keys[id]

    if field_key in data:
        data[field_key] = score

    with open('hall.json', 'w') as file:
        json.dump(data,file,indent=2)


def high_score(score,data,id,keys,lenght):
    if id == lenght:
        return 
    else:
        if score >= data[keys[id]]:
            print(score,data[keys[id]])
            return id
        else:
            return high_score(score,data,id+1,keys,lenght)
        
