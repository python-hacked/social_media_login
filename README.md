# social_media_login

This is a Django web application that demonstrates how to implement social media authorization login using Django-allauth library. Users can log in to the application using their Google, Facebook, and other social media accounts.

## Getting Started

To run this project locally, follow the steps below:

### Prerequisites

Make sure you have the following software installed on your system:

- Python (version 3.10 or higher)
- Django (version 4.2.2 or higher)
- pip (Python package manager)

### Installation

1. Clone this repository to your local machine:`https://github.com/python-hacked/social_media_login.git`


2. Install the required Python packages using pip:


3. Configure Django-allauth:

   - Open the `social_media_login/settings.py` file.
   - Update the `INSTALLED_APPS` list and add the required allauth apps.
   - Update the `AUTHENTICATION_BACKENDS` list to include allauth backend.
   - Add your social media app credentials in the settings for Google, Facebook, and any other providers you wish to use.

### Running the Application

1. Apply the database migrations:`python manage.py makemigrations` and Migrate `python manage.py migrate`


2. Create a superuser (admin) to access the Django admin interface:`python manage.py runserver`


4. Access the application in your web browser at `http://localhost:8000/accounts/login/.`

## Usage

1. Click on the "Login with Google" or "Login with Facebook" link to authorize using your social media account.
2. After successful authorization, you will be redirected to your profile page, where you can see the connected social media accounts.

## Contributing

If you would like to contribute to this project, follow these steps:

1. Fork the repository and create a new branch from `main`.
2. Make your changes and ensure they are thoroughly tested.
3. Commit your changes and push them to your forked repository.
4. Submit a pull request to the original repository.



## Acknowledgments

- The project uses the [Django](https://www.djangoproject.com/) web framework.
- The social media authorization is implemented using [Django-allauth](https://django-allauth.readthedocs.io/) library.

Feel free to modify this README file to add more specific instructions or include any additional information that might be helpful for users and contributors to understand and use your project.

Happy coding!


