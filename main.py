from fastapi import FastAPI

class Apple():
    pass

apples = []

app = FastAPI()

@app.get('/apples/')
def hello(id,all):
    return str(apples)

@app.post('/apples/')
def hi():
    new_apple = Apple()
    apples.append(new_apple)
    return str(new_apple)

@app.delete('/apple/{id}')
def delete(id):
    del apples[int(id)]