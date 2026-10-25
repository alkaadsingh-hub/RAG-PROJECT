IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL. XX, NO. XX, XX 2018
15
TABLE 8
A summary of characteristics of visualization data and research problems. Citations refer to example work instead of full instances.
Characteristics of Visualization Data
Research Problems
It contains multimodal information such as programs, underlying data,
and images.
How to represent visualization data [9], translate from one modality to
another [31], and fuse and align information between modalities [67].
It is unnatural artifacts purposefully constructed with domain knowledge.
How to automatically infer and/or incorporate with domain knowledge [49].
It is susceptible to detailed local information such as marks’ color and
size.
How to develop algorithms with higher precision and granularity [31] or involve
human in the loop to ﬁx errors made by algorithms [115].
It encodes data and is therefore data-dependent.
How to handle data-dependent problems such as mathematical reasoning [12].
The above systems mostly apply simple statistical analysis [8],
[11], [40], [42], [94] or clustering techniques [95]. However,
patterns might become meaningless numbers unless they are
interpreted as insights or used to empower novel applications, e.g.,
to motivate design ideas. As such, several systems [8], [94] propose
interactive visual interfaces for users to browse the visualization
database and ﬁnd examples. Other approaches also leverage mined
design patterns to recommend visual designs [8], [95].
Mining Data Patterns. Another line of research aims to
explore the data patterns encoded in visualization ensembles.
This concept has been widely implemented in exploring visu-
alization ensembles with respect to a speciﬁed type of charts
(e.g., ScagExplorer [140] and TimeSeer [141]). We identify two
approaches that are irrespective of the chart types, namely Chart
Constellations [56] and ChartSeer [9]. Both adopt a visual analytic
approach by projecting charts into a 2D space whereby supporting
clustering analysis and interactive analysis.
6.7.2
Discussion and Open Questions
There exist several promising directions for future work. For
design patterns, existing approaches focus on visualization usage.
It would be beneﬁcial to mine underlying semantic patterns
from visualization collections, e.g., the relationships between
linked views in a multiple-view visualization, and the “good” or
“bad” practices in existing visualization designs. Those guidelines
could motivate the design of recommender systems that automate
the creation of visualizations. For instance, many recommender
systems in our survey rely on manual coding to derive the design
space of visualizations (e.g., [2], [88], [90]). Automated mining of
design space would signiﬁcantly reduce the manual efforts.
Most current mining techniques are limited to simple statistics.
However, it is likely that there exist hidden patterns in visualization
corpora. Therefore, one could explore the visualization collection
with advanced mining techniques and human-in-the-loop analytics
to uncover those patterns. A research challenge would be to develop
visual analytic systems for analyzing visualization collections.
7
FUTURE RESEARCH OPPORTUNITIES
This survey describes the research vision of formalizing visual-
izations as a data format. As shown in Table 8, visualization data
presents several differences from common data formats such as
images and text. Despite many research efforts, there exist sufﬁcient
research gaps and potentials for future research. In this section, we
outline an organized overview of future research directions.
7.1
Visualization Standards and Interoperability
Our analysis reveals different content formats of visualization
data that have been inconsistently adapted (subsection 4.1). Such
inconsistency impedes interoperability among different visual-
ization systems. Being able to combine different systems and
libraries is a common need in application settings. For instance,
visualization generation tools such as VizML [38] recommend data
encodings, while other systems like MobileVixFixer [2] adjust
non-data encodings (visual styles). Both systems do not work
well together since their formats are incompatible with each other.
Notably, it is a common practice to select partial information from
the full speciﬁcations as the intermediate format. This leads to the
need for a common standard of visualizations that cover all existing
partial formats, as well as derivative tools for auto-completing
partial speciﬁcations to generate universally compatible formats.
Besides, systems for visualization enhancements usually have
to engage in the reverse engineering to extract the underlying
programs from graphics. Despite extensive research efforts, reverse
engineering remains computationally expensive and lacks robust-
ness [31]. Particularly, our analysis in subsection 6.1 suggests that it
is currently impossible to perform reverse engineering on bespoke
charts. Although recent work like Chartem [7] and VisCode [6]
proposes new standards for storing programs in graphics, there is
a long way before such standards are adopted in existing systems.
Thus, continued research on reverse engineering is essential and
beneﬁcial to interoperability.
7.2
Visualization-Tailored Machine Learning
Recent research has increasingly leveraged machine learning to
generate or transform visualization. However, it remains chal-
lenging to choose the “best” representation and ML models for
visualizations [142]. On the one hand, programs are compact and
effective representations that are computationally inexpensive [38],
[49]. However, programs might not generalize since they are often
limited to speciﬁc chart types and might not apply to parameter
values not observed during training. On the other hand, graphics
appear to be a general representation. However, research suggests
that off-the-shelf computer vision models for natural images
achieve dissatisfactory results in tasks such as visual perceptual
learning [66], visual question answering [12], and assessment [61].
This gap is not surprising due to the characteristics of visu-
alization images. Compared with natural images, visualizations
are sensitive to local details, e.g., the sizes of graphical marks are
of vital importance. Text information is also critical, taking on
various roles (e.g., legends, axis labels) that have no tolerance for
misinterpretation, e.g., missing a single character in axis labels
leads to a great blunder. Those characteristics make it challenging
to design an ML model that are tailored to visualizations. Recent
work in visualization question answering (e.g., [12], [67], [70])
has proposed sophisticated models to fuse multimodal features and
capture visualization-speciﬁc features. However, such attempts are
limited and their efﬁcacy remains to be thoroughly evaluated.
Another important perspective lies in augmenting machine
learning models with knowledge derived from empirical studies.
Machine learning models are often criticized for poor explainability.
Fortunately, empirical research in the visualization ﬁeld has accu-
mulated a valuable knowledge base about how visualizations should
be interpreted, assessed, and created. It is therefore promising
