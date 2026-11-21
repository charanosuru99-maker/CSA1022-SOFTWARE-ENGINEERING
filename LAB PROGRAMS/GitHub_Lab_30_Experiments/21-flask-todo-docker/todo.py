from flask import Flask, request, jsonify
app=Flask(__name__); tasks=[]
@app.get('/health')
def health(): return jsonify(status='ok')
@app.get('/tasks')
def get_tasks(): return jsonify(tasks)
@app.post('/tasks')
def add_task():
    data=request.get_json(force=True); tasks.append(data.get('task','')); return jsonify(tasks=tasks),201
if __name__=='__main__': app.run(host='0.0.0.0',port=5000)
