# About This Project
A RESTful API using Django and Django REST framework for a social media platform, enabling user registration, profile management, post creation and retrieval, interactions like likes and comments, and other core social media functionalities, and view API documentation via swagger.
  #HOW TO USE 
# Clone the repository
git clone https://github.com/olenaliuby/social-media-api.git

# Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate

# Install necessary packages
pip install -r requirements.txt

# Apply migrations and start the server
python manage.py migrate
python manage.py runserver

### Features:
    User Profile Management: Users can create, retrieve, and update their profiles, including profile pictures, bios, and other details. 

    Follow/Unfollow: Users can follow and unfollow other users, and retrieve lists of their followers and those they are following.

    Post Creation and Management: Users can create, retrieve, and update their posts, with text content and optional media attachments (images as an optional feature).

    Interactions: Users can like/unlike posts, retrieve posts they have liked, and add comments to posts.

    User Registration and Authentication: Users register with their email and passwords and receive a token upon login for subsequent authentication. The API also includes a logout function.

    API Permissions: The API uses Django's authentication and permission classes to ensure security and confidentiality. Only authenticated users can perform actions like creating posts, liking posts, and following/unfollowing others.

    API Documentation: All the endpoints are well-documented by DRF documentation via swagger.


