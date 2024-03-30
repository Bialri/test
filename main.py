from fastapi import FastAPI

class Apple():
    pass

apples = []

app = FastAPI()

@app.get('/')
def hello():
    return '<h1 style="color: red"></h1>'

@app.post('/apples/')
def hi():
    new_apple = Apple()
    apples.append(new_apple)
    return str(new_apple)

@app.delete('/apple/{id}')
def delete(id):
    del apples[int(id)]