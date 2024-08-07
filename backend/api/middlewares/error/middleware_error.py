from flask import jsonify

class ValidationError(Exception):
    def __init__(self, message, fields=None):
        super().__init__(message)
        self.fields = fields or {}

class NotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)

def handle_validation_error(error):
    response = jsonify({
        'error': str(error),
        'fields': getattr(error, 'fields', {}),
        'data': None
    })
    response.status_code = 400
    return response

def handle_not_found_error(error):
    response = jsonify({
        'error': str(error),
        'data': None
    })
    response.status_code = 404
    return response

def handle_generic_error(error):
    response = jsonify({
        'error': str(error),
        'data': None
    })
    response.status_code = 500
    return response
