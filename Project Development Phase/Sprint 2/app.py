from flask import Flask, render_template,request,session, redirect,url_for
import ibm_db

app = Flask(__name__)
app.secret_key='py@ibm22'


conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=mkm01183;PWD=mKT78oYehFXk50wj",'','')

print(conn)
print("connection successful...")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('account/login.html')

@app.route('/register', methods=['POST'])
def signup():
 if request.method == 'POST':
    try:
        sql = "INSERT INTO users VALUES('{}','{}','{}')".format(request.form["name"],request.form["email"],request.form["password"])
        ibm_db.exec_immediate(conn,sql)
        return render_template('account/login.html')
    except:
        return render_template('account/signup.html')
 else:
    return render_template('account/signup.html')
        # name = request.form['name']
         #email = request.form['email']
         #phone = request.form['phone']
         #password = request.form['password']
        
         #sql ="INSERT INTO users VALUES (?,?,?,?)"
         #stmt = ibm_db.prepare(conn,sql)
         #ibm_db.bind_param(stmt, 1, name)
         #ibm_db.bind_param(stmt, 2, email)
         #ibm_db.bind_param(stmt, 3, phone)
         #ibm_db.bind_param(stmt, 4, password)
         #ibm_db.execute(stmt)
   # return render_template('signup.html')


if __name__=='__main__':
    app.config['SESSION_TYPE']= 'filesystem'
    app.run(debug=True)
