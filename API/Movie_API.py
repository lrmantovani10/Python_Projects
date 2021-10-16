import  os, uuid
from flask import Flask, request, session, redirect, url_for
from base64 import b64encode
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy as SQL
from werkzeug.security import generate_password_hash, check_password_hash

# Setting up the app

load_dotenv()
flask_mode = os.getenv('FLASK_ENV')
app_file = os.getenv('FLASK_APP')
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = 'easy_password'

db = SQL(app)

# Building the API

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    description = db.Column(db.String(300), unique = False, nullable = False)
    strengths = db.Column(db.String(150), unique = False, nullable = False)

    def __repr__(self):
        return "{name}, {id}".format(name = self.name, id = self.id)

class Users(db.Model):
     id = db.Column(db.String, primary_key=True)
     name = db.Column(db.String)
     password = db.Column(db.String)
     api_key = db.Column(db.String)

     def __repr__(self):
        return "{name}, {id}".format(name = self.name, id = self.id)

###### Handling the user

# Create/Update User - Must provide user name and password

@app.route('/update_user', methods = ['POST', 'PATCH'])
def update_user():
    input_data = request.get_json() 
    api_key = request.headers.get('api_key')
    try: 
        user = Users.query.filter_by(name=input_data['name']).first()
        hashed_password = generate_password_hash(input_data['password'], method='sha256')
        random_key = os.urandom(32)
        decoded_key = b64encode(random_key).decode('utf-8')

        if 'user_logged' in session and api_key == user.api_key and user is not None and request.method == "PATCH":
            Users(id = user.id, name = input_data['name'], password = hashed_password) 
            return "User information updated successfully!", 202
        
        elif 'user_logged' in session and api_key != user.api_key and request.method == "PATCH":
            if api_key == None:
                return "Please provide an API key!"
            return "Please provide a valid API key!"
        
        elif 'user_logged' not in session and request.method == "PATCH":
            return "Please log in first!"
        
        elif user is None and request.method == "PATCH":
            return "User cannot be updated because it wasn't found in the database", 409
        
        elif request.method == "POST" and user is None:
            new_user = Users(id=str(uuid.uuid4()), name = input_data['name'], password = hashed_password, api_key = decoded_key)
            db.session.add(new_user)  
            db.session.commit()    
            session['user_logged'] = True
            session['api_key'] = new_user.api_key
            session['username'] = new_user.name

            # User will always be logged as unless they log out
            session.permanent = True
            return 'User registered successfully! Use this API key for future requests: {}'.format(decoded_key)
        elif request.method == "POST" and user is not None:
            return 'User already exists!', 409
    
    except KeyError as missing_key:
        if missing_key == "api_key":
            return f"Request header missing API key!", 400
        else:
            return f"Request body missing parameter {missing_key}", 400


# Login User

@app.route('/login_user')  
def login_user(): 
    api_key = request.headers.get('api_key')
    if 'user_logged' in session:
        return "You are already logged in", 400
    else:
        try:
            auth = request.authorization
            if auth is None:
                return "Request missing authorization header!", 400
        except:
            return "Request missing authorization header!", 400
        try:
            provided_username = auth.username
            provided_password = auth.password
        except KeyError as missing_key:
            return "User authentication is missing {} key".format(missing_key), 401
        except:
            return str(auth)
        user = Users.query.filter_by(name = provided_username).first()   
        if user is not None:
            if check_password_hash(user.password, provided_password) and api_key == user.api_key:  
                session['user_logged'] = True
                session['username'] = user.name
                session['api_key'] = user.api_key
                session.permanent = True
                return redirect(url_for('index')), 302
            else:
                return "Please provide a valid api key and password", 401

        else:
            return "User doesn't exist with credentials provided in the authroization header. Please create it first!", 404

# Logout User

@app.route('/logout_user')  
def logout_user(): 
    if 'user_logged' in session:
        session.clear()
        return "Successfully logged out!", 200
    else:
        return "You are not even logged in!", 400

# Delete User

@app.route('/delete_user', methods=['DELETE'])  
def delete_user(): 
    if 'user_logged' in session:
        specified_user = Users.query.filter_by(name = session['username']).first()
        if session['api_key'] == specified_user.api_key:
            db.session.delete(specified_user)
            db.session.commit()
            session.clear()
            return "Successfully deleted user!", 204
        else:
            return "A wrong API key was used in the login process. Please try again!", 401
    else:
        return "You must be logged in to perform this action!", 400

######

###### Handling the characters

#  Gives all movie characters

@app.route('/get_characters')
def index():
    if 'user_logged' in session and Users.query.filter_by(name = session['username'], api_key = session['api_key']).first() != None:
        all_characters = Character.query.all()
        total_characters = []
        for character in all_characters:
            personal_data = {'name':character.name, 'bio': character.description, 'strengths': character.strengths}
            total_characters.append(personal_data)
        return {'characters':total_characters}, 200
    else:
        return "Please log in with the user first!", 401

#  Gives movie character based on id provided
@app.route('/get_characters/<id>')
def get_character(id):
    if 'user_logged' in session and Users.query.filter_by(name = session['username'], api_key = session['api_key']).first() != None:
        selected_character = Character.query.get_or_404(id)
        return {'name':selected_character.name, 'bio':selected_character.description, 'strengths':selected_character.strengths}
    else:
        return "Please log in with the user first!", 401

# Creates ("POST") character based on body provided 
@app.route('/create_character', methods=['POST'])
def add_character():
    if 'user_logged' in session and Users.query.filter_by(name = session['username'], api_key = session['api_key']).first() != None:
        try:
            created_character = Character(name=request.json['name'], description = request.json['description'], strengths = request.json['strengths'])
        except Exception as exception:
            return f"Request body missing parameter {exception}"
        db.session.add(created_character)
        db.session.commit()
        return 'Successfully created character! {}'.format(created_character.name), 201
    else:
        return "Please log in with the user first!", 401

# Edits ("PATCH") character based on body provided 
@app.route('/edit_character/<id>', methods=['PATCH'])
def edit_character(id):
    if 'user_logged' in session and Users.query.filter_by(name = session['username'], api_key = session['api_key']).first() != None:
        try:
            edit_character = Character.query.filter_by(id=id).first()
            edit_character.name = request.json['name']
            edit_character.description = request.json['description']
            edit_character.strengths = request.json['strengths']
        except KeyError as missing_key:
            return f"Request body missing parameter {missing_key}", 400
        db.session.commit()
        return 'Successfully updated character with id {}!'.format(edit_character.id), 200
    else:
        return "Please log in with the user first!", 401

# Deletes a character based on id provided 
@app.route('/delete_character/<id>', methods=['DELETE'])
def remove_character(id):
    if 'user_logged' in session and Users.query.filter_by(name = session['username'], api_key = session['api_key']).first() != None:
        specified_character = Character.query.get(id)
        if specified_character == None:
            return 'Character not found in database!', 404
        db.session.delete(specified_character)
        db.session.commit()
        return 'Successfully deleted character with id {}'.format(specified_character.id), 204
    else:
        return "Please log in with the user first!", 401

# Use session key to login as a certain character in the database
@app.route('/login_as_character/<id>')
def login_character(id):
    if 'user_logged' in session and Users.query.filter_by(name = session['username'], api_key = session['api_key']).first() != None:
        if 'character_id' not in session and 'character_name' not in session:
            found_character = Character.query.filter_by(id=id).first()
            session['character_id'] = found_character.id
            session['character_name'] = found_character.name
        else:
            return redirect(url_for('show_character')), 302
        return f"Set character to {session['character_name']}!", 200
    else:
        return "Please log in with the user first!", 401

# Logout as a certain character in the database and then go to page showing all characters in db
@app.route('/logout_as_character')
def logout_character():
    if 'user_logged' in session and Users.query.filter_by(name = session['username'], api_key = session['api_key']).first() != None:
        if 'character_id' in session and 'character_name' in session:
            session.pop('character_id', None)
            session.pop('character_name', None)
        return redirect(url_for('index'))
    else:
        return "Please log in with the user first!", 401

# Show information for character user is logged in as. If it fails, redirect user to page showing all characters
@app.route('/show_character_info')
def show_character():
    if 'user_logged' in session and Users.query.filter_by(name = session['username'], api_key = session['api_key']).first() != None:
        if 'character_id' in session and 'character_name' in session:
            return f"You have selected character {session['character_name']} with id {session['character_id']}"
        else:
            return redirect(url_for('index'))
    else:
        return "Please log in with the user first!", 401

######


# Starting the server
if __name__ == '__main__':
    app.run(debug=True)
