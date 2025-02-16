Description:This project automates data extraction from PostgreSQL, generates a CSV report, and emails it, reducing manual effort.

Key Features:

Connects to PostgreSQL using credentials from a config file.

Executes an SQL query to fetch booking data.

Exports data to a CSV file.

Emails the report as an attachment.

Uses SMTP for secure email transmission.

Technology Stack:

Language: Python

Database: PostgreSQL

Libraries: psycopg2, csv, configparser, smtplib, email.message

How It Works:

Reads credentials from a config file.

Connects to the database and fetches data.

Writes data to a CSV file.

Reads email credentials and sends the report via SMTP.

Use Cases:

Automating periodic reports.

Reducing manual effort.

Ensuring timely report delivery.

