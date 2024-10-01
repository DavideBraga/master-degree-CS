#import "problem_template.typ": template, title, example_file, display_subtasks_table, subtasks_usage
#show: template

#title

In principio era il logos, e ti vennero comunicati due numeri interi positivi $n$ e $k$.
Miliardi di anni dopo, rinchiuso in un qualche laboratorio, credi che nell'intervallo chiuso $[1,n]$ sia ricompreso un misterioso numero intero $x$ che devi assolutamente individuare.
Puoi porre domande del tipo "l'è miga $y$?" con $y$ un intero in $[1,n]$. Sai che alla tua $i$-esima domanda risponderà lo strumento $i % k$, ossia lo strumento che ha per nome il resto della divisione di $i$ per $k$. In altre parole, le domande vengono smistate in round robin sui $k$ strumenti. 
Le risposte constano di un singolo carattere nell'alfabeto ${<,>,=}$. Otterrai '$=$' se e solo se $y=x$.
Altrimenti, dipende ...
Se davvero vuoi risolvere tutti i subtask allora devi sapere che, in alcuni di essi, alcuni strumenti dicono ancora sempre il vero, ma altri sono _bugiardi incalliti_ e rispondono _consistentemente_ '$<$' *quando invece* $x>y$ e '$>$' *quando invece* $x<y$.

In ogni caso, vedi di non sprecare domande (riferisciti al criterio del caso peggiore).


== Protocollo di comunicazione

Il tuo programma interagirà col server leggendo dal proprio canale `stdin` e scrivendo sul proprio canale `stdout`.
La prima riga di `stdin` contiene $T$, il numero di testcase da affrontare.
All'inizio di ciascun testcase, trovi sulla prossima riga di `stdin` i tre numeri $n$, $k$ e $b$ separati da spazio. Il valore $b=0$ indica che tutti gli strumenti dicono il vero, mentre $b=1$ significa che ciascuno di loro (presi indipendentemente) potrebbe o dire sempre il vero o essere un mentitore seriale (deve ammettere il vero solo quando gli si chiede se $x=x$, come se lavorasse ad ordinamento invertito).
Inizia ora un loop che durerà fino a quando tu non sia sicuro di conoscere il numero misterioso $x$.
Non appena conoscerai con certezza l'identità di $x$ puoi chiudere il testcase in corso scrivendo su `stdout` una stringa che inizi per "!" seguito dal numero $x$. Altrimenti puoi sottoporre la tua prossima domanda per il testcase corrente scrivendo su `stdout` una stringa che inizi per "?" seguito da un numero ricompreso nell'intervallo chiuso $[1,n]$. In questo secondo caso dovrai raccogliere da `stdin` la risposta del server:
una riga di un singolo carattere nell'alfabeto ${<,>,=}$.

*Nota 1:* Ogni tua comunicazione verso il server deve essere collocata su una diversa riga di `stdout` e ricordati di forzarne l'invio immediato al server effettuando un flush del tuo output!

*Nota 2:* Il tuo dialogo diretto col server (ossia ancora prima di aver scritto una sola riga di codice) può aiutarti ad acquisire il corretto protocollo di comunicazione tra il server e il tuo programma. Verrai così anche a meglio conoscere il problema e sarai più pronto a progettare come condurre la fase di codifica. Verrai anche a meglio conoscere come gioca il server, il quale adotta una strategia adattiva per metterti alla prova secondo il criterio del caso peggiore. Il file `results.txt` verrà comunque scaricato nel folder `output` alla fine dell'interazione col server se la termini con `Ctrl`-`D`.

*Nota 3:* Per promuovere il dialogo diretto offriamo un servizio aggiuntivo che puoi chiamare con:

```
    rtal -s <URL>  connect -x <token> ricerca_binaria umano -a t=1 -a n=10 <inserisci_qua_altri_argomenti>
```

Non solo ti darà agio di dialogare nei tuoi tempi ma il suo comportamento può essere meglio parametrizzato attraverso i parametri aggiuntivi opzionali:
```
  -a t=1      per settare ad 1 (o altri valori) il numero di testcase
  -a n=1      per settare ad 1 (o altri valori) l'estremo destro n
  -a k=1      per settare ad 1 (o altri valori) il numero di strumenti k
  -a extra=1  per settare ad 1 (o altri valori) l'eccesso di domande concesso
  -a bugiardi=b  con b=0: nessun bugiardo; b=1: tutti bugiardi; b=2: sceglie il server con strategia adattiva
```

#pagebreak()


== Esempio

Le righe che iniziano con '?' o '!' sono quelle inviate dallo studente o da suo programma, le altre sono quelle inviate dal server. Inoltre: di ciascuna riga è di mero commento quella parte che comincia col primo carattere di cancelletto '\#'.

#example_file("example.int.txt") 

== Subtask

Il tempo limite per istanza (ossia per ciascun testcase) è sempre di $1$ secondo.

I testcase sono raggruppati nei seguenti subtask.

#display_subtasks_table

#subtasks_usage


