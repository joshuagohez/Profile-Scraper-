import os
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile 
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import (
    PersonIntel,
    person_intel_parser
)

def ice_break(name: str) -> Tuple[PersonIntel, str]:
    linkedin_profile_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url = linkedin_profile_url )


    summary_template = """
        given the information {linkedin_information} about a person, I want you to create:
        1. a short summary
        2. two interesting facts about them
        3. a topic that may interest them
        4. 2 creative ice breakers to open a conversation with them
        \n{format_instructions}
    """

    os.environ.get["OPENAI_API_KEY"] = ""

    summary_prompt_template = PromptTemplate(
        template=summary_template,
        input_variables=["linkedin_information"],
        partial_variables={"format_instructions": person_intel_parser.get_format_instructions()}
    )

    llm = ChatOpenAI(
        temperature=0, 
        model_name="gpt-3.5-turbo"
    )

    chain = LLMChain(
        llm=llm, 
        prompt=summary_prompt_template
    )

    res = chain.run(linkedin_information=linkedin_data)

    return person_intel_parser.parse(res), linkedin_data.get("profile_pic_url")

if __name__ == "__main__":
    print("running Langchain")
    res = ice_break(name="Joshua Goh")
    print(res)

    

 