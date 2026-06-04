from http import HTTPStatus

from ninja import NinjaAPI, Router

from authentication.auth import jwt_bearer_auth

api = NinjaAPI(
    auth=jwt_bearer_auth,
    description="""
 - Para authenticar utilize usuario 'teste01' senha '1api234@'
   no endpoint authentication/login
 - Copie e cole o token no botão 'Authorize' ao lado ->
""",
)
router = Router()


api.add_router('', router)
api.add_router('/authentication/', 'authentication.api.router')
api.add_router('/products/', 'product_type.api.router')
api.add_router('/categories/', 'category.api.router')
api.add_router('/attributes/', 'attributes.api.router')


@router.get('healthcheck', auth=None)
def healthcheck(request):
    return HTTPStatus.OK
