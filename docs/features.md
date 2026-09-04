# Features

Public capabilities, with links into the
[package reference](reference/subsurfaceio/).

## Site investigation

[SiteInvestigation](reference/subsurfaceio/site_investigation/) is the project
container.

- [In-situ tests](reference/subsurfaceio/site_investigation/in_situ_tests/):
  CPT, DMT, borehole / SPT, IST, UDT.
- Interpretation of CPT (Robertson), DMT (Marchetti), and SPT.
- Liquefaction triggering and related effects (shear-induced building
  settlement).
- Shallow-foundation settlements and capacity, and pile capacity, from in-situ
  data.
- [Laboratory](reference/subsurfaceio/site_investigation/laboratory/) on
  borehole specimens: water content, Atterberg limits, sieve and hydrometer,
  index and strength tests, sample classification.
- [Field strata](reference/subsurfaceio/site_investigation/strata/).
- [Depth aggregation and parametric analysis](reference/subsurfaceio/site_investigation/analysis/).
- [Visualization](reference/subsurfaceio/site_investigation/visualization/):
  geotechnical plots and plot sets, Plotly maps, multi-page HTML reports.
- [Graphical logs](reference/subsurfaceio/logplot/) (borehole, CPT, test-pit).
- [IO and export](reference/subsurfaceio/site_investigation/io/): Excel,
  CPeT-IT Excel, AGS (including Next-Generation Liquefaction), KML maps, DXF
  maps, and DXF [cross-sections](reference/subsurfaceio/cross_section/).
- Example [datasets](reference/subsurfaceio/datasets/); generic
  [file helpers](reference/subsurfaceio/io/).

## Calculations

Vectorized [correlations](reference/subsurfaceio/functions/) (CPT, DMT, SPT,
footing, pile, liquefaction, lab, USCS / AASHTO / USDA, site class, design
spectra, SSI). Named [pipelines](reference/subsurfaceio/function_sequences/)
covering those same domains. Shared
[parameters](reference/subsurfaceio/parameters/).

The [function sequence catalog](catalog/function_sequences.md) lists every
named recipe.

## Foundations and SSI

Standalone [shallow foundation](reference/subsurfaceio/footing_foundation/)
models (Terzaghi, Vesic, Meyerhof layered cases) and
[average parameters](reference/subsurfaceio/footing_foundation_average_parameters/);
[pile capacity](reference/subsurfaceio/pile_foundation_capacity/) (USACE),
[pile settlement](reference/subsurfaceio/pile_foundation_settlement/) (Poulos),
[pile groups](reference/subsurfaceio/pile_group/);
[soil-structure interaction](reference/subsurfaceio/soil_structure_interaction/)
(effects, footing and pile stiffness, group and node data).

## Seismic and classification

[Seismic site class](reference/subsurfaceio/seismic_site_class/),
[averaging](reference/subsurfaceio/seismic_site_class_averaging/) (Ns, Vs, Su),
[from averages](reference/subsurfaceio/seismic_site_class_from_averages/),
[design spectra](reference/subsurfaceio/site_design_spectra/).
[Soil classification](reference/subsurfaceio/soil_classification/) for USCS,
AASHTO, and USDA. [Interpolation](reference/subsurfaceio/interpolate/) for
resampling profiles.

## Graphics and reports

[Plots](reference/subsurfaceio/plot/) and
[geotechnical plots](reference/subsurfaceio/geotech_plot/) (Plotly or
matplotlib). [Graphical logs](reference/subsurfaceio/logplot/).
[CAD-native sections](reference/subsurfaceio/cross_section/).
[HTML reports](reference/subsurfaceio/html_report/) (logs, in-situ, laboratory,
NGA). [Published charts](reference/subsurfaceio/reference_figure/).
[Graphics](reference/subsurfaceio/graphics/) and
[tiles](reference/subsurfaceio/tiles/) for rendering support.

## Catalogs and project data

[Parameters](reference/subsurfaceio/parameters/),
[references](reference/subsurfaceio/references/),
[reference data](reference/subsurfaceio/reference_data/),
[base data](reference/subsurfaceio/base_data/),
[datasets](reference/subsurfaceio/datasets/),
[project](reference/subsurfaceio/project/),
[constants](reference/subsurfaceio/constants/).

Browse the generated [catalog](catalog/index.md) for parameters, function
sequences, references, datasets, and graphics.
