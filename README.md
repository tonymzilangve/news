# news


Pull the project from Github
* git clone https://github.com/schMok0uTr0nie/api_mail.git

Create virtual environment
* python -m pip install --upgrade pip
* python -m venv venv

Activate virtual environment
* venv/Scripts/activate

Install dependencies
* pip install --no-cache-dir -r requirements.txt

Migrate the database tables
* python manage.py migrate

Start a development server
* python manage.py runserver
