from http import HTTPStatus

from ninja import NinjaAPI, Router

from authentication.auth import jwt_bearer_auth

api = NinjaAPI(
    auth=jwt_bearer_auth,
    title='Backoffice API',
    version='1.0.0',
    description="""
API de lista de desejos para e-commerce.

## Como testar

Use as credenciais abaixo para autenticar:

| campo | valor |
|-------|-------|
| email | recrutador@teste.com |
| senha | recte123 |

**Passo a passo:**
1. Faça POST /api/auth/token com as credenciais acima
2. Copie o access_token retornado
3. Clique em **Authorize** 🔒 Ao lado
4. Cole o token no campo **Value** e clique em Authorize
5. Explore os endpoints à vontade!
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
