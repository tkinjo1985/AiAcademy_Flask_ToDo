DROP TABLE IF EXISTS todo;

CREATE TABLE todo (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_content TEXT(200) NOT NULL,
    done_flag INTEGER(10) DEFAULT 0,
    created_at TEXT
);
