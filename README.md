# Trendy-news-and-blogs (In development)
<br>
<p><strong>Deployment Link: <a href="https://trendy-dev.herokuapp.com/">trendy-dev.herokuapp.com/ </a></strong> </p>

<h4> At Trendy, You can view top news headlines on the go or Read blogs on interesting topics. </h4> 
<br>
I have covered the following points in the project.<br>
<p>
I. Web Development
<ol>
    <li> Authentication using django auth. </li>
    <li> API calls using news-api (requests), CRUD operations by users on Blog. </li>
    <li> Exposed an API endpoint for only the site admin the perform CRUD operations on Blog. Used Django Rest Framework. </li>
    <li> Designing (For the most part, I have used a custom UI kit and an icon library) </li>
</ol>
II. Deployment
The project has been deployed on Heroku.

</p>
<br>

## Demonstration

<br>

### Home Page
<img src="https://raw.githubusercontent.com/shreyan-haldankar/Trendy-news-and-blogs/main/static/images/demo_home.png">

### News Portal
<img src="https://raw.githubusercontent.com/shreyan-haldankar/Trendy-news-and-blogs/main/static/images/demo_news_main.png">

### Blog Posts
<img src="https://raw.githubusercontent.com/shreyan-haldankar/Trendy-news-and-blogs/main/static/images/demo_blogs.png">

### User Dashboard
<img src="https://raw.githubusercontent.com/shreyan-haldankar/Trendy-news-and-blogs/main/static/images/demo_account.png">

### Create a Blog Post
<img src="https://raw.githubusercontent.com/shreyan-haldankar/Trendy-news-and-blogs/main/static/images/demo_add_blog.png">

<br>

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/shreyan-haldankar/Trendy-news-and-blogs.git
```

Install requirements using:

```sh
$ pip install -r requirements.txt
```

Once `pip` has finished installing the requirements:
```sh      
$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

<br>

## API Usage 
In order to use the API endpoint https://trendy-dev.herokuapp.com/api/ , the user must be a site-admin.

To become a site-admin and test the api, you can

### 1. Install the repository locally
```sh
$ git clone https://github.com/shreyan-haldankar/Trendy-news-and-blogs.git
```

### 2. Create a superuser
```sh
$ python manage.py createsuperuser
```
Follow the command line steps

### 3. Run the server
```sh
$ python manage.py runserver
```

### 4. Access the API endpoint views via a browser
Go to <a href="http://127.0.0.1:8000/api/">127.0.0.1:8000/api/</a>

### 5. Test the API
Send HTTP requests to this API such as GET, POST, PUT, DELETE for performing CRUD operations on the Blogs.
