---
speaker: Fredrik Engström
affil: FLoV
title: Foundational principles of team semantics
date: 2021-10-29 10:15:00 +02:00
---
Team semantics is, when compared to standard Tarskian semantics, a more
expressive framework that can be used to express logical connectives,
operations and atoms that can't be expressed in Tarskian semantics. This
includes branching quantifiers, notions of dependence and independence, trace
quantification in linear-time temporal logic (LTL), and probabilistic notions
from quantum mechanics.  

Team semantics is based on the same notion of structure as Tarskian semantics,
but instead of a single assignment satisfying a formula (or not), in team
semantics a set, or a *team*, of assignments satisfies a formula (or not). In
other words, the semantic value of a formula is lifted from a set of
assignments (those that satisfy the formula) to a set of teams of
assignments. 
<!--more-->

In almost all (with only one exception that I'm aware of) logical systems
based on team semantics this lifting operation is the power set operation,
and as a result the set of teams satisfying a formula is closed downwards.
This is often taken as a basic and foundational principle of team
semantics. 

In this talk I will discuss this principle and present some ideas on why, or
why not, the power set operation is the most natural lift operation. By using
other lift operations we can get a more powerful semantics, but, it seems,
also a more complicated one. 

References:

- Engström, F. (2012) "Generalized quantifiers in dependence logic"
- Nurmi, V. (2009) "Dependence Logic: Investigations into Higher-Order
  Semantics Defined on Teams"
- Väänänen, J. (2007) "Dependence logic: A new approach to independence
  friendly logic"