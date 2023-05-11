from typing import Tuple
from third_parties.linkedin import scrape_linkedin_profile 
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import (
    Summary,
    Interest,
    IceBreaker,
    summary_parser,
    interest_parser,
    icebreaker_parser
)
from chains.custom_chains import (
    get_summary_chain,
    get_interest_chain,
    get_icebreaker_chain
)

def ice_break(name: str) -> Tuple[Summary, Interest, IceBreaker, str]:
    linkedin_profile_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url = linkedin_profile_url )

    summary_chain = get_summary_chain()
    summary_facts = summary_chain.run(linkedin_information=linkedin_data)
    summary_facts = summary_parser.parse(summary_facts)

    interest_chain = get_interest_chain()
    interests = interest_chain.run(linkedin_information=linkedin_data)
    interests = interest_parser.parse(interests)

    icebreaker_chain = get_icebreaker_chain()
    icebreakers = icebreaker_chain.run(linkedin_information=linkedin_data)
    icebreakers = icebreaker_parser.parse(icebreakers)

    # try:
    #     res = chain.run(linkedin_information=linkedin_data)
    # except ValueError as e:
    #     res = str(e)
    #     if not res.startswith("Could not parse LLM output: `"):
    #         raise e
    #     res = res.removeprefix("Could not parse LLM output: `").removesuffix("`")

    return summary_facts, interests, icebreakers, linkedin_data.get("profile_pic_url")

if __name__ == "__main__":
    pass

    

 