import sys
import sqlite3
from sqlite3 import Error
import custom_exceptions as exc
from sql_statements import SQLStatements as sql

class DatabaseWrapper:
    def __init__(self, config):
        self._config = config

        self._debug = self._config["debug"]
        self._conn = self._create_connection()

        if type(self._debug) != bool:
            self._conn.close()
            raise exc.IncorrectConfig("debug")
        

    def _log(self, message):
        '''
        Generic logging function
        '''
        if self._DEBUG:
            print(message)


    def cur_wrapper(self, func, commit=False):
        def inner(self, *args, **kwargs):
            cur = self._conn.cursor()
            func(self, cur, *args, **kwargs)

            if commit:
                self._conn.commit()

        return inner

    

    def _create_connection(self):
        '''
        Creates and return a database
        connection object
        '''
        try:
            conn = sqlite3.connect(self._config["db"]["file_name"])
            self._log(f"Connected to database. Sqlite3 ver: {sqlite3.version}")
            
            return conn
        except Error as e:
            self._log(e)
            self._conn.close()
            sys.exit("Fatal Error Has occured. Execution cannot continue")


    @cur_wrapper(commit=True)
    def add_host(self, cur, hostname, name=None, description=None):
        cur.execute(sql.add_host, (hostname, name, description,))

        


    def create_vlan(self, vlan_id, ip_start, ip_end, netmask, name=None):
        pass


    def add_address(self, address, netmask, host_id, description=None):
        pass