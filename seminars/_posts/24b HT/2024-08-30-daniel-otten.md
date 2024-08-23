---
speaker: Daniël Otten
affil: University of Amsterdam
title: Cyclic Type Theory
date: 2024-08-30 10:15:00 +02:00
location: J577
---

We explain some of the connections between two research areas: cyclic proof theory and proof assistants.
This talk is based on joint work-in-progress with Lide Grotenhuis.

In cyclic proof theory, we replace induction axioms with circular reasoning.
By carefully placing restrictions on cycles, we can make sure that we do not prove more than with induction.
Such cyclic proofs can be interpreted as programs using the Curry-Howard correspondence: cycles correspond to recursive calls, while the restrictions make sure that the program always terminates.
Using this perspective, we show how the type theory implemented by proof assistants can be seen as a cyclic proof system: one where programs/proofs are defined using (co)pattern matching.
We show some of the difficulties that come up specifically in dependent type theory: why unification becomes important, and how one can translate cyclic proofs to inductive proofs while preserving computational behavior.
In addition, we show how some of the techniques from cyclic proof theory might be used to extend proof assistants.