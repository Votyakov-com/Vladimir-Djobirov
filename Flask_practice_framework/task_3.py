from flask import Flask, request

app = Flask(__name__)
tasks = []
task_id = 1


@app.post("/tasks")
def tasks_post():
    global task_id
    data = request.json
    task = dict()
    task["description"] = data["description"]
    task["task_id"] = task_id
    task["title"] = data["title"]
    tasks.append(task)
    task_id += 1
    return (task, 200, {"content-type": "application/json"})


@app.get("/tasks")
def tasks_get():
    return (tasks, 200, {"content-type": "application/json"})


app.run()
