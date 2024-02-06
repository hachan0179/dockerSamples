import bottle

# CONFIG

PORT = 80
HOST = '0.0.0.0'
DEBUG = True
RELOADER = True

app = bottle.Bottle()

@app.route('/')
def index():
    return '''
        <h1>Hello,World!</h1>    
    '''

if(__name__=='__main__'):
    app.run(host=HOST,port=PORT,debug=DEBUG,reloader=RELOADER)