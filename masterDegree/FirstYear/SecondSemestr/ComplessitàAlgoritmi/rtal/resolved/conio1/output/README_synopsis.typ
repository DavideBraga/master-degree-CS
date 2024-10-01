When you are working on problem <problem_name> and you want to find out about the services the problem-maker has set up for you, issue the following:

```bash
rtal connect BFS synopsis
```

Here, `synopsis` is an universal service of our collection of problems meant to provide semantic problem-specific informations about the available services and their possible arguments.

To know how to use it in the concrete, apply it to itself with, for example:

```bash
rtal connect accensione synopsis -a service=synopsis
```

Nota: il servizio synopsis offre una rendition efficace delle informazioni altrimenti contenute nel file meta.yaml del problema.

