
<img align="left" width="300" src="http://unternehmerverband-auv.de/fileadmin/user_upload/csm_HZG_Logo_100_RGB_11eefdbf4a.png"/>
<img align="right" width="300" src="http://www.hszg.de/fileadmin/template/HSZG/imgs/logo/Logo-F-EI.gif"/>

<br>
<br>
<br>
<br>

# Algorithmen und Komplexität

Es handelt sich um Material, welches im Modul **[Algorithmen und Komplexität](https://web1.hszg.de/modulkatalog/index.php?mid=3532&uid=11&uidaus=11&uid1=11&start=0&activTopic=4&activNav=5&letter=w&kennz=ausgabe&y=1)** verwendet wird.

Dieses Modul soll in die Entwicklung und Analyse von Algorithmen einführen. Zudem lernen Sie wichtige Datenstrukturen kennen, die für das Lösen von algorithmischen Problemen wichtig sind. 

Für alle 14 Kapitel, gibt es je ein JupyterNotebook, mit dem benötigte theoretische Grundlagen erläutert und Beispiele in Form von praktischen Algorithmen und Datenstrukturen gezeigt und implementiert werden. Haben Sie sich durch ein Kapitel durchgearbeitet, so stehen Übungsaufgaben bereit, die Sie lösen und anschließend mit den Musterlösungen vergleichen können.

Die Notebooks wurden von zwei Studierenden (Herrn Weiß, Bachelorstudent, und Herrn Zücker, Masterstudent) mit sehr guten Studienleistungen auch auf der Basis vorhandener Materialien entworfen und anschließend von Prof. Wagenknecht überarbeitet. Uns war es sehr wichtig, dass "die Sprache der Studierenden" verwendet wird, um einen attraktiveren Zugang zu den mathematisch-algorithmischen Inhalten zu gewährleisten.

<!-- # Installation -->

 <!-- ### Repository Checkout

```
git clone https://github.com/hszg-algodat/algorithmen-und-komplexitaet
```
-->

### JupyterNotebooks herunterladen

Laden Sie die komplette [Zip-Datei](https://github.com/wagenkn/AuK/archive/master.zip) herunter und expandieren Sie sie in ein geeignetes lokales Verzeichnis.


### Anaconda Installation

Es ist empfehlenswert Jupyter zusammen mit der [Anaconda Distribution](https://www.anaconda.com/download/) zu 
installieren, da es außer Python selbst und Jupyter noch weitere wichtige Pakete zum wissenschaftlichen Rechnen, wie 
[NumPy](http://www.numpy.org/) oder [Pandas](https://pandas.pydata.org/), beinhaltet.

Nach erfolgreicher Installation von Anaconda steht auch Jupyter bereit!

### Starten von Jupyter

#### Windows

Starten Sie Jupyter Notebook im Anaconda-Unterverzeichnis aus der App-Liste. Navigieren Sie in das Verzeichnis, in das Sie die vorbereiten Notebooks gespeichert haben.

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

