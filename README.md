FastAPI is being used, a framework for handling HTTP requests.

Studied about @app.get, and how each is a request to that specific URL, or a "request", as we call it, is sent when we visit that specific URL. Then, the function below it is called. We can use {} to fetch the values in the url.

PostGRES is using SQL commands. That is our primary database being used. Servers are stateless in their own python code.

I created a new folder named db, which has the connection file, which contains the connection function, being used in app.py, to connect to the PostGres. It is imported in the file at the top using the file name, and used as a route/decorator.


We use config.py to load the env variables at once, so that now we can use the config.py everywhere else, instead of directly using .env. 

import os is a way of talking to the OS, like files, folders, env files, etc. It helps load the env using load_dotenv(), only after which functions like os.getenv("DB_NAME") work.