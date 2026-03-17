# Premier League Standings -ETL Pipeline

## Project Overview

A busy sports bar in London hosts live football matches every week. While the main screen shows the match, fans often want to quickly check the current Premier League standings after each game.

Instead of manually searching for the standings, the bar wanted a second screen displaying the live league table, along with smaller table-top displays and tablets around the venue.

This project solves that problem by building a data pipeline that automatically pulls Premier League standings from a REST API, processes the data with Python, and stores it in a MySQL database so it can be displayed on screens across the bar.

The goal is to ensure fans can instantly see updated league rankings after every match.

## Business Problem

Fans frequently ask staff for the latest Premier League standings after matches. Manually checking or searching for standings during busy match nights slows down service and disrupts the fan experience.

The bar needed a simple automated system that retrieves and displays the latest league standings across multiple screens.

## Success Metric

The project is successful if:

- The latest Premier League standings are automatically fetched from an API.

- The data is cleaned and structured for reliable display.

- The standings are stored in a relational database.

- The data can be displayed on secondary screens and tablets across the bar.

- The key metric is data freshness — ensuring standings are updated immediately after games.


## Project Architecture

The pipeline follows a standard ETL workflow:

Extract → Transform → Load

REST API → Python Script → Pandas DataFrame → MySQL Database → Display Screens

## Tech Stack

- Python

- Pandas

- Requests

- MySQL

- MySQL Connector

- dotenv

- VS Code


## Project Workflow

### 1️⃣ Extract – Fetch Data from API

The first step is retrieving league standings from a football data API.

Steps

- Read API documentation to understand endpoints

- Create a project folder in VS Code

-Create a Python virtual environment

- Install required libraries

- Create configuration files:

### Security Best Practice

API keys are stored in .env and excluded from Git using .gitignore.

### Process

- Load libraries into main.py

- Read environment variables

- Create API request

- Send GET request to retrieve data

### 2️⃣ Transform – Parse API Response

The API returns data in JSON format.

This step converts the raw response into a structured dataset.

#### Steps

- Parse JSON response

- Convert data into a Pandas DataFrame

- Preview and validate the dataset

This ensures the data is clean, structured, and ready for storage.

### 3️⃣ Load – Store Data in MySQL

Once cleaned, the standings are stored in a MySQL database for easy access and display.

#### Steps

- Create MySQL user

- Create database

- Grant database privileges

- Connect to MySQL server

- Connect to the database

- Upsert data into the Premier League standings table

- Verify successful data load

Using upsert logic ensures records are updated rather than duplicated.

### Business Impact

Implementing this system can:

- ✅ Improve customer experience during match nights
- ✅ Reduce staff interruptions and manual searches
- ✅ Deliver real-time insights to fans
- ✅ Create a more engaging sports bar environment

Beyond this use case, the same architecture can support:

- Live match statistics

- Goal alerts

- Team performance dashboards

- Sports analytics displays

### Future Improvements

- Possible extensions to the project include:

- Automating scheduled updates using cron jobs

- Building a Power BI or dashboard visualization

- Displaying live match statistics

- Creating a web interface for the screens