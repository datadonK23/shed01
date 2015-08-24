CREATE TABLE ratings (
	user_id SERIAL PRIMARY KEY,
	rated_at TIMESTAMP DEFAULT current_timestamp,
	rat_book_01 INTEGER,
	rat_book_02 INTEGER,
	rat_book_03 INTEGER,
	rat_book_04 INTEGER,
	rat_book_05 INTEGER,
	rat_book_06 INTEGER,
	rat_book_07 INTEGER,
	rat_book_08 INTEGER,
	rat_book_09 INTEGER,
	rat_book_10 INTEGER,
	rat_book_11 INTEGER,
	rat_book_12 INTEGER,
	rat_book_13 INTEGER,
	rat_book_14 INTEGER,
	rat_book_15 INTEGER
	);

CREATE TABLE books (
	book_id INTEGER NOT NULL PRIMARY KEY,
	title VARCHAR
	);
	