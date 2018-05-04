# -*- coding: utf-8 -*-
DB_URI = 'sqlite:///./main.db'

# define
##API_PORT = 9088

# define Flask behaviour
APP_CONFIG = {
    # return all errors for wrong requests at once
    'BUNDLE_ERRORS' : True,
    'SERVER_PORT' : 9088
}


# Define all valid request params and map them to a context
valid_request_arguments = {
    'User' : ['api'],
    'Address' : ['name', 'str_name', 'str_no', 'city', 'post_code', 'country','start_date', 'end_date'],
    'Box' : ['name', 'status', 'weight', 'size']
}