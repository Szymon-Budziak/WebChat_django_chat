# WebChat

WebChat project written in Django and Tailwind CSS for WebRTC course at UNINA.

## The structure of the project

Project consists of 3 main parts:

- **core** directory where is the logic for the main page, login, signup and logout
- **room** directory, inside it there is a logic for rooms and chat where user can join and have a chat with
  someone else inside the specific room
- **webchat** directory where are the django initial files that are created while running `django-admin startproject`
  command

After running a server (prerequisites are below) we should have such a website where we can sign up or log in:

![main_page](https://user-images.githubusercontent.com/75530523/207906155-9f92690c-3f73-413b-8fab-8ed656f065e4.png)

When we are logged in we can enter rooms:

![rooms](https://user-images.githubusercontent.com/75530523/207906197-b49c437f-d0a6-4f13-a13d-c84fd5c68224.png)

After entering one of the rooms we can have a chat with other users:

![chat](https://user-images.githubusercontent.com/75530523/207906251-5111e6c7-3556-442e-bc9b-97dc7772100f.png)

When we log out we are redirected to the main page.
## Prerequisites

Before you start, you have to install all requirements. Installation process on Linux/macOS and Windows:

__1. Clone repository by typing:__

```
git clone https://github.com/Szymon-Budziak/WebChat_django_chat.git
```

__2. Enter `WebChat_django_chat` folder:__

```
cd WebChat_django_chat/
```

__3. Create new virtual environment for this project and activate it:__

- Linux/macOS machine:

```
python -m venv venv
source venv/bin/activate
```

(if python is not working try using python3)

- Windows machine:

```
py -m venv venv
venv\Scripts\activate
```

this will create new activated virtual environment with `venv` name.

__4. Install required packages:__

```
pip install -r requirements.txt
```

If this command is now working, install `django` and `channels` in command line:

```
pip install django channels==3.0.5
```

__5. Enter `webchat` folder and make migrations to create necessary databases for models:__

- Linux/macOS machine:

```
python manage.py migrate
```

(if python is not working try using python3)

- Windows machine:

```
py manage.py migrate
```

__6. Create `superuser` to have access to admin page:__

- Linux/macOS machine:

```
python manage.py createsuperuser
```

(if python is not working try using python3)

- Windows machine:

```
py manage.py createsuperuser
```

Now you are ready to explore Django code and run server, enter dashboard website `http://localhost:8000`:

- Linux/macOS machine:

```
python manage.py runserver
```

(if python is not working try using python3)

- Windows machine:

```
py manage.py runserver
```
