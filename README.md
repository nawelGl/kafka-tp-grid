# kafka-tp-grid
TP Outils pour le GRID :
- Créer un cluster Kafka mono broker
- Créer les scripts suivants : "create-topic", "list-topic"

## Prompts Gemini :
Je dois faire un cluster mono broker kafka que me proposes-tu ?  
...  
Ok et comment ça s'utilise ?  
...  
Et concretement cest quoi Kraft par rapport a kafka de base ?  
...  
okie et question : qu'est ce qui fait que notre instance avec Docker compose est un cluster ? Il y a un broker mais je peux créer le nombre de "clones" que je veux ?  
...  
nan le but est vraiment de faire un cluster mono broker dans le cadre d'un cours. Est ce faisable avec Kubernetes ?  
...  
ok et si je veux faire sans strimzi pour + avoir la main sur la conf, qu'est ce que ça implique, est ce beaucoup plus long a mettre en place ?  
...  
mmm ok bon donne moi la config et les étapes pour faire avec strimzi alors stp.   
...  
ok, j'ai pas compris concrètement ce que fait la toute dernière commande. Peut tu la réexpliquer ? aussi comment je sais que le cluster est lancé et comment je connais et peut configurer le nombre de machines ?  
...  
si j'arrête docker desktop du coup ça arrête aussi Kubernetes i guess. 
...  
ok cest clair, et du coup si je veux un cluster de 5 machines je change la ligne replicas et je met 5, j'aurais toujours un seul broker et 5 clones ?  
...  
okay je comprends, mais avec une seule machine on ne devrait pas pouvoir parler de cluster ..? si ?  
...  
Une fois que j'ai mon cluster la consigne était la suivante : "Faire les scripts python suivants :
- Create topic
- List topic".  
...  
mais du coup quel est l'interêt de faire des scripts Kafka alors qu'on a des commandes qui font déjà ça ?
<br><br>


Remarque : sur mon gemini j'ai configuré cette instruction : 
```
Quand je fais des requêtes qui concernent l'informatique (code, modélisation ...) donne-moi des réponses techniques avec des explications, mais qui sont regroupées au même endroit pour que je puisse aller droit au but si nécessaire. N'hésite pas ajouter des bonnes pratiques et à proposer des solutions plus optimales que celles que j'essaie de mettre en place si elles existent.
 ```
Du coup les réponses sont assez précises techniquement.


## Commandes

Création d'un espace de travail isolé : 
```kubectl create namespace kafka```

Installation de l'opérateur Strimzi dans ce namespace : 
```kubectl create -f 'https://strimzi.io/install/latest?namespace=kafka' -n kafka```

Vérification du démarrage du pod de l'opérateur (Attendre le statut 'Running') : 
```kubectl get pods -n kafka -w```

Appliquer la configuration : 
```kubectl apply -f kafka-strimzi.yaml```

Attendre que l'opérateur finalise la création du cluster et du réseau : 
```kubectl wait kafka/mon-cluster --for=condition=Ready --timeout=300s -n kafka```

Récupérer le port externe (ex: 9094:32293/TCP) : 
```kubectl get svc mon-cluster-kafka-externe-bootstrap -n kafka```

## Execution scripts :
```
nawel@MacBook-Pro-de-Nawel TP Kafka % python3 create-topic.py test
Succès : Le topic 'test' a été créé avec 1 partition(s) !
nawel@MacBook-Pro-de-Nawel TP Kafka % python3 list-topics.py      
--- Topics présents sur le cluster ---
- test
nawel@MacBook-Pro-de-Nawel TP Kafka % python3 create-topic.py test2
Succès : Le topic 'test2' a été créé avec 1 partition(s) !
nawel@MacBook-Pro-de-Nawel TP Kafka % python3 list-topics.py       
--- Topics présents sur le cluster ---
- test2
- test
```