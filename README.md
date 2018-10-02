
<img align="left" width="300" src="http://unternehmerverband-auv.de/fileadmin/user_upload/csm_HZG_Logo_100_RGB_11eefdbf4a.png"/>
<img align="right" width="300" src="http://www.hszg.de/fileadmin/template/HSZG/imgs/logo/Logo-F-EI.gif"/>

<br>
<br>
<br>
<br>

# Algorithmen und Komplexität

XXXXXMaterial, welches im Rahmen des Moduls **Algorithmen und Komplexität** an der Hochschule Zittau/Görlitz verwendet wird.

Dieses Modul soll in die Entwicklung und Analyse von Algorithmen einführen. Zudem lernen Sie wichtige Datenstrukturen kennen, die für das Lösen von algorithmischen Problemen wichtig sind.

Es gibt 13 Kapitel. Zu jedem gibt es ein Jupyter Notebook, bei welchem benötigte theoretische Grundlagen erläutert und Beispiele in Form von praktischen Algorithmen und Datenstrukturen gezeigt und implementiert werden. Haben Sie sich durch ein Kapitel durchgearbeitet, so stehen Übungsaufgaben bereit, die Sie lösen und anschließend mit den Musterlösungen abgleichen können.

# Installation

### Repository Checkout

```
git clone https://github.com/hszg-algodat/algorithmen-und-komplexitaet
```

### Anaconda Installation

Es ist empfehlenswert Jupyter zusammen mit der [Anaconda Distribution](https://www.anaconda.com/download/) zu 
installieren, da es außer Python selbst und Jupyter noch weitere wichtige Pakete zum Wissenschaftlichen Rechen, wie 
[NumPy](http://www.numpy.org/) oder [Pandas](https://pandas.pydata.org/), beinhaltet.

Der Installer für Anaconda kann **[hier](https://www.anaconda.com/download/)** heruntergeladen werden.

Nach erfolgreicher Installation von Anaconda ist Jupyter installiert!

### Starten von Jupyter

#### Windows

- Windows Suche: Anaconda Prompt
- Starten von Anaconda Prompt
- In das Verzeichnis, wo sich das Repository mit den Jupyter Notebooks befindet, navigieren 

Befehl in Anaconda Prompt:
```
jupyter notebook
```

#### Linux

```
bash Anaconda3-5.2.0-Linux-x86_64.sh
```
- `Do you wish the installer to prepend the Anaconda3 install location
  to PATH in your /home/sammy/.bashrc ? [yes|no]` mit `yes` antworten
- Nach Abschließen der Installation Terminal schließen und neustarten

```
conda update conda
```

- In das Verzeichnis, wo sich das Repository mit den Jupyter Notebooks befindet, navigieren 

```
jupyter notebook
```

#### Mac

- Starten von Anaconda Navigator unter Applications/anaconda/Navigator
- Klick auf 'Launch' unter Jupyter Notebook


Der Jupyter Server ist nun gestartet und kann im Browser über **http://localhost:8888** aufgerufen werden.

