<template>
    <div>
        <mavon-editor
      class="md"
     :value="context"
     :subfield = "prop.subfield"
     :defaultOpen = "prop.defaultOpen"
     :toolbarsFlag = "prop.toolbarsFlag"
     :editable="prop.editable"
     :scrollStyle="prop.scrollStyle"
  ></mavon-editor>
    </div>
</template>
<script>
export default {
  data () {
    return {
      context: '# About\r\n\r\nAs neural models become commonplace across industry and society, we must continue scrutinising this emerging technology to ensure its application is in the social interest and psycho-feeling experience of all. This is the main focus of our RISE lab and is an area of our research on various fairness and computational system robustness-related topics.\r\n\r\nWe develop highly systematic tools, fundamental theories, and diverse methodologies for ensuring the runtime correctness, reliability, and efficiency of deployed software and systems, focusing on automated techniques such as artificial intelligence model checking, human-centred machine learning, and industrial program analysis. Our up-to-date research lays the targets on a number of advanced software/systems in different categories, including advanced critical infrastructure, fully autonomous vehicles, and smart contracts.\r\n\r\n# verification\r\n\r\nAn area of focus is runtime robustness analysis of the main driver of artificial intelligence systems, namely artificial neural network models. Neural models have reached the date when they are considered as any other software program, although they do not follow hard-coded rules like other programs, instead follow optimization heuristics derived from large amounts of multimodal data. In this way, feasible, systematic testing, verification, and repair of neural systems are as critical as traditional software systems written purely by programmers, in order to prevent safety hazards and inconveniences in the application. Therefore, SOCRATES has been exclusively developed by our RISE laboratory at SMU to meet the stringent requirements imposed by the above procedures. SOCRATES is a unified platform for neural network analysis. It is designed to support a standardised format for multiple neural network models. One of its most prominent features is that the platform solves problems that have long been difficult for most existing neural network analysis methods, namely dispersion and incompatibility.\r\n\r\n# repair\r\n\r\nThere are unintentional adversarial examples of neural network-based AI systems that harm more than just security and convenience. These examples are likely to indicate discrimination and unfairness of the system under test. In this work, we aim to develop systematic theories, methods, and tools to improve fairness in AI systems. In this work, CARE, published at ICSE 2022, we address the problem of repairing neural networks to achieve desirable properties, with an emphasis on fairness. The causality-based neural network repair technique for neural networks plays a very important role in the whole process. We propose to construct a neural network that satisfies this property with minimal adjustment of the parameters of a given neural network, and substantially (\\>61%) improve the fairness of the neural network with respect to social factors such as age and gender.\r\n\r\n# Backdoor attack\r\n\r\nBackdoor attacks are a form of adversarial attacks on deep networks where the attacker provides poisoned data to the victim to train the model with, and then activates the at- tack by showing a specific small trigger pattern at the test time.\r\n\r\n# Publications:\r\n\r\nPham, L. H., & Sun, J. (2022). Verifying Neural Networks Against Backdoor Attacks. arXiv preprint arXiv:2205.06992.\r\n\r\nZhang, M., Sun, J., & Wang, J. (2022). Which neural network makes more explainable decisions? An approach towards measuring explainability. Automated Software Engineering, 29(2), 1-26.\r\n\r\nSun, B., Sun, J., Pham, L. H., & Shi, J. (2022, May). Causality-based neural network repair. In Proceedings of the 44th International Conference on Software Engineering (pp. 338-349).\r\n\r\nSun, B., Sun, J., Dai, T., & Zhang, L. (2021, November). Probabilistic verification of neural networks against group fairness. In International Symposium on Formal Methods (pp. 83-102). Springer, Cham.\r\n\r\n# Dataset\r\n\r\n## MNIST\r\n\r\nThe Modified National Institute of Standards and Technology database (MNIST) is a large database of handwritten digits commonly used to train various image processing systems.\r\n\r\n![](https://s1.ax1x.com/2022/08/18/vDf3i8.png)\r\n\r\n## CIFAR-10\r\n\r\nThe CIFAR-10 (Canadian Institute for Advanced Study) dataset is a set of images commonly used to train machine learning and computer vision algorithms.10 different classes representing planes, cars, birds, cats, deer, dogs, frogs, horses, boats and trucks.\r\n\r\n![](https://s1.ax1x.com/2022/08/18/vDfJzQ.png)\r\n\r\n## Census\r\n\r\nThis data was extracted from the [1994 Census bureau database](http://www.census.gov/en.html) by Ronny Kohavi and Barry Becker (Data Mining and Visualization, Silicon Graphics). The prediction task is to determine whether a person makes over \\$50K a year.\r\n\r\n![](https://s1.ax1x.com/2022/08/18/vDflIf.png)\r\n\r\n# GTSRB\r\n\r\nThe German Traffic Sign Benchmark is a multi-class, single-image classification challenge held at the International Joint Conference on Neural Networks (IJCNN) 2011.\r\n\r\n![](https://s1.ax1x.com/2022/08/18/vDftMj.png)\r\n\r\n# Fashion\r\n\r\na large-scale clothes database, which has several appealing properties:\r\n\r\nFirst, DeepFashion contains over **800,000** diverse fashion images ranging from well-posed shop images to unconstrained consumer photos, constituting the largest visual fashion analysis database.\r\n\r\n![](https://s1.ax1x.com/2022/08/18/vDf8JS.png)\r\n\r\n## Credit\r\n\r\nThis dataset contains information on default payments, demographic factors, credit data, history of payment, and bill statements of credit card clients in Taiwan from April 2005 to September 2005.\r\n\r\n![](https://s1.ax1x.com/2022/08/18/vDfGRg.png)\r\n\r\n## ACAS\r\n\r\nAlso, known as Airborne Collision Avoidance System.\r\n\r\nACAS has been designed to provide a backup collision avoidance service for the existing\r\n\r\nconventional air traffic control system while minimizing unwanted alarms in encounters for which the collision risk does not warrant escape manoeuvres. The operation of ACAS is not dependent upon any ground-based systems.\r\n\r\n## Model\r\n\r\n## CNN\r\n\r\nA Convolutional Neural Network (CNN) is a Deep Learning algorithm which can take in an input image, assign importance (learnable weights and biases) to various aspects/objects in the image and be able to differentiate one from the other. The pre-processing required in a ConvNet is much lower as compared to other classification algorithms. While in primitive methods filters are hand-engineered, with enough training, ConvNets have the ability to learn these filters/characteristics.\r\n\r\n## FNN/FFNN\r\n\r\nA feedforward neural network (FNN) is an artificial neural network wherein connections between the nodes do not form a cycle. As such, it is different from its descendant: recurrent neural networks.\r\n\r\nThe feedforward neural network was the first and simplest type of artificial neural network devised. In this network, the information moves in only one direction\xe2\x80\x94forward\xe2\x80\x94from the input nodes, through the hidden nodes (if any) and to the output nodes. There are no cycles or loops in the network.\r\n'
    }
  },
  props: {
    filename: String
  },
  components: {
  },
  computed: {
    prop () {
      const data = {
        subfield: false, // 单双栏模式
        defaultOpen: 'preview', // edit： 默认展示编辑区域 ， preview： 默认展示预览区域
        editable: false,
        imagelink: true,
        toolbarsFlag: false,
        scrollStyle: true
      }
      return data
    }
  }
}
</script>
