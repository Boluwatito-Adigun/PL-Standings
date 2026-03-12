CREATE DATABASE IF NOT EXISTS premier_league_db;

USE premier_league_db;

CREATE TABLE IF NOT EXISTS standings (
	season INT NOT NULL,
    position INT NOT NULL,
    team_id INT NOT NULL,
    team VARCHAR(100) NOT NULL,
    played INT NOT NULL,
    won INT NOT NULL,
    draw INT NOT NULL,
    lost INT NOT NULL,
    goals_for INT NOT NULL,
    goals_against INT NOT NULL,
    goals_diff INT NOT NULL,
    points INT NOT NULL,
    form VARCHAR(5) NOT NULL,
    PRIMARY KEY (season, team_id),
    UNIQUE KEY uniq_season_position (season, position)
);

