from  rest_framework.response import Response
from rest_framework import status
import datetime
import jwt
import os


JWT_KEY = 'password'


class Auth():
    '''
        Authentication class for create jwt token and verify it
    '''

    # Generate jwt token with user id and model = {clinic, patient}
    @staticmethod
    def generate_token(id, model):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'id': id,
            'model': model
        }
        jwt_token = jwt.encode(
            payload,
            JWT_KEY, 
            'HS256'
        )
        return {
            'token': jwt_token
        }

    # Authentication required decorator input_argument : model , return_argument : id, clinic
    @staticmethod
    def auth_required(model):
        def decorator(function):
            def wrapper(*args, **kwargs):
                request = args[1]
                if 'token' not in request.headers:
                    return Response(
                        {'error': 'Authentication token is not available, please login to get one'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                token = request.headers.get('token')
                data = Auth.decode_token(token)
                if data['error']:
                    return Response(
                        data['error'],
                        status=status.HTTP_400_BAD_REQUEST
                    )
                token_id = kwargs['id'] = data['data']['id']
                token_model = kwargs['model'] = data['data']['model']
                if token_model != model:
                    return Response(
                        {'error': 'Authentication is not valid.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                return function(*args, **kwargs)
            return wrapper
        return decorator

    # Decode given token 
    @staticmethod
    def decode_token(token: str):

        re = {'data': {}, 'error': {}}
        try:
            payload = jwt.decode(jwt=token, key=JWT_KEY, algorithms='HS256')
            re['data'] = {
                'id': payload['id'],
                'model': payload['model'] 
            }
            return re
        except jwt.ExpiredSignatureError:
            re['error'] = {'message': 'token expired, please login again'}
            return re
        except jwt.InvalidTokenError:
            re['error'] = {'message': 'Invalid token, please try again with a new token'}
            return re
            
