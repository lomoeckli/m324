a.out: main.cpp
	g++ main.cpp

# 3.2 Was muss getan werden, damit die Kompillierung nur durchläuft, wenn das File main.cpp auch existiert?
# Nach a.out: das File (main.cpp) angeben. Also so: a.out: main.cpp

# 3.3 Mit welchem Befehl kann das Programm via Makefile kompilliert werden?
# Mit g++ main.cpp

# 3.4 Was passiert, wenn dieser Befehl nochmals ausgeführt wird?
# Grundsätzlich nichts, da sich an main.cpp auch nichts geändert hat. Wenn man das Makefile also nochmals mit make ausführt,
# dann erhält man in der Konsole nur diese Ausgabe: make: 'a.out' is up to date.

# 3.5 Ändere die Ausgabe im C++ Programm auf “Compiled by Makefile”. Was passiert, 
# wenn der Befehl aus den vorhergehenden Aufgaben nochmals ausgeführt wird?
# Das main.cpp File wurde geändert und wird nun deshalb neu kompiliert.
# Wenn man dann mit ./a.out die Datei ausliest, steht neu "Compiled by Makefile" und nicht mehr "Hi from C++" in der Konsole.