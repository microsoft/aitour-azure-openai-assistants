import json
import sqlite3
import pandas as pd
from pydantic import BaseModel

DATA_BASE = "database/contoso-sales.db"


class QueryResults(BaseModel):
    display_format: str = ""
    json_format: str = ""


class SalesData:
    def __init__(self) -> None:
        self.conn = None

    def connect(self) -> None:
        """Establish a connection to the SQLite database."""
        try:
            self.conn = sqlite3.connect(DATA_BASE, uri=True)
            print("Database connection opened.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def close(self) -> None:
        """Close the SQLite database connection."""
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

    def _fetch_single_column(self, query: str) -> list:
        """Execute a query and return results from a single column as a list."""
        if self.conn is None:
            raise ConnectionError(
                "Database connection is not established. Call connect() first.")

        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            return [row[0] for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"An error occurred while executing query: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def get_table_names(self) -> list:
        """Return a list of table names."""
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';"
        return self._fetch_single_column(query)

    def get_column_info(self, table_name: str) -> list:
        """Return a list of column names and their types for a given table."""
        if self.conn is None:
            raise ConnectionError(
                "Database connection is not established. Call connect() first.")

        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"PRAGMA table_info('{table_name}');")
            return [f"{col[1]}: {col[2]}" for col in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"An error occurred while fetching column info: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def get_unique_values(self, column: str, table: str) -> list:
        """Return a list of unique values from a specific column in a table."""
        query = f"SELECT DISTINCT {column} FROM {table};"
        return self._fetch_single_column(query)

    def get_database_info(self) -> str:
        """Return a string summarizing the database schema and common fields."""
        try:
            tables = self.get_table_names()
            table_info = [
                f"Table {table}: Columns: {', '.join(self.get_column_info(table))}"
                for table in tables
            ]

            regions = self.get_unique_values("region", "sales_data")
            product_types = self.get_unique_values(
                "product_type", "sales_data")
            product_categories = self.get_unique_values(
                "main_category", "sales_data")
            reporting_years = list(
                map(str, self.get_unique_values("year", "sales_data")))

            return "\n".join(
                table_info
                + [
                    f"Regions: {', '.join(regions)}",
                    f"Product Types: {', '.join(product_types)}",
                    f"Product Categories: {', '.join(product_categories)}",
                    f"Reporting Years: {', '.join(reporting_years)}",
                ]
            )
        except sqlite3.Error as e:
            return f"An error occurred while generating database info: {e}"

    def fetch_sales_data_using_sqlite_query(self, query: str) -> str:
        """
        Execute an SQL query and return results in display and JSON formats.
        :param query: The dynamic SQL query to execute
        :rtype: str
        """

        if self.conn is None:
            raise ConnectionError(
                "Database connection is not established. Call connect() first.")

        print(f"\nQuery: {query}\n")

        try:
            result = pd.read_sql_query(query, self.conn)
            if result.empty:
                return json.dumps({"sales_query": "The query returned no results. Try a different query."})
            return json.dumps({"sales_query": result.to_dict(orient="records")})
        except sqlite3.Error as e:
            # pass the error back to the model so it can reevaluate the query
            return json.dumps({"fetch_sales_data_using_sqlite_query error": str(e), "query": query})
