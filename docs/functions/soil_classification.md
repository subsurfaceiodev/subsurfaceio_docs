---
title: soil_classification.py
---

## Formulae

#### `_get_soil_classification__usda1993soil_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_soil\_classification\_\_usda1993soil\_scalar}(\mathrm{percent\_sand}, \mathrm{percent\_clay}, \mathrm{language}) \\ \hspace{1em} \mathrm{uscs\_symbology} \gets \mathrm{DataMaps}.\mathrm{get\_uscs\_symbology} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathrm{symbol} \gets \textrm{""} \\ \hspace{1em} \mathrm{description} \gets \textrm{""} \\ \hspace{1em} \mathbf{if} \ \lnot \mathrm{np}.\mathrm{any} \mathopen{}\left( \mathrm{is\_null} \mathopen{}\left( \mathopen{}\left[ \mathrm{percent\_sand}, \mathrm{percent\_clay} \mathclose{}\right] \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathrm{percent\_sum} \gets \sum \mathopen{}\left[ \mathrm{percent\_sand}, \mathrm{percent\_clay} \mathclose{}\right] \\ \hspace{2em} \mathbf{if} \ \mathrm{percent\_sum} > 100 \\ \hspace{3em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"Sum of sand \& clay \% = \{\} can't be > 100\%"}.\mathrm{format} \mathopen{}\left( \mathrm{percent\_sum} \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathrm{percent\_silt} \gets 100 - \mathrm{percent\_sand} - \mathrm{percent\_clay} \\ \hspace{2em} \mathbf{if} \ \mathrm{percent\_silt} + 1.5 \mathrm{percent\_clay} < 15 \\ \hspace{3em} \mathrm{symbol} \gets \textrm{"Sa"} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ \mathrm{percent\_silt} + 1.5 \mathrm{percent\_clay} \ge 15 \land \mathrm{percent\_silt} + 2 \mathrm{percent\_clay} < 30 \\ \hspace{4em} \mathrm{symbol} \gets \textrm{"LoSa"} \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ 7 \le \mathrm{percent\_clay} < 20 \land \mathrm{percent\_sand} > 52 \land \mathrm{percent\_silt} + 2 \mathrm{percent\_clay} \ge 30 \lor \mathrm{percent\_clay} < 7 \land \mathrm{percent\_silt} < 50 \land \mathrm{percent\_silt} + 2 \mathrm{percent\_clay} \ge 30 \\ \hspace{5em} \mathrm{symbol} \gets \textrm{"SaLo"} \\ \hspace{4em} \mathbf{else} \\ \hspace{5em} \mathbf{if} \ 7 \le \mathrm{percent\_clay} < 27 \land 28 \le \mathrm{percent\_silt} < 50 \land \mathrm{percent\_sand} \le 52 \\ \hspace{6em} \mathrm{symbol} \gets \textrm{"Lo"} \\ \hspace{5em} \mathbf{else} \\ \hspace{6em} \mathbf{if} \ \mathrm{percent\_silt} \ge 50 \land 12 \le \mathrm{percent\_clay} < 27 \lor 50 \le \mathrm{percent\_silt} < 80 \land \mathrm{percent\_clay} < 12 \\ \hspace{7em} \mathrm{symbol} \gets \textrm{"SiLo"} \\ \hspace{6em} \mathbf{else} \\ \hspace{7em} \mathbf{if} \ \mathrm{percent\_silt} \ge 80 \land \mathrm{percent\_clay} < 12 \\ \hspace{8em} \mathrm{symbol} \gets \textrm{"Si"} \\ \hspace{7em} \mathbf{else} \\ \hspace{8em} \mathbf{if} \ 20 \le \mathrm{percent\_clay} < 35 \land \mathrm{percent\_silt} < 28 \land \mathrm{percent\_sand} > 45 \\ \hspace{9em} \mathrm{symbol} \gets \textrm{"SaClLo"} \\ \hspace{8em} \mathbf{else} \\ \hspace{9em} \mathbf{if} \ 27 \le \mathrm{percent\_clay} < 40 \land 20 < \mathrm{percent\_sand} \le 45 \\ \hspace{10em} \mathrm{symbol} \gets \textrm{"ClLo"} \\ \hspace{9em} \mathbf{else} \\ \hspace{10em} \mathbf{if} \ 27 \le \mathrm{percent\_clay} < 40 \land \mathrm{percent\_sand} \le 20 \\ \hspace{11em} \mathrm{symbol} \gets \textrm{"SiClLo"} \\ \hspace{10em} \mathbf{else} \\ \hspace{11em} \mathbf{if} \ \mathrm{percent\_clay} \ge 35 \land \mathrm{percent\_sand} > 45 \\ \hspace{12em} \mathrm{symbol} \gets \textrm{"SaCl"} \\ \hspace{11em} \mathbf{else} \\ \hspace{12em} \mathbf{if} \ \mathrm{percent\_clay} \ge 40 \land \mathrm{percent\_silt} \ge 40 \\ \hspace{13em} \mathrm{symbol} \gets \textrm{"SiCl"} \\ \hspace{12em} \mathbf{else} \\ \hspace{13em} \mathbf{if} \ \mathrm{percent\_clay} \ge 40 > \mathrm{percent\_silt} \land \mathrm{percent\_sand} \le 45 \\ \hspace{14em} \mathrm{symbol} \gets \textrm{"Cl"} \\ \hspace{13em} \mathbf{else} \\ \hspace{14em} \mathrm{symbol} \gets \textrm{""} \\ \hspace{13em} \mathbf{end \ if} \\ \hspace{12em} \mathbf{end \ if} \\ \hspace{11em} \mathbf{end \ if} \\ \hspace{10em} \mathbf{end \ if} \\ \hspace{9em} \mathbf{end \ if} \\ \hspace{8em} \mathbf{end \ if} \\ \hspace{7em} \mathbf{end \ if} \\ \hspace{6em} \mathbf{end \ if} \\ \hspace{5em} \mathbf{end \ if} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathrm{description} \gets \mathrm{uscs\_symbology}_{\mathrm{language}, \mathrm{symbol}} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( \mathrm{symbol}, \mathrm{description}.\mathrm{capitalize} \mathopen{}\left( \mathclose{}\right) \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{usda\_symbol} &= \text{USDA symbol}\\
\text{usda\_description} &= \text{USDA description}\\
\text{percent\_sand} &= \text{Percent sand (\%)}\\
\text{percent\_clay} &= \text{Percent clay (\%)}\\
\text{language} &= \text{Language}
\end{align*}
$$

#### `_get_soil_classification_aashto__astm2015d3282_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_soil\_classification\_aashto\_\_astm2015d3282\_scalar}(FC, P_{10}, P_{40}, LL, PI, NP, \mathrm{language}) \\ \hspace{1em} \mathrm{uscs\_symbology} \gets \mathrm{DataMaps}.\mathrm{get\_uscs\_symbology} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ NP \\ \hspace{2em} PI \gets 0 \\ \hspace{2em} LL \gets 0 \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathrm{aashto\_symbol} \gets \mathrm{None} \\ \hspace{1em} \mathrm{group\_index} \gets \mathrm{None} \\ \hspace{1em} \mathrm{description} \gets \textrm{""} \\ \hspace{1em} \mathbf{if} \ \lnot \mathrm{is\_null} \mathopen{}\left( FC \mathclose{}\right) \\ \hspace{2em} \mathbf{if} \ FC \le 35 \\ \hspace{3em} \mathbf{if} \ \lnot \mathrm{np}.\mathrm{any} \mathopen{}\left( \mathrm{is\_null} \mathopen{}\left( \mathopen{}\left[ FC, P_{10}, P_{40} \mathclose{}\right] \mathclose{}\right) \mathclose{}\right) \\ \hspace{4em} \mathrm{aashto\_symbol} \gets \mathrm{get\_aashto\_symbol\_coarse} \mathopen{}\left( FC, P_{10}, P_{40}, LL, PI, NP \mathclose{}\right) \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{if} \ FC > 35 \\ \hspace{3em} \mathbf{if} \ \lnot \mathrm{np}.\mathrm{any} \mathopen{}\left( \mathrm{is\_null} \mathopen{}\left( \mathopen{}\left[ PI, LL \mathclose{}\right] \mathclose{}\right) \mathclose{}\right) \\ \hspace{4em} \mathrm{aashto\_symbol} \gets \mathrm{get\_aashto\_symbol\_fine} \mathopen{}\left( PI, LL \mathclose{}\right) \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{if} \ \mathrm{aashto\_symbol} \not\equiv \mathrm{None} \\ \hspace{3em} \mathrm{group\_index} \gets \mathrm{get\_aashto\_group\_index} \mathopen{}\left( \mathrm{aashto\_symbol}, FC, PI, LL, NP \mathclose{}\right) \\ \hspace{3em} \mathrm{description} \gets \mathrm{uscs\_symbology}_{\mathrm{language}, \mathrm{aashto\_symbol}} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( \mathrm{aashto\_symbol}, \mathrm{group\_index}, \mathrm{description}.\mathrm{capitalize} \mathopen{}\left( \mathclose{}\right) \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{aashto\_symbol} &= \text{AASHTO symbol}\\
GI &= \text{AASHTO group index}\\
\text{aashto\_description} &= \text{AASHTO description}\\
FC &= \text{Fines content (\%)}\\
P_{10} &= \text{Percent passing No. 10 (\%)}\\
P_{40} &= \text{Percent passing No. 40 (\%)}\\
LL &= \text{Liquid limit (\%)}\\
PI &= \text{Plasticity index (\%)}\\
NP &= \text{Non-plastic}\\
\text{language} &= \text{Language}
\end{align*}
$$

#### `_get_soil_classification_uscs__astm2017d2487_coarse_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_soil\_classification\_uscs\_\_astm2017d2487\_coarse\_scalar}(\mathrm{percent\_sand}, \mathrm{percent\_gravel}, FC, C_u, C_c, LL, PI, \mathrm{language}, \mathrm{only\_group\_symbol\_and\_group}, \mathrm{moreno\_alonso\_plasticity\_modification}, \mathrm{has\_organic\_fines}) \\ \hspace{1em} \mathrm{uscs\_symbology} \gets \mathrm{DataMaps}.\mathrm{get\_uscs\_symbology} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathrm{uniformity\_coefficient\_map} \gets \mathrm{dict} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ \mathrm{np}.\mathrm{any} \mathopen{}\left( \mathrm{is\_null} \mathopen{}\left( \mathopen{}\left[ \mathrm{percent\_sand}, \mathrm{percent\_gravel} \mathclose{}\right] \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathrm{group\_symbol} \gets \textrm{"[S/G]"} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathrm{group\_symbol} \gets \left\{ \begin{array}{ll} \textrm{"S"}, & \mathrm{if} \ \mathrm{percent\_sand} \ge \mathrm{percent\_gravel} \\ \textrm{"G"}, & \mathrm{otherwise} \end{array} \right. \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathrm{group} \gets \mathrm{uscs\_symbology}_{\mathrm{language}, \mathrm{group\_symbol}} \\ \hspace{1em} \mathbf{if} \ \mathrm{only\_group\_symbol\_and\_group} \\ \hspace{2em} \mathbf{return} \ \mathopen{}\left( \mathrm{group\_symbol}, \mathrm{group} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{if} \ \mathrm{is\_null} \mathopen{}\left( FC \mathclose{}\right) \\ \hspace{2em} \mathbf{return} \ \mathopen{}\left( \mathrm{group\_symbol}, \mathrm{group} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathrm{combination\_str} \gets \mathrm{uscs\_symbology}_{\mathrm{language}, \textrm{"combination\_str"}} \\ \hspace{1em} \mathrm{combination\_str2} \gets \mathrm{uscs\_symbology}_{\mathrm{language}, \textrm{"combination\_str2"}} \\ \hspace{1em} \mathopen{}\left( \mathrm{fine\_group\_symbol}, \mathrm{fine\_group} \mathclose{}\right) \gets \mathopen{}\left( \mathrm{None}, \mathrm{None} \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ FC \ge 5 \\ \hspace{2em} \mathopen{}\left( \mathrm{fine\_group\_symbol}, \mathrm{fine\_group} \mathclose{}\right) \gets \mathrm{\_get\_soil\_classification\_uscs\_\_astm2017d2487\_fine\_scalar} \mathopen{}\left( LL, PI, \mathrm{percent\_sand}, \mathrm{percent\_gravel} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{if} \ FC \le 12 \\ \hspace{2em} \mathbf{if} \ \mathrm{group\_symbol} \ne \textrm{"[S/G]"} \land \lnot \mathrm{np}.\mathrm{any} \mathopen{}\left( \mathrm{is\_null} \mathopen{}\left( \mathopen{}\left[ C_u, C_c \mathclose{}\right] \mathclose{}\right) \mathclose{}\right) \\ \hspace{3em} \mathrm{graded\_symbol} \gets \left\{ \begin{array}{ll} \textrm{"W"}, & \mathrm{if} \ C_u \ge \mathrm{uniformity\_coefficient\_map}_{\mathrm{group\_symbol}} \land 1 \le C_c \le 3 \\ \textrm{"P"}, & \mathrm{otherwise} \end{array} \right. \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathrm{graded\_symbol} \gets \textrm{"[W/P]"} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathrm{graded\_description} \gets \mathrm{uscs\_symbology}_{\mathrm{language}, \mathrm{graded\_symbol}} \\ \hspace{2em} \mathrm{symbol} \gets \textrm{"\{\}\{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{group\_symbol}, \mathrm{graded\_symbol} \mathclose{}\right) \\ \hspace{2em} \mathrm{description} \gets \left\{ \begin{array}{ll} \textrm{"\{\} \{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{graded\_description}, \mathrm{group} \mathclose{}\right), & \mathrm{if} \ \mathrm{language} = \textrm{"en"} \\ \textrm{"\{\} \{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{group}, \mathrm{graded\_description} \mathclose{}\right), & \mathrm{otherwise} \end{array} \right. \\ \hspace{2em} \mathbf{if} \ FC \ge 5 \\ \hspace{3em} \mathrm{fine\_group\_symbol\_} \gets \mathrm{fine\_group\_symbol} \\ \hspace{3em} \mathbf{if} \ \mathrm{fine\_group\_symbol} \in \mathopen{}\left[ \textrm{"CL-ML"}, \textrm{"CH-MH"} \mathclose{}\right] \\ \hspace{4em} \mathrm{fine\_group\_symbol\_} \gets \textrm{"C"} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{3em} \mathrm{symbol} \gets \mathrm{symbol} + \textrm{"-\{\}\{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{group\_symbol}, \mathrm{fine\_group\_symbol\_} \mathclose{}\right) \\ \hspace{3em} \mathrm{description} \gets \mathrm{description} + \textrm{" \{\} \{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{combination\_str}, \mathrm{fine\_group} \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ FC > 12 \\ \hspace{3em} \mathrm{group\_ey} \gets \mathrm{uscs\_symbology}_{\mathrm{language}, \textrm{"\{\}-ey"}.\mathrm{format} \mathopen{}\left( \mathrm{fine\_group\_symbol} \mathclose{}\right)} \\ \hspace{3em} \mathrm{description} \gets \left\{ \begin{array}{ll} \textrm{"\{\} \{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{group\_ey}, \mathrm{group} \mathclose{}\right), & \mathrm{if} \ \mathrm{language} = \textrm{"en"} \\ \textrm{"\{\} \{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{group}, \mathrm{group\_ey} \mathclose{}\right), & \mathrm{otherwise} \end{array} \right. \\ \hspace{3em} \mathbf{if} \ \mathrm{fine\_group\_symbol} \in \mathopen{}\left[ \textrm{"CL-ML"}, \textrm{"CH-MH"} \mathclose{}\right] \\ \hspace{4em} \mathrm{symbol} \gets \textrm{"\{\}C-\{\}M"}.\mathrm{format} \mathopen{}\left( \mathrm{group\_symbol}, \mathrm{group\_symbol} \mathclose{}\right) \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathrm{symbol} \gets \textrm{"\{\}\{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{group\_symbol}, \mathrm{fine\_group\_symbol} \mathclose{}\right) \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathrm{symbol} \gets \textrm{""} \\ \hspace{3em} \mathrm{description} \gets \textrm{""} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{if} \ \mathrm{group\_symbol} \ne \textrm{"[S/G]"} \\ \hspace{2em} \mathrm{opposite\_group\_symbol} \gets \mathrm{OPPOSITE\_COARSE\_SYMBOL\_d}_{\mathrm{group\_symbol}} \\ \hspace{2em} \mathrm{opposite\_group\_en} \gets \mathrm{uscs\_symbology}_{\textrm{"en"}, \mathrm{opposite\_group\_symbol}} \\ \hspace{2em} \mathrm{opposite\_group} \gets \mathrm{uscs\_symbology}_{\mathrm{language}, \mathrm{opposite\_group\_symbol}} \\ \hspace{2em} \mathbf{if} \ \mathrm{locals} \mathopen{}\left( \mathclose{}\right)_{\textrm{"percent\_\{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{opposite\_group\_en} \mathclose{}\right)} \ge 15 \\ \hspace{3em} \mathrm{combination\_str\_} \gets \left\{ \begin{array}{ll} \mathrm{combination\_str2}, & \mathrm{if} \ \mathrm{combination\_str} \in \mathrm{description} \\ \mathrm{combination\_str}, & \mathrm{otherwise} \end{array} \right. \\ \hspace{3em} \mathrm{description} \gets \mathrm{description} + \textrm{" \{\} \{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{combination\_str\_}, \mathrm{opposite\_group} \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{if} \ \mathrm{has\_organic\_fines} \\ \hspace{3em} \mathrm{description} \gets \mathrm{description} + \textrm{" with organic fines"} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( \mathrm{symbol}, \mathrm{description} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{uscs\_symbol} &= \text{USCS symbol}\\
\text{uscs\_description} &= \text{USCS description}\\
\text{percent\_sand} &= \text{Percent sand (\%)}\\
\text{percent\_gravel} &= \text{Percent gravel (\%)}\\
FC &= \text{Fines content (\%)}\\
C_u &= \text{Uniformity coefficient}\\
C_c &= \text{Curvature coefficient}\\
LL &= \text{Liquid limit (\%)}\\
PI &= \text{Plasticity index (\%)}\\
\text{language} &= \text{Language}\\
\text{moreno\_alonso\_plasticity\_modification} &= \text{Moreno \& Alonso plasticity modification}\\
\text{has\_organic\_fines} &= \text{Has organic fines}
\end{align*}
$$

#### `_get_soil_classification_uscs__astm2017d2487_fine_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_soil\_classification\_uscs\_\_astm2017d2487\_fine\_scalar}(LL, PI, \mathrm{percent\_sand}, \mathrm{percent\_gravel}, \mathrm{language}, \mathrm{only\_group\_symbol\_and\_group}, \mathrm{moreno\_alonso\_plasticity\_modification}, \mathrm{has\_organic\_fines}) \\ \hspace{1em} \mathrm{uscs\_symbology} \gets \mathrm{DataMaps}.\mathrm{get\_uscs\_symbology} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathrm{description} \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{np}.\mathrm{any} \mathopen{}\left( \mathrm{is\_null} \mathopen{}\left( \mathopen{}\left[ LL, PI \mathclose{}\right] \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathrm{group\_symbol} \gets \textrm{"[C/M]"} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{moreno\_alonso\_plasticity\_modification} \\ \hspace{3em} \mathrm{cline\_plasticity\_index} \gets \frac{LL}{2} \\ \hspace{3em} \mathrm{mline\_plasticity\_index} \gets \frac{LL}{3} \\ \hspace{3em} \mathbf{if} \ PI > \mathrm{cline\_plasticity\_index} \\ \hspace{4em} \mathrm{group\_symbol} \gets \textrm{"C"} \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ PI > \mathrm{mline\_plasticity\_index} \\ \hspace{5em} \mathrm{group\_symbol} \gets \left\{ \begin{array}{ll} \textrm{"CL-ML"}, & \mathrm{if} \ LL < 50 \\ \textrm{"CH-MH"}, & \mathrm{otherwise} \end{array} \right. \\ \hspace{4em} \mathbf{else} \\ \hspace{5em} \mathrm{group\_symbol} \gets \textrm{"M"} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathrm{aline\_plots\_on} \gets \left\{ \begin{array}{ll} \textrm{"below"}, & \mathrm{if} \ PI < \left\{ \begin{array}{ll} 4, & \mathrm{if} \ LL \le 25.5 \\ 0.73 \mathopen{}\left( LL - 20 \mathclose{}\right), & \mathrm{otherwise} \end{array} \right. \\ \textrm{"above"}, & \mathrm{otherwise} \end{array} \right. \\ \hspace{3em} \mathbf{if} \ \lnot \mathrm{has\_organic\_fines} \\ \hspace{4em} \mathrm{group\_symbol} \gets \left\{ \begin{array}{ll} \textrm{"C"}, & \mathrm{if} \ \mathrm{aline\_plots\_on} = \textrm{"above"} \\ \textrm{"M"}, & \mathrm{otherwise} \end{array} \right. \\ \hspace{4em} \mathbf{if} \ \mathrm{aline\_plots\_on} = \textrm{"above"} \land 4 \le PI \le 7 \\ \hspace{5em} \mathrm{group\_symbol} \gets \textrm{"CL-ML"} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathrm{group\_symbol} \gets \left\{ \begin{array}{ll} \textrm{"O-C"}, & \mathrm{if} \ \mathrm{aline\_plots\_on} = \textrm{"above"} \\ \textrm{"O-M"}, & \mathrm{otherwise} \end{array} \right. \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathrm{group} \gets \mathrm{uscs\_symbology}_{\mathrm{language}, \mathrm{group\_symbol}} \\ \hspace{1em} \mathbf{if} \ \mathrm{has\_organic\_fines} \\ \hspace{2em} \mathrm{group\_symbol} \gets \mathrm{group\_symbol}.\mathrm{split} \mathopen{}\left( \textrm{"-"} \mathclose{}\right)_{0} \\ \hspace{2em} \mathrm{description} \gets \mathrm{group} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{if} \ \mathrm{only\_group\_symbol\_and\_group} \\ \hspace{2em} \mathbf{return} \ \mathopen{}\left( \mathrm{group\_symbol}, \mathrm{group} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{if} \ \mathrm{group\_symbol} \in \mathopen{}\left[ \textrm{"CL-ML"}, \textrm{"CH-MH"} \mathclose{}\right] \\ \hspace{2em} \mathrm{symbol} \gets \mathrm{group\_symbol} \\ \hspace{2em} \mathrm{description} \gets \mathrm{group} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{is\_null} \mathopen{}\left( LL \mathclose{}\right) \\ \hspace{3em} \mathrm{plasticity\_symbol} \gets \textrm{"[L/H]"} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathrm{plasticity\_symbol} \gets \left\{ \begin{array}{ll} \textrm{"L"}, & \mathrm{if} \ LL < 50 \\ \textrm{"H"}, & \mathrm{otherwise} \end{array} \right. \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathrm{symbol} \gets \textrm{"\{\}\{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{group\_symbol}, \mathrm{plasticity\_symbol} \mathclose{}\right) \\ \hspace{2em} \mathbf{if} \ \mathrm{description} \equiv \mathrm{None} \\ \hspace{3em} \mathrm{plasticity\_description} \gets \mathrm{uscs\_symbology}_{\mathrm{language}, \mathrm{plasticity\_symbol}} \\ \hspace{3em} \mathrm{description} \gets \left\{ \begin{array}{ll} \textrm{"\{\} \{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{plasticity\_description}, \mathrm{group} \mathclose{}\right), & \mathrm{if} \ \mathrm{language} = \textrm{"en"} \\ \textrm{"\{\} \{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{group}, \mathrm{plasticity\_description} \mathclose{}\right), & \mathrm{otherwise} \end{array} \right. \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathrm{combination\_str} \gets \mathrm{uscs\_symbology}_{\mathrm{language}, \textrm{"combination\_str"}} \\ \hspace{1em} \mathopen{}\left( \mathrm{coarse\_group\_symbol}, \mathrm{coarse\_group} \mathclose{}\right) \gets \mathrm{\_get\_soil\_classification\_uscs\_\_astm2017d2487\_coarse\_scalar} \mathopen{}\left( \mathrm{percent\_sand}, \mathrm{percent\_gravel} \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ \mathrm{coarse\_group\_symbol} \ne \textrm{"[S/G]"} \\ \hspace{2em} \mathrm{opposite\_coarse\_group\_en} \gets \mathrm{uscs\_symbology}_{\textrm{"en"}, \mathrm{OPPOSITE\_COARSE\_SYMBOL\_d}_{\mathrm{coarse\_group\_symbol}}} \\ \hspace{2em} \mathrm{opposite\_coarse\_group} \gets \mathrm{uscs\_symbology}_{\mathrm{language}, \mathrm{OPPOSITE\_COARSE\_SYMBOL\_d}_{\mathrm{coarse\_group\_symbol}}} \\ \hspace{2em} \mathbf{if} \ 15 \le \mathrm{percent\_sand} + \mathrm{percent\_gravel} < 30 \\ \hspace{3em} \mathrm{description} \gets \mathrm{description} + \textrm{" \{\} \{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{combination\_str}, \mathrm{coarse\_group} \mathclose{}\right) \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ \mathrm{percent\_sand} + \mathrm{percent\_gravel} \ge 30 \\ \hspace{4em} \mathrm{group\_ey} \gets \mathrm{uscs\_symbology}_{\mathrm{language}, \textrm{"\{\}-ey"}.\mathrm{format} \mathopen{}\left( \mathrm{coarse\_group\_symbol} \mathclose{}\right)} \\ \hspace{4em} \mathbf{if} \ \mathrm{language} = \textrm{"es"} \land \mathrm{group\_symbol} = \textrm{"M"} \\ \hspace{5em} \mathrm{group\_ey} \gets \mathrm{group\_ey}.\mathrm{replace} \mathopen{}\left( \textrm{"osa"}, \textrm{"oso"} \mathclose{}\right) \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{4em} \mathrm{description} \gets \left\{ \begin{array}{ll} \textrm{"\{\} \{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{group\_ey}, \mathrm{description} \mathclose{}\right), & \mathrm{if} \ \mathrm{language} = \textrm{"en"} \\ \textrm{"\{\} \{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{description}, \mathrm{group\_ey} \mathclose{}\right), & \mathrm{otherwise} \end{array} \right. \\ \hspace{4em} \mathbf{if} \ \mathrm{locals} \mathopen{}\left( \mathclose{}\right)_{\textrm{"percent\_\{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{opposite\_coarse\_group\_en} \mathclose{}\right)} \ge 15 \\ \hspace{5em} \mathrm{description} \gets \mathrm{description} + \textrm{" \{\} \{\}"}.\mathrm{format} \mathopen{}\left( \mathrm{combination\_str}, \mathrm{opposite\_coarse\_group} \mathclose{}\right) \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( \mathrm{symbol}, \mathrm{description} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{uscs\_symbol} &= \text{USCS symbol}\\
\text{uscs\_description} &= \text{USCS description}\\
LL &= \text{Liquid limit (\%)}\\
PI &= \text{Plasticity index (\%)}\\
\text{percent\_sand} &= \text{Percent sand (\%)}\\
\text{percent\_gravel} &= \text{Percent gravel (\%)}\\
\text{language} &= \text{Language}\\
\text{moreno\_alonso\_plasticity\_modification} &= \text{Moreno \& Alonso plasticity modification}\\
\text{has\_organic\_fines} &= \text{Has organic fines}
\end{align*}
$$

#### `_get_soil_classification_uscs__astm2017d2487_scalar`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{\_get\_soil\_classification\_uscs\_\_astm2017d2487\_scalar}(FC, \mathrm{percent\_sand}, \mathrm{percent\_gravel}, LL, PI, C_u, C_c, NP, \mathrm{language}, \mathrm{moreno\_alonso\_plasticity\_modification}, P_{4}, PL, \mathrm{has\_organic\_fines}) \\ \hspace{1em} \mathbf{if} \ NP \\ \hspace{2em} PI \gets 0 \\ \hspace{2em} LL \gets 0 \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{if} \ \lnot \mathrm{is\_null} \mathopen{}\left( PL \mathclose{}\right) \\ \hspace{2em} \mathbf{if} \ \mathrm{is\_null} \mathopen{}\left( PI \mathclose{}\right) \\ \hspace{3em} PI \gets LL - PL \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{if} \ \lnot \mathrm{is\_null} \mathopen{}\left( P_{4} \mathclose{}\right) \\ \hspace{2em} \mathbf{if} \ \mathrm{is\_null} \mathopen{}\left( \mathrm{percent\_gravel} \mathclose{}\right) \\ \hspace{3em} \mathrm{percent\_gravel} \gets 100 - P_{4} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{if} \ \mathrm{is\_null} \mathopen{}\left( \mathrm{percent\_sand} \mathclose{}\right) \\ \hspace{3em} \mathrm{percent\_sand} \gets P_{4} - FC \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{if} \ \lnot \mathrm{np}.\mathrm{any} \mathopen{}\left( \mathrm{is\_null} \mathopen{}\left( \mathopen{}\left[ FC, \mathrm{percent\_sand}, \mathrm{percent\_gravel} \mathclose{}\right] \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathrm{percent\_sum} \gets \sum \mathopen{}\left[ FC, \mathrm{percent\_sand}, \mathrm{percent\_gravel} \mathclose{}\right] \\ \hspace{2em} \mathbf{if} \ \lnot \mathrm{np}.\mathrm{isclose} \mathopen{}\left( \mathrm{percent\_sum}, 100 \mathclose{}\right) \\ \hspace{3em} \mathrm{raise\_value\_error} \mathopen{}\left( \textrm{"Sum of fines, sand \& gravel \% = \{\} not equal to 100\%"}.\mathrm{format} \mathopen{}\left( \mathrm{percent\_sum} \mathclose{}\right) \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathrm{symbol} \gets \textrm{""} \\ \hspace{1em} \mathrm{description} \gets \textrm{""} \\ \hspace{1em} \mathbf{if} \ \lnot \mathrm{is\_null} \mathopen{}\left( FC \mathclose{}\right) \\ \hspace{2em} \mathbf{if} \ FC < 50 \\ \hspace{3em} \mathopen{}\left( \mathrm{symbol}, \mathrm{description} \mathclose{}\right) \gets \mathrm{\_get\_soil\_classification\_uscs\_\_astm2017d2487\_coarse\_scalar} \mathopen{}\left( \mathrm{percent\_sand}, \mathrm{percent\_gravel}, FC, C_u, C_c, LL, PI, \mathrm{language} \mathclose{}\right) \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ FC \ge 50 \\ \hspace{4em} \mathopen{}\left( \mathrm{symbol}, \mathrm{description} \mathclose{}\right) \gets \mathrm{\_get\_soil\_classification\_uscs\_\_astm2017d2487\_fine\_scalar} \mathopen{}\left( LL, PI, \mathrm{percent\_sand}, \mathrm{percent\_gravel}, \mathrm{language} \mathclose{}\right) \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( \mathrm{symbol}, \mathrm{description}.\mathrm{capitalize} \mathopen{}\left( \mathclose{}\right) \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{uscs\_symbol} &= \text{USCS symbol}\\
\text{uscs\_description} &= \text{USCS description}\\
FC &= \text{Fines content (\%)}\\
\text{percent\_sand} &= \text{Percent sand (\%)}\\
\text{percent\_gravel} &= \text{Percent gravel (\%)}\\
LL &= \text{Liquid limit (\%)}\\
PI &= \text{Plasticity index (\%)}\\
C_u &= \text{Uniformity coefficient}\\
C_c &= \text{Curvature coefficient}\\
NP &= \text{Non-plastic}\\
\text{language} &= \text{Language}\\
\text{moreno\_alonso\_plasticity\_modification} &= \text{Moreno \& Alonso plasticity modification}\\
P_{4} &= \text{Percent passing No. 4 (\%)}\\
PL &= \text{Plastic limit (\%)}\\
\text{has\_organic\_fines} &= \text{Has organic fines}
\end{align*}
$$

#### `get_a2_group`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_a2\_group}(PI, LL) \\ \hspace{1em} \mathbf{if} \ \mathrm{is\_null} \mathopen{}\left( LL \mathclose{}\right) \\ \hspace{2em} \mathbf{return} \ \textrm{"A-2"} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ PI \le 10 \\ \hspace{3em} \mathbf{if} \ LL \le 40 \\ \hspace{4em} \mathbf{return} \ \textrm{"A-2-4"} \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ LL > 40 \\ \hspace{5em} \mathbf{return} \ \textrm{"A-2-5"} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ PI > 10 \\ \hspace{4em} \mathbf{if} \ LL \le 40 \\ \hspace{5em} \mathbf{return} \ \textrm{"A-2-6"} \\ \hspace{4em} \mathbf{else} \\ \hspace{5em} \mathbf{if} \ LL > 40 \\ \hspace{6em} \mathbf{return} \ \textrm{"A-2-7"} \\ \hspace{5em} \mathbf{end \ if} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{return} \ \mathrm{None} \\ \hspace{1em} \mathbf{end \ if} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{aashto\_symbol} &= \text{AASHTO symbol}\\
PI &= \text{Plasticity index (\%)}\\
LL &= \text{Liquid limit (\%)}
\end{align*}
$$

#### `get_aashto_group_index`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_aashto\_group\_index}(\mathrm{aashto\_symbol}, FC, PI, LL, NP) \\ \begin{array}{l} \hspace{1em} \mathbf{function} \ \mathrm{aashto\_group\_index\_round}(\mathrm{gi}) \\ \hspace{2em} \textrm{"Round AASHTO Group Index values to nearest integer, with 0.5 rounding up to 1"} \\ \hspace{2em} \mathbf{return} \ \mathopen{}\left\lceil \mathrm{gi} - 0.5 \mathclose{}\right\rceil \\ \hspace{1em} \mathbf{end \ function} \end{array} \\ \hspace{1em} \mathbf{if} \ \mathrm{aashto\_symbol} \in \mathopen{}\left[ \textrm{"A-1-a"}, \textrm{"A-1-b"}, \textrm{"A-3"}, \textrm{"A-2-4"}, \textrm{"A-2-5"} \mathclose{}\right] \\ \hspace{2em} \mathbf{return} \ 0 \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ NP \land \mathrm{is\_null} \mathopen{}\left( LL \mathclose{}\right) \\ \hspace{3em} \mathbf{return} \ 0 \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathrm{group\_index} \gets \mathrm{None} \\ \hspace{3em} \mathbf{if} \ \lnot \mathrm{is\_null} \mathopen{}\left( PI \mathclose{}\right) \\ \hspace{4em} \mathrm{group\_index\_plasticity\_index\_portion} \gets 0.01 \mathopen{}\left( FC - 15 \mathclose{}\right) \mathopen{}\left( PI - 10 \mathclose{}\right) \\ \hspace{4em} \mathbf{if} \ \mathrm{aashto\_symbol} \in \mathopen{}\left[ \textrm{"A-2-6"}, \textrm{"A-2-7"} \mathclose{}\right] \\ \hspace{5em} \mathrm{group\_index} \gets \mathrm{group\_index\_plasticity\_index\_portion} \\ \hspace{4em} \mathbf{else} \\ \hspace{5em} \mathbf{if} \ \lnot \mathrm{is\_null} \mathopen{}\left( LL \mathclose{}\right) \\ \hspace{6em} \mathrm{group\_index} \gets \mathopen{}\left( FC - 35 \mathclose{}\right) \mathopen{}\left( 0.2 + 0.005 \mathopen{}\left( LL - 40 \mathclose{}\right) \mathclose{}\right) + \mathrm{group\_index\_plasticity\_index\_portion} \\ \hspace{5em} \mathbf{end \ if} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{if} \ \lnot \mathrm{is\_null} \mathopen{}\left( \mathrm{group\_index} \mathclose{}\right) \\ \hspace{4em} \mathbf{return} \ \mathrm{aashto\_group\_index\_round} \mathopen{}\left( \mathrm{np}.\mathrm{clip} \mathopen{}\left( \mathrm{group\_index}, 0, \mathrm{None} \mathclose{}\right) \mathclose{}\right).\mathrm{astype} \mathopen{}\left( \mathrm{int} \mathclose{}\right) \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{return} \ \mathrm{None} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
GI &= \text{AASHTO group index}\\
\text{aashto\_symbol} &= \text{AASHTO symbol}\\
FC &= \text{Fines content (\%)}\\
PI &= \text{Plasticity index (\%)}\\
LL &= \text{Liquid limit (\%)}\\
NP &= \text{Non-plastic}
\end{align*}
$$

#### `get_aashto_symbol_coarse`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_aashto\_symbol\_coarse}(FC, P_{10}, P_{40}, LL, PI, NP) \\ \hspace{1em} \mathbf{if} \ P_{10} \le 50 \land P_{40} \le 30 \land FC \le 15 \land PI \le 6 \\ \hspace{2em} \mathbf{return} \ \textrm{"A-1-a"} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ P_{40} \le 50 \\ \hspace{3em} \mathbf{if} \ \lnot \mathrm{is\_null} \mathopen{}\left( PI \mathclose{}\right) \\ \hspace{4em} \mathbf{if} \ FC \le 25 \land PI \le 6 \\ \hspace{5em} \mathbf{return} \ \textrm{"A-1-b"} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{return} \ \mathrm{get\_a2\_group} \mathopen{}\left( PI, LL \mathclose{}\right) \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ P_{40} > 50 \\ \hspace{4em} \mathbf{if} \ FC \le 10 \land \mathopen{}\left( NP \lor PI = 0 \mathclose{}\right) \\ \hspace{5em} \mathbf{return} \ \textrm{"A-3"} \\ \hspace{4em} \mathbf{else} \\ \hspace{5em} \mathbf{return} \ \mathrm{get\_a2\_group} \mathopen{}\left( PI, LL \mathclose{}\right) \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathrm{None} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{aashto\_symbol} &= \text{AASHTO symbol}\\
FC &= \text{Fines content (\%)}\\
P_{10} &= \text{Percent passing No. 10 (\%)}\\
P_{40} &= \text{Percent passing No. 40 (\%)}\\
LL &= \text{Liquid limit (\%)}\\
PI &= \text{Plasticity index (\%)}\\
NP &= \text{Non-plastic}
\end{align*}
$$

#### `get_aashto_symbol_fine`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_aashto\_symbol\_fine}(PI, LL) \\ \hspace{1em} \mathrm{aashto\_symbol} \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ PI \le 10 \\ \hspace{2em} \mathbf{if} \ LL \le 40 \\ \hspace{3em} \mathrm{aashto\_symbol} \gets \textrm{"A-4"} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathbf{if} \ LL > 40 \\ \hspace{4em} \mathrm{aashto\_symbol} \gets \textrm{"A-5"} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ PI > 10 \\ \hspace{3em} \mathbf{if} \ LL \le 40 \\ \hspace{4em} \mathrm{aashto\_symbol} \gets \textrm{"A-6"} \\ \hspace{3em} \mathbf{else} \\ \hspace{4em} \mathbf{if} \ LL > 40 \\ \hspace{5em} \mathbf{if} \ PI \le LL - 30 \\ \hspace{6em} \mathrm{aashto\_symbol} \gets \textrm{"A-7-5"} \\ \hspace{5em} \mathbf{else} \\ \hspace{6em} \mathbf{if} \ PI > LL - 30 \\ \hspace{7em} \mathrm{aashto\_symbol} \gets \textrm{"A-7-6"} \\ \hspace{6em} \mathbf{end \ if} \\ \hspace{5em} \mathbf{end \ if} \\ \hspace{4em} \mathbf{end \ if} \\ \hspace{3em} \mathbf{end \ if} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathrm{aashto\_symbol} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{aashto\_symbol} &= \text{AASHTO symbol}\\
PI &= \text{Plasticity index (\%)}\\
LL &= \text{Liquid limit (\%)}
\end{align*}
$$

#### `get_soil_classification__usda1993soil`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_classification\_\_usda1993soil}(\mathrm{percent\_sand}, \mathrm{percent\_clay}, \mathrm{language}) \\ \hspace{1em} \mathrm{soil\_classification\_\_usda1993soil} \gets \mathrm{\_get\_soil\_classification\_\_usda1993soil\_vec} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{soil\_classification\_\_usda1993soil} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{usda\_symbol} &= \text{USDA symbol}\\
\text{usda\_description} &= \text{USDA description}\\
\text{percent\_sand} &= \text{Percent sand (\%)}\\
\text{percent\_clay} &= \text{Percent clay (\%)}\\
\text{language} &= \text{Language}
\end{align*}
$$

#### `get_soil_classification_aashto__astm2015d3282`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_classification\_aashto\_\_astm2015d3282}(FC, P_{10}, P_{40}, LL, PI, NP, \mathrm{language}) \\ \hspace{1em} \mathrm{soil\_classification\_aashto} \gets \mathrm{\_get\_soil\_classification\_aashto\_\_astm2015d3282\_vec} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{soil\_classification\_aashto} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{aashto\_symbol} &= \text{AASHTO symbol}\\
GI &= \text{AASHTO group index}\\
\text{aashto\_description} &= \text{AASHTO description}\\
FC &= \text{Fines content (\%)}\\
P_{10} &= \text{Percent passing No. 10 (\%)}\\
P_{40} &= \text{Percent passing No. 40 (\%)}\\
LL &= \text{Liquid limit (\%)}\\
PI &= \text{Plasticity index (\%)}\\
NP &= \text{Non-plastic}\\
\text{language} &= \text{Language}
\end{align*}
$$

#### `get_soil_classification_uscs__astm2017d2487`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_classification\_uscs\_\_astm2017d2487}(FC, \mathrm{percent\_sand}, \mathrm{percent\_gravel}, LL, PI, C_u, C_c, NP, \mathrm{language}, \mathrm{moreno\_alonso\_plasticity\_modification}, P_{4}, PL, \mathrm{has\_organic\_fines}) \\ \hspace{1em} \mathrm{soil\_classification\_uscs\_\_astm2017d2487} \gets \mathrm{\_get\_soil\_classification\_uscs\_\_astm2017d2487\_vec} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{soil\_classification\_uscs\_\_astm2017d2487} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{uscs\_symbol} &= \text{USCS symbol}\\
\text{uscs\_description} &= \text{USCS description}\\
FC &= \text{Fines content (\%)}\\
\text{percent\_sand} &= \text{Percent sand (\%)}\\
\text{percent\_gravel} &= \text{Percent gravel (\%)}\\
LL &= \text{Liquid limit (\%)}\\
PI &= \text{Plasticity index (\%)}\\
C_u &= \text{Uniformity coefficient}\\
C_c &= \text{Curvature coefficient}\\
NP &= \text{Non-plastic}\\
\text{language} &= \text{Language}\\
\text{moreno\_alonso\_plasticity\_modification} &= \text{Moreno \& Alonso plasticity modification}\\
P_{4} &= \text{Percent passing No. 4 (\%)}\\
PL &= \text{Plastic limit (\%)}\\
\text{has\_organic\_fines} &= \text{Has organic fines}
\end{align*}
$$

#### `get_soil_classification_usda__moreno2018clay`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_soil\_classification\_usda\_\_moreno2018clay}(\mathrm{percent\_sand}, LL, PI, NP, \mathrm{language}) \\ \hspace{1em} \mathrm{uscs\_symbology} \gets \mathrm{DataMaps}.\mathrm{get\_uscs\_symbology} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} \mathrm{language} \gets \mathrm{np}.\mathrm{squeeze} \mathopen{}\left( \mathrm{language} \mathclose{}\right).\mathrm{item} \mathopen{}\left( \mathclose{}\right) \\ \hspace{1em} PI \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( NP, 0, PI \mathclose{}\right) \\ \hspace{1em} LL \gets \mathrm{np}.\mathrm{where} \mathopen{}\left( NP, 1, LL \mathclose{}\right) \\ \hspace{1em} \mathrm{symbol} \gets \mathrm{USDAMoreno2018ChartFigure}.\mathrm{assign\_polygons\_labels\_from\_xy\_data} \mathopen{}\left( \mathrm{percent\_sand}, \mathrm{np}.\mathrm{clip} \mathopen{}\left( \frac{PI}{LL}, 0.0001, 1 \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathrm{description} \gets \mathopen{}\left[  \mathclose{}\right] \\ \hspace{1em} \mathbf{for} \ \mathrm{symbol\_} \in \mathrm{np}.\mathrm{atleast\_1d} \mathopen{}\left( \mathrm{symbol} \mathclose{}\right) \ \mathbf{do} \\ \hspace{2em} \mathbf{if} \ \mathrm{symbol\_} \ne \textrm{""} \\ \hspace{3em} \mathrm{description\_} \gets \mathrm{uscs\_symbology}_{\mathrm{language}, \mathrm{symbol\_}} \\ \hspace{2em} \mathbf{else} \\ \hspace{3em} \mathrm{description\_} \gets \textrm{""} \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{2em} \mathrm{description}.\mathrm{append} \mathopen{}\left( \mathrm{description\_}.\mathrm{capitalize} \mathopen{}\left( \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ for} \\ \hspace{1em} \mathbf{return} \ \mathopen{}\left( \mathrm{symbol}, \mathrm{description} \mathclose{}\right) \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{usda\_symbol} &= \text{USDA symbol}\\
\text{usda\_description} &= \text{USDA description}\\
\text{percent\_sand} &= \text{Percent sand (\%)}\\
LL &= \text{Liquid limit (\%)}\\
PI &= \text{Plasticity index (\%)}\\
NP &= \text{Non-plastic}\\
\text{language} &= \text{Language}
\end{align*}
$$
