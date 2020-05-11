import uuid
from datetime import datetime
from ..services import util, sqlite

def add(users_id, message_text):
    query = "INSERT INTO messages (created_at, users_id, message) VALUES (?,?,?)"
    params = (datetime.utcnow().isoformat(), users_id, message_text)
    if sqlite.write(query, params):
        return True
    return False

def all():
    query = "SELECT m.id, m.created_at, m.message, u.name FROM messages AS m INNER JOIN users AS u ON m.users_id = u.id ORDER BY m.created_at DESC"
    return sqlite.read(query)
