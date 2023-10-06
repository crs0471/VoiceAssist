from datetime import datetime
import random
def get_greeting(*args, **kwargs):
    def get_time_greet():
        c = datetime.now()
        current_time = int(c.strftime('%H'))
        if current_time < 12:
            return 'morning'
        elif current_time < 16:
            return 'afternoon'
        else: 
            return 'evening'
    greet_list = [
        'Hello sir, How Are You.',
        f"good {get_time_greet()} sir, How have you been?",
    ]
    return random.choice(greet_list)