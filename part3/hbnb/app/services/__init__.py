from app.services.facade import HBnBFacade

facade = HBnBFacade() 

admin_email = "admin@example.com"
if not facade.get_user_by_email(admin_email):
    facade.create_user({
        "first_name": "Admin",
        "last_name": "User",
        "email": admin_email,
        "password": "admin123",
        "is_admin": True
    })