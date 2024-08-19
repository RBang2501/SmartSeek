import mysql.connector
from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from config import Config

# Database connection setup
def get_db_connection() -> MySQLConnection:
    config = Config()
    db_conf = {
        "host": config.tidb_host,
        "port": config.tidb_port,
        "user": config.tidb_user,
        "password": config.tidb_password,
        "database": config.tidb_db_name,
        "autocommit": True,
        "use_pure": True
    }
    
    if config.ca_path:
        db_conf["ssl_verify_cert"] = True
        db_conf["ssl_verify_identity"] = True
        db_conf["ssl_ca"] = config.ca_path
    
    return mysql.connector.connect(**db_conf)

# Read all directories
def read_all_directories() -> None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM directories')
    directories = cursor.fetchall()
    for directory in directories:
        print(f"Directory ID: {directory['id']}, Path: {directory['path']}")
    conn.close()

# Read all files
def read_all_files() -> None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM files')
    files = cursor.fetchall()
    for file in files:
        print(f"File ID: {file['id']}, Path: {file['path']}, Type: {file['type_id']}, Caption: {file['caption']}, OCR Text: {file['ocr_text'][0:10]}..., Directory ID: {file['directory_id']}")
    conn.close()

# Read all embeddings
def read_all_embeddings() -> None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM embeddings')
    embeddings = cursor.fetchall()
    for embedding in embeddings:
        print(f"Embedding ID: {embedding['id']}, File ID: {embedding['file_id']}, Embedding Type: {embedding['embedding_type']}, Embedding Data: {embedding['embedding_data']}")
    conn.close()

if __name__ == "__main__":
    # Read data from all tables
    read_all_directories()
    read_all_files()
    read_all_embeddings()
