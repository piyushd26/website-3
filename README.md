website
=======
[![Build Status](https://travis-ci.org/jonge-democraten/website.svg?branch=master)](https://travis-ci.org/jonge-democraten/website)

JD website

## Installation
 * **Build a new work environment:** `$ ./build_env.sh`
 * **Remove the current work env:** `$ ./clean_env.sh`
 * **Generate local settings:** `$ python3 create_local_settings.py`
 * **Activate work env:** `$ source ./env/bin/activate`
 * **Create a database:** `(env) $ python3 website/manage.py createdb`
 * **Run the test server:** `(env) $ python3 website/manage.py runserver`
 
## Testing 
All application logic code is to be unit tested. Unit tests are ideally created before development of functionality.
It supports development and documents, in real code instead of text, what classes and functions are supposed to do.
Feature branches are only merged if unit tests are written and all pass. 

Higher level user interface actions are tested manually. 

#### Unit tests
The project uses the [Django unit test](https://docs.djangoproject.com/en/dev/topics/testing/overview/) framework to create unit tests. 
This framework is based on the Python unittest module. 

Tests are defined in the `tests.py` file of the application directory. 

##### Run tests
Tests for the project's Django applications can be run with the following command, 

`(env) $ python website/manage.py test <appname>`

#### Automated testing
[Travis](https://travis-ci.org/jonge-democraten/website) is used to automatically install the environment and run tests on changes in the project. 

The file `.travis.yml` contains the Travis commands to install and test the project.

The build indicator on top of this document shows the status of the last automated install and tests.


## Development
This section provides some guidelines to ensure consistency within the project and streamline the workflow.  

#### Coding standards
The default Python and Django code style is used. Read about it [here](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/).

*"Write code as simple as possible and focus on readability. Write code for others to understand and read."* - [source
(http://c2.com/cgi/wiki?CodeForTheMaintainer)


#### Workflow
New features are developed on a separate feature branch. 

This allows you to work independently on a feature and still share code. Push feature branch commits often to communicate what you are working on. 

Read more about this workflow [here](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow).

#### Logging
The Python logging module is used for logging. Add and commit plenty of useful log statements. This support effective debugging. 

The logging is configured in the Django `settings.py` `LOGGING` variables. Information about configuration you can be found [here](https://docs.djangoproject.com/en/1.7/topics/logging/). New applications have to be added before logging becomes active for those applications. 

##### How to use
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
##### Levels
Five log levels are available, `logger.debug()`, `logger.info()`, `logger.warning()`, `logger.error()`, `logger.critical()`. 

The log statements for the applications are written to the console, if DEBUG=True, and always to `debug.log` and `error.log`. Django errors can be found in `django.log`.

##### Confidential information 
Confidential information should not be logged. During initial development, logging of confidential information is allowed if marked with a `CONF` tag, `logger.debug('CONF ' + member.DNA)`. These will be removed before deployment. 
