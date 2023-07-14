# Algorytm-Kruskala
Algorytm Kruskala – algorytm grafowy wyznaczający MST (minimalne drzewo rozpinające) dla grafu nieskierowanego ważonego.

Inicjalizuje on zbiór wierzchołków (**V**), krawędzi (**E**) i wag (**W**). Następnie tworzy poszczególne zbiory dla każdego wierzchołka za pomocą funkcji **make_set**. Krawędzie są sortowane w porządku niemalejącym na podstawie wag przy użyciu funkcji **get_weight**.

Następnie algorytm konstruuje minimalne drzewo rozpinające (**A**), iterując po posortowanych krawędziach. Dla każdej krawędzi sprawdza, czy wierzchołki **u** i **v** należą do różnych zbiorów za pomocą funkcji **find_set**. Jeśli tak, krawędź jest dodawana do MST (**A**), a zbiory są scalane przy użyciu funkcji **union**.

Na koniec MST (**A**) jest wypisywane jako wynik działania algorytmu.

![kruskal1](https://github.com/maxyymmm/Algorytm-Kruskala/assets/120425774/d3c3b8d5-681e-4567-88c4-7a8f779c183b)
![kruskal2](https://github.com/maxyymmm/Algorytm-Kruskala/assets/120425774/47cfabf1-c859-483c-838f-c1dc15bad749)
