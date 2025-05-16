from sqlite3 import connect, Error
from pathlib import Path
from functools import wraps
import pandas as pd

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
#### YOUR CODE HERE
# db_path = Path('python-package/employee_events/employee_events.db')
ROOT_DIR = Path(__file__).resolve().parent.parent  
db_path = ROOT_DIR / 'employee_events/employee_events.db'
# print(db_path.resolve())

# OPTION 1: MIXIN
# Define a class called `QueryMixin`
# class QueryMixin:
    
    # Define a method named `pandas_query`
    # that receives an sql query as a string
    # and returns the query's result
    # as a pandas dataframe
    #### YOUR CODE HERE
    # def pandas_query(self, sqlquery):
    #     return()


    # Define a method named `query`
    # that receives an sql_query as a string
    # and returns the query's result as
    # a list of tuples. (You will need
    # to use an sqlite3 cursor)
    #### YOUR CODE HERE
    

 
 # Leave this code unchanged
def query(func):
    """
    Decorator that runs a standard sql execution
    and returns a list of tuples
    """

    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        # connection = connect(db_path)

        #Open a connection to database
        connection = connect(db_path)
        cursor = connection.cursor()

        # Add try and except conditions for error handling
        try:
            result = cursor.execute(query_string).fetchall()
            return result
        except Error as e:
            print(f"Error occurred: {e}")
        finally:
            # Close cursor and connection
            cursor.close()
            connection.close()
    
    return run_query

## TEST AREA BELOW

# test usage
# @query
# def testfunc():
#     return "SELECT (first_name||' '||last_name), employee_id FROM employee"

# testresult = pd.DataFrame(testfunc())

# print(testresult)
