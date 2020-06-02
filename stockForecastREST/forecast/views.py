from django.http.response import JsonResponse


from rest_framework.decorators import api_view
from forecast.function import Bayesian_Prediction
# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def historical(request,symbol):
    #GET list of historical data, POST a new entry of historical data, DELETE all historical data
    if request.method == 'GET':
        data=Bayesian_Prediction(symbol)
        return JsonResponse(data, safe=False)
        # 'safe=False' for objects serialization