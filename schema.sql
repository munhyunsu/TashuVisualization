DROP TABLE IF EXISTS entries;
CREATE TABLE station (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    location TEXT NOT NULL
);

CREATE TABLE transaction (
    timestamp INTEGER NOT NULL,
    src INTEGER NOT NULL,
    dst INTEGER NOT NULL
);
