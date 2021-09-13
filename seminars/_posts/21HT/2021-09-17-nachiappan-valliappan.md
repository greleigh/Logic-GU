---
speaker: Nachiappan Valliappan
affil: Chalmers
title: Normalization for Fitch-style Modal Lambda Calculi
date: 2021-09-17 10:15:00 +02:00
---
Fitch-style modal lambda calculi (Borghuis 1994; Clouston 2018) provide a solution to programming necessity modalities in a typed lambda calculus by extending the typing context with a delimiting operator (denoted by a lock). The addition of locks simplifies the formulation of typing rules for calculi that incorporate different modal axioms, but obscures weakening and substitution, and requires tedious and seemingly ad hoc syntactic lemmas to prove normalization.
<!--more-->

In this work, we take a semantic approach to normalization, called Normalization by Evaluation (NbE) (Berger and Schwichtenberg 1991), by leveraging the possible world semantics of Fitch-style calculi. We show that NbE models can be constructed for calculi that incorporate the K, T and 4 axioms, with suitable instantiations of the frames in their possible world semantics. In addition to existing results that handle beta reduction (or computational rules), our work also considers eta expansion (or extensional equality rules).

References:

- Borghuis, V.A.J. (1994). "Coming to terms with modal logic : on the interpretation of modalities in typed lambda-calculus".
- Clouston, Ranald (2018). "Fitch-Style Modal Lambda Calculi".
- Berger, Ulrich and Helmut Schwichtenberg (1991). "An Inverse of the Evaluation Functional for Typed lambda-calculus".
