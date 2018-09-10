class User():

    user_data = []

    def __init__(self):
        self.user_dict = {}

    def create_user(self, first_name, last_name, email, password, confirm_password):

        user_id = len(User.user_data) + 1

        if email is None:
            return {"msg": "Please input an email address"}
        if first_name is None:
            return {"msg": "Please input first name."}
        if last_name is None:
            return {"msg": "Please input last name."}
        if password is None:
            return {"msg": "Please input a password."}
        if confirm_password is None:
            return {"msg": "Please confirm password."}

        for user in User.user_data:
            if email == user['email']:
                return {"msg": "Account with Email already exists. Please log in."}

        if len(password) < 6:
            return {"msg": "Input a password that is at least 6 characters long."}

        if password == confirm_password:
            self.user_dict['user_id'] = user_id
            self.user_dict['first name'] = first_name
            self.user_dict['last name'] = last_name
            self.user_dict['email'] = email
            self.user_dict['password'] = password
            self.user_dict['is admin'] = False

            User.user_data.append(self.user_dict)
        else:
            return {"msg": "Passwords do not match. Try again."}
        return {'msg': 'User created successfully.', 'user_data': self.user_dict}

    def login_user(self, email, password):

        if email is None:
            return {"msg": "Please input an email address"}
        if password is None:
            return {"msg": "Please input a password."}

        for user in User.user_data:
            if email == user['email']:
                if password == user['password']:
                    return {"msg": "Successfully logged in!", 'user_data': self.user_dict}
                return {"msg": "Wrong Password. Try again."}
            return {"msg": "You have no account,please sign up"}

    def reset_password(self, email, new_password, confirm_new_password):

        if email is None:
            return {"msg": "Please input an email address"}
        if new_password is None:
            return {"msg": "Please input a new password."}
        if confirm_new_password is None:
            return {"msg": "Please confirm your new password."}

        for user in User.user_data:
            if email == user['email']:
                if new_password == confirm_new_password:
                    self.user_dict['password'] = new_password
                    return {"message": "Your password has been reset"}
                return {"msg": "Passwords don't match"}
            return {"msg": "You have no account, please sign up"}

    def update_user(self, email):
        for user in User.user_data:
            if email == user['email']:
                self.user_dict['is admin'] = True
                return {"msg": "User updated"}
            return {"msg": "No such user exists"}
