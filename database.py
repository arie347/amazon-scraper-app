import sqlite3
import os
from datetime import datetime

DB_NAME = "scraper_app.db"

def init_db():
    """Initialize the database with the files table"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            original_filename TEXT NOT NULL,
            upload_date TEXT NOT NULL,
            status TEXT DEFAULT 'Ready', -- Ready, Running, Completed, Failed
            last_scraped TEXT,
            result_filename TEXT,
            progress_current INTEGER DEFAULT 0,
            progress_total INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_file(filename, original_filename):
    """Add a new file to the database"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    upload_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute('INSERT INTO files (filename, original_filename, upload_date) VALUES (?, ?, ?)',
              (filename, original_filename, upload_date))
    file_id = c.lastrowid
    conn.commit()
    conn.close()
    return file_id

def get_all_files():
    """Get all files from the database"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM files ORDER BY upload_date DESC')
    files = [dict(row) for row in c.fetchall()]
    conn.close()
    return files

def get_file(file_id):
    """Get a specific file by ID"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM files WHERE id = ?', (file_id,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None

def update_status(file_id, status, result_filename=None):
    """Update the status of a file"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    last_scraped = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if result_filename:
        c.execute('UPDATE files SET status = ?, last_scraped = ?, result_filename = ? WHERE id = ?',
                  (status, last_scraped, result_filename, file_id))
    else:
        c.execute('UPDATE files SET status = ?, last_scraped = ? WHERE id = ?',
                  (status, last_scraped, file_id))
    
    conn.commit()
    conn.close()

def update_progress(file_id, current, total):
    """Update the progress of a scraping task"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('UPDATE files SET progress_current = ?, progress_total = ? WHERE id = ?',
              (current, total, file_id))
    conn.commit()
    conn.close()

def delete_file(file_id):
    """Delete a file from the database"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM files WHERE id = ?', (file_id,))
    conn.commit()
    conn.close()
