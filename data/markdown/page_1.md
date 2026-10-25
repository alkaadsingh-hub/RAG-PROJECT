IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL. XX, NO. XX, XX 2018
2
Goal
Visualization 
Generation
Visualization
Enhancement
Visualization 
Analysis
Task
Assessment
Recommendation
Reasoning
Comparison
Transformation
Querying
Mining
WHY
B
HOW
C
Visualization Data
Representation
WHAT
A
Graphics
Program
Hybrid
Internal
Representation
Feature 
Representation
Fig. 1. We categorize the surveyed papers from three aspects: A What is the visualization data and its representation; B Goals for why apply AI to
visualization data; and C How to apply AI to visualization data, where we outline seven tasks and separately discuss corresponding AI approaches.
visualization paper types [17], i.e., a technique paper focuses
on a single task, while a system paper might accomplish
multiple tasks. In total, we note seven common tasks and
discuss the AI approaches for each task separately.
Drawing upon the discussion, we outline research opportunities.
We make the list of surveyed papers with related material available
online at ai4vis.github.io. We hope that our survey will
stimulate new theories, problems, techniques, and applications
in this growing research area.
2
RELATED SURVEYS
Our ability to collect data has signiﬁcantly exceeded our ability
to analyze it, contributing to the emergence of AI approaches
that automate the processes. Recently, there are active ongoing
discussions about how visualization research could be interwoven
with artiﬁcial intelligence (AI) [18], [19]. However, AI has been
deﬁned and operationalized as a broad notion. To clarify our
discussion, our speciﬁc prospect is to formalize visualizations as
an emerging format of data. We see visualizations different from
existing types such as images and texts, thereby raising many
research questions regarding how AI facilitates the manipulation
and analysis of visualizations.
Several surveys review techniques for automating the creation
of visualizations. Saket et al. [20] discussed the prospect of learning
visualization design and classiﬁed automated visualization design
systems into knowledge-based (i.e., rule-based), data-driven (i.e.,
machine-learning), and hybrid approaches. This classiﬁcation was
systematically reviewed in a recent survey about visualization and
infographics recommendation [21]. Besides, Qin et al. [22] drew
on research in the database community to survey what makes data
visualization more efﬁcient and effective. In addition to automated
creation and recommendation, Davila et al. [23] reviewed research
over the past eight years to formalize chart mining, deﬁned as “the
process of automatic detection, extraction and analysis of charts to
reproduce the tabular data that was originally used to create them”.
Wang et al. [24] recently surveyed machine learning models applied
to visualizations. Different from them, our objective is to provide a
comprehensive review of AI4VIS research, that is, a scaffold for
emerging research problems to be formulated and understood (e.g.,
automatic assessment and summarization of visualizations).
3
METHODOLOGY
In this section, we describe the scope of our literature survey, the
search methodology and corpus, as well as our analysis method.
3.1
Deﬁnition and Scope
This survey focuses on AI approaches applied to visualization
data. We deﬁne visualization data as the digital representations
of visualizations in computers. Thus, we include existing work
that contributes AI techniques or systems that primarily focuses
on inputting or outputting visualization data. However, due to the
wide scope of visualizations and related research, we constrict the
scope of visualizations for manageability.
Excluding scientiﬁc visualizations. We cover literature related
to information visualization and visual analytics, particularly for
which visualizations are represented as charts and infographics.
This restriction excludes literature that primarily focuses on
scientiﬁc visualizations. Scientiﬁc visualizations represent scientiﬁc
data such as ﬂows and volumes, which are typically designed with
a strong inherent reference to space and time [25]. We exclude
them due to their heterogeneous nature that yields different research
challenges and interests [15].
Excluding research speciﬁc to a chart type. The research
problems and proposed techniques could vary among different chart
types. For instance, a conference (i.e., International Symposium on
Graph Drawing) in the graph visualization community focuses on
the graph layout problem, whereas their problems might not apply
to other visualizations like histograms. Those chart-speciﬁc studies
are large-scale and therefore might not be covered in a single
survey, e.g., Behrisch et al. [26] devoted a survey to discussions
about assessment metrics for different charts. Different from them,
our goal is to identify common research problems (i.e., assessment,
recommending) irrespective of the chart types. Nevertheless, we
note a few chart-type-speciﬁc studies and discuss how they might
fall into our taxonomy in section 8.
Excluding human interaction data. Finally, we emphasize
the central role of visualization data in the surveyed AI approaches.
In other words, we do not consider work whose primary goal is to
collect and analyze human interaction data when creating or using
visualizations. Therefore, we exclude provenance data [15] and
data collected for natural language interfaces [27].
3.2
Method and Corpus
To establish the corpus of papers we discussed in this survey, we
apply a relation-search method [14] to traverse the literature. Our
method starts with a linear scan of full papers published at the 2020
IEEE Visualization Conference to collect the starting points. This
initial set of papers has nine papers [1]–[9]. We further augment
