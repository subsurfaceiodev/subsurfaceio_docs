---
title: liquefaction.py
---

#### `get_area_replacement_ratio`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_area\_replacement\_ratio}(\mathrm{stone\_column\_arrangement}, D, S) \\ \hspace{1em} \mathbf{if} \ \mathrm{stone\_column\_arrangement} = \textrm{"triangular"} \\ \hspace{2em} A_r \gets 0.907 \mathopen{}\left( \frac{D}{S} \mathclose{}\right)^{2} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{stone\_column\_arrangement} = \textrm{"rectangular"} \\ \hspace{3em} A_r \gets \mathrm{np}.\pi \cdot \mathopen{}\left( \frac{0.5 D}{S} \mathclose{}\right)^{2} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} A_r \gets \mathrm{None} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ A_r \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
A_r &= \text{Area replacement ratio}\\
\text{stone\_column\_arrangement} &= \text{Stone column arrangement}\\
D &= \text{Stone column diameter (m)}\\
S &= \text{Stone column spacing (m)}
\end{align*}
$$

#### `get_cyclic_resistance_ratio`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_cyclic\_resistance\_ratio}(CRR_{7.5}, MSF, K_σ, K_α, \mathrm{is\_potentially\_liquefiable}) \\ \hspace{1em} CRR \gets CRR_{7.5} \cdot K_σ \cdot K_α \cdot MSF \\ \hspace{1em} CRR \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( CRR, \mathrm{None}, 2 \mathclose{}\right) \\ \hspace{1em} CRR \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( \mathrm{np}.\mathrm{isnan} \mathopen{}\left( CRR \mathclose{}\right) \mathbin{|} \mathord{\sim} \mathrm{is\_potentially\_liquefiable}, 2, CRR \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ CRR \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
CRR &= \text{Cyclic resistance ratio}\\
CRR_{7.5} &= \text{Cyclic resistance ratio magnitude 7.5}\\
MSF &= \text{Magnitude scaling factor}\\
K_σ &= \text{Overburden correction for CRR}\\
K_α &= \text{Initial static shear correction}\\
\text{is\_potentially\_liquefiable} &= \text{Is potentially liquefiable}
\end{align*}
$$

#### `get_cyclic_resistance_ratio__cetin2004standard`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_cyclic\_resistance\_ratio\_\_cetin2004standard}(N_{160}, σ_v', FC, M_w, \mathrm{is\_potentially\_liquefiable}) \\ \hspace{1em} PL_{liq} \gets 50 \\ \hspace{1em} \mathopen{}\left( \mathrm{theta1}, \mathrm{theta2}, \mathrm{theta3}, \mathrm{theta4}, \mathrm{theta5}, \mathrm{theta6}, \mathrm{theta\_epsilon} \mathclose{}\right) \gets \mathrm{DataMaps}.\mathrm{ModelCoefficientsCetin2004}.\mathrm{data\_values} \\ \hspace{1em} CRR \gets \exp \mathopen{}\left( \frac{N_{160} \cdot \mathopen{}\left( 1 + \mathrm{theta1} \cdot FC \mathclose{}\right) - \mathrm{theta2} \cdot \log M_w - \mathrm{theta3} \cdot \log \mathopen{}\left( \frac{σ_v'}{101.325} \mathclose{}\right) + \mathrm{theta4} \cdot FC + \mathrm{theta5} + \mathrm{theta\_epsilon} \cdot \mathrm{norm} \mathopen{}\left( \mathclose{}\right).\mathrm{ppf} \mathopen{}\left( \frac{PL_{liq}}{100} \mathclose{}\right)}{\mathrm{theta6}} \mathclose{}\right) \\ \hspace{1em} CRR \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( \mathrm{np}.\mathrm{isnan} \mathopen{}\left( CRR \mathclose{}\right) \mathbin{|} \mathord{\sim} \mathrm{is\_potentially\_liquefiable}, 2, CRR \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ CRR \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
CRR &= \text{Cyclic resistance ratio}\\
N_{160} &= \text{Normalized blow count}\\
σ_v' &= \text{Effective stress (kPa)}\\
FC &= \text{Fines content (\%)}\\
M_w &= \text{Moment magnitude}\\
\text{is\_potentially\_liquefiable} &= \text{Is potentially liquefiable}
\end{align*}
$$

#### `get_cyclic_resistance_ratio__cetin2018use`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_cyclic\_resistance\_ratio\_\_cetin2018use}(N_{160}, σ_v', FC, M_w, \mathrm{is\_potentially\_liquefiable}) \\ \hspace{1em} PL_{liq} \gets 50 \\ \hspace{1em} \mathopen{}\left( \mathrm{theta1}, \mathrm{theta2}, \mathrm{theta3}, \mathrm{theta4}, \mathrm{theta5}, \mathrm{theta6}, \mathrm{theta\_epsilon} \mathclose{}\right) \gets \mathrm{DataMaps}.\mathrm{ModelCoefficientsCetin2018}.\mathrm{data\_values} \\ \hspace{1em} CRR \gets \exp \mathopen{}\left( \frac{N_{160} \cdot \mathopen{}\left( 1 + \mathrm{theta1} \cdot FC \mathclose{}\right) - \mathrm{theta2} \cdot \log M_w - \mathrm{theta3} \cdot \log \mathopen{}\left( \frac{σ_v'}{101.325} \mathclose{}\right) + \mathrm{theta4} \cdot FC + \mathrm{theta5} + \mathrm{theta\_epsilon} \cdot \mathrm{norm} \mathopen{}\left( \mathclose{}\right).\mathrm{ppf} \mathopen{}\left( \frac{PL_{liq}}{100} \mathclose{}\right)}{\mathrm{theta6}} \mathclose{}\right) \\ \hspace{1em} CRR \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( \mathrm{np}.\mathrm{isnan} \mathopen{}\left( CRR \mathclose{}\right) \mathbin{|} \mathord{\sim} \mathrm{is\_potentially\_liquefiable}, 2, CRR \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ CRR \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
CRR &= \text{Cyclic resistance ratio}\\
N_{160} &= \text{Normalized blow count}\\
σ_v' &= \text{Effective stress (kPa)}\\
FC &= \text{Fines content (\%)}\\
M_w &= \text{Moment magnitude}\\
\text{is\_potentially\_liquefiable} &= \text{Is potentially liquefiable}
\end{align*}
$$

#### `get_cyclic_resistance_ratio__saye2021common`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_cyclic\_resistance\_ratio\_\_saye2021common}(CRR_{7.5}, MSF, \mathrm{is\_potentially\_liquefiable}) \\ \hspace{1em} K_σ \gets 1 \\ \hspace{1em} K_α \gets 1 \\ \hspace{1em} \mathbf{return} \ \mathrm{get\_cyclic\_resistance\_ratio} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
CRR &= \text{Cyclic resistance ratio}\\
CRR_{7.5} &= \text{Cyclic resistance ratio magnitude 7.5}\\
MSF &= \text{Magnitude scaling factor}\\
\text{is\_potentially\_liquefiable} &= \text{Is potentially liquefiable}
\end{align*}
$$

#### `get_cyclic_resistance_ratio_magnitude_7_5__cetin2018use`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_cyclic\_resistance\_ratio\_magnitude\_7\_5\_\_cetin2018use}(CRR, MSF, K_σ, K_α, \mathrm{is\_potentially\_liquefiable}) \\ \hspace{1em} CRR_{7.5} \gets \frac{CRR}{K_σ \cdot K_α \cdot MSF} \\ \hspace{1em} CRR_{7.5} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( CRR_{7.5}, \mathrm{None}, 2 \mathclose{}\right) \\ \hspace{1em} CRR_{7.5} \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( \mathrm{np}.\mathrm{isnan} \mathopen{}\left( CRR_{7.5} \mathclose{}\right) \mathbin{|} \mathord{\sim} \mathrm{is\_potentially\_liquefiable}, 2, CRR_{7.5} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ CRR_{7.5} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
CRR_{7.5} &= \text{Cyclic resistance ratio magnitude 7.5}\\
CRR &= \text{Cyclic resistance ratio}\\
MSF &= \text{Magnitude scaling factor}\\
K_σ &= \text{Overburden correction for CRR}\\
K_α &= \text{Initial static shear correction}\\
\text{is\_potentially\_liquefiable} &= \text{Is potentially liquefiable}
\end{align*}
$$

#### `get_cyclic_resistance_ratio_magnitude_7_5_spt__idriss2006semi`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_cyclic\_resistance\_ratio\_magnitude\_7\_5\_spt\_\_idriss2006semi}(N_{160cs}, \mathrm{is\_potentially\_liquefiable}) \\ \hspace{1em} CRR_{7.5} \gets \exp \mathopen{}\left( \frac{N_{160cs}}{14.1} + \mathopen{}\left( \frac{N_{160cs}}{126} \mathclose{}\right)^{2} - \mathopen{}\left( \frac{N_{160cs}}{23.6} \mathclose{}\right)^{3} + \mathopen{}\left( \frac{N_{160cs}}{25.4} \mathclose{}\right)^{4} - 2.8 \mathclose{}\right) \\ \hspace{1em} CRR_{7.5} \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( \mathopen{}\left( N_{160cs} \ge 37.5 \mathclose{}\right) \mathbin{|} \mathrm{np}.\mathrm{isnan} \mathopen{}\left( CRR_{7.5} \mathclose{}\right) \mathbin{|} \mathord{\sim} \mathrm{is\_potentially\_liquefiable}, 2, CRR_{7.5} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ CRR_{7.5} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
CRR_{7.5} &= \text{Cyclic resistance ratio magnitude 7.5}\\
N_{160cs} &= \text{Clean sand normalized blow count}\\
\text{is\_potentially\_liquefiable} &= \text{Is potentially liquefiable}
\end{align*}
$$

#### `get_cyclic_stress_ratio`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_cyclic\_stress\_ratio}(PGA, σ_v, σ_v', r_d, sc_{present}, K_G) \\ \hspace{1em} CSR \gets 0.65 PGA \frac{σ_v}{σ_v'} \cdot r_d \\ \hspace{1em} CSR \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( CSR \mathclose{}\right) \\ \hspace{1em} sc_{present} \gets \mathrm{np}.\mathrm{broadcast\_to} \mathopen{}\left( sc_{present}, CSR.\mathrm{shape} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( CSR, sc_{present}, CSR \cdot K_G \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ CSR \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
CSR &= \text{Cyclic stress ratio}\\
PGA &= \text{Peak ground acceleration (g)}\\
σ_v &= \text{Total stress (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
r_d &= \text{Shear stress reduction coefﬁcient}\\
sc_{present} &= \text{Stone column is present}\\
K_G &= \text{Shear stress reduction factor}
\end{align*}
$$

#### `get_cyclic_stress_ratio_ss_20_1d_1atm__cetin2009probabilistica`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_cyclic\_stress\_ratio\_ss\_20\_1d\_1atm\_\_cetin2009probabilistica}(CSR, K_σ, K_{mc}, K_r) \\ \hspace{1em} CSR_{SS,20,1D,1atm} \gets CSR \cdot K_σ \cdot K_{mc} \cdot K_r \\ \hspace{1em} \mathbf{return} \ CSR_{SS,20,1D,1atm} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
CSR_{SS,20,1D,1atm} &= \text{Cyclic stress ratio SS,20,1D,1atm}\\
CSR &= \text{Cyclic stress ratio}\\
K_σ &= \text{Overburden correction for CRR}\\
K_{mc} &= \text{Membrane compliance correction}\\
K_r &= \text{Triaxial planes correction}
\end{align*}
$$

#### `get_depth_middle`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_depth\_middle}(z, H) \\ \hspace{1em} z_{middle} \gets z - \frac{H}{2} \\ \hspace{1em} \mathbf{return} \ z_{middle} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
z_{middle} &= \text{Depth middle (m)}\\
z &= \text{Depth (m)}\\
H &= \text{Thickness (m)}
\end{align*}
$$

#### `get_initial_static_shear_correction`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_initial\_static\_shear\_correction}() \\ \hspace{1em} K_α \gets 1 \\ \hspace{1em} \mathbf{return} \ K_α \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K_α &= \text{Initial static shear correction}
\end{align*}
$$

#### `get_is_potentially_liquefiable`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_is\_potentially\_liquefiable}(\mathrm{below\_water\_table}, z, LIQ_{max\ z}, \mathrm{soil\_type}, \mathrm{exclude\_clay\_like\_sands}, \mathrm{uscs\_symbol}, FC, PI) \\ \hspace{1em} \mathbf{if} \ \mathrm{np}.\mathrm{isnan} \mathopen{}\left( LIQ_{max\ z} \mathclose{}\right) \\ \hspace{2em} LIQ_{max\ z} \gets \mathrm{np}.\mathrm{inf} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathrm{is\_potentially\_liquefiable} \gets \mathrm{below\_water\_table} \mathbin{\&} \mathopen{}\left( z \le LIQ_{max\ z} \mathclose{}\right) \mathbin{\&} \mathopen{}\left( \mathrm{soil\_type} = \textrm{"Sand"} \mathclose{}\right) \\ \hspace{1em} \mathrm{is\_potentially\_liquefiable} \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( \mathrm{is\_potentially\_liquefiable} \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ \mathrm{exclude\_clay\_like\_sands} \\ \hspace{2em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( \mathrm{is\_potentially\_liquefiable}, \mathopen{}\left( \mathrm{uscs\_symbol} = \textrm{"SC"} \mathclose{}\right) \mathbin{\&} \mathopen{}\left( FC > 35 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( PI > 12 \mathclose{}\right), \mathrm{False} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathrm{is\_potentially\_liquefiable} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{is\_potentially\_liquefiable} &= \text{Is potentially liquefiable}\\
\text{below\_water\_table} &= \text{Below water table}\\
z &= \text{Depth (m)}\\
LIQ_{max\ z} &= \text{Liquefaction max. depth (m)}\\
\text{soil\_type} &= \text{Soil type}\\
\text{exclude\_clay\_like\_sands} &= \text{Exclude clay-like sands}\\
\text{uscs\_symbol} &= \text{USCS symbol}\\
FC &= \text{Fines content (\%)}\\
PI &= \text{Plasticity index (\%)}
\end{align*}
$$

#### `get_is_potentially_liquefiable_thickness`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_is\_potentially\_liquefiable\_thickness}(H, \mathrm{is\_potentially\_liquefiable}) \\ \hspace{1em} \textrm{" calculated as the consecutive runs of potentially liquefiable layers thickness "} \\ \hspace{1em} \mathbf{if} \ \mathrm{np}.\mathrm{ndim} \mathopen{}\left( \mathrm{is\_potentially\_liquefiable} \mathclose{}\right) = 0 \\ \hspace{2em} \mathbf{return} \ \left\{ \begin{array}{ll} H, & \mathrm{if} \ \mathrm{is\_potentially\_liquefiable} \\ 0, & \mathrm{otherwise} \end{array} \right. \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathrm{is\_potentially\_liquefiable\_thickness} \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( H, 0 \mathclose{}\right) \\ \hspace{1em} \mathopen{}\left( \mathrm{run\_values}, \mathrm{run\_starts}, \mathrm{run\_lengths} \mathclose{}\right) \gets \mathrm{find\_runs} \mathopen{}\left( \mathrm{is\_potentially\_liquefiable} \mathclose{}\right) \\ \hspace{1em} \mathbf{for} \ \mathopen{}\left( \mathrm{value}, \mathrm{starts}, \mathrm{length} \mathclose{}\right) \in \mathrm{zip} \mathopen{}\left( \mathrm{run\_values}, \mathrm{run\_starts}, \mathrm{run\_lengths} \mathclose{}\right) \ \mathbf{do} \\ \hspace{2em} \mathbf{if} \ \mathrm{value} \\ \hspace{3em} \mathrm{ends} \gets \mathrm{starts} + \mathrm{length} \\ \hspace{3em} \mathrm{indices} \gets \mathrm{np}.\mathrm{arange} \mathopen{}\left( \mathrm{starts}, \mathrm{ends} \mathclose{}\right) \\ \hspace{3em} \mathrm{is\_potentially\_liquefiable\_thickness}_{\mathrm{indices}} \gets \sum \mathrm{thickness}_{\mathrm{indices}} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ for} \\ \hspace{1em} \mathbf{return} \ \mathrm{is\_potentially\_liquefiable\_thickness} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{is\_potentially\_liquefiable\_thickness} &= \text{Is potentially liquefiable thickness (m)}\\
H &= \text{Thickness (m)}\\
\text{is\_potentially\_liquefiable} &= \text{Is potentially liquefiable}
\end{align*}
$$

#### `get_is_t15_liquefiable_layers`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_is\_t15\_liquefiable\_layers}(\mathrm{is\_potentially\_liquefiable}, N_{160}, LD_{potential}) \\ \hspace{1em} T_{15\ flag} \gets \mathrm{is\_potentially\_liquefiable} \mathbin{\&} \mathopen{}\left( N_{160} < 15 \mathclose{}\right) \mathbin{\&} LD_{potential} \\ \hspace{1em} \mathbf{return} \ T_{15\ flag} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
T_{15\ flag} &= \text{Is T15 liquefiable layers}\\
\text{is\_potentially\_liquefiable} &= \text{Is potentially liquefiable}\\
N_{160} &= \text{Normalized blow count}\\
LD_{potential} &= \text{Lateral displacement potential}
\end{align*}
$$

#### `get_lateral_displacement_inc__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_lateral\_displacement\_inc\_\_idriss2008soil}(z) \\ \hspace{1em} LD_i \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( z, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ LD_i \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
LD_i &= \text{Lateral spread displacement inc. (m)}\\
z &= \text{Depth (m)}
\end{align*}
$$

#### `get_lateral_displacement_index`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_lateral\_displacement\_index}(LDI_i) \\ \hspace{1em} LDI \gets \mathrm{reverse\_cumsum} \mathopen{}\left( LDI_i \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ LDI \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
LDI &= \text{Lateral displacement index (m)}\\
LDI_i &= \text{Lateral displacement index inc. (m)}
\end{align*}
$$

#### `get_lateral_displacement_index_inc`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_lateral\_displacement\_index\_inc}(γ_{max}, H, LD_{potential}) \\ \hspace{1em} LDI_i \gets \frac{γ_{max}}{100} \cdot H \\ \hspace{1em} LDI_i \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( LD_{potential}, LDI_i, 0 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ LDI_i \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
LDI_i &= \text{Lateral displacement index inc. (m)}\\
γ_{max} &= \text{Max. shear strain (\%)}\\
H &= \text{Thickness (m)}\\
LD_{potential} &= \text{Lateral displacement potential}
\end{align*}
$$

#### `get_lateral_displacement_index_sum`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_lateral\_displacement\_index\_sum}(LDI_i) \\ \hspace{1em} ΣLDI \gets \sum LDI_i \\ \hspace{1em} \mathbf{return} \ ΣLDI \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ΣLDI &= \text{Lateral displacement index sum (m)}\\
LDI_i &= \text{Lateral displacement index inc. (m)}
\end{align*}
$$

#### `get_lateral_displacement_potential`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_lateral\_displacement\_potential}(\mathrm{is\_potentially\_liquefiable\_thickness}, LD_{min\ thickness}) \\ \hspace{1em} LD_{potential} \gets \mathrm{is\_potentially\_liquefiable\_thickness} \ge LD_{min\ thickness} \\ \hspace{1em} \mathbf{return} \ LD_{potential} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
LD_{potential} &= \text{Lateral displacement potential}\\
\text{is\_potentially\_liquefiable\_thickness} &= \text{Is potentially liquefiable thickness (m)}\\
LD_{min\ thickness} &= \text{Lateral displacement min. thickness (m)}
\end{align*}
$$

#### `get_lateral_spread_displacement`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_lateral\_spread\_displacement}(LD_i) \\ \hspace{1em} LD \gets \mathrm{reverse\_cumsum} \mathopen{}\left( LD_i \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ LD \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
LD &= \text{Lateral spread displacement (m)}\\
LD_i &= \text{Lateral spread displacement inc. (m)}
\end{align*}
$$

#### `get_lateral_spread_displacement_inc__youd2002revised`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_lateral\_spread\_displacement\_inc\_\_youd2002revised}(\mathrm{site\_ground\_condition}, M_w, R, LD_{potential}, T_{15\ flag}, FC, D_{50}, H, S, H, L, LD_{scalar}) \\ \hspace{1em} \mathrm{site\_ground\_condition} \gets \mathrm{site\_ground\_condition}.\mathrm{item} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} LD_i \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{site\_ground\_condition} = \textrm{"level\_ground"} \\ \hspace{2em} \mathbf{if} \ \lnot LD_{scalar} \\ \hspace{3em} LD_i \gets \mathrm{np}.\mathrm{zeros\_like} \mathopen{}\left( H \mathclose{}\right) \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} LD_i \gets 0 \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{return} \ LD_i \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathopen{}\left( T_{15}, FC_{T15}, D_{50T15} \mathclose{}\right) \gets \mathrm{get\_youd2002revised\_t15\_parameters} \mathopen{}\left( T_{15\ flag}, FC, D_{50}, H, LD_{scalar} \mathclose{}\right) \\ \hspace{2em} \mathbf{if} \ \mathrm{site\_ground\_condition} = \textrm{"sloping\_ground"} \\ \hspace{3em} \mathbf{if} \ \lnot \mathopen{}\left( 0.1 \le S \le 6 \mathclose{}\right) \\ \hspace{4em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"ground\_slope must be between 0.1 to 6 \%"} \mathclose{}\right) \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{3em} LD_i \gets 10^{-16.213 + 1.532 M_w - 1.406 \log_{10} \mathopen{}\left( 10^{0.89 M_w - 5.64} + R \mathclose{}\right) - 0.012 R + 0.338 \log_{10} S + 0.54 \log_{10} T_{15} + 3.413 \log_{10} \mathopen{}\left( 100.0 - FC_{T15} \mathclose{}\right) - 0.795 \log_{10} \mathopen{}\left( D_{50T15} + 0.1 \mathclose{}\right)} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ \mathrm{site\_ground\_condition} = \textrm{"free\_face"} \\ \hspace{4em} \mathbf{if} \ \lnot \mathopen{}\left( 1 \le 100 \frac{H}{L} \le 20 \mathclose{}\right) \\ \hspace{5em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"free\_face\_height / free\_face\_length must be between 1 to 20 \%"} \mathclose{}\right) \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{4em} LD_i \gets 10^{-16.713 + 1.532 M_w - 1.406 \log_{10} \mathopen{}\left( 10^{0.89 M_w - 5.64} + R \mathclose{}\right) - 0.012 R + 0.592 \log_{10} \mathopen{}\left( 100 \frac{H}{L} \mathclose{}\right) + 0.54 \log_{10} T_{15} + 3.413 \log_{10} \mathopen{}\left( 100 - FC_{T15} \mathclose{}\right) - 0.795 \log_{10} \mathopen{}\left( D_{50T15} + 0.1 \mathclose{}\right)} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{if} \ \lnot LD_{scalar} \\ \hspace{3em} LD_i \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( LD_i \mathclose{}\right) \\ \hspace{3em} LD_i \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( LD_{potential}, LD_i, 0 \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ LD_i \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
LD_i &= \text{Lateral spread displacement inc. (m)}\\
\text{site\_ground\_condition} &= \text{Site ground condition}\\
M_w &= \text{Moment magnitude}\\
R &= \text{Site-to-seismic-source distance (km)}\\
LD_{potential} &= \text{Lateral displacement potential}\\
T_{15\ flag} &= \text{Is T15 liquefiable layers}\\
FC &= \text{Fines content (\%)}\\
D_{50} &= \text{Diameter at 50\% finer (mm)}\\
H &= \text{Thickness (m)}\\
S &= \text{Ground slope (\%)}\\
H &= \text{Free face height (m)}\\
L &= \text{Free face length (m)}\\
LD_{scalar} &= \text{Lateral spread displacement as scalar}
\end{align*}
$$

#### `get_lateral_spread_displacement_inc__zhang2004estimating`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_lateral\_spread\_displacement\_inc\_\_zhang2004estimating}(\mathrm{site\_ground\_condition}, LDI_i, S, H, L) \\ \hspace{1em} \mathrm{site\_ground\_condition} \gets \mathrm{site\_ground\_condition}.\mathrm{item} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} LD_{ratio} \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{site\_ground\_condition} = \textrm{"level\_ground"} \\ \hspace{2em} LD_{ratio} \gets \mathrm{np}.\mathrm{zeros\_like} \mathopen{}\left( LDI_i \mathclose{}\right) \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{site\_ground\_condition} = \textrm{"sloping\_ground"} \\ \hspace{3em} \mathbf{if} \ \lnot \mathopen{}\left( 0.2 < S < 3.5 \mathclose{}\right) \\ \hspace{4em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"ground\_slope must be between 0.2 to 3.5 \%"} \mathclose{}\right) \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{3em} LD_{ratio} \gets S + 0.2 \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ \mathrm{site\_ground\_condition} = \textrm{"free\_face"} \\ \hspace{4em} \mathbf{if} \ \lnot \mathopen{}\left( 4 < \frac{L}{H} < 40 \mathclose{}\right) \\ \hspace{5em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"free\_face\_height / free\_face\_length must be between 4 to 40"} \mathclose{}\right) \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{4em} LD_{ratio} \gets 6 \mathopen{}\left( \frac{L}{H} \mathclose{}\right)^{-0.8} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} LD_i \gets LDI_i \cdot LD_{ratio} \\ \hspace{1em} \mathbf{return} \ LD_i \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
LD_i &= \text{Lateral spread displacement inc. (m)}\\
\text{site\_ground\_condition} &= \text{Site ground condition}\\
LDI_i &= \text{Lateral displacement index inc. (m)}\\
S &= \text{Ground slope (\%)}\\
H &= \text{Free face height (m)}\\
L &= \text{Free face length (m)}
\end{align*}
$$

#### `get_lateral_spread_displacement_sum`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_lateral\_spread\_displacement\_sum}(LD_i) \\ \hspace{1em} ΣLD \gets \sum LD_i \\ \hspace{1em} \mathbf{return} \ ΣLD \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ΣLD &= \text{Lateral spread displacement sum (m)}\\
LD_i &= \text{Lateral spread displacement inc. (m)}
\end{align*}
$$

#### `get_liquefaction_building_settlement_index__bray2017simplified`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_building\_settlement\_index\_\_bray2017simplified}(D_f, γ_{max}, z, H) \\ \hspace{1em} z_{middle} \gets \mathrm{get\_depth\_middle} \mathopen{}\left( z, H \mathclose{}\right) \\ \hspace{1em} W \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( z < D_f, 0, 1 \mathclose{}\right) \\ \hspace{1em} LBS \gets \sum \mathopen{}\left( W \frac{γ_{max}}{z_{middle}} \cdot H \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ LBS \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
LBS &= \text{Liquefaction building settlement index}\\
D_f &= \text{Footing embedment (m)}\\
γ_{max} &= \text{Max. shear strain (\%)}\\
z &= \text{Depth (m)}\\
H &= \text{Thickness (m)}
\end{align*}
$$

#### `get_liquefaction_potential_index`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_potential\_index}(LPI_i) \\ \hspace{1em} LPI \gets \mathrm{reverse\_cumsum} \mathopen{}\left( LPI_i \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ LPI \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
LPI &= \text{Liquefaction potential index}\\
LPI_i &= \text{Liquefaction potential index inc.}
\end{align*}
$$

#### `get_liquefaction_potential_index_inc`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_potential\_index\_inc}(FS_{liq}, z, H, ΣLPI_{method}, H_1) \\ \hspace{1em} LPI_i \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ ΣLPI_{method} = \textrm{"iwasaki1978"} \\ \hspace{2em} LPI_i \gets \mathrm{get\_liquefaction\_potential\_index\_inc\_\_iwasaki1978practical} \mathopen{}\left( FS_{liq}, z, H \mathclose{}\right) \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ ΣLPI_{method} = \textrm{"maurer2015"} \\ \hspace{3em} LPI_i \gets \mathrm{get\_liquefaction\_potential\_index\_inc\_\_maurer2015moving} \mathopen{}\left( FS_{liq}, z, H, H_1 \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ LPI_i \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
LPI_i &= \text{Liquefaction potential index inc.}\\
FS_{liq} &= \text{Liquefaction safety factor}\\
z &= \text{Depth (m)}\\
H &= \text{Thickness (m)}\\
ΣLPI_{method} &= \text{Liquefaction potential index method}\\
H_1 &= \text{Thickness of non liquefiable layer (m)}
\end{align*}
$$

#### `get_liquefaction_potential_index_inc__iwasaki1978practical`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_potential\_index\_inc\_\_iwasaki1978practical}(FS_{liq}, z, H) \\ \hspace{1em} LPI_i \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( FS_{liq} \le 1, 1 - FS_{liq}, 0 \mathclose{}\right) \cdot \mathrm{np}.\mathrm{where} \mathopen{}\left( z \le 20, 10 - 0.5 z, 0 \mathclose{}\right) H \\ \hspace{1em} LPI_i \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( LPI_i \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ LPI_i \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
LPI_i &= \text{Liquefaction potential index inc.}\\
FS_{liq} &= \text{Liquefaction safety factor}\\
z &= \text{Depth (m)}\\
H &= \text{Thickness (m)}
\end{align*}
$$

#### `get_liquefaction_potential_index_inc__maurer2015moving`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_potential\_index\_inc\_\_maurer2015moving}(FS_{liq}, z, H, H_1) \\ \hspace{1em} \mathrm{m\_i} \gets \exp \mathopen{}\left( \frac{5}{25.56 \mathopen{}\left( 1 - FS_{liq} \mathclose{}\right)} \mathclose{}\right) - 1 \\ \hspace{1em} H_1 \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( H_1, 0.4, \mathrm{None} \mathclose{}\right) \\ \hspace{1em} LPI_i \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( \mathopen{}\left( FS_{liq} \le 1 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( H_1 \cdot \mathrm{m\_i} \le 3 \mathclose{}\right), 1 - FS_{liq}, 0 \mathclose{}\right) \cdot \mathrm{np}.\mathrm{where} \mathopen{}\left( z \le 20, \frac{25.56}{z}, 0 \mathclose{}\right) H \\ \hspace{1em} LPI_i \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( LPI_i \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ LPI_i \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
LPI_i &= \text{Liquefaction potential index inc.}\\
FS_{liq} &= \text{Liquefaction safety factor}\\
z &= \text{Depth (m)}\\
H &= \text{Thickness (m)}\\
H_1 &= \text{Thickness of non liquefiable layer (m)}
\end{align*}
$$

#### `get_liquefaction_potential_index_sum`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_potential\_index\_sum}(LPI_i) \\ \hspace{1em} ΣLPI \gets \sum LPI_i \\ \hspace{1em} \mathbf{return} \ ΣLPI \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ΣLPI &= \text{Liquefaction potential index sum}\\
LPI_i &= \text{Liquefaction potential index inc.}
\end{align*}
$$

#### `get_liquefaction_potential_index_sum_label`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_potential\_index\_sum\_label}(ΣLPI) \\ \hspace{1em} ΣLPI_{label} \gets \mathrm{PARAMETERS}_{\textrm{"liquefaction\_potential\_index\_sum"}}.\mathrm{data\_bins}_{\textrm{"liquefaction\_potential\_index\_sum\_label"}}.\mathrm{bin\_data} \mathopen{}\left( ΣLPI \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ ΣLPI_{label} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ΣLPI_{label} &= \text{Liquefaction potential index sum label}\\
ΣLPI &= \text{Liquefaction potential index sum}
\end{align*}
$$

#### `get_liquefaction_probability__boulanger2014cpt`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_probability\_\_boulanger2014cpt}(FS_{liq}) \\ \hspace{1em} PL_{liq} \gets 100 \mathopen{}\left( 1 - \mathrm{norm} \mathopen{}\left( \mathclose{}\right).\mathrm{cdf} \mathopen{}\left( \frac{0.2 + \log FS_{liq}}{0.2} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} PL_{liq} \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( PL_{liq} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( PL_{liq}, FS_{liq} \ge 2, 0 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ PL_{liq} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
PL_{liq} &= \text{Liquefaction probability (\%)}\\
FS_{liq} &= \text{Liquefaction safety factor}
\end{align*}
$$

#### `get_liquefaction_probability__cetin2004standard`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_probability\_\_cetin2004standard}(N_{160}, σ_v', FC, M_w, CSR, \mathrm{is\_potentially\_liquefiable}) \\ \hspace{1em} \mathopen{}\left( \mathrm{theta1}, \mathrm{theta2}, \mathrm{theta3}, \mathrm{theta4}, \mathrm{theta5}, \mathrm{theta6}, \mathrm{sigma\_epsilon} \mathclose{}\right) \gets \mathrm{DataMaps}.\mathrm{ModelCoefficientsCetin2004}.\mathrm{data\_values} \\ \hspace{1em} FC \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( FC, 5, 35 \mathclose{}\right) \\ \hspace{1em} PL_{liq} \gets 100 \mathrm{norm} \mathopen{}\left( \mathclose{}\right).\mathrm{cdf} \mathopen{}\left( \frac{-\mathopen{}\left( N_{160} \cdot \mathopen{}\left( 1 + \mathrm{theta1} \cdot FC \mathclose{}\right) - \mathrm{theta6} \cdot \log CSR - \mathrm{theta2} \cdot \log M_w - \mathrm{theta3} \cdot \log \mathopen{}\left( \frac{σ_v'}{101.325} \mathclose{}\right) + \mathrm{theta4} \cdot FC + \mathrm{theta5} \mathclose{}\right)}{\mathrm{sigma\_epsilon}} \mathclose{}\right) \\ \hspace{1em} PL_{liq} \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( \mathrm{np}.\mathrm{isnan} \mathopen{}\left( PL_{liq} \mathclose{}\right) \mathbin{|} \mathord{\sim} \mathrm{is\_potentially\_liquefiable}, 0, PL_{liq} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ PL_{liq} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
PL_{liq} &= \text{Liquefaction probability (\%)}\\
N_{160} &= \text{Normalized blow count}\\
σ_v' &= \text{Effective stress (kPa)}\\
FC &= \text{Fines content (\%)}\\
M_w &= \text{Moment magnitude}\\
CSR &= \text{Cyclic stress ratio}\\
\text{is\_potentially\_liquefiable} &= \text{Is potentially liquefiable}
\end{align*}
$$

#### `get_liquefaction_probability__cetin2018use`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_probability\_\_cetin2018use}(N_{160}, σ_v', FC, M_w, CSR, \mathrm{is\_potentially\_liquefiable}) \\ \hspace{1em} \mathopen{}\left( \mathrm{theta1}, \mathrm{theta2}, \mathrm{theta3}, \mathrm{theta4}, \mathrm{theta5}, \mathrm{theta6}, \mathrm{sigma\_epsilon} \mathclose{}\right) \gets \mathrm{DataMaps}.\mathrm{ModelCoefficientsCetin2018}.\mathrm{data\_values} \\ \hspace{1em} FC \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( FC, 5, 35 \mathclose{}\right) \\ \hspace{1em} PL_{liq} \gets 100 \mathrm{norm} \mathopen{}\left( \mathclose{}\right).\mathrm{cdf} \mathopen{}\left( \frac{-\mathopen{}\left( N_{160} \cdot \mathopen{}\left( 1 + \mathrm{theta1} \cdot FC \mathclose{}\right) - \mathrm{theta6} \cdot \log CSR - \mathrm{theta2} \cdot \log M_w - \mathrm{theta3} \cdot \log \mathopen{}\left( \frac{σ_v'}{101.325} \mathclose{}\right) + \mathrm{theta4} \cdot FC + \mathrm{theta5} \mathclose{}\right)}{\mathrm{sigma\_epsilon}} \mathclose{}\right) \\ \hspace{1em} PL_{liq} \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( \mathrm{np}.\mathrm{isnan} \mathopen{}\left( PL_{liq} \mathclose{}\right) \mathbin{|} \mathord{\sim} \mathrm{is\_potentially\_liquefiable}, 0, PL_{liq} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ PL_{liq} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
PL_{liq} &= \text{Liquefaction probability (\%)}\\
N_{160} &= \text{Normalized blow count}\\
σ_v' &= \text{Effective stress (kPa)}\\
FC &= \text{Fines content (\%)}\\
M_w &= \text{Moment magnitude}\\
CSR &= \text{Cyclic stress ratio}\\
\text{is\_potentially\_liquefiable} &= \text{Is potentially liquefiable}
\end{align*}
$$

#### `get_liquefaction_probability__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_probability\_\_idriss2008soil}(FS_{liq}) \\ \hspace{1em} PL_{liq} \gets 100 \mathopen{}\left( 1 - \mathrm{norm} \mathopen{}\left( \mathclose{}\right).\mathrm{cdf} \mathopen{}\left( \frac{0 + \log FS_{liq}}{0.13} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} PL_{liq} \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( PL_{liq} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( PL_{liq}, FS_{liq} \ge 2, 0 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ PL_{liq} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
PL_{liq} &= \text{Liquefaction probability (\%)}\\
FS_{liq} &= \text{Liquefaction safety factor}
\end{align*}
$$

#### `get_liquefaction_probability__ku2012probabilistic`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_probability\_\_ku2012probabilistic}(FS_{liq}) \\ \hspace{1em} PL_{liq} \gets 100 \mathopen{}\left( 1 - \mathrm{norm} \mathopen{}\left( \mathclose{}\right).\mathrm{cdf} \mathopen{}\left( \frac{0.102 + \log FS_{liq}}{0.276} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ PL_{liq} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
PL_{liq} &= \text{Liquefaction probability (\%)}\\
FS_{liq} &= \text{Liquefaction safety factor}
\end{align*}
$$

#### `get_liquefaction_safety_factor`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_safety\_factor}(CRR, CSR) \\ \hspace{1em} FS_{liq} \gets \frac{CRR}{CSR} \\ \hspace{1em} FS_{liq} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( FS_{liq}, \mathrm{None}, 2 \mathclose{}\right) \\ \hspace{1em} FS_{liq} \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( FS_{liq} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ FS_{liq} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
FS_{liq} &= \text{Liquefaction safety factor}\\
CRR &= \text{Cyclic resistance ratio}\\
CSR &= \text{Cyclic stress ratio}
\end{align*}
$$

#### `get_liquefaction_settlement`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_settlement}(S_{v-1D\ i}) \\ \hspace{1em} S_{v-1D} \gets \mathrm{reverse\_cumsum} \mathopen{}\left( S_{v-1D\ i} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ S_{v-1D} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_{v-1D} &= \text{Liquefaction settlement (m)}\\
S_{v-1D\ i} &= \text{Liquefaction settlement inc. (m)}
\end{align*}
$$

#### `get_liquefaction_settlement_inc`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_settlement\_inc}(ε_v, H) \\ \hspace{1em} S_{v-1D\ i} \gets \frac{ε_v}{100} \cdot H \\ \hspace{1em} \mathbf{return} \ S_{v-1D\ i} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_{v-1D\ i} &= \text{Liquefaction settlement inc. (m)}\\
ε_v &= \text{Volumetric strain (\%)}\\
H &= \text{Thickness (m)}
\end{align*}
$$

#### `get_liquefaction_settlement_sum`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_settlement\_sum}(S_{v-1D\ i}) \\ \hspace{1em} ΣS_{v-1D} \gets \sum S_{v-1D\ i} \\ \hspace{1em} \mathbf{return} \ ΣS_{v-1D} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ΣS_{v-1D} &= \text{Liquefaction settlement sum (m)}\\
S_{v-1D\ i} &= \text{Liquefaction settlement inc. (m)}
\end{align*}
$$

#### `get_liquefaction_severity_number`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_severity\_number}(LSN_i) \\ \hspace{1em} LSN \gets \mathrm{reverse\_cumsum} \mathopen{}\left( LSN_i \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ LSN \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
LSN &= \text{Liquefaction severity number}\\
LSN_i &= \text{Liquefaction severity number inc.}
\end{align*}
$$

#### `get_liquefaction_severity_number_inc__van2014assessment`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_severity\_number\_inc\_\_van2014assessment}(ε_v, z, H, LSN_{max\ z}) \\ \hspace{1em} LSN_{max\ z} \gets LSN_{max\ z}.\mathrm{item} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} LSN_i \gets 1000 \frac{\frac{ε_v}{100}}{z} \cdot H \\ \hspace{1em} LSN_i \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( LSN_i \mathclose{}\right) \\ \hspace{1em} \mathrm{flag} \gets z > LSN_{max\ z} \\ \hspace{1em} \mathrm{flag} \gets \mathrm{np}.\mathrm{broadcast\_to} \mathopen{}\left( \mathrm{flag}, LSN_i.\mathrm{shape} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( LSN_i, \mathrm{flag}, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} LSN_i \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( LSN_i \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ LSN_i \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
LSN_i &= \text{Liquefaction severity number inc.}\\
ε_v &= \text{Volumetric strain (\%)}\\
z &= \text{Depth (m)}\\
H &= \text{Thickness (m)}\\
LSN_{max\ z} &= \text{Liquefaction severity number max. depth (m)}
\end{align*}
$$

#### `get_liquefaction_severity_number_sum`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_severity\_number\_sum}(LSN_i) \\ \hspace{1em} ΣLSN \gets \sum LSN_i \\ \hspace{1em} \mathbf{return} \ ΣLSN \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ΣLSN &= \text{Liquefaction severity number sum}\\
LSN_i &= \text{Liquefaction severity number inc.}
\end{align*}
$$

#### `get_liquefaction_severity_number_sum_label`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_severity\_number\_sum\_label}(ΣLSN) \\ \hspace{1em} ΣLSN_{label} \gets \mathrm{PARAMETERS}_{\textrm{"liquefaction\_severity\_number\_sum"}}.\mathrm{data\_bins}_{\textrm{"liquefaction\_severity\_number\_sum\_label"}}.\mathrm{bin\_data} \mathopen{}\left( ΣLSN \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ ΣLSN_{label} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ΣLSN_{label} &= \text{Liquefaction severity number sum label}\\
ΣLSN &= \text{Liquefaction severity number sum}
\end{align*}
$$

#### `get_liquefaction_shear_induced_building_settlement__bray2017simplified`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_shear\_induced\_building\_settlement\_\_bray2017simplified}(B, H_2, LBS, CAV_{STD}, Sa_1, Q) \\ \hspace{1em} \epsilon \gets 0 \\ \hspace{1em} \mathbf{if} \ LBS \le 16 \\ \hspace{2em} \mathrm{c1} \gets -8.35 \\ \hspace{2em} \mathrm{c2} \gets 0.072 \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathrm{c1} \gets -7.48 \\ \hspace{2em} \mathrm{c2} \gets 0.014 \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} D_s \gets \exp \mathopen{}\left( \mathrm{c1} + 4.59 \log Q - 0.42 \mathopen{}\left( \log Q \mathclose{}\right)^{2} + \mathrm{c2} \cdot LBS + 0.58 \log \tanh \mathopen{}\left( \frac{H_2}{6} \mathclose{}\right) - 0.02 B + 0.84 \log CAV_{STD} + 0.41 \log Sa_1 + \epsilon \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ D_s \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
D_s &= \text{Liquefaction shear-induced settlement (mm)}\\
B &= \text{Footing width (m)}\\
H_2 &= \text{Thickness of liquefiable layer (m)}\\
LBS &= \text{Liquefaction building settlement index}\\
CAV_{STD} &= \text{Standardized cumulative absolute velocity (g-sec)}\\
Sa_1 &= \text{Spectral acceleration at 1 sec. (g)}\\
Q &= \text{Foundation contact pressure (kPa)}
\end{align*}
$$

#### `get_liquefaction_susceptibility__bray2006assessment`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquefaction\_susceptibility\_\_bray2006assessment}(w_c\ /\ LL, PI) \\ \hspace{1em} \mathrm{liquefaction\_susceptibility} \gets \mathrm{LiquefactionSusceptibilityFigure}.\mathrm{assign\_polygons\_labels\_from\_xy\_data} \mathopen{}\left( w_c\ /\ LL, PI \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{liquefaction\_susceptibility} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{liquefaction\_susceptibility} &= \text{Liquefaction susceptibility}\\
w_c\ /\ LL &= \text{Water content to liquid limit ratio}\\
PI &= \text{Plasticity index (\%)}
\end{align*}
$$

#### `get_magnitude_scaling_factor__boulanger2014cpt`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_magnitude\_scaling\_factor\_\_boulanger2014cpt}(M_w, MSF_{max}) \\ \hspace{1em} MSF \gets 1 + \mathopen{}\left( MSF_{max} - 1 \mathclose{}\right) \mathopen{}\left( 8.64 \exp \mathopen{}\left( \frac{-M_w}{4} \mathclose{}\right) - 1.325 \mathclose{}\right) \\ \hspace{1em} MSF \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( MSF, \mathrm{None}, MSF_{max} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ MSF \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
MSF &= \text{Magnitude scaling factor}\\
M_w &= \text{Moment magnitude}\\
MSF_{max} &= \text{Magnitude scaling factor max.}
\end{align*}
$$

#### `get_magnitude_scaling_factor__cetin2018use`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_magnitude\_scaling\_factor\_\_cetin2018use}(M_w) \\ \hspace{1em} \mathrm{cetineayy\_coeffs} \gets \mathrm{DataMaps}.\mathrm{ModelCoefficientsCetin2018}.\mathrm{data} \\ \hspace{1em} \mathopen{}\left( \mathrm{theta2}, \mathrm{theta6} \mathclose{}\right) \gets \mathopen{}\left( \mathrm{cetineayy\_coeffs}_{\textrm{"2"}}, \mathrm{cetineayy\_coeffs}_{\textrm{"6"}} \mathclose{}\right) \\ \hspace{1em} M_w \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( M_w, 5.5, 8.4 \mathclose{}\right) \\ \hspace{1em} MSF \gets \mathopen{}\left( \frac{M_w}{7.5} \mathclose{}\right)^{\frac{-\mathrm{theta2}}{\mathrm{theta6}}} \\ \hspace{1em} \mathbf{return} \ MSF \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
MSF &= \text{Magnitude scaling factor}\\
M_w &= \text{Moment magnitude}
\end{align*}
$$

#### `get_magnitude_scaling_factor__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_magnitude\_scaling\_factor\_\_idriss2008soil}(M_w) \\ \hspace{1em} MSF \gets 6.9 \exp \mathopen{}\left( \frac{-M_w}{4} \mathclose{}\right) - 0.058 \\ \hspace{1em} MSF \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( MSF, \mathrm{None}, 1.8 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ MSF \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
MSF &= \text{Magnitude scaling factor}\\
M_w &= \text{Moment magnitude}
\end{align*}
$$

#### `get_magnitude_scaling_factor__youd2001liquefaction`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_magnitude\_scaling\_factor\_\_youd2001liquefaction}(M_w) \\ \hspace{1em} MSF \gets \frac{10^{2.24}}{M_w^{2.56}} \\ \hspace{1em} \mathbf{return} \ MSF \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
MSF &= \text{Magnitude scaling factor}\\
M_w &= \text{Moment magnitude}
\end{align*}
$$

#### `get_magnitude_scaling_factor_max_spt__boulanger2014cpt`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_magnitude\_scaling\_factor\_max\_spt\_\_boulanger2014cpt}(N_{160cs}) \\ \hspace{1em} MSF_{max} \gets 1.09 + \mathopen{}\left( \frac{N_{160cs}}{31.5} \mathclose{}\right)^{2} \\ \hspace{1em} MSF_{max} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( MSF_{max}, \mathrm{None}, 2.2 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ MSF_{max} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
MSF_{max} &= \text{Magnitude scaling factor max.}\\
N_{160cs} &= \text{Clean sand normalized blow count}
\end{align*}
$$

#### `get_max_shear_strain__cetin2009probabilistica`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_max\_shear\_strain\_\_cetin2009probabilistica}(N_{160cs}, FS_{liq}, CSR_{SS,20,1D,1atm}) \\ \hspace{1em} CSR_{SS,20,1D,1atm} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( CSR_{SS,20,1D,1atm}, 0.05, 0.6 \mathclose{}\right) \\ \hspace{1em} N_{160cs} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( N_{160cs}, 5, 40 \mathclose{}\right) \\ \hspace{1em} γ_{max} \gets \frac{-0.025 N_{160cs} + \log CSR_{SS,20,1D,1atm} + 2.613}{0.004 N_{160cs} + 0.001} \\ \hspace{1em} γ_{max} \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( \mathrm{np}.\mathrm{isnan} \mathopen{}\left( γ_{max} \mathclose{}\right) \mathbin{|} \mathopen{}\left( FS_{liq} \ge 2 \mathclose{}\right), 0, \mathrm{np}.\mathrm{clip} \mathopen{}\left( γ_{max}, 0, 100 \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ γ_{max} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
γ_{max} &= \text{Max. shear strain (\%)}\\
N_{160cs} &= \text{Clean sand normalized blow count}\\
FS_{liq} &= \text{Liquefaction safety factor}\\
CSR_{SS,20,1D,1atm} &= \text{Cyclic stress ratio SS,20,1D,1atm}
\end{align*}
$$

#### `get_max_shear_strain__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_max\_shear\_strain\_\_idriss2008soil}(FS_{liq}, F_α, γ_{lim}) \\ \hspace{1em} γ_{max} \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( FS_{liq}, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( γ_{max}, FS_{liq} \ge 2, 0 \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( γ_{max}, \mathopen{}\left( FS_{liq} > F_α \mathclose{}\right) \mathbin{\&} \mathopen{}\left( FS_{liq} < 2 \mathclose{}\right), \mathrm{np}.\mathrm{clip} \mathopen{}\left( \frac{100 \cdot 0.035 \mathopen{}\left( 1 - F_α \mathclose{}\right) \mathopen{}\left( 2 - FS_{liq} \mathclose{}\right)}{FS_{liq} - F_α}, \mathrm{None}, γ_{lim} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( γ_{max}, FS_{liq} \le F_α, γ_{lim} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ γ_{max} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
γ_{max} &= \text{Max. shear strain (\%)}\\
FS_{liq} &= \text{Liquefaction safety factor}\\
F_α &= \text{Max. shear strain Fα term}\\
γ_{lim} &= \text{Shear strain limit (\%)}
\end{align*}
$$

#### `get_max_shear_strain_f_alpha_term_spt__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_max\_shear\_strain\_f\_alpha\_term\_spt\_\_idriss2008soil}(N_{160cs}) \\ \hspace{1em} N_{160cs} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( N_{160cs}, 7, \mathrm{None} \mathclose{}\right) \\ \hspace{1em} F_α \gets 0.032 + 0.69 \sqrt{ N_{160cs} } - 0.13 N_{160cs} \\ \hspace{1em} F_α \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( F_α \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ F_α \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
F_α &= \text{Max. shear strain Fα term}\\
N_{160cs} &= \text{Clean sand normalized blow count}
\end{align*}
$$

#### `get_membrane_compliance_correction__cetin2009probabilistica`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_membrane\_compliance\_correction\_\_cetin2009probabilistica}(N_{160}, D_r) \\ \hspace{1em} K_{mc} \gets -3e-05 D_r^{2} + 0.0048 D_r + 0.7222 \\ \hspace{1em} \mathbf{return} \ K_{mc} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K_{mc} &= \text{Membrane compliance correction}\\
N_{160} &= \text{Normalized blow count}\\
D_r &= \text{Relative density (\%)}
\end{align*}
$$

#### `get_overburden_correction_coefficient_spt__idriss2006semi`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overburden\_correction\_coefficient\_spt\_\_idriss2006semi}(N_{160}) \\ \hspace{1em} N_{160} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( N_{160}, \mathrm{None}, 37 \mathclose{}\right) \\ \hspace{1em} C_σ \gets \frac{1}{18.9 - 2.55 \sqrt{ N_{160} }} \\ \hspace{1em} \mathbf{return} \ C_σ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_σ &= \text{Overburden correction coefficient}\\
N_{160} &= \text{Normalized blow count}
\end{align*}
$$

#### `get_overburden_correction_coefficient_spt__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overburden\_correction\_coefficient\_spt\_\_idriss2008soil}(N_{160cs}) \\ \hspace{1em} \mathbf{return} \ \mathrm{get\_overburden\_correction\_coefficient\_spt\_\_idriss2006semi} \mathopen{}\left( N_{160cs} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_σ &= \text{Overburden correction coefficient}\\
N_{160cs} &= \text{Clean sand normalized blow count}
\end{align*}
$$

#### `get_overburden_correction_crr__cetin2018use`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overburden\_correction\_crr\_\_cetin2018use}(σ_v') \\ \hspace{1em} \mathrm{cetineayy\_coeffs} \gets \mathrm{DataMaps}.\mathrm{ModelCoefficientsCetin2018}.\mathrm{data} \\ \hspace{1em} \mathopen{}\left( \mathrm{theta3}, \mathrm{theta6} \mathclose{}\right) \gets \mathopen{}\left( \mathrm{cetineayy\_coeffs}_{\textrm{"3"}}, \mathrm{cetineayy\_coeffs}_{\textrm{"6"}} \mathclose{}\right) \\ \hspace{1em} K_σ \gets \mathopen{}\left( \frac{σ_v'}{101.325} \mathclose{}\right)^{\frac{-\mathrm{theta3}}{\mathrm{theta6}}} \\ \hspace{1em} K_σ \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( K_σ, 0.8, 1.6 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ K_σ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K_σ &= \text{Overburden correction for CRR}\\
σ_v' &= \text{Effective stress (kPa)}
\end{align*}
$$

#### `get_overburden_correction_crr__hynes2018influence`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overburden\_correction\_crr\_\_hynes2018influence}(σ_v') \\ \hspace{1em} f \gets 0.8 \\ \hspace{1em} K_σ \gets \mathopen{}\left( \frac{σ_v'}{101.325} \mathclose{}\right)^{f - 1} \\ \hspace{1em} K_σ \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( K_σ, 0, 1 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ K_σ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K_σ &= \text{Overburden correction for CRR}\\
σ_v' &= \text{Effective stress (kPa)}
\end{align*}
$$

#### `get_overburden_correction_crr__idriss2006semi`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overburden\_correction\_crr\_\_idriss2006semi}(C_σ, σ_v') \\ \hspace{1em} K_σ \gets 1 - C_σ \cdot \log \mathopen{}\left( \frac{σ_v'}{101.325} \mathclose{}\right) \\ \hspace{1em} K_σ \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( K_σ, \mathrm{None}, 1.1 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ K_σ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K_σ &= \text{Overburden correction for CRR}\\
C_σ &= \text{Overburden correction coefficient}\\
σ_v' &= \text{Effective stress (kPa)}
\end{align*}
$$

#### `get_overburden_correction_crr__youd2001liquefaction`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overburden\_correction\_crr\_\_youd2001liquefaction}(D_r, σ_v') \\ \hspace{1em} K_σ \gets \mathopen{}\left( \frac{σ_v'}{101.325} \mathclose{}\right)^{1 - 0.005 \frac{D_r}{100} - 1} \\ \hspace{1em} \mathbf{return} \ K_σ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K_σ &= \text{Overburden correction for CRR}\\
D_r &= \text{Relative density (\%)}\\
σ_v' &= \text{Effective stress (kPa)}
\end{align*}
$$

#### `get_post_liquefaction_residual_shear_strength`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_post\_liquefaction\_residual\_shear\_strength}(S_{r\ ratio}, σ_v', \mathrm{is\_fine\_soil}) \\ \hspace{1em} S_r \gets S_{r\ ratio} \cdot σ_v' \\ \hspace{1em} \mathbf{return} \ S_r \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_r &= \text{Post-liquefaction residual shear strength (kPa)}\\
S_{r\ ratio} &= \text{Normalized residual shear strength}\\
σ_v' &= \text{Effective stress (kPa)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_shear_strain_limit_spt__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shear\_strain\_limit\_spt\_\_idriss2008soil}(N_{160cs}) \\ \hspace{1em} γ_{lim} \gets 100 \cdot 1.859 \mathopen{}\left( 1.1 - \sqrt{ \frac{N_{160cs}}{46} } \mathclose{}\right)^{3} \\ \hspace{1em} γ_{lim} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( γ_{lim}, 0, 50 \mathclose{}\right) \\ \hspace{1em} γ_{lim} \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( γ_{lim} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ γ_{lim} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
γ_{lim} &= \text{Shear strain limit (\%)}\\
N_{160cs} &= \text{Clean sand normalized blow count}
\end{align*}
$$

#### `get_shear_stress_reduction_coefficient__cetin2004standard`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shear\_stress\_reduction\_coefficient\_\_cetin2004standard}(z, M_w, PGA, V_{s12}) \\ \hspace{1em} r_d \gets \frac{1 + \frac{-23.013 - 2.949 PGA + 0.999 M_w + 0.0525 V_{s12}}{16.258 + 0.201 \exp \mathopen{}\left( 0.341 \mathopen{}\left( -z + 0.0785 V_{s12} + 7.586 \mathclose{}\right) \mathclose{}\right)}}{1 + \frac{-23.013 - 2.949 PGA + 0.999 M_w + 0.0525 V_{s12}}{16.258 + 0.201 \exp \mathopen{}\left( 0.341 \mathopen{}\left( 0.0785 V_{s12} + 7.586 \mathclose{}\right) \mathclose{}\right)}} - 0.0046 \mathopen{}\left( \mathrm{np}.\mathrm{clip} \mathopen{}\left( z, 20, \mathrm{None} \mathclose{}\right) - 20 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ r_d \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
r_d &= \text{Shear stress reduction coefﬁcient}\\
z &= \text{Depth (m)}\\
M_w &= \text{Moment magnitude}\\
PGA &= \text{Peak ground acceleration (g)}\\
V_{s12} &= \text{Average shear velocity 12 m (m/s)}
\end{align*}
$$

#### `get_shear_stress_reduction_coefficient__idriss2006semi`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shear\_stress\_reduction\_coefficient\_\_idriss2006semi}(z, M_w) \\ \hspace{1em} \alpha \gets -1.012 - 1.126 \sin \mathopen{}\left( \frac{z}{11.73} + 5.133 \mathclose{}\right) \\ \hspace{1em} \beta \gets 0.106 + 0.118 \sin \mathopen{}\left( \frac{z}{11.28} + 5.142 \mathclose{}\right) \\ \hspace{1em} r_d \gets \exp \mathopen{}\left( \alpha + M_w \cdot \beta \mathclose{}\right) \\ \hspace{1em} r_d \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( r_d, \mathrm{None}, 1 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ r_d \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
r_d &= \text{Shear stress reduction coefﬁcient}\\
z &= \text{Depth (m)}\\
M_w &= \text{Moment magnitude}
\end{align*}
$$

#### `get_shear_stress_reduction_coefficient__liao1986catalog`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shear\_stress\_reduction\_coefficient\_\_liao1986catalog}(z) \\ \hspace{1em} r_d \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( z, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( r_d, z \le 9.15, 1 - 0.00765 z \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( r_d, \mathopen{}\left( z > 9.15 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( z \le 23 \mathclose{}\right), 1.174 - 0.0267 z \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ r_d \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
r_d &= \text{Shear stress reduction coefﬁcient}\\
z &= \text{Depth (m)}
\end{align*}
$$

#### `get_shear_stress_reduction_coefficient__youd2001liquefaction`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shear\_stress\_reduction\_coefficient\_\_youd2001liquefaction}(z) \\ \hspace{1em} r_d \gets \frac{1 - 0.4113 z^{0.5} + 0.04052 z + 0.001753 z^{1.5}}{1 - 0.4177 z^{0.5} + 0.05729 z - 0.006205 z^{1.5} + 0.00121 z^{2}} \\ \hspace{1em} r_d \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( r_d, 0, 1 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ r_d \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
r_d &= \text{Shear stress reduction coefﬁcient}\\
z &= \text{Depth (m)}
\end{align*}
$$

#### `get_shear_stress_reduction_factor__baez1993advances`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shear\_stress\_reduction\_factor\_\_baez1993advances}(\mathrm{stone\_column\_arrangement}, A_r, G_r) \\ \hspace{1em} \mathbf{if} \ \mathrm{is\_null} \mathopen{}\left( \mathrm{stone\_column\_arrangement} \mathclose{}\right) \lor \mathrm{stone\_column\_arrangement} = \textrm{"none"} \\ \hspace{2em} \mathbf{return} \ \mathrm{None} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} K_G \gets \frac{1}{1 + A_r \cdot \mathopen{}\left( G_r - 1 \mathclose{}\right)} \\ \hspace{1em} \mathbf{return} \ K_G \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K_G &= \text{Shear stress reduction factor}\\
\text{stone\_column\_arrangement} &= \text{Stone column arrangement}\\
A_r &= \text{Area replacement ratio}\\
G_r &= \text{Shear modulus ratio}
\end{align*}
$$

#### `get_stone_column_is_present`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_stone\_column\_is\_present}(\mathrm{stone\_column\_arrangement}, z, z_{top}, z_{bottom}) \\ \hspace{1em} \mathbf{if} \ \mathrm{is\_null} \mathopen{}\left( \mathrm{stone\_column\_arrangement} \mathclose{}\right) \lor \mathrm{stone\_column\_arrangement} = \textrm{"none"} \\ \hspace{2em} \mathbf{return} \ \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( z, \mathrm{False} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( z \ge z_{top} \mathclose{}\right) \mathbin{\&} \mathopen{}\left( z \le z_{bottom} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
sc_{present} &= \text{Stone column is present}\\
\text{stone\_column\_arrangement} &= \text{Stone column arrangement}\\
z &= \text{Depth (m)}\\
z_{top} &= \text{Stone column top depth (m)}\\
z_{bottom} &= \text{Stone column bottom depth (m)}
\end{align*}
$$

#### `get_thickness_liquefiable_layer`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_thickness\_liquefiable\_layer}(FS_{liq}, H) \\ \hspace{1em} \textrm{" calculated as the total thickness of liquefiable sand layers "} \\ \hspace{1em} H \gets \mathrm{np}.\mathrm{broadcast\_to} \mathopen{}\left( H, FS_{liq}.\mathrm{shape} \mathclose{}\right) \\ \hspace{1em} H_2 \gets H.\mathrm{copy} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( H_2, \mathord{\sim} \mathopen{}\left( FS_{liq} \le 1 \mathclose{}\right), 0 \mathclose{}\right) \\ \hspace{1em} H_2 \gets \sum H_2 \\ \hspace{1em} \mathbf{return} \ H_2 \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
H_2 &= \text{Thickness of liquefiable layer (m)}\\
FS_{liq} &= \text{Liquefaction safety factor}\\
H &= \text{Thickness (m)}
\end{align*}
$$

#### `get_thickness_non_liquefiable_layer`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_thickness\_non\_liquefiable\_layer}(FS_{liq}, z) \\ \hspace{1em} \textrm{" calculated as the total thickness above the first liquefiable sand layer "} \\ \hspace{1em} H_1 \gets \mathopen{}\left[  \mathclose{}\right] \\ \hspace{1em} \mathbf{for} \ \mathrm{fs\_liq} \in \mathrm{np}.\mathrm{atleast\_2d} \mathopen{}\left( FS_{liq} \mathclose{}\right) \ \mathbf{do} \\ \hspace{2em} \mathrm{flag} \gets \mathrm{fs\_liq} \le 1 \\ \hspace{2em} \mathbf{if} \ \mathrm{np}.\mathrm{any} \mathopen{}\left( \mathrm{flag} \mathclose{}\right) \\ \hspace{3em} a \gets \mathrm{flag}.\mathrm{argmax} \mathopen{}\left( \mathclose{}\right) \\ \hspace{3em} \mathrm{z\_surface\_layer} \gets \left\{ \begin{array}{ll} \mathrm{depth}_{a - 1}, & \mathrm{if} \ a > 0 \\ 0, & \mathrm{otherwise} \end{array} \right. \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathrm{z\_surface\_layer} \gets \mathrm{np}.\mathrm{inf} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} H_1.\mathrm{append} \mathopen{}\left( \mathrm{z\_surface\_layer} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ for} \\ \hspace{1em} \mathbf{if} \ FS_{liq}.\mathrm{ndim} < 2 \\ \hspace{2em} H_1 \gets \mathrm{thickness\_non\_liquefiable\_layer}_{0} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ H_1 \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
H_1 &= \text{Thickness of non liquefiable layer (m)}\\
FS_{liq} &= \text{Liquefaction safety factor}\\
z &= \text{Depth (m)}
\end{align*}
$$

#### `get_triaxial_planes_correction`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_triaxial\_planes\_correction}() \\ \hspace{1em} K_r \gets 1 \\ \hspace{1em} \mathbf{return} \ K_r \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K_r &= \text{Triaxial planes correction}
\end{align*}
$$

#### `get_volumetric_strain__cetin2009probabilisticb`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_volumetric\_strain\_\_cetin2009probabilisticb}(N_{160cs}, DF, FS_{liq}, CSR_{SS,20,1D,1atm}) \\ \hspace{1em} CSR_{SS,20,1D,1atm} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( CSR_{SS,20,1D,1atm}, 0.05, 0.6 \mathclose{}\right) \\ \hspace{1em} N_{160cs} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( N_{160cs}, 5, 40 \mathclose{}\right) \\ \hspace{1em} ε_v \gets 1.879 \log \mathopen{}\left( \frac{780.416 \log CSR_{SS,20,1D,1atm} - N_{160cs} + 2442.465}{636.613 N_{160cs} + 306.732} \mathclose{}\right) + 5.583 \\ \hspace{1em} ε_v \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( FS_{liq} \ge 2, 0, ε_v \mathclose{}\right) \\ \hspace{1em} ε_v \gets ε_v \cdot DF \\ \hspace{1em} \mathrm{calibration\_coefficient} \gets 1.15 \\ \hspace{1em} ε_v \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( ε_v, 0, \mathrm{None} \mathclose{}\right) \\ \hspace{1em} ε_v \gets \mathrm{calibration\_coefficient} \cdot \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( ε_v \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ ε_v \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ε_v &= \text{Volumetric strain (\%)}\\
N_{160cs} &= \text{Clean sand normalized blow count}\\
DF &= \text{Volumetric strain depth weighting factor}\\
FS_{liq} &= \text{Liquefaction safety factor}\\
CSR_{SS,20,1D,1atm} &= \text{Cyclic stress ratio SS,20,1D,1atm}
\end{align*}
$$

#### `get_volumetric_strain_depth_weighting_factor__cetin2009probabilisticb`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_volumetric\_strain\_depth\_weighting\_factor\_\_cetin2009probabilisticb}(z) \\ \hspace{1em} DF \gets \mathopen{}\left| 1 - \frac{z}{18} \mathclose{}\right| \\ \hspace{1em} \mathbf{return} \ DF \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
DF &= \text{Volumetric strain depth weighting factor}\\
z &= \text{Depth (m)}
\end{align*}
$$

#### `get_volumetric_strain_spt__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_volumetric\_strain\_spt\_\_idriss2008soil}(γ_{max}, N_{160cs}) \\ \hspace{1em} γ_{max} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( γ_{max}, \mathrm{None}, 100 \cdot 0.08 \mathclose{}\right) \\ \hspace{1em} ε_v \gets 1.5 \exp \mathopen{}\left( -0.369 \sqrt{ N_{160cs} } \mathclose{}\right) γ_{max} \\ \hspace{1em} ε_v \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( ε_v \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ ε_v \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ε_v &= \text{Volumetric strain (\%)}\\
γ_{max} &= \text{Max. shear strain (\%)}\\
N_{160cs} &= \text{Clean sand normalized blow count}
\end{align*}
$$

#### `get_youd2002revised_t15_parameters`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_youd2002revised\_t15\_parameters}(T_{15\ flag}, FC, D_{50}, H, LD_{scalar}) \\ \hspace{1em} \mathbf{if} \ \mathrm{np}.\mathrm{any} \mathopen{}\left( \mathrm{is\_null} \mathopen{}\left( \mathrm{np}.\mathrm{extract} \mathopen{}\left( T_{15\ flag}, D_{50} \mathclose{}\right) \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"null diameter\_at\_50\_percent\_finer values at is\_t15\_liquefiable\_layers, check inputs"} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} T_{15} \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( T_{15\ flag}, H, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ LD_{scalar} \\ \hspace{2em} T_{15} \gets \mathrm{np}.\mathrm{nansum} \mathopen{}\left( T_{15} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} FC_{T15} \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( T_{15\ flag}, FC, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ LD_{scalar} \\ \hspace{2em} FC_{T15} \gets \mathrm{np}.\mathrm{nanmean} \mathopen{}\left( FC_{T15} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} D_{50T15} \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( T_{15\ flag}, D_{50}, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ LD_{scalar} \\ \hspace{2em} D_{50T15} \gets \mathrm{np}.\mathrm{nanmean} \mathopen{}\left( D_{50T15} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( T_{15}, FC_{T15}, D_{50T15} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
T_{15} &= \text{Cumulative thickness of liquefiable layers (m)}\\
FC_{T15} &= \text{Fines content of liquefiable layers (\%)}\\
D_{50T15} &= \text{Diameter at 50\% finer of liquefiable layers (mm)}\\
T_{15\ flag} &= \text{Is T15 liquefiable layers}\\
FC &= \text{Fines content (\%)}\\
D_{50} &= \text{Diameter at 50\% finer (mm)}\\
H &= \text{Thickness (m)}\\
LD_{scalar} &= \text{Lateral spread displacement as scalar}
\end{align*}
$$
