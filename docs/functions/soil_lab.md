---
title: soil_lab.py
---

## Formulae

#### `get_a_parameter`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_a\_parameter}(T, G_s) \\ \hspace{1em} A \gets \mathrm{ReferenceData}.\mathrm{HydrometerDFactor}.\mathrm{interpolate\_at\_index\_column} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{a\_parameter}_{0} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
A &= \text{A parameter}\\
T &= \text{Temperature (°C)}\\
G_s &= \text{Specific gravity}
\end{align*}
$$

#### `get_corrected_hydrometer_reading`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_corrected\_hydrometer\_reading}(R, F_T, F_z) \\ \hspace{1em} R_{cp} \gets R + F_T - F_z \\ \hspace{1em} \mathbf{return} \ R_{cp} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
R_{cp} &= \text{Corrected hydrometer reading}\\
R &= \text{Hydrometer reading}\\
F_T &= \text{Temperature correction}\\
F_z &= \text{Zero correction}
\end{align*}
$$

#### `get_cumulative_mass_retained`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_cumulative\_mass\_retained}(W_n) \\ \hspace{1em} W_{n\ cum} \gets \mathrm{np}.\mathrm{cumsum} \mathopen{}\left( W_n \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ W_{n\ cum} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
W_{n\ cum} &= \text{Cumulative mass retained (g)}\\
W_n &= \text{Mass retained sieve (g)}
\end{align*}
$$

#### `get_curvature_coefficient`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_curvature\_coefficient}(D_{10}, D_{30}, D_{60}) \\ \hspace{1em} C_c \gets \frac{D_{30}^{2}}{D_{10} \cdot D_{60}} \\ \hspace{1em} \mathbf{return} \ C_c \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_c &= \text{Curvature coefficient}\\
D_{10} &= \text{Diameter at 10\% finer (mm)}\\
D_{30} &= \text{Diameter at 30\% finer (mm)}\\
D_{60} &= \text{Diameter at 60\% finer (mm)}
\end{align*}
$$

#### `get_dry_soil_mass`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_dry\_soil\_mass}(W_{can}, W_{can+drysoil}) \\ \hspace{1em} W_{dry\ soil} \gets W_{can+drysoil} - W_{can} \\ \hspace{1em} \mathbf{return} \ W_{dry\ soil} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
W_{dry\ soil} &= \text{Dry soil mass (g)}\\
W_{can} &= \text{Can mass (g)}\\
W_{can+drysoil} &= \text{Can + dry soil mass (g)}
\end{align*}
$$

#### `get_effective_length`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_effective\_length}(R_{cL}, \mathrm{hydrometer\_type}) \\ \hspace{1em} L \gets \mathrm{None} \\ \hspace{1em} \mathrm{hydrometer\_type} \gets \mathrm{hydrometer\_type}.\mathrm{item} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ \mathrm{hydrometer\_type} = \textrm{"152H"} \\ \hspace{2em} L \gets -0.164 R_{cL} + 16.295 \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{hydrometer\_type} = \textrm{"151H"} \\ \hspace{3em} L \gets -0.2645 R_{cL} + 16.295 \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ L \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
L &= \text{Effective length (cm)}\\
R_{cL} &= \text{Effective length corrected reading}\\
\text{hydrometer\_type} &= \text{Hydrometer type}
\end{align*}
$$

#### `get_effective_length_corrected_reading`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_effective\_length\_corrected\_reading}(R, F_m) \\ \hspace{1em} R_{cL} \gets R + F_m \\ \hspace{1em} \mathbf{return} \ R_{cL} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
R_{cL} &= \text{Effective length corrected reading}\\
R &= \text{Hydrometer reading}\\
F_m &= \text{Meniscus correction}
\end{align*}
$$

#### `get_hydrometer_percent_finer`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_hydrometer\_percent\_finer}(\mathrm{percent\_finer\_uncorrected}, FC) \\ \hspace{1em} \mathbf{if} \ FC < 90 \\ \hspace{2em} \mathrm{percent\_finer} \gets \mathrm{percent\_finer\_uncorrected} \cdot \frac{FC}{100} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathrm{percent\_finer} \gets \mathrm{percent\_finer\_uncorrected} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathrm{percent\_finer} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{percent\_finer} &= \text{Percent finer (\%)}\\
\text{percent\_finer\_uncorrected} &= \text{Percent finer uncorrected (\%)}\\
FC &= \text{Fines content (\%)}
\end{align*}
$$

#### `get_liquid_limit`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquid\_limit}(LL_{method}, N, w_c) \\ \hspace{1em} \mathbf{if} \ LL_{method} = \textrm{"single\_point"} \\ \hspace{2em} \mathbf{if} \ N < 20 \lor N > 30 \\ \hspace{3em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"\{\} must be between 20 and 30 for single point liquid limit method"}.\mathrm{format} \mathopen{}\left( N \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} LL \gets w_c \cdot \mathopen{}\left( \frac{N}{25} \mathclose{}\right)^{0.121} \\ \hspace{2em} \mathbf{return} \ \mathopen{}\left( LL.\mathrm{item} \mathopen{}\left( \mathclose{}\right), \mathrm{None} \mathclose{}\right) \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ LL_{method} = \textrm{"multi\_point"} \\ \hspace{3em} \mathrm{fit} \gets \mathrm{np}.\mathrm{polyfit} \mathopen{}\left( \log_{10} N, w_c, 1 \mathclose{}\right) \\ \hspace{3em} I_F \gets \mathopen{}\left| \mathrm{fit}_{0} \mathclose{}\right| \\ \hspace{3em} f \gets \mathrm{np}.\mathrm{poly1d} \mathopen{}\left( \mathrm{fit} \mathclose{}\right) \\ \hspace{3em} LL \gets f \mathopen{}\left( \log_{10} 25 \mathclose{}\right) \\ \hspace{3em} \mathbf{return} \ \mathopen{}\left( LL, I_F \mathclose{}\right) \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"\{\} method not valid"}.\mathrm{format} \mathopen{}\left( LL_{method} \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathrm{None} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
LL &= \text{Liquid limit (\%)}\\
I_F &= \text{Flow index}\\
LL_{method} &= \text{Liquid limit method}\\
N &= \text{Liquid limit blows}\\
w_c &= \text{Water content (trials) (\%)}
\end{align*}
$$

#### `get_liquidity_index`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_liquidity\_index}(w_c, LL, PI, \mathrm{is\_fine\_soil}) \\ \hspace{1em} LI \gets \frac{w_c - \mathopen{}\left( LL - PI \mathclose{}\right)}{PI} \\ \hspace{1em} \mathbf{return} \ LI \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
LI &= \text{Liquidity index}\\
w_c &= \text{Water content (\%)}\\
LL &= \text{Liquid limit (\%)}\\
PI &= \text{Plasticity index (\%)}\\
\text{is\_fine\_soil} &= \text{Is fine soil}
\end{align*}
$$

#### `get_moisture_mass`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_moisture\_mass}(W_{can+wetsoil}, W_{can+drysoil}) \\ \hspace{1em} W_{moisture} \gets W_{can+wetsoil} - W_{can+drysoil} \\ \hspace{1em} \mathbf{return} \ W_{moisture} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
W_{moisture} &= \text{Moisture mass (g)}\\
W_{can+wetsoil} &= \text{Can + wet soil mass (g)}\\
W_{can+drysoil} &= \text{Can + dry soil mass (g)}
\end{align*}
$$

#### `get_particle_size`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_particle\_size}(L, \mathrm{hydrometer\_time}, A) \\ \hspace{1em} D \gets A \cdot \sqrt{ \frac{L}{\mathrm{hydrometer\_time}} } \\ \hspace{1em} \mathbf{return} \ D \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
D &= \text{Particle size (mm)}\\
L &= \text{Effective length (cm)}\\
\text{hydrometer\_time} &= \text{Hydrometer time (min)}\\
A &= \text{A parameter}
\end{align*}
$$

#### `get_particle_size_from_sieve_number`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_particle\_size\_from\_sieve\_number}(\mathrm{sieve\_number}) \\ \hspace{1em} D \gets \mathrm{replace\_from\_mapping} \mathopen{}\left( \mathrm{sieve\_number}, \mathrm{SIEVES\_SI\_TO\_PARTICLE\_SIZE\_MAP} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ D \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
D &= \text{Particle size (mm)}\\
\text{sieve\_number} &= \text{Sieve number}
\end{align*}
$$

#### `get_percent_clay`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_percent\_clay}(D, \mathrm{percent\_finer}, D_{silt\ clay}) \\ \hspace{1em} f \gets \mathrm{interpolate1d} \mathopen{}\left( \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( D \mathclose{}\right), \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( \mathrm{percent\_finer} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathrm{percent\_clay} \gets f \mathopen{}\left( D_{silt\ clay} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{percent\_clay} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{percent\_clay} &= \text{Percent clay (\%)}\\
D &= \text{Particle size (mm)}\\
\text{percent\_finer} &= \text{Percent finer (\%)}\\
D_{silt\ clay} &= \text{Silt/clay particle size breakpoint (mm)}
\end{align*}
$$

#### `get_percent_finer`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_percent\_finer}(W_{dry\ soil}, W_{n\ cum}) \\ \hspace{1em} \mathrm{percent\_finer} \gets \frac{100 \mathopen{}\left( W_{dry\ soil} - W_{n\ cum} \mathclose{}\right)}{W_{dry\ soil}} \\ \hspace{1em} \mathbf{return} \ \mathrm{percent\_finer} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{percent\_finer} &= \text{Percent finer (\%)}\\
W_{dry\ soil} &= \text{Dry soil mass (g)}\\
W_{n\ cum} &= \text{Cumulative mass retained (g)}
\end{align*}
$$

#### `get_percent_finer_at_sieve_number`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_percent\_finer\_at\_sieve\_number}(\mathrm{sieve\_number}, \mathrm{percent\_finer}) \\ \hspace{1em} \mathrm{percent\_finer\_map} \gets \mathrm{dict} \mathopen{}\left( \mathrm{zip} \mathopen{}\left( \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( \mathrm{sieve\_number} \mathclose{}\right), \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( \mathrm{percent\_finer} \mathclose{}\right) \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathrm{sieve\_number\_targets} \gets \mathopen{}\left( \textrm{"3/4 ""}, \textrm{"No. 4"}, \textrm{"No. 10"}, \textrm{"No. 40"}, \textrm{"No. 200"} \mathclose{}\right) \\ \hspace{1em} \mathrm{percent\_finer\_at\_sieve\_number} \gets \mathopen{}\left[  \mathclose{}\right] \\ \hspace{1em} \mathbf{for} \ \mathrm{sieve\_number\_target} \in \mathrm{sieve\_number\_targets} \ \mathbf{do} \\ \hspace{2em} \mathrm{percent\_finer\_at\_sieve\_number}.\mathrm{append} \mathopen{}\left( \mathrm{percent\_finer\_map}.\mathrm{get} \mathopen{}\left( \mathrm{sieve\_number\_target} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ for} \\ \hspace{1em} \mathbf{return} \ \mathrm{tuple} \mathopen{}\left( \mathrm{percent\_finer\_at\_sieve\_number} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
P_{3/4} &= \text{Percent passing 3/4" (\%)}\\
P_{4} &= \text{Percent passing No. 4 (\%)}\\
P_{10} &= \text{Percent passing No. 10 (\%)}\\
P_{40} &= \text{Percent passing No. 40 (\%)}\\
FC &= \text{Fines content (\%)}\\
\text{sieve\_number} &= \text{Sieve number}\\
\text{percent\_finer} &= \text{Percent finer (\%)}
\end{align*}
$$

#### `get_percent_finer_diameters`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_percent\_finer\_diameters}(D, \mathrm{percent\_finer}, FC) \\ \hspace{1em} \mathrm{percent\_finer\_targets} \gets \mathopen{}\left( 60, 50, 30, 10 \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ FC.\mathrm{item} \mathopen{}\left( \mathclose{}\right) \le 50 \\ \hspace{2em} f \gets \mathrm{interpolate1d} \mathopen{}\left( \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( \mathrm{percent\_finer} \mathclose{}\right), \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( D \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathrm{percent\_finer\_diameters} \gets f \mathopen{}\left( \mathrm{percent\_finer\_targets} \mathclose{}\right) \\ \hspace{2em} \mathrm{to\_return} \gets \mathrm{tuple} \mathopen{}\left( \mathrm{percent\_finer\_diameters} \mathclose{}\right) \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathrm{to\_return} \gets \mathopen{}\left( \mathrm{np}.\mathrm{nan} \mathclose{}\right) \mathrm{len} \mathopen{}\left( \mathrm{percent\_finer\_targets} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathrm{to\_return} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
D_{60} &= \text{Diameter at 60\% finer (mm)}\\
D_{50} &= \text{Diameter at 50\% finer (mm)}\\
D_{30} &= \text{Diameter at 30\% finer (mm)}\\
D_{10} &= \text{Diameter at 10\% finer (mm)}\\
D &= \text{Particle size (mm)}\\
\text{percent\_finer} &= \text{Percent finer (\%)}\\
FC &= \text{Fines content (\%)}
\end{align*}
$$

#### `get_percent_finer_uncorrected`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_percent\_finer\_uncorrected}(R_{cp}, W_{dry\ soil}, a) \\ \hspace{1em} \mathrm{percent\_finer\_uncorrected} \gets \frac{100 a \cdot R_{cp}}{W_{dry\ soil}} \\ \hspace{1em} \mathbf{return} \ \mathrm{percent\_finer\_uncorrected} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{percent\_finer\_uncorrected} &= \text{Percent finer uncorrected (\%)}\\
R_{cp} &= \text{Corrected hydrometer reading}\\
W_{dry\ soil} &= \text{Dry soil mass (g)}\\
a &= \text{Specific gravity correction}
\end{align*}
$$

#### `get_percent_fraction`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_percent\_fraction}(P_{3/4}, P_{4}, P_{10}, P_{40}, FC) \\ \hspace{1em} \mathrm{percent\_gravel} \gets 100 - P_{4} \\ \hspace{1em} \mathrm{percent\_coarse\_gravel} \gets 100 - P_{3/4} \\ \hspace{1em} \mathrm{percent\_fine\_gravel} \gets P_{3/4} - P_{4} \\ \hspace{1em} \mathrm{percent\_sand} \gets P_{4} - FC \\ \hspace{1em} \mathrm{percent\_coarse\_sand} \gets P_{4} - P_{10} \\ \hspace{1em} \mathrm{percent\_medium\_sand} \gets P_{10} - P_{40} \\ \hspace{1em} \mathrm{percent\_fine\_sand} \gets P_{40} - FC \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( \mathrm{percent\_gravel}, \mathrm{percent\_coarse\_gravel}, \mathrm{percent\_fine\_gravel}, \mathrm{percent\_sand}, \mathrm{percent\_coarse\_sand}, \mathrm{percent\_medium\_sand}, \mathrm{percent\_fine\_sand} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{percent\_gravel} &= \text{Percent gravel (\%)}\\
\text{percent\_coarse\_gravel} &= \text{Percent coarse gravel (\%)}\\
\text{percent\_fine\_gravel} &= \text{Percent fine gravel (\%)}\\
\text{percent\_sand} &= \text{Percent sand (\%)}\\
\text{percent\_coarse\_sand} &= \text{Percent coarse sand (\%)}\\
\text{percent\_medium\_sand} &= \text{Percent medium sand (\%)}\\
\text{percent\_fine\_sand} &= \text{Percent fine sand (\%)}\\
P_{3/4} &= \text{Percent passing 3/4" (\%)}\\
P_{4} &= \text{Percent passing No. 4 (\%)}\\
P_{10} &= \text{Percent passing No. 10 (\%)}\\
P_{40} &= \text{Percent passing No. 40 (\%)}\\
FC &= \text{Fines content (\%)}
\end{align*}
$$

#### `get_percent_silt`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_percent\_silt}(FC, \mathrm{percent\_clay}) \\ \hspace{1em} \mathrm{percent\_silt} \gets FC - \mathrm{percent\_clay} \\ \hspace{1em} \mathbf{return} \ \mathrm{percent\_silt} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{percent\_silt} &= \text{Percent silt (\%)}\\
FC &= \text{Fines content (\%)}\\
\text{percent\_clay} &= \text{Percent clay (\%)}
\end{align*}
$$

#### `get_plastic_limit`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_plastic\_limit}(w_c) \\ \hspace{1em} PL \gets \mathrm{np}.\mathrm{nanmean} \mathopen{}\left( w_c \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ PL \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
PL &= \text{Plastic limit (\%)}\\
w_c &= \text{Water content (trials) (\%)}
\end{align*}
$$

#### `get_plasticity_index`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_plasticity\_index}(LL, PL) \\ \hspace{1em} PI \gets LL - PL \\ \hspace{1em} \mathbf{return} \ PI \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
PI &= \text{Plasticity index (\%)}\\
LL &= \text{Liquid limit (\%)}\\
PL &= \text{Plastic limit (\%)}
\end{align*}
$$

#### `get_specific_gravity_correction`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_specific\_gravity\_correction}(G_s) \\ \hspace{1em} a \gets \frac{\frac{1.65}{2.65} \cdot G_s}{G_s - 1} \\ \hspace{1em} \mathbf{return} \ a \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
a &= \text{Specific gravity correction}\\
G_s &= \text{Specific gravity}
\end{align*}
$$

#### `get_temperature_correction`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_temperature\_correction}(T) \\ \hspace{1em} F_T \gets -4.85 + 0.25 T \\ \hspace{1em} \mathbf{return} \ F_T \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
F_T &= \text{Temperature correction}\\
T &= \text{Temperature (°C)}
\end{align*}
$$

#### `get_uniformity_coefficient`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_uniformity\_coefficient}(D_{10}, D_{60}) \\ \hspace{1em} C_u \gets \frac{D_{60}}{D_{10}} \\ \hspace{1em} \mathbf{return} \ C_u \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
C_u &= \text{Uniformity coefficient}\\
D_{10} &= \text{Diameter at 10\% finer (mm)}\\
D_{60} &= \text{Diameter at 60\% finer (mm)}
\end{align*}
$$

#### `get_water_content`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_water\_content}(w_c) \\ \hspace{1em} w_c \gets \mathrm{np}.\mathrm{nanmean} \mathopen{}\left( w_c \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ w_c \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
w_c &= \text{Water content (\%)}\\
w_c &= \text{Water content (trials) (\%)}
\end{align*}
$$

#### `get_water_content_liquid_limit_ratio`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_water\_content\_liquid\_limit\_ratio}(w_c, LL) \\ \hspace{1em} w_c\ /\ LL \gets \frac{w_c}{LL} \\ \hspace{1em} \mathbf{return} \ w_c\ /\ LL \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
w_c\ /\ LL &= \text{Water content to liquid limit ratio}\\
w_c &= \text{Water content (\%)}\\
LL &= \text{Liquid limit (\%)}
\end{align*}
$$

#### `get_water_content_trials`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_water\_content\_trials}(W_{moisture}, W_{dry\ soil}) \\ \hspace{1em} w_c \gets \frac{W_{moisture} \cdot 100}{W_{dry\ soil}} \\ \hspace{1em} \mathbf{return} \ w_c \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
w_c &= \text{Water content (trials) (\%)}\\
W_{moisture} &= \text{Moisture mass (g)}\\
W_{dry\ soil} &= \text{Dry soil mass (g)}
\end{align*}
$$
