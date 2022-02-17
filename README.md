# My Blog
A simple blog application where all can read blogs without log in. Anyone need to registration themselves as `Member` to create post and update them. An `Editor` have to approve the post to get rid off from unwanted contents. After getting approved those post will be shown in Homepage. `Admin` can do all CRUD operations. All `User` of the system can see their profile page and their personal information.




## Getting Started
- Clone the repository
- Create a virtual environment, ideally with a name starting with `venv-` as it's
auto-ignored.
- Activate the virtual environment.
- Run: `pip install -r requirements.txt`
- Run: `python manage.py makemigrations`
- Run: `python manage.py migrate`
- Run: `python manage.py createsuperuser` to create a `Admin`
- Run: `python manage.py runserver` and follow that link.
- You should see the `Homepage` of web application.
- You can log in with `Admin's` login credentials.
- You can also register new user and make new post.
- `Admin` has to make a new user as `Editor` to approve those post.
- After getting approval the post's will be shown in `Homepage`

## Live Server
[Imran's Blog](https://alimran.pythonanywhere.com/)
