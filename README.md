# Strzelanka w PyGame
Gra została stworzona w ramach projektu na przedmiocie "Programowanie obiektowe" prowadzonego w Instytucie Informatyki Uniwersytetu Wrocławskiego.

# Fabuła
Spełnił się Twój najstraszniejszy koszmar. Nie wiesz gdzie jesteś. Wokół Ciebie pojawiają się przerażające istoty, a Ty nie wiesz co robić. Nagle obok Twoich stóp, jak spod ziemi, wyłania się lufa karabinu. Nie zastanawiając się długo, chwytasz broń i zaczynasz strzelać do potworów. Musisz przetrwać! Jeszcze nie wiesz, że żeby się wydostać, będziesz musiał pokonać samego siebie...

# Instrukcja uruchomienia

## Potrzebne programy
By uruchomić grę, należy zainstalować na swoim systemie interpreter języka Python w wersji 3.6 lub wyższej ([link](https://www.python.org/downloads/)), a także doinstalować do niego za pomocą menedżera pip, bibliotekę pygame.

```bash
python3 -m pip install -U pygame --user
```
([link do szczegółów](https://www.pygame.org/wiki/GettingStarted]))

## Uruchomienie
By włączyć grę, wystarczy uruchomić ją za pomocą interpretera Python.

```bash
python3 main.py
```
Gdy nie znajdujemy się w folderze projektu, zamiast "main.py" należy podać ścieżkę bezwględną do tego pliku.

# Opis modelu obiektowego
Postać, którą poruszamy, a także nasi przeciwnicy to podklasy klasy Character dziedziczącej po pygame.sprite.Sprite.
Sprite od Pygame, dostarcza całkiem dobry i prosty sposób wykrywania kolizji obiektów, co jest przydatne przy takich projektach.
Ustawienia poszczególnych rund trzymane są w podklasach klasy Round. Każda z tych klas ma w sobie wskaźnik na następną.
Gdy dojdziemy do końca, gra powiadamia nas o zwycięstwie. W Round tworzone są i ustawiane na mapie obiekty przeciwników.
Ważnym elementem gry jest klasa Interface, która odpowiada za informacje na dolnym panelu, a także, za pomocą klasy Square,
zarządza wybranymi przez gracza broniami - decyduje, czy umożliwić graczowi wybór danej broni czy nie.
Dostępne w danej rundzie bronie ustala się podczas tworzenia obiektu klasy Round.
Strzały z broni dziedziczą po klasie Blast. Każdy strzał jest obiektem, dla którego sprawdzana jest kolizja z innymi obiektami.
Obiekt klasy Textures trzyma w sobie wszystkie potrzebne w grze tekstury.
Za interakcję z użytkownikiem odpowiadają funkcje w pliku interactive.py, a także metody klasy Interface

# Diagram klas
Diagram klas dostępny jest w pliku dependency_class.png, w głównym folderze projektu.

#Autor
Bartosz Jaśkiewicz