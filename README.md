# eshop | recommendation based ecommerce
## description
 IVth year major project for **Cosmos College of Engineering and Management**

## setting up for first usage
## requirements
### python
navigate to `/backend` and run:
```
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install Pillow
pip install numpy
pip install scipy
pip install scikit-learn
```
### node
navigate to `/frontend` and run:
```
npm i
npm i --save vue
npm i -g @vue/cli
npm i --save vue-router
npm i --save vuex
npm install vue-star-rating@next
```


## starting the server
### backend (python)
```
python manage.py runsever
```
### frontend (node)
```
npm run serve
```

## syncing backend for making changes to database
```
python manage.py makemigrations
python manage.py migrate
```