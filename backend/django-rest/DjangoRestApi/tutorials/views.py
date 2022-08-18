from email.encoders import encode_base64
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from tutorials.attack.adversarial_attack import *
from tutorials.attack.get_text import get_text

from tutorials.models import Tutorial,AdversarialAttack,TextAttack
from tutorials.serializers import *
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def adversarial_attack_generate(request):
    if request.method == 'GET':
        adversarials = AdversarialAttack.objects.all()
        
        adversarial_serializer = AdversarialAttackSerializer(adversarials, many=True)
        return JsonResponse(adversarial_serializer.data, safe=False)
    elif request.method == 'POST':
        attack = JSONParser().parse(request)
        img_data = attack['image'].replace('data:image/jpeg;base64,','')
        img_id = 'test'
        try:
            epsilon = float(attack['epsilon'])
        except:
            epsilon = 0.3
        try:
            iter = int(attack['iter'])
        except:
            iter = 40
        img_path = './data/images/'+img_id+'.png'
        attack_path = img_path.replace('images','attack')
        perturb_path = img_path.replace('images','perturbation')
        get_base64_image(img_data,img_path)
        labels, img_class = predict_class(img_path)
        attack['image_class'] = img_class
        attack_class,perturb_class = pgd_attack(labels,img_path,attack_path,eps=epsilon,alpha =2/255,iters=iter )
        attack['attack_class'] = attack_class
        attack['perturbation_class'] = perturb_class
        attack['perturbation'] = 'data:image/jpeg;base64,' + encode_base64(perturb_path).decode('utf-8')
        attack['attack_image'] = 'data:image/jpeg;base64,' + encode_base64(attack_path).decode('utf-8')
        adversarial_serializer = AdversarialAttackSerializer(data=attack)
        if adversarial_serializer.is_valid():
            adversarial_serializer.save()
            return JsonResponse(adversarial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(adversarial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def adversarial_detail(request,pk):
    try: 
        adversarials = AdversarialAttack.objects.get(pk=pk) 
    except AdversarialAttack.DoesNotExist: 
        return JsonResponse({'message': 'The image does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        adversarial_serializer = AdversarialAttackSerializer(adversarials)
        return JsonResponse(adversarial_serializer.data) 
    elif request.method == 'PUT': 
        adversarial_data = JSONParser().parse(request) 
        adversarial_serializer = AdversarialAttackSerializer(adversarials, data=adversarial_data) 
        if adversarial_serializer.is_valid(): 
            adversarial_serializer.save() 
            return JsonResponse(adversarial_serializer.data) 
        return JsonResponse(adversarial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        adversarials.delete() 
        return JsonResponse({'message': 'Adversarials was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET','POST'])
def backdoor_attack_generate(request):
    if request.method == 'GET':
        backdoors = BackdoorAttack.objects.all()
        backdoor_serializer = BackdoorAttackSerializer(backdoors, many=True)
        return JsonResponse(backdoor_serializer.data, safe=False)
    elif request.method == 'POST':
        attack = JSONParser().parse(request)
        backdoor_serializer = BackdoorAttackSerializer(data=attack)
        if backdoor_serializer.is_valid():
            backdoor_serializer.save()
            return JsonResponse(backdoor_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(backdoor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def backdoor_detail(request,pk):
    try: 
        backdoors = BackdoorAttack.objects.get(pk=pk) 
    except BackdoorAttack.DoesNotExist: 
        return JsonResponse({'message': 'The image does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        backdoor_serializer = BackdoorAttackSerializer(backdoors)
        return JsonResponse(backdoor_serializer.data) 

@api_view(['GET','POST'])
def text_attack_generate(request):
    if request.method == 'GET':
        texts = TextAttack.objects.all()
        text_serializer = TextAttackSerializer(texts, many=True)
        return JsonResponse(text_serializer.data, safe=False)
    elif request.method == 'POST':
        attack = JSONParser().parse(request)
        text_message = attack['text']
        origin_class,attack_class ,origin_sentence,attack_sentence  = get_text(text_message)
        attack["text"] = origin_sentence
        attack['attack_text'] = attack_sentence
        attack['text_class'] = origin_class
        attack['attack_class'] = attack_class
        text_serializer = TextAttackSerializer(data=attack)
        if text_serializer.is_valid():
            text_serializer.save()
            return JsonResponse(text_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(text_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def text_detail(request,pk):
    try: 
        texts = TextAttack.objects.get(pk=pk) 
    except TextAttack.DoesNotExist: 
        return JsonResponse({'message': 'The image does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        text_serializer = TextAttackSerializer(texts)
        return JsonResponse(text_serializer.data) 

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 

@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        tutorial = Tutorial.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    
