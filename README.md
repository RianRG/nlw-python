# Pass In
This is a rocketseat project (NLW Unite) built for checkIn systems.

## Description
This API is built on SOLID principles, ensuring a robust and maintainable architecture, making it easy to extend and adapt to changing requirements.

## Main Concepts
To build this project, first we need to establish a connection with our database (On this case, we'll use the SQL Alchemy library), then we create *REPOSITORIES* for each use case of our application (like save a user, get all users, get a user by his id, get his relations, and others). On this project, we're following SOLID concepts, so we need to create repositories for each entity (Attendees, Events and Checkins).

The repository is the "place" of the application that makes contact with database.

After building the repositories, we need to build the ROUTES of our app, this is the "place" of the application that receives requests and return responses (On this project, through a HTTP protocol), and makes contact with repositories. Completely isolated of database and other dependencies.

Its very important to create Error Handlers for our application, because the errors usually dont have a "good" format to read and understand. So we build Error Handlers to help the user or our coworkers.



## Technical Details

* Python
* Flask
* Flask CORS
* SQL Alchemy
