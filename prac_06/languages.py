from prac_06.programming_language import ProgrammingLanguage


def main():
    """Start the program"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    all_languages = [ruby, python, visual_basic]
    print("The Dynamically typed languages are:")
    for language in all_languages:
        if language.is_dynamic():
            print(language.name)


main()
