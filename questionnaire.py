
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


Questionnaire(
    (
        Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
        Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
        Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
        # on peut alimenter nos data (questions) ici sans modifier le code partout plus pratique
    )
).lancer_questionnaire()




# __________Reflexion _________POO pr definir les entitées
"""
class Questions: (entitées)
    __init__(self, titre, questions, bonne_reponse) => min, max
    #__ Données :
        - titre, questions (bonne_reponse), bonne_reponse(choix)

    #__ Actions (methodes)
        - poser_et_afficher_question(self):
            print(titre)
            bonne_reponse = self.questions[2]
            for i in self.questions:
            print(i)
            reponse_user = input() # Question.demander_reponse_numerique()

            return True or False (Pourquoi pas)

        - demander_reponse_numerique(self) # gestion d'erreure et recuperation de choix utilisateur
            - (POURQUOI pas une variable d'instance ici)
             reponse_user = input(self.min, self.max)

             return something...

             
class Questionnaire(Questions): (Nouvelle entitée => Herite de Questions)
    def __init__(self):
        super().__ini__()
    def lancer_questionnaire():
        score = 0
        if super().poser_et_afficher_question(): == True:
            score += 1
            => reponse bonne
        print(result de.....score )

question1 = Questions(
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
)
q = Questionnaire(question1)
q.lancer_questionnaire()

"""
# ____Mise en pratique de notre reflexions avec quelques modifications par rapport à notre reflexion ___
"""class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse
    
    # Autre façon avec la methode de calsse => impressionant
    #def FromData(data):
       # q = Question(data[2], data[0], data[1])
        #return q
    
    def poser_question(self):
        print("Titre ", self.titre)
        for i in range(len(self.choix)):
            print(f" {i + 1} - {self.choix[i]} " )

        choix_user = Question.demander_reponse_numerique(1, len(self.choix))
        a = False
        if self.choix[choix_user - 1] == self.bonne_reponse:
            print("Bonne réponse")
            a = True
        else: 
            print("Mauvaise réponse")
        return a
    
    def demander_reponse_numerique(min, max): # methode de class/statique (on a pas besoin du self ici)
        choix_utilisateur_str = input("Votre choix entre " + str(min) + " et " + str(max) + " " )
        try:
            choix_utilisateur_int = int(choix_utilisateur_str)
        except:
            print("ERREUR : Vous devez entrer une valeur numérique")
            return Question.demander_reponse_numerique(min, max)
        
        if not (min <= choix_utilisateur_int <= max):
                print("ERREUR : Vous devez entrer un nombre entre ", min, "et" , max)
                return Question.demander_reponse_numerique(min, max)
        return choix_utilisateur_int

class Questionnaire: 
    def __init__(self, questionnaire):
         self.questionnaire = questionnaire

    def lancer_questionnaire(self):
         score = 0
         for question in self.questionnaire:
            if question.poser_question(): # on peut appeler la fonction ou methode d'une classe ici (poser_question de de Question)
                score += 1
         print(f"Votre score : {score}")
        

question1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
question2 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")

# question1.poser_question() 
questions = (
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
)   

questionnaire = Questionnaire(questions)
questionnaire.lancer_questionnaire() """