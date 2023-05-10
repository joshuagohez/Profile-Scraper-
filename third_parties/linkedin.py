import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profiles 
    """

    PROXYCURL_API_KEY = os.environ.get('PROXYCURL_API_KEY')

    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    header_dic = {'Authorization': 'Bearer ' + PROXYCURL_API_KEY}
    params = {
        'url': linkedin_profile_url,
    }

    response = requests.get(api_endpoint,
                            params=params,
                            headers=header_dic)
    data = response.json()
    print(data)

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["volunteer_work", "public_identifier", "country_full_name", "country", "last_name", "first_name", "certifications", "connections", "follower_count", "background_cover_image_url", "languages", "people_also_viewed", "similarly_named_profiles", "activities", "accomplishment_projects", "social_networking_services", "similarly_named_profiles", "certifications", "languages"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    
    return data