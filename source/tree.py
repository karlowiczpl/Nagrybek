class Skill:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def activate(self):
        # Funkcja aktywująca umiejętność, która może mieć jakiś efekt w grze
        print(f"Aktywowano umiejętność: {self.name}. Efekt: {self.effect}")


# Drzewo umiejętności: Chronomancer
class ChronomancerTree:
    def __init__(self):
        self.skills = [
            Skill("Czasowy Spokój", 
                  "Spowalnia czas wokół Ciebie i przeciwników o 50% przez 5 sekund.", 
                  "Spowolnienie przeciwników o 50% przez 5 sekund."),
            Skill("Zwiększona Projekcja Czasowa", 
                  "Zwiększa obszar spowolnienia o 30% i zadaje obrażenia.", 
                  "Większy obszar spowolnienia oraz obrażenia w obszarze."),
            Skill("Chrono Reflex", 
                  "Automatyczne ataki w czasie spowolnienia.", 
                  "Automatyczne ataki w czasie spowolnienia."),
            Skill("Zniekształcony Czas", 
                  "Odbicie obrażeń od przeciwnika i osłabienie go.", 
                  "Odbicie obrażeń oraz osłabienie przeciwnika."),
            Skill("Mistrz Chronomancji", 
                  "Cofanie się w czasie o 2 sekundy.", 
                  "Cofanie się w czasie o 2 sekundy."),
        ]

    def activate_skill(self, skill_index):
        """Aktywuj umiejętność na podstawie indeksu w drzewie umiejętności."""
        if 0 <= skill_index < len(self.skills):
            self.skills[skill_index].activate()
        else:
            print("Nieprawidłowy indeks umiejętności!")


# Drzewo umiejętności: Temporal Blade
class TemporalBladeTree:
    def __init__(self):
        self.skills = [
            Skill("Cios Przeszłości", 
                  "Zadaje cios, który powtarza się po 1 sekundzie.", 
                  "Podwójne obrażenia z tego samego ciosu."),
            Skill("Echo Ciosu", 
                  "Cios ma szansę wywołać echo z przyszłości, które zadaje obrażenia.", 
                  "Cios wywołuje echo, zadając dodatkowe obrażenia."),
            Skill("Temporal Stance", 
                  "Pozycja, w której unikasz ataków przez 2 sekundy.", 
                  "Unik ataków przez 2 sekundy."),
            Skill("Paralelny Cios", 
                  "Ciosy z przeszłości i teraźniejszości wywołują obrażenia równocześnie.", 
                  "Ciosy z przeszłości i teraźniejszości."),
            Skill("Chrono Fury", 
                  "Ciosy zadawane z różnych momentów czasowych.", 
                  "Zadawanie obrażeń w różnych momentach czasowych."),
        ]

    def activate_skill(self, skill_index):
        """Aktywuj umiejętność na podstawie indeksu w drzewie umiejętności."""
        if 0 <= skill_index < len(self.skills):
            self.skills[skill_index].activate()
        else:
            print("Nieprawidłowy indeks umiejętności!")


# Drzewo umiejętności: Chrono Gunslinger
class ChronoGunslingerTree:
    def __init__(self):
        self.skills = [
            Skill("Pocisk Przyszłości", 
                  "Pocisk, który zadaje obrażenia i spowalnia przeciwnika.", 
                  "Zwiększone obrażenia oraz spowolnienie."),
            Skill("Chrono Strzelec", 
                  "Strzały mogą się klonować i trafić różnych przeciwników.", 
                  "Strzały klonują się i trafiają kilku przeciwników."),
            Skill("Czasowa Pułapka", 
                  "Ustawienie pułapki, która spowalnia przeciwników w promieniu.", 
                  "Spowolnienie przeciwników w określonym obszarze."),
            Skill("Mocny Strzał", 
                  "Strzały zadają zwiększone obrażenia w czasie spowolnienia.", 
                  "Obrażenia wzrastają przy spowolnieniu."),
            Skill("Przyszłość w Rękach", 
                  "Strzały przebijają wrogów, zadając obrażenia wszystkim po drodze.", 
                  "Strzały przebijają wrogów, zadając obrażenia."),
        ]

    def activate_skill(self, skill_index):
        """Aktywuj umiejętność na podstawie indeksu w drzewie umiejętności."""
        if 0 <= skill_index < len(self.skills):
            self.skills[skill_index].activate()
        else:
            print("Nieprawidłowy indeks umiejętności!")