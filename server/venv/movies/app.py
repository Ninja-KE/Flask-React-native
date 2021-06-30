from flask import Flask, render_template, request, redirect, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

#configure sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)

#cross origin resource sharing
CORS(app)

#configure migrations
Migrate(app, db)

##marshmallow
ma = Marshmallow(app)

#create model movies
class Shows(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    category = db.Column(db.String(50))
    rating = db.Column(db.Integer)
    actor = db.Column(db.String(50))
    country = db.Column(db.String(60))

    def __repr__(self):
        return '<Shows %r>' % self.id

#marshmallow schema based on model Shows
class ShowsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Shows

#routes
@app.route('/')
def page():
    return render_template('index.html')

#add movies route
@app.route('/add', methods=['POST'])
def addMovies():
    if request.method == 'POST':
        #get form data from index.html
        title = request.form['title']
        category = request.form['category']
        rating = request.form['rating']
        actor = request.form['actor']
        country = request.form['country']

        new_data = Shows(title=title, category=category, rating=rating, actor=actor, country=country)

        #add to database
        try:
            db.session.add(new_data)
            db.session.commit()
            return redirect('/')
        except:
            return 'The tv show could not be added'

#fetch records
@app.route('/getData', methods=['GET'])
def movies():
    if request.method == 'GET':
        items = Shows.query.order_by(Shows.id).all()
        the_schema = ShowsSchema(many=True)
        shows = the_schema.dump(items)
        return jsonify({'shows' : shows})


#delete
@app.route('/delete')
def delete():
    try:
        db.session.query(Shows).delete()
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

