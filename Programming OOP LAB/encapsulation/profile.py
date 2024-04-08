class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):

        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        upper_case = False
        digit = False
        len_of_pass = True if len(value) >= 8 else False

        for character in value:
            if str(character).isupper():
                upper_case = True
            if str(character).isdigit():
                digit = True

        if not (upper_case and digit and len_of_pass):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {len(self.password) * "*"}'