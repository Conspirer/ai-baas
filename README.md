FastAPI is being used, a framework for handling HTTP requests.

Studied about @app.get, and how each is a request to that specific URL, or a "request", as we call it, is sent when we visit that specific URL. Then, the function below it is called. We can use {} to fetch the values in the url.

PostGRES is using SQL commands. That is our primary database being used. Servers are stateless in their own python code. The driver being used to talk to DB is psycopg2.

I created a new folder named db, which has the connection file, which contains the connection function, being used in app.py, to connect to the PostGres. It is imported in the file at the top using the file name, and used as a route/decorator.


We use config.py to load the env variables at once, so that now we can use the config.py everywhere else, instead of directly using .env. 

import os is a way of talking to the OS, like files, folders, env files, etc. It helps load the env using load_dotenv(), only after which functions like os.getenv("DB_NAME") work.

We useSQLAlchemy to manage database connections. We use a database connection string in the engine.py file to address the DB. The engine creates a pool of connections. 

We're use ORM of SQLAlchemy to map the database tables to python classes. Create the base.py to use models, which are just python classes that represent data. Great for coding and using python instead of SQL. ORM is the middle translator. Declarative base creates a registry, tracking the information of the db. Base makes the python function understand it is to use the database.

Sessions allow for a workspace for db operations. sessionmaker is a blueprint for making sessions.