# Django High Request

Django High Request is a web application designed to manage and schedule classes for an educational institution. 
Students can view their class schedules. 
The application leverages Django for the backend, Docker for containerization, and Redis for caching to ensure high performance and scalability. 


## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Next Steps](#next-steps)

## Requirements
1. [Docker](https://www.docker.com/products/docker-desktop/)
2. [Python](https://www.python.org/downloads/)


# Installation
0. Create your own `.env` file in the root directory of the project and add/update the variables:
   ```sh
   cp .env.example .env
   ```
1. Build and start the Docker containers:
   ```sh
   docker compose up --build -d
   
2. To run all the unit tests, use the following command:
    ```sh
    docker-compose exec web python src/manage.py test src/apps/


# Features

1. **Docker** is used to containerize the application, ensuring that it runs consistently across different environments. The Dockerfile defines the environment in which the application runs, including the base image, dependencies, and commands to set up and run the application.  Docker Compose is used to manage multi-container Docker applications. It allows you to define and run multiple containers as a single service. The docker-compose.yml file specifies the services, networks, and volumes required for the application.
2. **Docker Compose** is used to manage multi-container Docker applications. It allows you to define and run multiple containers as a single service. The docker-compose.yml file specifies the services, networks, and volumes required for the application.
3. **Logging** is configured to capture and store logs for debugging and monitoring purposes. The run.sh script configures Gunicorn to log access and error messages to access.log and error.log files, respectively. This helps in tracking the application's behavior and diagnosing issues.
4. **Redis** is used for caching to improve the performance and scalability of the application. It stores frequently accessed data in memory, reducing the load on the database and speeding up response times.
5. **Gunicorn** is a Python WSGI HTTP server for UNIX. It is used to serve the Django application. The run.sh script starts the Gunicorn server with optimized settings, including the number of workers, worker class, and connection settings, to handle high traffic efficiently.
6. **Unit Tests** are implemented to ensure the reliability of the application. The tests are written using Django's testing framework and can be run using Docker to ensure consistency across different environments. The tests cover various aspects of the application, including API endpoints, data validation, and business logic.


# API Endpoints

```
GET /schedule/
```
Response:
```
[
    {
        "student_class": {
            "name": "Class 5",
            "student_count": 20
        },
        "subject": {
            "name": "Subject 29"
        },
        "day_of_week": 1,
        "hour": 8,
        "teacher": {
            "name": "Teacher 34"
        }
    }, 
    ...
]
```


# Next Steps
1. **CI/CD Pipeline**: Set up a Continuous Integration/Continuous Deployment (CI/CD) pipeline to automate testing and deployment.
2. **Performance Monitoring**: Integrate performance monitoring tools to track the application's performance and identify bottlenecks.
3. **API Documentation**: Use tools like Swagger or Postman to create comprehensive API documentation for developers.
4. **Environment Variable Validation**: Implement a mechanism to validate the environment variables to ensure they are set correctly before the application starts.
5. **Local Development info and set-up**: Add detailed instructions on how to set up the project for local development and testing.