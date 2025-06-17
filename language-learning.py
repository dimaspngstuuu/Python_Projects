import random
words = [
    {"es": "de", "en": "of/from"},
    {"es": "la", "en": "the (feminine)"},
    {"es": "que", "en": "that/which"},
    {"es": "el", "en": "the (masculine)"},
    {"es": "en", "en": "in/on"},
    {"es": "y", "en": "and"},
    {"es": "a", "en": "to/at"},
    {"es": "los", "en": "the (masculine plural)"},
    {"es": "se", "en": "oneself"},
    {"es": "del", "en": "from the"},
    {"es": "las", "en": "the (feminine plural)"},
    {"es": "un", "en": "a/an"},
    {"es": "por", "en": "by/for/through"},
    {"es": "con", "en": "with"},
    {"es": "no", "en": "no/not"},
    {"es": "una", "en": "a/an/one"},
    {"es": "su", "en": "his/her/its/your/their"},
    {"es": "para", "en": "for/to/in order to"},
    {"es": "es", "en": "is"},
    {"es": "al", "en": "to the"},
    {"es": "hola", "en": "hello"},
    {"es": "por favor", "en": "please"},
    {"es": "gracias", "en": "thank you"},
    {"es": "de nada", "en": "you're welcome"},
    {"es": "sí", "en": "yes"},
    {"es": "no", "en": "no"},
    {"es": "buenos días", "en": "good morning"},
    {"es": "buenas tardes", "en": "good afternoon"},
    {"es": "buenas noches", "en": "good evening/night"},
    {"es": "amiga", "en": "friend (female)"},
    {"es": "antes", "en": "before"},
    {"es": "ahora", "en": "now"},
    {"es": "después", "en": "later"},
    {"es": "momento", "en": "moment"},
    {"es": "me gusta", "en": "I like"},
    {"es": "no me gusta", "en": "I don't like"},
    {"es": "muy", "en": "very"},
    {"es": "nunca", "en": "never"},
    {"es": "mismo", "en": "same"},
    {"es": "igual", "en": "the same"},
    {"es": "ser", "en": "to be (permanent)"},
    {"es": "estar", "en": "to be (temporary)"},
    {"es": "ir", "en": "to go"},
    {"es": "hacer", "en": "to do/make"},
    {"es": "haber", "en": "to have (auxiliary)"},
    {"es": "tener", "en": "to have (possession)"},
    {"es": "poner", "en": "to put"},
    {"es": "entender", "en": "to understand"},
    {"es": "deber", "en": "to owe/should"},
    {"es": "pagar", "en": "to pay"},
    {"es": "comer", "en": "to eat"},
    {"es": "beber", "en": "to drink"},
    {"es": "tomar", "en": "to take/drink"},
    {"es": "hablar", "en": "to speak"},
    {"es": "decir", "en": "to say"},
    {"es": "escuchar", "en": "to listen"},
    {"es": "mirar", "en": "to watch/look at"},
    {"es": "ver", "en": "to see"},
    {"es": "llegar", "en": "to arrive"},
    {"es": "nuevo", "en": "new"},
    {"es": "viejo", "en": "old"},
    {"es": "feliz", "en": "happy"},
    {"es": "triste", "en": "sad"},
    {"es": "enfermo", "en": "sick"},
    {"es": "bien", "en": "well"},
    {"es": "grande", "en": "big"},
    {"es": "chico", "en": "small (Latin America)"},
    {"es": "pequeño", "en": "small (Spain)"},
    {"es": "bueno", "en": "good"},
    {"es": "malo", "en": "bad"},
    {"es": "sin", "en": "without"},
    {"es": "con", "en": "with"},
    {"es": "mucho", "en": "a lot"},
    {"es": "poco", "en": "a little"},
    {"es": "hermoso", "en": "beautiful"},
    {"es": "feo", "en": "ugly"},
    {"es": "fácil", "en": "easy"},
    {"es": "fantástico", "en": "fantastic"},
    {"es": "automático", "en": "automatic"},
    {"es": "celular", "en": "cell phone"},
    {"es": "móvil", "en": "mobile phone"},
    {"es": "agenda", "en": "agenda"},
    {"es": "documento", "en": "document"},
    {"es": "máquina", "en": "machine"},
    {"es": "día", "en": "day"},
    {"es": "segundo", "en": "second"},
    {"es": "minuto", "en": "minute"},
    {"es": "hora", "en": "hour"},
    {"es": "usar", "en": "to use"},
    {"es": "difícil", "en": "difficult"},
    {"es": "carro", "en": "car"},
    {"es": "persona", "en": "person"},
    {"es": "familia", "en": "family"},
    {"es": "alcohol", "en": "alcohol"},
    {"es": "animal", "en": "animal"},
    {"es": "romántico", "en": "romantic"},
    {"es": "pánico", "en": "panic"},
    {"es": "plástico", "en": "plastic"},
    {"es": "cómico", "en": "comical/funny"},
]
def quiz_user(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the english translation of {word['es']} ?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['en'].lower()

        if user_answer == correct_answer:
            print("Correct!!\n!")
            score+=10
        else:
            print(f"Sorry, your answer is wrong, the answer is {word['en']}")
    print("")


def main():
    print("Welcome to the language learning app")
    input("Press Enter to start the quiz")
    quiz_user(words)

if __name__ == "__main__":
    main()