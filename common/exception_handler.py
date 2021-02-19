from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)
    if isinstance(exc, AuthenticationFailed):
        
        response.data = {
            'message': 'Authentication failed',
            'errors': ['Sesión no autorizada o ha caducado'],
            'exception': str(exc)
            
        }
        response.status_code = 401

    if response is not None:
        data = response.data
        response.data = {}
        errors = []

        try:
            for field, value in data.items():
                errors.append('{}'.format(''.join(value)))
        except Exception as e:
            for value in data:
                errors.append('{}'.format(''.join(value)))

        response.data['message'] = 'Bad request'
        response.data['errors'] = errors
        response.data['exception'] = str(exc)

    return response
