from ninja import NinjaAPI


api = NinjaAPI()

api.add_router('/products/', 'product_type.api.router')
api.add_router('/categories/', 'category.api.router')
api.add_router('/attributes/', 'attributes.api.router')
