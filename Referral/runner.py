"""
Runner file
"""

from behave import __main__ as runner

if __name__ == "__main__":
    runner.main('./features/ '
                '-f allure_behave.formatter:AllureFormatter '
                '-o reports --no-capture --no-skipped --no-capture-stderr -f plain '                
                '--tags=api_test')

