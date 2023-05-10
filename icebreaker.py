import os
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile 
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

information = """
Mr. Lim Hua Min is the Executive Chairman of PhillipCapital Group of Companies and was also appointed Chairman of IFS Capital Limited on 20 May 2003. He began his career holding senior positions in the Stock Exchange of Singapore and the Securities Research Institute. He has served on a number of committees and sub-committees of the Stock Exchange of Singapore. In 1997, he was appointed Chairman of the Stock Exchange of Singapore (SES) Review Committee, which is responsible for devising a conceptual framework to make Singapore’s capital markets more globalised, competitive and robust. For this service, he was awarded the Public Service Medal (PBM) in 1999 by the Singapore Government. In 2014, he was also awarded “IBF Distinguished Fellow" (Securities & Futures), the highest certification mark bestowed by The Institute of Banking and Finance on industry captains who are the epitome of professional stature, integrity and achievement. In 2018, he was named Businessman of the Year 2017 at the annual Singapore Business Awards, which is Singapore’s most prestigious business accolade.

He served as a board member in the Inland Revenue Authority Singapore from 2004 to 2010. He was Chairman and Elder of Covenant Evangelical Free Church, Singapore for a number of years.

Mr. Lim holds a Bachelor of Science Degree (Honours) in Chemical Engineering from the University of Surrey and obtained a Master’s Degree in Operations Research and Management Studies from Imperial College, London University.
"""

if __name__ == "__main__":
    print("running Langchain")

    linkedin_profile_url = linkedin_lookup_agent(name="Joshua Goh")

    summary_template = """
        given the information {information} about a person, I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    os.environ.get["OPENAI_API_KEY"] = ""

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], 
        template=summary_template
    )

    llm = ChatOpenAI(
        temperature=0, 
        model_name="gpt-3.5-turbo"
    )

    chain = LLMChain(
        llm=llm, 
        prompt=summary_prompt_template
    )

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url = linkedin_profile_url )

    print(chain.run(information=linkedin_data))

