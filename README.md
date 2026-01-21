Django Flight Routes System

This project is a simple Django application that manages airport routes and performs route-based calculations.

What this project does

Each airport is stored as a node in a route with:

Airport Code

Position in the route

Duration (time)

Features

Add Airport Route

Create routes with ordered airports and durations.

Find Nth Left or Right Airport

Select an airport and find another airport N positions left or right.

Find Longest Duration Airport

Shows the airport with the maximum duration in a route.

Find Shortest Airport Between Two Airports

Finds the airport with the least duration between two selected airports.

Admin Panel

Easy route management with search, filter, and edit options.

How to Run
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

URLs

Add Route: add/

Find Nth Node: nth/

Reports: reports/

Admin: /admin/
