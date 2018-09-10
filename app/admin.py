class Admin():

    admin_data = []

    def __init__(self):
        self.admin_dict = {}

    def create_admin(self, email, first_name, last_name, password, confirm_password):

        admin_id = len(Admin.admin_data) + 1

        if email is None:
            return {"msg": "Please input admin email address"}
        if first_name is None:
            return {"msg": "Please input first name."}
        if last_name is None:
            return {"msg": "Please input last name."}
        if password is None:
            return {"msg": "Please input admin password."}
        if confirm_password is None:
            return {"msg": "Please confirm admin password."}

        for admin in Admin.admin_data:
            if email == admin['email']:
                return {"msg": "Account with Email already exists. Please log in."}

        if len(password) < 6:
            return {"msg": "Input a password that is at least 6 characters long."}

        if password == confirm_password:
            self.admin_dict['admin_id'] = admin_id
            self.admin_dict['first name'] = first_name
            self.admin_dict['last name'] = last_name
            self.admin_dict['email'] = email
            self.admin_dict['password'] = password
            self.admin_dict['is admin'] = True

            Admin.admin_data.append(self.admin_dict)
        else:
            return {"msg": "Passwords do not match. Try again."}
        return {'msg': 'Admin created successfully.', 'user_data': self.admin_dict}

    def login_admin(self, email, password):

        if email is None:
            return {"msg": "Please input an email address"}
        if password is None:
            return {"msg": "Please input a password."}

        for admin in Admin.admin_data:
            if email == admin['email']:
                if password == admin['password']:
                    return {"msg": "Successfully logged in!", 'user_data': self.admin_dict}
                return {"msg": "Wrong Password. Try again."}
        return {"msg": "You are not an admin for this page,please sign up."}

    def reset_password(self, email, new_password, confirm_new_password):

        if email is None:
            return {"msg": "Please input an email address"}
        if new_password is None:
            return {"msg": "Please input a new password."}
        if confirm_new_password is None:
            return {"msg": "Please confirm your new password."}

        for admin in Admin.admin_data:
            if email == admin['email']:
                if new_password == confirm_new_password:
                    self.admin_dict['password'] = new_password
                    return {"message": "Your password has been reset"}
                return {"msg": "Passwords don't match"}
        return {"msg": "You have no account, please sign up"}

