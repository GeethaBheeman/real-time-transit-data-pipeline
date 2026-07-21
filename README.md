\# Real-Time Transit Data Pipeline and Analytics Application



\## Overview



This project implements an end-to-end transit data pipeline that retrieves live MBTA Route 1 vehicle-location data through a REST API, stores historical bus records in MySQL, displays current bus locations through a Flask and Mapbox web application, and synchronizes database changes to MongoDB using Debezium Change Data Capture.



The project also uses Python and Jupyter Notebook to analyze historical transit data, estimate route-completion time, and calculate average vehicle speed from geographic coordinates.



\## Architecture



```text

MBTA Vehicle REST API

&#x20;         │

&#x20;         ▼

Python API Client

&#x20;         │

&#x20;         ├──────────────► Flask Web Application

&#x20;         │                        │

&#x20;         │                        ▼

&#x20;         │               Mapbox Bus Visualization

&#x20;         │

&#x20;         ▼

MySQL Transit Database

&#x20;         │

&#x20;         ▼

Debezium Change Data Capture

&#x20;         │

&#x20;         ▼

Java Spring Boot CDC Listener

&#x20;         │

&#x20;         ▼

MongoDB

&#x20;         │

&#x20;         ▼

Java CDC Validation

```



\## Features



\* Retrieves live MBTA Route 1 bus-location data

\* Parses API responses in Python

\* Stores historical transit records in MySQL

\* Displays bus positions through Flask and Mapbox

\* Runs MySQL and MongoDB in Docker containers

\* Uses Debezium to capture MySQL database changes

\* Writes CDC events to MongoDB through Java

\* Validates replicated records using a Java MongoDB client

\* Analyzes route-completion time and vehicle speed in Jupyter Notebook



\## Technologies



\* Python

\* Flask

\* REST APIs

\* MySQL

\* MongoDB

\* Debezium

\* Docker

\* Java

\* Spring Boot

\* Maven

\* Mapbox

\* Pandas

\* Matplotlib

\* Jupyter Notebook

\* JSON

\* Git



\## Project Structure



```text

Transit Data Application/

├── README.md

├── .gitignore

└── MBTASample/

&#x20;   ├── Module16 - Template.ipynb

&#x20;   ├── Module16ProjectFlask/

&#x20;   ├── mysqlDocker/

&#x20;   ├── DebeziumCDC/

&#x20;   └── java-quick-start/

```



\## Security



Mapbox tokens, database passwords, generated data, runtime logs, build artifacts, and environment-specific secrets should not be committed to version control.



\## Author



\*\*Geetha Bheeman\*\*



MIT xPRO — Professional Certificate in Data Engineering



