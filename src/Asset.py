import inquirer
import contants

from logger import logger
from Storage import Storage
from datetime import datetime

class Asset():
    def __init__(self) -> None:
        self.storage = Storage()

    def view_asset(self):
        pass

    def asset_update(self, type: str):
        ans = self.get_asset_dets()

        match type:
            case "Sell Asset":
                self.sell_asset(ans)
            case "Buy Asset":
                self.buy_asset(ans)
            case "Add Interest":
                self.add_interest()
            case "Add Dividend":
                self.add_dividend()

    # TODO: fix repeated code
    def buy_asset(self, ans):
        self.storage.write_record(contants.INSERT_INTO_ASSETS, 
                                (
                                    datetime.now().strftime("%Y-%m-%d"),
                                    "Buy",
                                    ans["description"],
                                    ans["ticker"],
                                    ans["value"],
                                    ans["currency"]
                                ),
                                "assets"
                                )

    def sell_asset(self, ans):
        self.storage.write_record(contants.INSERT_INTO_ASSETS, 
                                (
                                    datetime.now().strftime("%Y-%m-%d"),
                                    "Sell",
                                    ans["description"],
                                    ans["ticker"],
                                    ans["value"],
                                    ans["currency"]
                                ),
                                "assets"
                                )

    def add_interest(self, ans):
        self.storage.write_record(contants.INSERT_INTO_ASSETS, 
                                (
                                    datetime.now().strftime("%Y-%m-%d"),
                                    "Interest",
                                    ans["description"],
                                    ans["ticker"],
                                    ans["value"],
                                    ans["currency"]
                                ),
                                "assets"
                                )

    def add_dividend(self, ans):
        self.storage.write_record(contants.INSERT_INTO_ASSETS, 
                                (
                                    datetime.now().strftime("%Y-%m-%d"),
                                    "Dividend",
                                    ans["description"],
                                    ans["ticker"],
                                    ans["value"],
                                    ans["currency"]
                                ),
                                "assets"
                                )

    def get_asset_dets(self):
        questions = [
            inquirer.Text('value', message="What was the value? (Note: brokerage is incl. in purchse)"),
            inquirer.Text('ticker', message="What is the ticker? (If it is not a stock/crypto enter NA)"),
            inquirer.List(
                "currency",
                message="Currency",
                choices=["USD", "AUD"]
            ),
            inquirer.Text('description', message="Short description")
        ]

        answers = inquirer.prompt(questions)
    
        # Logging all details for tracking purposes
        logger.info(f"value: {answers['value']}")
        logger.info(f"ticker: {answers['ticker']}")
        logger.info(f"currency: {answers['currency']}")
        logger.info(f"description: {answers['description']}")

        return answers
    