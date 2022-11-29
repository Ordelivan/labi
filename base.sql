id INTEGER NOT NULL PRIMARY KEY,
    surname VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE organizing committee(
    id INTEGER NOT NULL PRIMARY KEY,
    conferenceid INTEGER NOT NULL,
    name VARCHAR(100)
);

CREATE TABLE conference(
    id INTEGER NOT NULL PRIMARY KEY,   
    name INTEGER NOT NULL,
    place INTEGER NOT NULL,
    date INTEGER NOT NULL,
    speakerid INTEGER NOT NULL
);