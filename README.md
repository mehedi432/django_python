<h3 style="text-align: center">Django Critical Parts</h3> <hr>

  <b>
    1. How to use static files in Django?
  </b>

Static files are the files which are used for designing user interfaces. The term static means of using CSS, JavaScript, Images in our application which won't be changed at application runtime. If we want to use these types of static files than we have to follow these rules -

    * Make a static folder in root project directory
    * We must have to explicitly tell django settings to use static files. For this we need to add below lines in core settings.py file -
    
```py
    # settings.py
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, '{project_name}/static')
    ]
```
    * Now we have to run a simple command to collect all the static files in our application. The command is - 
```sh
    python3 manage.py collectstatic
```
    * Congratulations - now we have a new folder in our root directory named as static & we are now able to use static html, css, image or webfonts in our application.

<b>2. How can we use static files in our template file or .html file ?</b>

    * Now we want to use static files in our templates. So, first of all we have to create a templates folder and we have to specify the template folder in our settings.py file as -
```py
TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    },
]
```
    * Now we can make a templates folder in the root of our application & create a base.html file. In this base.html file we can now load static files. The process is given below -

```html
<!-- In the above of our html file we have to add a line for loading static. -->
{% load static %}

<!-- Now, we have the ability to use static folder's items -->
<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}" crossorigin="anonymous">
```

