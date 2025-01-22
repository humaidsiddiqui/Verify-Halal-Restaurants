from flask import Flask, render_template , request , redirect , url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/flaskdb?client_encoding=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class flaskdb(db.Model): #creating schema fro your table in postgresql 
    __tablename__ = 'flaskdb'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone= db.Column(db.String(100), nullable=False)
    restaurant_name= db.Column(db.String(100), nullable=False)
    restaurant_address= db.Column(db.String(100), nullable=False)
    choice = db.Column(db.String(50), nullable=False)
    comments= db.Column(db.String(100), nullable=False)
    def __init__(self,name,email,phone,restaurant_name,restaurant_address,choice,comments): #taking inputs from the user using __init__ method 
        self.name = name
        self.email = email
        self.phone = phone
        self.restaurant_name = restaurant_name
        self.restaurant_address = restaurant_address
        self.choice = choice
        self.comments = comments

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST': #storing the data taken from user to in your postgresql coloumns
        print("Received form data ",request.form)
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        restaurant_name = request.form['restaurant_name']
        restaurant_address = request.form['restaurant_address']
        choice= request.form.get('choice','Not Provided') #default in no selection
        comments = request.form['comments']

        print(f"Received and Inserting: {name}, {email}, {phone}, {restaurant_name}, {restaurant_address}, {choice}, {comments}")

        
        data = flaskdb(name=name,email=email,phone=phone,restaurant_name=restaurant_name,restaurant_address=restaurant_address,choice=choice,comments=comments)
        db.session.add(data)
        db.session.commit()
        print('Data Inserted Successfully!')

        # fetch data using postgresql
        fetch=db.session.query(flaskdb)
        for f in fetch:
            print(f.name) #printing the name of the user as the acknowldgement.

        # return render_template('success.html', data=name)
    


if __name__=="__main__":
    app.run(debug=True)
    with app.app_context():
        db.create_all()
        app.run(debug=True)