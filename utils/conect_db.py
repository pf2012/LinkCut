import sqlite3


def save_link(url,user_secret_key,short_url):
    conn = sqlite3.connect('linkcut.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
        url_original TEXT,
        url_curta TEXT,
        user_secret_key TEXT,
        qtd_acessos INTEGER DEFAULT 0,
        ultimo_acesso TIMESTAMP,
        UNIQUE(url_curta)            
    )
    """)
    conn.commit()
    cursor.execute("""
    INSERT OR IGNORE INTO links (url_original, url_curta, user_secret_key)
    VALUES (?, ?, ?)
    """, (url, short_url, user_secret_key))
    conn.commit()
    conn.close()



def get_original_url(c):
    conn = sqlite3.connect('linkcut.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT url_original FROM links where url_curta = ?
    """, (c,))
    result = cursor.fetchone()[0]
    if result:
        cursor.execute("""
        UPDATE links SET qtd_acessos = qtd_acessos + 1, ultimo_acesso = CURRENT_TIMESTAMP WHERE url_curta = ?
        """, (c,))
        conn.commit()
        conn.close()
        return result
    conn.close()
    return None



def get_statistics(links, user_secret_key=''):
    conn = sqlite3.connect('linkcut.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT url_original, url_curta, created_at, qtd_acessos, ultimo_acesso FROM links
    WHERE user_secret_key = ? and url_original IN ({})
    """.format(','.join('?' for _ in links)), [user_secret_key] + links)
    result = cursor.fetchall()
    conn.close()
    return result


def get_access_count(c,user_secret_key):
    conn = sqlite3.connect('linkcut.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT url_original, qtd_acessos, ultimo_acesso  FROM links WHERE url_curta = ? and user_secret_key = ?
    """, (c,user_secret_key,))
    result = cursor.fetchone()
    conn.close()
    return result
