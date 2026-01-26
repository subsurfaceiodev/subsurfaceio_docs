---
title: site_design_spectra.py
---

## Formulae

#### `_get_factors__carlton2018simplified`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_factors\_\_carlton2018simplified}(T, H, V_{s\ mean}, γ_{0.5\ mean}, CRR_{min}) \\ \hspace{1em} c \gets \mathrm{dict} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathrm{ref} \gets \mathrm{ReferenceData}.\mathrm{Carlton2018Table6} \\ \hspace{1em} \mathbf{for} \ \mathopen{}\left( \mathrm{c\_key}, \mathrm{c\_} \mathclose{}\right) \in \mathrm{ref}.\mathrm{items} \mathopen{}\left( \mathclose{}\right) \ \mathbf{do} \\ \hspace{2em} \mathbf{if} \ \mathrm{c\_key} = \textrm{"period"} \\ \hspace{3em} \mathbf{continue} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} c_{\mathrm{c\_key}} \gets \mathrm{np}.\mathrm{interp} \mathopen{}\left( T, \mathrm{ref}_{\textrm{"period"}}, \mathrm{c\_} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ for} \\ \hspace{1em} \mathrm{f1} \gets c_{1} + c_{2} \cdot \log H + c_{3} \cdot \log V_{s\ mean} + c_{4} \cdot \log γ_{0.5\ mean} \\ \hspace{1em} \mathrm{f2} \gets c_{5} + c_{6} \cdot \log CRR_{min} \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( \mathrm{f1}, \mathrm{f2} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
T &= \text{Period (s)}\\
H &= \text{Special layers thickness (m)}\\
V_{s\ mean} &= \text{Special shear velocity mean (m/s)}\\
γ_{0.5\ mean} &= \text{Special shear strain mean (\%)}\\
CRR_{min} &= \text{Special cyclic resistance ratio min.}
\end{align*}
$$

#### `get_pseudo_spectral_acceleration__carlton2018simplified`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pseudo\_spectral\_acceleration\_\_carlton2018simplified}(T, PSa, H, V_{s\ mean}, γ_{0.5\ mean}, CRR_{min}, \mathrm{period\_new}, \mathrm{number\_of\_standard\_deviations}) \\ \hspace{1em} \mathbf{if} \ \mathrm{period\_new} \not\equiv \mathrm{None} \\ \hspace{2em} PSa \gets \mathrm{np}.\mathrm{interp} \mathopen{}\left( \mathrm{period\_new}, T, PSa \mathclose{}\right) \\ \hspace{2em} T \gets \mathrm{period\_new} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathopen{}\left( \mathrm{f1}, \mathrm{f2} \mathclose{}\right) \gets \mathrm{\_get\_factors\_\_carlton2018simplified} \mathopen{}\left( T, H, V_{s\ mean}, γ_{0.5\ mean}, CRR_{min} \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ \mathrm{number\_of\_standard\_deviations} > 0 \\ \hspace{2em} \mathrm{table7} \gets \mathrm{ReferenceData}.\mathrm{Carlton2018Table7} \\ \hspace{2em} \mathrm{std} \gets \mathrm{number\_of\_standard\_deviations} \cdot \mathrm{np}.\mathrm{interp} \mathopen{}\left( T, \mathrm{table7}_{\textrm{"period"}}, \mathrm{table7}_{\textrm{"σtotal"}} \mathclose{}\right) \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathrm{std} \gets 0 \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathrm{amp} \gets \exp \mathopen{}\left( \mathrm{f1} + \mathrm{f2} \cdot \log \mathopen{}\left( \frac{PSa + 0.1}{0.1} \mathclose{}\right) + \mathrm{std} \mathclose{}\right) \\ \hspace{1em} PSa \gets PSa \cdot \mathrm{amp} \\ \hspace{1em} \mathbf{return} \ PSa \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
PSa &= \text{Pseudo-spectral acceleration (g)}\\
T &= \text{Period (s)}\\
H &= \text{Special layers thickness (m)}\\
V_{s\ mean} &= \text{Special shear velocity mean (m/s)}\\
γ_{0.5\ mean} &= \text{Special shear strain mean (\%)}\\
CRR_{min} &= \text{Special cyclic resistance ratio min.}\\
\text{number\_of\_standard\_deviations} &= \text{Number of standard deviations}
\end{align*}
$$
