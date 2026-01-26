---
title: dmt.py
---

## Formulae

#### `get_coefficient_of_earth_pressure_at_rest__marchetti1981flat`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_coefficient\_of\_earth\_pressure\_at\_rest\_\_marchetti1981flat}(K_d, \mathrm{is\_fine\_soil}) \\ \hspace{1em} K_o \gets \mathopen{}\left( \frac{K_d}{1.5} \mathclose{}\right)^{0.47} - 0.6 \\ \hspace{1em} K_o \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( K_o, 0.3, \mathrm{None} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ K_o \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K_o &= \text{Coefficient of lateral earth pressure at rest}\\
K_d &= \text{Horizontal stress index}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_constrained_modulus__marchetti1981flat`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_constrained\_modulus\_\_marchetti1981flat}(I_D, K_d, E_d) \\ \hspace{1em} \mathrm{conditions} \gets \mathopen{}\left[ I_D \le 0.6, I_D < 3, I_D \ge 3 \mathclose{}\right] \\ \hspace{1em} \mathrm{rm0} \gets 0.14 + \frac{0.36 \mathopen{}\left( I_D - 0.6 \mathclose{}\right)}{2.4} \\ \hspace{1em} \mathrm{choices} \gets \mathopen{}\left[ 0.14 + 2.36 \log_{10} K_d, \mathrm{rm0} + \mathopen{}\left( 2.5 - \mathrm{rm0} \mathclose{}\right) \log_{10} K_d, 0.5 + 2 \log_{10} K_d \mathclose{}\right] \\ \hspace{1em} R_M \gets \mathrm{np}.\mathrm{select} \mathopen{}\left( \mathrm{conditions}, \mathrm{choices} \mathclose{}\right) \\ \hspace{1em} R_M \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( R_M, 0.85, \mathrm{None} \mathclose{}\right) \\ \hspace{1em} M \gets R_M \cdot E_d \\ \hspace{1em} \mathbf{return} \ M \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
M &= \text{Constrained modulus (MPa)}\\
I_D &= \text{Material index}\\
K_d &= \text{Horizontal stress index}\\
E_d &= \text{Dilatometer modulus (MPa)}
\end{align*}
$$

#### `get_corrected_pressure_p0`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_corrected\_pressure\_p0}(A, B, Z_{M\ A}, ΔA, ΔB) \\ \hspace{1em} P_0 \gets 1.05 \mathopen{}\left( A - Z_{M\ A} + ΔA \mathclose{}\right) - 0.05 \mathopen{}\left( B - Z_{M\ A} - ΔB \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ P_0 \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
P_0 &= \text{Corrected pressure P0 (kPa)}\\
A &= \text{Raw A reading (kPa)}\\
B &= \text{Raw B reading (kPa)}\\
Z_{M\ A} &= \text{Vented control unit reading for A (kPa)}\\
ΔA &= \text{Free air correction to A reading (kPa)}\\
ΔB &= \text{Free air correction to B reading (kPa)}
\end{align*}
$$

#### `get_corrected_pressure_p1`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_corrected\_pressure\_p1}(B, Z_{M\ B}, ΔB) \\ \hspace{1em} P_1 \gets B - Z_{M\ B} - ΔB \\ \hspace{1em} \mathbf{return} \ P_1 \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
P_1 &= \text{Corrected pressure P1 (kPa)}\\
B &= \text{Raw B reading (kPa)}\\
Z_{M\ B} &= \text{Vented control unit reading for B (kPa)}\\
ΔB &= \text{Free air correction to B reading (kPa)}
\end{align*}
$$

#### `get_corrected_pressure_p2`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_corrected\_pressure\_p2}(C, ΔA) \\ \hspace{1em} P_2 \gets C + ΔA \\ \hspace{1em} \mathbf{return} \ P_2 \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
P_2 &= \text{Corrected pressure P2 (kPa)}\\
C &= \text{Raw C reading (kPa)}\\
ΔA &= \text{Free air correction to A reading (kPa)}
\end{align*}
$$

#### `get_dilatometer_modulus`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_dilatometer\_modulus}(P_0, P_1) \\ \hspace{1em} E_d \gets 34.7 \mathopen{}\left( P_1 - P_0 \mathclose{}\right) \\ \hspace{1em} E_d \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( E_d \le 0, \mathrm{np}.\mathrm{nan}, E_d \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \frac{1}{1000} \cdot E_d \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
E_d &= \text{Dilatometer modulus (MPa)}\\
P_0 &= \text{Corrected pressure P0 (kPa)}\\
P_1 &= \text{Corrected pressure P1 (kPa)}
\end{align*}
$$

#### `get_elasticity_modulus__marchetti1981flat`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_elasticity\_modulus\_\_marchetti1981flat}(M, E_s\ /\ M) \\ \hspace{1em} E_s \gets E_s\ /\ M \cdot M \\ \hspace{1em} \mathbf{return} \ E_s \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
E_s &= \text{Elasticity modulus (MPa)}\\
M &= \text{Constrained modulus (MPa)}\\
E_s\ /\ M &= \text{Elasticity to constrained modulus ratio}
\end{align*}
$$

#### `get_friction_angle__marchetti1997flat`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_friction\_angle\_\_marchetti1997flat}(K_d, I_D) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( K_d, I_D \le 1.8, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} ϕ \gets 28 + 14.6 \log_{10} K_d - 2.1 \mathopen{}\left( \log_{10} K_d \mathclose{}\right)^{2} \\ \hspace{1em} \mathbf{return} \ ϕ \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
ϕ &= \text{Friction angle (°)}\\
K_d &= \text{Horizontal stress index}\\
I_D &= \text{Material index}
\end{align*}
$$

#### `get_horizontal_stress_index`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_horizontal\_stress\_index}(P_0, u_0, σ_v') \\ \hspace{1em} K_d \gets \frac{P_0 - u_0}{σ_v'} \\ \hspace{1em} \mathbf{return} \ K_d \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
K_d &= \text{Horizontal stress index}\\
P_0 &= \text{Corrected pressure P0 (kPa)}\\
u_0 &= \text{Pore water pressure (kPa)}\\
σ_v' &= \text{Effective stress (kPa)}
\end{align*}
$$

#### `get_is_fine_soil_dmt`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_is\_fine\_soil\_dmt}(I_D) \\ \hspace{1em} \mathrm{is\_fine\_soil} \gets I_D < 1.2 \\ \hspace{1em} \mathbf{return} \ \mathrm{is\_fine\_soil} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{is\_fine\_soil} &= \text{Is fine soil}\\
I_D &= \text{Material index}
\end{align*}
$$

#### `get_material_description`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_material\_description}(I_D, E_d) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( I_D, E_d < 1.2, \mathrm{np}.\mathrm{where} \mathopen{}\left( I_D < 0.1, -1.5, -0.5 \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathrm{material\_description} \gets \mathrm{PARAMETERS}_{\textrm{"material\_index"}}.\mathrm{data\_bins}_{\textrm{"material\_description"}}.\mathrm{bin\_data} \mathopen{}\left( I_D \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{material\_description} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{material\_description} &= \text{Material description}\\
I_D &= \text{Material index}\\
E_d &= \text{Dilatometer modulus (MPa)}
\end{align*}
$$

#### `get_material_index`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_material\_index}(P_0, P_1, u_0) \\ \hspace{1em} I_D \gets \frac{P_1 - P_0}{P_0 - u_0} \\ \hspace{1em} I_D \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( I_D \le 0, \mathrm{np}.\mathrm{nan}, I_D \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ I_D \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
I_D &= \text{Material index}\\
P_0 &= \text{Corrected pressure P0 (kPa)}\\
P_1 &= \text{Corrected pressure P1 (kPa)}\\
u_0 &= \text{Pore water pressure (kPa)}
\end{align*}
$$

#### `get_overconsolidation_ratio__marchetti1981flat`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_overconsolidation\_ratio\_\_marchetti1981flat}(K_d, \mathrm{is\_fine\_soil}) \\ \hspace{1em} OCR \gets \mathopen{}\left( 0.5 K_d \mathclose{}\right)^{1.56} \\ \hspace{1em} OCR \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( OCR, 0.8, 99.9 \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ OCR \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
OCR &= \text{Overconsolidation ratio}\\
K_d &= \text{Horizontal stress index}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_pore_pressure_index`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_pore\_pressure\_index}(P_0, P_2, u_0) \\ \hspace{1em} U_D \gets \frac{P_2 - u_0}{P_0 - u_0} \\ \hspace{1em} \mathbf{return} \ U_D \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
U_D &= \text{Pore pressure index}\\
P_0 &= \text{Corrected pressure P0 (kPa)}\\
P_2 &= \text{Corrected pressure P2 (kPa)}\\
u_0 &= \text{Pore water pressure (kPa)}
\end{align*}
$$

#### `get_relative_density__reyna1991dilatometer`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_relative\_density\_\_reyna1991dilatometer}(K_d, I_D) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( K_d, I_D \le 1.8, \mathrm{np}.\mathrm{nan} \mathclose{}\right) \\ \hspace{1em} D_r \gets \mathrm{RelativeDensityReyna1991Figure}.\mathrm{interpolate\_at\_x} \mathopen{}\left( K_d \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ D_r \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
D_r &= \text{Relative density (\%)}\\
K_d &= \text{Horizontal stress index}\\
I_D &= \text{Material index}
\end{align*}
$$

#### `get_shear_modulus__amoroso2013prediction`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_shear\_modulus\_\_amoroso2013prediction}(I_D, K_d, M) \\ \hspace{1em} \mathrm{conditions} \gets \mathopen{}\left[ I_D < 0.6, \mathopen{}\left( I_D \ge 0.6 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( I_D < 1.8 \mathclose{}\right), I_D \ge 1.8 \mathclose{}\right] \\ \hspace{1em} \mathrm{choices} \gets \mathopen{}\left[ M \cdot 26.177 K_d^{-1.0066}, M \cdot 15.686 K_d^{-0.921}, M \cdot 4.5613 K_d^{-0.7967} \mathclose{}\right] \\ \hspace{1em} G_o \gets \mathrm{np}.\mathrm{select} \mathopen{}\left( \mathrm{conditions}, \mathrm{choices} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ G_o \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
G_o &= \text{Small strain shear modulus (MPa)}\\
I_D &= \text{Material index}\\
K_d &= \text{Horizontal stress index}\\
M &= \text{Constrained modulus (MPa)}
\end{align*}
$$

#### `get_undrained_shear_strength__marchetti1981flat`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_undrained\_shear\_strength\_\_marchetti1981flat}(K_d, σ_v', \mathrm{is\_fine\_soil}) \\ \hspace{1em} S_u \gets 0.22 σ_v' \cdot \mathopen{}\left( 0.5 K_d \mathclose{}\right)^{1.25} \\ \hspace{1em} \mathbf{return} \ S_u \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_u &= \text{Undrained shear strength (kPa)}\\
K_d &= \text{Horizontal stress index}\\
σ_v' &= \text{Effective stress (kPa)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_unit_weight__marchetti1981flat`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_unit\_weight\_\_marchetti1981flat}(I_D, E_d) \\ \hspace{1em} n \gets \begin{bmatrix} 1.737 \\ 2.013 \\ 2.289 \\ 2.564 \end{bmatrix} \\ \hspace{1em} m \gets \begin{bmatrix} 0.585 \\ 0.621 \\ 0.657 \\ 0.694 \end{bmatrix} \\ \hspace{1em} \mathrm{gamma\_table} \gets \begin{bmatrix} 1.6 & 1.6 & 1.7 \\ 1.7 & 1.7 & 1.8 \\ 1.8 & 1.8 & 1.9 \\ 1.9 & 1.95 & 2.0 \\ 2.05 & 2.1 & 2.15 \end{bmatrix} \\ \hspace{1em} γ \gets \mathrm{np}.\mathrm{full\_like} \mathopen{}\left( I_D, 1.4 \mathclose{}\right) \\ \hspace{1em} \mathrm{flag} \gets E_d < 1.2 \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( γ, \mathrm{flag} \mathbin{\&} \mathopen{}\left( I_D < 0.1 \mathclose{}\right), 1.4 \mathclose{}\right) \\ \hspace{1em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( γ, \mathrm{flag} \mathbin{\&} \mathopen{}\left( I_D \ge 0.1 \mathclose{}\right), 1.5 \mathclose{}\right) \\ \hspace{1em} \mathrm{flag} \gets E_d \ge 1.2 \\ \hspace{1em} \mathbf{if} \ \mathrm{np}.\mathrm{any} \mathopen{}\left( \mathrm{flag} \mathclose{}\right) \\ \hspace{2em} \mathrm{thresholds} \gets n + m \cdot \log_{10} I_D + \log_{10} 0.1 \\ \hspace{2em} \mathrm{table\_i} \gets \sum \mathopen{}\left( \log_{10} E_d \ge \mathrm{thresholds} \mathclose{}\right) \\ \hspace{2em} \mathrm{table\_j} \gets \mathrm{np}.\mathrm{select} \mathopen{}\left( \mathopen{}\left[ I_D > 1.8, I_D > 0.6, I_D > 0.0 \mathclose{}\right], \mathopen{}\left[ 2, 1, 0 \mathclose{}\right] \mathclose{}\right) \\ \hspace{2em} \mathrm{mask} \gets \mathrm{flag} \mathbin{\&} \mathopen{}\left( \mathrm{table\_j} \ge 0 \mathclose{}\right) \\ \hspace{2em} \mathrm{np}.\mathrm{putmask} \mathopen{}\left( γ, \mathrm{mask}, \mathrm{gamma\_table}_{\mathopen{}\left( \mathrm{table\_i}, \mathrm{table\_j} \mathclose{}\right), \mathrm{mask}} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ γ \cdot 9.81 \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
γ &= \text{Unit weight (kN/m3)}\\
I_D &= \text{Material index}\\
E_d &= \text{Dilatometer modulus (MPa)}
\end{align*}
$$
