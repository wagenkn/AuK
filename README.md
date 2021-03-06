
<img align="left" width="300" src="https://www.hszg.de/typo3conf/ext/pt_hszg_site/Resources/Public/Images/HZG_Logo.svg"/>
<!-- alternativ: http://unternehmerverband-auv.de/fileadmin/user_upload/csm_HZG_Logo_100_RGB_11eefdbf4a.png -->
<img align="right" width="300" src="http://www.hszg.de/fileadmin/template/HSZG/imgs/logo/Logo-F-EI.gif"/>

<br>
<br>
<br>
<br>

# Algorithmen und Komplexität

## Beschreibung

Dieses Material wird im Modul **[Algorithmen und Komplexität](https://web1.hszg.de/modulkatalog/index.php?mid=3532&uid=11&uidaus=11&uid1=11&start=0&activTopic=4&activNav=5&letter=w&kennz=ausgabe&y=1)** ([Prof.Dr.Christian Wagenknecht](https://www.hszg.de/f-ei/fakultaet/professoren/christian-wagenknecht/person.html)) verwendet. Es ist in Kapitel gegliedert. An welcher Stelle das jeweilige Kapitel behandelt wird, ergibt sich aus der didaktischen Konzeption und wird in der Studierendengruppe besprochen.

Dieses Modul soll in die Entwicklung und Analyse von Algorithmen einführen. Zudem lernen Sie wichtige Datenstrukturen kennen, die für das Lösen von algorithmischen Problemen relevant sind. 

Für alle Kapitel gibt es je ein JupyterNotebook, mit dem benötigte theoretische Grundlagen erläutert und Beispiele in Form grundlegender Algorithmen und passender Datenstrukturen gezeigt und mit editierbaren Python-Programmen implementiert werden. Haben Sie sich durch ein Kapitel hindurch gearbeitet, so stehen Übungsaufgaben bereit, die Sie lösen und anschließend mit den Musterlösungen vergleichen können.

Zur Erarbeitung und Erprobung der JupyterNotebooks haben die Herren D. Weiß und R. Zücker maßgeblich beigetragen. Uns war es sehr wichtig,  "die Sprache der Studierenden" zu treffen, um einen attraktiveren Zugang zu den mathematisch-algorithmischen Inhalten zu finden.

## Technische Voraussetzungen

### JupyterNotebooks herunterladen

Zur Nutzung der JupyterNotebooks ist eine *lokale* Installation von Anaconda auf Ihrem Laptop notwendig. Die hier bereitgestellten JupyterNotebooks laden Sie entweder als ZIP-Datei herunter und expandieren sie in ein geeignetes lokales Verzeichnis. Oder Sie installieren git (verteiltes Versionskontrollsystem) und clonen das gesamte Repository in einem Schritt. Letzteres ist zur begleitenden Aktualisierung der Materialien von Vorteil, aber nicht Bedingung. Grüner Knopf oben: clone or download. 

### Anaconda Installation

Es ist empfehlenswert Jupyter zusammen mit der [Anaconda Distribution](https://www.anaconda.com/download/) zu 
installieren, da sie außer Python selbst und Jupyter noch weitere wichtige Pakete zum wissenschaftlichen Rechnen, wie 
[NumPy](http://www.numpy.org/) oder [Pandas](https://pandas.pydata.org/), beinhaltet.

Haben Sie etwas Geduld: Der Installationsvorgang kann relativ lange (< 15 min.) dauern. Wenn Ihr Laptop nicht mehr so ganz leistungsstark ist, können Sie alternativ [Miniconda](https://conda.io/miniconda.html) verwenden.

Nach erfolgreicher Installation von Anaconda steht auch Jupyter bereit!

#### Ggf.(!) das Arbeitsverzeichnis von jupyter verändern:
1. Anaconda prompt: jupyter notebook --generate-config
2. In der (damit angelegten) Datei  C:\Users\User\.jupyter\jupyter_notebook_config.py den folgenden Eintrag anpassen:
    #c.NotebookApp.notebook_dir = 'D:/Repositories/'
Wichtig (Windows): Angabe des Pfades mit ' und /, wie im Beispiel
3. `#` am Anfang entfernen und speichern
4. AnacondaNavigator starten
5. Jupyter aufrufen

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


Der Jupyter Server läuft nun lokal unter http://localhost:8888/...  

