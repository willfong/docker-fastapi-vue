DROP TABLE IF EXISTS messages;
CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    created_at TEXT,
    users_id INT,
    message TEXT
);

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    oauth TEXT,
    admin BOOLEAN,
    name TEXT,
    last_login TEXT,
    UNIQUE(oauth)
);

