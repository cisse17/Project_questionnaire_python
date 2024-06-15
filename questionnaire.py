# 2 eme version code avec POO
class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    # def FromData(data):
        # q = Question(data[0], data[1], data[2])     #  on appel la class Question car ici cette methode depend de la class pas du init
        # return q

    def poser_question(self):
        print("QUESTION")
        print(" ", self.titre)
        for i in range(len(self.choix)):
            print(" ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int - 1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")

        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):  #    cette fonction va etre un variable de class donc ne pas oublier de mettre le nom de la class avant comme Question.demander_reponse_numerique_utlisateur()
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)

class Questionnaire:
    def __init__(self, questions):
        self.questions = questions
    def lancer_questionnaire(self):
        score = 0
        for question in self.questions:
            if question.poser_question():
                score += 1
        print("Score final :", score, "sur", len(self.questions))


Questionnaire(
    (
        Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
        Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
        Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
        # on peut alimenter nos data (questions) ici sans modifier le code partout plus pratique
    )
).lancer_questionnaire()



"""questions = (
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
    Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")

)
"""

"""data = (("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
        )
q = Question.FromData(data)
#q.poser_question()
#print(q.__dict__) # affiche en format dictionnaire
"""


#____1ere version code ______
"""
def reponse_numerique(min, max):
    choix_str = input("Quel est votre reponse ? entre " + str(min) + " et " + str(max) + " ")
    try:
        choix_int = int(choix_str)
        if min <= choix_int <= max:
            return choix_int
        print("vous devez entrer un nombre entre " + str(min) + " et " + str(max))
    except:
        print("vous devez entrer une valeur numerique")
    return reponse_numerique(min, max)

def poser_question(question):
    bonne_reponse = question[2]
    choix_reponse = question[1]
    print(" ", "QUESTIONS")
    print(question[0])
    #print(question[1])
    for i in range(len(choix_reponse)):
        print(str(i+1), " - ", str(choix_reponse[i]))

    reponse_correcte = False
    choix_int = reponse_numerique(1, len(choix_reponse))
    if choix_reponse[choix_int-1].lower() == bonne_reponse.lower():
        print("reponse correcte")
        reponse_correcte = True
    else:
        print("reonse incorrecte")

    return reponse_correcte
    print()


def afficher_questiionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print("votre score", score)




question1 = ("Quelle est la capitale de l'Italie ?", ("Venise", "Pise", "Florence", "Rome", "Lille"), "Rome")
question2 = ("Quelle est la capitale de la France ?", ("Venise", "Pise", "Florence", "Paris", "Lille"), "Paris")

questionnaire = (question1, question2)
afficher_questiionnaire(questionnaire)"""




