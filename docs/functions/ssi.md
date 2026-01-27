---
title: ssi.py
---

#### `_get_dashpot_edge_factor_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_dashpot\_edge\_factor\_scalar}(R_e, c, R_k, c_z^i, B_h, L_h, j) \\ \hspace{1em} R_c \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ j = \textrm{"xx"} \\ \hspace{2em} R_c \gets \frac{\frac{3 c}{4 c_z^i \cdot B_h^{3} \cdot L_h}}{R_k \cdot \mathopen{}\left( 1 - \mathopen{}\left( 1 - R_e \mathclose{}\right)^{3} \mathclose{}\right) + \mathopen{}\left( 1 - R_e \mathclose{}\right)^{3}} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ j = \textrm{"yy"} \\ \hspace{3em} R_c \gets \frac{\frac{3 c}{4 c_z^i \cdot B_h \cdot L_h^{3}}}{R_k \cdot \mathopen{}\left( 1 - \mathopen{}\left( 1 - R_e \mathclose{}\right)^{3} \mathclose{}\right) + \mathopen{}\left( 1 - R_e \mathclose{}\right)^{3}} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ j = \textrm{"z"} \\ \hspace{4em} R_c \gets 1 \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ R_c \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
R_c &= \text{Dashpot edge factor}\\
R_e &= \text{End length ratio}\\
c &= \text{Dashpot coefficient (MN-s/m or MN-m/rad)}\\
R_k &= \text{Stiffness edge factor}\\
c_z^i &= \text{Dashpot coefficient intensity vertical (MN-s/m3)}\\
B_h &= \text{Footing half width (m)}\\
L_h &= \text{Footing half length (m)}\\
j &= \text{Vibration mode}
\end{align*}
$$

#### `_get_dimensionless_pile_length_parameter_ksd_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_dimensionless\_pile\_length\_parameter\_ksd\_scalar}(E_p, I_p, j, k_{sd}) \\ \hspace{1em} λL \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ j = \textrm{"yy"} \\ \hspace{2em} λL \gets \mathopen{}\left( \frac{k_{sd}}{4 E_p \cdot I_p} \mathclose{}\right)^{\frac{1}{4}} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ λL \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
λL &= \text{Dimensionless pile length parameter}\\
E_p &= \text{Pile elasticity modulus (MPa)}\\
I_p &= \text{Pile moment of inertia (m4)}\\
j &= \text{Vibration mode}\\
k_{sd} &= \text{Subgrade reaction modulus at diameter (MPa)}
\end{align*}
$$

#### `_get_dimensionless_pile_length_parameter_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_dimensionless\_pile\_length\_parameter\_scalar}(E_p, E_s, δ, D, L, j) \\ \hspace{1em} λL \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ j = \textrm{"z"} \land D \ne 0 \\ \hspace{2em} λL \gets \mathopen{}\left( \frac{4 δ}{\mathrm{np}.\pi} \mathclose{}\right)^{\frac{1}{2}} \mathopen{}\left( \frac{E_p}{E_s} \mathclose{}\right)^{\frac{-1}{2}} \frac{L}{D} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ λL \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
λL &= \text{Dimensionless pile length parameter}\\
E_p &= \text{Pile elasticity modulus (MPa)}\\
E_s &= \text{Elasticity modulus (MPa)}\\
δ &= \text{Dimensionless subgrade reaction modulus}\\
D &= \text{Pile diameter (m)}\\
L &= \text{Pile embedment length (m)}\\
j &= \text{Vibration mode}
\end{align*}
$$

#### `_get_dimensionless_pile_tip_stiffness_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_dimensionless\_pile\_tip\_stiffness\_scalar}(E_p, E_s, δ, ν, j) \\ \hspace{1em} Ω \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ j = \textrm{"z"} \\ \hspace{2em} Ω \gets \frac{2}{\sqrt{ \mathrm{np}.\pi \cdot δ } \cdot \mathopen{}\left( 1 - ν^{2} \mathclose{}\right)} \mathopen{}\left( \frac{E_p}{E_s} \mathclose{}\right)^{\frac{-1}{2}} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ Ω \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Ω &= \text{Dimensionless pile tip stiffness}\\
E_p &= \text{Pile elasticity modulus (MPa)}\\
E_s &= \text{Elasticity modulus (MPa)}\\
δ &= \text{Dimensionless subgrade reaction modulus}\\
ν &= \text{Poisson’s ratio}\\
j &= \text{Vibration mode}
\end{align*}
$$

#### `_get_dimensionless_subgrade_reaction_modulus_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_dimensionless\_subgrade\_reaction\_modulus\_scalar}(E_p, E_s, j) \\ \hspace{1em} δ \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ j \in \mathopen{}\left( \textrm{"x"}, \textrm{"y"} \mathclose{}\right) \\ \hspace{2em} δ \gets 2 \mathopen{}\left( \frac{E_p}{E_s} \mathclose{}\right)^{\frac{-3}{40}} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ j = \textrm{"z"} \\ \hspace{3em} δ \gets 0.6 \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ j = \textrm{"yy"} \\ \hspace{4em} δ \gets 1.2 \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ δ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
δ &= \text{Dimensionless subgrade reaction modulus}\\
E_p &= \text{Pile elasticity modulus (MPa)}\\
E_s &= \text{Elasticity modulus (MPa)}\\
j &= \text{Vibration mode}
\end{align*}
$$

#### `_get_dynamic_stiffness_modifier_pile_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_dynamic\_stiffness\_modifier\_pile\_scalar}(δ, γ_p, γ, ν, a_0, j, w_s) \\ \hspace{1em} α \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ j = \textrm{"x"} \\ \hspace{2em} α \gets 1 - \frac{3 \mathrm{np}.\pi}{32 δ} \frac{\frac{γ_p}{γ}}{1 + ν} \cdot a_0^{2} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ j = \textrm{"z"} \\ \hspace{3em} α \gets 1 - w_s \cdot \mathopen{}\left( \frac{\mathrm{np}.\pi}{8 δ} \frac{\frac{γ_p}{γ}}{1 + ν} \cdot a_0^{2} - \frac{1}{2} \cdot a_0^{\frac{1}{2}} \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ α \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
α &= \text{Dynamic stiffness modifier}\\
δ &= \text{Dimensionless subgrade reaction modulus}\\
γ_p &= \text{Pile unit weight (kN/m3)}\\
γ &= \text{Unit weight (kN/m3)}\\
ν &= \text{Poisson’s ratio}\\
a_0 &= \text{Dimensionless frequency}\\
j &= \text{Vibration mode}\\
w_s &= \text{Stiffness weight factor soil}
\end{align*}
$$

#### `_get_dynamic_stiffness_modifier_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_dynamic\_stiffness\_modifier\_scalar}(a_0, L_h, B_h, j) \\ \hspace{1em} α \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ j \in \mathopen{}\left( \textrm{"x"}, \textrm{"y"} \mathclose{}\right) \\ \hspace{2em} α \gets 1 \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ j = \textrm{"z"} \\ \hspace{3em} α \gets 1 - \frac{\mathopen{}\left( 0.4 + \frac{0.2}{\frac{L_h}{B_h}} \mathclose{}\right) a_0^{2}}{\frac{10}{1 + 3 \mathopen{}\left( \frac{L_h}{B_h} - 1 \mathclose{}\right)} + a_0^{2}} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ j = \textrm{"xx"} \\ \hspace{4em} α \gets 1 - \frac{\mathopen{}\left( 0.55 + 0.01 \sqrt{ \frac{L_h}{B_h} - 1 } \mathclose{}\right) a_0^{2}}{2.4 - \frac{0.4}{\mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{3}} + a_0^{2}} \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ j = \textrm{"yy"} \\ \hspace{5em} α \gets 1 - \frac{0.55 a_0^{2}}{0.6 + \frac{1.4}{\mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{3}} + a_0^{2}} \\ \hspace{4em} \mathbf{else} \\ \hspace{5em} \mathbf{if} \ j = \textrm{"zz"} \\ \hspace{6em} α \gets 1 - \frac{0.33 - 0.03 \sqrt{ \frac{L_h}{B_h} - 1 } \cdot a_0^{2}}{\frac{0.8}{1 + 0.33 \mathopen{}\left( \frac{L_h}{B_h} - 1 \mathclose{}\right)} + a_0^{2}} \\ \hspace{5em} \mathbf{end \ if} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ α \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
α &= \text{Dynamic stiffness modifier}\\
a_0 &= \text{Dimensionless frequency}\\
L_h &= \text{Footing half length (m)}\\
B_h &= \text{Footing half width (m)}\\
j &= \text{Vibration mode}
\end{align*}
$$

#### `_get_effective_profile_depth_pile_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_effective\_profile\_depth\_pile\_scalar}(j, L, L_a) \\ \hspace{1em} z_p \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ j = \textrm{"z"} \\ \hspace{2em} z_p \gets L \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ j \in \mathopen{}\left( \textrm{"x"}, \textrm{"y"} \mathclose{}\right) \\ \hspace{3em} z_p \gets L_a \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ z_p \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
z_p &= \text{Effective profile depth (m)}\\
j &= \text{Vibration mode}\\
L &= \text{Pile embedment length (m)}\\
L_a &= \text{Active pile length (m)}
\end{align*}
$$

#### `_get_effective_profile_depth_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_effective\_profile\_depth\_scalar}(j, B_h, L_h) \\ \hspace{1em} z_p \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ j \in \mathopen{}\left( \textrm{"x"}, \textrm{"y"}, \textrm{"z"} \mathclose{}\right) \\ \hspace{2em} z_p \gets \mathopen{}\left( B_h \cdot L_h \mathclose{}\right)^{0.5} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ j = \textrm{"xx"} \\ \hspace{3em} z_p \gets \mathopen{}\left( B_h^{3} \cdot L_h \mathclose{}\right)^{0.25} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ j = \textrm{"yy"} \\ \hspace{4em} z_p \gets \mathopen{}\left( B_h \cdot L_h^{3} \mathclose{}\right)^{0.25} \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ j = \textrm{"zz"} \\ \hspace{5em} z_p \gets \mathopen{}\left( B_h^{3} \cdot L_h + B_h \cdot L_h^{3} \mathclose{}\right)^{0.25} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ z_p \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
z_p &= \text{Effective profile depth (m)}\\
j &= \text{Vibration mode}\\
B_h &= \text{Footing half width (m)}\\
L_h &= \text{Footing half length (m)}
\end{align*}
$$

#### `_get_embedment_factor_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_embedment\_factor\_scalar}(D_f, L_h, B_h, j, \mathrm{foundation\_is\_embedded}) \\ \hspace{1em} \mathbf{if} \ \mathrm{foundation\_is\_embedded} \\ \hspace{2em} \mathbf{return} \ \mathrm{None} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} η \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ j \in \mathopen{}\left( \textrm{"x"}, \textrm{"y"} \mathclose{}\right) \\ \hspace{2em} η \gets 1 + \mathopen{}\left( 0.33 + \frac{1.34}{1 + \frac{L_h}{B_h}} \mathclose{}\right) \mathopen{}\left( \frac{D_f}{B_h} \mathclose{}\right)^{0.8} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ j = \textrm{"z"} \\ \hspace{3em} η \gets 1 + \mathopen{}\left( 0.25 + \frac{0.25}{\frac{L_h}{B_h}} \mathclose{}\right) \mathopen{}\left( \frac{D_f}{B_h} \mathclose{}\right)^{0.8} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ j = \textrm{"xx"} \\ \hspace{4em} η \gets 1 + \frac{D_f}{B_h} + \frac{1.6}{0.35 + \frac{L_h}{B_h}} \cdot \mathopen{}\left( \frac{D_f}{B_h} \mathclose{}\right)^{2} \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ j = \textrm{"yy"} \\ \hspace{5em} η \gets 1 + \frac{D_f}{B_h} + \frac{1.6}{0.35 + \mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{4}} \mathopen{}\left( \frac{D_f}{B_h} \mathclose{}\right)^{2} \\ \hspace{4em} \mathbf{else} \\ \hspace{5em} \mathbf{if} \ j = \textrm{"zz"} \\ \hspace{6em} η \gets 1 + \mathopen{}\left( 1.3 + \frac{1.32}{\frac{L_h}{B_h}} \mathclose{}\right) \mathopen{}\left( \frac{D_f}{B_h} \mathclose{}\right)^{0.9} \\ \hspace{5em} \mathbf{end \ if} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ η \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
η &= \text{Embedment factor}\\
D_f &= \text{Footing embedment (m)}\\
L_h &= \text{Footing half length (m)}\\
B_h &= \text{Footing half width (m)}\\
j &= \text{Vibration mode}\\
\text{foundation\_is\_embedded} &= \text{Foundation is embedded}
\end{align*}
$$

#### `_get_pile_group_damping_ratio`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_pile\_group\_damping\_ratio}(a_0, j, \mathrm{pile\_group\_configuration}) \\ \hspace{1em} \mathbf{if} \ j = \textrm{"y"} \\ \hspace{2em} j \gets \textrm{"x"} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} β_G \gets \mathrm{SSI\_GROUP\_EFFECTS\_MAP}_{\textrm{"pile\_group\_damping\_ratio"}, j}.\mathrm{interpolate\_at\_x} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ β_G \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
β_G &= \text{Pile group damping ratio}\\
a_0 &= \text{Dimensionless frequency}\\
j &= \text{Vibration mode}\\
\text{pile\_group\_configuration} &= \text{Pile group configuration}
\end{align*}
$$

#### `_get_pile_group_efficiency_factor`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_pile\_group\_efficiency\_factor}(a_0, j, \mathrm{pile\_group\_configuration}) \\ \hspace{1em} \mathbf{if} \ j \in \mathopen{}\left[ \textrm{"x and y"}, \textrm{"y"} \mathclose{}\right] \\ \hspace{2em} j \gets \textrm{"x"} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} EF \gets \mathrm{SSI\_GROUP\_EFFECTS\_MAP}_{\textrm{"eff\_factor"}, j}.\mathrm{interpolate\_at\_x} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ EF \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
EF &= \text{Pile group efficiency factor}\\
a_0 &= \text{Dimensionless frequency}\\
j &= \text{Vibration mode}\\
\text{pile\_group\_configuration} &= \text{Pile group configuration}
\end{align*}
$$

#### `_get_radiation_damping_ratio_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_radiation\_damping\_ratio\_scalar}(G, L_h, B_h, a_0, α, K, j, \mathrm{foundation\_is\_embedded}, ψ, D_f) \\ \hspace{1em} β \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{foundation\_is\_embedded} \\ \hspace{2em} \mathbf{if} \ j \in \mathopen{}\left( \textrm{"x"}, \textrm{"y"} \mathclose{}\right) \\ \hspace{3em} β \gets \frac{4 \frac{L_h}{B_h}}{\frac{K}{G \cdot B_h}} \frac{a_0}{2 α} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ j = \textrm{"z"} \\ \hspace{4em} β \gets \frac{4 ψ \frac{L_h}{B_h}}{\frac{K}{G \cdot B_h}} \frac{a_0}{2 α} \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ j = \textrm{"xx"} \\ \hspace{5em} β \gets \frac{\frac{4 ψ}{3} \frac{L_h}{B_h} \cdot a_0^{2}}{\frac{K}{G \cdot B_h^{3}} \cdot \mathopen{}\left( 2.2 - \frac{0.4}{\mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{3}} + a_0^{2} \mathclose{}\right)} \frac{a_0}{2 α} \\ \hspace{4em} \mathbf{else} \\ \hspace{5em} \mathbf{if} \ j = \textrm{"yy"} \\ \hspace{6em} β \gets \frac{\frac{4 ψ}{3} \cdot \mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{3} a_0^{2}}{\frac{K}{G \cdot B_h^{3}} \cdot \mathopen{}\left( \frac{1.8}{1 + 1.75 \mathopen{}\left( \frac{L_h}{B_h} - 1 \mathclose{}\right)} + a_0^{2} \mathclose{}\right)} \frac{a_0}{2 α} \\ \hspace{5em} \mathbf{else} \\ \hspace{6em} \mathbf{if} \ j = \textrm{"zz"} \\ \hspace{7em} β \gets \frac{\frac{4}{3} \cdot \mathopen{}\left( \mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{3} + \frac{L_h}{B_h} \mathclose{}\right) a_0^{2}}{\frac{K}{G \cdot B_h^{3}} \cdot \mathopen{}\left( \frac{1.4}{1 + 3 \mathopen{}\left( \frac{L_h}{B_h} - 1 \mathclose{}\right)^{0.7}} + a_0^{2} \mathclose{}\right)} \frac{a_0}{2 α} \\ \hspace{6em} \mathbf{end \ if} \\ \hspace{5em} \mathbf{end \ if} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ j = \textrm{"x"} \\ \hspace{3em} β \gets \frac{4 \mathopen{}\left( \frac{L_h}{B_h} + \frac{D_f}{B_h} \cdot \mathopen{}\left( ψ + \frac{L_h}{B_h} \mathclose{}\right) \mathclose{}\right)}{\frac{K}{G \cdot B_h}} \frac{a_0}{2 α} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ j = \textrm{"y"} \\ \hspace{4em} β \gets \frac{4 \mathopen{}\left( \frac{L_h}{B_h} + \frac{D_f}{B_h} \cdot \mathopen{}\left( 1 + ψ \cdot \frac{L_h}{B_h} \mathclose{}\right) \mathclose{}\right)}{\frac{K}{G \cdot B_h}} \frac{a_0}{2 α} \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ j = \textrm{"z"} \\ \hspace{5em} β \gets \frac{4 \mathopen{}\left( ψ \cdot \frac{L_h}{B_h} + \frac{D_f}{B_h} \cdot \mathopen{}\left( 1 + \frac{L_h}{B_h} \mathclose{}\right) \mathclose{}\right)}{\frac{K}{G \cdot B_h}} \frac{a_0}{2 α} \\ \hspace{4em} \mathbf{else} \\ \hspace{5em} \mathbf{if} \ j = \textrm{"xx"} \\ \hspace{6em} β \gets \mathopen{}\left( \frac{\frac{4}{3} \cdot \mathopen{}\left( \frac{D_f}{B_h} + \mathopen{}\left( \frac{D_f}{B_h} \mathclose{}\right)^{3} + ψ \cdot \frac{L_h}{B_h} \cdot \mathopen{}\left( \frac{D_f}{B_h} \mathclose{}\right)^{3} + 3 \frac{D_f}{B_h} \frac{L_h}{B_h} + ψ \cdot \frac{L_h}{B_h} \mathclose{}\right) a_0^{2}}{\frac{K}{G \cdot B_h^{3}} \cdot \mathopen{}\left( \frac{1.8}{1 + 1.75 \mathopen{}\left( \frac{L_h}{B_h} - 1 \mathclose{}\right)} + a_0^{2} \mathclose{}\right)} + \frac{\frac{4}{3} \cdot \mathopen{}\left( ψ \cdot \frac{L_h}{B_h} + 1 \mathclose{}\right) \mathopen{}\left( \frac{D_f}{B_h} \mathclose{}\right)^{3}}{\frac{K}{G \cdot B_h^{3}}} \mathclose{}\right) \frac{a_0}{2 α} \\ \hspace{5em} \mathbf{else} \\ \hspace{6em} \mathbf{if} \ j = \textrm{"yy"} \\ \hspace{7em} β \gets \mathopen{}\left( \frac{\frac{4}{3} \cdot \mathopen{}\left( \mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{3} \frac{D_f}{B_h} + ψ \cdot \mathopen{}\left( \frac{D_f}{B_h} \mathclose{}\right)^{3} \frac{L_h}{B_h} + \mathopen{}\left( \frac{D_f}{B_h} \mathclose{}\right)^{3} + 3 \frac{D_f}{B_h} \cdot \mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{2} + ψ \cdot \mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{3} \mathclose{}\right) a_0^{2}}{\frac{K}{G \cdot B_h^{3}} \cdot \mathopen{}\left( \frac{1.8}{1 + 1.75 \mathopen{}\left( \frac{L_h}{B_h} - 1 \mathclose{}\right)} + a_0^{2} \mathclose{}\right)} + \frac{\frac{4}{3} \cdot \mathopen{}\left( \frac{L_h}{B_h} + ψ \mathclose{}\right) \mathopen{}\left( \frac{D_f}{B_h} \mathclose{}\right)^{3}}{\frac{K}{G \cdot B_h^{3}}} \mathclose{}\right) \frac{a_0}{2 α} \\ \hspace{6em} \mathbf{else} \\ \hspace{7em} \mathbf{if} \ j = \textrm{"zz"} \\ \hspace{8em} β \gets \frac{\frac{4}{3} \cdot \mathopen{}\left( 3 \frac{L_h}{B_h} \frac{D_f}{B_h} + ψ \cdot \mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{3} \frac{D_f}{B_h} + 3 \mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{2} \frac{D_f}{B_h} + ψ \cdot \frac{D_f}{B_h} + \mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{3} + \frac{L_h}{B_h} \mathclose{}\right) a_0^{2}}{\frac{K}{G \cdot B_h^{3}}} \cdot \mathopen{}\left( \frac{1.4}{1 + 3 \mathopen{}\left( \frac{L_h}{B_h} - 1 \mathclose{}\right)^{0.7}} + a_0^{2} \mathclose{}\right) \frac{a_0}{2 α} \\ \hspace{7em} \mathbf{end \ if} \\ \hspace{6em} \mathbf{end \ if} \\ \hspace{5em} \mathbf{end \ if} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ β \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
β &= \text{Radiation damping ratio}\\
G &= \text{Shear modulus (MPa)}\\
L_h &= \text{Footing half length (m)}\\
B_h &= \text{Footing half width (m)}\\
a_0 &= \text{Dimensionless frequency}\\
α &= \text{Dynamic stiffness modifier}\\
K &= \text{Static stiffness (MN/m or MN-m/rad)}\\
j &= \text{Vibration mode}\\
\text{foundation\_is\_embedded} &= \text{Foundation is embedded}\\
ψ &= \text{Poisson’s adjustment factor}\\
D_f &= \text{Footing embedment (m)}
\end{align*}
$$

#### `_get_static_stiffness_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_static\_stiffness\_scalar}(G, L_h, B_h, j, \mathrm{foundation\_is\_embedded}, ν, η) \\ \hspace{1em} K \gets \mathrm{np}.\mathrm{nan} \\ \hspace{1em} \mathbf{if} \ j = \textrm{"x"} \\ \hspace{2em} K \gets \frac{G \cdot B_h}{2 - ν} \cdot \mathopen{}\left( 6.8 \mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{0.65} + 2.4 \mathclose{}\right) \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ j = \textrm{"y"} \\ \hspace{3em} K \gets \frac{G \cdot B_h}{2 - ν} \cdot \mathopen{}\left( 6.8 \mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{0.65} + 0.8 \frac{L_h}{B_h} + 1.6 \mathclose{}\right) \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ j = \textrm{"z"} \\ \hspace{4em} K \gets \frac{G \cdot B_h}{1 - ν} \cdot \mathopen{}\left( 3.1 \mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{0.75} + 1.6 \mathclose{}\right) \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ j = \textrm{"xx"} \\ \hspace{5em} K \gets \frac{G \cdot B_h^{3}}{1 - ν} \cdot \mathopen{}\left( 3.2 \frac{L_h}{B_h} + 0.8 \mathclose{}\right) \\ \hspace{4em} \mathbf{else} \\ \hspace{5em} \mathbf{if} \ j = \textrm{"yy"} \\ \hspace{6em} K \gets \frac{G \cdot B_h^{3}}{1 - ν} \cdot \mathopen{}\left( 3.73 \mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{2.4} + 0.27 \mathclose{}\right) \\ \hspace{5em} \mathbf{else} \\ \hspace{6em} \mathbf{if} \ j = \textrm{"zz"} \\ \hspace{7em} K \gets G \cdot B_h^{3} \cdot \mathopen{}\left( 4.25 \mathopen{}\left( \frac{L_h}{B_h} \mathclose{}\right)^{2.45} + 4.06 \mathclose{}\right) \\ \hspace{6em} \mathbf{end \ if} \\ \hspace{5em} \mathbf{end \ if} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{if} \ \lnot \mathrm{foundation\_is\_embedded} \\ \hspace{2em} K \gets K \cdot η \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ K \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K &= \text{Static stiffness (MN/m or MN-m/rad)}\\
G &= \text{Shear modulus (MPa)}\\
L_h &= \text{Footing half length (m)}\\
B_h &= \text{Footing half width (m)}\\
j &= \text{Vibration mode}\\
\text{foundation\_is\_embedded} &= \text{Foundation is embedded}\\
ν &= \text{Poisson’s ratio}\\
η &= \text{Embedment factor}
\end{align*}
$$

#### `_get_stiffness_edge_factor_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_stiffness\_edge\_factor\_scalar}(R_e, k, k_z^i, B_h, L_h, j) \\ \hspace{1em} R_k \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ j = \textrm{"xx"} \\ \hspace{2em} \mathbf{if} \ R_e = 0 \\ \hspace{3em} R_k \gets 0 \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} R_k \gets \frac{\frac{3 k}{4 k_z^i \cdot B_h^{3} \cdot L_h} - \mathopen{}\left( 1 - R_e \mathclose{}\right)^{3}}{1 - \mathopen{}\left( 1 - R_e \mathclose{}\right)^{3}} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ j = \textrm{"yy"} \\ \hspace{3em} \mathbf{if} \ R_e = 0 \\ \hspace{4em} R_k \gets 0 \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} R_k \gets \frac{\frac{3 k}{4 k_z^i \cdot B_h \cdot L_h^{3}} - \mathopen{}\left( 1 - R_e \mathclose{}\right)^{3}}{1 - \mathopen{}\left( 1 - R_e \mathclose{}\right)^{3}} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ j = \textrm{"z"} \\ \hspace{4em} R_k \gets 1 \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ R_k \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
R_k &= \text{Stiffness edge factor}\\
R_e &= \text{End length ratio}\\
k &= \text{Stiffness (MN/m or MN-m/rad)}\\
k_z^i &= \text{Vertical stiffness intensity (MN/m3)}\\
B_h &= \text{Footing half width (m)}\\
L_h &= \text{Footing half length (m)}\\
j &= \text{Vibration mode}
\end{align*}
$$

#### `_get_stiffness_weight_factor_soil_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_stiffness\_weight\_factor\_soil\_scalar}(λL, Ω, j) \\ \hspace{1em} w_s \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ j = \textrm{"x"} \\ \hspace{2em} w_s \gets \frac{3}{4} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ j = \textrm{"z"} \\ \hspace{3em} w_s \gets \frac{-2 \mathopen{}\left( λL \cdot \mathopen{}\left( Ω^{2} - 1 \mathclose{}\right) + Ω \mathclose{}\right) + 2 Ω \cdot \cosh \mathopen{}\left( 2 λL \mathclose{}\right) + \mathopen{}\left( 1 + Ω^{2} \mathclose{}\right) \sinh \mathopen{}\left( 2 λL \mathclose{}\right)}{4 \mathopen{}\left( \cosh λL \mathclose{}\right)^{2} \mathopen{}\left( Ω + \tanh λL \mathclose{}\right) \mathopen{}\left( 1 + Ω \cdot \tanh λL \mathclose{}\right)} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ w_s \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
w_s &= \text{Stiffness weight factor soil}\\
λL &= \text{Dimensionless pile length parameter}\\
Ω &= \text{Dimensionless pile tip stiffness}\\
j &= \text{Vibration mode}
\end{align*}
$$

#### `_get_vibration_constant_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_vibration\_constant\_scalar}(E_p, E_s, δ, j, λL, Ω) \\ \hspace{1em} χ \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ j = \textrm{"x"} \\ \hspace{2em} χ \gets \frac{1}{2} \cdot \mathrm{np}.\pi^{\frac{1}{4}} \cdot δ^{\frac{3}{4}} \cdot \mathopen{}\left( \frac{E_p}{E_s} \mathclose{}\right)^{\frac{1}{4}} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ j = \textrm{"z"} \\ \hspace{3em} χ \gets \mathopen{}\left( \frac{\mathrm{np}.\pi \cdot δ}{2} \mathclose{}\right)^{\frac{1}{2}} \mathopen{}\left( \frac{E_p}{E_s} \mathclose{}\right)^{\frac{1}{2}} \frac{Ω + \tanh λL}{1 + Ω \cdot \tanh λL} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ χ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
χ &= \text{Vibration constant}\\
E_p &= \text{Pile elasticity modulus (MPa)}\\
E_s &= \text{Elasticity modulus (MPa)}\\
δ &= \text{Dimensionless subgrade reaction modulus}\\
j &= \text{Vibration mode}\\
λL &= \text{Dimensionless pile length parameter}\\
Ω &= \text{Dimensionless pile tip stiffness}
\end{align*}
$$

#### `get_active_pile_length`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_active\_pile\_length}(E_s, E_p, D, \mathrm{is\_homogeneous\_soil}) \\ \hspace{1em} \mathbf{if} \ \mathrm{is\_homogeneous\_soil} \\ \hspace{2em} \mathopen{}\left( χ, n \mathclose{}\right) \gets \mathopen{}\left( 2.4, 0.25 \mathclose{}\right) \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathopen{}\left( χ, n \mathclose{}\right) \gets \mathopen{}\left( 2.5, 0.2 \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} L_a \gets χ \cdot \mathopen{}\left( \frac{E_p}{E_s} \mathclose{}\right)^{n} D \\ \hspace{1em} \mathbf{return} \ L_a \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
L_a &= \text{Active pile length (m)}\\
E_s &= \text{Elasticity modulus (MPa)}\\
E_p &= \text{Pile elasticity modulus (MPa)}\\
D &= \text{Pile diameter (m)}\\
\text{is\_homogeneous\_soil} &= \text{Is homogeneous soil}
\end{align*}
$$

#### `get_average_bottom_depth`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_average\_bottom\_depth}(D_f, z_p) \\ \hspace{1em} z_{bottom} \gets D_f + z_p \\ \hspace{1em} \mathbf{return} \ z_{bottom} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
z_{bottom} &= \text{Average bottom depth (m)}\\
D_f &= \text{Footing embedment (m)}\\
z_p &= \text{Effective profile depth (m)}
\end{align*}
$$

#### `get_average_effective_shear_velocity`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_average\_effective\_shear\_velocity}(V_s, z, z_{top}, z_{bottom}, G/G_0, γ) \\ \hspace{1em} V_{s,avg} \gets \mathrm{\_get\_average\_effective\_shear\_velocity} \mathopen{}\left( V_s, z, z_{top}, z_{bottom} \mathclose{}\right) \\ \hspace{1em} V_{s,avg\ red} \gets V_{s,avg} \cdot \sqrt{ G/G_0 } \\ \hspace{1em} G \gets \mathrm{get\_small\_strain\_shear\_modulus\_\_landau1959theory} \mathopen{}\left( γ, V_{s,avg\ red} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( V_{s,avg}, V_{s,avg\ red}, G \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
V_{s,avg} &= \text{Average effective shear velocity (m/s)}\\
V_{s,avg\ red} &= \text{Average effective shear velocity reduced (m/s)}\\
G &= \text{Shear modulus (MPa)}\\
V_s &= \text{Shear velocity (m/s)}\\
z &= \text{Depth (m)}\\
z_{top} &= \text{Average top depth (m)}\\
z_{bottom} &= \text{Average bottom depth (m)}\\
G/G_0 &= \text{Shear modulus reduction factor}\\
γ &= \text{Unit weight (kN/m3)}
\end{align*}
$$

#### `get_average_effective_shear_velocity_xx`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_average\_effective\_shear\_velocity\_xx}(V_s, z, z_p) \\ \hspace{1em} \mathrm{average\_effective\_shear\_velocity\_xx} \gets \mathrm{get\_site\_class\_average} \mathopen{}\left( V_s, z \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{average\_effective\_shear\_velocity\_xx} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
V_{s,avg} &= \text{Average effective shear velocity (m/s)}\\
V_s &= \text{Shear velocity (m/s)}\\
z &= \text{Depth (m)}\\
z_p &= \text{Effective profile depth (rotation) (m)}
\end{align*}
$$

#### `get_average_top_depth`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_average\_top\_depth}(\mathrm{foundation\_is\_embedded}, D_f) \\ \hspace{1em} z_{top} \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( \mathrm{foundation\_is\_embedded}, D_f, 0 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ z_{top} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
z_{top} &= \text{Average top depth (m)}\\
\text{foundation\_is\_embedded} &= \text{Foundation is embedded}\\
D_f &= \text{Footing embedment (m)}
\end{align*}
$$

#### `get_dashpot_coefficient`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_dashpot\_coefficient}(k, β, β_s, ω) \\ \hspace{1em} c \gets 2 k \frac{β + β_s}{ω} \\ \hspace{1em} \mathbf{return} \ c \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
c &= \text{Dashpot coefficient (MN-s/m or MN-m/rad)}\\
k &= \text{Stiffness (MN/m or MN-m/rad)}\\
β &= \text{Radiation damping ratio}\\
β_s &= \text{Soil damping ratio}\\
ω &= \text{Natural frequency (rad/s)}
\end{align*}
$$

#### `get_dashpot_coefficient_intensity`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_dashpot\_coefficient\_intensity}(c_z^i, R_k, R_c) \\ \hspace{1em} ci \gets c_z^i \cdot R_k \cdot R_c \\ \hspace{1em} \mathbf{return} \ ci \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ci &= \text{Dashpot coefficient intensity (MN-s/m3)}\\
c_z^i &= \text{Dashpot coefficient intensity vertical (MN-s/m3)}\\
R_k &= \text{Stiffness edge factor}\\
R_c &= \text{Dashpot edge factor}
\end{align*}
$$

#### `get_dashpot_coefficient_intensity_vertical`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_dashpot\_coefficient\_intensity\_vertical}(j, c, B_h, L_h) \\ \hspace{1em} \mathrm{dashpot\_coefficient\_map} \gets \mathrm{dict} \mathopen{}\left( \mathrm{zip} \mathopen{}\left( \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( j \mathclose{}\right), \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( c \mathclose{}\right) \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} c_z \gets \mathrm{dashpot\_coefficient\_map}_{\textrm{"z"}} \\ \hspace{1em} c_z^i \gets \frac{c_z}{4 B_h \cdot L_h} \\ \hspace{1em} \mathbf{return} \ c_z^i \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
c_z^i &= \text{Dashpot coefficient intensity vertical (MN-s/m3)}\\
j &= \text{Vibration mode}\\
c &= \text{Dashpot coefficient (MN-s/m or MN-m/rad)}\\
B_h &= \text{Footing half width (m)}\\
L_h &= \text{Footing half length (m)}
\end{align*}
$$

#### `get_dashpot_edge_factor`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_dashpot\_edge\_factor}(R_e, c, R_k, c_z^i, B_h, L_h, j) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_dashpot\_edge\_factor\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
R_c &= \text{Dashpot edge factor}\\
R_e &= \text{End length ratio}\\
c &= \text{Dashpot coefficient (MN-s/m or MN-m/rad)}\\
R_k &= \text{Stiffness edge factor}\\
c_z^i &= \text{Dashpot coefficient intensity vertical (MN-s/m3)}\\
B_h &= \text{Footing half width (m)}\\
L_h &= \text{Footing half length (m)}\\
j &= \text{Vibration mode}
\end{align*}
$$

#### `get_dimensionless_frequency`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_dimensionless\_frequency}(ω, B_h, V_{s,avg\ red}) \\ \hspace{1em} a_0 \gets \frac{ω \cdot B_h}{V_{s,avg\ red}} \\ \hspace{1em} \mathbf{return} \ a_0 \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
a_0 &= \text{Dimensionless frequency}\\
ω &= \text{Natural frequency (rad/s)}\\
B_h &= \text{Footing half width (m)}\\
V_{s,avg\ red} &= \text{Average effective shear velocity reduced (m/s)}
\end{align*}
$$

#### `get_dimensionless_frequency_pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_dimensionless\_frequency\_pile}(ω, D, V_{s,avg\ red}) \\ \hspace{1em} a_0 \gets \frac{ω \cdot D}{V_{s,avg\ red}} \\ \hspace{1em} \mathbf{return} \ a_0 \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
a_0 &= \text{Dimensionless frequency}\\
ω &= \text{Natural frequency (rad/s)}\\
D &= \text{Pile diameter (m)}\\
V_{s,avg\ red} &= \text{Average effective shear velocity reduced (m/s)}
\end{align*}
$$

#### `get_dimensionless_pile_length_parameter`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_dimensionless\_pile\_length\_parameter}(E_p, E_s, δ, D, L, j) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_dimensionless\_pile\_length\_parameter\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
λL &= \text{Dimensionless pile length parameter}\\
E_p &= \text{Pile elasticity modulus (MPa)}\\
E_s &= \text{Elasticity modulus (MPa)}\\
δ &= \text{Dimensionless subgrade reaction modulus}\\
D &= \text{Pile diameter (m)}\\
L &= \text{Pile embedment length (m)}\\
j &= \text{Vibration mode}
\end{align*}
$$

#### `get_dimensionless_pile_length_parameter_ksd`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_dimensionless\_pile\_length\_parameter\_ksd}(E_p, I_p, j, k_{sd}) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_dimensionless\_pile\_length\_parameter\_ksd\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
λL &= \text{Dimensionless pile length parameter}\\
E_p &= \text{Pile elasticity modulus (MPa)}\\
I_p &= \text{Pile moment of inertia (m4)}\\
j &= \text{Vibration mode}\\
k_{sd} &= \text{Subgrade reaction modulus at diameter (MPa)}
\end{align*}
$$

#### `get_dimensionless_pile_tip_stiffness`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_dimensionless\_pile\_tip\_stiffness}(E_p, E_s, δ, ν, j) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_dimensionless\_pile\_tip\_stiffness\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Ω &= \text{Dimensionless pile tip stiffness}\\
E_p &= \text{Pile elasticity modulus (MPa)}\\
E_s &= \text{Elasticity modulus (MPa)}\\
δ &= \text{Dimensionless subgrade reaction modulus}\\
ν &= \text{Poisson’s ratio}\\
j &= \text{Vibration mode}
\end{align*}
$$

#### `get_dimensionless_subgrade_reaction_modulus`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_dimensionless\_subgrade\_reaction\_modulus}(E_p, E_s, j) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_dimensionless\_subgrade\_reaction\_modulus\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
δ &= \text{Dimensionless subgrade reaction modulus}\\
E_p &= \text{Pile elasticity modulus (MPa)}\\
E_s &= \text{Elasticity modulus (MPa)}\\
j &= \text{Vibration mode}
\end{align*}
$$

#### `get_displacement_rotation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_displacement\_rotation}(K_{hh}, K_{rr}, K_{hr}, \mathrm{pile\_head\_lateral\_load}, \mathrm{pile\_head\_moment}) \\ \hspace{1em} \mathrm{stiffness\_matrix\_inverted} \gets \frac{1}{K_{hh} \cdot K_{rr} - K_{hr}^{2}} \cdot \begin{bmatrix} K_{rr}.\mathrm{item} \mathopen{}\left( \mathclose{}\right) & -K_{hr}.\mathrm{item} \mathopen{}\left( \mathclose{}\right) \\ -K_{hr}.\mathrm{item} \mathopen{}\left( \mathclose{}\right) & K_{hh}.\mathrm{item} \mathopen{}\left( \mathclose{}\right) \end{bmatrix} \\ \hspace{1em} \mathopen{}\left( u, θ \mathclose{}\right) \gets \mathrm{np}.\mathrm{matmul} \mathopen{}\left( \mathrm{stiffness\_matrix\_inverted}, \begin{bmatrix} \mathrm{pile\_head\_lateral\_load}.\mathrm{item} \mathopen{}\left( \mathclose{}\right) \\ \mathrm{pile\_head\_moment}.\mathrm{item} \mathopen{}\left( \mathclose{}\right) \end{bmatrix} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( u, θ \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
u &= \text{Pile head displacement (m)}\\
θ &= \text{Pile head rotation (rad)}\\
K_{hh} &= \text{Pile swaying stiffness (kN/m)}\\
K_{rr} &= \text{Pile rocking stiffness (kN-m/rad)}\\
K_{hr} &= \text{Pile cross-swaying-rocking stiffness (kN/m or kN-m/rad)}\\
\text{pile\_head\_lateral\_load} &= \text{Pile head lateral load (kN)}\\
\text{pile\_head\_moment} &= \text{Pile head moment (kN-m)}
\end{align*}
$$

#### `get_dynamic_stiffness_modifier`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_dynamic\_stiffness\_modifier}(a_0, L_h, B_h, j) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_dynamic\_stiffness\_modifier\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
α &= \text{Dynamic stiffness modifier}\\
a_0 &= \text{Dimensionless frequency}\\
L_h &= \text{Footing half length (m)}\\
B_h &= \text{Footing half width (m)}\\
j &= \text{Vibration mode}
\end{align*}
$$

#### `get_dynamic_stiffness_modifier_pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_dynamic\_stiffness\_modifier\_pile}(δ, γ_p, γ, ν, a_0, j, w_s) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_dynamic\_stiffness\_modifier\_pile\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
α &= \text{Dynamic stiffness modifier}\\
δ &= \text{Dimensionless subgrade reaction modulus}\\
γ_p &= \text{Pile unit weight (kN/m3)}\\
γ &= \text{Unit weight (kN/m3)}\\
ν &= \text{Poisson’s ratio}\\
a_0 &= \text{Dimensionless frequency}\\
j &= \text{Vibration mode}\\
w_s &= \text{Stiffness weight factor soil}
\end{align*}
$$

#### `get_effective_profile_depth`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_effective\_profile\_depth}(j, B_h, L_h) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_effective\_profile\_depth\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
z_p &= \text{Effective profile depth (m)}\\
j &= \text{Vibration mode}\\
B_h &= \text{Footing half width (m)}\\
L_h &= \text{Footing half length (m)}
\end{align*}
$$

#### `get_effective_profile_depth_pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_effective\_profile\_depth\_pile}(j, L, L_a) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_effective\_profile\_depth\_pile\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
z_p &= \text{Effective profile depth (m)}\\
j &= \text{Vibration mode}\\
L &= \text{Pile embedment length (m)}\\
L_a &= \text{Active pile length (m)}
\end{align*}
$$

#### `get_effective_profile_depth_rotation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_effective\_profile\_depth\_rotation}(D_f, B_h, L_h) \\ \hspace{1em} z_p \gets D_f + \mathrm{\_get\_effective\_profile\_depth\_scalar} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ z_p \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
z_p &= \text{Effective profile depth (rotation) (m)}\\
D_f &= \text{Footing embedment (m)}\\
B_h &= \text{Footing half width (m)}\\
L_h &= \text{Footing half length (m)}
\end{align*}
$$

#### `get_elasticity_modulus_z`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_elasticity\_modulus\_z}(E_s, z, D, a, n, \mathrm{soil\_profile\_shape}) \\ \hspace{1em} \mathbf{if} \ \mathrm{soil\_profile\_shape} = \textrm{"linear"} \\ \hspace{2em} n \gets 1 \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathrm{elasticity\_modulus\_z} \gets E_s \cdot \mathopen{}\left( a + \frac{\mathopen{}\left( 1 - a \mathclose{}\right) z}{D} \mathclose{}\right)^{n} \\ \hspace{1em} \mathbf{return} \ \mathrm{elasticity\_modulus\_z} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
E_s &= \text{Elasticity modulus (MPa)}\\
z &= \text{Depth (m)}\\
D &= \text{Pile diameter (m)}\\
a &= \text{Inhomogeneity alpha}\\
n &= \text{Inhomogeneity exponent}\\
\text{soil\_profile\_shape} &= \text{Soil profile shape}
\end{align*}
$$

#### `get_embedment_factor`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_embedment\_factor}(D_f, L_h, B_h, j, \mathrm{foundation\_is\_embedded}) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_embedment\_factor\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
η &= \text{Embedment factor}\\
D_f &= \text{Footing embedment (m)}\\
L_h &= \text{Footing half length (m)}\\
B_h &= \text{Footing half width (m)}\\
j &= \text{Vibration mode}\\
\text{foundation\_is\_embedded} &= \text{Foundation is embedded}
\end{align*}
$$

#### `get_footing_half_length`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_footing\_half\_length}(L) \\ \hspace{1em} L_h \gets \frac{L}{2} \\ \hspace{1em} \mathbf{return} \ L_h \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
L_h &= \text{Footing half length (m)}\\
L &= \text{Footing length (m)}
\end{align*}
$$

#### `get_footing_half_width`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_footing\_half\_width}(B) \\ \hspace{1em} B_h \gets \frac{B}{2} \\ \hspace{1em} \mathbf{return} \ B_h \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
B_h &= \text{Footing half width (m)}\\
B &= \text{Footing width (m)}
\end{align*}
$$

#### `get_footing_router`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_footing\_router}() \\ \hspace{1em} j_{group} \gets \mathopen{}\left[ \textrm{"x overall"}, \textrm{"y overall"}, \textrm{"x base spring"}, \textrm{"y base spring"}, \textrm{"z"}, \textrm{"xx"}, \textrm{"yy"}, \textrm{"zz"} \mathclose{}\right] \\ \hspace{1em} j \gets \mathopen{}\left[ \textrm{"x"}, \textrm{"y"}, \textrm{"x"}, \textrm{"y"}, \textrm{"z"}, \textrm{"xx"}, \textrm{"yy"}, \textrm{"zz"} \mathclose{}\right] \\ \hspace{1em} \mathrm{foundation\_is\_embedded} \gets \mathopen{}\left[ \mathrm{False}, \mathrm{False}, \mathrm{True}, \mathrm{True}, \mathrm{False}, \mathrm{False}, \mathrm{False}, \mathrm{False} \mathclose{}\right] \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( j_{group}, j, \mathrm{foundation\_is\_embedded} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
j_{group} &= \text{Vibration mode group}\\
j &= \text{Vibration mode}\\
\text{foundation\_is\_embedded} &= \text{Foundation is embedded}
\end{align*}
$$

#### `get_footing_zone`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_footing\_zone}(j, k, c) \\ \hspace{1em} \mathrm{stiffness\_map} \gets \mathrm{dict} \mathopen{}\left( \mathrm{zip} \mathopen{}\left( \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( j \mathclose{}\right), \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( k \mathclose{}\right) \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathrm{dashpot\_coefficient\_map} \gets \mathrm{dict} \mathopen{}\left( \mathrm{zip} \mathopen{}\left( \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( j \mathclose{}\right), \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( c \mathclose{}\right) \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} j \gets \mathopen{}\left[ \textrm{"z"}, \textrm{"xx"}, \textrm{"yy"}, \textrm{"xx and yy"} \mathclose{}\right] \\ \hspace{1em} k \gets \mathopen{}\left[ \mathrm{stiffness\_map}.\mathrm{get} \mathopen{}\left( k \mathclose{}\right) \mid k \in j \mathclose{}\right] \\ \hspace{1em} c \gets \mathopen{}\left[ \mathrm{dashpot\_coefficient\_map}.\mathrm{get} \mathopen{}\left( k \mathclose{}\right) \mid k \in j \mathclose{}\right] \\ \hspace{1em} \mathrm{footing\_zone} \gets \mathopen{}\left[ \textrm{"center"}, \textrm{"y edge"}, \textrm{"x edge"}, \textrm{"corner"} \mathclose{}\right] \\ \hspace{1em} \mathrm{color} \gets \mathopen{}\left[ \textrm{"grey"}, \textrm{"dodgerblue"}, \textrm{"yellow"}, \textrm{"red"} \mathclose{}\right] \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( \mathrm{footing\_zone}, \mathrm{color}, j, k, c \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{footing\_zone} &= \text{Footing zone}\\
j &= \text{Vibration mode}\\
k &= \text{Stiffness (MN/m or MN-m/rad)}\\
c &= \text{Dashpot coefficient (MN-s/m or MN-m/rad)}
\end{align*}
$$

#### `get_natural_frequency`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_natural\_frequency}(T_{flexible}) \\ \hspace{1em} ω \gets \frac{2 \mathrm{np}.\pi}{T_{flexible}} \\ \hspace{1em} \mathbf{return} \ ω \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ω &= \text{Natural frequency (rad/s)}\\
T_{flexible} &= \text{Structure flexible period (s)}
\end{align*}
$$

#### `get_period_lengthening_ratio`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_period\_lengthening\_ratio}(h/{V_s\ T}, h, B_h) \\ \hspace{1em} \mathrm{height\_width\_ratio} \gets \frac{h}{B_h} \\ \hspace{1em} T_{flexible}/T \gets \mathrm{PeriodLengtheningRatioFigure}.\mathrm{interpolate\_at\_x} \mathopen{}\left( \mathclose{}\right).\mathrm{item} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ T_{flexible}/T \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
T_{flexible}/T &= \text{Period lengthening ratio}\\
h/{V_s\ T} &= \text{Structure-to-soil stiffness ratio}\\
h &= \text{Structure effective modal height (m)}\\
B_h &= \text{Footing half width (m)}
\end{align*}
$$

#### `get_pile_cross_swaying_rocking_stiffness`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_cross\_swaying\_rocking\_stiffness}(E_p, I_p, μ, k_{sd}, D, \mathrm{soil\_profile\_shape}, a, n) \\ \hspace{1em} K_{hr} \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{soil\_profile\_shape} = \textrm{"linear"} \\ \hspace{2em} \mathbf{if} \ a = 1 \\ \hspace{3em} K_{hr} \gets 2 E_p \cdot I_p \cdot μ^{2} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} K_{hr} \gets E_p \cdot I_p \cdot μ^{2} + \frac{k_{sd}}{16 D \cdot μ^{3}} \cdot \mathopen{}\left( 3 + a \cdot \mathopen{}\left( 4 D \cdot μ - 3 \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{soil\_profile\_shape} = \textrm{"parabolic"} \\ \hspace{3em} K_{hr} \gets E_p \cdot I_p \cdot μ^{2} + k_{sd} \cdot 2^{\frac{-9 - 3 n}{2}} \cdot \mathopen{}\left( \frac{1}{μ \cdot D} \mathclose{}\right)^{n} \frac{\Gamma \mathopen{}\left( 1 + n \mathclose{}\right)}{μ^{2}} \mathopen{}\left( 2^{\frac{5 + n}{2}} - 4 \cos \mathopen{}\left( \frac{\mathopen{}\left( 1 + n \mathclose{}\right) \mathrm{np}.\pi}{4} \mathclose{}\right) + 4 \sin \mathopen{}\left( \frac{\mathopen{}\left( 1 + n \mathclose{}\right) \mathrm{np}.\pi}{4} \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ K_{hr} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K_{hr} &= \text{Pile cross-swaying-rocking stiffness (kN/m or kN-m/rad)}\\
E_p &= \text{Pile elasticity modulus (MPa)}\\
I_p &= \text{Pile moment of inertia (m4)}\\
μ &= \text{Shape parameter}\\
k_{sd} &= \text{Subgrade reaction modulus at diameter (MPa)}\\
D &= \text{Pile diameter (m)}\\
\text{soil\_profile\_shape} &= \text{Soil profile shape}\\
a &= \text{Inhomogeneity alpha}\\
n &= \text{Inhomogeneity exponent}
\end{align*}
$$

#### `get_pile_elasticity_modulus_solid_from_tubular_section`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_elasticity\_modulus\_solid\_from\_tubular\_section}(E_p, t, D) \\ \hspace{1em} E_p \gets E_p \cdot \mathopen{}\left( 1 - \mathopen{}\left( 1 - \frac{2 t}{D} \mathclose{}\right)^{1} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ E_p \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
E_p &= \text{Pile elasticity modulus (MPa)}\\
t &= \text{Pile wall thickness (m)}\\
D &= \text{Pile diameter (m)}
\end{align*}
$$

#### `get_pile_group_damping_ratio`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_group\_damping\_ratio}(a_0, j, \mathrm{pile\_group\_configuration}) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_pile\_group\_damping\_ratio\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
β_G &= \text{Pile group damping ratio}\\
a_0 &= \text{Dimensionless frequency}\\
j &= \text{Vibration mode}\\
\text{pile\_group\_configuration} &= \text{Pile group configuration}
\end{align*}
$$

#### `get_pile_group_efficiency_factor`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_group\_efficiency\_factor}(a_0, j, \mathrm{pile\_group\_configuration}) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_pile\_group\_efficiency\_factor} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
EF &= \text{Pile group efficiency factor}\\
a_0 &= \text{Dimensionless frequency}\\
j &= \text{Vibration mode}\\
\text{pile\_group\_configuration} &= \text{Pile group configuration}
\end{align*}
$$

#### `get_pile_moment_of_inertia`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_moment\_of\_inertia}(D, \mathrm{pile\_shape}) \\ \hspace{1em} I_p \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{pile\_shape} \in \mathopen{}\left( \textrm{"tubular"}, \textrm{"circle"} \mathclose{}\right) \\ \hspace{2em} I_p \gets \frac{\mathrm{np}.\pi \cdot D^{4}}{64} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ I_p \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
I_p &= \text{Pile moment of inertia (m4)}\\
D &= \text{Pile diameter (m)}\\
\text{pile\_shape} &= \text{Pile shape}
\end{align*}
$$

#### `get_pile_rocking_stiffness`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_rocking\_stiffness}(E_p, I_p, μ, k_{sd}, D, \mathrm{soil\_profile\_shape}, a, n) \\ \hspace{1em} K_{rr} \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{soil\_profile\_shape} = \textrm{"linear"} \\ \hspace{2em} \mathbf{if} \ a = 1 \\ \hspace{3em} K_{rr} \gets 2 E_p \cdot I_p \cdot μ \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} K_{rr} \gets \frac{3}{2} \cdot E_p \cdot I_p \cdot μ + \frac{k_{sd}}{8 D \cdot μ^{4}} \cdot \mathopen{}\left( 1 + a \cdot \mathopen{}\left( D \cdot μ - 1 \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{soil\_profile\_shape} = \textrm{"parabolic"} \\ \hspace{3em} K_{rr} \gets \frac{3}{2} \cdot E_p \cdot I_p \cdot μ + k_{sd} \cdot 2^{\frac{-9 - 3 n}{2}} \cdot \mathopen{}\left( \frac{1}{μ \cdot D} \mathclose{}\right)^{n} \frac{\Gamma \mathopen{}\left( 1 + n \mathclose{}\right)}{μ^{3}} \mathopen{}\left( 2^{\frac{5 + n}{2}} - 4 \cos \mathopen{}\left( \frac{\mathopen{}\left( 1 + n \mathclose{}\right) \mathrm{np}.\pi}{4} \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ K_{rr} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K_{rr} &= \text{Pile rocking stiffness (kN-m/rad)}\\
E_p &= \text{Pile elasticity modulus (MPa)}\\
I_p &= \text{Pile moment of inertia (m4)}\\
μ &= \text{Shape parameter}\\
k_{sd} &= \text{Subgrade reaction modulus at diameter (MPa)}\\
D &= \text{Pile diameter (m)}\\
\text{soil\_profile\_shape} &= \text{Soil profile shape}\\
a &= \text{Inhomogeneity alpha}\\
n &= \text{Inhomogeneity exponent}
\end{align*}
$$

#### `get_pile_router`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_router}() \\ \hspace{1em} j_{group} \gets \mathopen{}\left[ \textrm{"x and y"}, \textrm{"z"} \mathclose{}\right] \\ \hspace{1em} j \gets \mathopen{}\left[ \textrm{"x"}, \textrm{"z"} \mathclose{}\right] \\ \hspace{1em} \mathrm{foundation\_is\_embedded} \gets \mathopen{}\left[ \mathrm{True}, \mathrm{True} \mathclose{}\right] \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( j_{group}, j, \mathrm{foundation\_is\_embedded} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
j_{group} &= \text{Vibration mode group}\\
j &= \text{Vibration mode}\\
\text{foundation\_is\_embedded} &= \text{Foundation is embedded}
\end{align*}
$$

#### `get_pile_stiffness_in_group`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_stiffness\_in\_group}(EF, k_p) \\ \hspace{1em} k_{pG} \gets EF \cdot k_p \\ \hspace{1em} \mathbf{return} \ k_{pG} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
k_{pG} &= \text{Pile stiffness in group (MN/m or MN-m/rad)}\\
EF &= \text{Pile group efficiency factor}\\
k_p &= \text{Pile stiffness (MN/m or MN-m/rad)}
\end{align*}
$$

#### `get_pile_swaying_stiffness`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_swaying\_stiffness}(E_p, I_p, μ, k_{sd}, D, \mathrm{soil\_profile\_shape}, a, n) \\ \hspace{1em} K_{hh} \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{soil\_profile\_shape} = \textrm{"linear"} \\ \hspace{2em} \mathbf{if} \ a = 1 \\ \hspace{3em} K_{hh} \gets 4 E_p \cdot I_p \cdot μ^{3} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} K_{hh} \gets E_p \cdot I_p \cdot μ^{3} + \frac{3 k_{sd}}{8 D \cdot μ^{2}} \cdot \mathopen{}\left( 1 + a \cdot \mathopen{}\left( 2 D \cdot μ - 1 \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{soil\_profile\_shape} = \textrm{"parabolic"} \\ \hspace{3em} K_{hh} \gets E_p \cdot I_p \cdot μ^{3} + k_{sd} \cdot 2^{\frac{-5 - 3 n}{2}} \cdot \mathopen{}\left( \frac{1}{μ \cdot D} \mathclose{}\right)^{n} \frac{\Gamma \mathopen{}\left( 1 + n \mathclose{}\right)}{μ} \mathopen{}\left( 2^{\frac{3 + n}{2}} + 2 \sin \mathopen{}\left( \frac{\mathopen{}\left( 1 + n \mathclose{}\right) \mathrm{np}.\pi}{4} \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ K_{hh} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K_{hh} &= \text{Pile swaying stiffness (kN/m)}\\
E_p &= \text{Pile elasticity modulus (MPa)}\\
I_p &= \text{Pile moment of inertia (m4)}\\
μ &= \text{Shape parameter}\\
k_{sd} &= \text{Subgrade reaction modulus at diameter (MPa)}\\
D &= \text{Pile diameter (m)}\\
\text{soil\_profile\_shape} &= \text{Soil profile shape}\\
a &= \text{Inhomogeneity alpha}\\
n &= \text{Inhomogeneity exponent}
\end{align*}
$$

#### `get_poisson_adjustment_factor`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_poisson\_adjustment\_factor}(ν) \\ \hspace{1em} ψ \gets \sqrt{ \frac{2 \mathopen{}\left( 1 - ν \mathclose{}\right)}{1 - 2 ν} } \\ \hspace{1em} ψ \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( ψ, \mathrm{None}, 2.5 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ ψ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ψ &= \text{Poisson’s adjustment factor}\\
ν &= \text{Poisson’s ratio}
\end{align*}
$$

#### `get_radiation_damping_ratio`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_radiation\_damping\_ratio}(G, L_h, B_h, a_0, α, K, j, \mathrm{foundation\_is\_embedded}, ψ, D_f) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_radiation\_damping\_ratio\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
β &= \text{Radiation damping ratio}\\
G &= \text{Shear modulus (MPa)}\\
L_h &= \text{Footing half length (m)}\\
B_h &= \text{Footing half width (m)}\\
a_0 &= \text{Dimensionless frequency}\\
α &= \text{Dynamic stiffness modifier}\\
K &= \text{Static stiffness (MN/m or MN-m/rad)}\\
j &= \text{Vibration mode}\\
\text{foundation\_is\_embedded} &= \text{Foundation is embedded}\\
ψ &= \text{Poisson’s adjustment factor}\\
D_f &= \text{Footing embedment (m)}
\end{align*}
$$

#### `get_radiation_damping_ratio_rx`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_radiation\_damping\_ratio\_rx}(α, δ, ν, a_0) \\ \hspace{1em} β \gets \frac{3}{2 α \cdot \mathopen{}\left( 1 + ν \mathclose{}\right) δ} \cdot a_0^{\frac{3}{4}} \\ \hspace{1em} \mathbf{return} \ β \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
β &= \text{Radiation damping ratio}\\
α &= \text{Dynamic stiffness modifier}\\
δ &= \text{Dimensionless subgrade reaction modulus}\\
ν &= \text{Poisson’s ratio}\\
a_0 &= \text{Dimensionless frequency}
\end{align*}
$$

#### `get_response_embedment_modification__lizundia2020practical`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_response\_embedment\_modification\_\_lizundia2020practical}(D_f, V_{s,avg}, T) \\ \hspace{1em} T \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( T, 0.2, \mathrm{None} \mathclose{}\right) \\ \hspace{1em} RRS_e \gets 0.25 + 0.75 \cos \mathopen{}\left( \frac{2 \mathrm{np}.\pi \cdot D_f}{T \cdot V_{s,avg}} \mathclose{}\right) \\ \hspace{1em} RRS_e \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( RRS_e, 0.7, \mathrm{None} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ RRS_e \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
RRS_e &= \text{Response embedment modification}\\
D_f &= \text{Footing embedment (m)}\\
V_{s,avg} &= \text{Average effective shear velocity (m/s)}\\
T &= \text{Period (s)}
\end{align*}
$$

#### `get_shape_parameter`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shape\_parameter}(L_a, D, λL, \mathrm{soil\_profile\_shape}, a, n) \\ \hspace{1em} μ \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{soil\_profile\_shape} = \textrm{"linear"} \\ \hspace{2em} \mathbf{if} \ a = 1 \\ \hspace{3em} μ \gets λL \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} μ \gets \frac{4 λL}{5 D^{\frac{1}{4}} \cdot L_a \cdot \mathopen{}\left( a - 1 \mathclose{}\right)} \mathopen{}\left( \mathopen{}\left( a \cdot D \mathclose{}\right)^{\frac{5}{4}} - \mathopen{}\left( a \cdot D - a \cdot L_a + L_a \mathclose{}\right)^{\frac{5}{4}} \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{soil\_profile\_shape} = \textrm{"parabolic"} \\ \hspace{3em} μ \gets \frac{4}{4 + n} \cdot \mathopen{}\left( \frac{L_a}{D} \mathclose{}\right)^{\frac{n}{4}} λL \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ μ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
μ &= \text{Shape parameter}\\
L_a &= \text{Active pile length (m)}\\
D &= \text{Pile diameter (m)}\\
λL &= \text{Dimensionless pile length parameter}\\
\text{soil\_profile\_shape} &= \text{Soil profile shape}\\
a &= \text{Inhomogeneity alpha}\\
n &= \text{Inhomogeneity exponent}
\end{align*}
$$

#### `get_site_class_average`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_site\_class\_average}(\mathrm{values\_to\_average}, z, z_{top}, z_{bottom}) \\ \hspace{1em} \mathrm{values\_to\_average} \gets \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( \mathrm{values\_to\_average} \mathclose{}\right) \\ \hspace{1em} z \gets \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( z \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ \mathrm{is\_null} \mathopen{}\left( z_{bottom} \mathclose{}\right) \\ \hspace{2em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"average\_bottom\_depth is null"} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathrm{valid\_flag} \gets \mathopen{}\left( \mathrm{values\_to\_average} > 0 \mathclose{}\right) \mathbin{\&} \mathord{\sim} \mathrm{is\_null} \mathopen{}\left( \mathrm{values\_to\_average} \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ \mathrm{np}.\mathrm{any} \mathopen{}\left( \mathord{\sim} \mathrm{valid\_flag} \mathclose{}\right) \\ \hspace{2em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"site\_class\_average: only positive, non-null values supported"} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathrm{depth\_valid} \gets \mathrm{np}.\mathrm{extract} \mathopen{}\left( \mathrm{valid\_flag}, z \mathclose{}\right) \\ \hspace{1em} \mathrm{depth\_max} \gets \mathrm{np}.\mathrm{max} \mathopen{}\left( \mathrm{depth\_valid} \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ z_{bottom} > \mathrm{depth\_max} \\ \hspace{2em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"average\_bottom\_depth=\{\} is greater than depth\_max=\{\}"}.\mathrm{format} \mathopen{}\left( z_{bottom}, \mathrm{depth\_max} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathrm{depth\_in\_window} \gets \mathrm{np}.\mathrm{r\_}_{\mathopen{}\left( z_{top}, \mathrm{np}.\mathrm{extract} \mathopen{}\left( \mathopen{}\left( \mathrm{depth\_valid} > z_{top} \mathclose{}\right) \mathbin{\&} \mathopen{}\left( \mathrm{depth\_valid} < z_{bottom} \mathclose{}\right), \mathrm{depth\_valid} \mathclose{}\right), z_{bottom} \mathclose{}\right)} \\ \hspace{1em} \mathrm{values\_to\_average\_in\_window} \gets \mathrm{values\_to\_average}_{\mathrm{np}.\mathrm{searchsorted} \mathopen{}\left( \mathrm{depth\_valid}, \mathrm{depth\_in\_window} \mathclose{}\right)} \\ \hspace{1em} H \gets \mathrm{get\_thickness} \mathopen{}\left( \mathrm{depth\_in\_window} - z_{top} \mathclose{}\right) \\ \hspace{1em} \mathrm{site\_class\_average} \gets \frac{\sum H}{\sum \mathopen{}\left( \frac{H}{\mathrm{values\_to\_average\_in\_window}} \mathclose{}\right)} \\ \hspace{1em} \mathbf{return} \ \mathrm{site\_class\_average} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{site\_class\_average} &= \text{Site class average}\\
\text{values\_to\_average} &= \text{Values to average}\\
z &= \text{Depth (m)}\\
z_{top} &= \text{Average top depth (m)}\\
z_{bottom} &= \text{Average bottom depth (m)}
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

#### `get_square_equivalent_circle_diameter`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_square\_equivalent\_circle\_diameter}(D) \\ \hspace{1em} D \gets 2 \mathopen{}\left( \frac{D^{2}}{\mathrm{np}.\pi} \mathclose{}\right)^{0.5} \\ \hspace{1em} \mathbf{return} \ D \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
D &= \text{Pile diameter (m)}
\end{align*}
$$

#### `get_ssi_effects_expected`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_ssi\_effects\_expected}(h/{V_s\ T}) \\ \hspace{1em} \mathrm{ssi\_effects\_expected} \gets h/{V_s\ T} > 0.1 \\ \hspace{1em} \mathbf{return} \ \mathrm{ssi\_effects\_expected} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{ssi\_effects\_expected} &= \text{SSI effects expected}\\
h/{V_s\ T} &= \text{Structure-to-soil stiffness ratio}
\end{align*}
$$

#### `get_static_pile_stiffness`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_static\_pile\_stiffness}(E_s, D, χ) \\ \hspace{1em} K \gets χ \cdot E_s \cdot D \\ \hspace{1em} \mathbf{return} \ K \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K &= \text{Static stiffness (MN/m or MN-m/rad)}\\
E_s &= \text{Elasticity modulus (MPa)}\\
D &= \text{Pile diameter (m)}\\
χ &= \text{Vibration constant}
\end{align*}
$$

#### `get_static_stiffness`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_static\_stiffness}(G, L_h, B_h, j, \mathrm{foundation\_is\_embedded}, ν, η) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_static\_stiffness\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K &= \text{Static stiffness (MN/m or MN-m/rad)}\\
G &= \text{Shear modulus (MPa)}\\
L_h &= \text{Footing half length (m)}\\
B_h &= \text{Footing half width (m)}\\
j &= \text{Vibration mode}\\
\text{foundation\_is\_embedded} &= \text{Foundation is embedded}\\
ν &= \text{Poisson’s ratio}\\
η &= \text{Embedment factor}
\end{align*}
$$

#### `get_stiffness`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_stiffness}(α, K) \\ \hspace{1em} k \gets α \cdot K \\ \hspace{1em} \mathbf{return} \ k \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
k &= \text{Stiffness (MN/m or MN-m/rad)}\\
α &= \text{Dynamic stiffness modifier}\\
K &= \text{Static stiffness (MN/m or MN-m/rad)}
\end{align*}
$$

#### `get_stiffness_edge_factor`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_stiffness\_edge\_factor}(R_e, k, k_z^i, B_h, L_h, j) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_stiffness\_edge\_factor\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
R_k &= \text{Stiffness edge factor}\\
R_e &= \text{End length ratio}\\
k &= \text{Stiffness (MN/m or MN-m/rad)}\\
k_z^i &= \text{Vertical stiffness intensity (MN/m3)}\\
B_h &= \text{Footing half width (m)}\\
L_h &= \text{Footing half length (m)}\\
j &= \text{Vibration mode}
\end{align*}
$$

#### `get_stiffness_intensity`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_stiffness\_intensity}(k_z^i, R_k) \\ \hspace{1em} k_i \gets k_z^i \cdot R_k \\ \hspace{1em} \mathbf{return} \ k_i \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
k_i &= \text{Stiffness intensity (MN/m3)}\\
k_z^i &= \text{Vertical stiffness intensity (MN/m3)}\\
R_k &= \text{Stiffness edge factor}
\end{align*}
$$

#### `get_stiffness_weight_factor_pile_tip_x`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_stiffness\_weight\_factor\_pile\_tip\_x}() \\ \hspace{1em} w_b \gets 0 \\ \hspace{1em} \mathbf{return} \ w_b \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
w_b &= \text{Stiffness weight factor pile tip}
\end{align*}
$$

#### `get_stiffness_weight_factor_pile_tip_z`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_stiffness\_weight\_factor\_pile\_tip\_z}(λL, Ω) \\ \hspace{1em} w_b \gets \frac{2 Ω}{2 Ω \cdot \cosh λL \cdot \mathopen{}\left( 1 + Ω^{2} \mathclose{}\right) \sinh λL} \\ \hspace{1em} \mathbf{return} \ w_b \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
w_b &= \text{Stiffness weight factor pile tip}\\
λL &= \text{Dimensionless pile length parameter}\\
Ω &= \text{Dimensionless pile tip stiffness}
\end{align*}
$$

#### `get_stiffness_weight_factor_pile_x`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_stiffness\_weight\_factor\_pile\_x}() \\ \hspace{1em} w_p \gets \frac{1}{4} \\ \hspace{1em} \mathbf{return} \ w_p \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
w_p &= \text{Stiffness weight factor pile}
\end{align*}
$$

#### `get_stiffness_weight_factor_pile_z`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_stiffness\_weight\_factor\_pile\_z}(w_s, w_b) \\ \hspace{1em} w_p \gets 1 - \mathopen{}\left( w_s + w_b \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ w_p \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
w_p &= \text{Stiffness weight factor pile}\\
w_s &= \text{Stiffness weight factor soil}\\
w_b &= \text{Stiffness weight factor pile tip}
\end{align*}
$$

#### `get_stiffness_weight_factor_soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_stiffness\_weight\_factor\_soil}(λL, Ω, j) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_stiffness\_weight\_factor\_soil\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
w_s &= \text{Stiffness weight factor soil}\\
λL &= \text{Dimensionless pile length parameter}\\
Ω &= \text{Dimensionless pile tip stiffness}\\
j &= \text{Vibration mode}
\end{align*}
$$

#### `get_structure_effective_modal_height`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_structure\_effective\_modal\_height}(h_{total}) \\ \hspace{1em} h \gets \frac{2}{3} \cdot h_{total} \\ \hspace{1em} \mathbf{return} \ h \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
h &= \text{Structure effective modal height (m)}\\
h_{total} &= \text{Structure total height (m)}
\end{align*}
$$

#### `get_structure_to_soil_stiffness_ratio`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_structure\_to\_soil\_stiffness\_ratio}(h, V_{s,avg}, T) \\ \hspace{1em} h/{V_s\ T} \gets \frac{h}{V_{s,avg} \cdot T} \\ \hspace{1em} \mathbf{return} \ h/{V_s\ T} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
h/{V_s\ T} &= \text{Structure-to-soil stiffness ratio}\\
h &= \text{Structure effective modal height (m)}\\
V_{s,avg} &= \text{Average effective shear velocity (m/s)}\\
T &= \text{Structure rigid period (s)}
\end{align*}
$$

#### `get_subgrade_reaction_modulus_at_diameter`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_subgrade\_reaction\_modulus\_at\_diameter}(δ, E_s) \\ \hspace{1em} k_{sd} \gets δ \cdot E_s \\ \hspace{1em} \mathbf{return} \ k_{sd} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
k_{sd} &= \text{Subgrade reaction modulus at diameter (MPa)}\\
δ &= \text{Dimensionless subgrade reaction modulus}\\
E_s &= \text{Elasticity modulus (MPa)}
\end{align*}
$$

#### `get_vertical_stiffness_intensity`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_vertical\_stiffness\_intensity}(j, k, B_h, L_h) \\ \hspace{1em} \mathrm{stiffness\_map} \gets \mathrm{dict} \mathopen{}\left( \mathrm{zip} \mathopen{}\left( \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( j \mathclose{}\right), \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( k \mathclose{}\right) \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} k_z \gets \mathrm{stiffness\_map}_{\textrm{"z"}} \\ \hspace{1em} k_z^i \gets \frac{k_z}{4 B_h \cdot L_h} \\ \hspace{1em} \mathbf{return} \ k_z^i \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
k_z^i &= \text{Vertical stiffness intensity (MN/m3)}\\
j &= \text{Vibration mode}\\
k &= \text{Stiffness (MN/m or MN-m/rad)}\\
B_h &= \text{Footing half width (m)}\\
L_h &= \text{Footing half length (m)}
\end{align*}
$$

#### `get_vibration_constant`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_vibration\_constant}(E_p, E_s, δ, j, λL, Ω) \\ \hspace{1em} \mathbf{return} \ \mathrm{\_vibration\_constant\_vec} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
χ &= \text{Vibration constant}\\
E_p &= \text{Pile elasticity modulus (MPa)}\\
E_s &= \text{Elasticity modulus (MPa)}\\
δ &= \text{Dimensionless subgrade reaction modulus}\\
j &= \text{Vibration mode}\\
λL &= \text{Dimensionless pile length parameter}\\
Ω &= \text{Dimensionless pile tip stiffness}
\end{align*}
$$
