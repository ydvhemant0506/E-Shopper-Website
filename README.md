# E-Shopper-Website
This is a basic demo of an online shopping website. Its frontend is very similar to a real shopping app and it has many of the same features. Its Frontend is done with HTML, CSS and Javascript whereas backend is done with django completely.
# File Description in Project:
-> ECommerceWeb is our project direectory and it consists of the following files in it:
    urls.py : This consists of all the urls which a user hit on websearch and divert them to the respective endpoints.
    settings.py : This file has all the settings of project regarding app registration static and templates configuration and smtp authentication also.
    Along with these two it also consists of _init_.py, wsgi.py, asgi.py and also contains a directory _pycache_

-> home is the app of our project. Its File description is as follows:
    views.py : This file consists of all the views(functions) that we create in the project. These views fetches data from our models(in database) and feed
                them to the required templates.
    urls.py : This file consists of all the urls to endpoints of the project that a user after logging in can access. urls.py of our project basically direct
                all the request to this urls.py of the app and then further processing occurs from here itself.
    models.py : This File consists of all the models that we have made in our project.
    admin.py : Here we register all our models which are created in models.py
    Along with these files app also contains _init_.py, apps.py, tests.py and a migration directory which stores all the migration which a user made during the
    project.

-> static Directory:
    This consists of all the static files of project which includes css, fonts, js and images directory which are a part of project's frontend part.

-> templates:
    This directory consists of all the HTML templates which will be rendered when user made specific requests. Basically all the templates are stored here.

-> ecommerce:
    This directory consists of two subdirectories that are pimg(consists of all product images) and accimg(consists of all user images) these are uploaded at
    the time we save them in the admin pannel.

-> Along with this we also have manage.py file and db.sqlite3 file which is created whenever a project is created.

# Working of the Project:
-> Working Flow of the Project:
    When ever a new user comes in he will be shown wiith the home page. When user signup or login into the server then he/she can surf the E-Shopper website
    can view all the products both in general and descriptive view. User can also have the detailed view of all the products in the product tab. Also user 
    can select any product and add ot to cart. Also one can see the account details in the accounts tab. After making the cart user can also checkout the order
    and then all his orders placed will be shown in the Your Orders tab. A user can also search specific products by their brands, category, subcategory and 
    by the name of product itself by writing in the search bar. A user can also reset his.her password by clicking on forget password during loggin in into
    website. user can also access contact page where he/she can provide the contact details and any concerns which are store in the database backend.
