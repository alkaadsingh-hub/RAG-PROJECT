IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL. XX, NO. XX, XX 2018
3
7
4
19
7
34
6
5
11
4
1
11 22
7
1
4
24
7
12
7
2
1
SUM ∑
SUM ∑
2
2
2
2
1
1
1
4
2
2
2
2
3
12
7
2
8
2
1
4
2
1
1
4
4
2
2
1
1
1
1
1
1
3
2
1
1
1
1
1
1
1
1
1
Before
2011
2012
2013
2014
2015
2016
2017
2018
2019
2020
Artificial Intelligence
Computer Graphics
Computer Vision
Data Mining
Databases
Human-computer Interaction
Natural Language Processing
Programming Languages
Visualization
Web & Information Retrieval
98
Fig. 2. The number of papers per research area and per year.
these starting points with papers covered in related surveys [20]–
[23]. If a paper is selected to be included, we traverse both its
references and citations. We search for papers breadth-ﬁrst in an
attempt to avoid over-focus on one particular line of research.
Our relation-search method results in an interdisciplinary
corpus consisting of 98 papers from 10 research areas. We decide
the research area of each paper according to the classiﬁcation of
computer science areas by CSRankings1. Figure 2 lists the research
areas, indicating the interdisciplinary nature and widespread
popularity of visualizations. The primary area is Visualization,
accounting for around one-third (34/98). The next areas are
Human-computer Interaction and Databases. Besides, we see
research efforts from Artiﬁcial Intelligence, Data Mining, Computer
Graphics, and the Web & Information Retrieval.
Another ﬁnding is the increasing trend of applying AI methods
for data visualization. Figure 2 shows that the total number of
publications has been increasing steadily over the last decade,
particularly with a surge since 2018 and a peak at 2020. Given the
wide and ever-growing research efforts and interests, we believe
that this topic will receive more attention in the near future.
We acknowledge the limitations of our search methodology
which is based on manual search over citation and reference graphs.
Consequently, our survey should be seen as an effort in investigating
the diversity of related research, providing sufﬁcient research
instances to contextualize the current research landscape, and
indicating future research opportunities. As such, we do not claim
comprehensiveness nor exhaustiveness. Instead, future research
could augment the corpus by automated graph traversal.
3.3
Coding and Classiﬁcation
Figure 1 provides an overview of our classiﬁcations of surveyed
papers, which is organized according to the what-why-how axes.
This organization is well-established in visualization-related sur-
veys [15], [26]. Nevertheless, we introduce two modiﬁcations to
the “what” and “how” axes in order to contextualize our discussion
in AI4VIS research.
Firstly, from the “what” perspective, we discuss not only
what visualization data is but also its representation (section 4).
For representation, we review internal representations (how vi-
sualization data is stored and operated in systems) and feature
representation (how visualizations are converted into features that
are mathematically and computationally convenient for analysis).
1. http://csrankings.org/
Secondly, from the “how” perspective, we organize approaches
with a novel task abstraction. We identify seven common tasks
for AI4VIS research and discuss approaches for each task in
section 6. Our motivations for such task abstractions are two-fold:
• Reconciling techniques with system papers. We ﬁnd our
corpus a mixture of technique and system papers that confound
the discussion. A technique paper typically solves a single task,
while a system paper could consist of multiple components,
each for different tasks [17]. As such, we aim to decompose
system papers into abstract tasks that allow for a collectively
exhaustive taxonomy of tasks.
• Unifying Inconsistent Vocabularies. Due to the interdis-
ciplinary nature of our corpus, we ﬁnd tasks are usually
described in inconsistent vocabularies. For instance, the task
of extracting encoding choices from visualization images or
speciﬁcations is described as deconstruction [1], [2] or chart
mining [23]. Thus, we wish to establish a common vocabulary
that enables consistent discussions for researchers from
different areas to communicate the relevance and subtleties.
For the above purposes, we adopted a bottom-up approach by
iteratively categorizing and labeling the tasks in surveyed papers.
Thanks to the interdisciplinary nature of our corpus, we were
able to start from several “seeding” tasks by referring to task
taxonomy in other ﬁelds [28]. Subsequently, two authors labelled
and veriﬁed whether the task could map to existing categories, and
if not applicable, discussed alternative task categorizations with
the remaining authors. Conﬂicts of labels were also discussed until
reaching a consensus. During the labeling process, we found that
most tasks conformed to the “seeding” terms with few exceptions
that reﬂected the peculiarity of visualizations. For exceptions,
we discussed candidate terms in surveyed literature to select
tasks that were understandable and widely communicated (e.g.,
recommendation). We discuss details of the task taxonomy in
section 6.
Our supplemental website, available at ai4vis.github.io, pro-
vides the details of our labels. Particularly, we label tasks at the
(sub-)section level, and provide quotes from the paper to help
readers understand why it falls into the task category. The website
also provides an overview of the surveyed paper. In the following
text, citations refer to all instances for the reported category, except
where noted otherwise by phrases such as “for instance” or “like”.
4
DATA: WHAT IS VISUALIZATION DATA
In this section, we formalize the concept of visualization data.
Speciﬁcally, we discuss and categorize visualization data in
terms of its raw data format (subsection 4.1) and representations
(subsection 4.2). As shown in Figure 3, we classify visualization
data formats into graphics, programs, and hybrid that blends the
beneﬁts of both. In addition to raw data, we note visualizations
are sometimes represented as carefully designed internal repre-
sentation formats in surveyed systems. Internal representations
are usually proposed to facilitate the computing by removing
unnecessary information, e.g., the VQL format [29] only stores
data transformation and encoding without style information. As
such, internal representations are usually not exposed (outputted
and shared). Finally, we review feature presentations, including
feature engineering and feature learning. Feature presentations
are vital for machine learning tasks by concerting visualizations into
features that are mathematically and computationally convenient to
analyze. We discuss them due to the increasing interest in applying
machine learning to visualizations.
