---
layout: page
title:  Workshop on Fixed Points and Ill-founded Proofs
permalink: events/wofpip
---
{% assign logic-ML = site.data.links['gu-mailing-list'].url %}
{% assign contact = site.data.people['dominik'].name %}
{% assign contact-email = site.data.people['dominik'].email %}

<!-- Some dangerous hackery here -->
![Logo](/assets/WoFPIP.svg){: height="66" style="float: left"} <br/>
University of Gothenburg, April 27-28, 2023.

**TODO** **TODO** Some blurb about Jormungandr **TODO** **TODO**

## Location
The workshop will take place at the [Humanities faculty building](https://www.openstreetmap.org/?mlat=57.69438&mlon=11.98496#map=19/57.69438/11.98496) of the
University of Gothenburg. It is located next to the Korsvägen transport hub and
within walking distance from the city centre.

## Schedule

#### Thursday, April 27th

<table>
<colgroup>
<col width="10%" />
<col width="80%" />
<col width="10%" />
</colgroup>
<thead>
<tr class="header">
<th>Time</th>
<th>Occasion</th>
<th>Location</th>
</tr>
</thead>
<tbody>
<!--   Thursday morning   -->
<tr>
<td markdown="span">9:30</td>
<td markdown="span">Welcome fika</td>
<td rowspan="4">J411</td>
</tr>
<tr>
<td markdown="span">10:00</td>
<td markdown="span">Talk: Anupam Das</td>
</tr>
<tr>
<td markdown="span">11:00</td>
<td markdown="span">Talk: Lide Grotenhuis <br/> _Ill-founded proofs for intuitionistic linear-time temporal logic_</td>
</tr>
<tr>
<td markdown="span">11:40</td>
<td markdown="span">Talk: Dominik Wehr<br/>_Ordinal annotations for cyclic first-order arithmetics_</td>
</tr>

<tr>
<td markdown="span">12:30</td>
<td markdown="span">Lunch</td>
<td markdown="span">Cafeteria</td>
</tr>

<!--   Thursday afternoon   -->
<tr>
<td markdown="span">14:00</td>
<td markdown="span">Talk: Guillermo Menéndez Turata</td>
<td rowspan="3">J444</td>
</tr>
<tr>
<td markdown="span">14:40</td>
<td markdown="span">Talk: Giacomo Barlucchi</td>
</tr>
<tr>
<td markdown="span">15:15</td>
<td markdown="span">Fika</td>
</tr>
</tbody>
</table>

#### Friday, April 28th

<table>
<colgroup>
<col width="10%" />
<col width="80%" />
<col width="10%" />
</colgroup>
<thead>
<tr class="header">
<th>Time</th>
<th>Occasion</th>
<th>Location</th>
</tr>
</thead>
<tbody>
<!--   Friday morning   -->
<tr>
<td markdown="span">10:00</td>
<td markdown="span">Talk: Sebastian Enqvist (abstract below)<br/> _Herbrand meets cyclic proofs_
</td>
<td rowspan="3">J442</td>
</tr>
<tr>
<td markdown="span">10:40</td>
<td markdown="span">Talk: Johannes Kloibhofer</td>
</tr>
<tr>
<td markdown="span">11:20</td>
<td markdown="span">Talk: Gianluca Curzi (abstract below)<br/>_On the computational expressivity of (circular) proofs with fixed points_</td>
</tr>

<tr>
<td markdown="span">12:00</td>
<td markdown="span">Lunch</td>
<td markdown="span">Cafeteria</td>
</tr>

<tr>
<td markdown="span">14:00</td>
<td markdown="span">[Licentiate defense](https://www.logic-gu.se/seminars#licentiate-defence-dominik-wehr-representation-matters-in-cyclic-proof-theory): Dominik Wehr (opponent: Anupam Das)<br/>_Representation matters in cyclic proof theory_</td>
<td markdown="span">J439</td>
</tr>

<tr>
<td markdown="span">16:00</td>
<td markdown="span">Reception with coffee and cake</td>
<td markdown="span">FLoV</td>
</tr>

<tr>
<td markdown="span">19:00</td>
<td markdown="span">Workshop dinner</td>
<td markdown="span">TBA</td>
</tr>

</tbody>
</table>

## Workshop dinner

On Friday evening, there will be a workshop dinner. More details to follow.

## Abstracts

#### Sebastian Enqvist: Herbrand meets cyclic proofs

Herbrand's theorem provides a sort of computational content to classical logic.
A standard way to prove it uses cut elimination in sequent calculus. In recent
work by Afshari, Hetzl and Leigh, it was shown how to extract Herbrand
disjunctions directly from sequent calculus proofs without eliminating cuts
first. The idea is to associate a higher-order recursion scheme with a given
proof, from which a set of witnessing terms can be extracted. In this talk I
will present ongoing work, joint with Bahareh Afshari and Graham Leigh, in which
we show how such "Herbrand schemes" can be adapted to provide a method for
witness extraction from cyclic sequent calculus proofs in the setting of the
classical theory of inductively defined predicates. Indeed, this is a quite
natural step to take, as recursion schemes in general are cyclic structures.

#### Gianluca Curzi: On the computational expressivity of (circular) proofs with fixed points

We study the computational expressivity of proof systems with fixed point
operators, within the 'proofs-as-programs' paradigm. We start with a calculus
muLJ (due to Clairambault) that extends intuitionistic logic by least and
greatest positive fixed points. Based in the sequent calculus, muLJ admits an
extension to a 'circular' calculus CmuLJ in a standard way.

Our main result is that, perhaps surprisingly, both muLJ and CmuLJ represent the
same first-order functions: those provably total in Pi12-CA0, a subsystem of
second-order arithmetic beyond the 'big five' of reverse mathematics and one of
the strongest theories for which we have an ordinal analysis (due to Rathjen).
This solves various questions in the literature on the computational strength of
(circular) proof systems with fixed points.

For the lower bound we give a realisability interpretation from an extension of
Peano Arithmetic by fixed points that has been shown to be arithmetically
equivalent to Pi12-CA0 (due to Möllerfeld). For the upper bound we give a novel
totality argument for circular proofs with fixed points. In fact we must
formalise this argument itself within Pi12-CA0 in order to obtain the tight
bounds we are after, requiring a choice of higher computability model distinct
from usual type structures for second-order systems (such as Girard-Reynolds'
F). Along the way we develop some novel reverse mathematics for the
Knaster-Tarski fixed point theorem.
