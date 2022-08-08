from PIL import Image
from torchvision import models
import torch
import json
import torch.nn as nn
import torchvision
import base64
use_cuda = True
device = torch.device("cuda" if use_cuda else "cpu")
import torchvision.transforms as transforms
model = models.inception_v3(pretrained=True).to(device)
model.eval()
class_idx = json.load(open("./data/imagenet_class_index.json"))
idx2label = [class_idx[str(k)][1] for k in range(len(class_idx))]

def get_base64_image(base64_data,img_name):
    with open(img_name,'wb') as file:
        img = base64.b64decode(base64_data)
        file.write(img)
        
def encode_base64(file):
    with open(file,'rb') as f:
        img_data = f.read()
        base64_data = base64.b64encode(img_data)
        return base64_data    

def predict_class(img_name):
    transform = transforms.Compose([
    transforms.Resize((299, 299)),
    transforms.ToTensor(), # ToTensor : [0, 255] -> [0, 1]
])
    images = Image.open(img_name)
    images = images.convert('RGB')
    images = transform(images)
    images = images.to(device)
    images = images.unsqueeze(0)
    outputs = model(images)
    _, pre = torch.max(outputs.data, 1)
    return pre.cpu(), [idx2label[i] for i in pre][0]

# PGD Attack
# MNIST init
def pgd_attack(labels, img_name,save_path, eps=0.3, alpha=2/255, iters=40, ) :
    transform = transforms.Compose([
    transforms.Resize((299, 299)),
    transforms.ToTensor(), # ToTensor : [0, 255] -> [0, 1]
])
    images = Image.open(img_name)
    images = images.convert('RGB')
    images = transform(images)
    images = images.unsqueeze(0)
    images = images.to(device)
    loss = nn.CrossEntropyLoss()
        
    ori_images = images.data
        
    images.requires_grad = True
    outputs = model(images)
    labels = labels.to(device)
    model.zero_grad()
    cost = loss(outputs, labels).to(device)
    cost.backward()

    adv_images = images + alpha*images.grad.sign()
    eta = torch.clamp(adv_images - ori_images, min=-eps, max=eps)
    images = torch.clamp(ori_images + eta, min=0, max=1).detach_()
    outputs = model(images)
    perturbation = images - ori_images
    per_outputs = model(perturbation)
    _ , per_pre = torch.max(per_outputs.data, 1)
    _, pre = torch.max(outputs.data, 1)

    category = [idx2label[i] for i in pre][0]
    per = [idx2label[i] for i in per_pre][0]
    torchvision.utils.save_image(images.cpu().data,save_path)
    torchvision.utils.save_image(perturbation.cpu().data,save_path.replace('attack','perturbation'),normalize=True)

    return category,per
