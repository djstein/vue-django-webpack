!!! Disclaimer: This package is not maintained and therefore is not recommended for production use. It is also recommended not to deploy a JavaScript application through Django. Please refer to load balancing with nginx or ELB/ALB and storing files on S3 or similar services.

# vue-django-webpack

<h1 align="center">
  Vue.js and Django Web Application
</h1>

<p align="center">
  <img src="https://raw.githubusercontent.com/djstein/vue-django-webpack/master/app/vueapp/src/assets/vue-logo.png" width="75" />
  <img src="https://raw.githubusercontent.com/djstein/vue-django-webpack/master/app/vueapp/src/assets/django-logo.png" width="200" />
</p>

- Use of Vue.js in component form
- Webpack building the JavaScript and CSS portions of the application
- Django serving builds with django-webpack-loader

The advantage to this over a pure Vue.js application are those niceties included in Django's core library such as database managment and URL routing. This also includes the ability to add third party applications such as, the Django REST Framework, quickly and painfree.

Once a bundle has been created with Webpack, it can easily be served with Django's django.contrib.staticfiles app.

##Installation
Setup a new Python 3 virtualenv and install the pip and npm requirements.
```bash
git clone https://github.com/djstein/vue-django-webpack.git
cd vue-django-webpack

# Virtual environment
virtualenv -p python3 venv
source venv/bin/activate

pip install -r requirements.txt
npm install
```

## Development
During development it is useful to access the hot-load features without the need to rebuild the application.
Do so by running Django in one terminal and the node server in another.
```bash
# Run Django webserver
python manage.py runserver

# Run node webserver
npm run dev
```
Any changes made to `app/vueapp/src/` will now be seen automatically in development. Feel free to add components / new pages / etc.

## Webpack Build
### Local
To use the application without the use of the node server, use webpack to create a build. This will automatically switch the path needed in webpack-stats.json to reprsent the local build development bundles (.js and .css), with no changes to Django for local development.
```bash
# Local Build
npm run build
```
Django can continue to run while the build is recreated, however it is advised to stop the webserver and clear the browswer cache when creating new builds.
```bash
# Run Django webserver
python manage.py runserver
```

### Production
**Production Instructions Are Not Complete**

For production builds, using build-proudction will pack and UglifyJS the application. IT IS RECOMMENDED TO STILL COMPLETE THE  [DJANGO](https://docs.djangoproject.com/en/dev/howto/deployment/checklist/) AND [VUE.JS](https://vuejs.org/v2/guide/deployment.html) PRODUCTION DOCUMENTATION BEFORE DEPLOYING.
```bash
# Production Build
npm run build-production
```

## Sources 

These resources were heavily referenced:

https://github.com/vuejs-templates/webpack/tree/master/template

https://github.com/owais/django-webpack-loader/tree/master/examples

## Contributions
Please feel free to pull, fork, or add suggestions
