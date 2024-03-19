"""Database Module."""

import sqlite3


class DatabaseManager:
    """Creating and closing database connections."""

    def __init__(self, database_filename) -> None:
        self.connection = sqlite3.connect(database_filename)

    def __del__(self):
        self.connection.close()

    def _execute(self, statement, values=None):
        """Execute SQL statements."""
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(statement, values or [])
            return cursor

    def create_table(self, table_name, columns):
        """Create SQL table.

        Parameters
        ----------
        table_name: str
            Database table name
        columns: Dict
            A dictionary of column names mapped to 
            their data types and constraints.
        """
        columns_with_types = [
            f"{column_name} {data_type}" for column_name, data_type in columns.items()]
        self._execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table_name}
            ({", ".join(columns_with_types)});
            """
        )

    def add_data(self, table_name, data):
        """Add data to SQL table.

        Parameters
        ----------
        table_name
            Database table name
        data
            A dictionary that maps column
            names to column values.
        Returns
        -------
        Query
        """
        placeholders = ", ".join("?" * len(data))
        column_names = ", ".join(data.keys())
        column_values = tuple(data.values())
        print(column_values)
        self._execute(
            f"""
            INSERT INTO {table_name}
            ({column_names})
            VALUES ({placeholders});
            """,
            column_values
        )

    def delete(self, table_name, criteria):
        """Delete data from SQL table.

        Parameters
        ----------
        table_name
            Table name to delete record from.
        criteria
            A dictionary mapping column names 
            to the value to match on.

        """
        placeholder = [f"{column} = ?" for column in criteria.keys()]
        delete_criteria = " AND ".join(placeholder)
        self._execute(
            f"""
            DELETE FROM {table_name}
            WHERE {delete_criteria};
            """,
            tuple(criteria.values()),
        )

    def select(self, table_name, criteria=None, order_by=None):
        """Select data SQL table."""
        criteria = criteria or {}

        query = f"SELECT * FROM {table_name}"
        if criteria:
            placeholder = [f"{column} =?" for column in criteria.keys()]
            select_criteria = " AND ".join(placeholder)
            query += f" WHERE {select_criteria}"

        if order_by:
            query += f" ORDER BY {order_by}"
        return self._execute(
            query,
            tuple(criteria.values())
        )
