class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, language: str, skills_earned: int):
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        return f"{self.name} does not know {language}"

    def change_language(self, new_language: str, skills_needed: int):
        if self.language != new_language and self.skills >= skills_needed:
            previous_language = self.language
            self.language = new_language
            return f"{self.name} switched from {previous_language} to {new_language}"

        elif self.language == new_language:
            return f"{self.name} already knows {self.language}"

        elif self.skills < skills_needed:
            diff = skills_needed - self.skills
            return f"{self.name} needs {diff} more skills"