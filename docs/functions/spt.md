---
title: spt.py
---

#### `_get_coefficient_of_consolidation__navfac1982soil_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_coefficient\_of\_consolidation\_\_navfac1982soil\_scalar}(LL, \mathrm{is\_disturbed\_soil}, \mathrm{consolidation\_state}) \\ \hspace{1em} \mathrm{key} \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{is\_disturbed\_soil} \\ \hspace{2em} \mathrm{key} \gets \textrm{"Remolded"} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{consolidation\_state} = \textrm{"NC"} \\ \hspace{3em} \mathrm{key} \gets \textrm{"Virgin"} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ \mathrm{consolidation\_state} \in \mathopen{}\left[ \textrm{"LOC"}, \textrm{"MOC"}, \textrm{"HOC"} \mathclose{}\right] \\ \hspace{4em} \mathrm{key} \gets \textrm{"Reloading"} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{if} \ \mathrm{key} \equiv \mathrm{None} \\ \hspace{2em} C_v \gets \mathrm{None} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} C_v \gets \mathrm{CoefficientOfConsolidationNAVFAC1982Figure}.\mathrm{interpolate\_at\_x} \mathopen{}\left( LL \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ C_v \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_v &= \text{Coefficient of consolidation (m2/year)}\\
LL &= \text{Liquid limit (\%)}\\
\text{is\_disturbed\_soil} &= \text{Is disturbed soil}\\
\text{consolidation\_state} &= \text{Consolidation state}
\end{align*}
$$

#### `_get_unit_weight__cetin2018use_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_unit\_weight\_\_cetin2018use\_scalar}(N_{60}, \mathrm{is\_fine\_soil}, \mathrm{below\_water\_table}, γ_{default}) \\ \hspace{1em} \mathbf{if} \ \lnot \mathrm{is\_fine\_soil} \\ \hspace{2em} \mathbf{if} \ \lnot \mathrm{below\_water\_table} \\ \hspace{3em} \mathrm{key} \gets \textrm{"unit\_weight.Coarse.Moist"} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathrm{key} \gets \textrm{"unit\_weight.Coarse.Saturated"} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \lnot \mathrm{below\_water\_table} \\ \hspace{3em} \mathrm{key} \gets \textrm{"unit\_weight.Fine.Moist"} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathrm{key} \gets \textrm{"unit\_weight.Fine.Saturated"} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} γ \gets \mathrm{PARAMETERS}_{\textrm{"corrected\_blow\_count"}}.\mathrm{data\_bins}_{\mathrm{key}}.\mathrm{bin\_data} \mathopen{}\left( N_{60} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ γ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
γ &= \text{Unit weight (kN/m3)}\\
N_{60} &= \text{Corrected blow count}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{below\_water\_table} &= \text{Below water table}\\
γ_{default} &= \text{Default unit weight (kN/m3)}
\end{align*}
$$

#### `get_borehole_diameter_correction__skempton1986standard`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_borehole\_diameter\_correction\_\_skempton1986standard}(D_{bh}, \mathrm{use\_simplified\_blows\_correction}, z) \\ \hspace{1em} \mathbf{if} \ \mathrm{use\_simplified\_blows\_correction} \\ \hspace{2em} C_B \gets 1 \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} C_B \gets \mathrm{PARAMETERS}_{\textrm{"borehole\_diameter"}}.\mathrm{data\_bins}_{\textrm{"borehole\_diameter\_correction"}}.\mathrm{bin\_data} \mathopen{}\left( D_{bh} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} C_B \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( z, C_B \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ C_B \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_B &= \text{Borehole diameter correction}\\
D_{bh} &= \text{Borehole diameter (mm)}\\
\text{use\_simplified\_blows\_correction} &= \text{Use simplified blows correction}\\
z &= \text{Depth (m)}
\end{align*}
$$

#### `get_clean_sand_normalized_blow_count__cetin2004standard`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_clean\_sand\_normalized\_blow\_count\_\_cetin2004standard}(N_{160}, C_{FINES}, \mathrm{is\_fine\_soil}) \\ \hspace{1em} N_{160cs} \gets N_{160} \cdot C_{FINES} \\ \hspace{1em} \mathbf{return} \ N_{160cs} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_{160cs} &= \text{Clean sand normalized blow count}\\
N_{160} &= \text{Normalized blow count}\\
C_{FINES} &= \text{Fines content factor}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_clean_sand_normalized_blow_count__seed1987design`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_clean\_sand\_normalized\_blow\_count\_\_seed1987design}(N_{160}, ΔN_{160}, \mathrm{is\_fine\_soil}) \\ \hspace{1em} N_{160cs} \gets N_{160} + ΔN_{160} \\ \hspace{1em} \mathbf{return} \ N_{160cs} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_{160cs} &= \text{Clean sand normalized blow count}\\
N_{160} &= \text{Normalized blow count}\\
ΔN_{160} &= \text{Normalized blow count fines inc.}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_clean_sand_normalized_blow_count_sr__idriss2003estimating`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_clean\_sand\_normalized\_blow\_count\_sr\_\_idriss2003estimating}(N_{160}, ΔN_{160-Sr}, \mathrm{is\_fine\_soil}) \\ \hspace{1em} \mathbf{return} \ \mathrm{get\_clean\_sand\_normalized\_blow\_count\_\_seed1987design} \mathopen{}\left( N_{160}, ΔN_{160-Sr} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_{160cs-Sr} &= \text{Clean sand normalized blow count (Sr)}\\
N_{160} &= \text{Normalized blow count}\\
ΔN_{160-Sr} &= \text{Normalized blow count fines inc. (Sr)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_coefficient_of_consolidation__navfac1982soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_coefficient\_of\_consolidation\_\_navfac1982soil}(LL, \mathrm{is\_disturbed\_soil}, \mathrm{consolidation\_state}, \mathrm{is\_fine\_soil}) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_get\_coefficient\_of\_consolidation\_\_navfac1982soil\_vec} \mathopen{}\left( LL, \mathrm{is\_disturbed\_soil}, \mathrm{consolidation\_state} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_v &= \text{Coefficient of consolidation (m2/year)}\\
LL &= \text{Liquid limit (\%)}\\
\text{is\_disturbed\_soil} &= \text{Is disturbed soil}\\
\text{consolidation\_state} &= \text{Consolidation state}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_compression_index__rendon1983closure`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_compression\_index\_\_rendon1983closure}(w_c, \mathrm{is\_fine\_soil}) \\ \hspace{1em} C_c \gets 0.01 \mathopen{}\left( w_c - 7.549 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ C_c \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_c &= \text{Compression index}\\
w_c &= \text{Water content (\%)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_compression_ratio__lambe1969soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_compression\_ratio\_\_lambe1969soil}(w_c, \mathrm{is\_fine\_soil}) \\ \hspace{1em} CR \gets \mathrm{CompressionRatioLambe1969Figure}.\mathrm{interpolate\_at\_x} \mathopen{}\left( w_c \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ CR \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
CR &= \text{Compression ratio}\\
w_c &= \text{Water content (\%)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_constrained_modulus__janbu1985soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_constrained\_modulus\_\_janbu1985soil}(w_c, σ_v', \mathrm{is\_fine\_soil}) \\ \hspace{1em} \textrm{" Equation obtained from kulhawy1990manual"} \\ \hspace{1em} m \gets 107.3 \exp \mathopen{}\left( -0.05042 w_c \mathclose{}\right) + 2.834 \\ \hspace{1em} M \gets 0.001 \cdot m \cdot σ_v' \\ \hspace{1em} \mathbf{return} \ M \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
M &= \text{Constrained modulus (MPa)}\\
w_c &= \text{Water content (\%)}\\
σ_v' &= \text{Effective stress (kPa)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_corrected_blow_count__skempton1986standard`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_corrected\_blow\_count\_\_skempton1986standard}(N, C_E, C_B, C_R, C_S) \\ \hspace{1em} N_{60} \gets N \cdot C_E \cdot C_B \cdot C_R \cdot C_S \\ \hspace{1em} \mathbf{return} \ N_{60} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_{60} &= \text{Corrected blow count}\\
N &= \text{Blow count}\\
C_E &= \text{Energy ratio correction}\\
C_B &= \text{Borehole diameter correction}\\
C_R &= \text{Rod length correction}\\
C_S &= \text{Sampler correction}
\end{align*}
$$

#### `get_energy_ratio_correction__skempton1986standard`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_energy\_ratio\_correction\_\_skempton1986standard}(ER, z) \\ \hspace{1em} C_E \gets \frac{ER}{60} \\ \hspace{1em} C_E \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( z, C_E \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ C_E \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_E &= \text{Energy ratio correction}\\
ER &= \text{Energy ratio (\%)}\\
z &= \text{Depth (m)}
\end{align*}
$$

#### `get_fines_content_factor__cetin2004standard`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_fines\_content\_factor\_\_cetin2004standard}(N_{160}, FC, \mathrm{is\_fine\_soil}) \\ \hspace{1em} FC \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( FC, 5, 35 \mathclose{}\right) \\ \hspace{1em} C_{FINES} \gets 1 + 0.004 FC + 0.05 \frac{FC}{N_{160}} \\ \hspace{1em} \mathbf{return} \ C_{FINES} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_{FINES} &= \text{Fines content factor}\\
N_{160} &= \text{Normalized blow count}\\
FC &= \text{Fines content (\%)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_friction_angle__schnaid2009prediction`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_friction\_angle\_\_schnaid2009prediction}(N_{160}, \mathrm{is\_fine\_soil}) \\ \hspace{1em} ϕ \gets 18 N_{160}^{0.234} \\ \hspace{1em} \mathbf{return} \ ϕ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ϕ &= \text{Friction angle (°)}\\
N_{160} &= \text{Normalized blow count}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_is_fine_soil_spt`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_is\_fine\_soil\_spt}(\mathrm{soil\_type2}) \\ \hspace{1em} \mathrm{is\_fine\_soil} \gets \mathrm{soil\_type2} \ne \textrm{"Coarse"} \\ \hspace{1em} \mathbf{return} \ \mathrm{is\_fine\_soil} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{soil\_type2} &= \text{Soil type 2}
\end{align*}
$$

#### `get_iterative_parameters_spt__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_iterative\_parameters\_spt\_\_idriss2008soil}(N_{60}, ΔN_{160}, σ_v', \mathrm{is\_fine\_soil}) \\ \hspace{1em} \mathrm{max\_iter} \gets 10 \\ \hspace{1em} \mathrm{tol} \gets 0.0001 \\ \hspace{1em} n \gets \mathrm{None} \\ \hspace{1em} C_n \gets \mathrm{None} \\ \hspace{1em} N_{160cs} \gets \mathrm{np}.\mathrm{ones\_like} \mathopen{}\left( N_{60} \mathclose{}\right) \\ \hspace{1em} \mathbf{for} \ \mathrm{\_} \in \mathrm{range} \mathopen{}\left( \mathrm{max\_iter} \mathclose{}\right) \ \mathbf{do} \\ \hspace{2em} \mathrm{clean\_sand\_normalized\_blow\_count\_old} \gets N_{160cs}.\mathrm{copy} \mathopen{}\left( \mathclose{}\right) \\ \hspace{2em} n \gets 0.784 - 0.0768 \sqrt{ \mathrm{np}.\mathrm{clip} \mathopen{}\left( N_{160cs}, 1, 46 \mathclose{}\right) } \\ \hspace{2em} C_n \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( \mathopen{}\left( \frac{101.325}{σ_v'} \mathclose{}\right)^{n}, 0, 1.7 \mathclose{}\right) \\ \hspace{2em} N_{160cs} \gets N_{60} \cdot C_n + ΔN_{160} \\ \hspace{2em} \mathbf{if} \ \mathrm{np}.\mathrm{nanmax} \mathopen{}\left( \mathopen{}\left| N_{160cs} - \mathrm{clean\_sand\_normalized\_blow\_count\_old} \mathclose{}\right| \mathclose{}\right) < \mathrm{tol} \\ \hspace{3em} \mathbf{break} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ for} \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( n, C_n, N_{160cs} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
n &= \text{Overburden stress exponent}\\
C_n &= \text{Overburden correction}\\
N_{160cs} &= \text{Clean sand normalized blow count}\\
N_{60} &= \text{Corrected blow count}\\
ΔN_{160} &= \text{Normalized blow count fines inc.}\\
σ_v' &= \text{Effective stress (kPa)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_normalized_blow_count__liao1986overburden`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_blow\_count\_\_liao1986overburden}(N_{60}, C_n, \mathrm{is\_fine\_soil}) \\ \hspace{1em} \textrm{" coduto: Although Liao and Whitman did not place any limits on this correction, it is probably best to keep
  (N1)60 < 2 corrected\_blow\_count. This limit avoids excessively high values at shallow depths "} \\ \hspace{1em} \textrm{" SPTCorr uses 0.4 <= overburden\_correction <= 1.7 limits "} \\ \hspace{1em} \textrm{" boulanger2014cpt shows 0.0 <= overburden\_correction <= 1.7 limits "} \\ \hspace{1em} \textrm{" Also used by cetin2004standard who limits it to 1.6 "} \\ \hspace{1em} \textrm{" Also used by cetin2018use who limits it to 2.0 "} \\ \hspace{1em} N_{160} \gets N_{60} \cdot C_n \\ \hspace{1em} \mathbf{return} \ N_{160} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_{160} &= \text{Normalized blow count}\\
N_{60} &= \text{Corrected blow count}\\
C_n &= \text{Overburden correction}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_normalized_blow_count_fines_inc__cetin2018use`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_blow\_count\_fines\_inc\_\_cetin2018use}(N_{160}, FC, \mathrm{is\_fine\_soil}) \\ \hspace{1em} \mathrm{cetineayy\_coeffs} \gets \mathrm{DataMaps}.\mathrm{ModelCoefficientsCetin2018}.\mathrm{data} \\ \hspace{1em} \mathopen{}\left( \mathrm{theta1}, \mathrm{theta4} \mathclose{}\right) \gets \mathopen{}\left( \mathrm{cetineayy\_coeffs}_{\textrm{"1"}}, \mathrm{cetineayy\_coeffs}_{\textrm{"4"}} \mathclose{}\right) \\ \hspace{1em} FC \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( FC, 5, 35 \mathclose{}\right) \\ \hspace{1em} ΔN_{160} \gets FC \cdot \mathopen{}\left( \mathrm{theta1} \cdot N_{160} + \mathrm{theta4} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ ΔN_{160} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ΔN_{160} &= \text{Normalized blow count fines inc.}\\
N_{160} &= \text{Normalized blow count}\\
FC &= \text{Fines content (\%)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_normalized_blow_count_fines_inc__idriss2006semi`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_blow\_count\_fines\_inc\_\_idriss2006semi}(FC, \mathrm{is\_fine\_soil}) \\ \hspace{1em} ΔN_{160} \gets \exp \mathopen{}\left( 1.63 + \frac{9.7}{FC + 0.01} - \mathopen{}\left( \frac{15.7}{FC + 0.01} \mathclose{}\right)^{2} \mathclose{}\right) \\ \hspace{1em} ΔN_{160} \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( ΔN_{160} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( ΔN_{160}, \mathrm{np}.\mathrm{isclose} \mathopen{}\left( ΔN_{160}, 0 \mathclose{}\right), 0 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ ΔN_{160} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ΔN_{160} &= \text{Normalized blow count fines inc.}\\
FC &= \text{Fines content (\%)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_normalized_blow_count_fines_inc_sr__seed1987design`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_blow\_count\_fines\_inc\_sr\_\_seed1987design}(FC, \mathrm{is\_fine\_soil}) \\ \hspace{1em} ΔN_{160} \gets \mathrm{PARAMETERS}_{\textrm{"fines\_content"}}.\mathrm{data\_bins}_{\textrm{"normalized\_blow\_count\_fines\_inc"}}.\mathrm{bin\_data} \mathopen{}\left( FC \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ ΔN_{160} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ΔN_{160-Sr} &= \text{Normalized blow count fines inc. (Sr)}\\
FC &= \text{Fines content (\%)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_normalized_residual_shear_strength__kramer2015empirical`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_residual\_shear\_strength\_\_kramer2015empirical}(N_{160}, σ_v', \mathrm{is\_fine\_soil}) \\ \hspace{1em} S_r \gets 101.325 \cdot \exp \mathopen{}\left( -8.444 + 0.109 N_{160} + 5.379 \mathopen{}\left( \frac{σ_v'}{101.325} \mathclose{}\right)^{0.1} \mathclose{}\right) \\ \hspace{1em} S_r \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( N_{160} \le 15, S_r, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} S_{r\ ratio} \gets \frac{S_r}{σ_v'} \\ \hspace{1em} \mathbf{return} \ S_{r\ ratio} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_{r\ ratio} &= \text{Normalized residual shear strength}\\
N_{160} &= \text{Normalized blow count}\\
σ_v' &= \text{Effective stress (kPa)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_normalized_residual_shear_strength__weber2015engineering`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_residual\_shear\_strength\_\_weber2015engineering}(N_{160cs}, σ_v', \mathrm{is\_fine\_soil}) \\ \hspace{1em} S_r \gets 0.048 \cdot \mathopen{}\left( \exp \mathopen{}\left( 0.1407 N_{160cs} + 4.2399 \mathopen{}\left( \frac{σ_v'}{101.325} \mathclose{}\right)^{0.12} \mathclose{}\right) - 0.43991 \mathopen{}\left( N_{160cs}^{1.45} + 0.2 N_{160cs} \cdot \mathopen{}\left( \frac{σ_v'}{101.325} \mathclose{}\right)^{2.48} + 41.13 \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} S_r \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( S_r, \mathrm{None}, 0.29 σ_v' \mathclose{}\right) \\ \hspace{1em} S_{r\ ratio} \gets \frac{S_r}{σ_v'} \\ \hspace{1em} \mathbf{return} \ S_{r\ ratio} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_{r\ ratio} &= \text{Normalized residual shear strength}\\
N_{160cs} &= \text{Clean sand normalized blow count}\\
σ_v' &= \text{Effective stress (kPa)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_normalized_residual_shear_strength_spt__idriss2007spt`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_residual\_shear\_strength\_spt\_\_idriss2007spt}(N_{160cs}, \mathrm{void\_redistribution\_is\_significant}) \\ \hspace{1em} \textrm{" Equation obtained from idriss2008soil "} \\ \hspace{1em} S_{r\ ratio} \gets \exp \mathopen{}\left( \frac{N_{160cs}}{16} + \mathopen{}\left( \frac{N_{160cs} - 16}{21.2} \mathclose{}\right)^{3} - 3 \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ \lnot \mathrm{void\_redistribution\_is\_significant} \\ \hspace{2em} S_{r\ ratio} \gets S_{r\ ratio} \cdot \mathopen{}\left( 1 + \exp \mathopen{}\left( \frac{N_{160cs}}{2.4} - 6.6 \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} S_{r\ ratio} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( S_{r\ ratio}, 0, \mathrm{tandg} \mathopen{}\left( 25 \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ S_{r\ ratio} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_{r\ ratio} &= \text{Normalized residual shear strength}\\
N_{160cs} &= \text{Clean sand normalized blow count}\\
\text{void\_redistribution\_is\_significant} &= \text{Void redistribution is significant}
\end{align*}
$$

#### `get_normalized_residual_shear_strength_spt__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_residual\_shear\_strength\_spt\_\_idriss2008soil}(N_{160cs-Sr}, \mathrm{void\_redistribution\_is\_significant}) \\ \hspace{1em} \mathbf{return} \ \mathrm{get\_normalized\_residual\_shear\_strength\_spt\_\_idriss2007spt} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_{r\ ratio} &= \text{Normalized residual shear strength}\\
N_{160cs-Sr} &= \text{Clean sand normalized blow count (Sr)}\\
\text{void\_redistribution\_is\_significant} &= \text{Void redistribution is significant}
\end{align*}
$$

#### `get_overburden_correction__cetin2004standard`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overburden\_correction\_\_cetin2004standard}(σ_v', n) \\ \hspace{1em} \mathbf{return} \ \mathrm{get\_overburden\_correction\_\_liao1986overburden} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_n &= \text{Overburden correction}\\
σ_v' &= \text{Effective stress (kPa)}\\
n &= \text{Overburden stress exponent}\\
C_{n\ lim} &= \text{Overburden correction limit}
\end{align*}
$$

#### `get_overburden_correction__cetin2018use`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overburden\_correction\_\_cetin2018use}(σ_v', n) \\ \hspace{1em} \mathbf{return} \ \mathrm{get\_overburden\_correction\_\_liao1986overburden} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_n &= \text{Overburden correction}\\
σ_v' &= \text{Effective stress (kPa)}\\
n &= \text{Overburden stress exponent}\\
C_{n\ lim} &= \text{Overburden correction limit}
\end{align*}
$$

#### `get_overburden_correction__liao1986overburden`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overburden\_correction\_\_liao1986overburden}(n, σ_v') \\ \hspace{1em} C_n \gets \mathopen{}\left( \frac{101.325}{σ_v'} \mathclose{}\right)^{n} \\ \hspace{1em} C_n \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( C_n, 0, C_{n\ lim} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ C_n \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_n &= \text{Overburden correction}\\
n &= \text{Overburden stress exponent}\\
σ_v' &= \text{Effective stress (kPa)}\\
C_{n\ lim} &= \text{Overburden correction limit}
\end{align*}
$$

#### `get_overburden_stress_exponent__liao1986overburden`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overburden\_stress\_exponent\_\_liao1986overburden}(z) \\ \hspace{1em} n \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( z, 0.5 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ n \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
n &= \text{Overburden stress exponent}\\
z &= \text{Depth (m)}
\end{align*}
$$

#### `get_peak_friction_angle__sorensen2013correlation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_peak\_friction\_angle\_\_sorensen2013correlation}(PI, \mathrm{is\_fine\_soil}) \\ \hspace{1em} ϕ' \gets 43 - 10 \log_{10} PI \\ \hspace{1em} \mathbf{return} \ ϕ' \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ϕ' &= \text{Peak friction angle (°)}\\
PI &= \text{Plasticity index (\%)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_permeability__chapuis2004predicting`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_permeability\_\_chapuis2004predicting}(e, D_{10}, \mathrm{is\_fine\_soil}) \\ \hspace{1em} k \gets 0.01 \cdot 2.4622 \mathopen{}\left( D_{10}^{2} \cdot \frac{e^{3}}{1 + e} \mathclose{}\right)^{0.7825} \\ \hspace{1em} \mathbf{return} \ k \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
k &= \text{Permeability (m/s)}\\
e &= \text{Void ratio}\\
D_{10} &= \text{Diameter at 10\% finer (mm)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_permeability__chapuis2012predicting`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_permeability\_\_chapuis2012predicting}(e, D_{10}, LL, γ, \mathrm{is\_fine\_soil}) \\ \hspace{1em} \mathrm{k\_is\_fine\_soil} \gets \mathrm{get\_permeability\_\_mbonimpa2002practical} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathrm{k\_is\_granular} \gets \mathrm{get\_permeability\_\_chapuis2004predicting} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} k \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( \mathrm{is\_fine\_soil}, \mathrm{k\_is\_fine\_soil}, \mathrm{k\_is\_granular} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ k \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
k &= \text{Permeability (m/s)}\\
e &= \text{Void ratio}\\
D_{10} &= \text{Diameter at 10\% finer (mm)}\\
LL &= \text{Liquid limit (\%)}\\
γ &= \text{Unit weight (kN/m3)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
γ_w &= \text{Water unit weight (kN/m3)}
\end{align*}
$$

#### `get_permeability__mbonimpa2002practical`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_permeability\_\_mbonimpa2002practical}(e, LL, γ, \mathrm{is\_fine\_soil}) \\ \hspace{1em} \mathrm{C\_p} \gets 5.6 \\ \hspace{1em} \mathrm{mu\_w} \gets 0.001 \\ \hspace{1em} x \gets 7.7 LL^{-0.15} - 3 \\ \hspace{1em} \chi \gets 1.5 \\ \hspace{1em} \mathrm{rho\_s} \gets \frac{1000 γ}{g} \\ \hspace{1em} k \gets 0.01 \mathrm{C\_p} \frac{γ_w}{\mathrm{mu\_w}} \frac{e^{3 + x}}{1 + e} \frac{1}{\mathrm{rho\_s}^{2} \cdot LL^{2 \chi}} \\ \hspace{1em} \mathbf{return} \ k \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
k &= \text{Permeability (m/s)}\\
e &= \text{Void ratio}\\
LL &= \text{Liquid limit (\%)}\\
γ &= \text{Unit weight (kN/m3)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
γ_w &= \text{Water unit weight (kN/m3)}
\end{align*}
$$

#### `get_poisson_ratio__bowles1996foundation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_poisson\_ratio\_\_bowles1996foundation}(z, \mathrm{soil\_type}, \mathrm{below\_water\_table}) \\ \hspace{1em} \textrm{" Table 7.2 Values or value ranges for Poisson's ratio ν by bowles1996foundation "} \\ \hspace{1em} \mathrm{mapping} \gets \mathrm{DataMaps}.\mathrm{PoissonRatioBowles1996}.\mathrm{to\_dict} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} ν \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( z, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( ν, \mathopen{}\left( \mathrm{soil\_type} = \textrm{"Clay"} \mathclose{}\right) \mathbin{\&} \mathord{\sim} \mathrm{below\_water\_table}, \mathrm{mapping}_{\textrm{"Clay.Unsaturated"}} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( ν, \mathopen{}\left( \mathrm{soil\_type} = \textrm{"Clay"} \mathclose{}\right) \mathbin{\&} \mathrm{below\_water\_table}, \mathrm{mapping}_{\textrm{"Clay.Saturated"}} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( ν, \mathrm{soil\_type} = \textrm{"Silt"}, \mathrm{mapping}_{\textrm{"Silt"}} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( ν, \mathopen{}\left( \mathrm{soil\_type} = \textrm{"Sand"} \mathclose{}\right) \mathbin{|} \mathopen{}\left( \mathrm{soil\_type} = \textrm{"Gravel"} \mathclose{}\right), \mathrm{mapping}_{\textrm{"Sand, gravelly sand"}} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( ν, \mathopen{}\left( \mathrm{soil\_type} = \textrm{"Peat"} \mathclose{}\right) \mathbin{|} \mathopen{}\left( \mathrm{soil\_type} = \textrm{"Organic"} \mathclose{}\right), \mathrm{mapping}_{\textrm{"Peat, organic (from Long et al. (2022))"}} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( ν, \mathrm{soil\_type} = \textrm{"Other"}, \mathrm{mapping}_{\textrm{"All soils"}} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ ν \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ν &= \text{Poisson’s ratio}\\
z &= \text{Depth (m)}\\
\text{soil\_type} &= \text{Soil type}\\
\text{below\_water\_table} &= \text{Below water table}
\end{align*}
$$

#### `get_recompression_index__lo1982prediction`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_recompression\_index\_\_lo1982prediction}(C_c, \mathrm{is\_fine\_soil}) \\ \hspace{1em} C_r \gets -0.00327 + 0.139 C_c \\ \hspace{1em} \mathbf{return} \ C_r \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_r &= \text{Recompression index}\\
C_c &= \text{Compression index}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_recompression_ratio__lo1982prediction`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_recompression\_ratio\_\_lo1982prediction}(CR, \mathrm{is\_fine\_soil}) \\ \hspace{1em} RR \gets \mathrm{get\_recompression\_index\_\_lo1982prediction} \mathopen{}\left( CR \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ RR \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
RR &= \text{Recompression ratio}\\
CR &= \text{Compression ratio}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_relative_density__idriss2003estimating`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_relative\_density\_\_idriss2003estimating}(N_{160}, \mathrm{is\_fine\_soil}) \\ \hspace{1em} D_r \gets 100 \sqrt{ \frac{N_{160}}{46} } \\ \hspace{1em} \mathbf{return} \ D_r \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
D_r &= \text{Relative density (\%)}\\
N_{160} &= \text{Normalized blow count}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_remolded_undrained_shear_strength__degroot2019engineering`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_remolded\_undrained\_shear\_strength\_\_degroot2019engineering}(LI, \mathrm{is\_fine\_soil}) \\ \hspace{1em} \textrm{" Based on ngi database for liquidity\_index > 0 "} \\ \hspace{1em} S_{ur} \gets 4.5 LI^{-1.5} \\ \hspace{1em} S_{ur} \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( LI > 0, S_{ur}, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ S_{ur} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_{ur} &= \text{Remolded undrained shear strength (kPa)}\\
LI &= \text{Liquidity index}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_rod_length_correction__cetin2004standard`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_rod\_length\_correction\_\_cetin2004standard}(z, \mathrm{rod\_length}, \mathrm{use\_simplified\_blows\_correction}) \\ \hspace{1em} \mathbf{if} \ \mathrm{use\_simplified\_blows\_correction} \\ \hspace{2em} C_R \gets 1 \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} C_R \gets \frac{1}{0.9898 + \frac{4.3166}{\mathopen{}\left( \mathrm{rod\_length} + z \mathclose{}\right)^{2}}} \\ \hspace{2em} C_R \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( C_R, 0.75, 1 \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ C_R \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_R &= \text{Rod length correction}\\
z &= \text{Depth (m)}\\
\text{rod\_length} &= \text{Rod length (m)}\\
\text{use\_simplified\_blows\_correction} &= \text{Use simplified blows correction}
\end{align*}
$$

#### `get_rod_length_correction__cetin2018use`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_rod\_length\_correction\_\_cetin2018use}(z, \mathrm{rod\_length}, \mathrm{use\_simplified\_blows\_correction}) \\ \hspace{1em} \mathbf{if} \ \mathrm{use\_simplified\_blows\_correction} \\ \hspace{2em} C_R \gets 1 \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} C_R \gets 0.48 + 0.225 \log \mathopen{}\left( \mathrm{rod\_length} + z \mathclose{}\right) \\ \hspace{2em} C_R \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( C_R \mathclose{}\right) \\ \hspace{2em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( C_R, \mathrm{rod\_length} + z > 10, 1 \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ C_R \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_R &= \text{Rod length correction}\\
z &= \text{Depth (m)}\\
\text{rod\_length} &= \text{Rod length (m)}\\
\text{use\_simplified\_blows\_correction} &= \text{Use simplified blows correction}
\end{align*}
$$

#### `get_rod_length_correction__skempton1986standard`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_rod\_length\_correction\_\_skempton1986standard}(z, \mathrm{rod\_length}, \mathrm{use\_simplified\_blows\_correction}) \\ \hspace{1em} \mathbf{if} \ \mathrm{use\_simplified\_blows\_correction} \\ \hspace{2em} C_R \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( z, 1 \mathclose{}\right) \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} C_R \gets \mathrm{PARAMETERS}_{\textrm{"depth\_plus\_rod\_length"}}.\mathrm{data\_bins}_{\textrm{"rod\_length\_correction"}}.\mathrm{bin\_data} \mathopen{}\left( z + \mathrm{rod\_length} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ C_R \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_R &= \text{Rod length correction}\\
z &= \text{Depth (m)}\\
\text{rod\_length} &= \text{Rod length (m)}\\
\text{use\_simplified\_blows\_correction} &= \text{Use simplified blows correction}
\end{align*}
$$

#### `get_shear_velocity__wair2012guidelines`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shear\_velocity\_\_wair2012guidelines}(N_{60}, σ_v', \mathrm{soil\_type}, \mathrm{geological\_epoch}) \\ \hspace{1em} \textrm{" Age scaling factors are provided too: [All, Clay \& Silt, Sand]: 0.87, 0.88, 0.90 for Holocene and
   1.13, 1.12, 1.17 for Pleistocene "} \\ \hspace{1em} \mathrm{conditions} \gets \mathopen{}\left[ \mathopen{}\left( \mathrm{soil\_type} = \textrm{"Clay"} \mathclose{}\right) \mathbin{|} \mathopen{}\left( \mathrm{soil\_type} = \textrm{"Silt"} \mathclose{}\right), \mathrm{soil\_type} = \textrm{"Sand"}, \mathopen{}\left( \mathrm{soil\_type} = \textrm{"Gravel"} \mathclose{}\right) \mathbin{\&} \mathopen{}\left( \mathrm{geological\_epoch} = \textrm{"Holocene"} \mathclose{}\right), \mathopen{}\left( \mathrm{soil\_type} = \textrm{"Gravel"} \mathclose{}\right) \mathbin{\&} \mathopen{}\left( \mathrm{geological\_epoch} = \textrm{"Pleistocene"} \mathclose{}\right) \mathclose{}\right] \\ \hspace{1em} \mathrm{choices} \gets \mathopen{}\left[ 26 N_{60}^{0.17} \cdot σ_v'^{0.32}, 30 N_{60}^{0.23} \cdot σ_v'^{0.23}, 53 N_{60}^{0.19} \cdot σ_v'^{0.18}, 115 N_{60}^{0.17} \cdot σ_v'^{0.12} \mathclose{}\right] \\ \hspace{1em} V_s \gets \mathrm{np}.\mathrm{select} \mathopen{}\left( \mathrm{conditions}, \mathrm{choices} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ V_s \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
V_s &= \text{Shear velocity (m/s)}\\
N_{60} &= \text{Corrected blow count}\\
σ_v' &= \text{Effective stress (kPa)}\\
\text{soil\_type} &= \text{Soil type}\\
\text{geological\_epoch} &= \text{Geological epoch}
\end{align*}
$$

#### `get_undrained_shear_strength__sivrikaya2006determination`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_undrained\_shear\_strength\_\_sivrikaya2006determination}(N_{60}, \mathrm{uscs\_symbol}, \mathrm{soil\_type}, \mathrm{is\_fine\_soil}) \\ \hspace{1em} \mathrm{conditions} \gets \mathopen{}\left[ \mathrm{uscs\_symbol} = \textrm{"CH"}, \mathrm{uscs\_symbol} = \textrm{"CL"}, \mathrm{soil\_type} = \textrm{"Clay"}, \mathrm{is\_fine\_soil} \mathclose{}\right] \\ \hspace{1em} \mathrm{choices} \gets \mathopen{}\left[ 7.8 N_{60}, 5.35 N_{60}, 6.9 N_{60}, 6.35 N_{60} \mathclose{}\right] \\ \hspace{1em} S_u \gets \mathrm{np}.\mathrm{select} \mathopen{}\left( \mathrm{conditions}, \mathrm{choices} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ S_u \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_u &= \text{Undrained shear strength (kPa)}\\
N_{60} &= \text{Corrected blow count}\\
\text{uscs\_symbol} &= \text{USCS symbol}\\
\text{soil\_type} &= \text{Soil type}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_unit_weight__cetin2018use`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_unit\_weight\_\_cetin2018use}(N_{60}, \mathrm{is\_fine\_soil}, \mathrm{below\_water\_table}, γ_{default}) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_get\_unit\_weight\_\_cetin2018use\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
γ &= \text{Unit weight (kN/m3)}\\
N_{60} &= \text{Corrected blow count}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{below\_water\_table} &= \text{Below water table}\\
γ_{default} &= \text{Default unit weight (kN/m3)}
\end{align*}
$$
