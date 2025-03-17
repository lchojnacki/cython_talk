---
# You can also start simply with 'default'
theme: default
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: ./img/dpld_bg.png
# some information about your slides (markdown enabled)
title: "Cython: Turbodoładowanie Pythona czy zbędna komplikacja?" 
info: |
  Cython talk slides
# apply unocss classes to the current slide
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
---
<div class="title-slide-container">
    <div class="title-slide-left">
        <div class="title-slide-logo">
            <img src="./img/dpld.png">
        </div>
        <div class="title-slide-title">
            <h1>Cython: Turbodoładowanie Pythona czy zbędna komplikacja?</h1>
        </div>
        <div class="title-slide-accent">
            <h3>2025-03-25</h3>
        </div>
    </div>
    <div>
        <div style="padding: 40px 0 10px 0">
            <h3 class="title-slide-accent">Prezentuje:</h3>
        </div>
        <div>
            <img src="./img/tag.png" class="title-slide-tag">
        </div>
        <div>
            <img src="./img/IMG_6682.jpg" class="title-slide-presenter-image">
        </div>
        <div class="title-slide-presenter-name">
            <h2>Łukasz Chojnacki</h2>
        </div>
        <div>
            <h3 class="title-slide-accent">Python Developer</h3>
        </div>
    </div>
</div>

<!--

-->

---
transition: fade-out
---
<div class="slide-container">
<h1>whoami</h1>

- 🐍 **Python Web Developer** w Deployed.pl
- 🧑‍🏫 Od wielu lat udzielam korepetycji z **Pythona**
- 🧑‍💻 **Cythona** poznałem na studiach, ale nie wykorzystuję go w swojej codziennej pracy
- ⚽🏴󠁧󠁢󠁥󠁮󠁧󠁿 Poza programowaniem interesuję się piłką nożną, szczególnie w wydaniu **angielskim**
</div>
<!--

-->

---
level: 2
---

# Czym jest Cython?

<div class="w-60 relative">
  <div class="relative w-40 h-40">
    <img
      v-click
      v-motion
      :initial="{ y: 500, x: -100, scale: 2 }"
      :enter="final_python"
      class="absolute inset-0"
      src="./img/logo-circle-green.png"
      style="z-index: 1"
      alt=""
    />
  <img
      v-click
      v-motion
      :initial="{ y: 700, x: -100, scale: 5 }"
      :enter="final_cython"
      class="absolute inset-0"
      src="./img/logo-circle-blue.png"
      alt=""
    />
    <div
      v-click
      v-motion
      :initial="{ y: 500, x: -100, scale: 2 }"
      :enter="final_python_text"
      class="absolute inset-0"
      style="z-index: 2; text-align: center; color: black"
    >
      def lambda class continue yield raise
  </div>
    <div
      v-click
      v-motion
      :initial="{ y: 500, x: -100, scale: 2 }"
      :enter="final_cython_text"
      class="absolute inset-0"
      style="z-index: 2; text-align: center; color: black"
    >
      long cdivision malloc libc fopen
  </div>
  </div>
</div>

<!-- vue script setup scripts can be directly used in markdown, and will only affects current page -->
<script setup lang="ts">
const final_python = {
  x: 300,
  y: 100,
  rotate: 0,
  scale: 2,
  transition: {
    type: 'spring',
    damping: 10,
    stiffness: 20,
    mass: 2
  }
};
const final_python_text = {
  x: 270,
  y: 120,
  rotate: 0,
  scale: 1,
  transition: {
    type: 'spring',
    damping: 10,
    stiffness: 20,
    mass: 2
  }
};
const final_cython = {
  x: 350,
  y: 200,
  rotate: 0,
  scale: 4,
  transition: {
    type: 'spring',
    damping: 10,
    stiffness: 20,
    mass: 2
  }
};
const final_cython_text = {
  x: 300,
  y: 300,
  rotate: 0,
  scale: 1.5,
  transition: {
    type: 'spring',
    damping: 10,
    stiffness: 20,
    mass: 2
  }
}
</script>
<!--
Nadzbiorem Pythona, chociaż od wydania wersji 3 w 2023 roku to pojęcie się trochę
rozmyło. Obecnie można z niego korzystać trochę jak z biblioteki
udostępniającej dodatkowe typy czy dostęp do funkcji C/C++.

Kompilatorem Pythona do C/C++.

Za dokumentacją - prawie każdy kod w Pythonie można skompilować za pomocą Cythona.

-->

---

# Jak to działa?


<div v-click>1. Piszesz swoją funkcję 👨‍💻</div>
<div v-click>2. Konfigurujesz plik setup.py ⚙️</div>
<div v-click>3. Kompilator Cythona wytwarza plik C/C++ 🔧</div>
<div v-click>4. Kompilator C/C++ wytwarza plik .so (Unix) lub .pyd (Windows) 🧙‍♂️</div>
<div v-click>5. Skompilowany plik możesz zaimportować w kodzie Pythona 🐍</div>
<div v-click>6. Profit 🚀
<img 
  v-motion
  :enter="{ y: -100, x: 0, scale: 0.5 }"
  src="./img/I_Am_Speed.jpg" 
  alt=""
>
</div>

---
layout: center
class: text-center
---

<div>
<img
  src="./img/let-me-see.gif"
  alt=""
>
</div>

---

# Przykładowa funkcja w Pythonie

````md magic-move {lines: true}
```python
def loop(n: int = 10_000_000) -> int:
    result = 0
    for i in range(n):
        result += i
    return result
```
````
<div v-click="[1,2]">Konfigurujemy setup.py:
````md magic-move {lines: true}
```python
from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [
    Extension("loop.optimized", ["mypackage/loop/optimized.py"]),
]

setup(
    ext_modules=cythonize(extensions, annotate=True),
)
```
````
</div>
<div v-click="2" style="margin-top: -220px">Kompilujemy...</div>
<div v-click="3">Porównujemy wyniki...
```
Running Python version...
49999995000000
Running Cython version...
49999995000000
```
</div>
<div v-click="4">Mierzymy czas...
```
Running Python version...
1 loop, best of 5: 223 msec per loop
Running Cython version...
1 loop, best of 5: 226 msec per loop
```
</div>

<!--
Skoro prawie każdy kod Pythona poprawnym kodem Cythona, to sprawdźmy jaki efekt 
osiągniemy po prostu kompilując go. 
-->

---
layout: center
class: text-center
---

<div>
<img
  src="./img/powinno-wyjsc-inaczej.jpg"
  alt=""
>
</div>

---
layout: center
class: text-center
---

<div>
<img
  src="./img/no_speed_gains.jpg"
  alt=""
>
</div>

<!--
Sama kompilacja kodu Pythona zwykle nie przyspieszy kodu, ponieważ wygenerowany
kod nadal będzie korzystał z obiektów pythona, a co za tym idzie, komunikował
się z interpreterem pythona.
-->

---

# Analiza wydajności

<div>
<Loop1 />
</div>

<!--
Raport interakcji kodu Cythona z interpreterem Pythona. Biały = zero interakcji
z pythonem, maksymalna wydajność. Im ciemniejszy żółty, tym więcej interakcji
z pythonem. Raport jest interaktywny - kliknięcie w linijkę odsłania kod C,
który jej odpowiada.

Najwięcej interakcji z pythonem - deklaracja funkcji i nagłówek pętli for.
-->

---

# Make Cython great again!

````md magic-move {at: 1, lines: true}
```python 
def loop(n: int = 10_000_000) -> int:
    result = 0
    for i in range(n):
        result += i
    return result
```

```python {*|1|5|*|*|*|*|*|3-4}
import cython

def loop(n: cython.int = 10_000_000) -> cython.int:
    result: cython.int = 0
    i: cython.int
    for i in range(n):
        result += i
    return result
```

```python
import cython

def loop(n: cython.int = 10_000_000) -> cython.long:
    result: cython.long = 0
    i: cython.int
    for i in range(n):
        result += i
    return result
```
````

<div v-click="[5, 8]">Kompilujemy...</div>
<div v-click="[6, 8]">Porównujemy wyniki...
```
Running Python version...
49999995000000
Running Cython version...
-2014260032
```
</div>

<div v-click="12" style="margin-top: -150px">Kompilujemy...</div>
<div v-click="13">Porównujemy wyniki...
```
Running Python version...
49999995000000
Running Cython version...
49999995000000
```
</div>
<div v-click="14">Mierzymy czas...
```
Running Python version...
1 loop, best of 5: 210 msec per loop
Running Cython version...
20000000 loops, best of 5: 18.3 nsec per loop
```
</div>

<div v-click="[7, 8]">
<img
  v-motion
  :enter="{ y: -450, x: 300, scale: 0.5 }"
  src="./img/scared.jpg"
  alt=""
  style="z-index: 2"
/>
</div>

<div v-click="[11,12]">
<img
  v-motion
  :enter="{ y: -1000, x: 100, scale: 0.5 }"
  src="./img/int_is_int.jpg"
  alt=""
/>
</div>

<div v-click="15">
<img
  v-motion
  :enter="{ y: -1400, x: 300, scale: 1.5 }"
  src="./img/yes.gif"
  alt=""
/>
</div>




<!--
Typ zmiennej result jest za mały, wynik nie mieści się w int
-->

---
layout: center
class: text-center
---

<div>
<img
  src="./img/deeper.jpeg"
>
</div>

<!--
Następny przykład: liczba pi + prange
-->

---

# Przybliżenie liczby π
<div></div>
Czyli wykorzystujemy algorym z XV wieku zamiast wykonać `from math import pi`

<div v-click>
<br>Szereg Nilakantha:

$$
3 + \frac{4}{2+3+4} - \frac{4}{4+5+6} + \frac{4}{6+7+8} - \frac{4}{8+9+10} + ... 
$$
</div>

<div v-click>
<br>Przedstawiony za pomocą sumy:

$$
3 + \sum_{n=1}^{\infty} -((-1)^n) \frac{4}{(2*n) * (2*n+1) * (2*n+2)}  
$$
</div>

---

# Przybliżenie liczby π

````md magic-move {at: 1, lines: true}
```python
def pi(loops: int = 999_999) -> float:
    pi_estimate: float = 3.0
    for n in range(1, loops + 1):
        sign: int = -((-1) ** n)
        term = 4 / (2 * n * (2 * n + 1) * (2 * n + 2))
        pi_estimate += sign * term

    return pi_estimate
```

```python{*|3|4|*|*|*|10}
import cython

@cython.cdivision(True)
@cython.cpow(True)
def pi(loops: cython.int = 999_999) -> cython.double:
    pi_estimate: cython.double = 3.0
    n: cython.long
    for n in range(1, loops + 1):
        sign: cython.short = -((-1) ** n)
        term: cython.double = 4 / (2 * n * (2 * n + 1) * (2 * n + 2))
        pi_estimate += sign * term

    return pi_estimate
```

```python
import cython

@cython.cdivision(True)
@cython.cpow(True)
def pi(loops: cython.int = 999_999) -> cython.double:
    pi_estimate: cython.double = 3.0
    n: cython.long
    for n in range(1, loops + 1):
        sign: cython.short = -((-1) ** n)
        term: cython.double = 4.0 / (2 * n * (2 * n + 1) * (2 * n + 2))
        pi_estimate += sign * term

    return pi_estimate
```
````
<div v-click="[5,8]">Kompilujemy...</div>
<div v-click="[6,8]">Porównujemy wyniki...
```
Running Python version...
3.141592653589787
Running Cython version...
3.0
```
</div>
<div v-click="[9,11]" style="margin-top: -150px">Kompilujemy...</div>
<div v-click="[10,11]">Porównujemy wyniki...
```
Running Python version...
3.141592653589787
Running Cython version...
3.141592653589787
```
</div>
<div v-click="11" style="margin-top: -150px; z-index: 999">Mierzymy czas...
```
Running Python version...
1 loop, best of 5: 296 msec per loop
Running Cython version...
20 loops, best of 5: 12.9 msec per loop
```
</div>
<div v-click="12">🚀</div>

<!--
cdivision - pomija pythonową walidację, np. nie rzuci ZeroDivisionError, ok 35% szybsza operacja dzielenia jeśli True

cpow - utrzymuje typ wyniku potęgowania taki sam jak typy operandów


-->

---
layout: center
class: text-center
---

<div>
<img
  src="./img/multiple_cores.jpg"
  alt=""
>
</div>

---

# Przybliżenie liczby π

````md magic-move {at: 1, lines: true}
```python
import cython

@cython.cdivision(True)
@cython.cpow(True)
def pi(loops: cython.int = 999_999) -> cython.double:
    pi_estimate: cython.double = 3.0
    n: cython.long
    for n in range(1, loops + 1):
        sign: cython.short = -((-1) ** n)
        term: cython.double = 4.0 / (2 * n * (2 * n + 1) * (2 * n + 2))
        pi_estimate += sign * term

    return pi_estimate
```
```python
import cython
from cython.parallel import prange

@cython.cdivision(True)
@cython.cpow(True)
def pi(loops: cython.int = 999_999) -> cython.double:
    pi_estimate: cython.double = 3.0
    n: cython.long
    for n in prange(1, loops + 1, nogil=True):
        sign: cython.short = -((-1) ** n)
        term: cython.double = 4.0 / (2 * n * (2 * n + 1) * (2 * n + 2))
        pi_estimate += sign * term

    return pi_estimate
```
````
<arrow v-click="[2,3]" x1="550" y1="180" x2="395" y2="245" color="#953" width="2" arrowSize="1" />

<div v-click="[3,5]">Kompilujemy...</div>
<div v-click="[4,5]">Porównujemy wyniki...
```
Running Python version...
3.141592653589787
Running Cython version...
3.141592653589787
```
</div>

<div v-click="5" style="margin-top: -150px; z-index: 999">Mierzymy czas...
```
Running Python version...
1 loop, best of 5: 296 msec per loop
Running Cython version...
100 loops, best of 5: 2.75 msec per loop
```
</div>

<div v-click="6">
<img
  v-motion
  :enter="{ y: -200, x: 250, scale: 0.5 }"
  src="./img/owen-wilson-wow.gif"
  alt=""
>
</div>

<!--

prange używa wątków, domyślnie tworzy tyle wątków ile rdzeni ma procesor, można zmienić to zachowanie

w naszym przypadku nie ma znaczenia kolejność dodawania wyrazów szeregu, każdy wyraz jest w stanie samodzielnie się wyliczyć

prange wymaga wyłączenia GIL, który uniemożliwia współbieżne wykonywanie kodu

oprócz pokazanej tu metody GIL można też wyłączyć dekoratorem i context managerem

prange wymaga instalacji OpenMP w systemie i przekazania odpowiedniej flagi podczas kompilacji

-->

---
layout: center
class: text-center
---

<div
  v-motion
  :enter="{ scale: 2.5 }"
>
```mermaid
---
config:
    themeVariables:
        xyChart:
            backgroundColor: "#0C0D1B"
---
    xychart-beta
    x-axis [Python, Cython, "Cython (prange)"]
    y-axis "Time (msec)" 0 --> 300
    bar [296, 12.9, 2.75]
```
</div>

<!--
cython ok 23x szybszy
cython + prange ok 4 razy szybszy niż zwykły cython

nie zawsze tak jest: tutaj wyszło fajnie, bo mamy dużo iteracji - przy 15 iteracjach wersja prange wypadła minimialnie gorzej niż zwykła range - narzut na tworzenie wątków
-->

---
layout: center
class: text-center
---

<div>
<img
  src="./img/use_malloc.jpg"
  alt=""
>
</div>

---

# Wykorzystanie `malloc`

````md magic-move {at: 1, lines: true}
```python
def allocation(size: int = 999_999) -> list[int]:
    numbers = [0] * size
    for i in range(size):
        numbers[i] = i * 2
    return numbers
```
```python{*|8|6-9|11-12|19|21|*}
import cython
from cython.cimports.libc.stdlib import malloc, free


def allocation(size: cython.int = 999_999):
    numbers: cython.p_int = cython.cast(
        cython.p_int,
        malloc(size * cython.sizeof(cython.int))
    )

    if not numbers:
        raise MemoryError("Memory allocation failed")

    try:
        i: cython.int
        for i in range(size):
            numbers[i] = i * 2

        return [x for x in numbers[:size]]
    finally:
        free(numbers)
```
````

<!--
symulacja alokacji pamięci - wypełniamy zerami listę długości `size`

następnie tak utworzoną listę wypełniamy kolejnymi liczbami parzystymi

[click] jak ktoś pamięta składnię malloc w C to zauważy tu znajomą składnię

[click] robimy alokację pamięci rozmiary size * sizeof(int)

[click] wykonujemy cast na typ p_int, czyli wskaźnik na int

[click] powinniśmy ręcznie obsłużyć potencjalny z alokacją

[click] zwracaną wartość rzutujemy na pythonową listę, co zmniejsza wydajność, ale python nie poradzi sobie jak dostanie wskaźnik na int

[click] obowiązkowo też zwalniamy pamięć
-->

---

# A jak z wydajnością takiego rozwiązania?

<div v-click>
```
Running Python version...
10 loops, best of 5: 33.6 msec per loop
Running Cython version...
10 loops, best of 5: 23.7 msec per loop
```
</div>
<div v-click>
<img
  v-motion
  :enter="{ y: 0, x: 100, scale: 1 }"
  src="./img/not-great-not-terrible.gif"
  alt=""
>
</div>

<!--
nie jest źle, ale mogłoby być lepiej - konwersja na listę pythonową zabija wydajność

na przykładzie z malloc widać, że czasami kod napisany w cythonie będzie się znacznie różnił od  tego w pythonie

podobnie będzie w kolejnym przypadku, gdzie będziemy otwierać plik tekstowy i liczyć statystykę występujących w nim liter
-->

---

# Częstotliwość występowania liter w pliku

````md magic-move {at: 1, lines: true}
```python
import string
from collections import Counter
from pathlib import Path


def lettercount(filename: str = "./data/6mb-text-file.txt"):
    file_path = Path(filename)

    with file_path.open("r", encoding="utf-8") as f:
        text = f.read().lower()

    # Filter only lowercase ASCII letters and count them
    letter_counts = Counter(
        letter for letter in text 
        if letter in string.ascii_lowercase
    )

    return dict(letter_counts)
```
```python
import string
from pathlib import Path


def lettercount(filename: str = "./data/6mb-text-file.txt"):
    file_path = Path(filename)
    letter_counts = dict()

    with file_path.open("r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            for letter in line.lower():
                if letter.isupper():
                    letter = letter.lower()
                if letter in string.ascii_lowercase:
                    if letter in letter_counts:
                        letter_counts[letter] += 1
                    else:
                        letter_counts[letter] = 1

    return letter_counts
```
```python{*|2,7-9|15|23|*}
import cython
from cython.cimports.libc.stdio import fclose, fopen, FILE
from cython.cimports.posix.stdio import getline
from cython.cimports.libcpp.unordered_map import unordered_map

def lettercount(filename: bytes = b"./data/6mb-text-file.txt"):
    file = fopen(filename, b"r")

    if file is cython.NULL: return

    line: cython.p_char = cython.NULL
    l: cython.size_t = 1
    read: cython.Py_ssize_t

    letter_counts: unordered_map[cython.char, cython.int]
    letter: cython.char

    while True:
        {...}

    fclose(file)

    return {chr(key): value for key, value in letter_counts}
```
```python{*|14-15|*}
import cython
from cython.cimports.libc.stdio import fclose, fopen, FILE
from cython.cimports.posix.stdio import getline
from cython.cimports.libcpp.unordered_map import unordered_map

def lettercount(filename: bytes = b"./data/biblia-tysiaclecia.txt"):
    {...}

    while True:
        read = getline(cython.address(line), cython.address(l), file)
        if read == -1:
            break
        for letter in line:
            if 65 <= letter <= 90:
                letter = letter + 32
            if 97 <= letter <= 122:
                if letter_counts.find(letter) == letter_counts.end():
                    letter_counts[letter] = 1
                else:
                    letter_counts[letter] += 1

    fclose(file)

    return {chr(key): value for key, value in letter_counts}

```
````

<!--
Napisany w czystym Pythonie kod jest nieprzenaszalny 1:1 do C/C++ - ten napisany tutaj jest zwięzły i czytelny, bo to Python

[click] przekształcona forma czyta plik linia po linii, konwertuje pojedyncze znaki na lowercase i nie używa Countera ani nawet defaultdict - aby jak najbardziej zbliżyć się do tego, co moglibśmy napisać bez użycia pythona

co ciekawe, nie ma to wcale dużego przełożenia na performance - obydwie wykonują się między 250 a 300 ms

[click] kod przepisany na cythona przestał mieścić się na jednym slajdzie, więc pokażę go w dwóch etapach

[click] widać, że wykorzystamy otwieranie plików znane z języka C

[click] użyjemy też kolekcji `unordered_map` z C++ do zasymulowania pythonowego słownika

[click] na końcu i tak musimy przekonwertować wynik na słownik, aby wywołujący funkcję kod pythona sobie z tym poradził

[click:3] iterując po kolejnych znakach linii otrzymamy ich liczbową reprezentację, więc +32 zamiast lower
-->

---

# Częstotliwość występowania liter w pliku

Dane są sortowane alfabetycznie już po zwróceniu z funkcji, aby nie zaburzyć benchmarku

Walidacja wyników:
```
Running Python version...
{'a': 341977, 'b': 84467, 'c': 151037, 'd': 146691, 'e': 318719, 'f': 6232, 'g': 68704, 'h': 45303, 'i': 408257, 
'j': 93793, 'k': 103787, 'l': 83617, 'm': 132526, 'n': 178039, 'o': 284004, 'p': 101724, 'q': 2, 'r': 156178, 
's': 185192, 't': 125342, 'u': 82149, 'v': 95, 'w': 179369, 'x': 31, 'y': 154438, 'z': 242550}
Running Cython version...
{'a': 341977, 'b': 84467, 'c': 151037, 'd': 146691, 'e': 318719, 'f': 6232, 'g': 68704, 'h': 45303, 'i': 408257, 
'j': 93793, 'k': 103787, 'l': 83617, 'm': 132526, 'n': 178039, 'o': 284004, 'p': 101724, 'q': 2, 'r': 156178, 
's': 185192, 't': 125342, 'u': 82149, 'v': 95, 'w': 179369, 'x': 31, 'y': 154438, 'z': 242550}
```

<div v-click>
Pomiary czasowe:

```
Running Python version...
1 loop, best of 5: 271 msec per loop
Running Cython version...
20 loops, best of 5: 18 msec per loop
```
</div>

---
layout: center
class: text-center
---

<div>
<img
  src="./img/cython_everywhere.jpg"
  alt=""
>
</div>

---
layout: center
class: text-center
---

<div>
<img
  src="./img/the-evilest-thing.jpg"
  alt=""
>
</div>

---

# Kiedy nie warto używać Cythona?

<div v-click>1. Kiedy Twój problem nie leży w wydajności Pythona 🤷</div>
<div v-click>2. Kiedy Twój problem można rozwiązać bibliotekami typu numpy/pandas/polars 🐻‍❄️</div>
<div v-click>3. Kiedy Twój kod bazuje na algorytmach i strukturach danych wbudowanych w Pythona 🐍</div>
<div v-click>4. Kiedy Twój program ma być przenośny między systemami operacyjnymi 🚚</div>
<div v-click>5. Kiedy Twój program nie musi być szybki 🐌</div>
<div v-click>6. Kiedy Twój projekt musi być dowieziony szybko ⏲️</div>

<div v-click><br>Czy zatem warto w ogóle zaprzątać sobie tym głowę?</div>

<div v-click><br>Tak! Jeśli:</div>

<div v-click>1. Masz intensywne obliczeniowo operacje, które jesteś w stanie wyizolować bez użycia typów Pythona 🧩</div>
<div v-click>2. Chcesz łatwo zrównoleglić obliczenia bez ograniczeń GIL ⛓️‍💥</div>
<div v-click>3. Chcesz zintegrować się z bibliotekami języka C/C++ 🧑‍💻</div>

<!--

[click] Jeśli Cython to młotek, to nie każdy problem powinien wyglądać jak gwóźdż.

W aplikacjach webowych często wąskim gardłem jest sieć lub baza danych. Optymalizacja 200ms na 175ms będzie niezauważalna.
W przypadku Django najczęstsze optymalizacje to odpowiednio wykonane JOINy pomiędzy tabelkami w bazie danych.

Często lepszym rozwiązaniem będzie wykorzystanie asyncio.

[click] te biblioteki są już zoptymalizowane i korzystają pod spodem z C lub Rusta

[click] widzieliśmy na przykładzie zliczania liter ile kodu trzeba dopisać aby był optymalniejszy

[click] kompilator produkuje pliki .so lub .pyd w zależności od platformy

[click] Czasami wydajność nie jest kluczowa, a dodatkowa porcja wiedzy jaką musi przyswoić zespół aby utrzymywać kod w Cythonie jest niepotrzebnym narzutem

[click] wykorzystanie Cythona często spowolni development

trochę problematyczne jest to, że Cython 3, wprowadzający tryb "Pure Python" oficjalnie pojawił się w 2023 roku, więc wiele źródeł podaje rozwiązania problemów dla starszych wersji,
gdzie kod pisało się w pliku `.pyx` a nie `.py`.

-->

---

# Używasz Cythona już dzisiaj, nawet jeśli o tym nie wiesz
<div></div>
Wiele projektów znanych ze swojej szybkości wykorzystuje Cythona:

<ul>
<li v-click="1">asyncpg</li>
<li v-click="2">uvloop</li>
<li v-click="3">kivy</li>
<li v-click="4">lxml</li>
<li v-click="5">pandas</li>
<li v-click="6">scikit-learn</li>
<li v-click="7">scipy</li>
</ul>

<div>
<img
  v-click="1"
  v-motion
  :enter="{ x: 175, y: -220, scale: 0.7 }"
  src="./img/asyncpg.png"
>
<img
  v-click="2"
  v-motion
  :enter="{ x: 475, y: -320, scale: 0.7 }"
  src="./img/uvloop.png"
>
<img
  v-click="3"
  v-motion
  :enter="{ x: 575, y: -350, scale: 0.7 }"
  src="./img/kivy.png"
>
<img
  v-click="4"
  v-motion
  :enter="{ x: 575, y: -750, scale: 0.7 }"
  src="./img/lxml.png"
>
<img
  v-click="5"
  v-motion
  :enter="{ x: 215, y: -730, scale: 0.7 }"
  src="./img/pandas.png"
>
<img
  v-click="6"
  v-motion
  :enter="{ x: 315, y: -730, scale: 0.7 }"
  src="./img/scikit-learn.png"
>
<img
  v-click="7"
  v-motion
  :enter="{ x: 50, y: -930, scale: 0.7 }"
  src="./img/scipy.png"
>
</div>

<!--
asyncpg

uvloop

kivy

lxml

pandas

scikit-learn

scipy
-->

---

# Czy do pisania kodu w Cythonie potrzebna jest znajomość C?

<div v-click>
Choć nie jest to konieczne, to znajomość C/C++ może być bardzo przydatna przy korzystaniu z Cythona.
Bez znajomości C/C++ można korzystać z Cythona, ale nie można w pełni wykorzystać jego potencjału.
</div>
<div v-click>
Łatwo też wpędzić się w pułapki takie jak dzielenie liczb całkowitych czy przepełnienie typu int.

<div>
<img 
  v-motion
  :enter="{ x: 135, y: -55, scale: 0.7 }"
  src="./img/patrick.gif"
  alt=""
>
</div>
</div>

---

# Czy programista C może pisać w Cythonie bez znajomości Pythona?

<div v-click>
Praktycznie nie. Cython jest nadzbiorem Pythona, co oznacza, że korzysta z jego składni. Wykorzystanie Cythona 
bez znajomości chociażby podstaw Pythona będzie bardzo trudne.

<div>
<img 
  v-motion
  :enter="{ x: 90, y: -40, scale: 0.7 }"
  src="./img/monkey-tools.gif"
  alt=""
>
</div>
</div>

---
layout: center
class: text-center
---

# Dzięki za uwagę!

<img src="./img/any-questions.gif">

---

# Źródła

* https://cython.readthedocs.io/
* Kurt W. Smith - _"Cython. A guide for Python programmers"_, O’Reilly Media,Inc., 2015
