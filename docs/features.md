# Features

## Site investigation

The [project container](reference/subsurfaceio/site_investigation/) holds
in-situ tests, laboratory specimens, and field strata.

- [In-situ tests](reference/subsurfaceio/site_investigation/in_situ_tests/):
  CPT, DMT, borehole / SPT, IST, UDT.
- Interpretation of CPT (Robertson), DMT (Marchetti), and SPT.
- Liquefaction triggering:
    - CPT: Robertson, Idriss 2008, Boulanger 2014, Saye 2021.
    - DMT: Marchetti.
    - SPT: Cetin 2004, Idriss 2008, Boulanger 2014, Cetin 2018.
- Shear-induced building settlement from liquefaction (Bray 2017).
- Shallow-foundation settlements and capacity, and pile capacity, from in-situ
  data.
- [Laboratory](reference/subsurfaceio/site_investigation/laboratory/) on
  borehole specimens: water content, Atterberg limits, sieve and hydrometer,
  index and strength tests, sample classification.
- [Field strata](reference/subsurfaceio/site_investigation/strata/).
- [Depth aggregation and parametric analysis](reference/subsurfaceio/site_investigation/analysis/).
- [Visualization](reference/subsurfaceio/site_investigation/visualization/):
  geotechnical plots and plot sets, Plotly maps, multi-page HTML reports.
- [Graphical logs](reference/subsurfaceio/logplot/): borehole, CPT, test-pit.
- [IO and export](reference/subsurfaceio/site_investigation/io/): Excel,
  CPeT-IT Excel, AGS (including Next-Generation Liquefaction), KML maps, DXF
  maps, and DXF [cross-sections](reference/subsurfaceio/cross_section/).
- Example [datasets](reference/subsurfaceio/datasets/) and generic
  [file helpers](reference/subsurfaceio/io/).

## Calculations

- [Correlations](reference/subsurfaceio/functions/): CPT, DMT, SPT, footing,
  pile, liquefaction, lab, USCS / AASHTO / USDA, site class, design spectra,
  SSI.
- [Pipelines](reference/subsurfaceio/function_sequences/) covering those same
  domains.
- Shared [parameters](reference/subsurfaceio/parameters/).
- [Function sequence catalog](catalog/function_sequences.md): every named
  recipe.

## Foundations and SSI

- [Shallow foundation](reference/subsurfaceio/footing_foundation/): Terzaghi,
  Vesic, Meyerhof layered cases.
- [Average parameters](reference/subsurfaceio/footing_foundation_average_parameters/).
- [Pile capacity](reference/subsurfaceio/pile_foundation_capacity/) (USACE).
- [Pile settlement](reference/subsurfaceio/pile_foundation_settlement/)
  (Poulos).
- [Pile groups](reference/subsurfaceio/pile_group/).
- [Soil-structure interaction](reference/subsurfaceio/soil_structure_interaction/):
  effects, footing and pile stiffness, group and node data.

## Seismic and classification

- [Seismic site class](reference/subsurfaceio/seismic_site_class/).
- [Averaging](reference/subsurfaceio/seismic_site_class_averaging/) (Ns, Vs,
  Su).
- [From averages](reference/subsurfaceio/seismic_site_class_from_averages/).
- [Design spectra](reference/subsurfaceio/site_design_spectra/).
- [Soil classification](reference/subsurfaceio/soil_classification/): USCS,
  AASHTO, and USDA.
- [Interpolation](reference/subsurfaceio/interpolate/) for resampling
  profiles.

## Graphics and reports

- [Plots](reference/subsurfaceio/plot/) and
  [geotechnical plots](reference/subsurfaceio/geotech_plot/) (Plotly or
  matplotlib).
- [HTML reports](reference/subsurfaceio/html_report/): logs, in-situ,
  laboratory, NGA.
- [Published charts](reference/subsurfaceio/reference_figure/).
- [Graphics](reference/subsurfaceio/graphics/) and
  [tiles](reference/subsurfaceio/tiles/) for rendering support.

## Catalogs and project data

Named parameters, references, datasets, and graphics are in the
[catalog](catalog/index.md).
