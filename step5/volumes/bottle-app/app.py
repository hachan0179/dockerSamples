# INPORT LIBRALY##########################################
import bottle
import peewee
import time

# WEB APP CONFIG #########################################
PORT = 80
HOST = '0.0.0.0'
DEBUG = True
RELOADER = True

# DB CONFIG ##############################################
DB_HOST = 'mysql-db'
DB_PORT = 3306
DB_USER = 'root'
DB_PASS = 'mysql'
DB_SCHEMA = 'sample'
DB_TABLE = 'User'

# wait 60sec until mysql server is up
time.sleep(60)

# 
app = bottle.Bottle()
db = peewee.MySQLDatabase(database=DB_SCHEMA,host=DB_HOST,port=DB_PORT,user=DB_USER,password=DB_PASS)

# MODEL #####################################################
class User(peewee.Model):
    id=peewee.PrimaryKeyField()
    username=peewee.TextField()
    password=peewee.TextField()
    class Meta:
        database=db
        db_table=DB_TABLE

db.connect()
db.create_tables([User])
newuser = User.create(username='hachan',password='th1s_1s_s3cr3t')
newuser.save()


# CONTROLER ################################################
@app.route('/')
def index():
    return '''
        <h1>[Step3] Hello,World!</h1>    
    '''

@app.route('/show/<username>')
def show(username):
    try:
        user = User.get(User.username==username)
    except:
        return f'''
            <p>{username} is not exist</p>
        '''

    return f'''
        <p>{username}'s password is {user.password}</p>
    '''

# RUN ########################################3
if(__name__=='__main__'):
    app.run(host=HOST,port=PORT,debug=DEBUG,reloader=RELOADER)