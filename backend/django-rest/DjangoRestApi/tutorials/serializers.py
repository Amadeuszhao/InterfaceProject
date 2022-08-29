from rest_framework import serializers 
from tutorials.models import Tutorial, AdversarialAttack,BackdoorAttack,TextAttack,ModelVerify
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')

class AdversarialAttackSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = AdversarialAttack
        fields = ('id',
                  'iter',
                  'epsilon',
                  'image_class',
                  'attack_method',
                  'image',
                  'perturbation',
                  'attack_image',
                  'attack_class',
                  'perturbation_class'
                )

class BackdoorAttackSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = BackdoorAttack
        fields = ('id',
                  'image_class',
                  'attack_method',
                  'image',
                  'perturbation',
                  'attack_image',
                  'attack_class',
                )

class TextAttackSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = TextAttack
        fields = ('id',
                  'text_class',
                  'attack_method',
                  'text',
                  'attack_text',
                  'attack_class',
                  'dataset',
                  'model',
                )

class VerificationSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ModelVerify
        fields = ('id',
                  'model',
                  'input',
                  'auxiliary_variables',
                  'verified_output',
                  'Verified',
                  'Falsified',
                  'Time',
                  'Timeout',
                )