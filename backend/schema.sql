DROP TABLE IF EXISTS user;
--DROP TABLE IF EXISTS recipe;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
    -- TODO: add column for user saved ingredients
);

-- TODO: create recipe table
