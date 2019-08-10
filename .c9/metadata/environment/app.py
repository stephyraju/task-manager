{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":25,"position":25,"stack":[[{"start":{"row":0,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return 'Hello World ...again'","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":15,"column":0},"action":"remove","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return 'Hello World ...again'","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":21,"column":23},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId ","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":0,"column":0},"end":{"row":21,"column":23},"action":"remove","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId ","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":28},{"start":{"row":0,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","@app.route('/add_task')","def add_task():","    return render_template('addtask.html')","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)",""]}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["a"],"id":29},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["d"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["d"]}],[{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"remove","lines":["s"],"id":30}],[{"start":{"row":15,"column":34},"end":{"row":15,"column":35},"action":"remove","lines":["k"],"id":31},{"start":{"row":15,"column":33},"end":{"row":15,"column":34},"action":"remove","lines":["s"]},{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"remove","lines":["a"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"remove","lines":["t"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"remove","lines":["d"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"remove","lines":["d"]},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"remove","lines":["a"]}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["t"],"id":32},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["a"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["s"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["k"]},{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"insert","lines":["s"]}],[{"start":{"row":0,"column":0},"end":{"row":27,"column":0},"action":"remove","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","@app.route('/add_task')","def add_task():","    return render_template('addtask.html')","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)",""],"id":33},{"start":{"row":0,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","@app.route('/add_task')","def add_task():","    return render_template('addtask.html')","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)",""]}],[{"start":{"row":20,"column":42},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":34},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]},{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"insert","lines":["c"]},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"insert","lines":["a"]},{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["t"]},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["g"],"id":35},{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":["o"]},{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":["r"]},{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["i"]},{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"insert","lines":["s"],"id":36},{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"insert","lines":["m"],"id":37},{"start":{"row":21,"column":16},"end":{"row":21,"column":17},"action":"insert","lines":["o"]},{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"insert","lines":["n"]},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["g"]},{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["o"]}],[{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["."],"id":38},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"insert","lines":["d"]},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["b"]},{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"insert","lines":["."]}],[{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["c"],"id":39},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["a"]},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["t"]},{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"insert","lines":["e"]},{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["g"]}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["o"],"id":40},{"start":{"row":21,"column":30},"end":{"row":21,"column":31},"action":"insert","lines":["r"]},{"start":{"row":21,"column":31},"end":{"row":21,"column":32},"action":"insert","lines":["i"]},{"start":{"row":21,"column":32},"end":{"row":21,"column":33},"action":"insert","lines":["e"]},{"start":{"row":21,"column":33},"end":{"row":21,"column":34},"action":"insert","lines":["s"]}],[{"start":{"row":21,"column":34},"end":{"row":21,"column":35},"action":"insert","lines":["."],"id":41},{"start":{"row":21,"column":35},"end":{"row":21,"column":36},"action":"insert","lines":["f"]},{"start":{"row":21,"column":36},"end":{"row":21,"column":37},"action":"insert","lines":["i"]},{"start":{"row":21,"column":37},"end":{"row":21,"column":38},"action":"insert","lines":["n"]},{"start":{"row":21,"column":38},"end":{"row":21,"column":39},"action":"insert","lines":["d"]}],[{"start":{"row":21,"column":39},"end":{"row":21,"column":40},"action":"insert","lines":["("],"id":42},{"start":{"row":21,"column":40},"end":{"row":21,"column":41},"action":"insert","lines":[")"]}],[{"start":{"row":20,"column":41},"end":{"row":20,"column":42},"action":"insert","lines":[","],"id":43}],[{"start":{"row":20,"column":42},"end":{"row":20,"column":43},"action":"remove","lines":[")"],"id":44}],[{"start":{"row":21,"column":41},"end":{"row":21,"column":42},"action":"insert","lines":[")"],"id":45}],[{"start":{"row":18,"column":0},"end":{"row":21,"column":42},"action":"remove","lines":["@app.route('/add_task')","def add_task():","    return render_template('addtask.html',","    categories=mongo.db.categories.find())"],"id":46},{"start":{"row":18,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["@app.route('/add_task')","def add_task():","    return render_template('addtask.html',","                           categories=mongo.db.categories.find())",""]}],[{"start":{"row":21,"column":65},"end":{"row":22,"column":0},"action":"remove","lines":["",""],"id":47}],[{"start":{"row":22,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["@app.route('/insert_task', methods=['POST'])","def insert_task():","    tasks = mongo.db.tasks","    tasks.insert_one(request.form.to_dict())","    return redirect(url_for('get_tasks'))","    "],"id":48}],[{"start":{"row":21,"column":65},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":49},{"start":{"row":22,"column":0},"end":{"row":22,"column":27},"action":"insert","lines":["                           "]}],[{"start":{"row":0,"column":0},"end":{"row":34,"column":0},"action":"remove","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","@app.route('/add_task')","def add_task():","    return render_template('addtask.html',","                           categories=mongo.db.categories.find())","                           ","@app.route('/insert_task', methods=['POST'])","def insert_task():","    tasks = mongo.db.tasks","    tasks.insert_one(request.form.to_dict())","    return redirect(url_for('get_tasks'))","    ","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)",""],"id":50},{"start":{"row":0,"column":0},"end":{"row":43,"column":0},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", ","                           tasks=mongo.db.tasks.find())","","","@app.route('/add_task')","def add_task():","    return render_template('addtask.html',","                           categories=mongo.db.categories.find())","","","@app.route('/insert_task', methods=['POST'])","def insert_task():","    tasks =  mongo.db.tasks","    tasks.insert_one(request.form.to_dict())","    return redirect(url_for('get_tasks'))","","@app.route('/edit_task/<task_id>')","def edit_task(task_id):","    the_task =  mongo.db.tasks.find_one({\"_id\": ObjectId(task_id)})","    all_categories =  mongo.db.categories.find()","    return render_template('edittask.html', task=the_task,","                           categories=all_categories)","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","        port=int(os.environ.get('PORT')),","        debug=True)",""]}],[{"start":{"row":0,"column":0},"end":{"row":43,"column":0},"action":"remove","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", ","                           tasks=mongo.db.tasks.find())","","","@app.route('/add_task')","def add_task():","    return render_template('addtask.html',","                           categories=mongo.db.categories.find())","","","@app.route('/insert_task', methods=['POST'])","def insert_task():","    tasks =  mongo.db.tasks","    tasks.insert_one(request.form.to_dict())","    return redirect(url_for('get_tasks'))","","@app.route('/edit_task/<task_id>')","def edit_task(task_id):","    the_task =  mongo.db.tasks.find_one({\"_id\": ObjectId(task_id)})","    all_categories =  mongo.db.categories.find()","    return render_template('edittask.html', task=the_task,","                           categories=all_categories)","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","        port=int(os.environ.get('PORT')),","        debug=True)",""],"id":51},{"start":{"row":0,"column":0},"end":{"row":105,"column":0},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","","app = Flask(__name__)","","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\",","    tasks=mongo.db.tasks.find())","","","@app.route('/add_task')","def add_task():","    return render_template('addtask.html',","    categories=mongo.db.categories.find())","    ","    ","@app.route('/insert_task', methods=['POST'])","def insert_task():","    tasks = mongo.db.tasks","    tasks.insert_one(request.form.to_dict())","    return redirect(url_for('get_tasks'))","","","@app.route('/edit_task/<task_id>')","def edit_task(task_id):","    the_task = mongo.db.tasks.find_one({\"_id\": ObjectId(task_id)})","    all_categories = mongo.db.categories.find()","    return render_template('edittask.html', task=the_task, categories=all_categories)","","","@app.route('/update_task/<task_id>', methods=['POST'])","def update_task(task_id):","    tasks = mongo.db.tasks","    tasks.update( {'_id': ObjectId(task_id)},","    {","        'task_name':request.form.get('task_name'),","        'category_name':request.form.get('category_name'),","        'task_description': request.form.get('task_description'),","        'due_date': request.form.get('due_date'),","        'is_urgent':request.form.get('is_urgent')","    })","    return redirect(url_for('get_tasks'))","    ","    ","@app.route('/delete_task/<task_id>')","def delete_task(task_id):","    mongo.db.tasks.remove({'_id': ObjectId(task_id)})","    return redirect(url_for('get_tasks'))","","","@app.route('/get_categories')","def get_categories():","    return render_template('categories.html',","    categories=mongo.db.categories.find())","    ","    ","@app.route('/edit_category/<category_id>')","def edit_category(category_id):","    return render_template('editcategory.html',","    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))","","","@app.route('/update_category/<category_id>', methods=['POST'])","def update_category(category_id):","    mongo.db.categories.update(","        {'_id': ObjectId(category_id)},","        {'category_name': request.form.get('category_name')})","    return redirect(url_for('get_categories'))","","","@app.route('/delete_category/<category_id>')","def delete_category(category_id):","    mongo.db.categories.remove({'_id': ObjectId(category_id)})","    return redirect(url_for('get_categories'))","","","@app.route('/insert_category', methods=['POST'])","def insert_category():","    categories = mongo.db.categories","    category_doc = {'category_name': request.form.get('category_name')}","    categories.insert_one(category_doc)","    return redirect(url_for('get_categories'))","    ","","@app.route('/new_category')","def new_category():","    return render_template('addcategory.html')","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","        port=int(os.environ.get('PORT')),","        debug=True)","    ",""]}]]},"ace":{"folds":[],"scrolltop":840,"scrollleft":0,"selection":{"start":{"row":105,"column":0},"end":{"row":105,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":51,"state":"start","mode":"ace/mode/python"}},"timestamp":1565373554805,"hash":"841371c35f239e37b1c91fd48ebe3c5522604a34"}