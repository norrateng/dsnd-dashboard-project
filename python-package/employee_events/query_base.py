# Import any dependencies needed to execute sql queries

from .sql_execution import QueryMixin

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.


class QueryBase(QueryMixin):

    # Create a class attribute called `name`
    # set the attribute to an empty string

    def __init__(self, name):
        self.name = name

    # Define a `names` method that receives
    # no passed arguments

    def names(self):

        # Return an empty list

        return []

    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe

    def event_counts(self, id):
        return self.pandas_query(
            # QUERY 1
            # Write an SQL query that groups by `event_date`
            # and sums the number of positive and negative events
            # Use f-string formatting to set the FROM {table}
            # to the `name` class attribute
            # Use f-string formatting to set the name
            # of id columns used for joining
            # order by the event_date column
            f"""select event_date,
            sum(positive_events) as positive_events,
            sum(negative_events) as negative_events
            from employee_events
            where {self.name}_id = {id}
            group by event_date
            order by event_date
            """
        )

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe

    def notes(self, id):
        return self.pandas_query(
            # QUERY 2
            # Write an SQL query that returns `note_date`, and `note`
            # from the `notes` table
            # Set the joined table names and id columns
            # with f-string formatting
            # so the query returns the notes
            # for the table name in the `name` class attribute
            f"""select a.note_date, a.note
            from notes as a
            left join {self.name} as b
              on a.{self.name}_id = b.{self.name}_id
            where a.{self.name}_id = {id}
            """
        )
