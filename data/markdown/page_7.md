IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL. XX, NO. XX, XX 2018
8
6.1
Transformation
Transformation is the operation that converts the content formats
of visualizations. Particularly, it is straightforward to transform
visualization programs into graphics by visualization tools or
libraries (e.g., [35], [37]). A more challenging problem is the
reverse process, i.e., reconstructing programs from graphics. This
process is also known as reverse engineering [31]. In the following
text, we focus on the reverse engineering problem.
Relations to goals and other tasks. Transformation is usually
the ﬁrst task for visualization enhancement and analysis, especially
when the input is images. As such, it is often a prerequisite for
remaining tasks. For instance, the extracted information can be
used for querying [94] and reasoning [96].
Relations to visualization data. Several works study the
problem of transforming visualization images into another image
by altering the data or visual styles [1], [89], [94]. Nevertheless,
their approaches are built on reverse engineering, i.e., to extract the
encodings ﬁrst and then replace the data. Little research explored
the direct transformation in the image space [6], [7], [97], [98]. As
such, we do not dedicate a separate discussion on image-to-image
transformation at the current stage. Future research could extend
our taxonomy with further development in this ﬁeld.
6.1.1
Challenges and Methods
Visualization reverse engineering has been widely and extensively
studied over the past decades. Early research could date back to
2001 when Zhou and Tan [99] proposed a learning-based paradigm
for chart recognition. Since then, much research has been devoted
to extracting semantic information from visualization images such
as chart types, visual encoding, and underlying data. Ideally, reverse
engineering is expected to yield cycle-consistency; that is, its output
should be able to re-generate the original visualization. Despite
promising preliminary results, several challenges remain to be
overcome since much work makes simplifying assumptions on the
expected input or output. For instance, several approaches take
vector graphics as input [2], [11], [34], [40], [89], [94], [100]–
[102], assuming the type of each visual element is available as
SVG. Most work is limited to a predeﬁned set of chart types,
while little work [2], [34], [58], [59], [89], [94], [100], [103]
applies to more bespoke visualizations. Besides, a large body of
research focuses on extracting a particular portion of information,
such as chart classiﬁcation [42], [51], [58], [59], [63]–[65], object
separation [104], [105], and object clustering [2], [100], [101].
We summarize a conceptual framework of the reverse engi-
neering process to provide an overview of existing approaches
and identify research gaps. We developed the framework via a
bottom-up approach, where we abstract existing methods, identify
their simplifying assumptions, and iteratively merge the results.
As shown in Figure 6, we identify two distinct phases. The ﬁrst
phase decomposes visualization graphics into semantic elements
(e.g., axis, mark) through machine learning and computer vision
techniques, including object detection, classiﬁcation, and clustering.
The second phase performs mathematical computation over the
decomposed semantic elements to extract visual encoding and/or
the underlying data. In the following text, we describe each phase.
Decomposing. The decomposing phase varies depending on
the input (Figure 6 A ). The primary step for raster graphics is to
detect and classify visual elements such as text and shapes. This is
approached by traditional image processing techniques (e.g., edge
detection, morphological operations) in early work [32], [46], [47],
Guide
Guide
Scale
Encoding
Encoding
Scale
Data
Data
Chart
Mark
Mark
Raster 
Image
Vector 
Image
Element
Chart
Guide
Mark
Others
Element 
Clustering
Decomposing
Composing
A
B
Known Chart Type
Unknown Chart Type
Element Detection 
& Classification
Chart Detection & Classification
Transformation
Fig. 6. The conceptual framework of the reverse engineering process:
A It ﬁrst decomposes input graphics into semantic groups such as
guides (axes and legends) and marks; B The resulting information is
fed into mathematical computation to extract the visual encoding and/or
underlying data, depending on whether the chart type is known. It remains
an open challenge to derive both visual encoding and data from bespoke,
unknown chart types.
[109] and machine learning or deep learning approaches (e.g., Mark
RCNN) in work published in 2015 and later [10], [31], [45], [46],
[60], [62], [91], [103], [110], [111]. This element recognition step
faces chart-speciﬁc challenges, e.g., to cope with visual clutter in
line charts and scatterplots [104], [105]. In addition, since existing
object detection models are prone to rotation that is common for pie
sectors, Choi et al. [46] proposed a special heuristic to pie charts
by grouping the nearby pixels with the same color. The output
of this element recognition step is usually the position and class
of each visual element, which are already available in the SVG
speciﬁcations of vector graphics. In other words, vector graphics
remove the overhead of element recognition.
Chart detection and classiﬁcation are an another step of the
decomposing phase. This step faces two important choices: the
classiﬁer and the feature representation. Classical classiﬁers (e.g.,
support vector machine) [32], [40], [45], [112] have been gradu-
ally superseded by deep learning classiﬁers (e.g., convolutional
neural network (CNN)) [42], [46], [51], [58]–[60], [62]–[65] in
visualization classiﬁcation tasks. This is mainly because CNNs can
effectively learn abstract features from raw visualization images,
while classical classiﬁers require hand-crafted image features
such as histograms of the image gradients (HOG) [112] and
dense sampling [32], [45]. Several approaches seek to improve
the representativeness of features by incorporating element-level
features such as text [32], [51] and shape style features [40]. The
last step of the decomposing phase addresses element clustering,
that is, to cluster visual elements into semantic groups, including
guides (axes and legends), marks, and other information such
as annotations. This step is typically separately discussed for
text and shape elements. On one hand, clustering text is usually
formalized as a classiﬁcation problem, that is, to classify and group
text according to their text roles such as x-axis-label and legend-
title [10], [31], [32], [45]–[47], [62], [91], [111], [113]. On the
other hand, this classiﬁcation-based approach is not always readily
applicable to shape clustering, since the roles of shape depend on
the chart type. As such, researchers usually simplify this problem
by focusing on common charts where shapes are well-deﬁned. For
