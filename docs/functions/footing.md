---
title: footing.py
---

## Formulae

#### `get_average_friction_angle__bowles1996foundation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_average\_friction\_angle\_\_bowles1996foundation}(H, ϕ, H) \\ \hspace{1em} ϕ \gets \mathrm{np}.\mathrm{rad2deg} \mathopen{}\left( \arctan \mathopen{}\left( \frac{\mathrm{np}.\mathrm{dot} \mathopen{}\left( H, \mathrm{tandg} \mathopen{}\left( ϕ \mathclose{}\right) \mathclose{}\right)}{H} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ ϕ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ϕ &= \text{Friction angle (°)}\\
H &= \text{Thickness (m)}\\
H &= \text{Effective shear depth (m)}
\end{align*}
$$

#### `get_average_parameters__bowles1996foundation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_average\_parameters\_\_bowles1996foundation}(B, D_f, z, ϕ, S_u) \\ \hspace{1em} \mathrm{ignore\_flag} \gets z < D_f \\ \hspace{1em} z \gets \mathrm{np}.\mathrm{extract} \mathopen{}\left( \mathord{\sim} \mathrm{ignore\_flag}, z \mathclose{}\right) \\ \hspace{1em} ϕ \gets \mathrm{np}.\mathrm{extract} \mathopen{}\left( \mathord{\sim} \mathrm{ignore\_flag}, ϕ \mathclose{}\right) \\ \hspace{1em} S_u \gets \mathrm{np}.\mathrm{extract} \mathopen{}\left( \mathord{\sim} \mathrm{ignore\_flag}, S_u \mathclose{}\right) \\ \hspace{1em} ϕ \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( ϕ \mathclose{}\right) \\ \hspace{1em} S_u \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( S_u \mathclose{}\right) \\ \hspace{1em} \mathrm{depth\_from\_embedment} \gets z - D_f \\ \hspace{1em} \mathrm{average\_friction\_angle} \gets \mathrm{np}.\mathrm{take} \mathopen{}\left( ϕ, 0 \mathclose{}\right) \\ \hspace{1em} \mathrm{effective\_shear\_depth\_previous} \gets 0 \\ \hspace{1em} \mathbf{while} \ \mathrm{True} \\ \hspace{2em} H \gets \mathrm{get\_effective\_shear\_depth} \mathopen{}\left( B, \mathrm{average\_friction\_angle} \mathclose{}\right) \\ \hspace{2em} \mathrm{max\_depth\_from\_embedment} \gets \mathrm{np}.\mathrm{max} \mathopen{}\left( \mathrm{depth\_from\_embedment} \mathclose{}\right) \\ \hspace{2em} \mathbf{if} \ \mathrm{max\_depth\_from\_embedment} < H \\ \hspace{3em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"max\_depth\_from\_embedment=\{\} < effective\_shear\_depth=\{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{max\_depth\_from\_embedment}, H \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathrm{depth\_in\_range} \gets \mathrm{depth\_from\_embedment}_{\mathrm{depth\_from\_embedment} < H} \\ \hspace{2em} \mathrm{depth\_in\_range} \gets \mathrm{np}.\mathrm{append} \mathopen{}\left( \mathrm{depth\_in\_range}, H \mathclose{}\right) \\ \hspace{2em} \mathrm{indices} \gets \mathrm{np}.\mathrm{searchsorted} \mathopen{}\left( \mathrm{depth\_from\_embedment}, \mathrm{depth\_in\_range} \mathclose{}\right) \\ \hspace{2em} \mathrm{thickness\_from\_embedment} \gets \mathrm{get\_thickness} \mathopen{}\left( \mathrm{depth\_in\_range} \mathclose{}\right) \\ \hspace{2em} \mathrm{average\_friction\_angle} \gets \mathrm{get\_average\_friction\_angle\_\_bowles1996foundation} \mathopen{}\left( \mathrm{thickness\_from\_embedment}, \mathrm{friction\_angle}_{\mathrm{indices}}, H \mathclose{}\right) \\ \hspace{2em} S_{u30} \gets \mathrm{get\_average\_undrained\_shear\_strength\_\_bowles1996foundation} \mathopen{}\left( \mathrm{thickness\_from\_embedment}, \mathrm{undrained\_shear\_strength}_{\mathrm{indices}}, H \mathclose{}\right) \\ \hspace{2em} \mathbf{if} \ \mathopen{}\left| H - \mathrm{effective\_shear\_depth\_previous} \mathclose{}\right| < 0.0001 \\ \hspace{3em} \mathbf{break} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathrm{effective\_shear\_depth\_previous} \gets H \\ \hspace{1em} \mathbf{end \ while} \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( H, \mathrm{average\_friction\_angle}, S_{u30} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
H &= \text{Effective shear depth (m)}\\
ϕ &= \text{Friction angle (°)}\\
S_u &= \text{Undrained shear strength (kPa)}\\
B &= \text{Footing width (m)}\\
D_f &= \text{Footing embedment (m)}\\
z &= \text{Depth (m)}
\end{align*}
$$

#### `get_average_undrained_shear_strength__bowles1996foundation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_average\_undrained\_shear\_strength\_\_bowles1996foundation}(H, S_u, H) \\ \hspace{1em} S_u \gets \frac{\mathrm{np}.\mathrm{dot} \mathopen{}\left( H, S_u \mathclose{}\right)}{H} \\ \hspace{1em} \mathbf{return} \ S_u \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_u &= \text{Undrained shear strength (kPa)}\\
H &= \text{Thickness (m)}\\
H &= \text{Effective shear depth (m)}
\end{align*}
$$

#### `get_bearing_capacity_factor_cohesion__terzaghi1943theoretical`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_bearing\_capacity\_factor\_cohesion\_\_terzaghi1943theoretical}(ϕ, N_q) \\ \hspace{1em} \mathbf{if} \ \mathrm{np}.\mathrm{equal} \mathopen{}\left( ϕ, 0 \mathclose{}\right) \\ \hspace{2em} N_c \gets 5.7 \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} N_c \gets \frac{N_q - 1}{\mathrm{tandg} \mathopen{}\left( ϕ \mathclose{}\right)} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ N_c \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_c &= \text{Bearing capacity factor for cohesion}\\
ϕ &= \text{Friction angle (°)}\\
N_q &= \text{Bearing capacity factor for surcharge}
\end{align*}
$$

#### `get_bearing_capacity_factor_cohesion__vesic1975bearing`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_bearing\_capacity\_factor\_cohesion\_\_vesic1975bearing}(ϕ, N_q) \\ \hspace{1em} \mathbf{if} \ ϕ = 0 \\ \hspace{2em} N_c \gets 5.14 \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} N_c \gets \frac{N_q - 1}{\mathrm{tandg} \mathopen{}\left( ϕ \mathclose{}\right)} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ N_c \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_c &= \text{Bearing capacity factor for cohesion}\\
ϕ &= \text{Friction angle (°)}\\
N_q &= \text{Bearing capacity factor for surcharge}
\end{align*}
$$

#### `get_bearing_capacity_factor_cohesion_bottom_layer__vesic1975bearing`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_bearing\_capacity\_factor\_cohesion\_bottom\_layer\_\_vesic1975bearing}() \\ \hspace{1em} N_{c\ bottom} \gets 5.14 \\ \hspace{1em} \mathbf{return} \ N_{c\ bottom} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_{c\ bottom} &= \text{Bearing capacity factor for cohesion bottom layer}
\end{align*}
$$

#### `get_bearing_capacity_factor_surcharge__terzaghi1943theoretical`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_bearing\_capacity\_factor\_surcharge\_\_terzaghi1943theoretical}(ϕ) \\ \hspace{1em} α_θ \gets \exp \mathopen{}\left( \mathrm{np}.\pi \cdot \mathopen{}\left( 0.75 - \frac{ϕ}{360} \mathclose{}\right) \mathrm{tandg} \mathopen{}\left( ϕ \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} N_q \gets \frac{α_θ^{2}}{2 \mathopen{}\left( \mathrm{cosdg} \mathopen{}\left( 45 + \frac{ϕ}{2} \mathclose{}\right) \mathclose{}\right)^{2}} \\ \hspace{1em} \mathbf{return} \ N_q \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_q &= \text{Bearing capacity factor for surcharge}\\
ϕ &= \text{Friction angle (°)}
\end{align*}
$$

#### `get_bearing_capacity_factor_surcharge__vesic1975bearing`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_bearing\_capacity\_factor\_surcharge\_\_vesic1975bearing}(ϕ) \\ \hspace{1em} N_q \gets \exp \mathopen{}\left( \mathrm{np}.\pi \cdot \mathrm{tandg} \mathopen{}\left( ϕ \mathclose{}\right) \mathclose{}\right) \cdot \mathopen{}\left( \mathrm{tandg} \mathopen{}\left( 45 + \frac{ϕ}{2} \mathclose{}\right) \mathclose{}\right)^{2} \\ \hspace{1em} \mathbf{return} \ N_q \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_q &= \text{Bearing capacity factor for surcharge}\\
ϕ &= \text{Friction angle (°)}
\end{align*}
$$

#### `get_bearing_capacity_factor_surcharge_bottom_layer__vesic1975bearing`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_bearing\_capacity\_factor\_surcharge\_bottom\_layer\_\_vesic1975bearing}(ϕ_{bottom}) \\ \hspace{1em} N_{q\ bottom} \gets \mathrm{get\_bearing\_capacity\_factor\_surcharge\_\_vesic1975bearing} \mathopen{}\left( ϕ_{bottom} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ N_{q\ bottom} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_{q\ bottom} &= \text{Bearing capacity factor for surcharge bottom layer}\\
ϕ_{bottom} &= \text{Friction angle bottom layer (°)}
\end{align*}
$$

#### `get_bearing_capacity_factor_unit_weight__terzaghi1943theoretical`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_bearing\_capacity\_factor\_unit\_weight\_\_terzaghi1943theoretical}(N_q, ϕ) \\ \hspace{1em} N_γ \gets \frac{2 \mathopen{}\left( N_q + 1 \mathclose{}\right) \mathrm{tandg} \mathopen{}\left( ϕ \mathclose{}\right)}{1 + 0.4 \mathrm{sindg} \mathopen{}\left( 4 ϕ \mathclose{}\right)} \\ \hspace{1em} \mathbf{return} \ N_γ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_γ &= \text{Bearing capacity factor for unit weight}\\
N_q &= \text{Bearing capacity factor for surcharge}\\
ϕ &= \text{Friction angle (°)}
\end{align*}
$$

#### `get_bearing_capacity_factor_unit_weight__vesic1975bearing`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_bearing\_capacity\_factor\_unit\_weight\_\_vesic1975bearing}(N_q, ϕ) \\ \hspace{1em} N_γ \gets 2 \mathopen{}\left( N_q + 1 \mathclose{}\right) \mathrm{tandg} \mathopen{}\left( ϕ \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ N_γ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_γ &= \text{Bearing capacity factor for unit weight}\\
N_q &= \text{Bearing capacity factor for surcharge}\\
ϕ &= \text{Friction angle (°)}
\end{align*}
$$

#### `get_bearing_capacity_factor_unit_weight_bottom_layer__vesic1975bearing`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_bearing\_capacity\_factor\_unit\_weight\_bottom\_layer\_\_vesic1975bearing}(N_{q\ bottom}, ϕ_{bottom}) \\ \hspace{1em} N_{γ\ bottom} \gets \mathrm{get\_bearing\_capacity\_factor\_unit\_weight\_\_vesic1975bearing} \mathopen{}\left( N_{q\ bottom}, ϕ_{bottom} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ N_{γ\ bottom} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_{γ\ bottom} &= \text{Bearing capacity factor for unit weight bottom layer}\\
N_{q\ bottom} &= \text{Bearing capacity factor for surcharge bottom layer}\\
ϕ_{bottom} &= \text{Friction angle bottom layer (°)}
\end{align*}
$$

#### `get_bearing_capacity_ratio_case1__meyerhof1978ultimate`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_bearing\_capacity\_ratio\_case1\_\_meyerhof1978ultimate}(S_{u\ bottom}, N_{c\ bottom}, γ', B, N_γ) \\ \hspace{1em} {q_2}/{q_1} \gets \frac{S_{u\ bottom} \cdot N_{c\ bottom}}{0.5 γ' \cdot B \cdot N_γ} \\ \hspace{1em} \mathbf{return} \ {q_2}/{q_1} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
{q_2}/{q_1} &= \text{Bearing capacity ratio}\\
S_{u\ bottom} &= \text{Undrained shear strength bottom layer (kPa)}\\
N_{c\ bottom} &= \text{Bearing capacity factor for cohesion bottom layer}\\
γ' &= \text{Effective unit weight (kN/m3)}\\
B &= \text{Footing width (m)}\\
N_γ &= \text{Bearing capacity factor for unit weight}
\end{align*}
$$

#### `get_bearing_capacity_ratio_case2__meyerhof1978ultimate`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_bearing\_capacity\_ratio\_case2\_\_meyerhof1978ultimate}(γ_{bottom}', N_{γ\ bottom}, γ', N_γ) \\ \hspace{1em} {q_2}/{q_1} \gets \frac{γ_{bottom}' \cdot N_{γ\ bottom}}{γ' \cdot N_γ} \\ \hspace{1em} \mathbf{return} \ {q_2}/{q_1} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
{q_2}/{q_1} &= \text{Bearing capacity ratio}\\
γ_{bottom}' &= \text{Effective unit weight bottom layer (kN/m3)}\\
N_{γ\ bottom} &= \text{Bearing capacity factor for unit weight bottom layer}\\
γ' &= \text{Effective unit weight (kN/m3)}\\
N_γ &= \text{Bearing capacity factor for unit weight}
\end{align*}
$$

#### `get_depth_factor_cohesion__vesic1975bearing`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_depth\_factor\_cohesion\_\_vesic1975bearing}(k) \\ \hspace{1em} d_c \gets 1 + 0.4 k \\ \hspace{1em} \mathbf{return} \ d_c \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
d_c &= \text{Depth factor for cohesion}\\
k &= \text{Footing embedment to width ratio}
\end{align*}
$$

#### `get_depth_factor_surcharge__vesic1975bearing`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_depth\_factor\_surcharge\_\_vesic1975bearing}(k, ϕ) \\ \hspace{1em} d_q \gets 1 + 2 k \cdot \mathrm{tandg} \mathopen{}\left( ϕ \mathclose{}\right) \mathopen{}\left( 1 - \mathrm{sindg} \mathopen{}\left( ϕ \mathclose{}\right) \mathclose{}\right)^{2} \\ \hspace{1em} \mathbf{return} \ d_q \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
d_q &= \text{Depth factor for surcharge}\\
k &= \text{Footing embedment to width ratio}\\
ϕ &= \text{Friction angle (°)}
\end{align*}
$$

#### `get_depth_factor_unit_weight__vesic1975bearing`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_depth\_factor\_unit\_weight\_\_vesic1975bearing}() \\ \hspace{1em} d_γ \gets 1 \\ \hspace{1em} \mathbf{return} \ d_γ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
d_γ &= \text{Depth factor for unit weight}
\end{align*}
$$

#### `get_effective_shear_depth`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_effective\_shear\_depth}(B, ϕ) \\ \hspace{1em} H \gets 0.5 B \cdot \mathrm{tandg} \mathopen{}\left( 45 + \frac{ϕ}{2} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ H \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
H &= \text{Effective shear depth (m)}\\
B &= \text{Footing width (m)}\\
ϕ &= \text{Friction angle (°)}
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

#### `get_effective_unit_weight__vesic1973analysis`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_effective\_unit\_weight\_\_vesic1973analysis}(γ, z_{w\ present}, z_w, D_f, B) \\ \hspace{1em} γ' \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \lnot z_{w\ present} \\ \hspace{2em} γ' \gets γ \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ z_w \le D_f \\ \hspace{3em} γ' \gets γ - γ_w \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ D_f + B > z_w \\ \hspace{4em} γ' \gets γ - γ_w \cdot \mathopen{}\left( 1 - \frac{z_w - D_f}{B} \mathclose{}\right) \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ D_f + B \le z_w \\ \hspace{5em} γ' \gets γ \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ γ' \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
γ' &= \text{Effective unit weight (kN/m3)}\\
γ &= \text{Unit weight (kN/m3)}\\
z_{w\ present} &= \text{Water table present}\\
z_w &= \text{Water table (m)}\\
D_f &= \text{Footing embedment (m)}\\
B &= \text{Footing width (m)}\\
γ_w &= \text{Water unit weight (kN/m3)}
\end{align*}
$$

#### `get_effective_unit_weight_bottom_layer__vesic1973analysis`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_effective\_unit\_weight\_bottom\_layer\_\_vesic1973analysis}(γ_{bottom}, z_{w\ present}, D_f, H_{top}, z_w, B) \\ \hspace{1em} γ_{bottom}' \gets \mathrm{get\_effective\_unit\_weight\_\_vesic1973analysis} \mathopen{}\left( γ_{bottom}, z_{w\ present}, z_w, D_f + H_{top}, B, γ_w \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ γ_{bottom}' \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
γ_{bottom}' &= \text{Effective unit weight bottom layer (kN/m3)}\\
γ_{bottom} &= \text{Unit weight bottom layer (kN/m3)}\\
z_{w\ present} &= \text{Water table present}\\
D_f &= \text{Footing embedment (m)}\\
H_{top} &= \text{Thickness of top layer (m)}\\
z_w &= \text{Water table (m)}\\
B &= \text{Footing width (m)}\\
γ_w &= \text{Water unit weight (kN/m3)}
\end{align*}
$$

#### `get_footing_creep_settlement_inc`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_footing\_creep\_settlement\_inc}(\mathrm{consider\_creep\_settlement}, H, M, σ_v', t, t_p) \\ \hspace{1em} \mathbf{if} \ \mathrm{consider\_creep\_settlement} \\ \hspace{2em} S_{creep} \gets 0.01 \frac{σ_v'}{M} \cdot H \cdot \log_{10} \mathopen{}\left( \frac{t}{t_p} \mathclose{}\right) \\ \hspace{2em} S_{creep} \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( S_{creep} \mathclose{}\right) \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} S_{creep} \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( H, 0 \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ S_{creep} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_{creep} &= \text{Footing creep settlement inc. (cm)}\\
\text{consider\_creep\_settlement} &= \text{Consider creep settlement}\\
H &= \text{Thickness (m)}\\
M &= \text{Constrained modulus (MPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
t &= \text{Consolidation time (month)}\\
t_p &= \text{Primary consolidation time (month)}
\end{align*}
$$

#### `get_footing_creep_settlement_sum`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_footing\_creep\_settlement\_sum}(S_{creep}) \\ \hspace{1em} ΣS_{creep} \gets \sum S_{creep} \\ \hspace{1em} \mathbf{return} \ ΣS_{creep} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ΣS_{creep} &= \text{Footing creep settlement sum (cm)}\\
S_{creep} &= \text{Footing creep settlement inc. (cm)}
\end{align*}
$$

#### `get_footing_effective_stress`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_footing\_effective\_stress}(σ_v, u_0) \\ \hspace{1em} σ_v' \gets \mathrm{get\_effective\_stress} \mathopen{}\left( σ_v, u_0 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ σ_v' \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
σ_v' &= \text{Effective stress (kPa)}\\
σ_v &= \text{Total stress (kPa)}\\
u_0 &= \text{Pore water pressure (kPa)}
\end{align*}
$$

#### `get_footing_embedment_to_width_ratio__vesic1975bearing`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_footing\_embedment\_to\_width\_ratio\_\_vesic1975bearing}(D_f, B) \\ \hspace{1em} k \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( \frac{D_f}{B} \le 1, \frac{D_f}{B}, \arctan \mathopen{}\left( \frac{D_f}{B} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ k \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
k &= \text{Footing embedment to width ratio}\\
D_f &= \text{Footing embedment (m)}\\
B &= \text{Footing width (m)}
\end{align*}
$$

#### `get_footing_influence_depth`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_footing\_influence\_depth}(B, D_f, IF) \\ \hspace{1em} z_{infl} \gets D_f + IF \cdot B \\ \hspace{1em} \mathbf{return} \ z_{infl} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
z_{infl} &= \text{Footing influence depth (m)}\\
B &= \text{Footing width (m)}\\
D_f &= \text{Footing embedment (m)}\\
IF &= \text{Footing influence width factor}
\end{align*}
$$

#### `get_footing_pore_water_pressure`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_footing\_pore\_water\_pressure}(z_{w\ present}, D_f, z_w) \\ \hspace{1em} u_0 \gets \mathrm{get\_pore\_water\_pressure} \mathopen{}\left( z_{w\ present}, z_w, D_f \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ u_0 \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
u_0 &= \text{Pore water pressure (kPa)}\\
z_{w\ present} &= \text{Water table present}\\
D_f &= \text{Footing embedment (m)}\\
z_w &= \text{Water table (m)}
\end{align*}
$$

#### `get_footing_settlement`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_footing\_settlement}(S_i) \\ \hspace{1em} S \gets \mathrm{reverse\_cumsum} \mathopen{}\left( S_i \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ S \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S &= \text{Footing settlement (cm)}\\
S_i &= \text{Footing settlement inc. (cm)}
\end{align*}
$$

#### `get_footing_settlement_inc`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_footing\_settlement\_inc}(H, M, Δ_σ, \mathrm{apply\_20\_percent\_rule}, σ_v') \\ \hspace{1em} \mathbf{if} \ \mathrm{apply\_20\_percent\_rule} \\ \hspace{2em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( Δ_σ, 0.2 σ_v' > Δ_σ, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} S_i \gets \frac{0.1 H \cdot Δ_σ}{M} \\ \hspace{1em} S_i \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( S_i \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ S_i \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_i &= \text{Footing settlement inc. (cm)}\\
H &= \text{Thickness (m)}\\
M &= \text{Constrained modulus (MPa)}\\
Δ_σ &= \text{Imposed stress (kPa)}\\
\text{apply\_20\_percent\_rule} &= \text{Apply 20\% rule}\\
σ_v' &= \text{Effective stress (kPa)}
\end{align*}
$$

#### `get_footing_settlement_sum`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_footing\_settlement\_sum}(S_i) \\ \hspace{1em} ΣS \gets \sum S_i \\ \hspace{1em} \mathbf{return} \ ΣS \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ΣS &= \text{Footing settlement sum (cm)}\\
S_i &= \text{Footing settlement inc. (cm)}
\end{align*}
$$

#### `get_footing_total_stress`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_footing\_total\_stress}(γ, D_f) \\ \hspace{1em} σ_v \gets \mathrm{get\_total\_stress} \mathopen{}\left( γ, D_f \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ σ_v \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
σ_v &= \text{Total stress (kPa)}\\
γ &= \text{Unit weight (kN/m3)}\\
D_f &= \text{Footing embedment (m)}
\end{align*}
$$

#### `get_imposed_stress`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_imposed\_stress}(q_o, I_z) \\ \hspace{1em} Δ_σ \gets q_o \cdot I_z \\ \hspace{1em} \mathbf{return} \ Δ_σ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Δ_σ &= \text{Imposed stress (kPa)}\\
q_o &= \text{Footing applied load (kPa)}\\
I_z &= \text{Stress influence factor}
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

#### `get_punching_shear_coefficient__meyerhof1978ultimate`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_punching\_shear\_coefficient\_\_meyerhof1978ultimate}({q_2}/{q_1}, ϕ) \\ \hspace{1em} K_s \gets \mathrm{PunchingShearCoefficientMeyerhof1978Figure}.\mathrm{as\_reference\_data} \mathopen{}\left( \mathclose{}\right).\mathrm{interpolate\_at\_index\_column} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ K_s \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K_s &= \text{Punching shear coefficient}\\
{q_2}/{q_1} &= \text{Bearing capacity ratio}\\
ϕ &= \text{Friction angle (°)}
\end{align*}
$$

#### `get_shape_factor_cohesion__vesic1975bearing`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shape\_factor\_cohesion\_\_vesic1975bearing}(B, N_q, N_c, L, \mathrm{footing\_shape}) \\ \hspace{1em} \mathbf{if} \ \mathrm{footing\_shape} = \textrm{"continuous"} \\ \hspace{2em} \mathbf{return} \ 1 \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{footing\_shape} \in \mathopen{}\left( \textrm{"square"}, \textrm{"circular"} \mathclose{}\right) \\ \hspace{3em} L \gets B \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} s_c \gets 1 + \frac{B}{L} \frac{N_q}{N_c} \\ \hspace{1em} \mathbf{return} \ s_c \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
s_c &= \text{Shape factor for cohesion}\\
B &= \text{Footing width (m)}\\
N_q &= \text{Bearing capacity factor for surcharge}\\
N_c &= \text{Bearing capacity factor for cohesion}\\
L &= \text{Footing length (m)}\\
\text{footing\_shape} &= \text{Footing shape}
\end{align*}
$$

#### `get_shape_factor_surcharge__vesic1975bearing`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shape\_factor\_surcharge\_\_vesic1975bearing}(B, ϕ, L, \mathrm{footing\_shape}) \\ \hspace{1em} \mathbf{if} \ \mathrm{footing\_shape} = \textrm{"continuous"} \\ \hspace{2em} \mathbf{return} \ 1 \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{footing\_shape} \in \mathopen{}\left( \textrm{"square"}, \textrm{"circular"} \mathclose{}\right) \\ \hspace{3em} L \gets B \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} s_q \gets 1 + \frac{B}{L} \cdot \mathrm{tandg} \mathopen{}\left( ϕ \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ s_q \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
s_q &= \text{Shape factor for surcharge}\\
B &= \text{Footing width (m)}\\
ϕ &= \text{Friction angle (°)}\\
L &= \text{Footing length (m)}\\
\text{footing\_shape} &= \text{Footing shape}
\end{align*}
$$

#### `get_shape_factor_surcharge_bottom_layer__vesic1975bearing`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shape\_factor\_surcharge\_bottom\_layer\_\_vesic1975bearing}(B, ϕ_{bottom}, L, \mathrm{footing\_shape}) \\ \hspace{1em} s_{q\ bottom} \gets \mathrm{get\_shape\_factor\_surcharge\_\_vesic1975bearing} \mathopen{}\left( B, ϕ_{bottom}, L, \mathrm{footing\_shape} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ s_{q\ bottom} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
s_{q\ bottom} &= \text{Shape factor for surcharge bottom layer}\\
B &= \text{Footing width (m)}\\
ϕ_{bottom} &= \text{Friction angle bottom layer (°)}\\
L &= \text{Footing length (m)}\\
\text{footing\_shape} &= \text{Footing shape}
\end{align*}
$$

#### `get_shape_factor_unit_weight__vesic1975bearing`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shape\_factor\_unit\_weight\_\_vesic1975bearing}(B, L, \mathrm{footing\_shape}) \\ \hspace{1em} \mathbf{if} \ \mathrm{footing\_shape} = \textrm{"continuous"} \\ \hspace{2em} \mathbf{return} \ 1 \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{footing\_shape} \in \mathopen{}\left( \textrm{"square"}, \textrm{"circular"} \mathclose{}\right) \\ \hspace{3em} L \gets B \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} s_γ \gets 1 - 0.4 \frac{B}{L} \\ \hspace{1em} \mathbf{return} \ s_γ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
s_γ &= \text{Shape factor for unit weight}\\
B &= \text{Footing width (m)}\\
L &= \text{Footing length (m)}\\
\text{footing\_shape} &= \text{Footing shape}
\end{align*}
$$

#### `get_stress_influence_factor`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_stress\_influence\_factor}(\mathrm{footing\_shape}, B, L, z, D_f) \\ \hspace{1em} I_z \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{footing\_shape} = \textrm{"square"} \\ \hspace{2em} L \gets B \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{if} \ \lnot \mathrm{is\_null} \mathopen{}\left( D_f \mathclose{}\right) \\ \hspace{2em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( z, z < D_f, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{2em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( z, z \ge D_f, z - D_f \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{if} \ \mathrm{footing\_shape} = \textrm{"circular"} \\ \hspace{2em} I_z \gets 1 - \frac{1}{\mathopen{}\left( 1 + \mathopen{}\left( \frac{B}{2 z} \mathclose{}\right)^{2} \mathclose{}\right)^{\frac{3}{2}}} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{footing\_shape} \in \mathopen{}\left( \textrm{"square"}, \textrm{"rectangular"} \mathclose{}\right) \\ \hspace{3em} m \gets \frac{L}{B} \\ \hspace{3em} n \gets \frac{z}{\frac{B}{2}} \\ \hspace{3em} I_z \gets \frac{2}{\mathrm{np}.\pi} \cdot \mathopen{}\left( \frac{\frac{m n}{\sqrt{ 1 + m^{2} + n^{2} }} \cdot \mathopen{}\left( 1 + m^{2} + 2 n^{2} \mathclose{}\right)}{\mathopen{}\left( 1 + n^{2} \mathclose{}\right) \mathopen{}\left( m^{2} + n^{2} \mathclose{}\right)} + \arcsin \mathopen{}\left( \frac{m}{\sqrt{ m^{2} + n^{2} } \cdot \sqrt{ 1 + n^{2} }} \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ I_z \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
I_z &= \text{Stress influence factor}\\
\text{footing\_shape} &= \text{Footing shape}\\
B &= \text{Footing width (m)}\\
L &= \text{Footing length (m)}\\
z &= \text{Depth (m)}\\
D_f &= \text{Footing embedment (m)}
\end{align*}
$$

#### `get_stress_influence_factor_at_corner`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_stress\_influence\_factor\_at\_corner}(B, L, z) \\ \hspace{1em} m \gets \frac{B}{z} \\ \hspace{1em} n \gets \frac{L}{z} \\ \hspace{1em} I_z \gets \frac{1}{4 \mathrm{np}.\pi} \cdot \mathopen{}\left( \frac{2 m n \cdot \sqrt{ m^{2} + n^{2} + 1 }}{m^{2} + n^{2} + m^{2} n^{2} + 1} \frac{m^{2} + n^{2} + 2}{m^{2} + n^{2} + 1} + \mathrm{np}.\mathrm{arctan2} \mathopen{}\left( 2 m n \cdot \sqrt{ m^{2} + n^{2} + 1 }, m^{2} + n^{2} - m^{2} n^{2} + 1 \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ I_z \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
I_z &= \text{Stress influence factor}\\
B &= \text{Footing width (m)}\\
L &= \text{Footing length (m)}\\
z &= \text{Depth (m)}
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

#### `get_ultimate_bearing_capacity__terzaghi1943theoretical`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_ultimate\_bearing\_capacity\_\_terzaghi1943theoretical}(\mathrm{footing\_shape}, B, S_u, σ_v', γ', N_c, N_q, N_γ) \\ \hspace{1em} \textrm{" From coduto16: terzaghi’s method is still often used, primarily because it is simple and familiar.
    However, it does not consider special cases, such as rectangular footings, inclined loads,
    or footings with large depth-to-width ratios "} \\ \hspace{1em} \mathbf{if} \ \mathrm{footing\_shape} = \textrm{"square"} \\ \hspace{2em} \mathrm{c1} \gets 1.3 \\ \hspace{2em} \mathrm{c2} \gets 0.4 \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{footing\_shape} = \textrm{"continuous"} \\ \hspace{3em} \mathrm{c1} \gets 1 \\ \hspace{3em} \mathrm{c2} \gets 0.5 \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ \mathrm{footing\_shape} = \textrm{"circular"} \\ \hspace{4em} \mathrm{c1} \gets 1.3 \\ \hspace{4em} \mathrm{c2} \gets 0.3 \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"\{\} shape not supported for this method"}.\mathrm{format} \mathopen{}\left( \mathrm{footing\_shape} \mathclose{}\right) \mathclose{}\right) \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} Q_{ult} \gets \mathrm{c1} \cdot S_u \cdot N_c + σ_v' \cdot N_q + \mathrm{c2} \cdot γ' \cdot B \cdot N_γ \\ \hspace{1em} \mathbf{return} \ Q_{ult} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_{ult} &= \text{Ultimate bearing capacity (kPa)}\\
\text{footing\_shape} &= \text{Footing shape}\\
B &= \text{Footing width (m)}\\
S_u &= \text{Undrained shear strength (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
γ' &= \text{Effective unit weight (kN/m3)}\\
N_c &= \text{Bearing capacity factor for cohesion}\\
N_q &= \text{Bearing capacity factor for surcharge}\\
N_γ &= \text{Bearing capacity factor for unit weight}
\end{align*}
$$

#### `get_ultimate_bearing_capacity__vesic1975bearing`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_ultimate\_bearing\_capacity\_\_vesic1975bearing}(B, S_u, σ_v', γ', N_c, N_q, N_γ, s_c, s_q, s_γ, d_c, d_q, d_γ) \\ \hspace{1em} Q_{ult} \gets S_u \cdot N_c \cdot s_c \cdot d_c + σ_v' \cdot N_q \cdot s_q \cdot d_q + 0.5 γ' \cdot B \cdot N_γ \cdot s_γ \cdot d_γ \\ \hspace{1em} \mathbf{return} \ Q_{ult} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_{ult} &= \text{Ultimate bearing capacity (kPa)}\\
B &= \text{Footing width (m)}\\
S_u &= \text{Undrained shear strength (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
γ' &= \text{Effective unit weight (kN/m3)}\\
N_c &= \text{Bearing capacity factor for cohesion}\\
N_q &= \text{Bearing capacity factor for surcharge}\\
N_γ &= \text{Bearing capacity factor for unit weight}\\
s_c &= \text{Shape factor for cohesion}\\
s_q &= \text{Shape factor for surcharge}\\
s_γ &= \text{Shape factor for unit weight}\\
d_c &= \text{Depth factor for cohesion}\\
d_q &= \text{Depth factor for surcharge}\\
d_γ &= \text{Depth factor for unit weight}
\end{align*}
$$

#### `get_ultimate_bearing_capacity_case1__meyerhof1978ultimate`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_ultimate\_bearing\_capacity\_case1\_\_meyerhof1978ultimate}(B, D_f, K_s, S_{u\ bottom}, σ_v', γ', H_{top}, ϕ, Q_{ult\ lim}, L, \mathrm{footing\_shape}) \\ \hspace{1em} \mathbf{if} \ \mathrm{footing\_shape} = \textrm{"continuous"} \\ \hspace{2em} L \gets \mathrm{np}.\mathrm{inf} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{footing\_shape} \in \mathopen{}\left( \textrm{"square"}, \textrm{"circular"} \mathclose{}\right) \\ \hspace{3em} L \gets B \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} Q_{ult} \gets \mathopen{}\left( 1 + 0.2 \frac{B}{L} \mathclose{}\right) \cdot 5.14 S_{u\ bottom} + γ' \cdot H_{top}^{2} \cdot \mathopen{}\left( 1 + \frac{B}{L} \mathclose{}\right) \mathopen{}\left( 1 + \frac{2 D_f}{H_{top}} \mathclose{}\right) \frac{K_s \cdot \mathrm{tandg} \mathopen{}\left( ϕ \mathclose{}\right)}{B} + σ_v' \\ \hspace{1em} Q_{ult} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( Q_{ult}, \mathrm{None}, Q_{ult\ lim} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ Q_{ult} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_{ult} &= \text{Ultimate bearing capacity (kPa)}\\
B &= \text{Footing width (m)}\\
D_f &= \text{Footing embedment (m)}\\
K_s &= \text{Punching shear coefficient}\\
S_{u\ bottom} &= \text{Undrained shear strength bottom layer (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
γ' &= \text{Effective unit weight (kN/m3)}\\
H_{top} &= \text{Thickness of top layer (m)}\\
ϕ &= \text{Friction angle (°)}\\
Q_{ult\ lim} &= \text{Ultimate bearing capacity limit (kPa)}\\
L &= \text{Footing length (m)}\\
\text{footing\_shape} &= \text{Footing shape}
\end{align*}
$$

#### `get_ultimate_bearing_capacity_case2__meyerhof1978ultimate`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_ultimate\_bearing\_capacity\_case2\_\_meyerhof1978ultimate}(ϕ, \mathrm{footing\_shape}, B, D_f, H_{top}, γ', K_s, N_{q\ bottom}, s_{q\ bottom}, N_{γ\ bottom}, s_γ, γ_{bottom}', Q_{ult\ lim}, L) \\ \hspace{1em} \mathbf{if} \ \mathrm{footing\_shape} \in \mathopen{}\left( \textrm{"square"}, \textrm{"circular"} \mathclose{}\right) \\ \hspace{2em} L \gets B \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} Q_{ult} \gets γ' \cdot \mathopen{}\left( D_f + H_{top} \mathclose{}\right) N_{q\ bottom} \cdot s_{q\ bottom} + 0.5 γ_{bottom}' \cdot B \cdot N_{γ\ bottom} \cdot s_γ + γ' \cdot H_{top}^{2} \cdot \mathopen{}\left( 1 + \frac{B}{L} \mathclose{}\right) \mathopen{}\left( 1 + \frac{2 D_f}{H_{top}} \mathclose{}\right) \frac{K_s \cdot \mathrm{tandg} \mathopen{}\left( ϕ \mathclose{}\right)}{B} - γ' \cdot H_{top} \\ \hspace{1em} Q_{ult} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( Q_{ult}, \mathrm{None}, Q_{ult\ lim} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ Q_{ult} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_{ult} &= \text{Ultimate bearing capacity (kPa)}\\
ϕ &= \text{Friction angle (°)}\\
\text{footing\_shape} &= \text{Footing shape}\\
B &= \text{Footing width (m)}\\
D_f &= \text{Footing embedment (m)}\\
H_{top} &= \text{Thickness of top layer (m)}\\
γ' &= \text{Effective unit weight (kN/m3)}\\
K_s &= \text{Punching shear coefficient}\\
N_{q\ bottom} &= \text{Bearing capacity factor for surcharge bottom layer}\\
s_{q\ bottom} &= \text{Shape factor for surcharge bottom layer}\\
N_{γ\ bottom} &= \text{Bearing capacity factor for unit weight bottom layer}\\
s_γ &= \text{Shape factor for unit weight}\\
γ_{bottom}' &= \text{Effective unit weight bottom layer (kN/m3)}\\
Q_{ult\ lim} &= \text{Ultimate bearing capacity limit (kPa)}\\
L &= \text{Footing length (m)}
\end{align*}
$$

#### `get_ultimate_bearing_capacity_case3__meyerhof1978ultimate`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_ultimate\_bearing\_capacity\_case3\_\_meyerhof1978ultimate}(B, c_α, S_{u\ bottom}, σ_v', H_{top}, Q_{ult\ lim}, L, \mathrm{footing\_shape}) \\ \hspace{1em} \mathbf{if} \ \mathrm{footing\_shape} = \textrm{"continuous"} \\ \hspace{2em} L \gets \mathrm{np}.\mathrm{inf} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{footing\_shape} \in \mathopen{}\left( \textrm{"square"}, \textrm{"circular"} \mathclose{}\right) \\ \hspace{3em} L \gets B \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} Q_{ult} \gets \mathopen{}\left( 1 + 0.2 \frac{B}{L} \mathclose{}\right) \cdot 5.14 S_{u\ bottom} + \mathopen{}\left( 1 + \frac{B}{L} \mathclose{}\right) \frac{2 c_α \cdot H_{top}}{B} + σ_v' \\ \hspace{1em} Q_{ult} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( Q_{ult}, \mathrm{None}, Q_{ult\ lim} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ Q_{ult} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_{ult} &= \text{Ultimate bearing capacity (kPa)}\\
B &= \text{Footing width (m)}\\
c_α &= \text{Unit adhesion (kPa)}\\
S_{u\ bottom} &= \text{Undrained shear strength bottom layer (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
H_{top} &= \text{Thickness of top layer (m)}\\
Q_{ult\ lim} &= \text{Ultimate bearing capacity limit (kPa)}\\
L &= \text{Footing length (m)}\\
\text{footing\_shape} &= \text{Footing shape}
\end{align*}
$$

#### `get_ultimate_bearing_capacity_limit_case1and2__meyerhof1978ultimate`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_ultimate\_bearing\_capacity\_limit\_case1and2\_\_meyerhof1978ultimate}(B, σ_v', γ', N_q, N_γ, s_q, s_γ) \\ \hspace{1em} Q_{ult\ lim} \gets \mathrm{get\_ultimate\_bearing\_capacity\_\_vesic1975bearing} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} a \gets 0 \\ \hspace{1em} d_q \gets 1 \\ \hspace{1em} d_γ \gets 1 \\ \hspace{1em} \mathbf{return} \ Q_{ult\ lim} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_{ult\ lim} &= \text{Ultimate bearing capacity limit (kPa)}\\
B &= \text{Footing width (m)}\\
σ_v' &= \text{Effective stress (kPa)}\\
γ' &= \text{Effective unit weight (kN/m3)}\\
N_q &= \text{Bearing capacity factor for surcharge}\\
N_γ &= \text{Bearing capacity factor for unit weight}\\
s_q &= \text{Shape factor for surcharge}\\
s_γ &= \text{Shape factor for unit weight}
\end{align*}
$$

#### `get_ultimate_bearing_capacity_limit_case3__meyerhof1978ultimate`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_ultimate\_bearing\_capacity\_limit\_case3\_\_meyerhof1978ultimate}(B, S_u, σ_v', L, \mathrm{footing\_shape}) \\ \hspace{1em} \mathbf{if} \ \mathrm{footing\_shape} = \textrm{"continuous"} \\ \hspace{2em} L \gets \mathrm{np}.\mathrm{inf} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{footing\_shape} \in \mathopen{}\left( \textrm{"square"}, \textrm{"circular"} \mathclose{}\right) \\ \hspace{3em} L \gets B \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} Q_{ult\ lim} \gets \mathopen{}\left( 1 + 0.2 \frac{B}{L} \mathclose{}\right) \cdot 5.14 S_u + σ_v' \\ \hspace{1em} \mathbf{return} \ Q_{ult\ lim} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_{ult\ lim} &= \text{Ultimate bearing capacity limit (kPa)}\\
B &= \text{Footing width (m)}\\
S_u &= \text{Undrained shear strength (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
L &= \text{Footing length (m)}\\
\text{footing\_shape} &= \text{Footing shape}
\end{align*}
$$

#### `get_unit_adhesion__meyerhof1978ultimate`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_unit\_adhesion\_\_meyerhof1978ultimate}(S_u, c_α/c_1) \\ \hspace{1em} c_α \gets S_u \cdot c_α/c_1 \\ \hspace{1em} \mathbf{return} \ c_α \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
c_α &= \text{Unit adhesion (kPa)}\\
S_u &= \text{Undrained shear strength (kPa)}\\
c_α/c_1 &= \text{Unit adhesion to cohesion ratio}
\end{align*}
$$

#### `get_unit_adhesion_to_cohesion_ratio__meyerhof1978ultimate`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_unit\_adhesion\_to\_cohesion\_ratio\_\_meyerhof1978ultimate}(S_u, S_{u\ bottom}) \\ \hspace{1em} {q_2}/{q_1} \gets \frac{S_{u\ bottom}}{S_u} \\ \hspace{1em} c_α/c_1 \gets \mathrm{UnitAdhesionToCohesionRatioMeyerhof1978Figure}.\mathrm{interpolate\_at\_x} \mathopen{}\left( {q_2}/{q_1} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ c_α/c_1 \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
c_α/c_1 &= \text{Unit adhesion to cohesion ratio}\\
S_u &= \text{Undrained shear strength (kPa)}\\
S_{u\ bottom} &= \text{Undrained shear strength bottom layer (kPa)}
\end{align*}
$$
