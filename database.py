from dotenv import load_dotenv
import os
from psycopg2 import connect, OperationalError


class DatabaseManager:
    def __init__(self):
        load_dotenv()
        self.connection = None
        self.create_connection()

    def create_connection(self):
        try:
            connection = connect(os.getenv('DATABASE_URL'), sslmode='require')
            self.connection = connection
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print(f"The error '{e}' occurred")

    def close_connection(self, debug=True):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
            if debug:
                print("Database connection closed.")

    def execute_query(self, query):
        if self.connection is not None:
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            try:
                cursor.execute(query)
                print("Query executed successfully")
            except OperationalError as e:
                print(f"The error '{e}' occurred")
            finally:
                cursor.close()

    def get_corpus_count(self):
        if self.connection is not None:
            cursor = self.connection.cursor()
            try:
                cursor.execute("SELECT COUNT(*) FROM corpuses")
                count = cursor.fetchone()
                return count[0]
            except OperationalError as e:
                print(f"The error '{e}' occurred")

    def get_latest_100_platforms(self):
        if self.connection is not None:
            cursor = self.connection.cursor()
            try:
                cursor.execute("""
                    SELECT data->>'platform' AS platform
                    FROM corpuses
                    ORDER BY id DESC
                    LIMIT 100
                """)
                platforms = cursor.fetchall()
                return [platform[0] for platform in platforms]
            except OperationalError as e:
                print(f"The error '{e}' occurred")


