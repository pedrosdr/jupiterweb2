from app import login_manager
from app.models.user import User

@login_manager.user_loader
def load_user(id):
    return User.new()