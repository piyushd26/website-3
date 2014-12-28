<h1>Developer manual</h1>
This is a manual for jdwebsite developers.

<h3>Topics</h3>
* Development environment installation instructions.
* A general workflow description.
* Information about logging and testing.
* Information about database management.
* Code and documentation guidelines.

<h3>Todo</h3>
* Mezzanine and jdwebsite; tweaks and pitfalls. 
* Deployment instructions.
* Versioning strategy.
* Useful development tools.
* Project structure

# Installation
Installation is easy on a Linux-like operating system.  
For Windows and Mac, we advise to create a Linux virtual machine. Instructions are given below.

<h3>Basics</h3>
1. `$ ./build_env.sh`
1. `$ source ./env/bin/activate`  
1. `$ python create_local_settings.py`
1. `$ python website/manage.py createdb`
1. `$ python website/manage.py loaddata demo_data` #Optional, loads demo data (login: admin/admin)
1. `$ python website/manage.py runserver`  

<h3>Requirements</h3>
**Linux**  
Installation of the full project, and running a test server, can be done in a few minutes on any Linux machine. Just follow the steps under 'detailed instructions'. There is no need for manual configuration.

**Windows and Mac**  
For Windows and Mac users, it is advised to install a Linux virtual machine and use this to install the project. To do so, follow the next steps,

1. Please visit [this](http://www.wikihow.com/Install-Ubuntu-on-VirtualBox) howto for step-by-step instructions to install Ubuntu on VirtualBox.  
2. Start Ubuntu in a VirtualBox, open the program called "Terminal" and install some required applications by entering the command,  
`$ sudo apt-get install git python-virtualenv python3-dev`  
3. Continue with the instructions below.

<h3>Detailed instructions</h3>
**Get the code**  
Create a new clone of the project in a directory of your choice,  
`$ git clone https://github.com/jonge-democraten/website.git`

**Virtual environment**  
Build a new work environment in the project directory. This creates a virtual environment `env` and installs all required modules,  
`$ ./build_env.sh`  
Activate the virtual environment,  
`$ source ./env/bin/activate`  
From now on, everything you do within the project should be from a shell with activated virtual env.

**Configure Django settings**  
A Django settings file, `local_settings.py`, with `SECRET_KEY` is generated by,  
`$ python create_local_settings.py`  

**Create a database**  
You have to create an initial database and a root user and password for the database,  
`(env) $ python website/manage.py createdb`

**Run a test server**  
You can run a local test server with the command,  
`(env) $ python website/manage.py runserver`  
and visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to view the web interface.

**Get the latest changes**  
To get the latest version of the project, type the following git command in your project directory,  
`$ git pull`

**Clean project**  
You can remove the virtual environment and database with,  
`$ ./clean_env.sh`


# Testing
All application logic code is to be unit tested. Unit tests are ideally created before development of functionality.  
It supports development and documents, in real code instead of text, what classes and functions are supposed to do.
Feature branches are only merged if unit tests are written and all pass.  
Higher level user interface actions are tested manually. 

<h3>Unit tests</h3>
The project uses the [Django unit test](https://docs.djangoproject.com/en/dev/topics/testing/overview/) framework to create unit tests. 
This framework is based on the Python unittest module.  
Tests are defined in the `tests.py` file of the application directory. 

**Run tests**  
Tests for the project's Django applications can be run with the following command,  
`(env) $ python website/manage.py test <app_label>`
 
<h3>Automated testing</h3>
[Travis](https://travis-ci.org/jonge-democraten/website) is used to automatically install the environment and run tests on changes in the project.  
The file `.travis.yml` contains the Travis commands to install and test the project.  
The build indicator on top of this document show


# Logging
The Python logging module is used for logging. Add and commit plenty of useful log statements. This support effective debugging. 

<h3>Example</h3>
To add log statements, simply add the following at the top of your Python file,
```python
import logging
logger = logging.getLogger(__name__)
```
and add a new log statement anywhere in this file by,
```python
logger.debug('debug log statement')
logger.warning('warning message')
logger.error('error message')
```
The log statements include log level, application, class, function and line number of the log statement,
```python
[2014-12-19 22:39:11] ERROR [website.tests::test_logfile() (23)]: Cannot find anything here.
```
<h3>Levels</h3>
Five log levels are available, `logger.debug()`, `logger.info()`, `logger.warning()`, `logger.error()`, `logger.critical()`. 

<h3>Output to console and file</h3>
The log statements for the applications are written to the console, if DEBUG=True, and always to `debug.log` and `error.log`. Django errors can be found in `django.log`.

<h3>Configuration</h3>
Logging is configured in the Django `settings.py` `LOGGING` variables. Information about configuration can be found [here](https://docs.djangoproject.com/en/1.7/topics/logging/). New applications have to be added before logging becomes active for those applications. 

<h3>Confidential information</h3>
Confidential information should not be logged. During initial development, logging of confidential information is allowed if marked with a `CONF` tag, `logger.debug('CONF ' + member.DNA)`. These will be removed before deployment.  


# Workflow
New features are developed on a separate feature branch.  
This allows you to work independently on a feature and still share code. Push feature branch commits often to communicate what you are working on.  
Read more about this workflow [here](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow).


# Code standards
The default Python and Django [code style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/) is used.  
Write code as simple as possible and focus on readability. Write code for others to understand and read.

*"Always code as if the person who ends up maintaining your code is a violent psychopath who knows where you live. "* - [source](http://c2.com/cgi/wiki?CodeForTheMaintainer)

<h3>Flake8</h3>
Flake8 is a Python tool to check code style. It runs automatically on Travis after each commit.  
You can find the Flake8 output in the [latest Travis build log](https://travis-ci.org/jonge-democraten/website).

# Code documentation
Add comments to code that is not self-explanatory.  
Use [python docstrings](http://en.wikipedia.org/wiki/Docstring#Python) to describe files, classes and functions.  
Add a brief docstring to files and classes. To functions only if necessary. Example,
```python
"""
File description.
"""

class ExampleClass(Example):
    """ Class description. """

    def example_function(self):
        """
        Function description 
        on multiple lines.
        """
```

# Database

<h3>Introduction</h3>

<h3>Migrations</h3>
A [database migration](https://docs.djangoproject.com/en/1.7/topics/migrations/) needs to be created after database structure changes in `models.py`,  
`$ python website/manage.py makemigrations <app_label>`  
The generated migration file is committed together with changes in `models.py`.  
Migrations have to be carefully managed between different branches, so keep track of other branches and prepare for a merge.