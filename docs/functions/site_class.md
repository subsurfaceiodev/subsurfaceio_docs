---
title: site_class.py
---

#### `get_average_blow_count`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_average\_blow\_count}(z, N, z_{top}, z_{bottom}) \\ \hspace{1em} N \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( N, \mathrm{None}, 100 \mathclose{}\right) \\ \hspace{1em} N_{30} \gets \mathrm{get\_site\_class\_average} \mathopen{}\left( N, z, z_{top}, z_{bottom} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ N_{30} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
N_{30} &= \text{Average blow count}\\
z &= \text{Depth (m)}\\
N &= \text{Blow count}\\
z_{top} &= \text{Average top depth (m)}\\
z_{bottom} &= \text{Average bottom depth (m)}
\end{align*}
$$

#### `get_average_shear_velocity`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_average\_shear\_velocity}(z, V_s, z_{top}, z_{bottom}, \mathrm{shallow\_velocity\_extrapolation\_method}) \\ \hspace{1em} \mathrm{valid\_flag} \gets \mathord{\sim} \mathopen{}\left( \mathrm{np}.\mathrm{isnan} \mathopen{}\left( V_s \mathclose{}\right) \mathbin{|} \mathopen{}\left( V_s = 0 \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathrm{depth\_valid} \gets \mathrm{np}.\mathrm{extract} \mathopen{}\left( \mathrm{valid\_flag}, z \mathclose{}\right) \\ \hspace{1em} \mathbf{if} \ \mathrm{depth\_valid}.\mathrm{size} = 0 \\ \hspace{2em} \mathrm{depth\_max} \gets 0 \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathrm{depth\_max} \gets \mathrm{np}.\mathrm{max} \mathopen{}\left( \mathrm{depth\_valid} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{if} \ \lnot \mathrm{is\_null} \mathopen{}\left( \mathrm{shallow\_velocity\_extrapolation\_method} \mathclose{}\right) \land \mathopen{}\left( \mathrm{depth\_max} \ge 10 \mathclose{}\right) \mathbin{\&} \mathopen{}\left( \mathrm{depth\_max} < 30 \mathclose{}\right) \\ \hspace{2em} \mathrm{vsd} \gets \mathrm{get\_site\_class\_average} \mathopen{}\left( V_s, z \mathclose{}\right) \\ \hspace{2em} \mathrm{table2} \gets \mathrm{ReferenceData}.\mathrm{Boore04Table2} \\ \hspace{2em} \mathrm{idx} \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( \mathrm{np}.\mathrm{searchsorted} \mathopen{}\left( \mathrm{table2}_{\textrm{"depth"}}, \mathrm{depth\_max} \mathclose{}\right), \mathrm{None}, 19 \mathclose{}\right) \\ \hspace{2em} \mathopen{}\left( a, b \mathclose{}\right) \gets \mathopen{}\left( \mathrm{table2}_{\textrm{"a"}, \mathrm{idx}}, \mathrm{table2}_{\textrm{"b"}, \mathrm{idx}} \mathclose{}\right) \\ \hspace{2em} V_{s30} \gets 10^{a + b \cdot \log_{10} \mathrm{vsd}} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} V_{s30} \gets \mathrm{get\_site\_class\_average} \mathopen{}\left( V_s, z, z_{top}, z_{bottom} \mathclose{}\right) \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ V_{s30} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
V_{s30} &= \text{Average shear velocity (m/s)}\\
z &= \text{Depth (m)}\\
V_s &= \text{Shear velocity (m/s)}\\
z_{top} &= \text{Average top depth (m)}\\
z_{bottom} &= \text{Average bottom depth (m)}\\
\text{shallow\_velocity\_extrapolation\_method} &= \text{Shallow velocity extrapolation method}
\end{align*}
$$

#### `get_average_undrained_shear_strength`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_average\_undrained\_shear\_strength}(z, S_u, z_{top}, z_{bottom}) \\ \hspace{1em} S_u \gets \mathrm{np}.\mathrm{clip} \mathopen{}\left( S_u, \mathrm{None}, 250 \mathclose{}\right) \\ \hspace{1em} S_{u30} \gets \mathrm{get\_site\_class\_average} \mathopen{}\left( S_u, z, z_{top}, z_{bottom} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ S_{u30} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
S_{u30} &= \text{Average undrained shear strength (kPa)}\\
z &= \text{Depth (m)}\\
S_u &= \text{Undrained shear strength (kPa)}\\
z_{top} &= \text{Average top depth (m)}\\
z_{bottom} &= \text{Average bottom depth (m)}
\end{align*}
$$

#### `get_site_class`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_site\_class}(\mathrm{is\_e\_site\_class}, \mathrm{is\_f1\_site\_class}, \mathrm{is\_f2\_site\_class}, \mathrm{is\_f3\_site\_class}, \mathrm{is\_f4\_site\_class}) \\ \hspace{1em} \mathrm{site\_classes} \gets \mathopen{}\left[  \mathclose{}\right] \\ \hspace{1em} \mathbf{for} \ \mathopen{}\left( \mathrm{is\_class}, \mathrm{site\_class\_} \mathclose{}\right) \in \mathrm{zip} \mathopen{}\left( \mathopen{}\left[ \mathopen{}\left[ \mathrm{is\_e\_site\_class} \mathclose{}\right], \mathopen{}\left[ \mathrm{is\_f1\_site\_class}, \mathrm{is\_f2\_site\_class}, \mathrm{is\_f3\_site\_class}, \mathrm{is\_f4\_site\_class} \mathclose{}\right] \mathclose{}\right], \mathopen{}\left[ \textrm{"E"}, \textrm{"F"} \mathclose{}\right] \mathclose{}\right) \ \mathbf{do} \\ \hspace{2em} \mathbf{if} \ \mathrm{np}.\mathrm{any} \mathopen{}\left( \mathrm{is\_class} \mathclose{}\right) \\ \hspace{3em} \mathrm{site\_classes}.\mathrm{append} \mathopen{}\left( \mathrm{site\_class\_} \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ for} \\ \hspace{1em} \mathrm{site\_classes} \gets \mathopen{}\left[ \mathrm{sc} \mid \mathopen{}\left( \mathrm{sc} \in \mathrm{site\_classes} \mathclose{}\right) \land \mathopen{}\left( \lnot \mathrm{is\_null} \mathopen{}\left( \mathrm{sc} \mathclose{}\right) \mathclose{}\right) \mathclose{}\right] \\ \hspace{1em} \mathbf{if} \ \lnot \mathrm{site\_classes} \\ \hspace{2em} \mathrm{site\_class} \gets \mathrm{None} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathrm{site\_classes} \gets \mathrm{sorted} \mathopen{}\left( \mathrm{site\_classes} \mathclose{}\right) \\ \hspace{2em} \mathrm{site\_class} \gets \mathrm{site\_classes}_{0} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ \mathrm{site\_class} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{site\_class} &= \text{Site class}\\
\text{is\_e\_site\_class} &= \text{Is E site class}\\
\text{is\_f1\_site\_class} &= \text{Is F1 site class}\\
\text{is\_f2\_site\_class} &= \text{Is F2 site class}\\
\text{is\_f3\_site\_class} &= \text{Is F3 site class}\\
\text{is\_f4\_site\_class} &= \text{Is F4 site class}
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

#### `get_site_class_average_blow_count`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_site\_class\_average\_blow\_count}(N_{30}) \\ \hspace{1em} \mathrm{site\_class} \gets \mathrm{PARAMETERS}_{\textrm{"average\_blow\_count"}}.\mathrm{data\_bins}_{\textrm{"site\_class"}}.\mathrm{bin\_data} \mathopen{}\left( N_{30} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{site\_class} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{site\_class} &= \text{Site class}\\
N_{30} &= \text{Average blow count}
\end{align*}
$$

#### `get_site_class_average_shear_velocity`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_site\_class\_average\_shear\_velocity}(V_{s30}) \\ \hspace{1em} \mathrm{site\_class} \gets \mathrm{PARAMETERS}_{\textrm{"average\_shear\_velocity"}}.\mathrm{data\_bins}_{\textrm{"site\_class"}}.\mathrm{bin\_data} \mathopen{}\left( V_{s30} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{site\_class} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{site\_class} &= \text{Site class}\\
V_{s30} &= \text{Average shear velocity (m/s)}
\end{align*}
$$

#### `get_site_class_average_undrained_shear_strength`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_site\_class\_average\_undrained\_shear\_strength}(S_{u30}) \\ \hspace{1em} \mathrm{site\_class} \gets \mathrm{PARAMETERS}_{\textrm{"average\_undrained\_shear\_strength"}}.\mathrm{data\_bins}_{\textrm{"site\_class"}}.\mathrm{bin\_data} \mathopen{}\left( S_{u30} \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{site\_class} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{site\_class} &= \text{Site class}\\
S_{u30} &= \text{Average undrained shear strength (kPa)}
\end{align*}
$$

#### `get_site_class_label`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_site\_class\_label}(\mathrm{site\_class}) \\ \hspace{1em} \mathrm{site\_class\_label} \gets \mathrm{replace\_from\_mapping} \mathopen{}\left( \mathrm{site\_class}, \mathrm{PARAMETERS}.\mathrm{get\_pair\_discrete\_field\_mapping} \mathopen{}\left( \textrm{"site\_class"}, \textrm{"site\_class\_label"} \mathclose{}\right) \mathclose{}\right) \\ \hspace{1em} \mathbf{return} \ \mathrm{site\_class\_label} \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
\text{site\_class\_label} &= \text{Site class label}\\
\text{site\_class} &= \text{Site class}
\end{align*}
$$

#### `get_site_period`

##### latex { data-search-exclude }

$$
\begin{array}{l} \mathbf{function} \ \mathrm{get\_site\_period}(V_s, z, \mathrm{method}) \\ \hspace{1em} H \gets \mathrm{get\_thickness} \mathopen{}\left( z \mathclose{}\right) \\ \hspace{1em} T_n \gets \mathrm{None} \\ \hspace{1em} \mathbf{if} \ \mathrm{method} = \textrm{"weighted average"} \\ \hspace{2em} \mathrm{depth\_max} \gets \mathrm{np}.\mathrm{max} \mathopen{}\left( z \mathclose{}\right) \\ \hspace{2em} \mathrm{vs\_asterisk} \gets \frac{\sum \mathopen{}\left( V_s \cdot H \mathclose{}\right)}{\mathrm{depth\_max}} \\ \hspace{2em} T_n \gets \frac{4 \mathrm{depth\_max}}{\mathrm{vs\_asterisk}} \\ \hspace{1em} \mathbf{else} \\ \hspace{2em} \mathbf{if} \ \mathrm{method} = \textrm{"sum of periods"} \\ \hspace{3em} T_n \gets 4 \sum \mathopen{}\left( \frac{H}{V_s} \mathclose{}\right) \\ \hspace{2em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{end \ if} \\ \hspace{1em} \mathbf{return} \ T_n \\ \mathbf{end \ function} \end{array}
$$

$$
\begin{align*}
T_n &= \text{Site period (s)}\\
V_s &= \text{Shear velocity (m/s)}\\
z &= \text{Depth (m)}\\
\text{method} &= \text{Method}
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
