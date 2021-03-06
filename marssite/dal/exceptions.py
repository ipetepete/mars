class BaseDalException(Exception):
    status_code = None
    error_message = None
    is_an_error_response = True

    def __init__(self, error_message):
        Exception.__init__(self)
        self.error_message = error_message
        
    def to_dict(self):
        return {'errorMessage': self.error_message}

class InvalidUsage(BaseDalException):
    status_code = 400


class UnknownSearchField(BaseDalException):
    status_code = 400
    

class BadTIFormat(BaseDalException):
    status_code = 400    

class BadNumeric(BaseDalException):
    status_code = 400    

class BadSearchSyntax(BaseDalException):
    status_code = 400    

class BadFakeError(BaseDalException):
    status_code = 400    

class CannotProcessContentType(BaseDalException):
    status_code = 400
    
    
