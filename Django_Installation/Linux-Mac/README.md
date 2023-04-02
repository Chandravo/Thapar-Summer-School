
# Setup guide of Django for  Linux/Mac Users




## Pre-Requisites

Before you start, make sure you have the following installed.

### Python 3.x
- you can check if you have python installed by running the following command on your terminal

```bash
$ python --version
```
or

```bash
$ python3 --version
```

Resources : 
- [Python installation on Linux](https://www.scaler.com/topics/python/install-python-on-linux/)
- [Python installation on Mac-os](https://www.dataquest.io/blog/installing-python-on-mac/)

### pip
- you can check if you have pip installed by running the following command on your terminal

```bash
$ pip --version
```
or

```bash
$ pip3 --version
```

<br>

<img src="https://res.cloudinary.com/dgbobpgf4/image/upload/v1680176102/django-tut/python-pip.png">

## Step 1 — Open Terminal
First, you need to open Terminal on your on linux or macos.


## Step 2  - Creating a Project Directory

This part involves the creation of a folder that will hold your Django application. For the purposes of this tutorial, we will refer to it as firstProject. However, in an actual project, you are free to choose a more appropriate name which describes the projetc more accurately.

Change into your preferred directory with the cd command. For this tutorial we will make the project in the Documents directory:

```bash
$ cd Documents
```

Create the directory using the mkdir command:

```bash
$ mkdir firstProject
```
Move into the firstProject directory using the cd command:
```bash
$ cd firstProject
```
Your prompt should now show you that you’re in the firstProject directory as shown in the following output:


<br>
<img src = "https://res.cloudinary.com/dgbobpgf4/image/upload/v1680176069/django-tut/firstProjectDirectory.png">

After setting up the working directory for your project, the next step is to establish a virtual environment where you can install Django.


## Step 3 - Creating a Virtual Environment

You'll first need to install the virtual environment package in global system to use it in project directories .

```bash 
$ pip install virtualenv
```

or

```bash 
$ pip3 install virtualenv
```

Next step, you’ll create a virtual environment for your project. A virtual environment is an isolated environment in Python where you can install the project dependencies without affecting other Python projects. This lets you create different projects that use different versions of Django.

If you don’t use a virtual environment, your projects in your system will use the same Django version installed globally. This might look like a good thing until the latest version of Django comes out with breaking changes causing your projects to fail altogether.

You can learn more about the virtual environment by following Python Virtual Environments: A Primer.

To create a virtual environment, type the following command and wait for a few seconds:

```bash
$ virtualenv env
```

The command will create a directory called env inside your project directory.

Next, confirm the env directory has been created by listing the directory contents using the ls command:

```bash
$ ls 
```

You should see the directory env in the output as shown :

<br>
<img src = "https://res.cloudinary.com/dgbobpgf4/image/upload/v1680175824/django-tut/installenv.png">

Now you’ve created the virtual environment directory, you’ll activate the environment.


## Step 4 - Activating the Virtual Environment

In this section, you’ll activate the virtual environment in your directory.

Run the following command to activate the virtual environment:
```bash
$ source env/bin/activate
```

After you run the command, you will see 
a (env) at the beginning of the prompt. This shows that the virtual environment is activated:

<img src="https://res.cloudinary.com/dgbobpgf4/image/upload/v1680176278/django-tut/activateEnv.png">

Now that you’ve activated the virtual environment for your project, the moment you’ve been waiting for is here. It’s time to install Django!

## Step 5 - Installing Django
In this section, you will install Django on your system using pip.
Make sure that your virtual environment is activated for the next commands. To activate your virtual environment follow step 4.
Run the following command to install the latest version of Django:
```bash
$ pip install django

```

If you want to install a different Django version, you can specify the version as follows:

```bash
$ pip install django==3.2.9

```
Once the installation finishes, you need to verify that Django has been installed. To do that, type the following command:
```bash 
$ django-admin --version

```
You will get output showing you the Django version installed on your system:

<img src="https://res.cloudinary.com/dgbobpgf4/image/upload/v1680176647/django-tut/installDjango.png">

At the time of writing, the latest Django version is 4.1.7, and that’s why my output shows that.

You’ve now installed Django on your system, great job! You’ll begin to create a Django project.


## Step 6 - Creating the Django Project
Now it’s time to create a project. A project has a different meaning from what you may be used to. The Django documentation defines it as:

A Python package – i.e. a directory of code – that contains all the settings for an instance of Django. This would include database configuration, Django-specific options and application-specific settings.

You create a project by using the command-line utility django-admin that comes with Django. The command generates files where you can configure the settings for your database, add third-party packages for your project to mention a few.

Note : Run all the commands with your virtual environment activated

Create the project using the django-admin startproject command:

```bashh
$ django-admin startproject test_project
```
Change into the test_project directory:

```bash
$ cd test_project
```
Type the following command to see the contents in the project directory:

```bash
$ ls
```
You will get output similar to this:

<br>
<img src="https://res.cloudinary.com/dgbobpgf4/image/upload/v1680178147/django-tut/startProject.png">


The directory test_project contains Django configuration files. 

The manage.py file is a command-line utility that comes with every Django project. It provides a way to interact with various aspects of the project, such as running the development server, creating database tables, and running tests. You can execute various commands in the terminal using python manage.py <command>. For example, python manage.py runserver starts the development server. We will be doing this in the next step.

The project folder, on the other hand, is the top-level folder of your Django project. It usually has the same name as your project and contains all the necessary files and folders to make your Django project work. Inside the project folder, you'll typically find a few files and directories, including the settings.py file, which contains the project settings, a urls.py file, which contains the URL configuration for the project, and a wsgi.py file, which is used for deployment.

Overall, the manage.py file and the project folder are both critical components of any Django project, and understanding how they work is essential to developing Django applications effectively.

## Step 9 - Running the Development Server
Now that the project has been created, we will start the Django development server.

Note : Run all the commands with your virtual environment activated

Start the development server using the manage.py runserver command:
```bash 
$ python manage.py runserver
```

Next, visit http://127.0.0.1:8000/ in your web browser. You should see a page similar to the following screenshot

![alt text](https://www.stanleyulili.com/assets/images/posts/2019-08-31-how-to-install-django-on-windows/server-running.jpg)



You can stop the server by holding CTRL+C. To deactivate the virtual environment, you can type deactivate on the prompt.

Now, you are ready to start developing your project, see you there in the session with multiple projects.
## References
https://docs.djangoproject.com/

## Credits
[Avnoor](https://github.com/avnoor-488)

Check out Avnoor's repository [here](https://github.com/avnoor-488/Thapar-Summer-School)
