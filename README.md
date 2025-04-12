# Social Media RESTful API

A RESTful API built with Django and Django REST framework for a social media platform. It enables user registration, profile management, post creation, interactions (likes/comments), and other core social media functionalities. API documentation is available via Swagger.

## Features

- **User Authentication**  
  - Register with email and password
  - Login/Logout functionality
  - Token-based authentication

- **User Profile Management**  
  - Create, retrieve, and update profiles
  - Profile pictures and bio support
  - Follow/Unfollow other users
  - View followers/following lists

- **Post Management**  
  - Create, retrieve, update, and delete posts
  - Text content with optional media attachments
  - Like/Unlike posts
  - Comment on posts

- **Security**  
  - Django authentication and permission classes
  - Protected endpoints for authenticated users only

- **API Documentation**  
  - Comprehensive documentation via Swagger UI

## How to Use
# Clone the repository
git clone https://github.com/thebaker-1/GDG-GROUP1.git

# Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate

# Install necessary packages
pip install -r requirements.txt

# Apply migrations and start the server
python manage.py migrate
python manage.py runserver

# Register a user and retrieve a token by user endpoints to test the API
