// 对于get请求大致写法如下
// 获得的res就是返回的结果值可以直接进行赋值处理
this.$axios.get("http://127.0.0.1:8080/api/adversarial_attack/1",{
})
.then(function(res){
    //console.log(res)          
})
.catch(function(err){
     console.log("请求失败233");
});

// 对于POST请求大致写法如下
// 获得的res就是返回的结果值可以直接进行赋值处理
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

// 具体返回的格式
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