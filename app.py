from flask import Flask, request, jsonify, Response;
from flask_sqlalchemy import SQLAlchemy;
from flask_marshmallow import Marshmallow;

app = Flask(__name__);
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///product.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False;

db = SQLAlchemy(app);
ma = Marshmallow(app);

app.app_context().push()
#Modelo de db Task
class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True);
    title = db.Column(db.String(70), unique =True);
    description = db.Column(db.String(100));
    
    def __init__(self, title, description):
        self.title = title
        self.description = description
        
            
db.create_all()

class TaskSchema(ma.Schema):
    class Meta:
        fields =('id', 'title', 'description')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@app.route('/tasks', methods = ['POST'])
def create_task():
    print(request)
    title = request.json['title']
    print(title)
    description = request.json['description']
    new_task = Task(title, description)
    
    db.session.add(new_task)
    db.session.commit()
    return 'Hecho'

@app.route('/task/<id>', methods =['GET'])
def get_task_by_id(id):
    task = Task.query.get(id)
    return task_schema.jsonify(task)
    
@app.route('/tasks', methods =['GET'])
def get_tasks():
    tasks = Task.query.all()
    result = tasks_schema.dump(tasks)
    
    return jsonify(result),202

@app.route('/task/<id>', methods =['DELETE'])
def delete_task_by_id(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return task_schema.jsonify(task)


@app.route('/task/<id>', methods =['PUT'])
def update_task_by_id(id):
    task = Task.query.get(id)
    title = request.json['title']
    desc = request.json['description']
    task.title = title
    task.description = desc
    db.session.commit()
    return task_schema.jsonify(task)
if __name__ == "__main__":
    app.run(debug=True)
    
'''
def canGenerateWord(word, blocks):
    block_list = list(blocks.split(","))
    new_block = []
    for j in range(0, len(block_list)):
        sublist = []
        sublist[:0] = block_list[j]
        new_block.append(sublist)
    
    position = []

    for i in range(0, len(block_list)):
        for x in range(0,2):
            for w in word:
                if new_block[i][x] == w:
                    
                    position.append(i)
                    
    selected_blocks = list(set(position))

    if len(selected_blocks) >= len(word):
        return True
    else:
        return False

if __name__ == '__main__': 
'''