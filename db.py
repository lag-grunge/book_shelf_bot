import sqlite3

def init_db():
    with sqlite3.connect('core.db') as c:
        cr = c.cursor()
        try:
            cr.execute('''
                        CREATE TABLE books (
                            id INT PRIMARY KEY,
                            raw_str VARCHAR,
                            user_id INT,
                        )
                        ''')
        except sqlite3.OperationalError:
            pass

def print_db():
    with sqlite3.connect('core.db') as c:
        cr = c.cursor()
        cr.execute('''
                    SELECT * FROM sqlite_master
                    ''')
        for row in cr:
            print(row)

def print_books():
    with sqlite3.connect('core.db') as c:
        cr = c.cursor()
        cr.execute('''
                    SELECT * FROM books
                    ''')
        for row in cr:
            print(row)

if __name__ == '__main__':
    # init_db()
    # print_db()
    print_books()