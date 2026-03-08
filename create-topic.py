import argparse
from confluent_kafka.admin import AdminClient, NewTopic

# 1. Configuration des paramètres en ligne de commande
parser = argparse.ArgumentParser(description="Créer un nouveau topic Kafka sur le cluster.")
parser.add_argument("nom_topic", help="Le nom du topic que tu souhaites créer")
parser.add_argument("--partitions", type=int, default=1, help="Nombre de partitions (défaut: 1)")

# Récupération des arguments tapés par l'utilisateur
args = parser.parse_args()

# 2. Connexion au broker
admin_client = AdminClient({'bootstrap.servers': 'localhost:30565'})

# 3. Création du topic avec les variables dynamiques
nouveau_topic = NewTopic(
    topic=args.nom_topic, 
    num_partitions=args.partitions, 
    replication_factor=1
)

futures = admin_client.create_topics([nouveau_topic])

# 4. Vérification
for topic, future in futures.items():
    try:
        future.result()
        print(f"Succès : Le topic '{topic}' a été créé avec {args.partitions} partition(s) !")
    except Exception as e:
        print(f"Échec : Impossible de créer le topic '{topic}'. Raison : {e}")