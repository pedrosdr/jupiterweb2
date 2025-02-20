from flask_login import UserMixin

class User(UserMixin):
    def __init__(self) -> None:
        super().__init__()
        self.id:int = None
        self.email:str = None
        self.password:str = None
        self.salt:str = None
        self.name:str = None
        self.last_name:str = None
        self.role:str = None
        self.active:str = None

    @staticmethod
    def new():
        user = User()
        user.id = 1
        user.email = "admin@admin.com"
        user.password = "password"
        user.salt = "a"
        user.name = "Admin"
        user.last_name = "Admin"
        user.role = "admin"
        user.active = True
        return user
        
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.id
        
    def __repr__(self):
        return f"User(email={self.email}, role={self.role})"