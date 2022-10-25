import json
import random


def load_question(json_file):
    # Ouvre le fichier JSON
    f = open(json_file, 'r', encoding='utf-8-sig')

    # Retourne le JSON sous forme de dictionnaire
    data = json.load(f)
    return data['list_questions']


def main():
    # récupère les données du fichier JSON sous forme de dict
    list_q = load_question('question.json')

    # Choisi X questions parmi la liste
    question_rd_choice = random.sample(range(len(list_q)), 3)

    count = 1
    print("=========================")

    for item in question_rd_choice:
        print("|| " + str(count) + ". " + list_q[item]["question"])
        count = count+1

    print("=========================")

    # Récupère le choix de l'user
    user_choix_question = int(input("Indiquer votre choix :"))

    id_q = question_rd_choice[user_choix_question-1]

    # Choisi 4 réponses aléatoire pour la question
    reponse_rd_choice = random.sample(range(len(list_q[id_q]["reponses"])), 4)

    count = 1
    secret = random.randrange(1, 5)
    print("=========================")

    for item in reponse_rd_choice:
        if secret == count:
            print("?? " + list_q[id_q]["reponses"][item])
        else:
            print("\|| " + list_q[id_q]["reponses"][item])
        count = count+1
    print("=========================")


if __name__ == "__main__":
    main()
