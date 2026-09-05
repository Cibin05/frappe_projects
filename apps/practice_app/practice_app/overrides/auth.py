import frappe
import jwt

SECRET_KEY = "my-secret-key"


def validate_custom_jwt():

    authorization = frappe.request.headers.get("Authorization")

    
    if not authorization:
        return

   
    if not authorization.startswith("Bearer "):
        return

    
    token = authorization.split(" ", 1)[1]

    try:
        
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        
        user = payload.get("user")

        if not user:
            return
        frappe.set_user(user)

    except jwt.InvalidTokenError:
        return