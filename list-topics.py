from confluent_kafka.admin import AdminClient

# Connexion au broker
admin_client = AdminClient({'bootstrap.servers': 'localhost:30565'})

# Récupération de l'ensemble des métadonnées du cluster (Timeout de 10 secondes)
metadonnees_cluster = admin_client.list_topics(timeout=10)

print("--- Topics présents sur le cluster ---")
# Parcours du dictionnaire des topics retourné par le broker
for nom_topic in metadonnees_cluster.topics:
    print(f"- {nom_topic}")