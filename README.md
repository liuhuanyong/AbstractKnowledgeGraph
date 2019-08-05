# AbstractKnowledgeGraph
AbstractKnowledgeGraph, a systematic knowledge graph that concentrate on abstract thing including abstract entity and action. 抽象知识图谱，集中于抽象知识，包括抽象实体，抽象动作，抽象事件。基于该知识图谱，可以进行不同层级的实体抽象和动作抽象，这与人类真实高度概括的认知是一致的。

# 项目介绍
抽象知识图谱，集中于对知识图谱和事件图谱中的实例事实进行抽象，包括实体抽象、动作抽象以及事件抽象，从而达到对人类真实认知的模拟。本项目目标有三个：  
1）论述抽象图谱。对抽象图谱的现实需求进行论述。  
2）介绍抽象图谱的相关工作。目前，关于抽象知识图谱的工作已经有一定的积累，如英文中的ConceptNet,MINDNET,verbnet；中文的CN-Probase,Hownet,大词林,百度百科Schema等。  
3）提出抽象知识图谱的实施路线并给出抽象接口实践。一个可用的抽象知识图谱构建路线，是对以上两个内容的实践说明。  

# 关于抽象知识图谱

1、抽象知识图谱的现实基础与需求

1）语言的语法特性。定语+主语+状语+谓语+补语+宾语是目前中文成句的重要形式，这种成分的占位与填充为了以词性标注、实体识别、句法分析已经语义角色标注的自然语言处理提供了基础。

2）语言抽象的层级特性。语义三角(包括符号，语义以及语境况三者构成的三角)，对人类社会认知进行了很好的刻画。语言形成的过程，是人类对认知(物体，动作，思想)概括和总结的过程。形式化是概括的手段，语言符号及符号体系是概括的结果。层次性是符号体系的一个重要特征，概念之间的上下位，概念之间的总括与构成等，形成构成了语言抽象层级性的物质基础。

3）抽象能力是认知能力的基础。认知的过程，是对现实世界火活动的交互过程，包括内在和外在两个组成部分，内在负责自身知识的总结，抽象，体系的构建过程，即学习过程。外在负责对内在部分形成的知识体系应用的过程，应用包括验证和补充两个部分，验证在于对内在知识形成的证伪，补充在于对新抽象知识的形成与抽象规则的修正两个方面。孩子从出生的一无所知到逐步认知能力的过程，就是对知识不断总结、概括以及应用的过程。

4）抽象数据与抽象规则的获取挑战

让机器能够达到小孩的智力，根本上需要具备抽象能力以及抽象数据基础两个条件。这是解决认知智能的一个方向之一，而目前现有的技术手段，还难以快速满足这两个条件。一方面，健全的抽象数据较难获取，抽象与概括的类型众多，既有对动作的抽象，也有对名词实体的抽象，也有对性状的抽象，抽象的角度以及抽象的粒度很难把握。另一方面，基于这类抽象数据，学习或总结出内在的抽象规则和抽象层级，是难以攻克的一点。  

2、抽象知识图谱的构成  
1）抽象知识图谱体系架构  
![image](https://github.com/liuhuanyong/AbstractKnowledgeGraph/blob/master/img/intro.png)  

2）抽象知识图谱的抽象层级  
a) 名词性实体的抽象  
b) 性状性修饰的抽象  
c) 动作性事件的抽象  

# 抽象图谱相关工作
1）ConceptNet  

2) Probase  

3) CN-probase  

4) HowNet  

5) BigCilin  

6) BaSchema  

# 抽象图谱构建技术路线



# 目前接口概述及调用
1，名词抽象路径

![image](https://github.com/liuhuanyong/AbstractKnowledgeGraph/blob/master/img/noun.png)
2，状态词抽象路径

![image](https://github.com/liuhuanyong/AbstractKnowledgeGraph/blob/master/img/adj.png)
3，动作抽象路径

![image](https://github.com/liuhuanyong/AbstractKnowledgeGraph/blob/master/img/verb.png)

# 总结


