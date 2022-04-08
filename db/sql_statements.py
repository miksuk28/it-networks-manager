class SQLStatements:
    add_host = '''
        INSERT INTO hosts (hostname, name, description)
        VALUES (?,?,?)
    '''