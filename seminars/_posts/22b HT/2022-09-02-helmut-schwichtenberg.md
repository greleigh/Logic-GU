---
speaker: Helmut Schwichtenberg
affil: LMU Munich
title: A theory of computable functionals
date: 2022-09-02 10:15:00 +02:00
---
We describe a theory of computable functionals (TCF) which
extends Heyting's arithmetic in all simple types by (i) adding
inductively and coinductively defined predicates, (ii) distinguishing
computationally relevant (c.r.) and non-computational (n.c.)
predicates, (iii) adding realizability predicates, and (iv) allowing
partial functionals defined by equations (possibly non-terminating,
like corecursion).  The underlying (minimal) logic has just
implication and universal quantification as primitive connectives;
existence, disjunction and conjunction are inductively defined.  The
axioms of TCF are the defining axioms for (co)inductive predicates,
bisimilarity axioms and invariance axioms stating that ''to assert is
to realize'' (Feferman 1978) for realizability-free formulas.  Using
these one can prove in TCF a soundness theorem: the term extracted
from a realizability-free proof of a formula A is a realizer of A.
TCF is implemented in the Minlog proof assistant.
