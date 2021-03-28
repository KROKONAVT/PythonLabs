import json

ids = []
completed_tasks = []
to_out = []

with open('in.json', 'r') as file:
    json_file = json.load(file)

for task in json_file:
    userID = task['userId']
    completed = task['completed']
    pos = -1
    for i in range(0, len(ids)):
        if ids[i] == userID:
            if completed == True:
                completed_tasks[i] += 1
            pos = i
    if pos == -1:
        ids.append(userID)
        if completed == True:
            completed_tasks.append(1)
        else:
            completed_tasks.append(0)
    
for i in range(0, len(ids)):
    out_element = {}
    out_element["userId"] = ids[i]
    out_element["task_completed"] = completed_tasks[i]
    to_out.append(out_element)
    
with open('out.json', 'w') as file:
    file.write(json.dumps(to_out, indent=2))