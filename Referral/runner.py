"""
Runner file with execution configurations
"""

from behave import __main__ as runner

if __name__ == "__main__":
    runner.main('-f allure_behave.formatter:AllureFormatter '
                '-o reports '
                './features/ '
                '--tags=test')
