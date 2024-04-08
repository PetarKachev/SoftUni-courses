class EmailValidator:

    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str):
        if "@" in name:
            current_name = name.split("@")[0]
        else:
            current_name = name

        if len(current_name) >= self.min_length:
            return True
        else:
            return False

    def __is_mail_valid(self, mail: str):
        if "." and "@" in mail:
            current_mail = mail.split(".")[0]
            current_mail = current_mail.split("@")[1]
        else:
            current_mail = mail


        if current_mail in self.mails:
            return True
        return False

    def __is_domain_valid(self, domain):
        if "." in domain:
            current_domain = domain.split(".")[1]
        else:
            current_domain = domain

        if current_domain in self.domains:
            return True
        return False

    def validate(self, email):

        if self.__is_name_valid(email) and self.__is_mail_valid(email) and self.__is_domain_valid(email):
            return True
        return False