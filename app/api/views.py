from django.shortcuts import render
from django.http import JsonResponse
import pickle
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.




@api_view(['GET', 'POST'])
def sneaker_predict(request):
    if request.method == "GET":
        return Response({'message': 'Sneaker quality prediction API is working!'}, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        # Accessing the form data
       
        product_id = request.POST.get('product_id')
        review_text = request.POST.get('review_text')
        print(f"product_id: {product_id}, review_text: {review_text}")

    with open('model/LogisticR_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

        X = [product_id, review_text]
        Y = model.predict(X)

    return Response({'prediction' : request.Y})
    #return Response({'data': request.data})