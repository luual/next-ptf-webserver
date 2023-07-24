# from flask import Blueprint
# from src.grql.schemas import schema

# stock_route = Blueprint('Stock', __name__)

# @stock_route.route("/stocks")
# def get_stocks():
#     query = '''
#     query {
#         allStock {
#             id, 
#             symbol, 
#             description,
#             currency,
#             figi,
#             mic
#         }
#     }
# '''
#     result = schema.execute(query)
#     return result.data['allStock']