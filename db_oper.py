import sqlite3


def open_db():
    conn = sqlite3.connect('results.db')
    c = conn.cursor()

    query = '''
    CREATE TABLE IF NOT EXISTS data (
        tir_nr INTEGER (3) NOT NULL ON CONFLICT ABORT,
        f1     INTEGER (2),
        f2     INTEGER (2),
        f3     INTEGER (2),
        f4     INTEGER (2),
        f5     INTEGER (2),
        a1     INTEGER (2),
        a2     INTEGER (2) 
    );
    '''

    c.execute(query)
    conn.commit()
    conn.close()
    return

def data_set(fibo=False):

    import sqlite3
    conn = sqlite3.connect("results.db")
    c = conn.cursor()

    with conn:
        if fibo:
            lst = list(c.execute('select * from  data where rowid in (1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232, 376, 609)'))
        else:
            lst = list(c.execute('select * from  data'))

    conn.commit()
    conn.close()

    return lst


def fill_db(arr, len):
    import sqlite3
    #
    conn = sqlite3.connect("results.db")
    c = conn.cursor()

    c.execute("DELETE from data")

    with conn:
        for i in range(len):
            c.execute("INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?, ?)", arr[i])

    conn.commit()
    conn.close()

    return