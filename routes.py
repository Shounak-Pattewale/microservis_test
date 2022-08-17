from account.services import UserLoginApi

def initialize_routes(api):
    api.add_resource(UserLoginApi, '/', endpoint='login')