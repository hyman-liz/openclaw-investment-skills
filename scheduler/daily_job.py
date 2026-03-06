import schedule
import time
from agent.investment_agent import main

schedule.every().day.at("14:40").do(main)

while True:

    schedule.run_pending()
    time.sleep(60)
