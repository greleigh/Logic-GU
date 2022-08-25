---
speaker: Mauricio Martel
affil: CSE, GU
title: On the Complexity of Conservative Extensions in the Two-Variable Guarded Fragment
date: 2022-06-03 10:15:00 +02:00
---

Conservative extensions are a fundamental notion in logic. In the area of description logic, deciding whether a logical theory is a conservative extension of another theory is a fundamental reasoning problem with applications in ontology engineering tasks, such as ontology modularity, ontology reuse and ontology versioning. It has been observed in recent years that conservative extensions are decidable in many modal and description logics, given that they can often be characterized elegantly in terms of appropriate notions of bisimulations. But no work has been done for more expressive logics such as the two-variable fragment and the guarded fragment, which are considered to be generalizations of modal and description logics, and are typically used to explain their good computational behavior.<!--more-->

In this talk, I attempt to fill this gap by considering the decidability of conservative extensions in the two-variable guarded fragment (<sc>gfo2</sc>). I will show that conservative extensions are decidable in <sc>gfo</sc>2 and that the computational complexity is 2<sc>exptime</sc>-complete. To prove these results I will rely on an automata-based approach, which consists in first giving a model-theoretic characterization of conservative extensions in terms of guarded bisimulations, to then use it as a foundation for a decision procedure based on tree automata. Since the usual notion of guarded bisimulations fail to characterize conservative extensions in <sc>gfo2</sc>, I will report on alternative model-theoretic characterizations in terms of bounded guarded bisimulations and the challenge of combining them with automata techniques.

This talk is based on joint work with Carsten Lutz, Jean Christoph Jung, Thomas Schneider, and Frank Wolter: <https://drops.dagstuhl.de/opus/volltexte/2017/7464/pdf/LIPIcs-ICALP-2017-108.pdf>
