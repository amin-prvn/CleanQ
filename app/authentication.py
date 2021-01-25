from functools import wraps
import datetime
import jwt
import os


class Auth():

    @staticmethod
    def generate_token(id, model):

        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'id': user_id,
            'model': model
        }
        jwt_token = jwt.encode(
            payload,
            'password', 
            'HS256'
        )
        return {
            'token': str(jwt_token)
        }


    @staticmethod
    def auth_required(func):

        @wraps(func)
        def decorated_auth(request:Request, *args, **kwargs):

            if 'token' not in request.headers:
                return JSONResponse(
                    content=jsonable_encoder({'error': 'Authentication token is not available, please login to get one'}),
                    status_code=400,
                    media_type="application/json"
                )
            token = request.headers.get('token')
            data = Auth.decode_token(token)
            if data['error']:
                return JSONResponse(
                    media_type="application/json",
                    content=jsonable_encoder(data['error']),
                    status_code=400
                )
                
            user_id = data['data']['user_id']
            from .models import User
            check_user = User.get_user(user_id)
            if not check_user:
                return JSONResponse(
                    media_type="application/json",
                    content=jsonable_encoder({'error': 'user does not exist, invalid token'}),
                    status_code=400
                )
            request.state.user = user_id
            return func(request, *args, **kwargs)
        return decorated_auth
  

    @staticmethod
    def decode_token(token: str):

        re = {'data': {}, 'error': {}}
        try:
            print(token)
            payload = jwt.decode(jwt=token, key='amin123', algorithms='HS256')
            re['data'] = {'user_id': payload['sub']}
            return re
        except jwt.ExpiredSignatureError:
            re['error'] = {'message': 'token expired, please login again'}
            return re
        except jwt.InvalidTokenError:
            re['error'] = {'message': 'Invalid token, please try again with a new token'}
            return re
            
