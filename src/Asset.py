import inquirer
import constants

from logger import logger
from Storage import Storage
from datetime import datetime

class Asset():
    def __init__(self) -> None:
        self.storage = Storage()

    def view_asset(self):
        pass

    def asset_update(self, type: str):

        match type:
            case "Sell Asset" | "Buy Asset":
                ans = self.get_asset_dets()

                {
                    "Sell Asset": self.sell_asset,
                    "Buy Asset": self.buy_asset
                }
                [type](ans)
               
            case "Add Interest":
                ans = self.get_interest_dets()
                self.add_interest(ans)
                
            case "Add Dividend":
                ans = self.get_divident_dets()
                self.add_dividend(ans)

    # TODO: fix repeated code
    def buy_asset(self, ans):
        self.storage.write_record(
                                query=constants.INSERT_INTO_ASSETS, 
                                data=(
                                    datetime.now().strftime("%Y-%m-%d"),
                                    "Buy",
                                    ans["description"],
                                    ans["ticker"],
                                    ans["value"],
                                    ans["currency"]
                                ),
                                table_name="assets"
                                )

    def sell_asset(self, ans):
        self.storage.write_record(
                                query=constants.INSERT_INTO_ASSETS, 
                                data=(
                                    datetime.now().strftime("%Y-%m-%d"),
                                    "Sell",
                                    ans["description"],
                                    ans["ticker"],
                                    ans["value"],
                                    ans["currency"]
                                ),
                                table_name="assets"
                                )

    def add_interest(self, ans):
        self.storage.write_record(
                                query=constants.INSERT_INTO_ASSETS, 
                                data=(
                                    datetime.now().strftime("%Y-%m-%d"),
                                    "Interest",
                                    f"{ans["source"]} interest",
                                    ans["source"],
                                    ans["value"],
                                    ans["currency"]
                                ),
                                table_name="assets"
                                )

    def add_dividend(self, ans):
        self.storage.write_record(
                                query=constants.INSERT_INTO_ASSETS, 
                                data=(
                                    datetime.now().strftime("%Y-%m-%d"),
                                    "Dividend",
                                    f"{ans["ticker"]} dividend",
                                    ans["ticker"],
                                    ans["value"],
                                    ans["currency"]
                                ),
                                table_name="assets"
                                )

    # TODO: combine below funcs
    def get_asset_dets(self):
        questions = [
            inquirer.Text('value', message="Value of trade? (incl. brokerage in purchase)"),
            inquirer.Text('ticker', message="What is the ticker? (if not stock/crypto use NA)"),
            inquirer.List(
                "currency",
                message="Currency",
                choices=["USD", "AUD"]
            ),
            inquirer.Text('description', message="Short description")
        ]

        answers = inquirer.prompt(questions)
    
        logger.info("Asset sale entry values below ->")
        logger.info(f"value: {answers['value']}")
        logger.info(f"ticker: {answers['ticker']}")
        logger.info(f"currency: {answers['currency']}")
        logger.info(f"description: {answers['description']}")

        return answers
    
    def get_dividend_dets(self):
        questions = [
            inquirer.Text('value', message="Dividend amount?"),
            inquirer.Text('ticker', message="What is the stock ticker?"),
            inquirer.List(
                "currency",
                message="Currency",
                choices=["USD", "AUD"]
            )
        ]

        answers = inquirer.prompt(questions)
    
        logger.info("Dividend entry values below ->")
        logger.info(f"value: {answers['value']}")
        logger.info(f"ticker: {answers['ticker']}")
        logger.info(f"currency: {answers['currency']}")

        return answers

    def get_interest_dets(self):
        questions = [
            inquirer.Text('value', message="Interest amount?"),
            inquirer.Text('source', message="What is the interest source? (CommBank, Vanguard etc)"),
            inquirer.List(
                "currency",
                message="Currency",
                choices=["USD", "AUD"]
            )
        ]

        answers = inquirer.prompt(questions)
    
        logger.info("Interest entry value below ->")
        logger.info(f"value: {answers['value']}")
        logger.info(f"source: {answers['source']}")
        logger.info(f"currency: {answers['currency']}")

        return answers
    