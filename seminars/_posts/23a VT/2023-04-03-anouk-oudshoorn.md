---
speaker: Anouk Oudshoorn
affil: TU Wien
title: Reconciling SHACL and Ontologies
date: 2023-04-03 10:15:00 +02:00
location: room J577
---
The World Wide Web Consortium (W3C) set Web Ontology Language (OWL) and Shape Constraint Language (SHACL) as international standards for managing semantically enriched data on the web.
However, there is a difference in how these languages handle the completeness of data.
In OWL, not all information has to be explicitly present; part of the information can be implied by logical rules.
Whereas SHACL, which enables us to check for certain structures in a given knowledge graph, assumes completeness of it.
Thus, with SHACL we can validate the given data, while with OWL we can infer knowledge.
Combining the functionalities of the two into one standard is relevant and not straightforward.
<!--more-->

In this seminar talk, we will introduce a new semantics for validating stratified SHACL constraints, a specific family of queries, in presence of an ontology.
We developed a refined chase technique, producing for each ontology a minimal model, i.e., a labeled graph, in which we can evaluate SHACL constraints.
However, this technique might still produce infinite models.
This can be avoided by rewriting the SHACL constraints with respect to the ontology, resulting in a standalone set of SHACL constraints that can directly be verified only over the data; our second contribution.
