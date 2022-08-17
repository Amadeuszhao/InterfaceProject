from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=1000000000000000000,blank=False, default='')
    published = models.BooleanField(default=False)

class AdversarialAttack(models.Model):
    iter = models.CharField(max_length=30,blank=False,default='40')
    epsilon = models.CharField(max_length=60,blank=False,default='0.3' )
    image_class = models.CharField(max_length=60,blank=False,default='candle' )
    attack_method = models.CharField(max_length=70,blank=False,default='pgd')
    image = models.CharField(max_length=1000000000000000000,blank=False, default='')
    perturbation = models.CharField(max_length=1000000000000000000,blank=False, default='')
    attack_image = models.CharField(max_length=1000000000000000000,blank=False, default='')
    attack_class = models.CharField(max_length=60,blank=False,default='candle' )
    perturbation_class = models.CharField(max_length=60,blank=False,default='candle' )

class BackdoorAttack(models.Model):
    image_class = models.CharField(max_length=60,blank=False,default='candle' )
    attack_method = models.CharField(max_length=70,blank=False,default='pgd')
    image = models.CharField(max_length=1000000000000000000,blank=False, default='')
    perturbation = models.CharField(max_length=1000000000000000000,blank=False, default='')
    attack_image = models.CharField(max_length=1000000000000000000,blank=False, default='')
    attack_class = models.CharField(max_length=60,blank=False,default='4' )

class TextAttack(models.Model):
    text_class = models.CharField(max_length=60,blank=False,default='candle' )
    attack_method = models.CharField(max_length=70,blank=False,default='pgd')
    text= models.CharField(max_length=1000000000000000000,blank=False, default='')
    attack_text = models.CharField(max_length=1000000000000000000,blank=False, default='')
    attack_class = models.CharField(max_length=60,blank=False,default='4' )
    dataset = models.CharField(max_length=60,blank=False,default='imdb' )
    model = models.CharField(max_length=60,blank=False,default='lstm' )

