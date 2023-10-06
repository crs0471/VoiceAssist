import webbrowser
from .search import search 

class OpenApplication:
    def open_application(self, *args, **kwargs):
        text = kwargs.get('text', None)
        url = None
        
        # social 
        if 'whatsapp' in text.lower():
            url = 'https://web.whatsapp.com/'
        
        elif 'instagram' in text.lower():
            url = 'https://www.instagram.com/'

        elif 'telegram' in text.lower():
            url = 'https://web.telegram.org/a/'

        # entertainment
        elif 'hot star' in text.lower():
            url = 'https://www.hotstar.com/in'

        elif 'mx player' in text.lower():
            url = 'https://www.mxplayer.in/'

        elif 'netflix' in text.lower():
            url = 'https://www.netflix.com/in/'

        # music and media
        elif 'spotify' in text.lower():
            url = 'https://open.spotify.com/'

        elif 'youtube' in text.lower():
            if 'search' in text:
                return search(*args, **kwargs)
            url = 'https://www.youtube.com/'
        
        
        if url:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(r"C:\Program Files\Google\Chrome\Application\chrome.exe"))
            webbrowser.get('chrome').open(url)
            return "Sure sir, Opening"
    



# def open_whatsapp(*args, **kwargs):
#     pg.press('winleft')
#     type('whatsapp')
#     sleep(0.5)
#     pg.press('enter')