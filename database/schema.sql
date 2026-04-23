-- Schema for Smart Irrigation System
-- Note: SQLAlchemy creates the tables automatically, but this is provided for reference/manual setup.

CREATE TABLE sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    moisture REAL NOT NULL,
    temperature REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pump_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status VARCHAR(10) NOT NULL,
    source VARCHAR(50),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ai_insights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reasoning VARCHAR(255) NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
