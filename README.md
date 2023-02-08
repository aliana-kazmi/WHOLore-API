# Doctor Who Rest API
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTD0dyUwF1M7nZovb0te6lgBVJEAsZPnZT1cg&usqp=CAU">
  <source media="(prefers-color-scheme: light)" srcset="https://logos-world.net/wp-content/uploads/2020/12/Doctor-Who-Logo-2018-present.jpg">
  <img alt="Shows Doctor Who logo in light mode and dark mode." src="https://logos-world.net/wp-content/uploads/2020/12/Doctor-Who-Logo-2018-present.jpg">
</picture>

# Documentation


## Introduction
This documentation will help you get familiar with the resources of the **Doctor Who API** and show you how to make different queries, so that you can get the most out of it.

##Baisc Set-up

To use the project, clone the project by typing the following command:

```
git clone https://github.com/aliana-kazmi/Doctor-Who-API.git
```

Change the directory to backend and run the command 

```
python manage.py runserver
```

**Base URL:**

The base url contains information about all available API's resources. All requests are `GET` requests and go over `https`. All responses will return data in `json`.
```
GET 
```

```
{
        'Doctors':'http://127.0.0.1:3000/characters/doctors/',
        'Companions':'http://127.0.0.1:3000/characters/companions/',
        'Villains':'http://127.0.0.1:3000/characters/villains/',
        'Alien Race':'http://127.0.0.1:3000/characters/alien-races/', 
        'Gadgets':'http://127.0.0.1:3000/gadgets/',  
        'Serials':'http://127.0.0.1:3000/serials/',
        'Episodes':'http://127.0.0.1:3000/episodes/'
}
```
## Currently available resources
**Doctors**: Used to get all the doctors

**Companions**: Used to get all companions

**Writers**: Used to get all writers on the show

**Gadgets**:Used to get all the gadgets used by the Doctor

**Serials**:Used to get all serials of the show Doctor Who

**Allies**:Used to get all allies of Doctor Who

