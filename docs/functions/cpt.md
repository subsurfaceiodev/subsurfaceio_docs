---
title: cpt.py
---

#### `_get_cross_correlation_function`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_cross\_correlation\_function}(x, y) \\ \hspace{1em} \mathrm{lags} \gets \mathrm{correlation\_lags} \mathopen{}\left( x.\mathrm{size}, y.\mathrm{size} \mathclose{}\right) \\ \hspace{1em} \mathrm{correlation} \gets \frac{\mathrm{correlate} \mathopen{}\left( y - \mathrm{np}.\mathrm{mean} \mathopen{}\left( y \mathclose{}\right), x - \mathrm{np}.\mathrm{mean} \mathopen{}\left( x \mathclose{}\right) \mathclose{}\right)}{\mathrm{np}.\mathrm{std} \mathopen{}\left( y \mathclose{}\right) \cdot \mathrm{np}.\mathrm{std} \mathopen{}\left( x \mathclose{}\right) \mathrm{len} \mathopen{}\left( y \mathclose{}\right)} \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( \mathrm{lags}, \mathrm{correlation} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

#### `_get_equivalent_cone_resistance__bustamante1982pile_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_equivalent\_cone\_resistance\_\_bustamante1982pile\_scalar}(q_t, z, z_{top}, z_{bottom}) \\ \hspace{1em} \mathrm{mask} \gets \mathopen{}\left( z_{top} \le z \mathclose{}\right) \mathbin{\&} \mathopen{}\left( z \le z_{bottom} \mathclose{}\right) \\ \hspace{1em} q_t \gets \mathrm{np}.\mathrm{extract} \mathopen{}\left( \mathrm{mask}, q_t \mathclose{}\right) \\ \hspace{1em} q'_{ca} \gets \mathrm{np}.\mathrm{mean} \mathopen{}\left( q_t \mathclose{}\right) \\ \hspace{1em} q_{ca} \gets \mathrm{np}.\mathrm{mean} \mathopen{}\left( \mathrm{np}.\mathrm{clip} \mathopen{}\left( q_t, 0.7 q'_{ca}, 1.3 q'_{ca} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( q'_{ca}, q_{ca} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
q'_{ca} &= \text{Equivalent cone resistance primed (MPa)}\\
q_{ca} &= \text{Equivalent cone resistance (MPa)}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
z &= \text{Depth (m)}\\
z_{top} &= \text{Depth top (m)}\\
z_{bottom} &= \text{Depth bottom (m)}
\end{align*}
$$

#### `_get_max_shear_strain__zhang2004estimating_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_max\_shear\_strain\_\_zhang2004estimating\_scalar}(FS_{liq}, D_r) \\ \hspace{1em} \mathrm{relative\_density\_\_zhang2004estimating\_list} \gets \mathopen{}\left[ 40, 50, 60, 70, 80, 90 \mathclose{}\right] \\ \hspace{1em} \mathbf{if} \ \mathrm{np}.\mathrm{isnan} \mathopen{}\left( FS_{liq} \mathclose{}\right) \lor \mathrm{np}.\mathrm{isnan} \mathopen{}\left( D_r \mathclose{}\right) \\ \hspace{2em} γ_{max} \gets 0 \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ D_r = 90 \\ \hspace{3em} \mathbf{if} \ FS_{liq} < 0.7 \\ \hspace{4em} γ_{max} \gets 6.2 \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} γ_{max} \gets 3.26 FS_{liq}^{-1.8} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ D_r = 80 \\ \hspace{4em} \mathbf{if} \ FS_{liq} < 0.56 \\ \hspace{5em} γ_{max} \gets 10 \\ \hspace{4em} \mathbf{else} \\ \hspace{5em} γ_{max} \gets 3.22 FS_{liq}^{-2.08} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ D_r = 70 \\ \hspace{5em} \mathbf{if} \ FS_{liq} < 0.59 \\ \hspace{6em} γ_{max} \gets 14.5 \\ \hspace{5em} \mathbf{else} \\ \hspace{6em} γ_{max} \gets 3.2 FS_{liq}^{-2.89} \\ \hspace{5em} \mathbf{end \ if} \\ \hspace{4em} \mathbf{else} \\ \hspace{5em} \mathbf{if} \ D_r = 60 \\ \hspace{6em} \mathbf{if} \ FS_{liq} < 0.66 \\ \hspace{7em} γ_{max} \gets 22.7 \\ \hspace{6em} \mathbf{else} \\ \hspace{7em} γ_{max} \gets 3.58 FS_{liq}^{-4.42} \\ \hspace{6em} \mathbf{end \ if} \\ \hspace{5em} \mathbf{else} \\ \hspace{6em} \mathbf{if} \ D_r = 50 \\ \hspace{7em} \mathbf{if} \ FS_{liq} < 0.72 \\ \hspace{8em} γ_{max} \gets 34.1 \\ \hspace{7em} \mathbf{else} \\ \hspace{8em} γ_{max} \gets 4.22 FS_{liq}^{-6.39} \\ \hspace{7em} \mathbf{end \ if} \\ \hspace{6em} \mathbf{else} \\ \hspace{7em} \mathbf{if} \ D_r = 40 \\ \hspace{8em} \mathbf{if} \ FS_{liq} < 0.81 \\ \hspace{9em} γ_{max} \gets 51.2 \\ \hspace{8em} \mathbf{else} \\ \hspace{9em} \mathbf{if} \ FS_{liq} \le 1 \\ \hspace{10em} γ_{max} \gets 250 \mathopen{}\left( 1 - FS_{liq} \mathclose{}\right) + 3.5 \\ \hspace{9em} \mathbf{else} \\ \hspace{10em} γ_{max} \gets \mathrm{np}.\mathrm{nan} \\ \hspace{9em} \mathbf{end \ if} \\ \hspace{8em} \mathbf{end \ if} \\ \hspace{7em} \mathbf{else} \\ \hspace{8em} \mathrm{idx} \gets \mathrm{np}.\mathrm{searchsorted} \mathopen{}\left( \mathrm{relative\_density\_\_zhang2004estimating\_list}, D_r \mathclose{}\right) \\ \hspace{8em} \mathrm{relative\_density\_bottom} \gets \mathrm{relative\_density\_\_zhang2004estimating\_list}_{\mathrm{idx} - 1} \\ \hspace{8em} \mathrm{max\_shear\_strain\_bottom} \gets \mathrm{\_get\_max\_shear\_strain\_\_zhang2004estimating\_scalar} \mathopen{}\left( FS_{liq}, \mathrm{relative\_density\_bottom} \mathclose{}\right) \\ \hspace{8em} \mathrm{relative\_density\_top} \gets \mathrm{relative\_density\_\_zhang2004estimating\_list}_{\mathrm{idx}} \\ \hspace{8em} \mathrm{max\_shear\_strain\_top} \gets \mathrm{\_get\_max\_shear\_strain\_\_zhang2004estimating\_scalar} \mathopen{}\left( FS_{liq}, \mathrm{relative\_density\_top} \mathclose{}\right) \\ \hspace{8em} γ_{max} \gets \mathrm{np}.\mathrm{interp} \mathopen{}\left( D_r, \mathopen{}\left[ \mathrm{relative\_density\_bottom}, \mathrm{relative\_density\_top} \mathclose{}\right], \mathopen{}\left[ \mathrm{max\_shear\_strain\_bottom}, \mathrm{max\_shear\_strain\_top} \mathclose{}\right] \mathclose{}\right) \\ \hspace{7em} \mathbf{end \ if} \\ \hspace{6em} \mathbf{end \ if} \\ \hspace{5em} \mathbf{end \ if} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ γ_{max} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
γ_{max} &= \text{Max. shear strain (\%)}\\
FS_{liq} &= \text{Liquefaction safety factor}\\
D_r &= \text{Relative density (\%)}
\end{align*}
$$

#### `_get_nature_of_soil__bustamante1982pile_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_nature\_of\_soil\_\_bustamante1982pile\_scalar}(Q_{tn}, R_f, I_B) \\ \hspace{1em} \mathrm{nos} \gets \textrm{"0"} \\ \hspace{1em} \mathbf{if} \ R_f > 10 \\ \hspace{2em} \mathrm{nos} \gets \textrm{"0"} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ I_B \le 32 \\ \hspace{3em} \mathbf{if} \ Q_{tn} \le 10 \\ \hspace{4em} \mathrm{nos} \gets \textrm{"1"} \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ Q_{tn} \le 50 \\ \hspace{5em} \mathrm{nos} \gets \textrm{"2"} \\ \hspace{4em} \mathbf{else} \\ \hspace{5em} \mathbf{if} \ Q_{tn} > 50 \\ \hspace{6em} \mathrm{nos} \gets \textrm{"4"} \\ \hspace{5em} \mathbf{end \ if} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ I_B > 32 \\ \hspace{4em} \mathbf{if} \ Q_{tn} \le 50 \\ \hspace{5em} \mathrm{nos} \gets \textrm{"3"} \\ \hspace{4em} \mathbf{else} \\ \hspace{5em} \mathbf{if} \ Q_{tn} \le 120 \\ \hspace{6em} \mathrm{nos} \gets \textrm{"5"} \\ \hspace{5em} \mathbf{else} \\ \hspace{6em} \mathbf{if} \ Q_{tn} > 120 \\ \hspace{7em} \mathrm{nos} \gets \textrm{"6"} \\ \hspace{6em} \mathbf{end \ if} \\ \hspace{5em} \mathbf{end \ if} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathrm{nos} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{nature\_of\_soil} &= \text{Nature of soil}\\
Q_{tn} &= \text{Stress-normalized cone resistance}\\
R_f &= \text{Friction ratio (\%)}\\
I_B &= \text{Modified soil behaviour type index}
\end{align*}
$$

#### `_get_pile_friction_coefficient__bustamante1982fellenius_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_pile\_friction\_coefficient\_\_bustamante1982fellenius\_scalar}(q_c, \mathrm{is\_fine\_soil}, \mathrm{pile\_type\_category}) \\ \hspace{1em} α \gets \mathrm{np}.\mathrm{nan} \\ \hspace{1em} \mathrm{is\_concrete} \gets \mathrm{pile\_type\_category} \ne \textrm{"IIB"} \\ \hspace{1em} \mathbf{if} \ \mathrm{is\_fine\_soil} \\ \hspace{2em} \mathbf{if} \ q_c < 1 \\ \hspace{3em} α \gets \left\{ \begin{array}{ll} 90, & \mathrm{if} \ \mathrm{is\_concrete} \\ 30, & \mathrm{otherwise} \end{array} \right. \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ q_c < 5 \\ \hspace{4em} α \gets \left\{ \begin{array}{ll} 40, & \mathrm{if} \ \mathrm{is\_concrete} \\ 80, & \mathrm{otherwise} \end{array} \right. \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ q_c \ge 5 \\ \hspace{5em} α \gets \left\{ \begin{array}{ll} 60, & \mathrm{if} \ \mathrm{is\_concrete} \\ 120, & \mathrm{otherwise} \end{array} \right. \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ q_c < 5 \\ \hspace{3em} α \gets \left\{ \begin{array}{ll} 60, & \mathrm{if} \ \mathrm{is\_concrete} \\ 120, & \mathrm{otherwise} \end{array} \right. \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ q_c < 12 \\ \hspace{4em} α \gets \left\{ \begin{array}{ll} 100, & \mathrm{if} \ \mathrm{is\_concrete} \\ 200, & \mathrm{otherwise} \end{array} \right. \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ q_c \ge 12 \\ \hspace{5em} α \gets \left\{ \begin{array}{ll} 150, & \mathrm{if} \ \mathrm{is\_concrete} \\ 200, & \mathrm{otherwise} \end{array} \right. \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ α \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
α &= \text{Pile friction coefficient}\\
q_c &= \text{Cone tip resistance (MPa)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{pile\_type\_category} &= \text{Pile type category}
\end{align*}
$$

#### `_get_pile_tip_resistance_factor__bustamante1982fellenius_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_pile\_tip\_resistance\_factor\_\_bustamante1982fellenius\_scalar}(q_c, \mathrm{is\_fine\_soil}, \mathrm{pile\_type\_category}) \\ \hspace{1em} k_c \gets \mathrm{np}.\mathrm{nan} \\ \hspace{1em} \mathrm{is\_bored} \gets \mathrm{pile\_type\_category} \in \mathopen{}\left( \textrm{"IA"}, \textrm{"IB"} \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ \mathrm{is\_fine\_soil} \\ \hspace{2em} \mathbf{if} \ q_c < 1 \\ \hspace{3em} k_c \gets \left\{ \begin{array}{ll} 0.4, & \mathrm{if} \ \mathrm{is\_bored} \\ 0.5, & \mathrm{otherwise} \end{array} \right. \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ q_c < 5 \\ \hspace{4em} k_c \gets \left\{ \begin{array}{ll} 0.35, & \mathrm{if} \ \mathrm{is\_bored} \\ 0.45, & \mathrm{otherwise} \end{array} \right. \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ q_c \ge 5 \\ \hspace{5em} k_c \gets \left\{ \begin{array}{ll} 0.45, & \mathrm{if} \ \mathrm{is\_bored} \\ 0.55, & \mathrm{otherwise} \end{array} \right. \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ q_c < 5 \\ \hspace{3em} k_c \gets \left\{ \begin{array}{ll} 0.2, & \mathrm{if} \ \mathrm{is\_bored} \\ 0.4, & \mathrm{otherwise} \end{array} \right. \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ q_c < 12 \\ \hspace{4em} k_c \gets \left\{ \begin{array}{ll} 0.4, & \mathrm{if} \ \mathrm{is\_bored} \\ 0.5, & \mathrm{otherwise} \end{array} \right. \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ q_c \ge 12 \\ \hspace{5em} k_c \gets \left\{ \begin{array}{ll} 0.3, & \mathrm{if} \ \mathrm{is\_bored} \\ 0.4, & \mathrm{otherwise} \end{array} \right. \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ k_c \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
k_c &= \text{Pile tip resistance factor}\\
q_c &= \text{Cone tip resistance (MPa)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{pile\_type\_category} &= \text{Pile type category}
\end{align*}
$$

#### `_get_unit_side_friction_limit__bustamante1982fellenius_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_unit\_side\_friction\_limit\_\_bustamante1982fellenius\_scalar}(q_c, \mathrm{is\_fine\_soil}) \\ \hspace{1em} f_{p\ lim} \gets \mathrm{np}.\mathrm{nan} \\ \hspace{1em} \mathbf{if} \ \mathrm{is\_fine\_soil} \\ \hspace{2em} \mathbf{if} \ q_c < 1 \\ \hspace{3em} f_{p\ lim} \gets 15 \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ q_c < 5 \\ \hspace{4em} f_{p\ lim} \gets 35 \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ q_c \ge 5 \\ \hspace{5em} f_{p\ lim} \gets 35 \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ q_c < 5 \\ \hspace{3em} f_{p\ lim} \gets 35 \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ q_c < 12 \\ \hspace{4em} f_{p\ lim} \gets 80 \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ q_c \ge 12 \\ \hspace{5em} f_{p\ lim} \gets 120 \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ f_{p\ lim} \cdot 0.001 \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
f_{p\ lim} &= \text{Unit side friction limit (MPa)}\\
q_c &= \text{Cone tip resistance (MPa)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_alternative_normalized_cone_resistance`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_alternative\_normalized\_cone\_resistance}(q_t, σ_v, σ_v') \\ \hspace{1em} \textrm{" Soil classification using the cone penetration test by robertson (1990)"} \\ \hspace{1em} Q_{t1} \gets \frac{q_t \cdot 1000 - σ_v}{σ_v'} \\ \hspace{1em} \mathbf{return} \ Q_{t1} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_{t1} &= \text{Alternative normalized cone resistance}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
σ_v &= \text{Total stress (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}
\end{align*}
$$

#### `get_alternative_normalized_friction_ratio`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_alternative\_normalized\_friction\_ratio}(f_s, q_c, σ_v) \\ \hspace{1em} F \gets \mathrm{get\_normalized\_friction\_ratio} \mathopen{}\left( f_s, q_c, σ_v \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ F \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
F &= \text{Alternative normalized friction ratio (\%)}\\
f_s &= \text{Sleeve friction (kPa)}\\
q_c &= \text{Cone tip resistance (MPa)}\\
σ_v &= \text{Total stress (kPa)}
\end{align*}
$$

#### `get_behaviour_correction_factor__robertson2022evaluation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_behaviour\_correction\_factor\_\_robertson2022evaluation}(I_c, \mathrm{remove\_loose\_sand\_criteria}, F_r, \mathrm{soil\_transition}) \\ \hspace{1em} \mathrm{conditions} \gets \mathopen{}\left[ I_c \ge 1.7, I_c < 1.7 \mathclose{}\right] \\ \hspace{1em} \mathrm{choices} \gets \mathopen{}\left[ 1.8346 I_c^{5} - 23.673 I_c^{4} + 124.02 I_c^{3} - 320.616 I_c^{2} + 405.821 I_c - 199.97, 1 \mathclose{}\right] \\ \hspace{1em} K_c \gets \mathrm{np}.\mathrm{select} \mathopen{}\left( \mathrm{conditions}, \mathrm{choices} \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ \lnot \mathrm{remove\_loose\_sand\_criteria} \\ \hspace{2em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( K_c, \mathopen{}\left( I_c > 1.64 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( I_c < 2.36 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( F_r < 0.5 \mathclose{}\right), 1 \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ K_c \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K_c &= \text{Behaviour correction factor}\\
I_c &= \text{Soil behavior type index}\\
\text{remove\_loose\_sand\_criteria} &= \text{Remove loose sand criteria}\\
F_r &= \text{Normalized friction ratio (\%)}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_clean_sand_normalized_cone_resistance_1atm_sr__idriss2003estimating`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_clean\_sand\_normalized\_cone\_resistance\_1atm\_sr\_\_idriss2003estimating}(q_{c1N}, Δq_{c1N-Sr}) \\ \hspace{1em} q_{c1Ncs-Sr} \gets q_{c1N} + Δq_{c1N-Sr} \\ \hspace{1em} \mathbf{return} \ q_{c1Ncs-Sr} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
q_{c1Ncs-Sr} &= \text{Clean sand normalized cone resistance at 1 atm (Sr)}\\
q_{c1N} &= \text{Normalized cone resistance at 1 atm}\\
Δq_{c1N-Sr} &= \text{Normalized cone resistance fines inc. (Sr)}
\end{align*}
$$

#### `get_clean_sand_normalized_cone_resistance__robertson2009interpretation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_clean\_sand\_normalized\_cone\_resistance\_\_robertson2009interpretation}(K_c, Q_{tn}, \mathrm{soil\_transition}) \\ \hspace{1em} \textrm{" Performance based earthquake design using the CPT by robertson (2009) "} \\ \hspace{1em} \textrm{" Evaluating cyclic liquefaction potential using the cone penetration test by robertson \& Wride (1998) "} \\ \hspace{1em} Q_{tncs} \gets K_c \cdot Q_{tn} \\ \hspace{1em} \mathbf{return} \ Q_{tncs} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_{tncs} &= \text{Clean sand normalized cone resistance}\\
K_c &= \text{Behaviour correction factor}\\
Q_{tn} &= \text{Stress-normalized cone resistance}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_clean_sand_normalized_cone_resistance__robertson2012interpretation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_clean\_sand\_normalized\_cone\_resistance\_\_robertson2012interpretation}(K_d, I_D) \\ \hspace{1em} Q_{tncs} \gets 25 K_d \\ \hspace{1em} Q_{tncs} \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( Q_{tncs} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( Q_{tncs}, \mathord{\sim} \mathopen{}\left( \mathopen{}\left( K_d > 2 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( K_d < 6 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( I_D > 1.2 \mathclose{}\right) \mathclose{}\right), \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ Q_{tncs} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_{tncs} &= \text{Clean sand normalized cone resistance}\\
K_d &= \text{Horizontal stress index}\\
I_D &= \text{Material index}
\end{align*}
$$

#### `get_constrained_modulus__robertson2009interpretation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_constrained\_modulus\_\_robertson2009interpretation}(I_c, Q_{tn}, q_t, σ_v, G_o) \\ \hspace{1em} M \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( I_c, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( M, I_c > 2.2, \mathrm{np}.\mathrm{clip} \mathopen{}\left( Q_{tn}, \mathrm{None}, 14 \mathclose{}\right) \cdot \mathopen{}\left( q_t - σ_v \cdot 0.001 \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( M, I_c \le 2.2, 1.6 G_o \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ M \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
M &= \text{Constrained modulus (MPa)}\\
I_c &= \text{Soil behavior type index}\\
Q_{tn} &= \text{Stress-normalized cone resistance}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
σ_v &= \text{Total stress (kPa)}\\
G_o &= \text{Small strain shear modulus (MPa)}
\end{align*}
$$

#### `get_constrained_modulus__robertson2022evaluation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_constrained\_modulus\_\_robertson2022evaluation}(I_c, Q_{tn}, q_t, σ_v, \mathrm{soil\_transition}) \\ \hspace{1em} α_M \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( I_c > 2.2, Q_{tn}, 0.0188 \cdot 10^{0.55 I_c + 1.68} \mathclose{}\right) \\ \hspace{1em} α_M \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( α_M, \mathrm{None}, 8 \mathclose{}\right) \\ \hspace{1em} M \gets α_M \cdot \mathopen{}\left( q_t - σ_v \cdot 0.001 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ M \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
M &= \text{Constrained modulus (MPa)}\\
I_c &= \text{Soil behavior type index}\\
Q_{tn} &= \text{Stress-normalized cone resistance}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
σ_v &= \text{Total stress (kPa)}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_corrected_blow_count__robertson2012interpretation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_corrected\_blow\_count\_\_robertson2012interpretation}(q_t, I_c, \mathrm{soil\_transition}) \\ \hspace{1em} N_{60} \gets \frac{1000 q_t}{101.325} \frac{1}{10^{1.1268 - 0.2817 I_c}} \\ \hspace{1em} N_{60} \gets \mathrm{np}.\mathrm{round} \mathopen{}\left( N_{60}, 0 \mathclose{}\right) \\ \hspace{1em} N_{60} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( N_{60}, \mathrm{None}, 100 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ N_{60} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_{60} &= \text{Corrected blow count}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
I_c &= \text{Soil behavior type index}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_corrected_cone_tip_resistance`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_corrected\_cone\_tip\_resistance}(q_c, u, a, \mathrm{is\_invalid\_data}) \\ \hspace{1em} q_t \gets q_c + 0.001 u \cdot \mathopen{}\left( 1 - a \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ q_t \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
q_t &= \text{Corrected cone tip resistance (MPa)}\\
q_c &= \text{Cone tip resistance (MPa)}\\
u &= \text{Pore pressure (kPa)}\\
a &= \text{Cone area ratio}\\
\text{is\_invalid\_data} &= \text{Is invalid data}
\end{align*}
$$

#### `get_cross_correlation_function`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_cross\_correlation\_function}(q_c, f_s, \mathrm{plot\_module}) \\ \hspace{1em} \mathrm{valid\_flag} \gets \mathord{\sim} \mathrm{np}.\mathrm{isnan} \mathopen{}\left( q_c + f_s \mathclose{}\right) \\ \hspace{1em} q_c \gets \mathrm{np}.\mathrm{extract} \mathopen{}\left( \mathrm{valid\_flag}, q_c \mathclose{}\right) \\ \hspace{1em} f_s \gets \mathrm{np}.\mathrm{extract} \mathopen{}\left( \mathrm{valid\_flag}, f_s \mathclose{}\right) \\ \hspace{1em} q_c \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( q_c, 0, \mathrm{None} \mathclose{}\right) \\ \hspace{1em} f_s \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( f_s, 0, \mathrm{None} \mathclose{}\right) \\ \hspace{1em} \mathopen{}\left( \mathrm{lags}, \mathrm{correlation} \mathclose{}\right) \gets \mathrm{\_get\_cross\_correlation\_function} \mathopen{}\left( q_c, f_s \mathclose{}\right) \\ \hspace{1em} \mathrm{correlation\_in\_central\_range} \gets \mathrm{correlation}.\mathrm{copy} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( \mathrm{correlation\_in\_central\_range}, \mathord{\sim} \mathopen{}\left( \mathopen{}\left( \mathrm{lags} \ge -20 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( \mathrm{lags} \le 20 \mathclose{}\right) \mathclose{}\right), -\mathrm{np}.\mathrm{inf} \mathclose{}\right) \\ \hspace{1em} \mathrm{corr\_max\_idx} \gets \mathrm{np}.\mathrm{argmax} \mathopen{}\left( \mathrm{correlation\_in\_central\_range} \mathclose{}\right) \\ \hspace{1em} \mathrm{lag} \gets \mathrm{lags}_{\mathrm{corr\_max\_idx}} \\ \hspace{1em} \mathrm{fig} \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{plot\_module} \not\equiv \mathrm{None} \\ \hspace{2em} \mathrm{corr\_max} \gets \mathrm{correlation}_{\mathrm{corr\_max\_idx}} \\ \hspace{2em} \mathrm{fig} \gets \mathrm{ReferenceFigures}.\mathrm{CrossCorrelation} \mathopen{}\left( \mathclose{}\right).\mathrm{plot} \mathopen{}\left( \mathclose{}\right).\mathrm{fig} \\ \hspace{2em} \mathbf{if} \ \mathrm{plot\_module} = \textrm{"mpl"} \\ \hspace{3em} \mathrm{ax} \gets \mathrm{fig}.\mathrm{get\_axes} \mathopen{}\left( \mathclose{}\right)_{0} \\ \hspace{3em} \mathrm{ax}.\mathrm{plot} \mathopen{}\left( \mathrm{lag}, \mathrm{corr\_max}, \textrm{"ro"} \mathclose{}\right) \\ \hspace{3em} \mathrm{ax}.\mathrm{text} \mathopen{}\left( \mathrm{lag}, \mathrm{corr\_max} + 0.05, \mathrm{str} \mathopen{}\left( \mathrm{lag} \mathclose{}\right) \mathclose{}\right) \\ \hspace{3em} \mathrm{ax}.\mathrm{axvline} \mathopen{}\left( \mathclose{}\right) \\ \hspace{3em} \mathrm{ax}.\mathrm{axhline} \mathopen{}\left( \mathclose{}\right) \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ \mathrm{plot\_module} = \textrm{"plotly"} \\ \hspace{4em} \mathrm{fig}.\mathrm{add\_scatter} \mathopen{}\left( \mathclose{}\right) \\ \hspace{4em} \mathrm{fig}.\mathrm{add\_vline} \mathopen{}\left( \mathclose{}\right) \\ \hspace{4em} \mathrm{fig}.\mathrm{add\_hline} \mathopen{}\left( \mathclose{}\right) \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( \mathrm{lag}, \mathrm{fig} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{cross\_correlation\_lag} &= \text{Cross correlation lag}\\
q_c &= \text{Cone tip resistance (MPa)}\\
f_s &= \text{Sleeve friction (kPa)}
\end{align*}
$$

#### `get_cyclic_resistance_ratio_magnitude_7_5__robertson2009interpretation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_cyclic\_resistance\_ratio\_magnitude\_7\_5\_\_robertson2009interpretation}(Q_{tncs}, \mathrm{is\_potentially\_liquefiable}) \\ \hspace{1em} \textrm{" Performance based earthquake design using the CPT by robertson (2009) "} \\ \hspace{1em} \textrm{" Evaluating cyclic liquefaction potential using the cone penetration test by robertson \& Wride (1998) "} \\ \hspace{1em} CRR_{7.5} \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( Q_{tncs}, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( CRR_{7.5}, \mathopen{}\left( Q_{tncs} < 50 \mathclose{}\right) \mathbin{\&} \mathrm{is\_potentially\_liquefiable}, 0.833 \frac{Q_{tncs}}{1000} + 0.05 \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( CRR_{7.5}, \mathopen{}\left( Q_{tncs} \ge 50 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} < 160 \mathclose{}\right) \mathbin{\&} \mathrm{is\_potentially\_liquefiable}, 93 \mathopen{}\left( \frac{Q_{tncs}}{1000} \mathclose{}\right)^{3} + 0.08 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ CRR_{7.5} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
CRR_{7.5} &= \text{Cyclic resistance ratio magnitude 7.5}\\
Q_{tncs} &= \text{Clean sand normalized cone resistance}\\
\text{is\_potentially\_liquefiable} &= \text{Is potentially liquefiable}
\end{align*}
$$

#### `get_cyclic_resistance_ratio_magnitude_7_5__saye2021common`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_cyclic\_resistance\_ratio\_magnitude\_7\_5\_\_saye2021common}(m_{CRR}, q_{c1}, σ, PL_{liq}) \\ \hspace{1em} \textrm{"
    From author:
    σ = standard deviation and is equal to 0.24 if input parameters for a given soil layer are uncertain, or 0.20 if
    input parameters for a given soil layer are certain. For most typical engineering applications, input parameters for
     liquefaction triggering assessment are based on limited site exploration and laboratory testing data and therefore
      justify σ = 0.24
    Here, we recommend using PL = 35\% with crr7.5 in Eq. (24) to define a deterministic liquefaction resistance
    boundary for use in design
    "} \\ \hspace{1em} CRR_{7.5} \gets 10^{\frac{m_{CRR} \cdot q_{c1}}{101.325} - 1.34 + σ \cdot \mathrm{norm} \mathopen{}\left( \mathclose{}\right).\mathrm{ppf} \mathopen{}\left( \frac{PL_{liq}}{100} \mathclose{}\right)} \\ \hspace{1em} CRR_{7.5} \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( CRR_{7.5} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( CRR_{7.5}, \mathopen{}\left( m_{CRR} > 0.1 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( \frac{q_{c1}}{101.325} > 180 \mathclose{}\right), \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} CRR_{7.5} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( CRR_{7.5}, \mathrm{None}, 4 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ CRR_{7.5} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
CRR_{7.5} &= \text{Cyclic resistance ratio magnitude 7.5}\\
m_{CRR} &= \text{Cyclic resistance ratio slope}\\
q_{c1} &= \text{Overburden normalized cone resistance}\\
σ &= \text{Standard deviation}\\
PL_{liq} &= \text{Liquefaction probability (\%)}
\end{align*}
$$

#### `get_cyclic_resistance_ratio_magnitude_7_5_cpt__boulanger2014cpt`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_cyclic\_resistance\_ratio\_magnitude\_7\_5\_cpt\_\_boulanger2014cpt}(q_{c1Ncs}) \\ \hspace{1em} CRR_{7.5} \gets \exp \mathopen{}\left( \frac{q_{c1Ncs}}{113} + \mathopen{}\left( \frac{q_{c1Ncs}}{1000} \mathclose{}\right)^{2} - \mathopen{}\left( \frac{q_{c1Ncs}}{140} \mathclose{}\right)^{3} + \mathopen{}\left( \frac{q_{c1Ncs}}{137} \mathclose{}\right)^{4} - 2.8 \mathclose{}\right) \\ \hspace{1em} CRR_{7.5} \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( CRR_{7.5} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( CRR_{7.5}, q_{c1Ncs} \ge 211, 2 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ CRR_{7.5} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
CRR_{7.5} &= \text{Cyclic resistance ratio magnitude 7.5}\\
q_{c1Ncs} &= \text{Clean sand normalized cone resistance at 1 atm}
\end{align*}
$$

#### `get_cyclic_resistance_ratio_magnitude_7_5_cpt__idriss2006semi`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_cyclic\_resistance\_ratio\_magnitude\_7\_5\_cpt\_\_idriss2006semi}(q_{c1Ncs}, \mathrm{is\_potentially\_liquefiable}) \\ \hspace{1em} CRR_{7.5} \gets \exp \mathopen{}\left( \frac{q_{c1Ncs}}{540} + \mathopen{}\left( \frac{q_{c1Ncs}}{67} \mathclose{}\right)^{2} - \mathopen{}\left( \frac{q_{c1Ncs}}{80} \mathclose{}\right)^{3} + \mathopen{}\left( \frac{q_{c1Ncs}}{114} \mathclose{}\right)^{4} - 3 \mathclose{}\right) \\ \hspace{1em} CRR_{7.5} \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( CRR_{7.5} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( CRR_{7.5}, q_{c1Ncs} \ge 211, 2 \mathclose{}\right) \\ \hspace{1em} CRR_{7.5} \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( \mathrm{np}.\mathrm{isnan} \mathopen{}\left( CRR_{7.5} \mathclose{}\right) \mathbin{|} \mathord{\sim} \mathrm{is\_potentially\_liquefiable}, 2, CRR_{7.5} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ CRR_{7.5} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
CRR_{7.5} &= \text{Cyclic resistance ratio magnitude 7.5}\\
q_{c1Ncs} &= \text{Clean sand normalized cone resistance at 1 atm}\\
\text{is\_potentially\_liquefiable} &= \text{Is potentially liquefiable}
\end{align*}
$$

#### `get_cyclic_resistance_ratio_slope__saye2021common`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_cyclic\_resistance\_ratio\_slope\_\_saye2021common}(ΔQ) \\ \hspace{1em} m_{CRR} \gets \frac{ΔQ}{178 ΔQ - 3349} \\ \hspace{1em} m_{CRR} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( m_{CRR}, \mathrm{None}, 0.1 \mathclose{}\right) \\ \hspace{1em} m_{CRR} \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( m_{CRR} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( m_{CRR}, ΔQ < 20, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ m_{CRR} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
m_{CRR} &= \text{Cyclic resistance ratio slope}\\
ΔQ &= \text{Soil classification index}
\end{align*}
$$

#### `get_diameter_at_50_percent_finer__saye2017linear`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_diameter\_at\_50\_percent\_finer\_\_saye2017linear}(ΔQ) \\ \hspace{1em} D_{50} \gets \mathrm{DiameterAt50PercentFinerSaye2017Figure}.\mathrm{interpolate\_at\_x} \mathopen{}\left( ΔQ \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ D_{50} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
D_{50} &= \text{Diameter at 50\% finer (mm)}\\
ΔQ &= \text{Soil classification index}
\end{align*}
$$

#### `get_dry_unit_weight__barounis2018estimation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_dry\_unit\_weight\_\_barounis2018estimation}(γ, w_c, \mathrm{soil\_transition}) \\ \hspace{1em} γ_{dry} \gets \frac{γ}{1 + 0.01 w_c} \\ \hspace{1em} \mathbf{return} \ γ_{dry} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
γ_{dry} &= \text{Dry unit weight (kN/m3)}\\
γ &= \text{Unit weight (kN/m3)}\\
w_c &= \text{Water content (\%)}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_effective_cone_resistance__eslami1997pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_effective\_cone\_resistance\_\_eslami1997pile}(q_t, u, \mathrm{is\_invalid\_data}) \\ \hspace{1em} q_E \gets \mathopen{}\left| q_t - \frac{u}{1000} \mathclose{}\right| \\ \hspace{1em} q_E \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( q_E \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ q_E \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
q_E &= \text{Effective cone resistance (MPa)}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
u &= \text{Pore pressure (kPa)}\\
\text{is\_invalid\_data} &= \text{Is invalid data}
\end{align*}
$$

#### `get_effective_cone_resistance_geometric_mean__eslami1997pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_effective\_cone\_resistance\_geometric\_mean\_\_eslami1997pile}(z, q_E, D, \mathrm{pile\_toe\_transition}) \\ \hspace{1em} \mathrm{z\_top} \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{pile\_toe\_transition} = \textrm{"weak\_to\_dense"} \\ \hspace{2em} \mathrm{z\_top} \gets 8 D \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{pile\_toe\_transition} = \textrm{"dense\_to\_weak"} \\ \hspace{3em} \mathrm{z\_top} \gets 2 D \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathrm{z\_bottom} \gets 4 D \\ \hspace{1em} \mathopen{}\left( \mathrm{z\_top\_array}, \mathrm{z\_bottom\_array} \mathclose{}\right) \gets \mathopen{}\left( z - \mathrm{z\_top}, z + \mathrm{z\_bottom} \mathclose{}\right) \\ \hspace{1em} q_{Eg} \gets \mathopen{}\left[  \mathclose{}\right] \\ \hspace{1em} \mathbf{for} \ \mathopen{}\left( \mathrm{z\_top\_}, \mathrm{z\_bottom\_} \mathclose{}\right) \in \mathrm{zip} \mathopen{}\left( \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( \mathrm{z\_top\_array} \mathclose{}\right), \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( \mathrm{z\_bottom\_array} \mathclose{}\right) \mathclose{}\right) \ \mathbf{do} \\ \hspace{2em} \mathrm{effective\_cone\_resistance\_bin} \gets \mathrm{np}.\mathrm{extract} \mathopen{}\left( \mathopen{}\left( \mathrm{z\_top\_} \le z \mathclose{}\right) \mathbin{\&} \mathopen{}\left( z \le \mathrm{z\_bottom\_} \mathclose{}\right), q_E \mathclose{}\right) \\ \hspace{2em} \mathbf{if} \ \mathrm{z\_top\_} \le 0 \\ \hspace{3em} \mathrm{effective\_cone\_resistance\_bin} \gets \mathrm{np}.\mathrm{insert} \mathopen{}\left( \mathrm{effective\_cone\_resistance\_bin}, 0, 0 \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( \mathrm{effective\_cone\_resistance\_bin}, \mathrm{effective\_cone\_resistance\_bin} = 0, 1e-06 \mathclose{}\right) \\ \hspace{2em} \mathrm{effective\_cone\_resistance\_bin} \gets \mathrm{np}.\mathrm{extract} \mathopen{}\left( \mathrm{effective\_cone\_resistance\_bin} > 0, \mathrm{effective\_cone\_resistance\_bin} \mathclose{}\right) \\ \hspace{2em} \mathrm{effective\_cone\_resistance\_geometric\_mean\_bin} \gets \mathrm{gmean} \mathopen{}\left( \mathrm{effective\_cone\_resistance\_bin} \mathclose{}\right) \\ \hspace{2em} q_{Eg}.\mathrm{append} \mathopen{}\left( \mathrm{effective\_cone\_resistance\_geometric\_mean\_bin} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ for} \\ \hspace{1em} \mathbf{return} \ q_{Eg} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
q_{Eg} &= \text{Effective cone resistance geometric mean (MPa)}\\
z &= \text{Depth (m)}\\
q_E &= \text{Effective cone resistance (MPa)}\\
D &= \text{Pile diameter (m)}\\
\text{pile\_toe\_transition} &= \text{Pile toe transition}
\end{align*}
$$

#### `get_elasticity_modulus__robertson2012interpretation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_elasticity\_modulus\_\_robertson2012interpretation}(q_t, σ_v, I_c, \mathrm{is\_invalid\_data}, SBT_n, \mathrm{is\_fine\_soil}, \mathrm{soil\_transition}) \\ \hspace{1em} E_s \gets \mathopen{}\left( q_t - 0.001 σ_v \mathclose{}\right) \cdot 0.015 \cdot 10^{0.55 I_c + 1.68} \\ \hspace{1em} \mathbf{return} \ E_s \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
E_s &= \text{Elasticity modulus (MPa)}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
σ_v &= \text{Total stress (kPa)}\\
I_c &= \text{Soil behavior type index}\\
\text{is\_invalid\_data} &= \text{Is invalid data}\\
SBT_n &= \text{Normalized soil behavior type}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_equivalent_cone_resistance__bustamante1982pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_equivalent\_cone\_resistance\_\_bustamante1982pile}(z, q_t, D) \\ \hspace{1em} \mathrm{z\_offset} \gets 1.5 D \\ \hspace{1em} \mathopen{}\left( z_{top}, z_{bottom} \mathclose{}\right) \gets \mathopen{}\left( z - \mathrm{z\_offset}, z + \mathrm{z\_offset} \mathclose{}\right) \\ \hspace{1em} \mathopen{}\left( q'_{ca}, q_{ca} \mathclose{}\right) \gets \mathrm{\_get\_equivalent\_cone\_resistance\_\_bustamante1982pile\_vec} \mathopen{}\left( q_t, z, z_{top}, z_{bottom} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( q'_{ca}, q_{ca} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
q'_{ca} &= \text{Equivalent cone resistance primed (MPa)}\\
q_{ca} &= \text{Equivalent cone resistance (MPa)}\\
z &= \text{Depth (m)}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
D &= \text{Pile diameter (m)}
\end{align*}
$$

#### `get_fines_content__boulanger2014cpt`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_fines\_content\_\_boulanger2014cpt}(I_c, C(FC)) \\ \hspace{1em} FC \gets 80 \mathopen{}\left( I_c + C(FC) \mathclose{}\right) - 137 \\ \hspace{1em} FC \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( FC, 0, 100 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ FC \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
FC &= \text{Fines content (\%)}\\
I_c &= \text{Soil behavior type index}\\
C(FC) &= \text{Fines content fitting parameter}
\end{align*}
$$

#### `get_fines_content__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_fines\_content\_\_idriss2008soil}(I_c) \\ \hspace{1em} FC \gets 2.8 I_c^{2.6} \\ \hspace{1em} FC \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( FC, 0, 100 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ FC \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
FC &= \text{Fines content (\%)}\\
I_c &= \text{Soil behavior type index}
\end{align*}
$$

#### `get_fines_content__robertson1998evaluating`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_fines\_content\_\_robertson1998evaluating}(I_c, F_r) \\ \hspace{1em} \mathrm{conditions} \gets \mathopen{}\left[ I_c \le 1.26, \mathopen{}\left( I_c > 1.26 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( I_c \le 3.5 \mathclose{}\right), I_c > 3.5, \mathopen{}\left( I_c \ge 1.64 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( I_c \le 2.36 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( F_r < 0.5 \mathclose{}\right) \mathclose{}\right] \\ \hspace{1em} \mathrm{choices} \gets \mathopen{}\left[ 0, 1.75 I_c^{3.25} - 3.7, 100, 5 \mathclose{}\right] \\ \hspace{1em} FC \gets \mathrm{np}.\mathrm{select} \mathopen{}\left( \mathrm{conditions}, \mathrm{choices} \mathclose{}\right) \\ \hspace{1em} FC \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( FC, \mathrm{None}, 100 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ FC \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
FC &= \text{Fines content (\%)}\\
I_c &= \text{Soil behavior type index}\\
F_r &= \text{Normalized friction ratio (\%)}
\end{align*}
$$

#### `get_fines_content__saye2017linear`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_fines\_content\_\_saye2017linear}(ΔQ) \\ \hspace{1em} FC \gets \mathrm{FinesContentSaye2017Figure}.\mathrm{interpolate\_at\_x} \mathopen{}\left( ΔQ \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ FC \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
FC &= \text{Fines content (\%)}\\
ΔQ &= \text{Soil classification index}
\end{align*}
$$

#### `get_friction_angle__kulhawy1990manual`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_friction\_angle\_\_kulhawy1990manual}(Q_{tn}, \mathrm{is\_fine\_soil}) \\ \hspace{1em} ϕ \gets 17.6 + 11 \log_{10} Q_{tn} \\ \hspace{1em} \mathbf{return} \ ϕ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ϕ &= \text{Friction angle (°)}\\
Q_{tn} &= \text{Stress-normalized cone resistance}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_friction_angle__robertson2012interpretation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_friction\_angle\_\_robertson2012interpretation}(ϕ_{cv}, Q_{tncs}, \mathrm{is\_invalid\_data}, SBT_n, \mathrm{is\_fine\_soil}, \mathrm{soil\_transition}) \\ \hspace{1em} ϕ \gets ϕ_{cv} + 15.84 \log_{10} Q_{tncs} - 26.88 \\ \hspace{1em} ϕ \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( ϕ, ϕ_{cv}, \mathrm{None} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ ϕ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ϕ &= \text{Friction angle (°)}\\
ϕ_{cv} &= \text{Constant volume friction angle (°)}\\
Q_{tncs} &= \text{Clean sand normalized cone resistance}\\
\text{is\_invalid\_data} &= \text{Is invalid data}\\
SBT_n &= \text{Normalized soil behavior type}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_friction_ratio`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_friction\_ratio}(f_s, q_t) \\ \hspace{1em} R_f \gets \frac{0.1 f_s}{q_t} \\ \hspace{1em} \mathbf{return} \ R_f \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
R_f &= \text{Friction ratio (\%)}\\
f_s &= \text{Sleeve friction (kPa)}\\
q_t &= \text{Corrected cone tip resistance (MPa)}
\end{align*}
$$

#### `get_is_fine_soil_bustamante1982fellenius`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_is\_fine\_soil\_bustamante1982fellenius}(\mathrm{soil\_type\_index}) \\ \hspace{1em} \mathrm{is\_fine\_soil} \gets \mathrm{np}.\mathrm{isin} \mathopen{}\left( \mathrm{soil\_type\_index}, \mathopen{}\left[ \textrm{"0"}, \textrm{"1"}, \textrm{"2"}, \textrm{"3"} \mathclose{}\right] \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{is\_fine\_soil} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{soil\_type\_index} &= \text{Soil type index}
\end{align*}
$$

#### `get_is_fine_soil_cpt`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_is\_fine\_soil\_cpt}(\mathrm{is\_fine\_soil\_criteria}, SBT_n, I_c, I_{c\ cutoff}) \\ \hspace{1em} \mathrm{is\_fine\_soil} \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{is\_fine\_soil\_criteria} = \textrm{"sbtn"} \\ \hspace{2em} \mathrm{is\_fine\_soil} \gets \mathrm{np}.\mathrm{isin} \mathopen{}\left( SBT_n, \mathopen{}\left[ \textrm{"1"}, \textrm{"2"}, \textrm{"3"}, \textrm{"4"}, \textrm{"9"} \mathclose{}\right] \mathclose{}\right) \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{is\_fine\_soil\_criteria} = \textrm{"ic\_cutoff"} \\ \hspace{3em} \mathrm{is\_fine\_soil} \gets I_c > I_{c\ cutoff} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathrm{is\_fine\_soil} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{is\_fine\_soil\_criteria} &= \text{Is fine soil criteria}\\
SBT_n &= \text{Normalized soil behavior type}\\
I_c &= \text{Soil behavior type index}\\
I_{c\ cutoff} &= \text{Soil behavior type index cutoff}
\end{align*}
$$

#### `get_is_invalid_data`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_is\_invalid\_data}(q_c) \\ \hspace{1em} \mathrm{is\_invalid\_data} \gets \mathrm{np}.\mathrm{isin} \mathopen{}\left( q_c, \mathopen{}\left[ -9999, -8888, -7777, -9876 \mathclose{}\right] \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{is\_invalid\_data} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{is\_invalid\_data} &= \text{Is invalid data}\\
q_c &= \text{Cone tip resistance (MPa)}
\end{align*}
$$

#### `get_is_potentially_liquefiable_cpt`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_is\_potentially\_liquefiable\_cpt}(\mathrm{below\_water\_table}, z, LIQ_{max\ z}, \mathrm{is\_fine\_soil}, \mathrm{soil\_transition}) \\ \hspace{1em} \mathbf{if} \ \mathrm{np}.\mathrm{isnan} \mathopen{}\left( LIQ_{max\ z} \mathclose{}\right) \\ \hspace{2em} LIQ_{max\ z} \gets \mathrm{np}.\mathrm{inf} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathrm{is\_potentially\_liquefiable} \gets \mathrm{below\_water\_table} \mathbin{\&} \mathopen{}\left( z \le LIQ_{max\ z} \mathclose{}\right) \mathbin{\&} \mathord{\sim} \mathrm{is\_fine\_soil} \mathbin{\&} \mathord{\sim} \mathrm{soil\_transition} \\ \hspace{1em} \mathbf{return} \ \mathrm{is\_potentially\_liquefiable} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{is\_potentially\_liquefiable} &= \text{Is potentially liquefiable}\\
\text{below\_water\_table} &= \text{Below water table}\\
z &= \text{Depth (m)}\\
LIQ_{max\ z} &= \text{Liquefaction max. depth (m)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_iterative_parameters_cpt__boulanger2014cpt`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_iterative\_parameters\_cpt\_\_boulanger2014cpt}(q_c, FC, σ_v', \mathrm{is\_invalid\_data}, \mathrm{is\_fine\_soil}) \\ \hspace{1em} n \gets \mathrm{None} \\ \hspace{1em} C_n \gets \mathrm{None} \\ \hspace{1em} Δq_{c1N} \gets \mathrm{None} \\ \hspace{1em} q_{c1Ncs} \gets \mathrm{None} \\ \hspace{1em} q_{c1N} \gets \mathrm{np}.\mathrm{ones\_like} \mathopen{}\left( q_c \mathclose{}\right) \\ \hspace{1em} \mathbf{for} \ \mathrm{\_} \in \mathrm{range} \mathopen{}\left( \mathrm{MAX\_ITER} \mathclose{}\right) \ \mathbf{do} \\ \hspace{2em} \mathrm{normalized\_cone\_resistance\_1atm\_old} \gets q_{c1N}.\mathrm{copy} \mathopen{}\left( \mathclose{}\right) \\ \hspace{2em} Δq_{c1N} \gets \mathopen{}\left( 11.9 + \frac{q_{c1N}}{14.6} \mathclose{}\right) \exp \mathopen{}\left( 1.63 - \frac{9.7}{FC + 2} - \mathopen{}\left( \frac{15.7}{FC + 2} \mathclose{}\right)^{2} \mathclose{}\right) \\ \hspace{2em} Δq_{c1N} \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( Δq_{c1N} \mathclose{}\right) \\ \hspace{2em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( Δq_{c1N}, \mathrm{np}.\mathrm{isclose} \mathopen{}\left( Δq_{c1N}, 0 \mathclose{}\right), 0 \mathclose{}\right) \\ \hspace{2em} q_{c1Ncs} \gets q_{c1N} + Δq_{c1N} \\ \hspace{2em} n \gets 1.338 - 0.249 \mathopen{}\left( \mathrm{np}.\mathrm{clip} \mathopen{}\left( q_{c1Ncs}, 21, 254 \mathclose{}\right) \mathclose{}\right)^{0.264} \\ \hspace{2em} C_n \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( \mathopen{}\left( \frac{101.325}{σ_v'} \mathclose{}\right)^{n}, 0, 1.7 \mathclose{}\right) \\ \hspace{2em} q_{c1N} \gets \frac{q_c \cdot 1000}{101.325} \cdot C_n \\ \hspace{2em} \mathbf{if} \ \mathrm{np}.\mathrm{nanmax} \mathopen{}\left( \mathopen{}\left| q_{c1N} - \mathrm{normalized\_cone\_resistance\_1atm\_old} \mathclose{}\right| \mathclose{}\right) < \mathrm{TOL} \\ \hspace{3em} \mathbf{break} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ for} \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( n, C_n, q_{c1N}, Δq_{c1N}, q_{c1Ncs} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
n &= \text{Overburden stress exponent}\\
C_n &= \text{Overburden correction}\\
q_{c1N} &= \text{Normalized cone resistance at 1 atm}\\
Δq_{c1N} &= \text{Normalized cone resistance fines inc.}\\
q_{c1Ncs} &= \text{Clean sand normalized cone resistance at 1 atm}\\
q_c &= \text{Cone tip resistance (MPa)}\\
FC &= \text{Fines content (\%)}\\
σ_v' &= \text{Effective stress (kPa)}\\
\text{is\_invalid\_data} &= \text{Is invalid data}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_iterative_parameters_cpt__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_iterative\_parameters\_cpt\_\_idriss2008soil}(q_c, FC, σ_v', \mathrm{is\_invalid\_data}, \mathrm{is\_fine\_soil}) \\ \hspace{1em} n \gets \mathrm{None} \\ \hspace{1em} C_n \gets \mathrm{None} \\ \hspace{1em} Δq_{c1N} \gets \mathrm{None} \\ \hspace{1em} q_{c1Ncs} \gets \mathrm{None} \\ \hspace{1em} q_{c1N} \gets \mathrm{np}.\mathrm{ones\_like} \mathopen{}\left( q_c \mathclose{}\right) \\ \hspace{1em} \mathbf{for} \ \mathrm{\_} \in \mathrm{range} \mathopen{}\left( \mathrm{MAX\_ITER} \mathclose{}\right) \ \mathbf{do} \\ \hspace{2em} \mathrm{normalized\_cone\_resistance\_1atm\_old} \gets q_{c1N}.\mathrm{copy} \mathopen{}\left( \mathclose{}\right) \\ \hspace{2em} Δq_{c1N} \gets \mathopen{}\left( 5.4 + \frac{q_{c1N}}{16} \mathclose{}\right) \exp \mathopen{}\left( 1.63 + \frac{9.7}{FC + 0.01} - \mathopen{}\left( \frac{15.7}{FC + 0.01} \mathclose{}\right)^{2} \mathclose{}\right) \\ \hspace{2em} Δq_{c1N} \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( Δq_{c1N} \mathclose{}\right) \\ \hspace{2em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( Δq_{c1N}, \mathrm{np}.\mathrm{isclose} \mathopen{}\left( Δq_{c1N}, 0 \mathclose{}\right), 0 \mathclose{}\right) \\ \hspace{2em} q_{c1Ncs} \gets q_{c1N} + Δq_{c1N} \\ \hspace{2em} n \gets 1.338 - 0.249 \mathopen{}\left( \mathrm{np}.\mathrm{clip} \mathopen{}\left( q_{c1Ncs}, 21, 254 \mathclose{}\right) \mathclose{}\right)^{0.264} \\ \hspace{2em} C_n \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( \mathopen{}\left( \frac{101.325}{σ_v'} \mathclose{}\right)^{n}, 0, 1.7 \mathclose{}\right) \\ \hspace{2em} q_{c1N} \gets \frac{q_c \cdot 1000}{101.325} \cdot C_n \\ \hspace{2em} \mathbf{if} \ \mathrm{np}.\mathrm{nanmax} \mathopen{}\left( \mathopen{}\left| q_{c1N} - \mathrm{normalized\_cone\_resistance\_1atm\_old} \mathclose{}\right| \mathclose{}\right) < \mathrm{TOL} \\ \hspace{3em} \mathbf{break} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ for} \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( n, C_n, q_{c1N}, Δq_{c1N}, q_{c1Ncs} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
n &= \text{Overburden stress exponent}\\
C_n &= \text{Overburden correction}\\
q_{c1N} &= \text{Normalized cone resistance at 1 atm}\\
Δq_{c1N} &= \text{Normalized cone resistance fines inc.}\\
q_{c1Ncs} &= \text{Clean sand normalized cone resistance at 1 atm}\\
q_c &= \text{Cone tip resistance (MPa)}\\
FC &= \text{Fines content (\%)}\\
σ_v' &= \text{Effective stress (kPa)}\\
\text{is\_invalid\_data} &= \text{Is invalid data}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_magnitude_scaling_factor_max_cpt__boulanger2014cpt`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_magnitude\_scaling\_factor\_max\_cpt\_\_boulanger2014cpt}(q_{c1Ncs}) \\ \hspace{1em} MSF_{max} \gets 1.09 + \mathopen{}\left( \frac{q_{c1Ncs}}{180} \mathclose{}\right)^{3} \\ \hspace{1em} MSF_{max} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( MSF_{max}, \mathrm{None}, 2.2 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ MSF_{max} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
MSF_{max} &= \text{Magnitude scaling factor max.}\\
q_{c1Ncs} &= \text{Clean sand normalized cone resistance at 1 atm}
\end{align*}
$$

#### `get_max_shear_strain__zhang2004estimating`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_max\_shear\_strain\_\_zhang2004estimating}(D_r, FS_{liq}) \\ \hspace{1em} γ_{max} \gets \mathrm{\_get\_max\_shear\_strain\_\_zhang2004estimating\_vec} \mathopen{}\left( FS_{liq}, D_r \mathclose{}\right) \\ \hspace{1em} γ_{max} \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( \mathrm{np}.\mathrm{isnan} \mathopen{}\left( γ_{max} \mathclose{}\right) \mathbin{|} \mathopen{}\left( FS_{liq} \ge 2 \mathclose{}\right), 0, γ_{max} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ γ_{max} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
γ_{max} &= \text{Max. shear strain (\%)}\\
D_r &= \text{Relative density (\%)}\\
FS_{liq} &= \text{Liquefaction safety factor}
\end{align*}
$$

#### `get_max_shear_strain_f_alpha_term_cpt__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_max\_shear\_strain\_f\_alpha\_term\_cpt\_\_idriss2008soil}(q_{c1Ncs}) \\ \hspace{1em} q_{c1Ncs} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( q_{c1Ncs}, 69, \mathrm{None} \mathclose{}\right) \\ \hspace{1em} F_α \gets -11.74 + 8.34 q_{c1Ncs}^{0.264} - 1.371 q_{c1Ncs}^{0.528} \\ \hspace{1em} F_α \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( F_α \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ F_α \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
F_α &= \text{Max. shear strain Fα term}\\
q_{c1Ncs} &= \text{Clean sand normalized cone resistance at 1 atm}
\end{align*}
$$

#### `get_mean_corrected_cone_tip_resistance`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_mean\_corrected\_cone\_tip\_resistance}(D_f, z_{infl}, z, q_t) \\ \hspace{1em} \mathrm{depth\_rounded} \gets \mathrm{np}.\mathrm{round} \mathopen{}\left( z, 5 \mathclose{}\right) \\ \hspace{1em} \mathrm{flag1} \gets \mathrm{np}.\mathrm{round} \mathopen{}\left( D_f, 5 \mathclose{}\right) \le \mathrm{depth\_rounded} \\ \hspace{1em} \mathrm{flag2} \gets \mathrm{depth\_rounded} \le \mathrm{np}.\mathrm{round} \mathopen{}\left( z_{infl}, 5 \mathclose{}\right) \\ \hspace{1em} \mathrm{flag} \gets \mathrm{flag1} \mathbin{\&} \mathrm{flag2} \\ \hspace{1em} q_t \gets \mathrm{np}.\mathrm{broadcast\_to} \mathopen{}\left( q_t, \mathrm{flag}.\mathrm{shape} \mathclose{}\right).\mathrm{copy} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( q_t, \mathord{\sim} \mathrm{flag}, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} q_{t\ mean} \gets \mathrm{np}.\mathrm{nanmean} \mathopen{}\left( q_t \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ q_{t\ mean} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
q_{t\ mean} &= \text{Mean corrected cone tip resistance (MPa)}\\
D_f &= \text{Footing embedment (m)}\\
z_{infl} &= \text{Footing influence depth (m)}\\
z &= \text{Depth (m)}\\
q_t &= \text{Corrected cone tip resistance (MPa)}
\end{align*}
$$

#### `get_modified_soil_behavior_type`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_modified\_soil\_behavior\_type}(F_r, Q_{tn}) \\ \hspace{1em} SBT_{n\ mod} \gets \mathrm{ModifiedSoilBehaviourTypeFigure}.\mathrm{assign\_polygons\_labels\_from\_xy\_data} \mathopen{}\left( F_r, Q_{tn} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ SBT_{n\ mod} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
SBT_{n\ mod} &= \text{Modified soil behavior type}\\
F_r &= \text{Normalized friction ratio (\%)}\\
Q_{tn} &= \text{Stress-normalized cone resistance}
\end{align*}
$$

#### `get_modified_soil_behavior_type_index`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_modified\_soil\_behavior\_type\_index}(Q_{tn}, F_r) \\ \hspace{1em} \textrm{" CPT-based Soil Behaviour Type (SBT) Classification System – an update by robertson (2016) "} \\ \hspace{1em} I_B \gets \frac{100 \mathopen{}\left( Q_{tn} + 10 \mathclose{}\right)}{Q_{tn} \cdot F_r + 70} \\ \hspace{1em} \mathbf{return} \ I_B \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
I_B &= \text{Modified soil behaviour type index}\\
Q_{tn} &= \text{Stress-normalized cone resistance}\\
F_r &= \text{Normalized friction ratio (\%)}
\end{align*}
$$

#### `get_modified_soil_behavior_type_label`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_modified\_soil\_behavior\_type\_label}(SBT_{n\ mod}) \\ \hspace{1em} SBT_{n\ mod\ label} \gets \mathrm{replace\_from\_mapping} \mathopen{}\left( SBT_{n\ mod}, \mathrm{PARAMETERS}.\mathrm{get\_pair\_discrete\_field\_mapping} \mathopen{}\left( \textrm{"modified\_soil\_behavior\_type"}, \textrm{"modified\_soil\_behavior\_type\_label"} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ SBT_{n\ mod\ label} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
SBT_{n\ mod\ label} &= \text{Modified soil behavior type label}\\
SBT_{n\ mod} &= \text{Modified soil behavior type}
\end{align*}
$$

#### `get_nature_of_soil__bustamante1982pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_nature\_of\_soil\_\_bustamante1982pile}(R_f, Q_{tn}) \\ \hspace{1em} \mathrm{nature\_of\_soil} \gets \mathrm{NatureOfSoilFigure}.\mathrm{assign\_polygons\_labels\_from\_xy\_data} \mathopen{}\left( R_f, Q_{tn} \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( \mathrm{nature\_of\_soil}, R_f < 0.1, \textrm{"6"} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{nature\_of\_soil} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{nature\_of\_soil} &= \text{Nature of soil}\\
R_f &= \text{Friction ratio (\%)}\\
Q_{tn} &= \text{Stress-normalized cone resistance}
\end{align*}
$$

#### `get_non_normalized_soil_behavior_type_index`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_non\_normalized\_soil\_behavior\_type\_index}(q_t, R_f) \\ \hspace{1em} I_{SBT} \gets \mathrm{get\_soil\_behavior\_type\_index} \mathopen{}\left( \frac{1000 q_t}{101.325}, R_f \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ I_{SBT} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
I_{SBT} &= \text{Non normalized soil behavior type index}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
R_f &= \text{Friction ratio (\%)}
\end{align*}
$$

#### `get_normalized_cone_resistance`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_cone\_resistance}(q_t) \\ \hspace{1em} Q_t \gets \frac{1000 q_t}{101.325} \\ \hspace{1em} \mathbf{return} \ Q_t \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_t &= \text{Normalized cone resistance}\\
q_t &= \text{Corrected cone tip resistance (MPa)}
\end{align*}
$$

#### `get_normalized_cone_resistance_fines_inc_sr__seed1987design`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_cone\_resistance\_fines\_inc\_sr\_\_seed1987design}(FC, \mathrm{is\_fine\_soil}) \\ \hspace{1em} Δq_{c1N-Sr} \gets \mathrm{NormalizedConeResistanceFinesIncSeed1987Figure}.\mathrm{interpolate\_at\_x} \mathopen{}\left( FC \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ Δq_{c1N-Sr} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Δq_{c1N-Sr} &= \text{Normalized cone resistance fines inc. (Sr)}\\
FC &= \text{Fines content (\%)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_normalized_friction_ratio`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_friction\_ratio}(f_s, q_t, σ_v) \\ \hspace{1em} \textrm{" Soil classification using the cone penetration test by robertson (1990)"} \\ \hspace{1em} F_r \gets \frac{100 f_s}{\frac{q_t}{0.001} - σ_v} \\ \hspace{1em} \mathbf{return} \ F_r \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
F_r &= \text{Normalized friction ratio (\%)}\\
f_s &= \text{Sleeve friction (kPa)}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
σ_v &= \text{Total stress (kPa)}
\end{align*}
$$

#### `get_normalized_pore_pressure`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_pore\_pressure}(u, u_0, σ_v', \mathrm{is\_invalid\_data}) \\ \hspace{1em} U_2 \gets \frac{u - u_0}{σ_v'} \\ \hspace{1em} \mathbf{return} \ U_2 \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
U_2 &= \text{Normalized pore pressure}\\
u &= \text{Pore pressure (kPa)}\\
u_0 &= \text{Pore water pressure (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
\text{is\_invalid\_data} &= \text{Is invalid data}
\end{align*}
$$

#### `get_normalized_pore_pressure_ratio`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_pore\_pressure\_ratio}(u, u_0, q_t, σ_v) \\ \hspace{1em} \textrm{" Soil classification using the cone penetration test by robertson (1990)"} \\ \hspace{1em} B_q \gets \frac{u - u_0}{q_t \cdot 1000 - σ_v} \\ \hspace{1em} \mathbf{return} \ B_q \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
B_q &= \text{Normalized pore pressure ratio}\\
u &= \text{Pore pressure (kPa)}\\
u_0 &= \text{Pore water pressure (kPa)}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
σ_v &= \text{Total stress (kPa)}
\end{align*}
$$

#### `get_normalized_residual_shear_strength__robertson2022evaluation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_residual\_shear\_strength\_\_robertson2022evaluation}(Q_{tncs}, I_c, f_s, σ_v', ϕ_{cv}, τ, SBT_n, \mathrm{soil\_transition}) \\ \hspace{1em} \mathrm{is\_fine\_soil} \gets \mathrm{get\_is\_fine\_soil\_cpt} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} S_{r\ ratio} \gets 0.0007 \exp \mathopen{}\left( 0.084 Q_{tncs} \mathclose{}\right) + \frac{0.3}{Q_{tncs}} \\ \hspace{1em} \mathbf{if} \ \mathrm{use\_constant\_volume\_friction\_angle} \\ \hspace{2em} ϕ \gets ϕ_{cv} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} ϕ \gets \mathrm{get\_friction\_angle\_\_robertson2012interpretation} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathrm{conditions} \gets \mathopen{}\left[ \mathopen{}\left( I_c < 3 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} < 20 \mathclose{}\right), \mathopen{}\left( I_c < 3 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \ge 20 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} < 80 \mathclose{}\right), \mathopen{}\left( I_c < 3 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \ge 80 \mathclose{}\right), I_c \ge 3 \mathclose{}\right] \\ \hspace{1em} \mathrm{choices} \gets \mathopen{}\left[ 0.02, S_{r\ ratio}, \mathrm{np}.\mathrm{clip} \mathopen{}\left( \mathrm{np}.\mathrm{where} \mathopen{}\left( \mathrm{is\_fine\_soil}, \mathrm{tandg} \mathopen{}\left( ϕ \mathclose{}\right), \mathrm{np}.\mathrm{where} \mathopen{}\left( σ_v' \ne 0, \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( \frac{τ}{σ_v'} \mathclose{}\right), \mathrm{tandg} \mathopen{}\left( ϕ \mathclose{}\right) \mathclose{}\right) \mathclose{}\right), \mathrm{None}, S_{r\ ratio} \mathclose{}\right), \mathrm{np}.\mathrm{where} \mathopen{}\left( σ_v' \ne 0, \frac{f_s}{σ_v'}, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \mathclose{}\right] \\ \hspace{1em} S_{r\ ratio} \gets \mathrm{np}.\mathrm{select} \mathopen{}\left( \mathrm{conditions}, \mathrm{choices} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ S_{r\ ratio} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_{r\ ratio} &= \text{Normalized residual shear strength}\\
Q_{tncs} &= \text{Clean sand normalized cone resistance}\\
I_c &= \text{Soil behavior type index}\\
f_s &= \text{Sleeve friction (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
ϕ_{cv} &= \text{Constant volume friction angle (°)}\\
τ &= \text{Shear strength (kPa)}\\
SBT_n &= \text{Normalized soil behavior type}\\
\text{soil\_transition} &= \text{Soil transition}\\
\text{use\_constant\_volume\_friction\_angle} &= \text{Use constant volume friction angle}
\end{align*}
$$

#### `get_normalized_residual_shear_strength_cpt__idriss2007spt`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_residual\_shear\_strength\_cpt\_\_idriss2007spt}(q_{c1Ncs}, ϕ, \mathrm{void\_redistribution\_is\_significant}, \mathrm{is\_fine\_soil}) \\ \hspace{1em} \textrm{" Equation obtained from Soil liquefaction during earthquakes by Idriss and Boulanger (2008) "} \\ \hspace{1em} S_{r\ ratio} \gets \exp \mathopen{}\left( \frac{q_{c1Ncs}}{24.5} - \mathopen{}\left( \frac{q_{c1Ncs}}{61.7} \mathclose{}\right)^{2} + \mathopen{}\left( \frac{q_{c1Ncs}}{106} \mathclose{}\right)^{3} - 4.42 \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ \lnot \mathrm{void\_redistribution\_is\_significant} \\ \hspace{2em} S_{r\ ratio} \gets S_{r\ ratio} \cdot \mathopen{}\left( 1 + \exp \mathopen{}\left( \frac{q_{c1Ncs}}{11.1} - 9.82 \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} S_{r\ ratio} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( S_{r\ ratio}, 0, \mathrm{tandg} \mathopen{}\left( ϕ \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ S_{r\ ratio} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_{r\ ratio} &= \text{Normalized residual shear strength}\\
q_{c1Ncs} &= \text{Clean sand normalized cone resistance at 1 atm}\\
ϕ &= \text{Friction angle (°)}\\
\text{void\_redistribution\_is\_significant} &= \text{Void redistribution is significant}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_normalized_residual_shear_strength_cpt__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_residual\_shear\_strength\_cpt\_\_idriss2008soil}(q_{c1Ncs-Sr}, ϕ, \mathrm{void\_redistribution\_is\_significant}, \mathrm{is\_fine\_soil}) \\ \hspace{1em} \mathbf{return} \ \mathrm{get\_normalized\_residual\_shear\_strength\_cpt\_\_idriss2007spt} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_{r\ ratio} &= \text{Normalized residual shear strength}\\
q_{c1Ncs-Sr} &= \text{Clean sand normalized cone resistance at 1 atm (Sr)}\\
ϕ &= \text{Friction angle (°)}\\
\text{void\_redistribution\_is\_significant} &= \text{Void redistribution is significant}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_normalized_residual_shear_strength_liq__robertson2022evaluation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_residual\_shear\_strength\_liq\_\_robertson2022evaluation}(Q_{tncs}, I_c, f_s, σ_v', ϕ_{cv}, τ, SBT_n) \\ \hspace{1em} \mathbf{return} \ \mathrm{get\_normalized\_residual\_shear\_strength\_\_robertson2022evaluation} \mathopen{}\left( \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_{r\ ratio} &= \text{Normalized residual shear strength}\\
Q_{tncs} &= \text{Clean sand normalized cone resistance}\\
I_c &= \text{Soil behavior type index}\\
f_s &= \text{Sleeve friction (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
ϕ_{cv} &= \text{Constant volume friction angle (°)}\\
τ &= \text{Shear strength (kPa)}\\
SBT_n &= \text{Normalized soil behavior type}
\end{align*}
$$

#### `get_normalized_soil_behavior_type`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_soil\_behavior\_type}(F_r, Q_{tn}) \\ \hspace{1em} SBT_n \gets \mathrm{NormalizedSoilBehaviourTypeFigure}.\mathrm{assign\_polygons\_labels\_from\_xy\_data} \mathopen{}\left( F_r, Q_{tn} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ SBT_n \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
SBT_n &= \text{Normalized soil behavior type}\\
F_r &= \text{Normalized friction ratio (\%)}\\
Q_{tn} &= \text{Stress-normalized cone resistance}
\end{align*}
$$

#### `get_normalized_soil_behavior_type_label`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_normalized\_soil\_behavior\_type\_label}(SBT_n) \\ \hspace{1em} SBT_{n\ label} \gets \mathrm{replace\_from\_mapping} \mathopen{}\left( SBT_n, \mathrm{PARAMETERS}.\mathrm{get\_pair\_discrete\_field\_mapping} \mathopen{}\left( \textrm{"normalized\_soil\_behavior\_type"}, \textrm{"normalized\_soil\_behavior\_type\_label"} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ SBT_{n\ label} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
SBT_{n\ label} &= \text{Normalized soil behavior type label}\\
SBT_n &= \text{Normalized soil behavior type}
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

#### `get_overburden_correction_coefficient_cpt__idriss2006semi`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overburden\_correction\_coefficient\_cpt\_\_idriss2006semi}(q_{c1N}) \\ \hspace{1em} q_{c1N} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( q_{c1N}, \mathrm{None}, 211 \mathclose{}\right) \\ \hspace{1em} C_σ \gets \frac{1}{37.3 - 8.27 q_{c1N}^{0.264}} \\ \hspace{1em} \mathbf{return} \ C_σ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_σ &= \text{Overburden correction coefficient}\\
q_{c1N} &= \text{Normalized cone resistance at 1 atm}
\end{align*}
$$

#### `get_overburden_correction_coefficient_cpt__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overburden\_correction\_coefficient\_cpt\_\_idriss2008soil}(q_{c1Ncs}) \\ \hspace{1em} \mathbf{return} \ \mathrm{get\_overburden\_correction\_coefficient\_cpt\_\_idriss2006semi} \mathopen{}\left( q_{c1Ncs} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_σ &= \text{Overburden correction coefficient}\\
q_{c1Ncs} &= \text{Clean sand normalized cone resistance at 1 atm}
\end{align*}
$$

#### `get_overburden_normalized_cone_resistance__saye2021common`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overburden\_normalized\_cone\_resistance\_\_saye2021common}(q_c, C_n) \\ \hspace{1em} q_{c1} \gets q_c \cdot 1000 C_n \\ \hspace{1em} \mathbf{return} \ q_{c1} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
q_{c1} &= \text{Overburden normalized cone resistance}\\
q_c &= \text{Cone tip resistance (MPa)}\\
C_n &= \text{Overburden correction}
\end{align*}
$$

#### `get_overburden_stress_exponent__robertson2009interpretation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overburden\_stress\_exponent\_\_robertson2009interpretation}(q_t, σ_v, σ_v', F_r, \mathrm{is\_invalid\_data}) \\ \hspace{1em} n \gets \mathrm{np}.\mathrm{ones\_like} \mathopen{}\left( q_t \mathclose{}\right) \\ \hspace{1em} \mathbf{for} \ \mathrm{\_} \in \mathrm{range} \mathopen{}\left( \mathrm{MAX\_ITER} \mathclose{}\right) \ \mathbf{do} \\ \hspace{2em} \mathrm{overburden\_stress\_exponent\_old} \gets n.\mathrm{copy} \mathopen{}\left( \mathclose{}\right) \\ \hspace{2em} Q_{tn} \gets \mathrm{get\_stress\_normalized\_cone\_resistance} \mathopen{}\left( q_t, σ_v, \mathrm{get\_overburden\_correction\_\_liao1986overburden} \mathopen{}\left( n, σ_v' \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} I_c \gets \mathrm{get\_soil\_behavior\_type\_index} \mathopen{}\left( Q_{tn}, F_r \mathclose{}\right) \\ \hspace{2em} n \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( 0.381 I_c + 0.05 \frac{σ_v'}{101.325} - 0.15, 0, 1 \mathclose{}\right) \\ \hspace{2em} \mathbf{if} \ \mathrm{np}.\mathrm{nanmax} \mathopen{}\left( \mathopen{}\left| n - \mathrm{overburden\_stress\_exponent\_old} \mathclose{}\right| \mathclose{}\right) < \mathrm{TOL} \\ \hspace{3em} \mathbf{break} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ for} \\ \hspace{1em} \mathbf{return} \ n \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
n &= \text{Overburden stress exponent}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
σ_v &= \text{Total stress (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
F_r &= \text{Normalized friction ratio (\%)}\\
\text{is\_invalid\_data} &= \text{Is invalid data}
\end{align*}
$$

#### `get_overconsolidation_ratio__robertson2012interpretation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overconsolidation\_ratio\_\_robertson2012interpretation}(k, Q_{tn}, \mathrm{is\_fine\_soil}, \mathrm{soil\_transition}) \\ \hspace{1em} OCR \gets k \cdot Q_{tn} \\ \hspace{1em} \mathbf{return} \ OCR \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
OCR &= \text{Overconsolidation ratio}\\
k &= \text{Overconsolidation ratio factor}\\
Q_{tn} &= \text{Stress-normalized cone resistance}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_overconsolidation_ratio_factor__robertson2012interpretation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overconsolidation\_ratio\_factor\_\_robertson2012interpretation}(Q_{tn}, F_r, \mathrm{is\_fine\_soil}, \mathrm{soil\_transition}) \\ \hspace{1em} k \gets \frac{Q_{tn}^{0.25}}{\mathopen{}\left( 2.625 + 1.75 \log_{10} F_r \mathclose{}\right)^{1.25}} \\ \hspace{1em} \mathbf{return} \ k \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
k &= \text{Overconsolidation ratio factor}\\
Q_{tn} &= \text{Stress-normalized cone resistance}\\
F_r &= \text{Normalized friction ratio (\%)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_peak_friction_angle__mayne2005integrated`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_peak\_friction\_angle\_\_mayne2005integrated}(B_q, Q_{tn}, \mathrm{soil\_transition}) \\ \hspace{1em} ϕ' \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( \mathopen{}\left( B_q > 0.1 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( B_q < 1 \mathclose{}\right), 29.5 B_q^{0.121} \cdot \mathopen{}\left( 0.256 + 0.336 B_q + \log_{10} Q_{tn} \mathclose{}\right), \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ ϕ' \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ϕ' &= \text{Peak friction angle (°)}\\
B_q &= \text{Normalized pore pressure ratio}\\
Q_{tn} &= \text{Stress-normalized cone resistance}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_peak_undrained_shear_strength_ratio__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_peak\_undrained\_shear\_strength\_ratio\_\_idriss2008soil}(I_c, q_{c1Ncs}, S_u, σ_v', ϕ_{cv}, \mathrm{is\_fine\_soil}) \\ \hspace{1em} S_{u\ ratio\ peak} \gets \mathrm{get\_peak\_undrained\_shear\_strength\_ratio\_\_robertson2022evaluation} \mathopen{}\left( I_c, q_{c1Ncs}, S_u, σ_v', ϕ_{cv} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ S_{u\ ratio\ peak} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_{u\ ratio\ peak} &= \text{Peak undrained shear strength ratio}\\
I_c &= \text{Soil behavior type index}\\
q_{c1Ncs} &= \text{Clean sand normalized cone resistance at 1 atm}\\
S_u &= \text{Undrained shear strength (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
ϕ_{cv} &= \text{Constant volume friction angle (°)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_peak_undrained_shear_strength_ratio__robertson2022evaluation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_peak\_undrained\_shear\_strength\_ratio\_\_robertson2022evaluation}(I_c, Q_{tncs}, S_u, σ_v', ϕ_{cv}) \\ \hspace{1em} ϕ \gets \mathrm{get\_friction\_angle\_\_robertson2012interpretation} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} S_{u\ ratio\ peak} \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( I_c < 3, \mathrm{tandg} \mathopen{}\left( ϕ \mathclose{}\right), \frac{S_u}{σ_v'} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ S_{u\ ratio\ peak} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_{u\ ratio\ peak} &= \text{Peak undrained shear strength ratio}\\
I_c &= \text{Soil behavior type index}\\
Q_{tncs} &= \text{Clean sand normalized cone resistance}\\
S_u &= \text{Undrained shear strength (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}\\
ϕ_{cv} &= \text{Constant volume friction angle (°)}
\end{align*}
$$

#### `get_permeability__robertson2010estimatingb`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_permeability\_\_robertson2010estimatingb}(I_c, \mathrm{is\_invalid\_data}, SBT_n, \mathrm{soil\_transition}) \\ \hspace{1em} \mathrm{conditions} \gets \mathopen{}\left[ \mathopen{}\left( I_c > 1 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( I_c \le 3.27 \mathclose{}\right), \mathopen{}\left( I_c > 3.27 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( I_c \le 4 \mathclose{}\right) \mathclose{}\right] \\ \hspace{1em} \mathrm{choices} \gets \mathopen{}\left[ 10^{0.952 - 3.04 I_c}, 10^{-4.52 - 1.37 I_c} \mathclose{}\right] \\ \hspace{1em} k \gets \mathrm{np}.\mathrm{select} \mathopen{}\left( \mathrm{conditions}, \mathrm{choices} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ k \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
k &= \text{Permeability (m/s)}\\
I_c &= \text{Soil behavior type index}\\
\text{is\_invalid\_data} &= \text{Is invalid data}\\
SBT_n &= \text{Normalized soil behavior type}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_pile_friction_coefficient__bustamante1982fellenius`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_friction\_coefficient\_\_bustamante1982fellenius}(q_c, \mathrm{is\_fine\_soil}, \mathrm{pile\_type\_category}) \\ \hspace{1em} \textrm{" steel if LCPC group equals IIB, else concrete "} \\ \hspace{1em} α \gets \mathrm{\_get\_pile\_friction\_coefficient\_\_bustamante1982fellenius\_vec} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ α \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
α &= \text{Pile friction coefficient}\\
q_c &= \text{Cone tip resistance (MPa)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{pile\_type\_category} &= \text{Pile type category}
\end{align*}
$$

#### `get_pile_friction_coefficient__bustamante1982pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_friction\_coefficient\_\_bustamante1982pile}(\mathrm{nature\_of\_soil}, \mathrm{pile\_type\_category}) \\ \hspace{1em} α \gets \mathrm{replace\_from\_mapping} \mathopen{}\left( \mathrm{nature\_of\_soil}, \mathrm{ReferenceData}.\mathrm{PileFrictionCoefficientBustamante1982}.\mathrm{get\_mapping} \mathopen{}\left( \textrm{"nature\_of\_soil"}, \mathrm{pile\_type\_category}.\mathrm{item} \mathopen{}\left( \mathclose{}\right) \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ α \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
α &= \text{Pile friction coefficient}\\
\text{nature\_of\_soil} &= \text{Nature of soil}\\
\text{pile\_type\_category} &= \text{Pile type category}
\end{align*}
$$

#### `get_pile_tip_resistance_coefficient__eslami1997pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_tip\_resistance\_coefficient\_\_eslami1997pile}(D) \\ \hspace{1em} C_t \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( D, 1 \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( C_t, D > 0.4, \frac{1}{3 D} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ C_t \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_t &= \text{Pile tip resistance coefficient}\\
D &= \text{Pile diameter (m)}
\end{align*}
$$

#### `get_pile_tip_resistance_factor__bustamante1982fellenius`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_tip\_resistance\_factor\_\_bustamante1982fellenius}(q_{ca}, \mathrm{is\_fine\_soil}, \mathrm{pile\_type\_category}) \\ \hspace{1em} \textrm{" bored if main LCPC group equals I, else driven "} \\ \hspace{1em} k_c \gets \mathrm{\_get\_pile\_tip\_resistance\_factor\_\_bustamante1982fellenius\_vec} \mathopen{}\left( q_{ca}, \mathrm{is\_fine\_soil}, \mathrm{pile\_type\_category} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ k_c \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
k_c &= \text{Pile tip resistance factor}\\
q_{ca} &= \text{Equivalent cone resistance (MPa)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{pile\_type\_category} &= \text{Pile type category}
\end{align*}
$$

#### `get_pile_tip_resistance_factor__bustamante1982pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_tip\_resistance\_factor\_\_bustamante1982pile}(\mathrm{nature\_of\_soil}, \mathrm{pile\_type\_category}) \\ \hspace{1em} k_c \gets \mathrm{replace\_from\_mapping} \mathopen{}\left( \mathrm{nature\_of\_soil}, \mathrm{ReferenceData}.\mathrm{PileTipResistanceFactorBustamante1982}.\mathrm{get\_mapping} \mathopen{}\left( \textrm{"nature\_of\_soil"}, \mathrm{pile\_type\_category}.\mathrm{item} \mathopen{}\left( \mathclose{}\right) \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ k_c \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
k_c &= \text{Pile tip resistance factor}\\
\text{nature\_of\_soil} &= \text{Nature of soil}\\
\text{pile\_type\_category} &= \text{Pile type category}
\end{align*}
$$

#### `get_pile_unit_tip_resistance__bustamante1982pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_unit\_tip\_resistance\_\_bustamante1982pile}(q_{ca}, k_c) \\ \hspace{1em} q_p \gets q_{ca} \cdot k_c \\ \hspace{1em} q_p \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( q_p, \mathrm{None}, 15 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ q_p \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
q_p &= \text{Pile unit tip resistance (MPa)}\\
q_{ca} &= \text{Equivalent cone resistance (MPa)}\\
k_c &= \text{Pile tip resistance factor}
\end{align*}
$$

#### `get_pile_unit_tip_resistance__eslami1997pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pile\_unit\_tip\_resistance\_\_eslami1997pile}(q_{Eg}, C_t) \\ \hspace{1em} q_p \gets q_{Eg} \cdot C_t \\ \hspace{1em} \mathbf{return} \ q_p \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
q_p &= \text{Pile unit tip resistance (MPa)}\\
q_{Eg} &= \text{Effective cone resistance geometric mean (MPa)}\\
C_t &= \text{Pile tip resistance coefficient}
\end{align*}
$$

#### `get_plasticity_index__ramsey2023estimating`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_plasticity\_index\_\_ramsey2023estimating}(F_r, B_q, Q_{t1}, \mathrm{soil\_transition}) \\ \hspace{1em} PI \gets \frac{12 F_r \cdot \mathopen{}\left( 1 + B_q \mathclose{}\right)^{1.2}}{\mathopen{}\left( \frac{Q_{t1}}{3} \mathclose{}\right)^{0.3}} \\ \hspace{1em} \mathbf{return} \ PI \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
PI &= \text{Plasticity index (\%)}\\
F_r &= \text{Normalized friction ratio (\%)}\\
B_q &= \text{Normalized pore pressure ratio}\\
Q_{t1} &= \text{Alternative normalized cone resistance}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_porosity__barounis2018estimation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_porosity\_\_barounis2018estimation}(e, \mathrm{soil\_transition}) \\ \hspace{1em} n \gets \frac{e}{1 + e} \\ \hspace{1em} \mathbf{return} \ n \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
n &= \text{Porosity}\\
e &= \text{Void ratio}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_relative_density__robertson2012guide`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_relative\_density\_\_robertson2012guide}(Q_{tn}, k_{D_r}, \mathrm{is\_invalid\_data}, SBT_n, \mathrm{is\_fine\_soil}) \\ \hspace{1em} D_r \gets 100 \mathopen{}\left( \frac{Q_{tn}}{k_{D_r}} \mathclose{}\right)^{0.5} \\ \hspace{1em} D_r \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( D_r, \mathrm{None}, 100 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ D_r \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
D_r &= \text{Relative density (\%)}\\
Q_{tn} &= \text{Stress-normalized cone resistance}\\
k_{D_r} &= \text{Relative density constant}\\
\text{is\_invalid\_data} &= \text{Is invalid data}\\
SBT_n &= \text{Normalized soil behavior type}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_relative_density__robertson2024guide`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_relative\_density\_\_robertson2024guide}(Q_{tncs}, k_{D_r}, \mathrm{is\_invalid\_data}, SBT_n, \mathrm{is\_fine\_soil}, \mathrm{soil\_transition}) \\ \hspace{1em} D_r \gets 100 \mathopen{}\left( \frac{Q_{tncs}}{k_{D_r}} \mathclose{}\right)^{0.5} \\ \hspace{1em} D_r \gets \mathrm{np}.\mathrm{round} \mathopen{}\left( D_r, 0 \mathclose{}\right) \\ \hspace{1em} D_r \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( D_r, \mathrm{None}, 100 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ D_r \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
D_r &= \text{Relative density (\%)}\\
Q_{tncs} &= \text{Clean sand normalized cone resistance}\\
k_{D_r} &= \text{Relative density constant}\\
\text{is\_invalid\_data} &= \text{Is invalid data}\\
SBT_n &= \text{Normalized soil behavior type}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_relative_density__tatsuoka1990evaluation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_relative\_density\_\_tatsuoka1990evaluation}(Q_{tn}, \mathrm{is\_fine\_soil}) \\ \hspace{1em} D_r \gets -85 + 76 \log_{10} Q_{tn} \\ \hspace{1em} D_r \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( D_r \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( D_r, \mathopen{}\left( Q_{tn} > 200 \mathclose{}\right) \mathbin{|} \mathopen{}\left( D_r \le 0 \mathclose{}\right), \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} D_r \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( \mathrm{np}.\mathrm{around} \mathopen{}\left( D_r \mathclose{}\right), 40, 90 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ D_r \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
D_r &= \text{Relative density (\%)}\\
Q_{tn} &= \text{Stress-normalized cone resistance}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_sensitivity__robertson2009interpretation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_sensitivity\_\_robertson2009interpretation}(N_S, F_r, \mathrm{is\_fine\_soil}, \mathrm{soil\_transition}) \\ \hspace{1em} S_t \gets \frac{N_S}{F_r} \\ \hspace{1em} \mathbf{return} \ S_t \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_t &= \text{Sensitivity}\\
N_S &= \text{Sensitivity constant}\\
F_r &= \text{Normalized friction ratio (\%)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_shear_modulus__robertson2009interpretation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shear\_modulus\_\_robertson2009interpretation}(q_t, σ_v, I_c) \\ \hspace{1em} G_o \gets \mathopen{}\left( q_t - σ_v \cdot 0.001 \mathclose{}\right) \cdot 0.0188 \cdot 10^{0.55 I_c + 1.68} \\ \hspace{1em} \mathbf{return} \ G_o \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
G_o &= \text{Small strain shear modulus (MPa)}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
σ_v &= \text{Total stress (kPa)}\\
I_c &= \text{Soil behavior type index}
\end{align*}
$$

#### `get_shear_strain_limit_cpt__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shear\_strain\_limit\_cpt\_\_idriss2008soil}(q_{c1Ncs}) \\ \hspace{1em} γ_{lim} \gets 100 \cdot 1.859 \mathopen{}\left( 2.163 - 0.478 q_{c1Ncs}^{0.264} \mathclose{}\right)^{3} \\ \hspace{1em} γ_{lim} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( γ_{lim}, 0, 50 \mathclose{}\right) \\ \hspace{1em} γ_{lim} \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( γ_{lim} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ γ_{lim} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
γ_{lim} &= \text{Shear strain limit (\%)}\\
q_{c1Ncs} &= \text{Clean sand normalized cone resistance at 1 atm}
\end{align*}
$$

#### `get_shear_velocity__robertson2022evaluation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shear\_velocity\_\_robertson2022evaluation}(q_t, σ_v, I_c, \mathrm{soil\_transition}) \\ \hspace{1em} α_{vs} \gets 10^{0.55 I_c + 1.68} \\ \hspace{1em} V_s \gets \mathopen{}\left( \frac{α_{vs} \cdot \mathopen{}\left( q_t \cdot 1000 - σ_v \mathclose{}\right)}{101.325} \mathclose{}\right)^{0.5} \\ \hspace{1em} \mathbf{return} \ V_s \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
V_s &= \text{Shear velocity (m/s)}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
σ_v &= \text{Total stress (kPa)}\\
I_c &= \text{Soil behavior type index}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_soil_behavior_type`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_behavior\_type}(R_f, Q_t) \\ \hspace{1em} SBT \gets \mathrm{SoilBehaviourTypeFigure}.\mathrm{assign\_polygons\_labels\_from\_xy\_data} \mathopen{}\left( R_f, Q_t \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ SBT \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
SBT &= \text{Soil behavior type}\\
R_f &= \text{Friction ratio (\%)}\\
Q_t &= \text{Normalized cone resistance}
\end{align*}
$$

#### `get_soil_behavior_type_index`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_behavior\_type\_index}(Q_{tn}, F_r) \\ \hspace{1em} \textrm{" Evaluating cyclic liquefaction potential using the cone penetration test by robertson \& Wride (1998) "} \\ \hspace{1em} I_c \gets \mathopen{}\left( \mathopen{}\left( 3.47 - \log_{10} Q_{tn} \mathclose{}\right)^{2} + \mathopen{}\left( \log_{10} F_r + 1.22 \mathclose{}\right)^{2} \mathclose{}\right)^{0.5} \\ \hspace{1em} I_c \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( I_c, \mathrm{None}, 4.06 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ I_c \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
I_c &= \text{Soil behavior type index}\\
Q_{tn} &= \text{Stress-normalized cone resistance}\\
F_r &= \text{Normalized friction ratio (\%)}
\end{align*}
$$

#### `get_soil_behavior_type_label`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_behavior\_type\_label}(SBT) \\ \hspace{1em} SBT_{label} \gets \mathrm{replace\_from\_mapping} \mathopen{}\left( SBT, \mathrm{PARAMETERS}.\mathrm{get\_pair\_discrete\_field\_mapping} \mathopen{}\left( \textrm{"soil\_behavior\_type"}, \textrm{"soil\_behavior\_type\_label"} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ SBT_{label} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
SBT_{label} &= \text{Soil behavior type label}\\
SBT &= \text{Soil behavior type}
\end{align*}
$$

#### `get_soil_behavior_type_schneider`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_behavior\_type\_schneider}(U_2, Q_{t1}) \\ \hspace{1em} SBT_{Schneider} \gets \mathrm{SoilBehaviourTypeSchneiderFigure}.\mathrm{assign\_polygons\_labels\_from\_xy\_data} \mathopen{}\left( U_2, Q_{t1} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ SBT_{Schneider} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
SBT_{Schneider} &= \text{Soil behavior type Schneider}\\
U_2 &= \text{Normalized pore pressure}\\
Q_{t1} &= \text{Alternative normalized cone resistance}
\end{align*}
$$

#### `get_soil_behavior_type_schneider_label`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_behavior\_type\_schneider\_label}(SBT_{Schneider}) \\ \hspace{1em} SBT_{Schneider\ label} \gets \mathrm{replace\_from\_mapping} \mathopen{}\left( SBT_{Schneider}, \mathrm{PARAMETERS}.\mathrm{get\_pair\_discrete\_field\_mapping} \mathopen{}\left( \textrm{"soil\_behavior\_type\_schneider"}, \textrm{"soil\_behavior\_type\_schneider\_label"} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ SBT_{Schneider\ label} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
SBT_{Schneider\ label} &= \text{Soil behavior type Schneider label}\\
SBT_{Schneider} &= \text{Soil behavior type Schneider}
\end{align*}
$$

#### `get_soil_classification_index__saye2017linear`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_classification\_index\_\_saye2017linear}(Q_{t1}, f_s, σ_v') \\ \hspace{1em} ΔQ \gets \frac{Q_{t1} + 10}{\frac{f_s}{σ_v'} + 0.67} \\ \hspace{1em} \mathbf{return} \ ΔQ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ΔQ &= \text{Soil classification index}\\
Q_{t1} &= \text{Alternative normalized cone resistance}\\
f_s &= \text{Sleeve friction (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}
\end{align*}
$$

#### `get_soil_classification_index_label__saye2017linear`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_classification\_index\_label\_\_saye2017linear}(ΔQ) \\ \hspace{1em} ΔQ_{label} \gets \mathrm{PARAMETERS}_{\textrm{"soil\_classification\_index"}}.\mathrm{data\_bins}_{\textrm{"soil\_classification\_index\_label"}}.\mathrm{bin\_data} \mathopen{}\left( ΔQ \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ ΔQ_{label} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ΔQ_{label} &= \text{Soil classification index label}\\
ΔQ &= \text{Soil classification index}
\end{align*}
$$

#### `get_soil_classification_index_uscs_symbol__saye2017linear`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_classification\_index\_uscs\_symbol\_\_saye2017linear}(ΔQ) \\ \hspace{1em} \mathrm{uscs\_symbol} \gets \mathrm{PARAMETERS}_{\textrm{"soil\_classification\_index"}}.\mathrm{data\_bins}_{\textrm{"soil\_classification\_index\_uscs\_symbol"}}.\mathrm{bin\_data} \mathopen{}\left( ΔQ \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{uscs\_symbol} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{soil\_classification\_index\_uscs\_symbol} &= \text{Soil classification index USCS symbol}\\
ΔQ &= \text{Soil classification index}
\end{align*}
$$

#### `get_soil_transition`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_transition}(I_c, z, I_{c\ min}, I_{c\ max}, \mathrm{soil\_transition\_min\_rate\_of\_change}, I_{c\ min\ points}, \mathrm{soil\_transition\_detection}) \\ \hspace{1em} \textrm{" Defines Ic transition zones based on rate of change in Ic "} \\ \hspace{1em} \mathrm{soil\_transition} \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( I_c \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ \lnot \mathrm{soil\_transition\_detection} \\ \hspace{2em} \mathbf{return} \ \mathrm{soil\_transition} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} I_{c\ cutoff} \gets 2.6 \\ \hspace{1em} \mathrm{diff} \gets \mathrm{np}.\mathrm{diff} \mathopen{}\left( I_c \mathclose{}\right) \\ \hspace{1em} \mathrm{is\_increasing} \gets \mathrm{diff} > 0 \\ \hspace{1em} \mathrm{is\_decreasing} \gets \mathrm{diff} < 0 \\ \hspace{1em} \mathrm{cpt\_delta\_ic\_ratio} \gets \frac{0.01 \mathopen{}\left| \mathrm{diff} \mathclose{}\right|}{\mathopen{}\left| \mathrm{np}.\mathrm{diff} \mathopen{}\left( z \mathclose{}\right) \mathclose{}\right|} \\ \hspace{1em} \mathrm{mask\_range} \gets \mathopen{}\left( I_c \ge I_{c\ min} \mathclose{}\right) \mathbin{\&} \mathopen{}\left( I_c \le I_{c\ max} \mathclose{}\right) \\ \hspace{1em} \mathrm{mask\_cpt\_delta\_ic\_ratio} \gets \mathrm{cpt\_delta\_ic\_ratio} \ge \mathrm{soil\_transition\_min\_rate\_of\_change} \\ \hspace{1em} \mathrm{is\_in\_range\_and\_valid\_delta\_ic\_ratio} \gets \mathrm{mask\_range} \mathbin{\&} \mathrm{mask\_cpt\_delta\_ic\_ratio} \\ \hspace{1em} I_{c\ min\ points} \gets \left\{ \begin{array}{ll} I_{c\ min\ points}, & \mathrm{if} \ I_{c\ min\ points} \ge 2 \\ 2, & \mathrm{otherwise} \end{array} \right. \\ \hspace{1em} \mathbf{for} \ \mathrm{soil\_behavior\_type\_index\_is\_} \in \mathopen{}\left[ \mathrm{is\_increasing}, \mathrm{is\_decreasing} \mathclose{}\right] \ \mathbf{do} \\ \hspace{2em} \mathrm{soil\_behavior\_type\_index\_is\_\_mask} \gets \mathrm{is\_in\_range\_and\_valid\_delta\_ic\_ratio} \mathbin{\&} \mathrm{soil\_behavior\_type\_index\_is\_} \\ \hspace{2em} \mathopen{}\left( \mathrm{run\_values}, \mathrm{run\_starts}, \mathrm{run\_lengths} \mathclose{}\right) \gets \mathrm{find\_runs} \mathopen{}\left( \mathrm{soil\_behavior\_type\_index\_is\_\_mask} \mathclose{}\right) \\ \hspace{2em} \mathbf{for} \ \mathopen{}\left( \mathrm{value}, \mathrm{starts}, \mathrm{length} \mathclose{}\right) \in \mathrm{zip} \mathopen{}\left( \mathrm{run\_values}, \mathrm{run\_starts}, \mathrm{run\_lengths} \mathclose{}\right) \ \mathbf{do} \\ \hspace{3em} \mathbf{if} \ \mathrm{value} \\ \hspace{4em} \mathbf{if} \ \mathrm{starts} > 0 \land \mathrm{np}.\mathrm{take} \mathopen{}\left( \mathrm{mask\_range}, \mathrm{starts} - 1 \mathclose{}\right) \\ \hspace{5em} \mathrm{starts} \gets \mathrm{starts} - 1 \\ \hspace{5em} \mathrm{length} \gets \mathrm{length} + 1 \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{4em} \mathrm{ends} \gets \mathrm{starts} + \mathrm{length} \\ \hspace{4em} \mathrm{indices} \gets \mathrm{np}.\mathrm{arange} \mathopen{}\left( \mathrm{starts}, \mathrm{ends} \mathclose{}\right) \\ \hspace{4em} \mathrm{soil\_behavior\_type\_index\_} \gets \mathrm{np}.\mathrm{take} \mathopen{}\left( I_c, \mathrm{indices} \mathclose{}\right) \\ \hspace{4em} \mathopen{}\left( \mathrm{soil\_behavior\_type\_index\_min}, \mathrm{soil\_behavior\_type\_index\_max} \mathclose{}\right) \gets \mathopen{}\left( \mathrm{np}.\mathrm{min} \mathopen{}\left( \mathrm{soil\_behavior\_type\_index\_} \mathclose{}\right), \mathrm{np}.\mathrm{max} \mathopen{}\left( \mathrm{soil\_behavior\_type\_index\_} \mathclose{}\right) \mathclose{}\right) \\ \hspace{4em} \mathrm{crosses\_cutoff} \gets \mathopen{}\left( \mathrm{soil\_behavior\_type\_index\_min} < I_{c\ cutoff} \mathclose{}\right) \mathbin{\&} \mathopen{}\left( I_{c\ cutoff} < \mathrm{soil\_behavior\_type\_index\_max} \mathclose{}\right) \\ \hspace{4em} \mathbf{if} \ \mathrm{length} \ge I_{c\ min\ points} \land \mathrm{crosses\_cutoff} \\ \hspace{5em} \mathrm{np}.\mathrm{put} \mathopen{}\left( \mathrm{soil\_transition}, \mathrm{indices}, \mathrm{True} \mathclose{}\right) \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ for} \\ \hspace{1em} \mathbf{end \ for} \\ \hspace{1em} \mathbf{return} \ \mathrm{soil\_transition} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{soil\_transition} &= \text{Soil transition}\\
I_c &= \text{Soil behavior type index}\\
z &= \text{Depth (m)}\\
I_{c\ min} &= \text{Soil transition min. index}\\
I_{c\ max} &= \text{Soil transition max. index}\\
\text{soil\_transition\_min\_rate\_of\_change} &= \text{Soil transition min. rate of change}\\
I_{c\ min\ points} &= \text{Soil transition min. points}\\
\text{soil\_transition\_detection} &= \text{Soil transition detection}
\end{align*}
$$

#### `get_soil_type_index`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_type\_index}(f_s, q_E) \\ \hspace{1em} \mathrm{soil\_type\_index} \gets \mathrm{SoilTypeIndexFigure}.\mathrm{assign\_polygons\_labels\_from\_xy\_data} \mathopen{}\left( f_s.\mathrm{clip} \mathopen{}\left( 1.5, \mathrm{None} \mathclose{}\right), q_E.\mathrm{clip} \mathopen{}\left( 0.15, \mathrm{None} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{soil\_type\_index} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{soil\_type\_index} &= \text{Soil type index}\\
f_s &= \text{Sleeve friction (kPa)}\\
q_E &= \text{Effective cone resistance (MPa)}
\end{align*}
$$

#### `get_soil_type_index_label`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_type\_index\_label}(\mathrm{soil\_type\_index}) \\ \hspace{1em} \mathrm{soil\_type\_index\_label} \gets \mathrm{replace\_from\_mapping} \mathopen{}\left( \mathrm{soil\_type\_index}, \mathrm{PARAMETERS}.\mathrm{get\_pair\_discrete\_field\_mapping} \mathopen{}\left( \textrm{"soil\_type\_index"}, \textrm{"soil\_type\_index\_label"} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{soil\_type\_index\_label} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{soil\_type\_index\_label} &= \text{Soil type index label}\\
\text{soil\_type\_index} &= \text{Soil type index}
\end{align*}
$$

#### `get_state_parameter__robertson2012interpretation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_state\_parameter\_\_robertson2012interpretation}(Q_{tncs}, \mathrm{is\_invalid\_data}, SBT_n, \mathrm{is\_fine\_soil}, \mathrm{soil\_transition}) \\ \hspace{1em} ψ \gets 0.56 - 0.33 \log_{10} Q_{tncs} \\ \hspace{1em} \mathbf{return} \ ψ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ψ &= \text{State parameter}\\
Q_{tncs} &= \text{Clean sand normalized cone resistance}\\
\text{is\_invalid\_data} &= \text{Is invalid data}\\
SBT_n &= \text{Normalized soil behavior type}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_stress_normalized_cone_resistance`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_stress\_normalized\_cone\_resistance}(q_t, σ_v, C_n) \\ \hspace{1em} \textrm{" Interpretation of cone penetration tests – a unified approach by robertson (2009) "} \\ \hspace{1em} \textrm{"  Estimating Liquefaction induced Ground Settlements From CPT for Level Ground by zhang (2002) "} \\ \hspace{1em} Q_{tn} \gets \frac{q_t \cdot 1000 - σ_v}{101.325} \cdot C_n \\ \hspace{1em} \mathbf{return} \ Q_{tn} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_{tn} &= \text{Stress-normalized cone resistance}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
σ_v &= \text{Total stress (kPa)}\\
C_n &= \text{Overburden correction}
\end{align*}
$$

#### `get_ultimate_bearing_capacity_cpt`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_ultimate\_bearing\_capacity\_cpt}(R_k, q_{t\ mean}) \\ \hspace{1em} Q_{ult} \gets 1000 R_k \cdot q_{t\ mean} \\ \hspace{1em} \mathbf{return} \ Q_{ult} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
Q_{ult} &= \text{Ultimate bearing capacity (kPa)}\\
R_k &= \text{Bearing capacity factor}\\
q_{t\ mean} &= \text{Mean corrected cone tip resistance (MPa)}
\end{align*}
$$

#### `get_undrained_shear_strength__robertson2012interpretation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_undrained\_shear\_strength\_\_robertson2012interpretation}(q_t, σ_v, N_{kt}, \mathrm{is\_fine\_soil}, \mathrm{soil\_transition}) \\ \hspace{1em} S_u \gets \frac{1000 q_t - σ_v}{N_{kt}} \\ \hspace{1em} \mathbf{return} \ S_u \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_u &= \text{Undrained shear strength (kPa)}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
σ_v &= \text{Total stress (kPa)}\\
N_{kt} &= \text{Undrained shear strength factor}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_undrained_shear_strength_factor__robertson2012interpretation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_undrained\_shear\_strength\_factor\_\_robertson2012interpretation}(F_r, \mathrm{is\_fine\_soil}, \mathrm{soil\_transition}) \\ \hspace{1em} N_{kt} \gets 10.5 + 7 \log_{10} F_r \\ \hspace{1em} \mathbf{return} \ N_{kt} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_{kt} &= \text{Undrained shear strength factor}\\
F_r &= \text{Normalized friction ratio (\%)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
\text{soil\_transition} &= \text{Soil transition}
\end{align*}
$$

#### `get_unit_side_friction__bustamante1982pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_unit\_side\_friction\_\_bustamante1982pile}(q_t, α, f_{p\ lim}) \\ \hspace{1em} f_p \gets \frac{q_t}{α} \\ \hspace{1em} f_p \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( f_p, \mathrm{None}, f_{p\ lim} \mathclose{}\right) \\ \hspace{1em} f_p \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( f_p \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ f_p \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
f_p &= \text{Unit side friction (MPa)}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
α &= \text{Pile friction coefficient}\\
f_{p\ lim} &= \text{Unit side friction limit (MPa)}
\end{align*}
$$

#### `get_unit_side_friction__eslami1997pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_unit\_side\_friction\_\_eslami1997pile}(C_s, q_E) \\ \hspace{1em} f_p \gets C_s \cdot q_E \\ \hspace{1em} \mathbf{return} \ f_p \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
f_p &= \text{Unit side friction (MPa)}\\
C_s &= \text{Unit side friction coefficient}\\
q_E &= \text{Effective cone resistance (MPa)}
\end{align*}
$$

#### `get_unit_side_friction_coefficient__eslami1997pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_unit\_side\_friction\_coefficient\_\_eslami1997pile}(\mathrm{soil\_type\_index}) \\ \hspace{1em} C_s \gets \mathrm{replace\_from\_mapping} \mathopen{}\left( \mathrm{soil\_type\_index}, \mathrm{DataMaps}.\mathrm{UnitSideFrictionCoefficientEslami1997}.\mathrm{data} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ C_s \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_s &= \text{Unit side friction coefficient}\\
\text{soil\_type\_index} &= \text{Soil type index}
\end{align*}
$$

#### `get_unit_side_friction_limit__bustamante1982fellenius`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_unit\_side\_friction\_limit\_\_bustamante1982fellenius}(q_c, \mathrm{is\_fine\_soil}, f_{p\ clip}) \\ \hspace{1em} \mathbf{if} \ f_{p\ clip} \\ \hspace{2em} f_{p\ lim} \gets \mathrm{\_get\_unit\_side\_friction\_limit\_\_bustamante1982fellenius\_vec} \mathopen{}\left( q_c, \mathrm{is\_fine\_soil} \mathclose{}\right) \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{return} \ \mathrm{np}.\mathrm{inf} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ f_{p\ lim} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
f_{p\ lim} &= \text{Unit side friction limit (MPa)}\\
q_c &= \text{Cone tip resistance (MPa)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}\\
f_{p\ clip} &= \text{Unit side friction clip}
\end{align*}
$$

#### `get_unit_side_friction_limit__bustamante1982pile`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_unit\_side\_friction\_limit\_\_bustamante1982pile}(\mathrm{nature\_of\_soil}, \mathrm{pile\_type\_category}, \mathrm{careful\_execution}, f_{p\ clip}) \\ \hspace{1em} \textrm{" if pile careful execution, then use values in parentheses "} \\ \hspace{1em} \mathbf{if} \ f_{p\ clip} \\ \hspace{2em} \mathbf{if} \ \mathrm{careful\_execution} \\ \hspace{3em} \mathrm{ref} \gets \mathrm{ReferenceData}.\mathrm{UnitSideFrictionLimitCareBustamante1982} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathrm{ref} \gets \mathrm{ReferenceData}.\mathrm{UnitSideFrictionLimitBustamante1982} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} f_{p\ lim} \gets \mathrm{replace\_from\_mapping} \mathopen{}\left( \mathrm{nature\_of\_soil}, \mathrm{ref}.\mathrm{get\_mapping} \mathopen{}\left( \textrm{"nature\_of\_soil"}, \mathrm{pile\_type\_category}.\mathrm{item} \mathopen{}\left( \mathclose{}\right) \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{return} \ \mathrm{np}.\mathrm{inf} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ f_{p\ lim} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
f_{p\ lim} &= \text{Unit side friction limit (MPa)}\\
\text{nature\_of\_soil} &= \text{Nature of soil}\\
\text{pile\_type\_category} &= \text{Pile type category}\\
\text{careful\_execution} &= \text{Careful execution}\\
f_{p\ clip} &= \text{Unit side friction clip}
\end{align*}
$$

#### `get_unit_weight__robertson2010estimatinga`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_unit\_weight\_\_robertson2010estimatinga}(R_f, q_t, \mathrm{is\_invalid\_data}) \\ \hspace{1em} γ \gets \frac{γ_w \cdot G_s}{2.65} \cdot \mathopen{}\left( 0.27 \log_{10} R_f + 0.36 \log_{10} \mathopen{}\left( \frac{1000 q_t}{101.325} \mathclose{}\right) + 1.236 \mathclose{}\right) \\ \hspace{1em} γ \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( γ, 1.4 g, 2.2 g \mathclose{}\right) \\ \hspace{1em} γ \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( γ \mathclose{}\right) \\ \hspace{1em} γ \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( γ \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( γ, \mathrm{is\_invalid\_data}, 18 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ γ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
γ &= \text{Unit weight (kN/m3)}\\
R_f &= \text{Friction ratio (\%)}\\
q_t &= \text{Corrected cone tip resistance (MPa)}\\
\text{is\_invalid\_data} &= \text{Is invalid data}\\
G_s &= \text{Specific gravity}\\
γ_w &= \text{Water unit weight (kN/m3)}
\end{align*}
$$

#### `get_void_ratio__barounis2018estimation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_void\_ratio\_\_barounis2018estimation}(w_c, \mathrm{below\_water\_table}, G_s, \mathrm{soil\_transition}) \\ \hspace{1em} e \gets \frac{0.01 w_c \cdot G_s}{S_r} \\ \hspace{1em} e \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( e \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( e, \mathord{\sim} \mathrm{below\_water\_table}, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ e \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
e &= \text{Void ratio}\\
w_c &= \text{Water content (\%)}\\
\text{below\_water\_table} &= \text{Below water table}\\
G_s &= \text{Specific gravity}\\
\text{soil\_transition} &= \text{Soil transition}\\
S_r &= \text{Saturation ratio}
\end{align*}
$$

#### `get_volumetric_strain__zhang2002estimating`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_volumetric\_strain\_\_zhang2002estimating}(FS_{liq}, Q_{tncs}) \\ \hspace{1em} FS_{liq} \gets \mathrm{np}.\mathrm{around} \mathopen{}\left( FS_{liq} \mathclose{}\right) \\ \hspace{1em} \mathrm{conditions} \gets \mathopen{}\left[ \mathopen{}\left( FS_{liq} \le 0.5 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \ge 33 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \le 200 \mathclose{}\right), \mathopen{}\left( FS_{liq} = 0.6 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \ge 33 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \le 147 \mathclose{}\right), \mathopen{}\left( FS_{liq} = 0.6 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} > 147 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \le 200 \mathclose{}\right), \mathopen{}\left( FS_{liq} = 0.7 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \ge 33 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \le 110 \mathclose{}\right), \mathopen{}\left( FS_{liq} = 0.7 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} > 110 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \le 200 \mathclose{}\right), \mathopen{}\left( FS_{liq} = 0.8 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \ge 33 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \le 80 \mathclose{}\right), \mathopen{}\left( FS_{liq} = 0.8 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} > 80 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \le 200 \mathclose{}\right), \mathopen{}\left( FS_{liq} = 0.9 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \ge 33 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \le 60 \mathclose{}\right), \mathopen{}\left( FS_{liq} = 0.9 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} > 60 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \le 200 \mathclose{}\right), \mathopen{}\left( FS_{liq} = 1.0 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \ge 33 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \le 200 \mathclose{}\right), \mathopen{}\left( FS_{liq} = 1.1 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \ge 33 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \le 200 \mathclose{}\right), \mathopen{}\left( FS_{liq} = 1.2 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \ge 33 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \le 200 \mathclose{}\right), \mathopen{}\left( FS_{liq} = 1.3 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \ge 33 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \le 200 \mathclose{}\right), \mathopen{}\left( FS_{liq} = 2 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \ge 33 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( Q_{tncs} \le 200 \mathclose{}\right) \mathclose{}\right] \\ \hspace{1em} \mathrm{choices} \gets \mathopen{}\left[ 102 Q_{tncs}^{-0.82}, 102 Q_{tncs}^{-0.82}, 2411 Q_{tncs}^{-1.45}, 102 Q_{tncs}^{-0.82}, 1701 Q_{tncs}^{-1.42}, 102 Q_{tncs}^{-0.82}, 1690 Q_{tncs}^{-1.46}, 102 Q_{tncs}^{-0.82}, 1430 Q_{tncs}^{-1.48}, 64 Q_{tncs}^{-0.93}, 11 Q_{tncs}^{-0.65}, 9.7 Q_{tncs}^{-0.69}, 7.6 Q_{tncs}^{-0.71}, 0 \mathclose{}\right] \\ \hspace{1em} ε_v \gets \mathrm{np}.\mathrm{select} \mathopen{}\left( \mathrm{conditions}, \mathrm{choices} \mathclose{}\right) \\ \hspace{1em} ε_v \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( \mathrm{np}.\mathrm{isnan} \mathopen{}\left( ε_v \mathclose{}\right) \mathbin{|} \mathopen{}\left( FS_{liq} \ge 2 \mathclose{}\right), 0, ε_v \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ ε_v \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ε_v &= \text{Volumetric strain (\%)}\\
FS_{liq} &= \text{Liquefaction safety factor}\\
Q_{tncs} &= \text{Clean sand normalized cone resistance}
\end{align*}
$$

#### `get_volumetric_strain_cpt__idriss2008soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_volumetric\_strain\_cpt\_\_idriss2008soil}(γ_{max}, q_{c1Ncs}) \\ \hspace{1em} q_{c1Ncs} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( q_{c1Ncs}, 21, \mathrm{None} \mathclose{}\right) \\ \hspace{1em} γ_{max} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( γ_{max}, \mathrm{None}, 100 \cdot 0.08 \mathclose{}\right) \\ \hspace{1em} ε_v \gets 1.5 \exp \mathopen{}\left( 2.551 - 1.147 q_{c1Ncs}^{0.264} \mathclose{}\right) γ_{max} \\ \hspace{1em} ε_v \gets \mathrm{np}.\mathrm{nan\_to\_num} \mathopen{}\left( ε_v \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ ε_v \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ε_v &= \text{Volumetric strain (\%)}\\
γ_{max} &= \text{Max. shear strain (\%)}\\
q_{c1Ncs} &= \text{Clean sand normalized cone resistance at 1 atm}
\end{align*}
$$

#### `get_water_content__barounis2018estimation`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_water\_content\_\_barounis2018estimation}(γ, \mathrm{below\_water\_table}, \mathrm{soil\_transition}) \\ \hspace{1em} w_c \gets \frac{100 \mathopen{}\left( G_s \cdot γ_w - γ \mathclose{}\right)}{G_s \cdot γ - G_s \cdot γ_w} \\ \hspace{1em} w_c \gets \mathrm{np}.\mathrm{asarray} \mathopen{}\left( w_c \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( w_c, \mathord{\sim} \mathrm{below\_water\_table}, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ w_c \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
w_c &= \text{Water content (\%)}\\
γ &= \text{Unit weight (kN/m3)}\\
\text{below\_water\_table} &= \text{Below water table}\\
\text{soil\_transition} &= \text{Soil transition}\\
G_s &= \text{Specific gravity}\\
γ_w &= \text{Water unit weight (kN/m3)}
\end{align*}
$$
