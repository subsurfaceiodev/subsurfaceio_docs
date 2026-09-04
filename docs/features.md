# Features

Public capabilities of the library, with links into the
[package reference](reference/subsurfaceio/).

## Site investigation

[`SiteInvestigation`][subsurfaceio.site_investigation.SiteInvestigation]
([subsurfaceio.site_investigation][]) is the project container.

- In-situ tests ([subsurfaceio.site_investigation.in_situ_tests][]): CPT, DMT,
  borehole / SPT, IST, UDT.
- Interpretation of CPT (Robertson), DMT (Marchetti), and SPT.
- Liquefaction triggering and related effects (shear-induced building
  settlement).
- Shallow-foundation settlements and capacity, and pile capacity, from in-situ
  data.
- Laboratory on borehole specimens
  ([subsurfaceio.site_investigation.laboratory][]): water content, Atterberg
  limits, sieve and hydrometer, index and strength tests, sample
  classification.
- Field strata ([subsurfaceio.site_investigation.strata][]).
- Depth aggregation and parametric analysis
  ([subsurfaceio.site_investigation.analysis][]).
- Visualization ([subsurfaceio.site_investigation.visualization][]):
  geotechnical plots and plot sets, Plotly maps, multi-page HTML reports.
- Graphical logs via [subsurfaceio.logplot][] (borehole, CPT, test-pit).
- IO and export ([subsurfaceio.site_investigation.io][]): Excel, CPeT-IT Excel,
  AGS (including Next-Generation Liquefaction), KML maps, DXF maps, and DXF
  cross-sections ([subsurfaceio.cross_section][]).
- Example inputs in [subsurfaceio.datasets][]; generic file helpers in
  [subsurfaceio.io][].

## Calculations

Vectorized correlations in [subsurfaceio.functions][] (CPT, DMT, SPT, footing,
pile, liquefaction, lab, USCS / AASHTO / USDA, site class, design spectra,
SSI). Named pipelines on [subsurfaceio.function_sequences][] covering those
same domains. Shared parameter definitions in [subsurfaceio.parameters][].

The [function sequence catalog](catalog/function_sequences.md) lists every
named recipe.

## Foundations and SSI

Standalone models: [subsurfaceio.footing_foundation][] (Terzaghi, Vesic,
Meyerhof layered cases) and
[subsurfaceio.footing_foundation_average_parameters][];
[subsurfaceio.pile_foundation_capacity][] (USACE),
[subsurfaceio.pile_foundation_settlement][] (Poulos),
[subsurfaceio.pile_group][]; [subsurfaceio.soil_structure_interaction][]
(effects, footing and pile stiffness, group and node data).

## Seismic and classification

[subsurfaceio.seismic_site_class][],
[subsurfaceio.seismic_site_class_averaging][] (Ns, Vs, Su),
[subsurfaceio.seismic_site_class_from_averages][],
[subsurfaceio.site_design_spectra][]. [subsurfaceio.soil_classification][] for
USCS, AASHTO, and USDA. [subsurfaceio.interpolate][] for resampling profiles.

## Graphics and reports

[subsurfaceio.plot][] and [subsurfaceio.geotech_plot][] (Plotly or matplotlib).
[subsurfaceio.logplot][] graphical logs. [subsurfaceio.cross_section][]
CAD-native sections. [subsurfaceio.html_report][] printable A4 reports (logs,
in-situ, laboratory, NGA). [subsurfaceio.reference_figure][] published charts.
[subsurfaceio.graphics][] and [subsurfaceio.tiles][] for rendering support.

## Catalogs and project data

[subsurfaceio.parameters][], [subsurfaceio.references][],
[subsurfaceio.reference_data][], [subsurfaceio.base_data][],
[subsurfaceio.datasets][], [subsurfaceio.project][],
[subsurfaceio.constants][].

Browse the generated [catalog](catalog/index.md) for parameters, function
sequences, references, datasets, and graphics.
