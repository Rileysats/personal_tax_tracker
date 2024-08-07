from Storage import Storage
from Asset import Asset
from Deduction import Deduction
from logger import logger

import inquirer
import argparse

questions = [
    inquirer.List(
        "action",
        message="Action?",
        choices=["Sell Asset", "Buy Asset", "Add Interest", "Add Dividend" ,"Add Deduction", "View Deductions", "View Assets"]
    )
]


# TODO: implement test mode
def main(test_mode: bool):
    if test_mode:
        logger.info("IN TEST MODE")
        
    answers = inquirer.prompt(questions)

    logger.info(f"Action picked: {answers['action']}")

    match answers["action"]:
        case "Sell Asset" | "Buy Asset" | "Add Interest" | "Add Dividend" | "View Assets":
            asset = Asset()

            if answers["action"] == "View Assets": asset.view_asset()
            else: asset.asset_update(answers["action"])

        case "Add Deduction" | "View Deductions":
            deduction = Deduction()

            if answers["action"] == "Add Deduction": deduction.add_deduction()
            if answers["action"] == "View Deductions": deduction.view_deductions()


if __name__ == "__main__":
    logger.info("Starting app")
    
    parser = argparse.ArgumentParser(description="Tax App")
    parser.add_argument("--test", action="store_true")

    args = parser.parse_args()

    main(args.test)