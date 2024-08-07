import inquirer
import constants

from logger import logger


class Deduction():
    def __init__(self) -> None:
        pass

    def add_deduction(self):
        print("In add deduction")
        ans = self.get_deduction_dets()

    def view_deductions(self):
        print("In view deduction")
        

    def get_deduction_dets(self):
        questions = [
            inquirer.Text("value", message="What was the value? (Note: brokerage is incl. in purchse)"),
            inquirer.List(
                "type",
                message="Type",
                choices=["Gift/Donation", "Work Expense", "Personal Super Contribution", "Cost of Managing Tax", "Other"]
            ),
            inquirer.Text("description", message="Short description")
        ]

        answers = inquirer.prompt(questions)

        # Logging all details for tracking purposes
        logger.info(f"value: {answers['value']}")
        logger.info(f"type: {answers['type']}")
        logger.info(f"description: {answers['description']}")

        return answers