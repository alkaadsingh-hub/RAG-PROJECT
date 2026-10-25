IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL. XX, NO. XX, XX 2018
7
Input Visualization
Single Visualization
Many Visualizations
Output Visualization
Visualization Generation (37)
Data-based (19)
Anchor-based (9)
Context-based (6)
Design-based (4)
Caption and Annotation (13)
Retarget (8)
Question Answering (7)
Interaction (3)
Visualization Analysis (14)
Visualization Retrieval (9)
 Visualization Mining (6)
Visual Data Analysis (2)
Visualization Enhancement (30)
Fig. 5. Matrix of goals of applying AI to visualization data with sub-
categories. We subdivide goals along two axes deductively. Numbers in
the parentheses indicate the count. A paper might have multiple goals.
5.1
Visualization Generation
One of the central research problems in the visualization community
is to ease the creation of visualizations, which is mostly studied
in surveyed papers (37 papers). This is important since authoring
effective visualizations is often time-consuming and challenging
even for professionals [22]. As such, the ultimate goal of work in
this category is to automatically generate visualizations. We iden-
tiﬁed four subcategories that distinguish visualization generation
approaches by user input.
Data-based generation outputs visualizations given a database
or a data-table. These approaches assist in visual data analysis
and have been extensively studied over the last decades. Early
research dates back to 1986 [87], while it still remains an important
question nowadays. Recent work like Draco [49], DeepEye [53],
VizML [38], and DataShot [88] make efforts on the direction.
Visual analysis is an iterative process where the next step of
analysis often depends on earlier insights, motivating the research
on anchor-based generation. The problem is to recommend a vi-
sualization given an anchor visualization. For instance, SeeDB [81]
intelligently recommends visualizations with large deviation to the
anchor visualizations, since they deem most “interesting” to users.
Similarly, DiVE [79] aims to vary the visualization recommenda-
tion, while Dziban [50] targets at maintaining consistency.
Related to anchor-based generation, design-based generation
studies the problem of generating visualizations by injecting the
target data into a reference design. This is referred to as style
transfer [89] or visualization-by-example [75]. Another recent
example is Retrieve-Then-Adapt [1] that applies pre-deﬁned design
templates to user information.
The last category is context-based generation, where the
input only provides some contextual information such as a natural
language description [90] or news articles [58]. An important task
for context-based generation is to recommend data that is mostly
related to the given context.
5.2
Visualization Enhancement
The proliferation of visualizations gives rise to research efforts
in enhancing the use of existing visualizations (30 papers). An
important question is to retarget visualizations to different en-
vironments. For example, VisCode [6] and Chartem [7] encode
additional information in visualization images. It is also common to
summarize visualizations to generate natural language descriptions
such as captions and annotations. This approach transforms
visualizations from visual to non-visual modality, whereby enabling
multimodal interactions [91] or enabling people with vision impair-
ments to consume charts [46]. Related to natural language, recent
research challenges machines to perform question answering
on visualizations, that is, to generate answers given a question
(e.g., [12]). Finally, some work explores adding interactions
to visualizations to improve the legibility and interactivity, e.g.,
Graphical Overlays [92] uses layered elements to aid chart reading.
5.3
Visualization Analysis
With the increasing availability of visualization data, recent
research has constructed visualization databases and investigated
methods for managing and analyzing these collections (14 papers).
Retrieval has been largely studied in the ﬁeld of information
systems and databases, helping users search for visualizations that
match their needs. For instance, Retrieve-Then-Adapt [1] assists
users in ﬁnding an example chart suitable for encoding their data.
Saleh et al. [93] developed a search engine that returns stylistically
similar visualizations given a query visualization.
Another promising set of work has started to mine visualization
collections to derive useful information such as the visualization
usage on the web [40] or in the scientiﬁc literature [11], [42], as
well as design patterns in visualizations [94], [95] and multiple-
view systems [8]. The mined patterns provide evidence for
recommending visualizations.
Related to mining, some work facilitates visual data analysis.
Speciﬁcally, they [9], [62] consider charts to be the analytical object
and propose a visual analytic approach for analyzing data from
charts ensembles by providing analytical guidance for effective
visual analysis, e.g., which charts to examine next.
6
TASKS: HOW TO APPLY AI TO VISUALIZATION
DATA
In this section, we focus on common tasks that researchers apply
to visualization data. We organize the observed tasks into seven
primary tasks as follows where the number indicates the count:
• Transformation coverts visualization data from one modality
(e.g., graphics) to another (e.g., program) (35/98).
• Assessment measures the absolute or relative quality of a
visualization in terms of scores or rankings (19/98).
• Comparison estimates the similarity or other metrics between
two visualizations (12/98).
• Querying ﬁnds the target visualization relevant with a user
query within visualization collections (10/98).
• Reasoning challenges AI to interpret visualizations to derive
high-level information like insights and summaries (22/98).
• Recommendation automates the creation of visualizations by
suggesting data and/or visual encodings (38/98).
• Mining discovers insights from visualization databases (7/98).
Most of those tasks originate from well-known terminology.
Transformation, assessment, and visual reasoning are well-studied
tasks in the ﬁeld of computer vision [28], while querying and
mining come from database and information system research.
Two exceptions are comparison and recommendation. Although
the comparison is similar to the image similarity search task in
computer vision [28], we ﬁnd a large body of visualization research
studying other metrics (e.g., difference) between two visualizations
and thus decide the wording comparison. Recommendation is a
widely studied task in the visualization literature (e.g., [21], [83]).
We obverse relationships between tasks and published venues.
For instance, the Visualization community has mainly studied
recommendation (17/34), while Computer Vision and Artiﬁcial
Intelligence research focuses more on transformation (8/16) and
reasoning (7/16). This shows the diversity and wide attention
among different research communities.
