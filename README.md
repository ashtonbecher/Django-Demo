# Django Demo

Small Django app that shows a beginner's proficiency with Django

---
### Installation
To install this project, you will need the following prerequisites:
* Django
  * To verify your Django installation, run the command `python -m django --version`
* Python
  * To verify your python installation, run the command `python`. The output should list the current Python version if you have Python installed


With these prerequisites installed, you should be able to clone the repository to your local machine and be set up to run the app.
1. With the project cloned, you can navigate to the project directory in your preferred terminal application and run the command `python manage.py runserver`
   * If you get the following, the installation worked and you can proceed to step 3. If not, continue to step 2: 
    ```
   Performing system checks...
    
    System check identified no issues (0 silenced).
    
    You have unapplied migrations; your app may not work properly until they are applied.
    Run 'python manage.py migrate' to apply them.
    
    February 14, 2023 - 15:50:53
    Django version 4.0, using settings 'mysite.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    ```
2. Verify that you have the most recent stable version of both Django and Python. If you do, delete the project, clone it, and try step 1 again
3. In a web browser, go to http://localhost:8000/polls for the user-facing application or http://localhost:8000/admin for the admin panel
    * If you don't have an admin user already, you will need to create one by running `$ python manage.py createsuperuser`
    * Enter a desired username, email, and password and your new admin user will be created
---

### Features & Overview
This is a very lightweight application that essentially just lists a collection of questions and their responses. The majority of the workload is done behind the scenes from the admin panel and the SQLite database.
The application is intentionally very barebones to simply showcase an entry-level understanding of Django, but the underlying code is easy to understand due to intentional code comments
to help the reader.

The user-facing site simply displays questions and then the responses once the question is clicked on. The questions are sorted by the number of votes each question has (in the db).

The admin panel is a bit fancier. An admin can manage users and groups under the "Authentication and Authorization" section. And admin can also directly inject data into the database with the "Polls" section by adding/editing/removing questions, responses, and votes.