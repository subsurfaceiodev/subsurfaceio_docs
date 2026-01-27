---
title: pile.py
---

#### `_get_average_pile_tip_resistance`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_average\_pile\_tip\_resistance}(z, Q_b, \mathrm{averaging\_diameter\_factor}, D, \mathrm{depth\_inc}) \\ \hspace{1em} \mathrm{average} \gets \mathopen{}\left[  \mathclose{}\right] \\ \hspace{1em} \mathrm{precision} \gets 5 \\ \hspace{1em} \mathrm{depth\_rounded} \gets \mathrm{np}.\mathrm{round} \mathopen{}\left( z, \mathrm{precision} \mathclose{}\right) \\ \hspace{1em} \mathbf{for} \ \mathrm{depth\_current} \in \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( z \mathclose{}\right) \ \mathbf{do} \\ \hspace{2em} \mathrm{z\_offset} \gets \mathrm{averaging\_diameter\_factor} \cdot D \\ \hspace{2em} \mathopen{}\left( z_{top}, z_{bottom} \mathclose{}\right) \gets \mathopen{}\left( \mathrm{depth\_current} - \mathrm{z\_offset}, \mathrm{depth\_current} + \mathrm{z\_offset} \mathclose{}\right) \\ \hspace{2em} \mathrm{mask} \gets \mathopen{}\left( \mathrm{round} \mathopen{}\left( z_{top}, \mathrm{precision} \mathclose{}\right) \le \mathrm{depth\_rounded} \mathclose{}\right) \mathbin{\&} \mathopen{}\left( \mathrm{depth\_rounded} \le \mathrm{round} \mathopen{}\left( z_{bottom}, \mathrm{precision} \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathrm{values} \gets \mathrm{np}.\mathrm{extract} \mathopen{}\left( Q_b, \mathrm{mask} \mathclose{}\right) \\ \hspace{2em} \mathrm{average\_} \gets \frac{\sum \mathopen{}\left( \mathrm{values} \cdot \mathrm{depth\_inc} \mathclose{}\right)}{2 \mathrm{averaging\_diameter\_factor} \cdot D} \\ \hspace{2em} \mathrm{average}.\mathrm{append} \mathopen{}\left( \mathrm{average\_} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ for} \\ \hspace{1em} \mathbf{return} \ \mathrm{average} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_b &= \text{Pile tip resistance (kN)}\\
z &= \text{Depth (m)}\\
D &= \text{Pile diameter (m)}
\end{align*}
$$

#### `get_basic_influence_factor_i1__poulos1980pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_basic\_influence\_factor\_i1\_\_poulos1980pile}(L/D) \\ \hspace{1em} I_1 \gets \mathrm{BasicInfluenceFactorI1Figure}.\mathrm{interpolate\_at\_x} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ I_1 \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
I_1 &= \text{Basic influence factor I1}\\
L/D &= \text{Pile length to diameter ratio}
\end{align*}
$$

#### `get_effective_stress__usace1991design`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_effective\_stress\_\_usace1991design}(z, \mathrm{pile\_critical\_depth}, γ') \\ \hspace{1em} \mathbf{if} \ \lnot \mathrm{is\_null} \mathopen{}\left( \mathrm{pile\_critical\_depth} \mathclose{}\right) \\ \hspace{2em} z \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( z, \mathrm{None}, \mathrm{pile\_critical\_depth} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} H \gets \mathrm{get\_thickness} \mathopen{}\left( z \mathclose{}\right) \\ \hspace{1em} σ_v' \gets \mathrm{np}.\mathrm{cumsum} \mathopen{}\left( γ' \cdot H \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ σ_v' \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
σ_v' &= \text{Effective stress (kPa)}\\
z &= \text{Depth (m)}\\
\text{pile\_critical\_depth} &= \text{Pile critical depth (m)}\\
γ' &= \text{Effective unit weight (kN/m3)}
\end{align*}
$$

#### `get_elasticity_modulus_bearing_ratio__poulos1980pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_elasticity\_modulus\_bearing\_ratio\_\_poulos1980pile}(E_s, E_b) \\ \hspace{1em} E_b\ /\ E_s \gets \frac{E_b}{E_s} \\ \hspace{1em} \mathbf{return} \ E_b\ /\ E_s \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
E_b\ /\ E_s &= \text{Elasticity modulus bearing ratio}\\
E_s &= \text{Elasticity modulus (MPa)}\\
E_b &= \text{Elasticity modulus of bearing soil (MPa)}
\end{align*}
$$

#### `get_pile_friction_coefficient__api1975recommended`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_friction\_coefficient\_\_api1975recommended}(S_u) \\ \hspace{1em} α \gets \mathrm{PileFrictionCoefficientAPI1975Figure}.\mathrm{interpolate\_at\_x} \mathopen{}\left( S_u \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ α \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
α &= \text{Pile friction coefficient}\\
S_u &= \text{Undrained shear strength (kPa)}
\end{align*}
$$

#### `get_pile_friction_coefficient__semple1984shaft`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_friction\_coefficient\_\_semple1984shaft}(S_u, σ_v', L, D) \\ \hspace{1em} \mathrm{alpha1} \gets \mathrm{PileFrictionCoefficient1Semple1984Figure}.\mathrm{interpolate\_at\_x} \mathopen{}\left( \frac{S_u}{σ_v'} \mathclose{}\right) \\ \hspace{1em} \mathrm{alpha2} \gets \mathrm{PileFrictionCoefficient1Semple1984Figure}.\mathrm{interpolate\_at\_x} \mathopen{}\left( \frac{L}{D} \mathclose{}\right) \\ \hspace{1em} α \gets \mathrm{alpha1} \cdot \mathrm{alpha2} \\ \hspace{1em} \mathbf{return} \ α \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
α &= \text{Pile friction coefficient}\\
S_u &= \text{Undrained shear strength (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
L &= \text{Pile embedment length (m)}\\
D &= \text{Pile diameter (m)}
\end{align*}
$$

#### `get_pile_friction_coefficient__usace1991design`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_friction\_coefficient\_\_usace1991design}(\mathrm{is\_long\_pile}, S_u, σ_v', L, D) \\ \hspace{1em} \mathbf{if} \ \mathrm{is\_long\_pile} \\ \hspace{2em} \mathbf{return} \ \mathrm{get\_pile\_friction\_coefficient\_\_semple1984shaft} \mathopen{}\left( S_u, σ_v', L, D \mathclose{}\right) \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{return} \ \mathrm{get\_pile\_friction\_coefficient\_\_api1975recommended} \mathopen{}\left( S_u \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
α &= \text{Pile friction coefficient}\\
\text{is\_long\_pile} &= \text{Is long pile}\\
S_u &= \text{Undrained shear strength (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
L &= \text{Pile embedment length (m)}\\
D &= \text{Pile diameter (m)}
\end{align*}
$$

#### `get_pile_influence_factor_bearing__poulos1980pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_influence\_factor\_bearing\_\_poulos1980pile}(I_1, R_K, R_b, R_v) \\ \hspace{1em} I \gets I_1 \cdot R_K \cdot R_b \cdot R_v \\ \hspace{1em} \mathbf{return} \ I \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
I &= \text{Pile influence factor}\\
I_1 &= \text{Basic influence factor I1}\\
R_K &= \text{Pile settlement correction for compressibility}\\
R_b &= \text{Pile settlement correction for bearing}\\
R_v &= \text{Pile settlement correction for Poisson’s ratio}
\end{align*}
$$

#### `get_pile_influence_factor_floating__poulos1980pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_influence\_factor\_floating\_\_poulos1980pile}(I_1, R_K, R_h, R_v) \\ \hspace{1em} I \gets I_1 \cdot R_K \cdot R_h \cdot R_v \\ \hspace{1em} \mathbf{return} \ I \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
I &= \text{Pile influence factor}\\
I_1 &= \text{Basic influence factor I1}\\
R_K &= \text{Pile settlement correction for compressibility}\\
R_h &= \text{Pile settlement correction for depth}\\
R_v &= \text{Pile settlement correction for Poisson’s ratio}
\end{align*}
$$

#### `get_pile_length_to_diameter_ratio`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_length\_to\_diameter\_ratio}(L, D) \\ \hspace{1em} L/D \gets \frac{L}{D} \\ \hspace{1em} \mathbf{return} \ L/D \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
L/D &= \text{Pile length to diameter ratio}\\
L &= \text{Pile embedment length (m)}\\
D &= \text{Pile diameter (m)}
\end{align*}
$$

#### `get_pile_length_to_soil_thickness_ratio`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_length\_to\_soil\_thickness\_ratio}(L, h) \\ \hspace{1em} L/h \gets \frac{L}{h} \\ \hspace{1em} \mathbf{return} \ L/h \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
L/h &= \text{Pile length to soil thickness ratio}\\
L &= \text{Pile embedment length (m)}\\
h &= \text{Soil thickness (m)}
\end{align*}
$$

#### `get_pile_perimeter`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_perimeter}(\mathrm{pile\_shape}, D) \\ \hspace{1em} P \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{pile\_shape} = \textrm{"circle"} \\ \hspace{2em} P \gets \mathrm{np}.\pi \cdot D \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{pile\_shape} = \textrm{"square"} \\ \hspace{3em} P \gets 4 D \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ P \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
P &= \text{Pile perimeter (m)}\\
\text{pile\_shape} &= \text{Pile shape}\\
D &= \text{Pile diameter (m)}
\end{align*}
$$

#### `get_pile_settlement__poulos1980pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_settlement\_\_poulos1980pile}(P, D, E_s, I) \\ \hspace{1em} S \gets \frac{P}{D \cdot E_s} \cdot I \\ \hspace{1em} S \gets \frac{S}{10} \\ \hspace{1em} \mathbf{return} \ S \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S &= \text{Pile settlement (cm)}\\
P &= \text{Pile head axial load (kN)}\\
D &= \text{Pile diameter (m)}\\
E_s &= \text{Elasticity modulus (MPa)}\\
I &= \text{Pile influence factor}
\end{align*}
$$

#### `get_pile_settlement_correction_bearing__poulos1980pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_settlement\_correction\_bearing\_\_poulos1980pile}(E_b\ /\ E_s, L/D, K) \\ \hspace{1em} \mathrm{ld\_nearest} \gets \mathrm{find\_nearest} \mathopen{}\left( \mathrm{list} \mathopen{}\left( \mathrm{ld\_reference\_figures\_map}.\mathrm{keys} \mathopen{}\left( \mathclose{}\right) \mathclose{}\right), L/D \mathclose{}\right) \\ \hspace{1em} \mathrm{bf} \gets \mathrm{ld\_reference\_figures\_map}_{\mathrm{ld\_nearest}} \\ \hspace{1em} R_b \gets \mathrm{bf}.\mathrm{interpolate\_at\_x} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ R_b \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
R_b &= \text{Pile settlement correction for bearing}\\
E_b\ /\ E_s &= \text{Elasticity modulus bearing ratio}\\
L/D &= \text{Pile length to diameter ratio}\\
K &= \text{Pile stiffness factor}
\end{align*}
$$

#### `get_pile_settlement_correction_compressibility__poulos1980pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_settlement\_correction\_compressibility\_\_poulos1980pile}(K, L/D) \\ \hspace{1em} R_K \gets \mathrm{PileSettlementCorrectionCompressibilityFigure}.\mathrm{interpolate\_at\_x} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ R_K \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
R_K &= \text{Pile settlement correction for compressibility}\\
K &= \text{Pile stiffness factor}\\
L/D &= \text{Pile length to diameter ratio}
\end{align*}
$$

#### `get_pile_settlement_correction_depth__poulos1980pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_settlement\_correction\_depth\_\_poulos1980pile}(L/h, L/D) \\ \hspace{1em} R_h \gets \mathrm{PileSettlementCorrectionDepthFigure}.\mathrm{interpolate\_at\_x} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ R_h \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
R_h &= \text{Pile settlement correction for depth}\\
L/h &= \text{Pile length to soil thickness ratio}\\
L/D &= \text{Pile length to diameter ratio}
\end{align*}
$$

#### `get_pile_settlement_correction_poisson__poulos1980pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_settlement\_correction\_poisson\_\_poulos1980pile}(ν, K) \\ \hspace{1em} R_v \gets \mathrm{PileSettlementCorrectionPoissonFigure}.\mathrm{interpolate\_at\_x} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ R_v \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
R_v &= \text{Pile settlement correction for Poisson’s ratio}\\
ν &= \text{Poisson’s ratio}\\
K &= \text{Pile stiffness factor}
\end{align*}
$$

#### `get_pile_shaft_resistance`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_shaft\_resistance}(Q_{s\ i}) \\ \hspace{1em} Q_s \gets \mathrm{np}.\mathrm{cumsum} \mathopen{}\left( Q_{s\ i} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ Q_s \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_s &= \text{Pile shaft resistance (kN)}\\
Q_{s\ i} &= \text{Pile shaft resistance inc. (kN)}
\end{align*}
$$

#### `get_pile_shaft_resistance_inc`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_shaft\_resistance\_inc}(f_p, A_s) \\ \hspace{1em} Q_{s\ i} \gets f_p \cdot A_s \cdot 1000 \\ \hspace{1em} \mathbf{return} \ Q_{s\ i} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_{s\ i} &= \text{Pile shaft resistance inc. (kN)}\\
f_p &= \text{Unit side friction (MPa)}\\
A_s &= \text{Pile side surface area (m2)}
\end{align*}
$$

#### `get_pile_side_surface_area`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_side\_surface\_area}(H, P) \\ \hspace{1em} A_s \gets H \cdot P \\ \hspace{1em} \mathbf{return} \ A_s \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
A_s &= \text{Pile side surface area (m2)}\\
H &= \text{Thickness (m)}\\
P &= \text{Pile perimeter (m)}
\end{align*}
$$

#### `get_pile_stiffness_factor__poulos1980pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_stiffness\_factor\_\_poulos1980pile}(E_p, E_s, R_A) \\ \hspace{1em} K \gets \frac{E_p \cdot R_A}{E_s} \\ \hspace{1em} \mathbf{return} \ K \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K &= \text{Pile stiffness factor}\\
E_p &= \text{Pile elasticity modulus (MPa)}\\
E_s &= \text{Elasticity modulus (MPa)}\\
R_A &= \text{Pile area ratio}
\end{align*}
$$

#### `get_pile_tip_area`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_tip\_area}(\mathrm{pile\_shape}, D) \\ \hspace{1em} A_p \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{pile\_shape} = \textrm{"circle"} \\ \hspace{2em} A_p \gets \mathrm{np}.\pi \cdot \mathopen{}\left( \frac{D}{2} \mathclose{}\right)^{2} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{pile\_shape} = \textrm{"square"} \\ \hspace{3em} A_p \gets D^{2} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ A_p \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
A_p &= \text{Pile tip area (m2)}\\
\text{pile\_shape} &= \text{Pile shape}\\
D &= \text{Pile diameter (m)}
\end{align*}
$$

#### `get_pile_tip_resistance`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_tip\_resistance}(q_p, A_p) \\ \hspace{1em} Q_b \gets q_p \cdot A_p \cdot 1000 \\ \hspace{1em} \mathbf{return} \ Q_b \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_b &= \text{Pile tip resistance (kN)}\\
q_p &= \text{Pile unit tip resistance (MPa)}\\
A_p &= \text{Pile tip area (m2)}
\end{align*}
$$

#### `get_pile_tip_resistance__usace1991design`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_tip\_resistance\_\_usace1991design}(z, \mathrm{averaging\_diameter\_factor}, D, \mathrm{depth\_inc}, \mathrm{soil\_type}, S_u, σ_v', N_q, A_p) \\ \hspace{1em} Q_b \gets \mathrm{np}.\mathrm{select} \mathopen{}\left( \mathopen{}\left[ \mathrm{soil\_type} = \textrm{"Clay"}, \mathrm{soil\_type} = \textrm{"Sand"} \mathclose{}\right], \mathopen{}\left[ \mathrm{get\_pile\_tip\_resistance\_cohesive\_\_usace1991design} \mathopen{}\left( S_u, A_p \mathclose{}\right), \mathrm{get\_pile\_tip\_resistance\_cohesionless\_\_usace1991design} \mathopen{}\left( σ_v', N_q, A_p \mathclose{}\right) \mathclose{}\right] \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ \mathrm{averaging\_diameter\_factor} > 0 \\ \hspace{2em} Q_b \gets \mathrm{\_get\_average\_pile\_tip\_resistance} \mathopen{}\left( z, Q_b, \mathrm{averaging\_diameter\_factor}, D, \mathrm{depth\_inc} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ Q_b \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_b &= \text{Pile tip resistance (kN)}\\
z &= \text{Depth (m)}\\
D &= \text{Pile diameter (m)}\\
\text{soil\_type} &= \text{Soil type}\\
S_u &= \text{Undrained shear strength (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
N_q &= \text{Bearing capacity factor for surcharge}\\
A_p &= \text{Pile tip area (m2)}
\end{align*}
$$

#### `get_pile_tip_resistance_cohesionless__usace1991design`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_tip\_resistance\_cohesionless\_\_usace1991design}(σ_v', N_q, A_p) \\ \hspace{1em} Q_b \gets σ_v' \cdot N_q \cdot A_p \\ \hspace{1em} \mathbf{return} \ Q_b \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_b &= \text{Pile tip resistance (kN)}\\
σ_v' &= \text{Effective stress (kPa)}\\
N_q &= \text{Bearing capacity factor for surcharge}\\
A_p &= \text{Pile tip area (m2)}
\end{align*}
$$

#### `get_pile_tip_resistance_cohesive__usace1991design`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_tip\_resistance\_cohesive\_\_usace1991design}(S_u, A_p) \\ \hspace{1em} Q_b \gets S_u \cdot 9 A_p \\ \hspace{1em} \mathbf{return} \ Q_b \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_b &= \text{Pile tip resistance (kN)}\\
S_u &= \text{Undrained shear strength (kPa)}\\
A_p &= \text{Pile tip area (m2)}
\end{align*}
$$

#### `get_pile_ultimate_resistance`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_ultimate\_resistance}(Q_b, Q_s) \\ \hspace{1em} Q_{ult} \gets Q_b + Q_s \\ \hspace{1em} \mathbf{return} \ Q_{ult} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_{ult} &= \text{Pile ultimate resistance (kN)}\\
Q_b &= \text{Pile tip resistance (kN)}\\
Q_s &= \text{Pile shaft resistance (kN)}
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

#### `get_unit_side_friction__usace1991design`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_unit\_side\_friction\_\_usace1991design}(z, \mathrm{soil\_type}, S_u, α, ϕ, σ_v', K_o, f_{p\ lim}, ZFL) \\ \hspace{1em} f_p \gets \mathrm{np}.\mathrm{select} \mathopen{}\left( \mathopen{}\left[ \mathrm{soil\_type} = \textrm{"Clay"}, \mathrm{soil\_type} = \textrm{"Sand"} \mathclose{}\right], \mathopen{}\left[ \mathrm{get\_unit\_side\_friction\_cohesive\_\_usace1991design} \mathopen{}\left( S_u, α, f_{p\ lim} \mathclose{}\right), \mathrm{get\_unit\_side\_friction\_cohesionless\_\_usace1991design} \mathopen{}\left( ϕ, σ_v', K_o, f_{p\ lim} \mathclose{}\right) \mathclose{}\right] \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( f_p, z \le ZFL, 0 \mathclose{}\right) \\ \hspace{1em} f_p \gets \frac{f_p}{1000} \\ \hspace{1em} \mathbf{return} \ f_p \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
f_p &= \text{Unit side friction (MPa)}\\
z &= \text{Depth (m)}\\
\text{soil\_type} &= \text{Soil type}\\
S_u &= \text{Undrained shear strength (kPa)}\\
α &= \text{Pile friction coefficient}\\
ϕ &= \text{Friction angle (°)}\\
σ_v' &= \text{Effective stress (kPa)}\\
K_o &= \text{Coefficient of lateral earth pressure at rest}\\
f_{p\ lim} &= \text{Unit side friction limit (MPa)}\\
ZFL &= \text{Zero-friction length (m)}
\end{align*}
$$

#### `get_unit_side_friction_cohesionless__usace1991design`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_unit\_side\_friction\_cohesionless\_\_usace1991design}(ϕ, σ_v', K_o, f_{p\ lim}) \\ \hspace{1em} f_p \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( K_o \cdot σ_v' \cdot \mathrm{tandg} \mathopen{}\left( 0.95 ϕ \mathclose{}\right), \mathrm{None}, f_{p\ lim} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ f_p \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
f_p &= \text{Unit side friction (MPa)}\\
ϕ &= \text{Friction angle (°)}\\
σ_v' &= \text{Effective stress (kPa)}\\
K_o &= \text{Coefficient of lateral earth pressure at rest}\\
f_{p\ lim} &= \text{Unit side friction limit (MPa)}
\end{align*}
$$

#### `get_unit_side_friction_cohesive__usace1991design`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_unit\_side\_friction\_cohesive\_\_usace1991design}(S_u, α, f_{p\ lim}) \\ \hspace{1em} f_p \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( S_u \cdot α, \mathrm{None}, f_{p\ lim} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ f_p \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
f_p &= \text{Unit side friction (MPa)}\\
S_u &= \text{Undrained shear strength (kPa)}\\
α &= \text{Pile friction coefficient}\\
f_{p\ lim} &= \text{Unit side friction limit (MPa)}
\end{align*}
$$
