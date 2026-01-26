---
title: base.py
---

## Formulae

#### `get_below_water_table`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_below\_water\_table}(z, z_{w\ present}, z_w) \\ \hspace{1em} \mathrm{below\_water\_table} \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( z, \mathrm{False} \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ z_{w\ present} \\ \hspace{2em} \mathbf{if} \ \mathrm{is\_null} \mathopen{}\left( z_w \mathclose{}\right) \\ \hspace{3em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"water\_table missing"} \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( \mathrm{below\_water\_table}, z > z_w, \mathrm{True} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathrm{below\_water\_table} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{below\_water\_table} &= \text{Below water table}\\
z &= \text{Depth (m)}\\
z_{w\ present} &= \text{Water table present}\\
z_w &= \text{Water table (m)}
\end{align*}
$$

#### `get_coefficient_of_consolidation__terzaghi1925principles`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_coefficient\_of\_consolidation\_\_terzaghi1925principles}(k, M) \\ \hspace{1em} C_v \gets 31536000 \cdot \frac{1000 k \cdot M}{g} \\ \hspace{1em} \mathbf{return} \ C_v \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_v &= \text{Coefficient of consolidation (m2/year)}\\
k &= \text{Permeability (m/s)}\\
M &= \text{Constrained modulus (MPa)}
\end{align*}
$$

#### `get_coefficient_of_earth_pressure_at_rest__mayne1982ko`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_coefficient\_of\_earth\_pressure\_at\_rest\_\_mayne1982ko}(ϕ, ϕ', OCR, \mathrm{is\_fine\_soil}) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( ϕ, \mathrm{is\_fine\_soil}, ϕ' \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( OCR, \mathrm{is\_null} \mathopen{}\left( OCR \mathclose{}\right) \mathbin{\&} \mathord{\sim} \mathrm{is\_fine\_soil}, 1 \mathclose{}\right) \\ \hspace{1em} K_o \gets \mathopen{}\left( 1 - \mathrm{sindg} \mathopen{}\left( ϕ \mathclose{}\right) \mathclose{}\right) OCR^{\mathrm{sindg} \mathopen{}\left( ϕ \mathclose{}\right)} \\ \hspace{1em} K_o \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( K_o \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ K_o \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K_o &= \text{Coefficient of lateral earth pressure at rest}\\
ϕ &= \text{Friction angle (°)}\\
ϕ' &= \text{Peak friction angle (°)}\\
OCR &= \text{Overconsolidation ratio}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_consolidation_state`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_consolidation\_state}(OCR) \\ \hspace{1em} \mathrm{consolidation\_state} \gets \mathrm{PARAMETERS}_{\textrm{"overconsolidation\_ratio"}}.\mathrm{data\_bins}_{\textrm{"consolidation\_state"}}.\mathrm{bin\_data} \mathopen{}\left( OCR \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{consolidation\_state} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{consolidation\_state} &= \text{Consolidation state}\\
OCR &= \text{Overconsolidation ratio}
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

#### `get_effective_stress`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_effective\_stress}(σ_v, u_0) \\ \hspace{1em} σ_v' \gets σ_v - u_0 \\ \hspace{1em} \mathbf{return} \ σ_v' \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
σ_v' &= \text{Effective stress (kPa)}\\
σ_v &= \text{Total stress (kPa)}\\
u_0 &= \text{Pore water pressure (kPa)}
\end{align*}
$$

#### `get_elasticity_modulus_from_shear_modulus`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_elasticity\_modulus\_from\_shear\_modulus}(G_o, ν) \\ \hspace{1em} E_s \gets 2 G_o \cdot \mathopen{}\left( 1 + ν \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ E_s \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
E_s &= \text{Elasticity modulus (MPa)}\\
G_o &= \text{Small strain shear modulus (MPa)}\\
ν &= \text{Poisson’s ratio}
\end{align*}
$$

#### `get_elevation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_elevation}(z, \mathrm{surface\_elevation}) \\ \hspace{1em} \mathrm{elevation} \gets \mathrm{surface\_elevation} - z \\ \hspace{1em} \mathbf{return} \ \mathrm{elevation} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{elevation} &= \text{Elevation (m)}\\
z &= \text{Depth (m)}\\
\text{surface\_elevation} &= \text{Surface elevation (m)}
\end{align*}
$$

#### `get_overconsolidation_ratio__ladd1991stability`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overconsolidation\_ratio\_\_ladd1991stability}(S_u, σ_v', s, m, \mathrm{is\_fine\_soil}) \\ \hspace{1em} OCR \gets \mathopen{}\left( \frac{S_u}{σ_v' \cdot s} \mathclose{}\right)^{\frac{1}{m}} \\ \hspace{1em} \mathbf{return} \ OCR \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
OCR &= \text{Overconsolidation ratio}\\
S_u &= \text{Undrained shear strength (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
s &= \text{SHANSEP method s}\\
m &= \text{SHANSEP method m}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_pore_water_pressure`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pore\_water\_pressure}(z_{w\ present}, z_w, z) \\ \hspace{1em} \mathbf{if} \ z_{w\ present} \\ \hspace{2em} \mathbf{if} \ \mathrm{is\_null} \mathopen{}\left( z_w \mathclose{}\right) \\ \hspace{3em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"null water\_table"} \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{if} \ z_w < 0 \\ \hspace{3em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"negative water\_table not supported"} \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} u_0 \gets \mathopen{}\left( z - z_w \mathclose{}\right) γ_w \\ \hspace{2em} u_0 \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( u_0, 0, \mathrm{None} \mathclose{}\right) \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} u_0 \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( z, 0 \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ u_0 \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
u_0 &= \text{Pore water pressure (kPa)}\\
z_{w\ present} &= \text{Water table present}\\
z_w &= \text{Water table (m)}\\
z &= \text{Depth (m)}\\
γ_w &= \text{Water unit weight (kN/m3)}
\end{align*}
$$

#### `get_shear_strength__terzaghi1943theoretical`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shear\_strength\_\_terzaghi1943theoretical}(S_u, σ_v', ϕ) \\ \hspace{1em} τ \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( S_u \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ τ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
τ &= \text{Shear strength (kPa)}\\
S_u &= \text{Undrained shear strength (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
ϕ &= \text{Friction angle (°)}
\end{align*}
$$

#### `get_shear_velocity__landau1959theory`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shear\_velocity\_\_landau1959theory}(G_o, γ) \\ \hspace{1em} V_s \gets \mathopen{}\left( \frac{g \cdot 1000 G_o}{γ} \mathclose{}\right)^{0.5} \\ \hspace{1em} \mathbf{return} \ V_s \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
V_s &= \text{Shear velocity (m/s)}\\
G_o &= \text{Small strain shear modulus (MPa)}\\
γ &= \text{Unit weight (kN/m3)}
\end{align*}
$$

#### `get_small_strain_shear_modulus__landau1959theory`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_small\_strain\_shear\_modulus\_\_landau1959theory}(γ, V_s) \\ \hspace{1em} G_o \gets \frac{\frac{γ}{g} \cdot V_s^{2}}{1000} \\ \hspace{1em} \mathbf{return} \ G_o \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
G_o &= \text{Small strain shear modulus (MPa)}\\
γ &= \text{Unit weight (kN/m3)}\\
V_s &= \text{Shear velocity (m/s)}
\end{align*}
$$

#### `get_soil_type`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_type}(\mathrm{uscs\_symbol}) \\ \hspace{1em} \mathrm{soil\_type} \gets \mathrm{replace\_from\_mapping} \mathopen{}\left( \mathrm{uscs\_symbol}, \mathrm{DataMaps}.\mathrm{USCSSoilType}.\mathrm{data} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{soil\_type} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{soil\_type} &= \text{Soil type}\\
\text{uscs\_symbol} &= \text{USCS symbol}
\end{align*}
$$

#### `get_soil_type2`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_type2}(\mathrm{uscs\_symbol}) \\ \hspace{1em} \mathrm{soil\_type2} \gets \mathrm{replace\_from\_mapping} \mathopen{}\left( \mathrm{uscs\_symbol}, \mathrm{DataMaps}.\mathrm{USCSSoilType2}.\mathrm{data} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{soil\_type2} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{soil\_type2} &= \text{Soil type 2}\\
\text{uscs\_symbol} &= \text{USCS symbol}
\end{align*}
$$

#### `get_soil_type3`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_type3}(\mathrm{uscs\_symbol}) \\ \hspace{1em} \mathrm{soil\_type3} \gets \mathrm{replace\_from\_mapping} \mathopen{}\left( \mathrm{uscs\_symbol}, \mathrm{DataMaps}.\mathrm{USCSSoilType3}.\mathrm{data} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{soil\_type3} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{soil\_type3} &= \text{Soil type 3}\\
\text{uscs\_symbol} &= \text{USCS symbol}
\end{align*}
$$

#### `get_thickness`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_thickness}(z) \\ \hspace{1em} \mathbf{if} \ \mathrm{np}.\mathrm{ndim} \mathopen{}\left( z \mathclose{}\right) = 0 \\ \hspace{2em} H \gets z \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} H \gets \mathrm{np}.\mathrm{diff} \mathopen{}\left( \mathrm{np}.\mathrm{r\_}_{\mathopen{}\left( 0, z \mathclose{}\right)} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ H \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
H &= \text{Thickness (m)}\\
z &= \text{Depth (m)}
\end{align*}
$$

#### `get_total_stress`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_total\_stress}(γ, H) \\ \hspace{1em} \mathbf{if} \ \mathrm{np}.\mathrm{any} \mathopen{}\left( \mathrm{is\_null} \mathopen{}\left( γ \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathrm{warnings}.\mathrm{warn} \mathopen{}\left( \textrm{"total\_stress: null unit\_weight values found, will be replaced by \{\}"}.\mathrm{format} \mathopen{}\left( γ_{default} \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} γ \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( γ \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} σ_v \gets \mathrm{np}.\mathrm{cumsum} \mathopen{}\left( H \cdot γ \mathclose{}\right) + σ_{v\ inc} \\ \hspace{1em} \mathbf{if} \ \mathrm{np}.\mathrm{ndim} \mathopen{}\left( H \cdot γ \mathclose{}\right) = 0 \\ \hspace{2em} σ_v \gets σ_v.\mathrm{item} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ σ_v \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
σ_v &= \text{Total stress (kPa)}\\
γ &= \text{Unit weight (kN/m3)}\\
H &= \text{Thickness (m)}\\
γ_{default} &= \text{Default unit weight (kN/m3)}\\
σ_{v\ inc} &= \text{Total stress inc. (kPa)}
\end{align*}
$$

#### `get_undrained_shear_strength_ratio`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_undrained\_shear\_strength\_ratio}(S_u, σ_v') \\ \hspace{1em} S_{u\ ratio} \gets \frac{S_u}{σ_v'} \\ \hspace{1em} \mathbf{return} \ S_{u\ ratio} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_{u\ ratio} &= \text{Undrained shear strength ratio}\\
S_u &= \text{Undrained shear strength (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}
\end{align*}
$$
