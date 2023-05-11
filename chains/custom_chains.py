from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from output_parsers import (
    summary_parser,
    interest_parser,
    icebreaker_parser
)

load_dotenv()

llm = ChatOpenAI(
        temperature=0, 
        model_name="gpt-3.5-turbo"
    )

llm_creative = ChatOpenAI(
        temperature=1, 
        model_name="gpt-3.5-turbo"
    )

def get_summary_chain() -> LLMChain:
    summary_template = """
        given the information {linkedin_information} about a person, I want you to create:
        1. a short summary
        2. two interesting facts about them
        \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        template=summary_template,
        input_variables=["linkedin_information"],
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        }
    )

    chain = LLMChain(
        llm = llm,
        prompt = summary_prompt_template
    )

    return chain

def get_interest_chain() -> LLMChain:
    interest_template = """
        given the information {linkedin_information} about a person, I want you to create:
        3 topics that may interest them
        \n{format_instructions}
    """

    interest_prompt_template = PromptTemplate(
        template=interest_template,
        input_variables=["linkedin_information"],
        partial_variables={
            "format_instructions": interest_parser.get_format_instructions()
        }
    )

    chain = LLMChain(
        llm = llm,
        prompt = interest_prompt_template
    )

    return chain

def get_icebreaker_chain() -> LLMChain:
    icebreaker_template = """
        given the information {linkedin_information} about a person, I want you to create:
        2 creative ice breakers to open a conversation with them, derived from their LinkedIn
        \n{format_instructions}
    """

    icebreaker_prompt_template = PromptTemplate(
        template=icebreaker_template,
        input_variables=["linkedin_information"],
        partial_variables={
            "format_instructions": icebreaker_parser.get_format_instructions()
        }
    )

    chain = LLMChain(
        llm = llm_creative,
        prompt = icebreaker_prompt_template
    )

    return chain