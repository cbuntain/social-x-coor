from urllib.parse import urlparse

def strip_video_id_from_url(url):
    '''Strips a URL from youtube to a video_id'''
    #print(url)
    
    if not isinstance(url, str):
        return None
    
    if ( "youtube.com" not in url and "youtu.be" not in url ):
        return None
    
    parsed_url = urlparse(url)
    
    video_id = None
    if (("youtube.com" in parsed_url.netloc) and ('/watch?' in url)):
        try:
            parsed_url = urlparse(url.replace("/#/", "/"))

            url_q = parsed_url.query + "&" + parsed_url.fragment
            url_q = url_q.replace("?", "&")
            url_q_arr = [x.partition("=")[-1] for x in url_q.split("&") if x.startswith("v")]
            
            if ( len(url_q_arr) > 0 ):
                video_id = url_q_arr[0]
        except:
            print(url)
            raise
        
    elif 'youtu.be' in parsed_url.netloc:
        video_id = parsed_url.path.partition("/")[-1]
   
    return video_id
