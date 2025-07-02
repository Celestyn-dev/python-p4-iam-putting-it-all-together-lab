#!/usr/bin/env python3

from random import randint, choice as rc
from faker import Faker

from app import app
from models import db, Recipe, User

fake = Faker()

with app.app_context():

    print("🌱 Deleting all records...")
    Recipe.query.delete()
    User.query.delete()
    db.session.commit()

    print("👤 Creating users...")
    users = []
    usernames = []

    for i in range(20):
        username = fake.first_name()
        while username in usernames:
            username = fake.first_name()
        usernames.append(username)

        user = User(
            username=username,
            bio=fake.paragraph(nb_sentences=3),
            image_url=fake.url()
        )
        user.password_hash = username + 'password'
        users.append(user)

    db.session.add_all(users)
    db.session.commit()  # ✅ Ensure users have IDs before assigning to recipes

    print("🍽️ Creating recipes...")
    recipes = []
    for i in range(100):
        instructions = fake.paragraph(nb_sentences=8)
        recipe = Recipe(
            title=fake.sentence(),
            instructions=instructions,
            minutes_to_complete=randint(15, 90),
            user_id=rc(users).id  # ✅ Set user_id directly after users are committed
        )
        recipes.append(recipe)

    db.session.add_all(recipes)
    db.session.commit()

    print("✅ Seeding complete!")
