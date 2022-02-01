import sys
import sqlite3
from schemas import sql_exp
from sqlite3 import Error


class DatabaseWrapper:
    def __init__(self, config):
        self._config = config
        self._DEBUG = bool(self._config["debug"])
        self._conn = self._create_connection()


    def _log(self, message):
        '''
        Generic logging function
        '''
        if self._DEBUG:
            print(message)
        else:
            pass

    
    def _create_connection(self):
        '''
        Creates and return a database
        connection object
        '''
        conn = None

        try:
            conn = sqlite3.connect(self._config["db"]["file_name"])
            self._log(f"Connected to database. Sqlite3 ver: {sqlite3.version}")
            return conn
        except Error as e:
            self._log(e)
            sys.exit("Fatal Error Has occured. Execution cannot continue")


    def _create_database(self):
        '''
        Creates required tables
        in database
        '''
        try:
            # Create cursor
            c = self._conn.cursor()

            c.execute(sql_exp["create_vlans_table"])
            c.execute(sql_exp["create_hosts_table"])
            c.execute(sql_exp["create_addresses_table"])
        
        except Error as e:
            self._log(e)
            sys.exit("Fatal Error Has occured. Execution cannot continue")
