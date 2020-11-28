DROP TABLE IF EXISTS fixtures;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS teams;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    player_info VARCHAR(255),
    games_played INT
);

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    team_name VARCHAR(255),
    location VARCHAR(255),
    stadium_name VARCHAR(255),
    stadium_capacity INT,
    fixtures_played INT,
    fixtures_won INT,
    fixtures_drawn INT,
    fixtures_lost INT,
    points INT,
    player_id INT REFERENCES players(id)
);

CREATE TABLE fixtures (
    id SERIAL PRIMARY KEY,
    team1_id SERIAL REFERENCES teams(id),
    team2_id SERIAL REFERENCES teams(id)
);