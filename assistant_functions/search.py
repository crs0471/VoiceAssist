import webbrowser

def search(*args, **kwargs):
    text = kwargs.get('text', None)
    text = text.lower() if text else None
    temp_1 = text.split('search') if text else None

    url = None
    
    # social 
    if 'whatsapp' in text:
        url = 'https://web.whatsapp.com/'
    
    elif 'instagram' in text:
        url = 'https://www.instagram.com/'

    elif 'telegram' in text:
        url = 'https://web.telegram.org/a/'

    # entertainment
    elif 'hot star' in text:
        url = 'https://www.hotstar.com/in'

    elif 'mx player' in text:
        url = 'https://www.mxplayer.in/'

    elif 'netflix' in text:
        url = 'https://www.netflix.com/in/'

    # music and media
    elif 'spotify' in text:
        temp_2 = temp_1[1].split('on spotify') if len(temp_1) > 1 else None
        search_q = temp_2[0] if temp_2 else None
        url = f'https://open.spotify.com/search/{search_q}'

    elif 'youtube' in text:
        temp_2 = temp_1[1].split('on youtube') if len(temp_1) > 1 else None
        search_q = temp_2[0] if temp_2 else None
        url = f'https://www.youtube.com/results?search_query={search_q}'
    
    
    if url:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(r"C:\Program Files\Google\Chrome\Application\chrome.exe"))
        webbrowser.get('chrome').open(url)
        return "Sure sir, Opening"
    