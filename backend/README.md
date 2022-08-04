# Django Restful API Backend
## 运行代码
```python
python manage.py runserver 8080
```
## Basic address
将上述的127.0.0.1:8080替换为https://f3d9-219-74-123-206.ap.ngrok.io
如https://f3d9-219-74-123-206.ap.ngrok.io/api/adversarial_attack/1
## demo
- 对于get请求大致写法如下
- 获得的res就是返回的结果值可以直接进行赋值处理
```
this.$axios.get("http://127.0.0.1:8080/api/adversarial_attack/1",{
})
.then(function(res){
    //console.log(res)          
})
.catch(function(err){
     console.log("请求失败233");
});
```
- 对于POST请求大致写法如下
- 后面的字典指的是POST请求发送的信息,如果你需要上传新的图片获取新的attack image采用该请求
- 获得的res就是返回的结果值可以直接进行赋值处理
```
this.$axios.post("http://127.0.0.1:8080/api/adversarial_attack",{"image":"这里填写你上传图片的base64格式",
                                                                "epsilon":0.3, // pgd attack epsilon参数,可写可不写
                                                                "iter":20, //pgd attack iter参数,可写可不写
                                                            })//传参 只需要传上面三个参数即可
.then(function(res){
      console.log(res)          
})
.catch(function(err){
      console.log("请求失败233");
});
```
## adversarial_attack
- 具体返回的格式
- GET请求 http://127.0.0.1:8080/api/adversarial_attack 获取全部的数据
- POST请求 http://127.0.0.1:8080/api/adversarial_attack 上传新的需要attackimage以及对应的参数,其中image参数必须用base64格式填写,剩余可不写
- GET请求 http://127.0.0.1:8080/api/adversarial_attack/1 获取id=1数据的

```
        fields = ('id', //"id" 
                  'iter', //"iter pgd attack iteration 设置"
                  'epsilon', //"epsilon"
                  'image_class', //原本的image_class
                  'attack_method', //
                  'image',       // 你上传的image base64码
                  'perturbation', //生成的perturbation image base64码
                  'attack_image', //生成的attack image base64码
                  'attack_class', // 生成的attack_image 的class
                  'perturbation_class' // 生成的perturbation的class
                )
```


## backdoor attack
- 具体返回的格式
- GET请求 http://127.0.0.1:8080/api/backdoor_attack 获取全部的数据
- GET请求 http://127.0.0.1:8080/api/backdoor_attack/1 获取id=1数据的
```
        fields = ('id',
                  'image_class',
                  'attack_method',
                  'image',
                  'perturbation',
                  'attack_image',
                  'attack_class',
                )
```
## text attack
- 具体返回的格式
- GET请求 http://127.0.0.1:8080/api/text_attack 获取全部的数据
- GET请求 http://127.0.0.1:8080/api/text_attack/1 获取id=1数据的
```
        fields = ('id',
                  'text_class',
                  'attack_method',
                  'text',
                  'attack_text',
                  'attack_class',
                  'dataset',
                  'model',
                )
```