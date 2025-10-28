import re

def is_valid_email(email):
        # Improved regex supporting multiple domain extensions
    pattern = r'^[\w\.-]+@[\w\.-]+\.(com|org|net|edu)$'
        #only accepts .com extension (fails to acknowledge other domains) 
    #pattern = r'^[\w\.-]+@[\w\.-]+\.com$'
    #pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None
