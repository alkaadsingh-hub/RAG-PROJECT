IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL. XX, NO. XX, XX 2018
6
TABLE 1
A summary of feature representation of visualizations for machine learning tasks.
Graphics
Program
Text
Underlying Data
Feature Engineering
general image descriptors [11], [32], [42], [45]
element positions or regions [31], [32], [40], [46],
[47]
element styles [40]
parameters [1], [2]
communicative
signals [48]
design rules [49], [50]
statistical models [3], [45],
[51], [52]
statistics [38], [43],
[53]–[55]
one-hot vector [56]
Feature Learning
convolutional neural network [12], [13], [31],
[46], [51], [57]–[61], [61]–[72]
autoencoder [6], [61]
autoencoder [9], [73]
embedding models [3], [56]
autoencoder [74]
limits their capability in high-level tasks such as assessment [61]
and visual question answering [12], where the performances are
relatively dissatisfactory.
Program features are extracted from the programs such as
speciﬁcations. Probably the most straightforward representation
is the parameters. For instance, MobileVisFixer [2] and Retrieve-
then-Adapt [1] train models that learn to operate on the chart
parameters, e.g., positioning the element. Burns et al. [48] extracted
communicative signals (such as whether a group of bars is colored
differently from the other bars) that they fed into a Bayesian
model. Draco [49] contains constraints over facts that encode
visualization design knowledge. These constraints describe whether
a visualization conforms to best practices of effective visual
design. However, little work uses programs as the training input
which might be due to several reasons, including the lack of
training data or the overheads of reserve engineering to extract
the program from visualization graphics. Still, programs are a
promising representation as they contain high-level visualization-
speciﬁc information. For example, ChartSeer [9] converts Vega-
Lite speciﬁcations of charts into visualization embeddings by
autoencoders. The embeddings are used to measure similarities
between charts to assist in analyzing chart ensembles, and proven
effective in user studies. Their results suggest that program features
are promising in semantically characterizing charts.
Text features refer to the text content in visualizations such as
titles. They are considered to improve the feature informativeness
by incorporating semantic information. For instance, two systems
describe text information with statistical models, i.e., bag-of-
words [45], [51], and incorporate the resulting text features with
graphical features to improve the performance for chart detection
and classiﬁcation tasks. Moreover, text features can capture the
subject matter of visualizations. VizCommender [3] is a recent
content-based recommendation system built on machine learning
models for predicting semantic similarity between two visualization
repositories, which shows a high agreement with a human majority
vote. Chart Constellations [56] uses word embeddings to measure
the similarity between charts. However, it still remains unclear how
text features could be effectively fused with graphical features to
more comprehensively represent a visualization, e.g., to balance
text-based and style-based similarities.
The last category of visualization features is in the underlying
data that the visualization encodes. Chart Constellations [56]
describes the encoded data columns by a one-hot vector encoding,
which is then used to compute chart-wise similarities. Besides
such descriptive purposes (i.e., to describe a visualization), data
features are found to be mainly predictive (i.e., to predict the
visual encoding). Data2Vis [74] adopts a sequence-to-sequence
autoencoder structure that models the input dataset in the JSON
format. However, the sequence-to-sequence structure might not well
capture the characteristics of the underlying data such as the data
type. DeepEye [52], [53], [55] and VizDeck [54] perform feature
engineering to consider data statistics such as the number of unique
values in a column. VizML [38] further extends this approach
to 841 features including single- and pairwise-column features
of the input dataset and signiﬁcantly outperforms Data2Vis and
DeepEye. The analysis of VizML suggests that those features are
not independent and some appear to be of little importance. Future
research should propose effective feature selection approaches or
complementary feature learning methods.
4.2.3
Discussion and Open Questions
Learning visualization-speciﬁc features. Existing off-the-shelf
computer vision or machine learning models are originally designed
for general visual content or relational data. They might fall short
when applied to visualizations, e.g., visualization assessment [61]
and Data2Vis [74] since they do not capture visualization-speciﬁc
features such as visual encodings and encoded data that are critical.
Researchers have proposed feature engineering approaches to craft
features, which, however, are labor-intensive without guarantees for
success. With the rapid development of deep learning techniques,
we envision models tailored to visualizations that effectively learn
visualization-speciﬁc features.
Fusing multimodal features. Visualizations are unlikely to
be comprehensively represented by only one feature. However, as
shown in Figure 3, most work only leverages graphic features while
other modalities remain under-explored. In contrast, fusing multi-
modal features could improve performances of chart detection and
classiﬁcation [45], [51]. Promising avenues for future work lie
in leveraging feature fusion for high-level tasks such as question
answering and similarity-based recommendation, which are not
well-solved by the single-modal feature.
5
GOAL: WHY APPLY AI TO VISUALIZATION DATA
The goals of applying AI to visualization data cover a wide
spectrum, pursued by research efforts from different areas. We
adopt a deductive classiﬁcation method to create a mutually ex-
clusive and collectively exhaustive taxonomy that better structures
our discussion. Speciﬁcally, we subdivide goals along two axes
deductively: whether visualizations are the input or output and
whether visualizations are single or many. We further merge
outputting single visualization and outputting many visualizations
from an inductive perspective, i.e., we observe that they share the
same sub-categorization. Therefore, we ﬁnally classify goals into 3
categories, which are further subdivided (Figure 5):
• Visualization Generation outputs single or many visualiza-
tions given different user inputs.
• Visualization Enhancement processes and applies enhance-
ment to an input visualization.
• Visualization Analysis concerns organizing and exploiting a
visualization collection.
It should be noted that some work is a technique paper that
introduces a novel algorithm without practically demonstrating
the applications (e.g., [66]). We do not label the goals for those
techniques but instead discuss their tasks in section 6.
