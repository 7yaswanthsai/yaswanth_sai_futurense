from flask import Flask # type: ignore
from flask_restful import Api, Resource # type: ignore
from flask_mysqldb import MySQL # type: ignore

app = Flask(__name__)
api = Api(app)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'yourusername'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB'] = 'yourdatabase'

mysql = MySQL(app)

class User(Resource):
    def get(self, user_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cur.fetchone()
        cur.close()
        if user:
            return {'id': user[0], 'name': user[1], 'email': user[2]}
        return {'message': 'User not found'}, 404

    def post(self):
        args = request.get_json() # type: ignore
        name = args['name']
        email = args['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        return {'message': 'User created'}, 201

api.add_resource(User, '/user/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
