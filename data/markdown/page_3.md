IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL. XX, NO. XX, XX 2018
4
Graphics
Program
Hybrid
Raster (44)
Logic Program (2)
Relational Program (10)
Set theoretic Program (1)
Graphic Feature (28)
Program Feature (7)
Text Feature (5)
Underlying Data Feature (7)
Hybrid Feature (4)
Imperative (0)
Declarative (42)
Embed programs into graphics (2)
Organize graphics by programs (1)
Vector (9)
Internal
Representation
Feature 
Representation
Visualization Data
A
Representation
B
Fig. 3. Summary of categorization of A visualization data and B its
representation. Numbers in the parentheses indicate the count.
4.1
Data
Visualization data can be stored in different content formats such
as graphics and programs. The choice of content formats directly
inﬂuences the downstream operation possibly on visualization data,
since different formats have own advantages and disadvantages.
Here, we discuss three formats we identiﬁed in our corpus: graphics,
programs, and hybrids. As shown in Figure 3, both graphics and
programs are common in the corpus, and three recent research
papers has proposed hybrid formats for the combined power.
4.1.1
Graphics
Graphics are a natural and expressive content format of visualiza-
tions, since visualizations are deﬁned as a graphical representation
of data. As such, they appear most frequently in our corpus. It
is common to author and store visualization as raster graphics
(bitmaps) for easy usage and sharing [30]. Nevertheless, raster
graphics are a standalone and lossy representation which loses the
visualization semantics (e.g., chart type, visual encoding, under-
lying data). To perform automated analysis, reverse engineering
is often a pre-requisite, i.e., to reconstruct the lost information
using computer vision and machine learning approaches [31], [32].
However, reverse engineering still remains an open problem with
challenges to overcome in terms of robustness and accuracy [7]. In
conclusion, the lossy nature of raster graphics hinders the machines
from easily interpreting and transforming the visualization [7].
Vector graphics represents a less lossy alternative. They have
advantages over raster graphics in that they can be scalable up
without aliasing. Visualizations are usually stored in the Scalable
Vector Graphics (SVG) format [30], which allows describing visual
elements as shapes (e.g., rectangles and text) with styles (e.g.,
positions and ﬁll-color). Those low-level descriptions reduce the
difﬁculties of reverse engineering, e.g., it is no longer necessary
to apply computer vision techniques to detect objects such as
texts [33]. Besides, this format enables support for interactivity and
animation. Nevertheless, high-level visualization semantics such as
visual encoding and underlying data is still lost, whose extraction
requires considerable effort [2], [34].
4.1.2
Program
Researchers have developed approaches for describing and storing
visualizations as computer programs. Programs retain necessary
information to construct the visualization, e.g., the underlying data.
The information is usually represented by languages, which are
classiﬁed into imperative and declarative programming.
Imperative visualization languages require users to specify
step-by-step commands to create the visualization. For example,
D3 [35] is a JavaScript-based toolkit that assists programmers in
specifying graphical marks (e.g., bar, line) with visual attributes.
Programs by imperative languages are open-ended and thus
allow the ﬂexible creation of visualizations. However, the open-
ended characteristic renders it unstructured, with irregularities and
ambiguities that hinder efﬁcient machine-analysis from extracting
the semantics (e.g., visual encodings). As such, we observe few
efforts in analyzing imperative programs. In a slightly different
vein, Bolte and Bruckner [36] recently proposed Vis-a-Vis, a
visual analytic approach for exploring visualization source codes.
The authors argued for more efforts on analyzing visualization
programs.
Declarative languages ask programmers to directly describe the
desired results, which is referred as speciﬁcations. Speciﬁcations
(e.g., Vega-Lite [37]) encapsulate step-by-step commands for
visualization reconstruction into semantic components such as
data encodings, axes, and legend properties. This encapsulation is
achieved by providing sensible defaults and introducing constraints
with prescribed properties and structures. As such, declarative
programs tend to be less or equally expressive as imperative
programs, depending on their design. Since speciﬁcations contain
tags or markers to separate semantic elements and enforce hierar-
chies, they are deemed semi-structured and thus more helpful for
computer processing. It is, therefore, common to generate or collect
speciﬁcations to conduct data-driven research (e.g., VizML [38]).
4.1.3
Hybrid
Recent research proposes several hybrid content formats that
incorporate the beneﬁts of both graphics and programs. Although
such efforts remain limited, we provide our embryonic classiﬁcation
here, hoping to motivate future theories and models.
Two approaches aim to embed programs into graphics.
VisCode [6] presents an embedding approach based on deep image
steganography, that is, to conceal visualization speciﬁcations and
meta information within the bitmap image. Similarly, Chartem [7]
encodes information (e.g., the visualization speciﬁcations) in the
background of a chart image. Both embedding techniques reduce
the overhead to decode underlying visualization speciﬁcations,
by showing that the encoded information can be extracted in
an efﬁcient and less error-prone manner while reducing the
interference to human perception.
Loom [39] takes a different approach and seeks to organize
graphics by programs. Loom proposes to share interactive
visualizations by ﬁlling the gap between two extremes, i.e., sharing
non-interactive formats such as images, and sharing the data,
source codes, and software. Speciﬁcally, it formulates interface
visualizations as a standalone object built on an action tree. Each
intermediate node of the tree represents an interaction such as
clicking, and the leaf node stores the resulting visualization image.
Therefore, users can share and interact with the graphics as if they
have access to the original source codes and software.
4.1.4
Discussion and Open Questions.
Despite the advantages of vector graphics, they appear less often
(9) than raster graphics (44), which might be due to the popularity
of raster graphics in daily life. However, the lossy nature restricts
the availability of machine interpretation and requires continued
research on reverse engineering.
Arguably, programs are not friendly to most people except
for programmers. As such, programs tend to be less shared by
laypeople online, which hinders their collection and reuse. For
