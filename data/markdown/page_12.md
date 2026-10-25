IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL. XX, NO. XX, XX 2018
13
6.5.2
Discussion and Open Questions
The reasoning task is currently undergoing changes since machine
learning approaches, particularly deep learning models, are increas-
ingly used. This change may attribute to the rapid advancement
and successful applications of deep learning in visual reasoning. In
the visualization context, research gaps emerge since off-the-shelf
models for natural images are often shown to yield dissatisfactory
performances on visualizations (e.g., [12], [66]). This gap is not
surprising since visualizations contain relational information that is
sensitive to small details that are not commonly present in natural
images, i.e., a local change to a bar shape might signiﬁcantly
impact the encoded data and conveyed meanings. This research
area remains largely under-explored. First, limited datasets are
available, which hinders model development and validation. For
instance, most existing datasets for visual question answering
contain synthetic questions and charts, which are far from being
representative for the actual use. Second, it would be pertinent
to study feature learning models that are tailored to visualization
images. The recent trend of decomposing end-to-end models to
structures containing multiple sub-networks might be a promising
method (e.g., [70]).
6.6
Recommendation
Recommendation is an important step for automating the creation
of visualizations. As shown in Table 6, there are three methods for
recommending visualizations [83]:
• Data recommendation suggests interesting data, insights, or
data transformation be visualized from a database.
• Encoding recommendation determines the visual encoding
(including both data and non-data encodings) given the data
or other visualization elements.
• Hybrid recommendation decides both data and encodings.
Recommending
Data to be encoded
Visualization
Fig. 11. Input-output model of recommendation.
Relations to goals and other tasks. Recommendation is
mainly for visualization generation. It is related to assessment and
comparison since the derived metrics are used as cost functions.
Relations to visualization data. Recommendation outputs
visualization programs and subsequently visualization graphics.
6.6.1
Challenges and Methods
Data Recommendation. Given a dataset, one step of recommend-
ing visualizations is to select data ﬁelds to be visualized, and when
applicable, corresponding data transformation as well. The simplest
approach to decide ﬁelds is enumeration. For instance, Voyager [84],
[85] enumerates all possible ﬁelds according to a predeﬁned
display order by the type and name. DataSite [128] improves
this enumeration approach by computing and communicating data
facts associated with the selected ﬁelds according to pre-deﬁned
templates (e.g., “Correlation of A was found between X and Y” if
selected data ﬁelds are X and Y). However, enumeration imposes a
heavy burden on users that motivates other research to recommend
the most useful data facts, also known as insights.
Recommending insights is often approached by proposing a
taxonomy of insight types (e.g., extrema), each type associated with
an assessment metric. Examples are Foresight [132], Proﬁlier [117],
TABLE 6
Recommendation is classiﬁed by the class (row) and methods (column)
Optimization
Prediction
Data
[4], [29], [79], [81], [88], [117], [122],
[132], [133]
Encoding
[1], [2], [4], [5], [49], [50], [59], [84], [87],
[90], [95], [106], [117], [122], [128],
[134]–[137]
[38], [74],
[88]
Hybrid
[4], [52], [53], [55], [83], [85], [88], [117],
[128], [135], [138]
Voder [122], DataShot [88], VisClean [29], and Calliope [4].
One key challenge that then arises is the assessment metric.
Voder [122] introduces threshold-based heuristics that classify
data facts into different tiers, while the remaining systems propose
various cost functions that better capture the differences between
data facts. Remarkably, QuickInsights [133] propose a uniﬁed
formulation of insights and scoring metrics irrespective of the type.
In the context of anchor-based generation where the goal is to
recommend data that meets some criteria with respect to anchor
data, the aforementioned assessment metrics are augmented by
or replaced by comparison metrics in VisClean [29], DiVE [79],
and SeeDB [81]. For instance, SeeDB [81] recommends data by
deviation with an anchor visualization.
Given the above metrics, the next challenge is to compute the
best or top-k insights. This is challenging since the space of data
facts grows exponentially with the number of data table columns.
As such, researchers have proposed multiple strategies to speed up
the computation. For instance, Foresight [132] uses sketching to
quickly approximate the costs. Other systems introduce efﬁcient
searching algorithms to recommend the top-k insights. Those
searching algorithms are primarily progressive or iterative [4], [29],
[79], [81], [88], outputting intermediate solutions that approximate
the optimal one. That said, this data recommendation problem has
not yet been formulated as a prediction problem that is solved
by machine-learning models, probably due to the lack of labeled
training data. Notably, two approaches explicitly adopt tree-based
algorithms [4], [29], leveraging the idea of GraphScape [119] that
the visualization design space can be modeled as a graph for greedy
or dynamic programming.
Several systems recommend data according to other input
beyond a database. Particularly, those inputs are related to natural
language that is beyond the core scope of this survey. Examples
include natural language statements in Text-to-Viz [90], news
articles in VizByWiki [58], keyword queries [55], and natural
language interfaces (e.g., NL4DV [136] and FlowSense [139]).
Encoding Recommendation decides data encodings and/or
non-data encodings for styling (e.g., positions).
Data encodings are extensively studied in the literature. Early
approaches date back to 1986 where the APT system [87] enumer-
ates the visual encoding space and selects the “best” encodings
according to the assessment ranking in terms of expressiveness and
effectiveness. This ranking-based recommendation is implemented
and extended in later systems such as ShowMe [134] and Voy-
ager [84]. In addition to ranking, several systems propose heuristic
rules to decide visual encodings given the insights extracted
from data recommendation or visual tasks, e.g., extreme insights
or ﬁnding extremes are mapped to histograms or scatterplots.
Examples include DataVizard [135], DataSite [128], Proﬁler [117],
NL4DV [136], Calliope [4], VizAssist [137], and Voder [122].
The above heuristic-based data-encoding recommenders have
recently been superseded by machine learning approaches due to
