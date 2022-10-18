## To start the API server locally, run the following command (main is the py file):
- flask --app main --debug run

## Dependencies:
- pip install -U Flask
- pip install flask-restful
    
## You'll need to create a db_connections.py file to connect to your local mySQL DB
- Here's the connections code:
db = mysql.connector.connect(
        host="localhost",
        user="your user",
        password="your password",
        database="marketplace"
    )
