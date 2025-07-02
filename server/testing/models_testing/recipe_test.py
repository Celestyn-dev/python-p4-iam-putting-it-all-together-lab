from app import app
from models import db, Recipe, User

class TestRecipe:
    def test_has_attributes(self):
        '''has attributes title, instructions, and minutes_to_complete.'''
        with app.app_context():
            # Clean up
            Recipe.query.delete()
            User.query.delete()
            db.session.commit()

            # Create a user first (corrected password handling)
            user = User(username="testuser")
            user.password_hash = "password123"  # ✅ Use the setter
            db.session.add(user)
            db.session.commit()

            # Create a recipe for that user
            recipe = Recipe(
                title="Delicious Shed Ham",
                instructions="Or kind rest bred with am shed then. In raptures building an bringing be. Elderly is detract tedious assured private so to visited. Do travelling companions contrasted it. Mistress strongly remember up to. Ham him compass you proceed calling detract. Better of always missed we person mr. September smallness northward situation few her certainty something.",
                minutes_to_complete=60,
                user_id=user.id
            )

            db.session.add(recipe)
            db.session.commit()

            new_recipe = Recipe.query.filter_by(title="Delicious Shed Ham").first()

            assert new_recipe.title == "Delicious Shed Ham"
            assert new_recipe.minutes_to_complete == 60
            assert new_recipe.user_id == user.id
