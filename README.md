# Django Chat GPT Integration with Django Channels

> This Django project demonstrates how to integrate Chat GPT with Django channels to enable live chat functionality.

### Prerequisite

1. [Install Python 3.9.0](https://www.python.org/downloads/)
2. [Install Pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv)
3. [Install Django 4.0.6](https://docs.djangoproject.com/en/4.0/topics/install/)
4. [Install PyCharm (Preferred IDE)](https://www.jetbrains.com/pycharm/download/)

# Installations
1. Clone this repository using git clone https://github.com/adnan9867/chat_gpt.git.
2. Create a virtual environment using python -m venv env and activate it using source env/bin/activate (on Linux/Mac) or env\Scripts\activate (on Windows).
3. Install the required packages using pip install -r requirements.txt.

# Configurations
1. Set up your Chat GPT credentials and Django secret key in a .env file. You can copy the .env.example file and update the values accordingly.
2. Set up your database by running python manage.py migrate.

# Usage
1. Run the Django development server using python manage.py runserver.
2. Open your browser and navigate to ws://127.0.0.1:8000/ws/chat_gpt/.
3. Type your message and click "Send" to send it to the Chat GPT model, which will respond with a message.
4. Continue chatting back and forth with the Chat GPT model as long as you want.

# Troubleshooting
1. If you encounter any issues with the installation or usage of this project, please refer to the Django documentation or seek help from the Django community.

# License
This project is licensed under the MIT License. Feel free to use and modify this project for your own purposes.




