# Profile-Scraper-
A generative ai application that crawls Linkedin data about a person and customises an icebreaker message directed to them via a LLM.

## Description
Invested into the ideation of this application to better understand the intricacies of langchain's agents and custom tools while familiarising with the concept of chaining. The agent uses a custom tool built that takes in a query prompt and utilises Google's SerpAPI to retrieve the respective LinkedIn URL. Subsequently with the help of ProxyURL, the URL is utilised for crawling the required data. In summary this application utilises the langchain framework built around LLMs with flask for a quick serverside backend and HTML/CSS for a simple frontend.

## Demo Screenshots

## Getting Started

### Dependencies

* Ensure LTS python version is installed

### Installing

`pip3 install langchain flask openai google-search-results`
* Ensure the appropriate API keys and relevant information are feed into the .env file

### Executing program

* How to run the program
```
python3 app.py
```
open `http://127.0.0.1:5000` in browser once successfully run in local

## Version History

* 1.0
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

* [Project ideation (LangChain- Develop LLM powered applications with LangChain)](https://www.udemy.com/course/langchain/)
* [Langchain documentation](https://python.langchain.com/en/latest/index.html)
* [Flask documentation](https://flask.palletsprojects.com/en/2.3.x/)
* [OpenAI API documentation](https://platform.openai.com/docs/introduction)
