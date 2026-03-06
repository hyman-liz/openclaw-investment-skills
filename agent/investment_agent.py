import asyncio
from openclaw_sdk import OpenClawClient, AgentConfig

from skills.macro_policy_skill import analyze_macro
from skills.futures_supply_demand_skill import analyze_futures
from skills.stock_multifactor_skill import select_stocks
from skills.market_sentiment_skill import analyze_sentiment
from skills.portfolio_optimizer_skill import optimize_portfolio


async def main():

    async with await OpenClawClient.connect() as client:

        agent = await client.create_agent(
            AgentConfig(
                agent_id="investment-agent",
                system_prompt="""
You are a hedge fund level AI investment agent.

You must:

1 analyze macro policy
2 analyze futures supply demand
3 run stock multifactor model
4 analyze market sentiment
5 optimize portfolio

Return structured investment report.
"""
            )
        )

        result = await agent.execute(
            "Generate today's investment analysis report."
        )

        print(result.content)

asyncio.run(main())
