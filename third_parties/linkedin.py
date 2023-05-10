import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profiles 
    """

    PROXYCURL_API_KEY = ''

    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    header_dic = {'Authorization': 'Bearer ' + PROXYCURL_API_KEY}
    params = {
        'url': linkedin_profile_url,
    }

    response = requests.get(api_endpoint,
                            params=params,
                            headers=header_dic)
    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "similarly_named_profiles", "activities"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    
    return data