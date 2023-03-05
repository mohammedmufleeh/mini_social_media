# Mini Social Media Project

This is a social media web application built with Django that allows users to upload photos with captions, view other users' photos, and add comments to photos.

## Installation

1. Clone the repository to your local machine:

```bash
  https://github.com/mohammedmufleeh/mini_social_media.git
```

2. Install the required dependencies:

```bash
  pip install django
```
3.Create a new PostgreSQL database for the project.

4.Set the database configuration in the settings.py file.

5.Run the migrations:


```bash
  python manage.py migrate

```
6. Create a new superuser account:

```bash
  python manage.py createsuperuser

```
7.Start the development server:
```bash
  python manage.py runserver


```
# Usage

User Authentication

Users can register for a new account by clicking the "Register" link on the login page. After registering, users can log in using their email address and password.

## Photo Upload

To upload a new photo, users can click the "New Photo" button on the home page and fill out the form with the photo file and caption. After submitting the form, the photo will be added to the home page.

## Viewing Photos

All photos uploaded by all users can be viewed on the home page. Each photo is displayed in a Bootstrap card element with the photo file, caption, and author's username.

## Adding Comments

To add a comment to a photo, users can click the "Add Comment" button on the photo detail page and fill out the comment form with their name and comment. After submitting the form, the comment will be added to the photo detail page.


```

