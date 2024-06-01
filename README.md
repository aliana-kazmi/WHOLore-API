# Doctor Who Rest API
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTD0dyUwF1M7nZovb0te6lgBVJEAsZPnZT1cg&usqp=CAU">
  <source media="(prefers-color-scheme: light)" srcset="https://logos-world.net/wp-content/uploads/2020/12/Doctor-Who-Logo-2018-present.jpg">
  <img alt="Shows Doctor Who logo in light mode and dark mode." src="https://logos-world.net/wp-content/uploads/2020/12/Doctor-Who-Logo-2018-present.jpg">
</picture>

# Documentation


## Introduction
This documentation will help you get familiar with the resources of the **Doctor Who API** and show you how to make different queries, so that you can get the most out of it.

## Baisc Set-up

To use the project, clone the project by typing the following command:

```
git clone https://github.com/aliana-kazmi/Doctor-Who-API.git
```

Change the directory to app and run the command 

```
python manage.py runserver
```

## Currently available resources

**Doctors Endpoint:**
- Purpose: Retrieve information about all doctors featured in Doctor Who.
- Usage:
  - /api/characters/doctors
  - /api/characters/doctors/{doctor-number}
- Response Format: JSON
- Example: GET /api/characters/doctors returns a list of all doctors with their respective details.

**Companions Endpoint:**
- Purpose: Access information about all companions featured in Doctor Who.
- Usage:
  - /api/characters/companions
  - /api/characters/companions/{companion-id}
- Response Format: JSON
- Example: GET /api/characters/companions provides a list of all companions and their relevant details.

**Villains Endpoint:**
- Purpose: Access information about all villains featured in Doctor Who.
- Usage:
  - /api/characters/villains
  - /api/characters/villains/{villain-id}
- Response Format: JSON
- Example: GET /api/characters/villains provides a list of all villains and their relevant details.

**Alien Races Endpoint:**
- Purpose: Retrieve information about all alien races associated with the character Doctor Who.
- Usage:
  - api/characters/alien-races
  - api/characters/alien-races/{alien-race-id}
- Response Format: JSON
- Example: GET api/characters/alien-races/ provides a list of alien races featured in the Doctor Who series

**Gadgets Endpoint:**
- Purpose: Retrieve information about all gadgets used by the Doctor in the series.
- Usage:
  - /api/gadgets
  - /api/gadgets/{gadget-id}
- Response Format: JSON
- Example: GET /api/gadgets provides a comprehensive list of gadgets featured in Doctor Who.

**Serials Endpoint:**
- Purpose: Access details about all serials (episodes) of the Doctor Who series.
- Usage:
  - /api/serials
  - /api/serials/{serial-number}
- Response Format: JSON
- Example: GET /api/serials returns a list of all serials along with relevant information.

**Episodes Endpoint:**
- Purpose: Access details about all episodes of the Doctor Who series.
- Usage:
  - /api/episodes
  - /api/episodes/{episodes-number}
- Response Format: JSON
- Example: GET /api/writers returns details about writers who contributed to the show.



