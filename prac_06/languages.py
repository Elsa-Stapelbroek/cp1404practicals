"""
Programming Languages
estimated: 30 minutes
actual: 16 minutes for main code, 22 including docstrings etc.
"""
from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
print("\n".join(language.name for language in languages if language.is_dynamic()))
