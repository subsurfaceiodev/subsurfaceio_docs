
### `a_parameter`
**symbol**: $A$  
**label**: A parameter  
**unit**: None  
**description**: Hydrometer parameter dependent on temperature and specific gravity  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `aashto_description`
**symbol**: $\text{aashto\_description}$  
**label**: AASHTO description  
**unit**: None  
**description**: AASHTO classification system description  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `aashto_group_index`
**symbol**: $GI$  
**label**: AASHTO group index  
**unit**: None  
**description**: AASHTO classification system group index  
**data_type**: `int`  
**corresponding_parameter_name**: `None`  
    

### `aashto_symbol`
**symbol**: $\text{aashto\_symbol}$  
**label**: AASHTO symbol  
**unit**: None  
**description**: AASHTO classification system symbol  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='A-1-a' value_secondary=None color=None  
value='A-1-b' value_secondary=None color=None  
value='A-3' value_secondary=None color=None  
value='A-2-4' value_secondary=None color=None  
value='A-2-5' value_secondary=None color=None  
value='A-2-6' value_secondary=None color=None  
value='A-2-7' value_secondary=None color=None  
value='A-4' value_secondary=None color=None  
value='A-5' value_secondary=None color=None  
value='A-6' value_secondary=None color=None  
value='A-7-5' value_secondary=None color=None  
value='A-7-6' value_secondary=None color=None  
value='A-8' value_secondary=None color=None  

### `acceleration`
**symbol**: $a$  
**label**: Acceleration  
**unit**: g  
**description**: Acceleration  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `active_pile_length`
**symbol**: $L_a$  
**label**: Active pile length  
**unit**: m  
**description**: Active pile length in lateral mode (typically < L_p)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `alternative_normalized_cone_resistance`
**symbol**: $Q_{t1}$  
**label**: Alternative normalized cone resistance  
**unit**: None  
**description**: Alternative normalized cone resistance from CPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `alternative_normalized_friction_ratio`
**symbol**: $F$  
**label**: Alternative normalized friction ratio  
**unit**: %  
**description**: Normalized friction ratio from cone tip resistance  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `apply_20_percent_rule`
**symbol**: $\text{apply\_20\_percent\_rule}$  
**label**: Apply 20% rule  
**unit**: None  
**description**: Ignores settlements where 20% of effective stress exceeds applied stress change  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `area_replacement_ratio`
**symbol**: $A_r$  
**label**: Area replacement ratio  
**unit**: None  
**description**: Ratio of one column area to the unit cell area  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `associated_file`
**symbol**: $\text{associated\_file}$  
**label**: Associated file  
**unit**: None  
**description**: Associated file reference  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `atmospheric_pressure`
**symbol**: $P_a$  
**label**: Atmospheric pressure  
**unit**: kPa  
**description**: Atmospheric pressure  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `average_blow_count`
**symbol**: $N_{30}$  
**label**: Average blow count  
**unit**: None  
**description**: Average SPT blow count to 30 m depth  
**data_type**: `float`  
**corresponding_parameter_name**: `site_class`  
    
#### data_bins

parameter_name: site_class

left=0.0 right=15.0 value='E' color=None  
left=15.0 right=50.0 value='D' color=None  
left=50.0 right=inf value='C' color=None  

### `average_bottom_depth`
**symbol**: $z_{bottom}$  
**label**: Average bottom depth  
**unit**: m  
**description**: Special average bottom depth  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `average_effective_shear_velocity`
**symbol**: $V_{s,avg}$  
**label**: Average effective shear velocity  
**unit**: m/s  
**description**: Average effective profile velocity  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `average_effective_shear_velocity_reduced`
**symbol**: $V_{s,avg\ red}$  
**label**: Average effective shear velocity reduced  
**unit**: m/s  
**description**: Average effective profile velocity reduced for strain compatibility  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `average_shear_velocity`
**symbol**: $V_{s30}$  
**label**: Average shear velocity  
**unit**: m/s  
**description**: Average shear wave velocity to 30 m depth  
**data_type**: `float`  
**corresponding_parameter_name**: `site_class`  
    
#### data_bins

parameter_name: site_class

left=0.0 right=180.0 value='E' color=None  
left=180.0 right=360.0 value='D' color=None  
left=360.0 right=760.0 value='C' color=None  
left=760.0 right=1500.0 value='B' color=None  
left=1500.0 right=inf value='A' color=None  

### `average_shear_velocity_12m`
**symbol**: $V_{s12}$  
**label**: Average shear velocity 12 m  
**unit**: m/s  
**description**: Average shear wave velocity to 12 m depth  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `average_top_depth`
**symbol**: $z_{top}$  
**label**: Average top depth  
**unit**: m  
**description**: Special average top depth  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `average_undrained_shear_strength`
**symbol**: $S_{u30}$  
**label**: Average undrained shear strength  
**unit**: kPa  
**description**: Average undrained shear strength to 30 m depth  
**data_type**: `float`  
**corresponding_parameter_name**: `site_class`  
    
#### data_bins

parameter_name: site_class

left=0.0 right=50.0 value='E' color=None  
left=50.0 right=100.0 value='D' color=None  
left=100.0 right=inf value='C' color=None  

### `basic_influence_factor_i1`
**symbol**: $I_1$  
**label**: Basic influence factor I1  
**unit**: None  
**description**: Pile settlement basic influence factor  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `bearing_capacity_factor`
**symbol**: $R_k$  
**label**: Bearing capacity factor  
**unit**: None  
**description**: Bearing capacity factor  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `bearing_capacity_factor_cohesion`
**symbol**: $N_c$  
**label**: Bearing capacity factor for cohesion  
**unit**: None  
**description**: Bearing capacity factor for cohesion  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `bearing_capacity_factor_cohesion_bottom_layer`
**symbol**: $N_{c\ bottom}$  
**label**: Bearing capacity factor for cohesion bottom layer  
**unit**: None  
**description**: Bearing capacity factor for cohesion of soil beneath foundation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `bearing_capacity_factor_surcharge`
**symbol**: $N_q$  
**label**: Bearing capacity factor for surcharge  
**unit**: None  
**description**: Bearing capacity factor for surcharge  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `bearing_capacity_factor_surcharge_bottom_layer`
**symbol**: $N_{q\ bottom}$  
**label**: Bearing capacity factor for surcharge bottom layer  
**unit**: None  
**description**: Bearing capacity factor for surcharge of soil beneath foundation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `bearing_capacity_factor_unit_weight`
**symbol**: $N_γ$  
**label**: Bearing capacity factor for unit weight  
**unit**: None  
**description**: Bearing capacity factor for unit weight  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `bearing_capacity_factor_unit_weight_bottom_layer`
**symbol**: $N_{γ\ bottom}$  
**label**: Bearing capacity factor for unit weight bottom layer  
**unit**: None  
**description**: Bearing capacity factor for unit weight of soil beneath foundation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `bearing_capacity_ratio`
**symbol**: ${q_2}/{q_1}$  
**label**: Bearing capacity ratio  
**unit**: None  
**description**: Ratio of bearing capacities q_2 to q_1  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `behaviour_correction_factor`
**symbol**: $K_c$  
**label**: Behaviour correction factor  
**unit**: None  
**description**: Correction factor for soil behavior  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `below_water_table`
**symbol**: $\text{below\_water\_table}$  
**label**: Below water table  
**unit**: None  
**description**: Indicates if soil layer is below water table  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `blow_count`
**symbol**: $N$  
**label**: Blow count  
**unit**: None  
**description**: SPT measured blow count  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `borehole_diameter`
**symbol**: $D_{bh}$  
**label**: Borehole diameter  
**unit**: mm  
**description**: Diameter of borehole for SPT or sampling  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    
#### data_bins

parameter_name: borehole_diameter_correction

left=0.0 right=115.1 value=1 color=None  
left=115.1 right=150.1 value=1.05 color=None  
left=150.1 right=inf value=1.15 color=None  

### `borehole_diameter_correction`
**symbol**: $C_B$  
**label**: Borehole diameter correction  
**unit**: None  
**description**: SPT correction factor for borehole diameter  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `boring_type`
**symbol**: $\text{boring\_type}$  
**label**: Boring type  
**unit**: None  
**description**: Type of boring  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `bulk_density`
**symbol**: $ρ$  
**label**: Bulk density  
**unit**: g/cm3  
**description**: Bulk soil density  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `can_mass`
**symbol**: $W_{can}$  
**label**: Can mass  
**unit**: g  
**description**: Mass of soil sample can  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `can_plus_dry_soil_mass`
**symbol**: $W_{can+drysoil}$  
**label**: Can + dry soil mass  
**unit**: g  
**description**: Mass of soil sample can plus dry soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `can_plus_wet_soil_mass`
**symbol**: $W_{can+wetsoil}$  
**label**: Can + wet soil mass  
**unit**: g  
**description**: Mass of soil sample can plus wet soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `careful_execution`
**symbol**: $\text{careful\_execution}$  
**label**: Careful execution  
**unit**: None  
**description**: Indicates careful execution with minimal soil disturbance  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `clean_sand_normalized_blow_count`
**symbol**: $N_{160cs}$  
**label**: Clean sand normalized blow count  
**unit**: None  
**description**: Equivalent clean sand SPT blow count (N_160)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `clean_sand_normalized_blow_count_sr`
**symbol**: $N_{160cs-Sr}$  
**label**: Clean sand normalized blow count (Sr)  
**unit**: None  
**description**: Equivalent clean sand N_160 for residual shear strength  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `clean_sand_normalized_cone_resistance`
**symbol**: $Q_{tncs}$  
**label**: Clean sand normalized cone resistance  
**unit**: None  
**description**: Normalized cone resistance for clean sand  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `clean_sand_normalized_cone_resistance_1atm`
**symbol**: $q_{c1Ncs}$  
**label**: Clean sand normalized cone resistance at 1 atm  
**unit**: None  
**description**: Equivalent clean sand normalized cone resistance at 1 atm  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `clean_sand_normalized_cone_resistance_1atm_sr`
**symbol**: $q_{c1Ncs-Sr}$  
**label**: Clean sand normalized cone resistance at 1 atm (Sr)  
**unit**: None  
**description**: Equivalent clean sand normalized cone resistance at 1 atm for residual shear strength  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `client`
**symbol**: $\text{client}$  
**label**: Client  
**unit**: None  
**description**: Client name  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `coefficient_of_consolidation`
**symbol**: $C_v$  
**label**: Coefficient of consolidation  
**unit**: m2/year  
**description**: Coefficient of consolidation for soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `coefficient_of_earth_pressure_at_rest`
**symbol**: $K_o$  
**label**: Coefficient of lateral earth pressure at rest  
**unit**: None  
**description**: Coefficient of lateral earth pressure at rest  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `compactability`
**symbol**: $\text{compactability}$  
**label**: Compactability  
**unit**: None  
**description**: Soil compactability description  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Compactable' value_secondary=None color='red'  
value='Less compactable' value_secondary=None color='orange'  
value='Already dense' value_secondary=None color='yellow'  

### `compactness`
**symbol**: $\text{compactness}$  
**label**: Compactness  
**unit**: None  
**description**: Soil compactness description  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Very loose' value_secondary=None color='gainsboro'  
value='Loose' value_secondary=None color='lightgray'  
value='Medium' value_secondary=None color='silver'  
value='Dense' value_secondary=None color='darkgray'  
value='Very dense' value_secondary=None color='gray'  

### `compression_index`
**symbol**: $C_c$  
**label**: Compression index  
**unit**: None  
**description**: Compression index for soil consolidation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `compression_ratio`
**symbol**: $CR$  
**label**: Compression ratio  
**unit**: None  
**description**: Compression ratio for soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `compressional_velocity`
**symbol**: $V_p$  
**label**: Compressional velocity  
**unit**: m/s  
**description**: Compressional wave velocity in soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `cone_area_ratio`
**symbol**: $a$  
**label**: Cone area ratio  
**unit**: None  
**description**: Net area ratio for CPT cone  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `cone_tip_resistance`
**symbol**: $q_c$  
**label**: Cone tip resistance  
**unit**: MPa  
**description**: Cone tip resistance from CPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `consider_creep_settlement`
**symbol**: $\text{consider\_creep\_settlement}$  
**label**: Consider creep settlement  
**unit**: None  
**description**: Indicates if creep settlement is considered in calculations  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `consistency`
**symbol**: $\text{consistency}$  
**label**: Consistency  
**unit**: None  
**description**: Soil consistency description  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Very soft' value_secondary='Squishes between fingers when squeezed' color='gainsboro'  
value='Soft' value_secondary='Very easily deformed by squeezing' color='lightgray'  
value='Medium' value_secondary='??' color='silver'  
value='Stiff' value_secondary='Hard to deform by hand squeezing' color='darkgray'  
value='Very stiff' value_secondary='Very hard to deform by hand squeezing' color='gray'  
value='Hard' value_secondary='Nearly impossible to deform by hand' color='dimgray'  

### `consolidation_state`
**symbol**: $\text{consolidation\_state}$  
**label**: Consolidation state  
**unit**: None  
**description**: Soil consolidation state description  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='UC' value_secondary='Under consolidated' color='gainsboro'  
value='NC' value_secondary='Normally consolidated' color='lightgray'  
value='LOC' value_secondary='Lightly over consolidated' color='silver'  
value='MOC' value_secondary='Moderately over consolidated' color='darkgray'  
value='HOC' value_secondary='Heavily over consolidated' color='gray'  

### `consolidation_time`
**symbol**: $t$  
**label**: Consolidation time  
**unit**: month  
**description**: Time for soil consolidation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `constant_volume_friction_angle`
**symbol**: $ϕ_{cv}$  
**label**: Constant volume friction angle  
**unit**: °  
**description**: Constant volume friction angle of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `constrained_modulus`
**symbol**: $M$  
**label**: Constrained modulus  
**unit**: MPa  
**description**: Constrained modulus of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `constrained_modulus_factor`
**symbol**: $α_M$  
**label**: Constrained modulus factor  
**unit**: None  
**description**: Factor for constrained modulus calculation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `contractor`
**symbol**: $\text{contractor}$  
**label**: Contractor  
**unit**: None  
**description**: Contractor name  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `coordinate_x`
**symbol**: $x$  
**label**: Coordinate x  
**unit**: m  
**description**: X-axis coordinate in spatial analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `coordinate_y`
**symbol**: $y$  
**label**: Coordinate y  
**unit**: m  
**description**: Y-axis coordinate in spatial analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `corrected_blow_count`
**symbol**: $N_{60}$  
**label**: Corrected blow count  
**unit**: None  
**description**: Blow count corrected for field conditions  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    
#### data_bins

parameter_name: compactness

left=0.0 right=4.0 value='Very loose' color='gainsboro'  
left=4.0 right=10.0 value='Loose' color='lightgray'  
left=10.0 right=30.0 value='Medium' color='silver'  
left=30.0 right=50.0 value='Dense' color='darkgray'  
left=50.0 right=inf value='Very dense' color='gray'  
parameter_name: unit_weight.Coarse.Moist

left=0.0 right=4.0 value=15.7 color=None  
left=4.0 right=10.0 value=17.3 color=None  
left=10.0 right=30.0 value=18.9 color=None  
left=30.0 right=inf value=19.6 color=None  
parameter_name: unit_weight.Coarse.Saturated

left=0.0 right=4.0 value=17.3 color=None  
left=4.0 right=10.0 value=18.9 color=None  
left=10.0 right=30.0 value=19.6 color=None  
left=30.0 right=inf value=21.2 color=None  
parameter_name: unit_weight.Fine.Moist

left=0.0 right=4.0 value=15.7 color=None  
left=4.0 right=8.0 value=17.3 color=None  
left=8.0 right=inf value=18.1 color=None  
parameter_name: unit_weight.Fine.Saturated

left=0.0 right=4.0 value=17.3 color=None  
left=4.0 right=8.0 value=18.9 color=None  
left=8.0 right=inf value=19.6 color=None  

### `corrected_cone_tip_resistance`
**symbol**: $q_t$  
**label**: Corrected cone tip resistance  
**unit**: MPa  
**description**: Corrected cone tip resistance from CPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `corrected_hydrometer_reading`
**symbol**: $R_{cp}$  
**label**: Corrected hydrometer reading  
**unit**: None  
**description**: Corrected hydrometer reading for percent finer calculation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `corrected_pressure_p0`
**symbol**: $P_0$  
**label**: Corrected pressure P0  
**unit**: kPa  
**description**: Corrected first dilatometer reading  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `corrected_pressure_p1`
**symbol**: $P_1$  
**label**: Corrected pressure P1  
**unit**: kPa  
**description**: Corrected second dilatometer reading  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `corrected_pressure_p2`
**symbol**: $P_2$  
**label**: Corrected pressure P2  
**unit**: kPa  
**description**: Corrected third dilatometer reading  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `crew`
**symbol**: $\text{crew}$  
**label**: Crew  
**unit**: None  
**description**: Name or identifier of the crew performing the test  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `cross_correlation_lag`
**symbol**: $\text{cross\_correlation\_lag}$  
**label**: Cross correlation lag  
**unit**: None  
**description**: Cross correlation lag of sleeve friction relative to cone resistance  
**data_type**: `int`  
**corresponding_parameter_name**: `None`  
    

### `cumulative_mass_retained`
**symbol**: $W_{n\ cum}$  
**label**: Cumulative mass retained  
**unit**: g  
**description**: Cumulative mass of soil retained on sieves  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `cumulative_thickness_liquefiable_layers`
**symbol**: $T_{15}$  
**label**: Cumulative thickness of liquefiable layers  
**unit**: m  
**description**: Cumulative thickness of saturated granular layers with N_160 < 15  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `curvature_coefficient`
**symbol**: $C_c$  
**label**: Curvature coefficient  
**unit**: None  
**description**: Curvature coefficient for particle size distribution  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `cyclic_resistance_ratio`
**symbol**: $CRR$  
**label**: Cyclic resistance ratio  
**unit**: None  
**description**: Cyclic resistance ratio for liquefaction  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `cyclic_resistance_ratio_magnitude_7_5`
**symbol**: $CRR_{7.5}$  
**label**: Cyclic resistance ratio magnitude 7.5  
**unit**: None  
**description**: Cyclic resistance ratio adjusted to moment magnitude 7.5  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `cyclic_resistance_ratio_slope`
**symbol**: $m_{CRR}$  
**label**: Cyclic resistance ratio slope  
**unit**: None  
**description**: Slope of liquefaction resistance boundaries  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `cyclic_stress_ratio`
**symbol**: $CSR$  
**label**: Cyclic stress ratio  
**unit**: None  
**description**: Cyclic stress ratio for liquefaction  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `cyclic_stress_ratio_ss_20_1d_1atm`
**symbol**: $CSR_{SS,20,1D,1atm}$  
**label**: Cyclic stress ratio SS,20,1D,1atm  
**unit**: None  
**description**: CSR value corresponding to a 1 dimensional, 20 uniform loading cycles simple shear test under a confinement pressure of 1 atm  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `damping_ratio`
**symbol**: $ζ$  
**label**: Damping ratio  
**unit**: None  
**description**: Soil or structural damping ratio  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `dashpot_coefficient`
**symbol**: $c$  
**label**: Dashpot coefficient  
**unit**: MN-s/m or MN-m/rad  
**description**: Dashpot coefficient for translation (MN-s/m) or rotation (MN-m/rad)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `dashpot_coefficient_intensity`
**symbol**: $ci$  
**label**: Dashpot coefficient intensity  
**unit**: MN-s/m3  
**description**: Dashpot coefficient intensity  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `dashpot_coefficient_intensity_vertical`
**symbol**: $c_z^i$  
**label**: Dashpot coefficient intensity vertical  
**unit**: MN-s/m3  
**description**: Vertical dashpot coefficient intensity  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `dashpot_coefficient_vertical`
**symbol**: $c_z$  
**label**: Dashpot coefficient vertical  
**unit**: MN-s/m or MN-m/rad  
**description**: Vertical dashpot coefficient for translation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `dashpot_edge_factor`
**symbol**: $R_c$  
**label**: Dashpot edge factor  
**unit**: None  
**description**: Dashpot edge decrease factor  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `date`
**symbol**: $\text{date}$  
**label**: Date  
**unit**: None  
**description**: Date sample taken  
**data_type**: `date`  
**corresponding_parameter_name**: `None`  
    

### `date_end`
**symbol**: $\text{date\_end}$  
**label**: Date end  
**unit**: None  
**description**: Date when testing or analysis ended  
**data_type**: `date`  
**corresponding_parameter_name**: `None`  
    

### `date_start`
**symbol**: $\text{date\_start}$  
**label**: Date start  
**unit**: None  
**description**: Date when testing or analysis started  
**data_type**: `date`  
**corresponding_parameter_name**: `None`  
    

### `default_unit_weight`
**symbol**: $γ_{default}$  
**label**: Default unit weight  
**unit**: kN/m3  
**description**: Unit weight used for missing or undefined values  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `depth`
**symbol**: $z$  
**label**: Depth  
**unit**: m  
**description**: Depth below ground surface to bottom of layer  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `depth_bottom`
**symbol**: $z_{bottom}$  
**label**: Depth bottom  
**unit**: m  
**description**: Depth below ground surface to bottom of layer  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `depth_factor_cohesion`
**symbol**: $d_c$  
**label**: Depth factor for cohesion  
**unit**: None  
**description**: Depth factor for cohesion in bearing capacity  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `depth_factor_surcharge`
**symbol**: $d_q$  
**label**: Depth factor for surcharge  
**unit**: None  
**description**: Depth factor for surcharge in bearing capacity  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `depth_factor_unit_weight`
**symbol**: $d_γ$  
**label**: Depth factor for unit weight  
**unit**: None  
**description**: Depth factor for unit weight in bearing capacity  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `depth_middle`
**symbol**: $z_{middle}$  
**label**: Depth middle  
**unit**: m  
**description**: Depth below ground surface to middle of layer  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `depth_plus_rod_length`
**symbol**: $\text{depth\_plus\_rod\_length}$  
**label**: Depth plus rod length  
**unit**: m  
**description**: Depth plus SPT rod length  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    
#### data_bins

parameter_name: rod_length_correction

left=0.0 right=3.0 value=0.75 color=None  
left=3.0 right=4.0 value=0.8 color=None  
left=4.0 right=6.0 value=0.85 color=None  
left=6.0 right=10.0 value=0.95 color=None  
left=10.0 right=inf value=1 color=None  

### `depth_top`
**symbol**: $z_{top}$  
**label**: Depth top  
**unit**: m  
**description**: Depth below ground surface to top of layer  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `description`
**symbol**: $\text{description}$  
**label**: Description  
**unit**: None  
**description**: Description  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `diameter_at_10_percent_finer`
**symbol**: $D_{10}$  
**label**: Diameter at 10% finer  
**unit**: mm  
**description**: Diameter at 10% finer from sieve analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `diameter_at_30_percent_finer`
**symbol**: $D_{30}$  
**label**: Diameter at 30% finer  
**unit**: mm  
**description**: Diameter at 30% finer from sieve analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `diameter_at_50_percent_finer`
**symbol**: $D_{50}$  
**label**: Diameter at 50% finer  
**unit**: mm  
**description**: Diameter at 50% finer from sieve analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `diameter_at_50_percent_finer_liquefiable_layers`
**symbol**: $D_{50T15}$  
**label**: Diameter at 50% finer of liquefiable layers  
**unit**: mm  
**description**: Average mean grain size for liquefiable layers within T_15  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `diameter_at_60_percent_finer`
**symbol**: $D_{60}$  
**label**: Diameter at 60% finer  
**unit**: mm  
**description**: Diameter at 60% finer from sieve analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `dilatometer_constrained_modulus_factor`
**symbol**: $R_M$  
**label**: Dilatometer constrained modulus factor  
**unit**: None  
**description**: DMT factor for constrained modulus calculation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `dilatometer_modulus`
**symbol**: $E_d$  
**label**: Dilatometer modulus  
**unit**: MPa  
**description**: Dilatometer modulus from DMT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `dimensionless_frequency`
**symbol**: $a_0$  
**label**: Dimensionless frequency  
**unit**: None  
**description**: Dimensionless frequency for dynamic analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `dimensionless_pile_length_parameter`
**symbol**: $λL$  
**label**: Dimensionless pile length parameter  
**unit**: None  
**description**: Dimensionless pile length parameter  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `dimensionless_pile_tip_stiffness`
**symbol**: $Ω$  
**label**: Dimensionless pile tip stiffness  
**unit**: None  
**description**: Dimensionless pile tip stiffness  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `dimensionless_subgrade_reaction_modulus`
**symbol**: $δ$  
**label**: Dimensionless subgrade reaction modulus  
**unit**: None  
**description**: Dimensionless modulus of subgrade reaction  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `dry_density`
**symbol**: $ρ_{dry}$  
**label**: Dry density  
**unit**: g/cm3  
**description**: Dry soil density  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `dry_soil_mass`
**symbol**: $W_{dry\ soil}$  
**label**: Dry soil mass  
**unit**: g  
**description**: Dry soil mass in sample  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `dry_unit_weight`
**symbol**: $γ_{dry}$  
**label**: Dry unit weight  
**unit**: kN/m3  
**description**: Unit weight of soil under dry conditions  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `ductility_ratio`
**symbol**: $μ$  
**label**: Ductility ratio  
**unit**: None  
**description**: Ductility ratio for structural analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `dynamic_stiffness_modifier`
**symbol**: $α$  
**label**: Dynamic stiffness modifier  
**unit**: None  
**description**: Frequency-dependent stiffness modifier for mode j  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `easting`
**symbol**: $\text{easting}$  
**label**: Easting  
**unit**: m  
**description**: UTM WGS84 easting coordinate  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `effective_cone_resistance`
**symbol**: $q_E$  
**label**: Effective cone resistance  
**unit**: MPa  
**description**: Effective cone resistance from CPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `effective_cone_resistance_geometric_mean`
**symbol**: $q_{Eg}$  
**label**: Effective cone resistance geometric mean  
**unit**: MPa  
**description**: Geometric mean of effective cone resistance over influence zone  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `effective_length`
**symbol**: $L$  
**label**: Effective length  
**unit**: cm  
**description**: Effective length for hydrometer particle size calculation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `effective_length_corrected_reading`
**symbol**: $R_{cL}$  
**label**: Effective length corrected reading  
**unit**: None  
**description**: Corrected reading for effective length determination  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `effective_profile_depth`
**symbol**: $z_p$  
**label**: Effective profile depth  
**unit**: m  
**description**: Effective profile depth for analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `effective_profile_depth_rotation`
**symbol**: $z_p$  
**label**: Effective profile depth (rotation)  
**unit**: m  
**description**: Effective profile depth for foundation rotation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `effective_shear_depth`
**symbol**: $H$  
**label**: Effective shear depth  
**unit**: m  
**description**: Effective footing shear depth  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `effective_stress`
**symbol**: $σ_v'$  
**label**: Effective stress  
**unit**: kPa  
**description**: Effective vertical stress in soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `effective_unit_weight`
**symbol**: $γ'$  
**label**: Effective unit weight  
**unit**: kN/m3  
**description**: Effective unit weight of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `effective_unit_weight_bottom_layer`
**symbol**: $γ_{bottom}'$  
**label**: Effective unit weight bottom layer  
**unit**: kN/m3  
**description**: Effective unit weight of soil beneath foundation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `elasticity_modulus`
**symbol**: $E_s$  
**label**: Elasticity modulus  
**unit**: MPa  
**description**: Modulus of elasticity of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `elasticity_modulus_bearing_ratio`
**symbol**: $E_b\ /\ E_s$  
**label**: Elasticity modulus bearing ratio  
**unit**: None  
**description**: Ratio of elasticity modulus of bearing soil to soil along pile shaft  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `elasticity_modulus_bearing_soil`
**symbol**: $E_b$  
**label**: Elasticity modulus of bearing soil  
**unit**: MPa  
**description**: Modulus of elasticity of bearing stratum below pile tip  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `elasticity_to_constrained_modulus_ratio`
**symbol**: $E_s\ /\ M$  
**label**: Elasticity to constrained modulus ratio  
**unit**: None  
**description**: Ratio of elasticity modulus to constrained modulus  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `elevation`
**symbol**: $\text{elevation}$  
**label**: Elevation  
**unit**: m  
**description**: Elevation of ground surface or soil layer bottom depth  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `embedment_factor`
**symbol**: $η$  
**label**: Embedment factor  
**unit**: None  
**description**: Embedment correction factor for rigid footing spring constants  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `end_length_ratio`
**symbol**: $R_e$  
**label**: End length ratio  
**unit**: None  
**description**: End length ratio  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `energy_ratio`
**symbol**: $ER$  
**label**: Energy ratio  
**unit**: %  
**description**: SPT equipment measured energy ratio  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `energy_ratio_correction`
**symbol**: $C_E$  
**label**: Energy ratio correction  
**unit**: None  
**description**: SPT correction factor for energy ratio  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `engineer`
**symbol**: $\text{engineer}$  
**label**: Engineer  
**unit**: None  
**description**: Engineer name  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `equivalent_cone_resistance`
**symbol**: $q_{ca}$  
**label**: Equivalent cone resistance  
**unit**: MPa  
**description**: LCPC method equivalent average cone resistance  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `equivalent_cone_resistance_primed`
**symbol**: $q'_{ca}$  
**label**: Equivalent cone resistance primed  
**unit**: MPa  
**description**: LCPC method mean cone resistance between -a and +a (a = 1.5D)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `exclude_clay_like_sands`
**symbol**: $\text{exclude\_clay\_like\_sands}$  
**label**: Exclude clay-like sands  
**unit**: None  
**description**: Ignores clayey sands (SC) with FC > 35% and PI > 12% for SPT-based liquefaction  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `final_depth`
**symbol**: $z_{final}$  
**label**: Final depth  
**unit**: m  
**description**: Final depth  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `fines_content`
**symbol**: $FC$  
**label**: Fines content  
**unit**: %  
**description**: Percentage of fines passing No. 200 sieve  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    
#### data_bins

parameter_name: normalized_blow_count_fines_inc

left=0.0 right=10.0 value=1.0 color=None  
left=10.0 right=25.0 value=2.0 color=None  
left=25.0 right=50.0 value=4.0 color=None  
left=50.0 right=75.0 value=5.0 color=None  
left=75.0 right=inf value=5.0 color=None  
parameter_name: normalized_cone_resistance_fines_inc

left=0.0 right=10.0 value=10.0 color=None  
left=10.0 right=25.0 value=25.0 color=None  
left=25.0 right=50.0 value=45.0 color=None  
left=50.0 right=75.0 value=55.0 color=None  
left=75.0 right=inf value=55.0 color=None  

### `fines_content_factor`
**symbol**: $C_{FINES}$  
**label**: Fines content factor  
**unit**: None  
**description**: Fines content factor for liquefaction analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `fines_content_fitting_parameter`
**symbol**: $C(FC)$  
**label**: Fines content fitting parameter  
**unit**: None  
**description**: Fines content fitting parameter for liquefaction  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `fines_content_liquefiable_layers`
**symbol**: $FC_{T15}$  
**label**: Fines content of liquefiable layers  
**unit**: %  
**description**: Average fines content for liquefiable layers within T_15  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `first_interval_blow_count`
**symbol**: $N_{first}$  
**label**: First interval blow count  
**unit**: None  
**description**: First interval blow count in SPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `flow_index`
**symbol**: $I_F$  
**label**: Flow index  
**unit**: None  
**description**: Slope of liquid limit flow line  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `footing_applied_load`
**symbol**: $q_o$  
**label**: Footing applied load  
**unit**: kPa  
**description**: Applied pressure or load on footing  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `footing_creep_settlement_inc`
**symbol**: $S_{creep}$  
**label**: Footing creep settlement inc.  
**unit**: cm  
**description**: Incremental creep settlement of footing  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `footing_creep_settlement_sum`
**symbol**: $ΣS_{creep}$  
**label**: Footing creep settlement sum  
**unit**: cm  
**description**: Sum of footing creep settlement increments  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `footing_embedment`
**symbol**: $D_f$  
**label**: Footing embedment  
**unit**: m  
**description**: Depth of footing embedment  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `footing_embedment_to_width_ratio`
**symbol**: $k$  
**label**: Footing embedment to width ratio  
**unit**: None  
**description**: Ratio of footing embedment to width  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `footing_half_length`
**symbol**: $L_h$  
**label**: Footing half length  
**unit**: m  
**description**: Footing half-length (large plan dimension)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `footing_half_width`
**symbol**: $B_h$  
**label**: Footing half width  
**unit**: m  
**description**: Footing half-width (small plan dimension)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `footing_influence_depth`
**symbol**: $z_{infl}$  
**label**: Footing influence depth  
**unit**: m  
**description**: Depth of influence for footing  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `footing_influence_width_factor`
**symbol**: $IF$  
**label**: Footing influence width factor  
**unit**: None  
**description**: Footing depth of influence width factor  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `footing_length`
**symbol**: $L$  
**label**: Footing length  
**unit**: m  
**description**: Footing length (large plan dimension)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `footing_settlement`
**symbol**: $S$  
**label**: Footing settlement  
**unit**: cm  
**description**: Settlement of footing  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `footing_settlement_inc`
**symbol**: $S_i$  
**label**: Footing settlement inc.  
**unit**: cm  
**description**: Incremental settlement of footing  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `footing_settlement_sum`
**symbol**: $ΣS$  
**label**: Footing settlement sum  
**unit**: cm  
**description**: Sum of footing settlement increments  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `footing_shape`
**symbol**: $\text{footing\_shape}$  
**label**: Footing shape  
**unit**: None  
**description**: Shape of footing  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='square' value_secondary=None color=None  
value='circular' value_secondary=None color=None  
value='rectangular' value_secondary=None color=None  
value='continuous' value_secondary=None color=None  

### `footing_width`
**symbol**: $B$  
**label**: Footing width  
**unit**: m  
**description**: Footing width (small plan dimension)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `footing_zone`
**symbol**: $\text{footing\_zone}$  
**label**: Footing zone  
**unit**: None  
**description**: Footing intensity zone description  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `foundation_contact_pressure`
**symbol**: $Q$  
**label**: Foundation contact pressure  
**unit**: kPa  
**description**: Contact pressure of building's foundation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `foundation_is_embedded`
**symbol**: $\text{foundation\_is\_embedded}$  
**label**: Foundation is embedded  
**unit**: None  
**description**: Indicates if foundation is embedded  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `fourth_interval_blow_count`
**symbol**: $N_{fourth}$  
**label**: Fourth interval blow count  
**unit**: None  
**description**: Fourth interval blow count in SPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `free_air_correction_a_reading`
**symbol**: $ΔA$  
**label**: Free air correction to A reading  
**unit**: kPa  
**description**: Free air correction for dilatometer A reading  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `free_air_correction_b_reading`
**symbol**: $ΔB$  
**label**: Free air correction to B reading  
**unit**: kPa  
**description**: Free air correction for dilatometer B reading  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `free_face_height`
**symbol**: $H$  
**label**: Free face height  
**unit**: m  
**description**: Height of free face for lateral spreading analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `free_face_length`
**symbol**: $L$  
**label**: Free face length  
**unit**: m  
**description**: Distance from base of free face to point of interest  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `friction_angle`
**symbol**: $ϕ$  
**label**: Friction angle  
**unit**: °  
**description**: Friction angle of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    
#### data_bins

parameter_name: compactness

left=0.0 right=28.0 value='Very loose' color='gainsboro'  
left=28.0 right=30.0 value='Loose' color='lightgray'  
left=30.0 right=36.0 value='Medium' color='silver'  
left=36.0 right=41.0 value='Dense' color='darkgray'  
left=41.0 right=inf value='Very dense' color='gray'  

### `friction_angle_bottom_layer`
**symbol**: $ϕ_{bottom}$  
**label**: Friction angle bottom layer  
**unit**: °  
**description**: Friction angle of sand layer beneath foundation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `friction_ratio`
**symbol**: $R_f$  
**label**: Friction ratio  
**unit**: %  
**description**: Friction ratio from CPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `generalized_interstory_drift`
**symbol**: $GID$  
**label**: Generalized interstory drift  
**unit**: cm  
**description**: Generalized interstory drift for seismic analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `geological_epoch`
**symbol**: $\text{geological\_epoch}$  
**label**: Geological epoch  
**unit**: None  
**description**: Geological epoch of soil formation  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='Holocene' value_secondary=None color=None  
value='Pleistocene' value_secondary=None color=None  

### `grain_angularity`
**symbol**: $\text{grain\_angularity}$  
**label**: Grain angularity  
**unit**: None  
**description**: Description of soil grain angularity  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='angular' value_secondary=None color=None  
value='round' value_secondary=None color=None  

### `ground_slope`
**symbol**: $S$  
**label**: Ground slope  
**unit**: %  
**description**: Slope of ground surface  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `hammer_drop_system`
**symbol**: $\text{hammer\_drop\_system}$  
**label**: Hammer drop system  
**unit**: None  
**description**: Hammer drop system  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `hardening_ratio`
**symbol**: $\text{hardening\_ratio}$  
**label**: Hardening ratio  
**unit**: None  
**description**: Stiffness-hardening ratio for soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `has_organic_fines`
**symbol**: $\text{has\_organic\_fines}$  
**label**: Has organic fines  
**unit**: None  
**description**: Indicates if the soil contains organic fines  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `horizontal_stress_index`
**symbol**: $K_d$  
**label**: Horizontal stress index  
**unit**: None  
**description**: Horizontal stress index from DMT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `hydrometer_reading`
**symbol**: $R$  
**label**: Hydrometer reading  
**unit**: None  
**description**: Hydrometer reading (151H: specific gravity, 152H: grams per liter)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `hydrometer_time`
**symbol**: $\text{hydrometer\_time}$  
**label**: Hydrometer time  
**unit**: min  
**description**: Elapsed time for hydrometer test  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `hydrometer_type`
**symbol**: $\text{hydrometer\_type}$  
**label**: Hydrometer type  
**unit**: None  
**description**: Type of hydrometer used  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='151H' value_secondary=None color=None  
value='152H' value_secondary=None color=None  

### `imposed_stress`
**symbol**: $Δ_σ$  
**label**: Imposed stress  
**unit**: kPa  
**description**: Imposed stress on soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `inclination`
**symbol**: $\text{inclination}$  
**label**: Inclination  
**unit**: °  
**description**: Penetration inclination relative to vertical  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `inhomogeneity_alpha`
**symbol**: $a$  
**label**: Inhomogeneity alpha  
**unit**: None  
**description**: Inhomogeneity alpha parameter  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `inhomogeneity_exponent`
**symbol**: $n$  
**label**: Inhomogeneity exponent  
**unit**: None  
**description**: Inhomogeneity exponent for soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `initial_static_shear_correction`
**symbol**: $K_α$  
**label**: Initial static shear correction  
**unit**: None  
**description**: Correction for initial static shear stress ratio  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `initial_void_ratio`
**symbol**: $e_o$  
**label**: Initial void ratio  
**unit**: None  
**description**: Initial void ratio of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `is_disturbed_soil`
**symbol**: $\text{is\_disturbed\_soil}$  
**label**: Is disturbed soil  
**unit**: None  
**description**: Indicates if soil sample is disturbed  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `is_e_site_class`
**symbol**: $\text{is\_e\_site\_class}$  
**label**: Is E site class  
**unit**: None  
**description**: Thickness of clay with [PI (%) > 20 & wc (%) ≥ 40 & Su (kPa) < 24] > 3  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `is_f1_site_class`
**symbol**: $\text{is\_f1\_site\_class}$  
**label**: Is F1 site class  
**unit**: None  
**description**: Soils vulnerable to potential failure / collapse under seismic loading: liquefiable soils, quick / highly sensitive clays, collapsible weakly cemented soils  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `is_f2_site_class`
**symbol**: $\text{is\_f2\_site\_class}$  
**label**: Is F2 site class  
**unit**: None  
**description**: Thickness of Peat and/or highly organic clays > 3  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `is_f3_site_class`
**symbol**: $\text{is\_f3\_site\_class}$  
**label**: Is F3 site class  
**unit**: None  
**description**: Thickness of Very high plasticity clays [PI (%) > 75] > 8  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `is_f4_site_class`
**symbol**: $\text{is\_f4\_site\_class}$  
**label**: Is F4 site class  
**unit**: None  
**description**: Thickness of Very thick, soft/medium stiff clays [Su (kPa) < 50] > 36  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `is_fine_soil`
**symbol**: $\text{is\_fine\_soil}$  
**label**: Is fine soil  
**unit**: None  
**description**: Indicates if soil is fine-grained  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `is_fine_soil_criteria`
**symbol**: $\text{is\_fine\_soil\_criteria}$  
**label**: Is fine soil criteria  
**unit**: None  
**description**: Criteria for fine soil classification  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='sbtn' value_secondary=None color=None  
value='ic_cutoff' value_secondary=None color=None  

### `is_homogeneous_soil`
**symbol**: $\text{is\_homogeneous\_soil}$  
**label**: Is homogeneous soil  
**unit**: None  
**description**: Indicates if soil is homogeneous  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `is_invalid_data`
**symbol**: $\text{is\_invalid\_data}$  
**label**: Is invalid data  
**unit**: None  
**description**: Indicates invalid input data  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `is_long_pile`
**symbol**: $\text{is\_long\_pile}$  
**label**: Is long pile  
**unit**: None  
**description**: Indicates if pile is long  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `is_potentially_liquefiable`
**symbol**: $\text{is\_potentially\_liquefiable}$  
**label**: Is potentially liquefiable  
**unit**: None  
**description**: Indicates if soil is potentially liquefiable  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `is_potentially_liquefiable_thickness`
**symbol**: $\text{is\_potentially\_liquefiable\_thickness}$  
**label**: Is potentially liquefiable thickness  
**unit**: m  
**description**: Thickness of potentially liquefiable group  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `is_sandy_gravel`
**symbol**: $\text{is\_sandy\_gravel}$  
**label**: Is sandy gravel  
**unit**: None  
**description**: Indicates if soil is sandy gravel  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `is_t15_liquefiable_layers`
**symbol**: $T_{15\ flag}$  
**label**: Is T15 liquefiable layers  
**unit**: None  
**description**: Liquefiable layers with N_160 < 15  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `ist_test_type`
**symbol**: $\text{ist\_test\_type}$  
**label**: Seismic test type  
**unit**: None  
**description**: Seismic test type  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `language`
**symbol**: $\text{language}$  
**label**: Language  
**unit**: None  
**description**: Language  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='en' value_secondary=None color=None  
value='es' value_secondary=None color=None  
value='fr' value_secondary=None color=None  

### `lateral_displacement_index`
**symbol**: $LDI$  
**label**: Lateral displacement index  
**unit**: m  
**description**: Lateral displacement index for liquefaction  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `lateral_displacement_index_inc`
**symbol**: $LDI_i$  
**label**: Lateral displacement index inc.  
**unit**: m  
**description**: Incremental lateral displacement index  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `lateral_displacement_index_ratio`
**symbol**: $LD_{ratio}$  
**label**: Lateral displacement index ratio  
**unit**: None  
**description**: Lateral displacement index ratio  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `lateral_displacement_index_sum`
**symbol**: $ΣLDI$  
**label**: Lateral displacement index sum  
**unit**: m  
**description**: Sum of lateral displacement indices  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `lateral_displacement_min_thickness`
**symbol**: $LD_{min\ thickness}$  
**label**: Lateral displacement min. thickness  
**unit**: m  
**description**: Minimum thickness for lateral displacement (Youd: 1.0 m, Zhang: 0.6 m)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `lateral_displacement_potential`
**symbol**: $LD_{potential}$  
**label**: Lateral displacement potential  
**unit**: None  
**description**: Applies when liquefiable group thickness >= min thickness  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `lateral_spread_displacement`
**symbol**: $LD$  
**label**: Lateral spread displacement  
**unit**: m  
**description**: Lateral spread displacement due to liquefaction  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `lateral_spread_displacement_as_scalar`
**symbol**: $LD_{scalar}$  
**label**: Lateral spread displacement as scalar  
**unit**: None  
**description**: If disabled, calculates lateral displacement for each depth  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `lateral_spread_displacement_inc`
**symbol**: $LD_i$  
**label**: Lateral spread displacement inc.  
**unit**: m  
**description**: Incremental lateral spread displacement  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `lateral_spread_displacement_sum`
**symbol**: $ΣLD$  
**label**: Lateral spread displacement sum  
**unit**: m  
**description**: Sum of lateral spread displacements  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `lateral_stiffness_ratio`
**symbol**: $α$  
**label**: Lateral stiffness ratio  
**unit**: None  
**description**: Lateral stiffness ratio (α=0: flexural beam,  α=650: shear beam)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `lateral_stress_increase_factor`
**symbol**: $K_m$  
**label**: Lateral stress increase factor  
**unit**: None  
**description**: Lateral stress increase factor for soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `latitude`
**symbol**: $\text{latitude}$  
**label**: Latitude  
**unit**: °  
**description**: Latitude in decimal degrees  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `liquefaction_building_settlement_index`
**symbol**: $LBS$  
**label**: Liquefaction building settlement index  
**unit**: None  
**description**: Liquefaction-induced building settlement index  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `liquefaction_likelihood`
**symbol**: $\text{liquefaction\_likelihood}$  
**label**: Liquefaction likelihood  
**unit**: None  
**description**: Likelihood of liquefaction occurrence  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Almost certain' value_secondary='Almost certain that it will liquefy' color='red'  
value='Very likely' value_secondary='Very likely' color='orange'  
value='Equally likely' value_secondary='Liquefaction/non-liquefaction is equally likely' color='yellow'  
value='Unlikely' value_secondary='Unlikely' color='#8fd400'  
value='Almost certain that not' value_secondary='Almost certain that it will not liquefy' color='yellowgreen'  

### `liquefaction_max_depth`
**symbol**: $LIQ_{max\ z}$  
**label**: Liquefaction max. depth  
**unit**: m  
**description**: Maximum depth for liquefaction analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `liquefaction_potential_index`
**symbol**: $LPI$  
**label**: Liquefaction potential index  
**unit**: None  
**description**: Liquefaction potential index for site  
**data_type**: `float`  
**corresponding_parameter_name**: `liquefaction_potential_index_label`  
    
#### data_bins

parameter_name: liquefaction_potential_index_label

left=0.0 right=5.0 value='Low' color='yellow'  
left=5.0 right=15.0 value='Moderate' color='orange'  
left=15.0 right=inf value='High' color='red'  

### `liquefaction_potential_index_inc`
**symbol**: $LPI_i$  
**label**: Liquefaction potential index inc.  
**unit**: None  
**description**: Incremental liquefaction potential index  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `liquefaction_potential_index_label`
**symbol**: $LPI_{label}$  
**label**: Liquefaction potential index label  
**unit**: None  
**description**: Label for liquefaction potential index  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Low' value_secondary=None color='yellow'  
value='Moderate' value_secondary=None color='orange'  
value='High' value_secondary=None color='red'  

### `liquefaction_potential_index_method`
**symbol**: $ΣLPI_{method}$  
**label**: Liquefaction potential index method  
**unit**: None  
**description**: Liquefaction potential index method  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='iwasaki1978' value_secondary=None color=None  
value='maurer2015' value_secondary=None color=None  

### `liquefaction_potential_index_sum`
**symbol**: $ΣLPI$  
**label**: Liquefaction potential index sum  
**unit**: None  
**description**: Sum of liquefaction potential indices  
**data_type**: `float`  
**corresponding_parameter_name**: `liquefaction_potential_index_sum_label`  
    
#### data_bins

parameter_name: liquefaction_potential_index_sum_label

left=0.0 right=5.0 value='Low' color='yellow'  
left=5.0 right=15.0 value='Moderate' color='orange'  
left=15.0 right=inf value='High' color='red'  

### `liquefaction_potential_index_sum_label`
**symbol**: $ΣLPI_{label}$  
**label**: Liquefaction potential index sum label  
**unit**: None  
**description**: Label for sum of liquefaction potential indices  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Low' value_secondary=None color='yellow'  
value='Moderate' value_secondary=None color='orange'  
value='High' value_secondary=None color='red'  

### `liquefaction_probability`
**symbol**: $PL_{liq}$  
**label**: Liquefaction probability  
**unit**: %  
**description**: Probability of liquefaction occurrence  
**data_type**: `float`  
**corresponding_parameter_name**: `liquefaction_likelihood`  
    
#### data_bins

parameter_name: liquefaction_likelihood

left=0.0 right=15.0 value='Almost certain that not' color='yellowgreen'  
left=15.0 right=35.0 value='Unlikely' color='#8fd400'  
left=35.0 right=65.0 value='Equally likely' color='yellow'  
left=65.0 right=85.0 value='Very likely' color='orange'  
left=85.0 right=100.0 value='Almost certain' color='red'  

### `liquefaction_safety_factor`
**symbol**: $FS_{liq}$  
**label**: Liquefaction safety factor  
**unit**: None  
**description**: Factor of safety against liquefaction triggering  
**data_type**: `float`  
**corresponding_parameter_name**: `liquefaction_likelihood`  
    
#### data_bins

parameter_name: liquefaction_likelihood

left=0.0 right=0.653 value='Almost certain' color='red'  
left=0.653 right=0.837 value='Very likely' color='orange'  
left=0.837 right=1.102 value='Equally likely' color='yellow'  
left=1.102 right=1.411 value='Unlikely' color='#8fd400'  
left=1.411 right=2.0 value='Almost certain that not' color='yellowgreen'  

### `liquefaction_settlement`
**symbol**: $S_{v-1D}$  
**label**: Liquefaction settlement  
**unit**: m  
**description**: Post-liquefaction vertical unidimensional settlement  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `liquefaction_settlement_inc`
**symbol**: $S_{v-1D\ i}$  
**label**: Liquefaction settlement inc.  
**unit**: m  
**description**: Incremental post-liquefaction vertical settlement  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `liquefaction_settlement_sum`
**symbol**: $ΣS_{v-1D}$  
**label**: Liquefaction settlement sum  
**unit**: m  
**description**: Sum of post-liquefaction vertical settlements  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `liquefaction_severity_number`
**symbol**: $LSN$  
**label**: Liquefaction severity number  
**unit**: None  
**description**: Liquefaction severity number for site  
**data_type**: `float`  
**corresponding_parameter_name**: `liquefaction_severity_number_label`  
    
#### data_bins

parameter_name: liquefaction_severity_number_label

left=0.0 right=10.0 value='Little to non' color='slateblue'  
left=10.0 right=20.0 value='Minor' color='blue'  
left=20.0 right=30.0 value='Moderate' color='gold'  
left=30.0 right=40.0 value='Moderate to severe' color='yellow'  
left=40.0 right=50.0 value='Mayor' color='orange'  
left=50.0 right=inf value='Severe damage' color='red'  

### `liquefaction_severity_number_inc`
**symbol**: $LSN_i$  
**label**: Liquefaction severity number inc.  
**unit**: None  
**description**: Incremental liquefaction severity number  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `liquefaction_severity_number_label`
**symbol**: $LSN_{label}$  
**label**: Liquefaction severity number label  
**unit**: None  
**description**: Label for liquefaction severity number  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Little to non' value_secondary=None color='slateblue'  
value='Minor' value_secondary=None color='blue'  
value='Moderate' value_secondary=None color='gold'  
value='Moderate to severe' value_secondary=None color='yellow'  
value='Mayor' value_secondary=None color='orange'  
value='Severe damage' value_secondary=None color='red'  

### `liquefaction_severity_number_max_depth`
**symbol**: $LSN_{max\ z}$  
**label**: Liquefaction severity number max. depth  
**unit**: m  
**description**: Maximum depth for liquefaction severity number analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `liquefaction_severity_number_sum`
**symbol**: $ΣLSN$  
**label**: Liquefaction severity number sum  
**unit**: None  
**description**: Sum of liquefaction severity numbers  
**data_type**: `float`  
**corresponding_parameter_name**: `liquefaction_severity_number_sum_label`  
    
#### data_bins

parameter_name: liquefaction_severity_number_sum_label

left=0.0 right=10.0 value='Little to non' color='slateblue'  
left=10.0 right=20.0 value='Minor' color='blue'  
left=20.0 right=30.0 value='Moderate' color='gold'  
left=30.0 right=40.0 value='Moderate to severe' color='yellow'  
left=40.0 right=50.0 value='Mayor' color='orange'  
left=50.0 right=inf value='Severe damage' color='red'  

### `liquefaction_severity_number_sum_label`
**symbol**: $ΣLSN_{label}$  
**label**: Liquefaction severity number sum label  
**unit**: None  
**description**: Label for sum of liquefaction severity numbers  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Little to non' value_secondary=None color='slateblue'  
value='Minor' value_secondary=None color='blue'  
value='Moderate' value_secondary=None color='gold'  
value='Moderate to severe' value_secondary=None color='yellow'  
value='Mayor' value_secondary=None color='orange'  
value='Severe damage' value_secondary=None color='red'  

### `liquefaction_shear_induced_building_settlement`
**symbol**: $D_s$  
**label**: Liquefaction shear-induced settlement  
**unit**: mm  
**description**: Shear-induced building settlement due to liquefaction  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `liquefaction_susceptibility`
**symbol**: $\text{liquefaction\_susceptibility}$  
**label**: Liquefaction susceptibility  
**unit**: None  
**description**: Susceptibility of soil to liquefaction  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Susceptible' value_secondary=None color='red'  
value='Mod. Susceptible' value_secondary=None color='orange'  
value='Not susceptible' value_secondary=None color='yellow'  

### `liquid_limit`
**symbol**: $LL$  
**label**: Liquid limit  
**unit**: %  
**description**: Liquid limit of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `liquid_limit_blows`
**symbol**: $N$  
**label**: Liquid limit blows  
**unit**: None  
**description**: Number of blows in liquid limit test  
**data_type**: `int`  
**corresponding_parameter_name**: `None`  
    

### `liquid_limit_method`
**symbol**: $LL_{method}$  
**label**: Liquid limit method  
**unit**: None  
**description**: Method used for liquid limit determination  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='single_point' value_secondary=None color=None  
value='multi_point' value_secondary=None color=None  

### `liquidity_index`
**symbol**: $LI$  
**label**: Liquidity index  
**unit**: None  
**description**: Liquidity index of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `liquidity_index_new`
**symbol**: $LIN$  
**label**: Liquidity index new  
**unit**: None  
**description**: Liquidity index per Koumoto and Houlsby (2001)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `location`
**symbol**: $\text{location}$  
**label**: Location  
**unit**: None  
**description**: Location of site  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `longitude`
**symbol**: $\text{longitude}$  
**label**: Longitude  
**unit**: °  
**description**: Longitude in decimal degrees  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `magnitude_scaling_factor`
**symbol**: $MSF$  
**label**: Magnitude scaling factor  
**unit**: None  
**description**: Magnitude scaling factor for liquefaction  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `magnitude_scaling_factor_max`
**symbol**: $MSF_{max}$  
**label**: Magnitude scaling factor max.  
**unit**: None  
**description**: Maximum magnitude scaling factor  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `mass_retained_sieve`
**symbol**: $W_n$  
**label**: Mass retained sieve  
**unit**: g  
**description**: Mass of soil retained on each sieve  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `material_description`
**symbol**: $\text{material\_description}$  
**label**: Material description  
**unit**: None  
**description**: Dilatometer material description  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Other' value_secondary='Other' color='#9e3300'  
value='Mud and/or Peat' value_secondary='MUD AND/OR PEAT' color='#9e3300'  
value='Mud' value_secondary='MUD' color='#9e3300'  
value='Clay' value_secondary='CLAY' color='green'  
value='Silty Clay' value_secondary='SILTY CLAY' color='green'  
value='Clayey Silt' value_secondary='CLAYEY SILT' color='orange'  
value='Silt' value_secondary='SILT' color='orange'  
value='Sandy Silt' value_secondary='SANDY SILT' color='orange'  
value='Silty Sand' value_secondary='SILTY SAND' color='grey'  
value='Sand' value_secondary='SAND' color='grey'  

### `material_index`
**symbol**: $I_D$  
**label**: Material index  
**unit**: None  
**description**: Dilatometer material index  
**data_type**: `float`  
**corresponding_parameter_name**: `material_description`  
    
#### data_bins

parameter_name: material_description

left=-2.0 right=-1.0 value='Mud and/or Peat' color='#9e3300'  
left=-1.0 right=0.1 value='Mud' color='#9e3300'  
left=0.1 right=0.33 value='Clay' color='green'  
left=0.33 right=0.6 value='Silty Clay' color='green'  
left=0.6 right=0.8 value='Clayey Silt' color='orange'  
left=0.8 right=1.2 value='Silt' color='orange'  
left=1.2 right=1.8 value='Sandy Silt' color='orange'  
left=1.8 right=3.3 value='Silty Sand' color='grey'  
left=3.3 right=10.0 value='Sand' color='grey'  

### `max_shear_strain`
**symbol**: $γ_{max}$  
**label**: Max. shear strain  
**unit**: %  
**description**: Maximum shear strain in soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `max_shear_strain_f_alpha_term`
**symbol**: $F_α$  
**label**: Max. shear strain Fα term  
**unit**: None  
**description**: Term for maximum shear strain calculation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `mean_corrected_cone_tip_resistance`
**symbol**: $q_{t\ mean}$  
**label**: Mean corrected cone tip resistance  
**unit**: MPa  
**description**: Corrected cone tip resistance averaged over footing influence depth  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `mean_effective_stress`
**symbol**: $σ_m'$  
**label**: Mean effective stress  
**unit**: kPa  
**description**: Mean effective stress in soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `membrane_compliance_correction`
**symbol**: $K_{mc}$  
**label**: Membrane compliance correction  
**unit**: None  
**description**: Correction factor for membrane compliance in DMT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `meniscus_correction`
**symbol**: $F_m$  
**label**: Meniscus correction  
**unit**: None  
**description**: Meniscus correction for hydrometer readings (always positive)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `method`
**symbol**: $\text{method}$  
**label**: Method  
**unit**: None  
**description**: Method (or standard) followed  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `mode_number`
**symbol**: $m$  
**label**: Mode number  
**unit**: None  
**description**: Number of modes in dynamic analysis  
**data_type**: `int`  
**corresponding_parameter_name**: `None`  
    

### `modified_soil_behavior_type`
**symbol**: $SBT_{n\ mod}$  
**label**: Modified soil behavior type  
**unit**: None  
**description**: Modified soil behavior type  
**data_type**: `str`  
**corresponding_parameter_name**: `modified_soil_behavior_type_label`  
    
#### discrete_data
is_categorical: True

value='0' value_secondary=None color=None  
value='1' value_secondary=None color=None  
value='2' value_secondary=None color=None  
value='3' value_secondary=None color=None  
value='4' value_secondary=None color=None  
value='5' value_secondary=None color=None  
value='6' value_secondary=None color=None  
value='7' value_secondary=None color=None  

### `modified_soil_behavior_type_index`
**symbol**: $I_B$  
**label**: Modified soil behaviour type index  
**unit**: None  
**description**: Modified soil behaviour type index  
**data_type**: `float`  
**corresponding_parameter_name**: `modified_soil_behavior_type_index_label`  
    
#### data_bins

parameter_name: modified_soil_behavior_type_index_label

left=10.0 right=22.0 value='Clay like' color='#29335e'  
left=22.0 right=32.0 value='Transitional' color='#8ad499'  
left=32.0 right=100.0 value='Sand like' color='#ff8a3b'  

### `modified_soil_behavior_type_index_label`
**symbol**: $I_{B\ label}$  
**label**: Modified soil behaviour type index label  
**unit**: None  
**description**: Label for modified soil behaviour type index  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Clay like' value_secondary=None color='#29335e'  
value='Transitional' value_secondary=None color='#8ad499'  
value='Sand like' value_secondary=None color='#ff8a3b'  

### `modified_soil_behavior_type_label`
**symbol**: $SBT_{n\ mod\ label}$  
**label**: Modified soil behavior type label  
**unit**: None  
**description**: Label for modified soil behavior type  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Other' value_secondary='Other' color='#FF0000'  
value='CSS' value_secondary='Clay-like - Contractive - Sensitive' color='#DD514A'  
value='CC' value_secondary='Clay-like - Contractive' color='#2E8EE2'  
value='CD' value_secondary='Clay-like - Dilative' color='#26207A'  
value='TC' value_secondary='Transitional - Contractive' color='#75E1AF'  
value='TD' value_secondary='Transitional - Dilative' color='#459184'  
value='SC' value_secondary='Sand-like - Contractive' color='#F09B49'  
value='SD' value_secondary='Sand-like - Dilative' color='#C0A264'  

### `moisture_mass`
**symbol**: $W_{moisture}$  
**label**: Moisture mass  
**unit**: g  
**description**: Mass of moisture in soil sample  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `moment_magnitude`
**symbol**: $M_w$  
**label**: Moment magnitude  
**unit**: None  
**description**: Seismic moment magnitude  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `moreno_alonso_plasticity_modification`
**symbol**: $\text{moreno\_alonso\_plasticity\_modification}$  
**label**: Moreno & Alonso plasticity modification  
**unit**: None  
**description**: Plasticity chart modification per Moreno & Alonso (2018)  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `moving_average_window_size`
**symbol**: $\text{moving\_average\_window\_size}$  
**label**: Moving average window size  
**unit**: None  
**description**: Window size for moving average applied to raw data  
**data_type**: `int`  
**corresponding_parameter_name**: `None`  
    

### `name`
**symbol**: $\text{name}$  
**label**: Name  
**unit**: None  
**description**: Name  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `natural_frequency`
**symbol**: $ω$  
**label**: Natural frequency  
**unit**: rad/s  
**description**: Undamped natural vibration frequency  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `nature_of_soil`
**symbol**: $\text{nature\_of\_soil}$  
**label**: Nature of soil  
**unit**: None  
**description**: Description of soil nature  
**data_type**: `str`  
**corresponding_parameter_name**: `nature_of_soil_label`  
    
#### discrete_data
is_categorical: True

value='0' value_secondary=None color=None  
value='1' value_secondary=None color=None  
value='2' value_secondary=None color=None  
value='3' value_secondary=None color=None  
value='4' value_secondary=None color=None  
value='5' value_secondary=None color=None  
value='6' value_secondary=None color=None  

### `nature_of_soil_label`
**symbol**: $\text{nature\_of\_soil\_label}$  
**label**: Nature of soil label  
**unit**: None  
**description**: Label for soil nature description  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Other' value_secondary=None color='#FF0000'  
value='Soft clay and mud' value_secondary=None color='#9e3300'  
value='Moderately compact clay' value_secondary=None color='green'  
value='Silt and loose sand' value_secondary=None color='darkorange'  
value='Compact to stiff clay and compact silt' value_secondary=None color='orange'  
value='Moderately compact sand and gravel' value_secondary=None color='darkgray'  
value='Compact to very compact sand and gravel' value_secondary=None color='gray'  

### `node_id`
**symbol**: $\text{node\_id}$  
**label**: Node id  
**unit**: None  
**description**: Identifier for node in analysis  
**data_type**: `int`  
**corresponding_parameter_name**: `None`  
    

### `non_normalized_soil_behavior_type_index`
**symbol**: $I_{SBT}$  
**label**: Non normalized soil behavior type index  
**unit**: None  
**description**: Non-normalized soil behavior type index  
**data_type**: `float`  
**corresponding_parameter_name**: `non_normalized_soil_behavior_type_index_label`  
    
#### data_bins

parameter_name: non_normalized_soil_behavior_type_index_label

left=1.0 right=1.31 value='Gravelly sand' color='#FF8A3B'  
left=1.31 right=2.05 value='Sands' color='#D19C00'  
left=2.05 right=2.6 value='Sand mixtures' color='#61d961'  
left=2.6 right=2.95 value='Silt mixtures' color='#2b802b'  
left=2.95 right=3.6 value='Clays' color='#213b69'  
left=3.6 right=4.0 value='Organic soils' color='#9e3300'  

### `non_normalized_soil_behavior_type_index_label`
**symbol**: $I_{SBT\ label}$  
**label**: Non normalized soil behavior type index label  
**unit**: None  
**description**: Label for non-normalized soil behavior type index  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Gravelly sand' value_secondary='Gravelly sand to dense sand' color='#FF8A3B'  
value='Sands' value_secondary='Sands & clean sand to silty\r\nsand' color='#D19C00'  
value='Sand mixtures' value_secondary='Sand mixtures & silty sand to\r\nsandy silt' color='#61d961'  
value='Silt mixtures' value_secondary='Silt mixtures & clayey silt to\r\nsilty clay' color='#2b802b'  
value='Clays' value_secondary='Clays & silty clay to clay' color='#213b69'  
value='Organic soils' value_secondary='Organic soils & clay' color='#9e3300'  

### `non_plastic`
**symbol**: $NP$  
**label**: Non-plastic  
**unit**: None  
**description**: Indicates non-plastic soil (PI=0)  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `normalized_blow_count`
**symbol**: $N_{160}$  
**label**: Normalized blow count  
**unit**: None  
**description**: N_60 corrected to 1 atm effective overburden stress  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    
#### data_bins

parameter_name: compactness

left=0.0 right=3.0 value='Very loose' color='gainsboro'  
left=3.0 right=8.0 value='Loose' color='lightgray'  
left=8.0 right=25.0 value='Medium' color='silver'  
left=25.0 right=42.0 value='Dense' color='darkgray'  
left=42.0 right=inf value='Very dense' color='gray'  

### `normalized_blow_count_fines_inc`
**symbol**: $ΔN_{160}$  
**label**: Normalized blow count fines inc.  
**unit**: None  
**description**: Fines content increment to normalized blow count  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `normalized_blow_count_fines_inc_sr`
**symbol**: $ΔN_{160-Sr}$  
**label**: Normalized blow count fines inc. (Sr)  
**unit**: None  
**description**: Fines content increment to normalized blow count for residual shear strength  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `normalized_blow_count_sr`
**symbol**: $N_{160-Sr}$  
**label**: Normalized blow count (Sr)  
**unit**: None  
**description**: N_60 corrected to 1 atm for residual shear strength  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `normalized_cone_resistance`
**symbol**: $Q_t$  
**label**: Normalized cone resistance  
**unit**: None  
**description**: Normalized cone resistance from CPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `normalized_cone_resistance_1atm`
**symbol**: $q_{c1N}$  
**label**: Normalized cone resistance at 1 atm  
**unit**: None  
**description**: Normalized cone resistance at 1 atm  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `normalized_cone_resistance_fines_inc`
**symbol**: $Δq_{c1N}$  
**label**: Normalized cone resistance fines inc.  
**unit**: None  
**description**: Fines content dependent increment to normalized cone resistance  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `normalized_cone_resistance_fines_inc_sr`
**symbol**: $Δq_{c1N-Sr}$  
**label**: Normalized cone resistance fines inc. (Sr)  
**unit**: None  
**description**: Fines content increment to normalized cone resistance for residual shear strength  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `normalized_excess_pore_pressure_ratio`
**symbol**: $r_u$  
**label**: Normalized excess pore water pressure ratio  
**unit**: None  
**description**: Normalized excess pore water pressure ratio  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `normalized_friction_ratio`
**symbol**: $F_r$  
**label**: Normalized friction ratio  
**unit**: %  
**description**: Normalized friction ratio from CPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `normalized_pore_pressure`
**symbol**: $U_2$  
**label**: Normalized pore pressure  
**unit**: None  
**description**: Normalized pore pressure from CPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `normalized_pore_pressure_ratio`
**symbol**: $B_q$  
**label**: Normalized pore pressure ratio  
**unit**: None  
**description**: Normalized pore pressure ratio from CPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `normalized_residual_shear_strength`
**symbol**: $S_{r\ ratio}$  
**label**: Normalized residual shear strength  
**unit**: None  
**description**: Post-liquefaction residual shear strength to effective stress ratio  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `normalized_soil_behavior_type`
**symbol**: $SBT_n$  
**label**: Normalized soil behavior type  
**unit**: None  
**description**: Normalized soil behavior type from CPT  
**data_type**: `str`  
**corresponding_parameter_name**: `normalized_soil_behavior_type_label`  
    
#### discrete_data
is_categorical: True

value='0' value_secondary=None color=None  
value='1' value_secondary=None color=None  
value='2' value_secondary=None color=None  
value='3' value_secondary=None color=None  
value='4' value_secondary=None color=None  
value='5' value_secondary=None color=None  
value='6' value_secondary=None color=None  
value='7' value_secondary=None color=None  
value='8' value_secondary=None color=None  
value='9' value_secondary=None color=None  

### `normalized_soil_behavior_type_label`
**symbol**: $SBT_{n\ label}$  
**label**: Normalized soil behavior type label  
**unit**: None  
**description**: Label for normalized soil behavior type  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Other' value_secondary='Other' color='#FF0000'  
value='Sensitive fine grained' value_secondary='Sensitive fine grained' color='#D42A1D'  
value='Organic soil' value_secondary='Organic material' color='#B46B40'  
value='Clay' value_secondary='Clay to silty clay' color='#4B5878'  
value='Clay & silty clay' value_secondary='Clayey silt to silty clay' color='#479085'  
value='Silty sand & sandy silt' value_secondary='Silty sand to sandy silt' color='#7EC4A0'  
value='Sand & silty sand' value_secondary='Clean sand to silty sand' color='#BFA364'  
value='Gravely sand & sand' value_secondary='Gravely sand to sand' color='#EB9D4A'  
value='Very stiff sand & clayey sand' value_secondary='Very stiff sand to clayey sand' color='#959595'  
value='Very stiff fine grained' value_secondary='Very stiff fine grained' color='#E6E6E6'  

### `northing`
**symbol**: $\text{northing}$  
**label**: Northing  
**unit**: m  
**description**: UTM WGS84 northing coordinate  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `number_of_standard_deviations`
**symbol**: $\text{number\_of\_standard\_deviations}$  
**label**: Number of standard deviations  
**unit**: None  
**description**: Number of standard deviations for statistical analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `overburden_correction`
**symbol**: $C_n$  
**label**: Overburden correction  
**unit**: None  
**description**: Overburden correction factor for SPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `overburden_correction_coefficient`
**symbol**: $C_σ$  
**label**: Overburden correction coefficient  
**unit**: None  
**description**: Coefficient for overburden correction  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `overburden_correction_crr`
**symbol**: $K_σ$  
**label**: Overburden correction for CRR  
**unit**: None  
**description**: Overburden correction factor for cyclic resistance ratio  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `overburden_correction_limit`
**symbol**: $C_{n\ lim}$  
**label**: Overburden correction limit  
**unit**: None  
**description**: Limit for overburden correction factor  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `overburden_correction_sr`
**symbol**: $C_{n-Sr}$  
**label**: Overburden correction (Sr)  
**unit**: None  
**description**: Overburden correction factor for residual shear strength  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `overburden_normalized_cone_resistance`
**symbol**: $q_{c1}$  
**label**: Overburden normalized cone resistance  
**unit**: None  
**description**: Overburden normalized cone resistance from CPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `overburden_stress_exponent`
**symbol**: $n$  
**label**: Overburden stress exponent  
**unit**: None  
**description**: Stress exponent for overburden correction  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `overburden_stress_exponent_sr`
**symbol**: $n_{Sr}$  
**label**: Overburden stress exponent (Sr)  
**unit**: None  
**description**: Stress exponent for overburden correction in residual shear strength  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `overconsolidation_ratio`
**symbol**: $OCR$  
**label**: Overconsolidation ratio  
**unit**: None  
**description**: Overconsolidation ratio of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `consolidation_state`  
    
#### data_bins

parameter_name: consolidation_state

left=0.0 right=1.0 value='UC' color='gainsboro'  
left=1.0 right=1.2 value='NC' color='lightgray'  
left=1.2 right=4.0 value='LOC' color='silver'  
left=4.0 right=10.0 value='MOC' color='darkgray'  
left=10.0 right=inf value='HOC' color='gray'  

### `overconsolidation_ratio_factor`
**symbol**: $k$  
**label**: Overconsolidation ratio factor  
**unit**: None  
**description**: Factor for overconsolidation ratio  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `particle_size`
**symbol**: $D$  
**label**: Particle size  
**unit**: mm  
**description**: Particle size from sieve or hydrometer analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `soil_fraction`  
    
#### data_bins

parameter_name: soil_fraction

left=75.0 right=100.0 value='Cobble' color=None  
left=19.0 right=75.0 value='Gravel (Coarse)' color=None  
left=4.75 right=19.0 value='Gravel (Fine)' color=None  
left=2.0 right=4.75 value='Sand (Coarse)' color=None  
left=0.425 right=2.0 value='Sand (Medium)' color=None  
left=0.075 right=0.425 value='Sand (Fine)' color=None  
left=0.005 right=0.075 value='Silt' color=None  
left=0.001 right=0.005 value='Clay' color=None  
left=0.0 right=0.001 value='Colloids' color=None  

### `peak_friction_angle`
**symbol**: $ϕ'$  
**label**: Peak friction angle  
**unit**: °  
**description**: Peak friction angle of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `peak_ground_acceleration`
**symbol**: $PGA$  
**label**: Peak ground acceleration  
**unit**: g  
**description**: Peak ground acceleration for seismic analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `peak_undrained_shear_strength_ratio`
**symbol**: $S_{u\ ratio\ peak}$  
**label**: Peak undrained shear strength ratio  
**unit**: None  
**description**: Peak undrained shear strength to effective stress ratio  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `penetration`
**symbol**: $\text{penetration}$  
**label**: Penetration  
**unit**: cm  
**description**: Penetration  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `penetration_rate`
**symbol**: $\text{penetration\_rate}$  
**label**: Penetration rate  
**unit**: mm/s  
**description**: Rate of penetration / push  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `percent_clay`
**symbol**: $\text{percent\_clay}$  
**label**: Percent clay  
**unit**: %  
**description**: Clay percentage for USDA classification  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `percent_coarse_gravel`
**symbol**: $\text{percent\_coarse\_gravel}$  
**label**: Percent coarse gravel  
**unit**: %  
**description**: Coarse gravel percentage (% retained on 3/4 " sieve)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `percent_coarse_sand`
**symbol**: $\text{percent\_coarse\_sand}$  
**label**: Percent coarse sand  
**unit**: %  
**description**: Coarse sand percentage (% passing No. 4 sieve, retained on No. 10)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `percent_fine_gravel`
**symbol**: $\text{percent\_fine\_gravel}$  
**label**: Percent fine gravel  
**unit**: %  
**description**: Fine gravel percentage (% passing 3/4 " sieve, retained on No. 4)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `percent_fine_sand`
**symbol**: $\text{percent\_fine\_sand}$  
**label**: Percent fine sand  
**unit**: %  
**description**: Fine sand percentage (% passing No. 40 sieve, retained on No. 200)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `percent_finer`
**symbol**: $\text{percent\_finer}$  
**label**: Percent finer  
**unit**: %  
**description**: Percentage of material finer than a given size  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `percent_finer_uncorrected`
**symbol**: $\text{percent\_finer\_uncorrected}$  
**label**: Percent finer uncorrected  
**unit**: %  
**description**: Uncorrected percentage finer from sieve analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `percent_gravel`
**symbol**: $\text{percent\_gravel}$  
**label**: Percent gravel  
**unit**: %  
**description**: Gravel percentage (% retained on No. 4 sieve)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `percent_medium_sand`
**symbol**: $\text{percent\_medium\_sand}$  
**label**: Percent medium sand  
**unit**: %  
**description**: Medium sand percentage (% passing No. 10 sieve, retained on No. 40)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `percent_passing_3in4`
**symbol**: $P_{3/4}$  
**label**: Percent passing 3/4"  
**unit**: %  
**description**: Percentage passing 3/4 " sieve  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `percent_passing_no10`
**symbol**: $P_{10}$  
**label**: Percent passing No. 10  
**unit**: %  
**description**: Percentage passing No. 10 sieve  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `percent_passing_no200`
**symbol**: $P_{200}$  
**label**: Percent passing No. 200  
**unit**: %  
**description**: Percentage passing No. 200 sieve  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `percent_passing_no4`
**symbol**: $P_{4}$  
**label**: Percent passing No. 4  
**unit**: %  
**description**: Percentage passing No. 4 sieve  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `percent_passing_no40`
**symbol**: $P_{40}$  
**label**: Percent passing No. 40  
**unit**: %  
**description**: Percentage passing No. 40 sieve  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `percent_sand`
**symbol**: $\text{percent\_sand}$  
**label**: Percent sand  
**unit**: %  
**description**: Sand percentage (% passing No. 4 sieve)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `percent_silt`
**symbol**: $\text{percent\_silt}$  
**label**: Percent silt  
**unit**: %  
**description**: Silt percentage for USDA classification  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `period`
**symbol**: $T$  
**label**: Period  
**unit**: s  
**description**: Vibration period of structure or soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `period_lengthening_ratio`
**symbol**: $T_{flexible}/T$  
**label**: Period lengthening ratio  
**unit**: None  
**description**: Ratio of flexible-base to rigid-base period  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `permeability`
**symbol**: $k$  
**label**: Permeability  
**unit**: m/s  
**description**: Soil permeability  
**data_type**: `float`  
**corresponding_parameter_name**: `relative_permeability`  
    
#### data_bins

parameter_name: relative_permeability

left=0.0 right=1e-09 value='Impermeable' color='gainsboro'  
left=1e-09 right=1e-07 value='Very low' color='lightgray'  
left=1e-07 right=1e-05 value='Low' color='silver'  
left=1e-05 right=0.001 value='Medium' color='darkgray'  
left=0.001 right=inf value='High' color='gray'  

### `pile_area_ratio`
**symbol**: $R_A$  
**label**: Pile area ratio  
**unit**: None  
**description**: Ratio of pile section area to total cross section area  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_count`
**symbol**: $n_{piles}$  
**label**: Pile count  
**unit**: None  
**description**: Number of piles  
**data_type**: `int`  
**corresponding_parameter_name**: `None`  
    

### `pile_critical_depth`
**symbol**: $\text{pile\_critical\_depth}$  
**label**: Pile critical depth  
**unit**: m  
**description**: Critical depth for pile analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_cross_swaying_rocking_stiffness`
**symbol**: $K_{hr}$  
**label**: Pile cross-swaying-rocking stiffness  
**unit**: kN/m or kN-m/rad  
**description**: Cross-swaying-rocking stiffness of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_diameter`
**symbol**: $D$  
**label**: Pile diameter  
**unit**: m  
**description**: Outside diameter of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_elasticity_modulus`
**symbol**: $E_p$  
**label**: Pile elasticity modulus  
**unit**: MPa  
**description**: Young’s modulus of pile material  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_embedment_length`
**symbol**: $L$  
**label**: Pile embedment length  
**unit**: m  
**description**: Embedment length of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_friction_coefficient`
**symbol**: $α$  
**label**: Pile friction coefficient  
**unit**: None  
**description**: Pile friction coefficient for shaft resistance  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_group_configuration`
**symbol**: $\text{pile\_group\_configuration}$  
**label**: Pile group configuration  
**unit**: None  
**description**: Configuration of pile group  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='2X2' value_secondary=None color=None  
value='3X3' value_secondary=None color=None  
value='4X4' value_secondary=None color=None  

### `pile_group_damping_ratio`
**symbol**: $β_G$  
**label**: Pile group damping ratio  
**unit**: None  
**description**: Damping ratio for pile group  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_group_efficiency_factor`
**symbol**: $EF$  
**label**: Pile group efficiency factor  
**unit**: None  
**description**: Efficiency factor for pile group  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_head_axial_load`
**symbol**: $P$  
**label**: Pile head axial load  
**unit**: kN  
**description**: Axial load at pile head  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_head_displacement`
**symbol**: $u$  
**label**: Pile head displacement  
**unit**: m  
**description**: Displacement at pile head  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_head_lateral_load`
**symbol**: $\text{pile\_head\_lateral\_load}$  
**label**: Pile head lateral load  
**unit**: kN  
**description**: Lateral load at pile head  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_head_moment`
**symbol**: $\text{pile\_head\_moment}$  
**label**: Pile head moment  
**unit**: kN-m  
**description**: Moment at pile head  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_head_rotation`
**symbol**: $θ$  
**label**: Pile head rotation  
**unit**: rad  
**description**: Rotation at pile head  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_horizontal_stiffness`
**symbol**: $k_{px}$  
**label**: Pile horizontal stiffness  
**unit**: MN/m  
**description**: Dynamic horizontal stiffness of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_influence_factor`
**symbol**: $I$  
**label**: Pile influence factor  
**unit**: None  
**description**: Influence factor for pile settlement  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_length_to_diameter_ratio`
**symbol**: $L/D$  
**label**: Pile length to diameter ratio  
**unit**: None  
**description**: Ratio of pile embedment length to diameter  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_length_to_soil_thickness_ratio`
**symbol**: $L/h$  
**label**: Pile length to soil thickness ratio  
**unit**: None  
**description**: Ratio of pile embedment length to soil layer depth  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_moment_of_inertia`
**symbol**: $I_p$  
**label**: Pile moment of inertia  
**unit**: m4  
**description**: Moment of inertia of equivalent solid pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_perimeter`
**symbol**: $P$  
**label**: Pile perimeter  
**unit**: m  
**description**: Perimeter of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_rocking_stiffness`
**symbol**: $K_{rr}$  
**label**: Pile rocking stiffness  
**unit**: kN-m/rad  
**description**: Rocking stiffness of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_settlement`
**symbol**: $S$  
**label**: Pile settlement  
**unit**: cm  
**description**: Settlement of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_settlement_correction_bearing`
**symbol**: $R_b$  
**label**: Pile settlement correction for bearing  
**unit**: None  
**description**: Correction factor for bearing stratum  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_settlement_correction_compressibility`
**symbol**: $R_K$  
**label**: Pile settlement correction for compressibility  
**unit**: None  
**description**: Correction factor for pile compressibility  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_settlement_correction_depth`
**symbol**: $R_h$  
**label**: Pile settlement correction for depth  
**unit**: None  
**description**: Correction factor for pile layer depth  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_settlement_correction_poisson`
**symbol**: $R_v$  
**label**: Pile settlement correction for Poisson’s ratio  
**unit**: None  
**description**: Correction factor for Poisson’s ratio  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_shaft_resistance`
**symbol**: $Q_s$  
**label**: Pile shaft resistance  
**unit**: kN  
**description**: Shaft resistance of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_shaft_resistance_inc`
**symbol**: $Q_{s\ i}$  
**label**: Pile shaft resistance inc.  
**unit**: kN  
**description**: Incremental shaft resistance of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_shape`
**symbol**: $\text{pile\_shape}$  
**label**: Pile shape  
**unit**: None  
**description**: Shape of pile  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='circle' value_secondary=None color=None  
value='square' value_secondary=None color=None  

### `pile_side_surface_area`
**symbol**: $A_s$  
**label**: Pile side surface area  
**unit**: m2  
**description**: Side surface area of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_stiffness`
**symbol**: $k_p$  
**label**: Pile stiffness  
**unit**: MN/m or MN-m/rad  
**description**: Dynamic stiffness of single pile for mode j (translation or rotation)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_stiffness_factor`
**symbol**: $K$  
**label**: Pile stiffness factor  
**unit**: None  
**description**: Stiffness factor for pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_stiffness_in_group`
**symbol**: $k_{pG}$  
**label**: Pile stiffness in group  
**unit**: MN/m or MN-m/rad  
**description**: Dynamic stiffness of pile in group for mode j  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_swaying_stiffness`
**symbol**: $K_{hh}$  
**label**: Pile swaying stiffness  
**unit**: kN/m  
**description**: Swaying stiffness of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_tip_area`
**symbol**: $A_p$  
**label**: Pile tip area  
**unit**: m2  
**description**: Tip area of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_tip_resistance`
**symbol**: $Q_b$  
**label**: Pile tip resistance  
**unit**: kN  
**description**: Tip resistance of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_tip_resistance_coefficient`
**symbol**: $C_t$  
**label**: Pile tip resistance coefficient  
**unit**: None  
**description**: Coefficient for pile tip resistance  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_tip_resistance_factor`
**symbol**: $k_c$  
**label**: Pile tip resistance factor  
**unit**: None  
**description**: LCPC method bearing capacity factor for pile tip  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_toe_transition`
**symbol**: $\text{pile\_toe\_transition}$  
**label**: Pile toe transition  
**unit**: None  
**description**: Transition type at pile toe  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='dense_to_weak' value_secondary=None color=None  
value='weak_to_dense' value_secondary=None color=None  

### `pile_type_category`
**symbol**: $\text{pile\_type\_category}$  
**label**: Pile type category  
**unit**: None  
**description**: Category of pile type  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='IA' value_secondary=None color=None  
value='IB' value_secondary=None color=None  
value='IIA' value_secondary=None color=None  
value='IIB' value_secondary=None color=None  

### `pile_ultimate_resistance`
**symbol**: $Q_{ult}$  
**label**: Pile ultimate resistance  
**unit**: kN  
**description**: Ultimate resistance of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_unit_tip_resistance`
**symbol**: $q_p$  
**label**: Pile unit tip resistance  
**unit**: MPa  
**description**: Unit tip resistance of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_unit_weight`
**symbol**: $γ_p$  
**label**: Pile unit weight  
**unit**: kN/m3  
**description**: Unit weight of pile material  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_vertical_stiffness`
**symbol**: $k_{pz}$  
**label**: Pile vertical stiffness  
**unit**: MN/m  
**description**: Dynamic vertical stiffness of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pile_wall_thickness`
**symbol**: $t$  
**label**: Pile wall thickness  
**unit**: m  
**description**: Wall thickness of pile  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `plastic_limit`
**symbol**: $PL$  
**label**: Plastic limit  
**unit**: %  
**description**: Plastic limit of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `plasticity_index`
**symbol**: $PI$  
**label**: Plasticity index  
**unit**: %  
**description**: Plasticity index of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `plasticity_index_liquid_limit_ratio`
**symbol**: $PI\ /\ LL$  
**label**: Plasticity index to liquid limit ratio  
**unit**: None  
**description**: Ratio of plasticity index to liquid limit  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `poisson_adjustment_factor`
**symbol**: $ψ$  
**label**: Poisson’s adjustment factor  
**unit**: None  
**description**: Adjustment factor for Poisson’s ratio  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `poisson_ratio`
**symbol**: $ν$  
**label**: Poisson’s ratio  
**unit**: None  
**description**: Poisson’s ratio of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pore_pressure`
**symbol**: $u$  
**label**: Pore pressure  
**unit**: kPa  
**description**: Pore pressure in soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pore_pressure_index`
**symbol**: $U_D$  
**label**: Pore pressure index  
**unit**: None  
**description**: Pore pressure index from DMT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `pore_water_pressure`
**symbol**: $u_0$  
**label**: Pore water pressure  
**unit**: kPa  
**description**: Pore water pressure in soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `porosity`
**symbol**: $n$  
**label**: Porosity  
**unit**: None  
**description**: Fraction of soil volume taken up by pore space  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `post_liquefaction_residual_shear_strength`
**symbol**: $S_r$  
**label**: Post-liquefaction residual shear strength  
**unit**: kPa  
**description**: Post-liquefaction residual shear strength  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `preconsolidation_stress`
**symbol**: $σ_p'$  
**label**: Preconsolidation stress  
**unit**: kPa  
**description**: Preconsolidation stress of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `primary_consolidation_time`
**symbol**: $t_p$  
**label**: Primary consolidation time  
**unit**: month  
**description**: Time for primary consolidation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `project_id`
**symbol**: $\text{project\_id}$  
**label**: Project ID  
**unit**: None  
**description**: Identifier for project  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `project_name`
**symbol**: $\text{project\_name}$  
**label**: Project name  
**unit**: None  
**description**: Project name  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `pseudo_spectral_acceleration`
**symbol**: $PSa$  
**label**: Pseudo-spectral acceleration  
**unit**: g  
**description**: Pseudo-spectral acceleration for seismic analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `punching_shear_coefficient`
**symbol**: $K_s$  
**label**: Punching shear coefficient  
**unit**: None  
**description**: Punching shear coefficient for foundation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `radiation_damping_ratio`
**symbol**: $β$  
**label**: Radiation damping ratio  
**unit**: None  
**description**: Radiation damping ratio for soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `raw_a_reading`
**symbol**: $A$  
**label**: Raw A reading  
**unit**: kPa  
**description**: First dilatometer reading  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `raw_b_reading`
**symbol**: $B$  
**label**: Raw B reading  
**unit**: kPa  
**description**: Second dilatometer reading  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `raw_c_reading`
**symbol**: $C$  
**label**: Raw C reading  
**unit**: kPa  
**description**: Third dilatometer reading  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `recompression_index`
**symbol**: $C_r$  
**label**: Recompression index  
**unit**: None  
**description**: Recompression (swelling) index of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `recompression_ratio`
**symbol**: $RR$  
**label**: Recompression ratio  
**unit**: None  
**description**: Recompression ratio of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `recovery`
**symbol**: $\text{recovery}$  
**label**: Recovery  
**unit**: %  
**description**: Ratio of recovered sample length to sampled interval  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `relative_density`
**symbol**: $D_r$  
**label**: Relative density  
**unit**: %  
**description**: Relative density of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    
#### data_bins

parameter_name: compactness

left=0.0 right=15.0 value='Very loose' color='gainsboro'  
left=15.0 right=35.0 value='Loose' color='lightgray'  
left=35.0 right=65.0 value='Medium' color='silver'  
left=65.0 right=85.0 value='Dense' color='darkgray'  
left=85.0 right=inf value='Very dense' color='gray'  

### `relative_density_constant`
**symbol**: $k_{D_r}$  
**label**: Relative density constant  
**unit**: None  
**description**: Constant for relative density calculation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `relative_permeability`
**symbol**: $k_{relative}$  
**label**: Relative permeability  
**unit**: None  
**description**: Relative permeability of soil  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Impermeable' value_secondary='Clay' color='gainsboro'  
value='Very low' value_secondary='Silt, silty clay' color='lightgray'  
value='Low' value_secondary='Sand, dirty sand, silty sand' color='silver'  
value='Medium' value_secondary='Sandy gravel, clean sand, fine sand' color='darkgray'  
value='High' value_secondary='Gravel' color='gray'  

### `remarks`
**symbol**: $\text{remarks}$  
**label**: Remarks  
**unit**: None  
**description**: Additional remarks or notes  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `remolded_undrained_shear_strength`
**symbol**: $S_{ur}$  
**label**: Remolded undrained shear strength  
**unit**: kPa  
**description**: Remolded undrained shear strength of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `remolded_undrained_shear_strength_ratio`
**symbol**: $S_{ur\ ratio}$  
**label**: Remolded undrained shear strength ratio  
**unit**: None  
**description**: Remolded undrained shear strength to effective stress ratio  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `remove_loose_sand_criteria`
**symbol**: $\text{remove\_loose\_sand\_criteria}$  
**label**: Remove loose sand criteria  
**unit**: None  
**description**: Sets K_c = 1.00 for I_c between 1.64 and 2.36 and F_r < 0.5  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `response_embedment_modification`
**symbol**: $RRS_e$  
**label**: Response embedment modification  
**unit**: None  
**description**: Response spectrum modification for embedment  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `rig_model`
**symbol**: $\text{rig\_model}$  
**label**: Rig model  
**unit**: None  
**description**: Boring rig model  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `rod_length`
**symbol**: $\text{rod\_length}$  
**label**: Rod length  
**unit**: m  
**description**: Total length of SPT rods  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `rod_length_correction`
**symbol**: $C_R$  
**label**: Rod length correction  
**unit**: None  
**description**: SPT correction factor for rod length  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `sample_diameter`
**symbol**: $D$  
**label**: Sample diameter  
**unit**: mm  
**description**: Sample diameter  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `sample_id`
**symbol**: $ID$  
**label**: Sample ID  
**unit**: None  
**description**: Identifier for soil sample  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `sample_name`
**symbol**: $ID$  
**label**: Sample name  
**unit**: None  
**description**: Sample name  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `sampler_correction`
**symbol**: $C_S$  
**label**: Sampler correction  
**unit**: None  
**description**: SPT correction factor for sampling method  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `sampler_type`
**symbol**: $\text{sampler\_type}$  
**label**: Sampler type  
**unit**: None  
**description**: Type of sampler used  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='GB' value_secondary=None color=None  
value='SPT' value_secondary=None color=None  
value='ST' value_secondary=None color=None  
value='RC' value_secondary=None color=None  
value='SS' value_secondary=None color=None  

### `sand_fineness`
**symbol**: $\text{sand\_fineness}$  
**label**: Sand fineness  
**unit**: None  
**description**: Category of sand fineness  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='fine' value_secondary=None color=None  
value='medium' value_secondary=None color=None  
value='coarse' value_secondary=None color=None  

### `saturation_ratio`
**symbol**: $S_r$  
**label**: Saturation ratio  
**unit**: None  
**description**: Ratio of water volume to total void space  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `second_interval_blow_count`
**symbol**: $N_{second}$  
**label**: Second interval blow count  
**unit**: None  
**description**: Second interval blow count in SPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `sensitivity`
**symbol**: $S_t$  
**label**: Sensitivity  
**unit**: None  
**description**: Sensitivity of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `sensitivity_constant`
**symbol**: $N_S$  
**label**: Sensitivity constant  
**unit**: None  
**description**: Constant for sensitivity calculation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shallow_velocity_extrapolation_method`
**symbol**: $\text{shallow\_velocity\_extrapolation\_method}$  
**label**: Shallow velocity extrapolation method  
**unit**: None  
**description**: Method for shallow velocity extrapolation  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='Boore04' value_secondary=None color=None  

### `shansep_method_m`
**symbol**: $m$  
**label**: SHANSEP method m  
**unit**: None  
**description**: SHANSEP method m parameter  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shansep_method_s`
**symbol**: $s$  
**label**: SHANSEP method s  
**unit**: None  
**description**: SHANSEP method s parameter  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shape_factor_cohesion`
**symbol**: $s_c$  
**label**: Shape factor for cohesion  
**unit**: None  
**description**: Shape factor for cohesion in bearing capacity  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shape_factor_surcharge`
**symbol**: $s_q$  
**label**: Shape factor for surcharge  
**unit**: None  
**description**: Shape factor for surcharge in bearing capacity  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shape_factor_surcharge_bottom_layer`
**symbol**: $s_{q\ bottom}$  
**label**: Shape factor for surcharge bottom layer  
**unit**: None  
**description**: Shape factor for surcharge of soil beneath foundation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shape_factor_unit_weight`
**symbol**: $s_γ$  
**label**: Shape factor for unit weight  
**unit**: None  
**description**: Shape factor for unit weight in bearing capacity  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shape_parameter`
**symbol**: $μ$  
**label**: Shape parameter  
**unit**: None  
**description**: Shape parameter analogous to a wavenumber  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shear_modulus`
**symbol**: $G$  
**label**: Shear modulus  
**unit**: MPa  
**description**: Shear modulus of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shear_modulus_ratio`
**symbol**: $G_r$  
**label**: Shear modulus ratio  
**unit**: None  
**description**: Ratio of stone column to soil shear modulus  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shear_modulus_reduction_factor`
**symbol**: $G/G_0$  
**label**: Shear modulus reduction factor  
**unit**: None  
**description**: Shear modulus reduction factor for soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shear_percent_contribution`
**symbol**: $PC_{shear}$  
**label**: Shear percent contribution  
**unit**: None  
**description**: Percent contribution from shear (Green et al., 2008)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shear_strain_limit`
**symbol**: $γ_{lim}$  
**label**: Shear strain limit  
**unit**: %  
**description**: Limiting value of shear strain  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shear_strength`
**symbol**: $τ$  
**label**: Shear strength  
**unit**: kPa  
**description**: Shear strength of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shear_stress`
**symbol**: $τ$  
**label**: Shear stress  
**unit**: kPa  
**description**: Shear stress in soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shear_stress_reduction_coefficient`
**symbol**: $r_d$  
**label**: Shear stress reduction coefﬁcient  
**unit**: None  
**description**: Shear stress reduction coefficient for liquefaction  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shear_stress_reduction_factor`
**symbol**: $K_G$  
**label**: Shear stress reduction factor  
**unit**: None  
**description**: Shear stress reduction factor for stone columns  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shear_velocity`
**symbol**: $V_s$  
**label**: Shear velocity  
**unit**: m/s  
**description**: Shear wave velocity of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `shear_velocity_factor`
**symbol**: $α_{vs}$  
**label**: Shear velocity factor  
**unit**: None  
**description**: Shear wave velocity factor  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `sieve_number`
**symbol**: $\text{sieve\_number}$  
**label**: Sieve number  
**unit**: None  
**description**: Sieve number for particle size analysis (SI units)  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='24 "' value_secondary=600.0 color=None  
value='12 "' value_secondary=300.0 color=None  
value='6 "' value_secondary=150.0 color=None  
value='3 "' value_secondary=75.0 color=None  
value='2 ½ "' value_secondary=63.0 color=None  
value='2 "' value_secondary=50.0 color=None  
value='1 ½ "' value_secondary=38.1 color=None  
value='1 "' value_secondary=25.0 color=None  
value='3/4 "' value_secondary=19.0 color=None  
value='1/2 "' value_secondary=12.5 color=None  
value='3/8 "' value_secondary=9.5 color=None  
value='No. 4' value_secondary=4.75 color=None  
value='No. 6' value_secondary=3.35 color=None  
value='No. 8' value_secondary=2.36 color=None  
value='No. 10' value_secondary=2.0 color=None  
value='No. 16' value_secondary=1.18 color=None  
value='No. 20' value_secondary=0.85 color=None  
value='No. 30' value_secondary=0.6 color=None  
value='No. 40' value_secondary=0.425 color=None  
value='No. 50' value_secondary=0.3 color=None  
value='No. 60' value_secondary=0.25 color=None  
value='No. 70' value_secondary=0.212 color=None  
value='No. 80' value_secondary=0.18 color=None  
value='No. 100' value_secondary=0.15 color=None  
value='No. 120' value_secondary=0.125 color=None  
value='No. 140' value_secondary=0.106 color=None  
value='No. 170' value_secondary=0.088 color=None  
value='No. 200' value_secondary=0.075 color=None  

### `silt_clay_particle_size_breakpoint`
**symbol**: $D_{silt\ clay}$  
**label**: Silt/clay particle size breakpoint  
**unit**: mm  
**description**: Breakpoint for silt and clay particle size  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `site_class`
**symbol**: $\text{site\_class}$  
**label**: Site class  
**unit**: None  
**description**: Seismic site class  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='F' value_secondary=None color=None  
value='E' value_secondary=None color=None  
value='D' value_secondary=None color=None  
value='C' value_secondary=None color=None  
value='B' value_secondary=None color=None  
value='A' value_secondary=None color=None  

### `site_class_average`
**symbol**: $\text{site\_class\_average}$  
**label**: Site class average  
**unit**: None  
**description**: Special average for site class determination  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `site_class_e_thickness`
**symbol**: $\text{site\_class\_e\_thickness}$  
**label**: Site class E thickness  
**unit**: m  
**description**: Thickness of Clay [PI (%) > 20 & wc (%) ≥ 40 & Su (kPa) < 24]  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `site_class_f2_thickness`
**symbol**: $\text{site\_class\_f2\_thickness}$  
**label**: Site class F2 thickness  
**unit**: m  
**description**: Thickness of Peat and/or highly organic clays  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `site_class_f3_thickness`
**symbol**: $\text{site\_class\_f3\_thickness}$  
**label**: Site class F3 thickness  
**unit**: m  
**description**: Thickness of Very high plasticity clays [PI (%) > 75]  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `site_class_f4_thickness`
**symbol**: $\text{site\_class\_f4\_thickness}$  
**label**: Site class F4 thickness  
**unit**: m  
**description**: Thickness of Very thick, soft/medium stiff clays [Su (kPa) < 50]  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `site_class_label`
**symbol**: $\text{site\_class\_label}$  
**label**: Site class label  
**unit**: None  
**description**: Label for seismic site class  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Soil requiring site-specific evaluations' value_secondary=None color=None  
value='Soft soil' value_secondary=None color=None  
value='Stiff soil' value_secondary=None color=None  
value='Very dense soil and soft rock' value_secondary=None color=None  
value='Rock' value_secondary=None color=None  
value='Hard rock' value_secondary=None color=None  

### `site_ground_condition`
**symbol**: $\text{site\_ground\_condition}$  
**label**: Site ground condition  
**unit**: None  
**description**: Description of site ground condition  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='level_ground' value_secondary=None color=None  
value='sloping_ground' value_secondary=None color=None  
value='free_face' value_secondary=None color=None  

### `site_period`
**symbol**: $T_n$  
**label**: Site period  
**unit**: s  
**description**: Natural period of site  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `site_to_seismic_source_distance`
**symbol**: $R$  
**label**: Site-to-seismic-source distance  
**unit**: km  
**description**: Horizontal distance to nearest seismic energy source  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `sleeve_friction`
**symbol**: $f_s$  
**label**: Sleeve friction  
**unit**: kPa  
**description**: Sleeve friction from CPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `small_strain_shear_modulus`
**symbol**: $G_o$  
**label**: Small strain shear modulus  
**unit**: MPa  
**description**: Small strain shear modulus of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `soil_behavior_type`
**symbol**: $SBT$  
**label**: Soil behavior type  
**unit**: None  
**description**: Soil behavior type from CPT  
**data_type**: `str`  
**corresponding_parameter_name**: `soil_behavior_type_label`  
    
#### discrete_data
is_categorical: True

value='0' value_secondary=None color=None  
value='1' value_secondary=None color=None  
value='2' value_secondary=None color=None  
value='3' value_secondary=None color=None  
value='4' value_secondary=None color=None  
value='5' value_secondary=None color=None  
value='6' value_secondary=None color=None  
value='7' value_secondary=None color=None  
value='8' value_secondary=None color=None  
value='9' value_secondary=None color=None  

### `soil_behavior_type_index`
**symbol**: $I_c$  
**label**: Soil behavior type index  
**unit**: None  
**description**: Normalized soil behavior type index from CPT  
**data_type**: `float`  
**corresponding_parameter_name**: `soil_behavior_type_index_label`  
    
#### data_bins

parameter_name: soil_behavior_type_index_label

left=1.0 right=1.31 value='Gravelly sand' color='#FF8A3B'  
left=1.31 right=2.05 value='Sands' color='#D19C00'  
left=2.05 right=2.6 value='Sand mixtures' color='#61d961'  
left=2.6 right=2.95 value='Silt mixtures' color='#2b802b'  
left=2.95 right=3.6 value='Clays' color='#213b69'  
left=3.6 right=4.0 value='Organic soils' color='#9e3300'  

### `soil_behavior_type_index_cutoff`
**symbol**: $I_{c\ cutoff}$  
**label**: Soil behavior type index cutoff  
**unit**: None  
**description**: Cutoff for fine soil criteria and transition layer detection  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `soil_behavior_type_index_label`
**symbol**: $I_{c\ label}$  
**label**: Soil behavior type index label  
**unit**: None  
**description**: Label for soil behavior type index  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Gravelly sand' value_secondary='Gravelly sand to dense sand' color='#FF8A3B'  
value='Sands' value_secondary='Sands & clean sand to silty\r\nsand' color='#D19C00'  
value='Sand mixtures' value_secondary='Sand mixtures & silty sand to\r\nsandy silt' color='#61d961'  
value='Silt mixtures' value_secondary='Silt mixtures & clayey silt to\r\nsilty clay' color='#2b802b'  
value='Clays' value_secondary='Clays & silty clay to clay' color='#213b69'  
value='Organic soils' value_secondary='Organic soils & clay' color='#9e3300'  

### `soil_behavior_type_label`
**symbol**: $SBT_{label}$  
**label**: Soil behavior type label  
**unit**: None  
**description**: Label for soil behavior type  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Other' value_secondary='Other' color='#FF0000'  
value='Sensitive fine grained' value_secondary='Sensitive fine grained' color='#D42A1D'  
value='Organic soil' value_secondary='Organic material' color='#B46B40'  
value='Clay' value_secondary='Clay to silty clay' color='#4B5878'  
value='Clay & silty clay' value_secondary='Clayey silt to silty clay' color='#479085'  
value='Silty sand & sandy silt' value_secondary='Silty sand to sandy silt' color='#7EC4A0'  
value='Sand & silty sand' value_secondary='Clean sand to silty sand' color='#BFA364'  
value='Gravely sand & sand' value_secondary='Gravely sand to sand' color='#EB9D4A'  
value='Very stiff sand & clayey sand' value_secondary='Very stiff sand to clayey sand' color='#959595'  
value='Very stiff fine grained' value_secondary='Very stiff fine grained' color='#E6E6E6'  

### `soil_behavior_type_schneider`
**symbol**: $SBT_{Schneider}$  
**label**: Soil behavior type Schneider  
**unit**: None  
**description**: Soil behavior type per Schneider classification  
**data_type**: `str`  
**corresponding_parameter_name**: `soil_behavior_type_schneider_label`  
    
#### discrete_data
is_categorical: True

value='0' value_secondary=None color=None  
value='1a' value_secondary=None color=None  
value='1b' value_secondary=None color=None  
value='1c' value_secondary=None color=None  
value='2' value_secondary=None color=None  
value='3' value_secondary=None color=None  

### `soil_behavior_type_schneider_label`
**symbol**: $SBT_{Schneider\ label}$  
**label**: Soil behavior type Schneider label  
**unit**: None  
**description**: Label for Schneider soil behavior type  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Other' value_secondary='Other' color='#FF0000'  
value='Clay and/or Silt' value_secondary="SILTS and 'Low Ir' CLAYS" color='#7EC4A0'  
value='Clay' value_secondary='CLAYS' color='#4B5878'  
value='Sensitive clay' value_secondary='Sensitive CLAYS' color='#7d8599'  
value='Sand' value_secondary='Essentially drained SANDS' color='#BFA364'  
value='Transitional' value_secondary='Transitional soils' color='#8ad499'  

### `soil_classification_index`
**symbol**: $ΔQ$  
**label**: Soil classification index  
**unit**: None  
**description**: Soil classification index per Saye  
**data_type**: `float`  
**corresponding_parameter_name**: `soil_classification_index_uscs_symbol`  
    
#### data_bins

parameter_name: soil_classification_index_label

left=0.0 right=15.0 value='6' color='#9e3300'  
left=15.0 right=19.0 value='5' color='#213b69'  
left=19.0 right=31.0 value='4' color='#42577d'  
left=31.0 right=70.0 value='3' color='#61d961'  
left=70.0 right=90.0 value='2' color='#D19C00'  
left=90.0 right=inf value='1' color='#FF8A3B'  
parameter_name: soil_classification_index_uscs_symbol

left=0.0 right=15.0 value='OL,OH,Pt' color='#9e3300'  
left=15.0 right=19.0 value='MH,CH' color='#213b69'  
left=19.0 right=31.0 value='ML,CL' color='#42577d'  
left=31.0 right=70.0 value='SM,SC,GM,GC' color='#61d961'  
left=70.0 right=90.0 value='SP-SM,SP-SC' color='#D19C00'  
left=90.0 right=inf value='SP,SW' color='#FF8A3B'  

### `soil_classification_index_label`
**symbol**: $ΔQ_{label}$  
**label**: Soil classification index label  
**unit**: None  
**description**: Label for soil classification index  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Other' value_secondary=None color='black'  
value='6' value_secondary=None color='#9e3300'  
value='5' value_secondary=None color='#213b69'  
value='4' value_secondary=None color='#42577d'  
value='3' value_secondary=None color='#61d961'  
value='2' value_secondary=None color='#D19C00'  
value='1' value_secondary=None color='#FF8A3B'  

### `soil_classification_index_uscs_symbol`
**symbol**: $\text{soil\_classification\_index\_uscs\_symbol}$  
**label**: Soil classification index USCS symbol  
**unit**: None  
**description**: USCS symbol for soil classification index  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Other' value_secondary=None color='black'  
value='OL,OH,Pt' value_secondary=None color='#9e3300'  
value='MH,CH' value_secondary=None color='#213b69'  
value='ML,CL' value_secondary=None color='#42577d'  
value='SM,SC,GM,GC' value_secondary=None color='#61d961'  
value='SP-SM,SP-SC' value_secondary=None color='#D19C00'  
value='SP,SW' value_secondary=None color='#FF8A3B'  

### `soil_damping_ratio`
**symbol**: $β_s$  
**label**: Soil damping ratio  
**unit**: None  
**description**: Hysteretic damping ratio of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `soil_fraction`
**symbol**: $\text{soil\_fraction}$  
**label**: Soil fraction  
**unit**: None  
**description**: Soil fraction based on ASTM particle size ranges  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Colloids' value_secondary=None color=None  
value='Clay' value_secondary=None color=None  
value='Silt' value_secondary=None color=None  
value='Sand (Fine)' value_secondary=None color=None  
value='Sand (Medium)' value_secondary=None color=None  
value='Sand (Coarse)' value_secondary=None color=None  
value='Gravel (Fine)' value_secondary=None color=None  
value='Gravel (Coarse)' value_secondary=None color=None  
value='Cobble' value_secondary=None color=None  

### `soil_origin`
**symbol**: $\text{soil\_origin}$  
**label**: Soil origin  
**unit**: None  
**description**: Origin of soil  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='alluvial' value_secondary=None color=None  
value='diluvial' value_secondary=None color=None  

### `soil_profile_shape`
**symbol**: $\text{soil\_profile\_shape}$  
**label**: Soil profile shape  
**unit**: None  
**description**: Shape of soil profile  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `soil_thickness`
**symbol**: $h$  
**label**: Soil thickness  
**unit**: m  
**description**: Total thickness of soil layers above rigid layer  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `soil_transition`
**symbol**: $\text{soil\_transition}$  
**label**: Soil transition  
**unit**: None  
**description**: Flag for soil type transition  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `soil_transition_detection`
**symbol**: $\text{soil\_transition\_detection}$  
**label**: Soil transition detection  
**unit**: None  
**description**: Detection of soil type transition  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `soil_transition_max_index`
**symbol**: $I_{c\ max}$  
**label**: Soil transition max. index  
**unit**: None  
**description**: Maximum I_c for soil type transition  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `soil_transition_min_index`
**symbol**: $I_{c\ min}$  
**label**: Soil transition min. index  
**unit**: None  
**description**: Minimum I_c for soil type transition  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `soil_transition_min_points`
**symbol**: $I_{c\ min\ points}$  
**label**: Soil transition min. points  
**unit**: None  
**description**: Minimum points for soil transition detection  
**data_type**: `int`  
**corresponding_parameter_name**: `None`  
    

### `soil_transition_min_rate_of_change`
**symbol**: $\text{soil\_transition\_min\_rate\_of\_change}$  
**label**: Soil transition min. rate of change  
**unit**: None  
**description**: Minimum rate of change for soil transition  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `soil_type`
**symbol**: $\text{soil\_type}$  
**label**: Soil type  
**unit**: None  
**description**: Primary soil type description  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Other' value_secondary=None color='#FF0000'  
value='Rock' value_secondary=None color='#FF0000'  
value='Weathered Rock' value_secondary=None color='#FF0000'  
value='Residual Soil' value_secondary=None color='#FF0000'  
value='Fill' value_secondary=None color='#FF0000'  
value='Artificial' value_secondary=None color='#FF0000'  
value='Organic' value_secondary=None color='black'  
value='Peat' value_secondary=None color='black'  
value='Clay' value_secondary=None color='green'  
value='Silt' value_secondary=None color='orange'  
value='Sand' value_secondary=None color='grey'  
value='Gravel' value_secondary=None color='orange'  

### `soil_type2`
**symbol**: $\text{soil\_type2}$  
**label**: Soil type 2  
**unit**: None  
**description**: Secondary soil type description  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Other' value_secondary=None color=None  
value='Highly organic' value_secondary=None color=None  
value='Fine' value_secondary=None color=None  
value='Coarse' value_secondary=None color=None  

### `soil_type3`
**symbol**: $\text{soil\_type3}$  
**label**: Soil type 3  
**unit**: None  
**description**: Tertiary soil type description  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Other' value_secondary=None color=None  
value='Clean sand' value_secondary=None color=None  
value='Clean sand/Sand with fines' value_secondary=None color=None  
value='Sand with fines' value_secondary=None color=None  
value='Clean gravel' value_secondary=None color=None  
value='Clean gravel/Gravel with fines' value_secondary=None color=None  
value='Gravel with fines' value_secondary=None color=None  

### `soil_type_index`
**symbol**: $\text{soil\_type\_index}$  
**label**: Soil type index  
**unit**: None  
**description**: Index for soil type classification  
**data_type**: `str`  
**corresponding_parameter_name**: `soil_type_index_label`  
    
#### discrete_data
is_categorical: True

value='0' value_secondary=None color=None  
value='1' value_secondary=None color=None  
value='2' value_secondary=None color=None  
value='3' value_secondary=None color=None  
value='4a' value_secondary=None color=None  
value='4b' value_secondary=None color=None  
value='5' value_secondary=None color=None  

### `soil_type_index_label`
**symbol**: $\text{soil\_type\_index\_label}$  
**label**: Soil type index label  
**unit**: None  
**description**: Label for soil type index  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Other' value_secondary='Other' color='#FF0000'  
value='Very soft clays' value_secondary='Very Soft Clays, or Sensitive or Collapsible Soils' color='#A5ABBB'  
value='Clay and/or Silt' value_secondary='Clay and/or Silt' color='#4B5878'  
value='Clayey Silt and/or Silty Clay' value_secondary='Clayey Silt and/or Silty Clay' color='#479085'  
value='Sandy Silt' value_secondary='Sandy Silt' color='#7EC4A0'  
value='Silty Sand' value_secondary='Silty Sand' color='#BFA364'  
value='Sand to Sandy Gravel' value_secondary='Sand to Sandy Gravel' color='#EB9D4A'  

### `special_cyclic_resistance_ratio_min`
**symbol**: $CRR_{min}$  
**label**: Special cyclic resistance ratio min.  
**unit**: None  
**description**: Minimum cyclic resistance ratio for special soil layers  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `special_layers_thickness`
**symbol**: $H$  
**label**: Special layers thickness  
**unit**: m  
**description**: Thickness of special soil layers (NEHRP F site classification)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `special_shear_strain_mean`
**symbol**: $γ_{0.5\ mean}$  
**label**: Special shear strain mean  
**unit**: %  
**description**: Mean shear strain at G/G_max=0.5 for special soil layers  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `special_shear_velocity_mean`
**symbol**: $V_{s\ mean}$  
**label**: Special shear velocity mean  
**unit**: m/s  
**description**: Mean shear wave velocity of special soil layers  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `specific_gravity`
**symbol**: $G_s$  
**label**: Specific gravity  
**unit**: None  
**description**: Specific gravity of soil solids  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `specific_gravity_correction`
**symbol**: $a$  
**label**: Specific gravity correction  
**unit**: None  
**description**: Correction for specific gravity (hydrometer calibrated for G_s = 2.65)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `specimen_id`
**symbol**: $\text{specimen\_id}$  
**label**: Specimen ID  
**unit**: None  
**description**: Identifier for specimen  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `specimen_reference`
**symbol**: $\text{specimen\_reference}$  
**label**: Specimen reference  
**unit**: None  
**description**: Reference name specified for a specimen within a sample  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `spectral_acceleration_at_1_sec`
**symbol**: $Sa_1$  
**label**: Spectral acceleration at 1 sec.  
**unit**: g  
**description**: Spectral acceleration at 1-second period  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `ssi_effects_expected`
**symbol**: $\text{ssi\_effects\_expected}$  
**label**: SSI effects expected  
**unit**: None  
**description**: Indicates expected soil-structure interaction effects  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `standard_deviation`
**symbol**: $σ$  
**label**: Standard deviation  
**unit**: None  
**description**: Standard deviation for statistical analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `standardized_cumulative_absolute_velocity`
**symbol**: $CAV_{STD}$  
**label**: Standardized cumulative absolute velocity  
**unit**: g-sec  
**description**: Standardized cumulative absolute velocity  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `state_parameter`
**symbol**: $ψ$  
**label**: State parameter  
**unit**: None  
**description**: State parameter for soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `static_stiffness`
**symbol**: $K$  
**label**: Static stiffness  
**unit**: MN/m or MN-m/rad  
**description**: Static stiffness for mode j (translation or rotation)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `stiffness`
**symbol**: $k$  
**label**: Stiffness  
**unit**: MN/m or MN-m/rad  
**description**: Dynamic stiffness for mode j (translation or rotation)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `stiffness_edge_factor`
**symbol**: $R_k$  
**label**: Stiffness edge factor  
**unit**: None  
**description**: Stiffness edge increase factor  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `stiffness_intensity`
**symbol**: $k_i$  
**label**: Stiffness intensity  
**unit**: MN/m3  
**description**: Stiffness intensity for foundation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `stiffness_weight_factor_pile`
**symbol**: $w_p$  
**label**: Stiffness weight factor pile  
**unit**: None  
**description**: Weight factor for pile stiffness contribution  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `stiffness_weight_factor_pile_tip`
**symbol**: $w_b$  
**label**: Stiffness weight factor pile tip  
**unit**: None  
**description**: Weight factor for pile tip stiffness contribution  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `stiffness_weight_factor_soil`
**symbol**: $w_s$  
**label**: Stiffness weight factor soil  
**unit**: None  
**description**: Weight factor for soil stiffness contribution  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `stone_column_arrangement`
**symbol**: $\text{stone\_column\_arrangement}$  
**label**: Stone column arrangement  
**unit**: None  
**description**: Arrangement of stone columns  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='none' value_secondary=None color=None  
value='triangular' value_secondary=None color=None  
value='rectangular' value_secondary=None color=None  

### `stone_column_bottom_depth`
**symbol**: $z_{bottom}$  
**label**: Stone column bottom depth  
**unit**: m  
**description**: Bottom depth of stone column  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `stone_column_diameter`
**symbol**: $D$  
**label**: Stone column diameter  
**unit**: m  
**description**: Diameter of stone column  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `stone_column_is_present`
**symbol**: $sc_{present}$  
**label**: Stone column is present  
**unit**: None  
**description**: Indicates presence of stone column  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `stone_column_spacing`
**symbol**: $S$  
**label**: Stone column spacing  
**unit**: m  
**description**: Spacing between stone columns  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `stone_column_top_depth`
**symbol**: $z_{top}$  
**label**: Stone column top depth  
**unit**: m  
**description**: Top depth of stone column  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `stress_influence_factor`
**symbol**: $I_z$  
**label**: Stress influence factor  
**unit**: None  
**description**: Stress influence factor below footing center  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `stress_normalized_cone_resistance`
**symbol**: $Q_{tn}$  
**label**: Stress-normalized cone resistance  
**unit**: None  
**description**: Stress-normalized cone resistance from CPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `structure_effective_modal_height`
**symbol**: $h$  
**label**: Structure effective modal height  
**unit**: m  
**description**: Height of center of mass for first-mode shape  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `structure_flexible_period`
**symbol**: $T_{flexible}$  
**label**: Structure flexible period  
**unit**: s  
**description**: Flexible-base period of structure  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `structure_rigid_period`
**symbol**: $T$  
**label**: Structure rigid period  
**unit**: s  
**description**: Undamped natural vibration period of structure  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `structure_to_soil_stiffness_ratio`
**symbol**: $h/{V_s\ T}$  
**label**: Structure-to-soil stiffness ratio  
**unit**: None  
**description**: Ratio of structure to soil stiffness  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `structure_total_height`
**symbol**: $h_{total}$  
**label**: Structure total height  
**unit**: m  
**description**: Building height from foundation to roof  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `subgrade_reaction_modulus_at_diameter`
**symbol**: $k_{sd}$  
**label**: Subgrade reaction modulus at diameter  
**unit**: MPa  
**description**: Subgrade reaction modulus at one pile diameter  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `surface_elevation`
**symbol**: $\text{surface\_elevation}$  
**label**: Surface elevation  
**unit**: m  
**description**: Ground surface elevation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `temperature`
**symbol**: $T$  
**label**: Temperature  
**unit**: °C  
**description**: Temperature during testing  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `temperature_correction`
**symbol**: $F_T$  
**label**: Temperature correction  
**unit**: None  
**description**: Correction for hydrometer test temperature (not 20°C)  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `test_id`
**symbol**: $\text{test\_id}$  
**label**: Test ID  
**unit**: None  
**description**: Identifier for test  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `test_type`
**symbol**: $\text{test\_type}$  
**label**: Test type  
**unit**: None  
**description**: Type of test  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `thickness`
**symbol**: $H$  
**label**: Thickness  
**unit**: m  
**description**: Thickness of soil layer  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `thickness_liquefiable_layer`
**symbol**: $H_2$  
**label**: Thickness of liquefiable layer  
**unit**: m  
**description**: Thickness of liquefiable sand layer  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `thickness_non_liquefiable_layer`
**symbol**: $H_1$  
**label**: Thickness of non liquefiable layer  
**unit**: m  
**description**: Thickness of non-liquefiable surface layer  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `thickness_top_layer`
**symbol**: $H_{top}$  
**label**: Thickness of top layer  
**unit**: m  
**description**: Thickness of top soil layer from beneath foundation embedment  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `third_interval_blow_count`
**symbol**: $N_{third}$  
**label**: Third interval blow count  
**unit**: None  
**description**: Third interval blow count in SPT  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `time_step`
**symbol**: $Δt$  
**label**: Time step  
**unit**: s  
**description**: Time step for dynamic analysis  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `total_stress`
**symbol**: $σ_v$  
**label**: Total stress  
**unit**: kPa  
**description**: Total vertical stress in soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `total_stress_inc`
**symbol**: $σ_{v\ inc}$  
**label**: Total stress inc.  
**unit**: kPa  
**description**: Total stress in soil increment  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `total_vertical_stiffness`
**symbol**: $k_{z\ total}$  
**label**: Total vertical stiffness  
**unit**: MN/m  
**description**: Total dynamic vertical stiffness of foundation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `triaxial_planes_correction`
**symbol**: $K_r$  
**label**: Triaxial planes correction  
**unit**: None  
**description**: Correction for shearing of incorrect planes in cyclic triaxial test  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `tributary_area`
**symbol**: $\text{tributary\_area}$  
**label**: Tributary area  
**unit**: m2  
**description**: Tributary area for load distribution  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `true_depth`
**symbol**: $z_{true}$  
**label**: True depth  
**unit**: m  
**description**: Inclination-corrected depth  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `ultimate_bearing_capacity`
**symbol**: $Q_{ult}$  
**label**: Ultimate bearing capacity  
**unit**: kPa  
**description**: Ultimate bearing capacity of foundation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `ultimate_bearing_capacity_limit`
**symbol**: $Q_{ult\ lim}$  
**label**: Ultimate bearing capacity limit  
**unit**: kPa  
**description**: Limit for ultimate bearing capacity  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `unconfined_compressive_strength`
**symbol**: $q_u$  
**label**: Unconfined compressive strength  
**unit**: kPa  
**description**: Unconfined compressive strength of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `undrained_shear_strength`
**symbol**: $S_u$  
**label**: Undrained shear strength  
**unit**: kPa  
**description**: Undrained shear strength of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `consistency`  
    
#### data_bins

parameter_name: consistency

left=0.0 right=12.5 value='Very soft' color='gainsboro'  
left=12.5 right=25.0 value='Soft' color='lightgray'  
left=25.0 right=50.0 value='Medium' color='silver'  
left=50.0 right=100.0 value='Stiff' color='darkgray'  
left=100.0 right=200.0 value='Very stiff' color='gray'  
left=200.0 right=inf value='Hard' color='dimgray'  

### `undrained_shear_strength_bottom_layer`
**symbol**: $S_{u\ bottom}$  
**label**: Undrained shear strength bottom layer  
**unit**: kPa  
**description**: Undrained shear strength of clay beneath foundation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `undrained_shear_strength_factor`
**symbol**: $N_{kt}$  
**label**: Undrained shear strength factor  
**unit**: None  
**description**: Factor for undrained shear strength  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `undrained_shear_strength_ratio`
**symbol**: $S_{u\ ratio}$  
**label**: Undrained shear strength ratio  
**unit**: None  
**description**: Undrained shear strength to effective stress ratio  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `undrained_shear_strength_torvane`
**symbol**: $S_{u\ torvane}$  
**label**: Undrained shear strength Torvane  
**unit**: kPa  
**description**: Undrained shear strength from Torvane test  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `uniformity_coefficient`
**symbol**: $C_u$  
**label**: Uniformity coefficient  
**unit**: None  
**description**: Uniformity coefficient for particle size distribution  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `unit_adhesion`
**symbol**: $c_α$  
**label**: Unit adhesion  
**unit**: kPa  
**description**: Unit adhesion for pile shaft  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `unit_adhesion_to_cohesion_ratio`
**symbol**: $c_α/c_1$  
**label**: Unit adhesion to cohesion ratio  
**unit**: None  
**description**: Ratio of unit adhesion to unit cohesion  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `unit_side_friction`
**symbol**: $f_p$  
**label**: Unit side friction  
**unit**: MPa  
**description**: Pile unit side friction  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `unit_side_friction_clip`
**symbol**: $f_{p\ clip}$  
**label**: Unit side friction clip  
**unit**: None  
**description**: Applies clip to pile unit side friction  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `unit_side_friction_coefficient`
**symbol**: $C_s$  
**label**: Unit side friction coefficient  
**unit**: None  
**description**: Coefficient for pile unit side friction  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `unit_side_friction_limit`
**symbol**: $f_{p\ lim}$  
**label**: Unit side friction limit  
**unit**: MPa  
**description**: Limit for pile unit side friction  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `unit_weight`
**symbol**: $γ$  
**label**: Unit weight  
**unit**: kN/m3  
**description**: Unit weight of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `unit_weight_bottom_layer`
**symbol**: $γ_{bottom}$  
**label**: Unit weight bottom layer  
**unit**: kN/m3  
**description**: Unit weight of soil beneath foundation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `uscs_description`
**symbol**: $\text{uscs\_description}$  
**label**: USCS description  
**unit**: None  
**description**: Unified Soil Classification System description  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `uscs_symbol`
**symbol**: $\text{uscs\_symbol}$  
**label**: USCS symbol  
**unit**: None  
**description**: Unified Soil Classification System symbol  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Other' value_secondary=None color='#FF0000'  
value='Rock' value_secondary=None color='#FF0000'  
value='Weathered Rock' value_secondary=None color='#FF0000'  
value='Residual Soil' value_secondary=None color='#FF0000'  
value='Fill' value_secondary=None color='#FF0000'  
value='Artificial' value_secondary=None color='#FF0000'  
value='Peat' value_secondary=None color='brown'  
value='Pt' value_secondary=None color='brown'  
value='Organic' value_secondary=None color='brown'  
value='OL' value_secondary=None color='brown'  
value='OH' value_secondary=None color='brown'  
value='Clay' value_secondary=None color='green'  
value='CL' value_secondary=None color='green'  
value='CL-ML' value_secondary=None color='green'  
value='CH' value_secondary=None color='green'  
value='Silt' value_secondary=None color='orange'  
value='ML' value_secondary=None color='orange'  
value='MH' value_secondary=None color='orange'  
value='Sand' value_secondary=None color='grey'  
value='SW' value_secondary=None color='grey'  
value='SP' value_secondary=None color='grey'  
value='SP-SW' value_secondary=None color='grey'  
value='SW-SM' value_secondary=None color='grey'  
value='SW-SC' value_secondary=None color='grey'  
value='SP-SM' value_secondary=None color='grey'  
value='SP-SC' value_secondary=None color='grey'  
value='SM' value_secondary=None color='grey'  
value='SC' value_secondary=None color='grey'  
value='SC-SM' value_secondary=None color='grey'  
value='Gravel' value_secondary=None color='orange'  
value='GW' value_secondary=None color='orange'  
value='GP' value_secondary=None color='orange'  
value='GP-GW' value_secondary=None color='orange'  
value='GW-GM' value_secondary=None color='orange'  
value='GW-GC' value_secondary=None color='orange'  
value='GP-GM' value_secondary=None color='orange'  
value='GP-GC' value_secondary=None color='orange'  
value='GM' value_secondary=None color='orange'  
value='GC' value_secondary=None color='orange'  
value='GC-GM' value_secondary=None color='orange'  

### `usda_description`
**symbol**: $\text{usda\_description}$  
**label**: USDA description  
**unit**: None  
**description**: USDA soil classification description  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `usda_symbol`
**symbol**: $\text{usda\_symbol}$  
**label**: USDA symbol  
**unit**: None  
**description**: USDA soil classification symbol  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: True

value='Cl' value_secondary='clay' color='#be826c'  
value='SiCl' value_secondary='silty clay' color='#cc6d4d'  
value='SaCl' value_secondary='sandy clay' color='#e99641'  
value='ClLo' value_secondary='clay loam' color='#e47b3b'  
value='SiClLo' value_secondary='silty clay loam' color='#ef9360'  
value='SaClLo' value_secondary='sandy clay loam' color='#efaf6f'  
value='Lo' value_secondary='loam' color='#f0a654'  
value='SiLo' value_secondary='silt loam' color='#d09662'  
value='SaLo' value_secondary='sandy loam' color='#faba75'  
value='Si' value_secondary='silt' color='#dfb48f'  
value='LoSa' value_secondary='loamy sand' color='#eacfbc'  
value='Sa' value_secondary='sand' color='#eee6da'  

### `use_alternate_equation`
**symbol**: $\text{use\_alternate\_equation}$  
**label**: Use alternate equation  
**unit**: None  
**description**: Uses alternate equation for calculations  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `use_constant_volume_friction_angle`
**symbol**: $\text{use\_constant\_volume\_friction\_angle}$  
**label**: Use constant volume friction angle  
**unit**: None  
**description**: Uses constant volume friction angle for residual strength  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `use_lower_bound`
**symbol**: $\text{use\_lower\_bound}$  
**label**: Use lower bound  
**unit**: None  
**description**: Uses lower bound for applicable formulations  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `use_simplified_blows_correction`
**symbol**: $\text{use\_simplified\_blows\_correction}$  
**label**: Use simplified blows correction  
**unit**: None  
**description**: Applies SPT blow count correction for energy only  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `values_to_average`
**symbol**: $\text{values\_to\_average}$  
**label**: Values to average  
**unit**: None  
**description**: Values used for averaging  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `vented_control_unit_reading_a`
**symbol**: $Z_{M\ A}$  
**label**: Vented control unit reading for A  
**unit**: kPa  
**description**: Control unit reading when system is vented for A  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `vented_control_unit_reading_b`
**symbol**: $Z_{M\ B}$  
**label**: Vented control unit reading for B  
**unit**: kPa  
**description**: Control unit reading when system is vented for B  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `vertical_stiffness`
**symbol**: $k_z$  
**label**: Vertical stiffness  
**unit**: MN/m  
**description**: Dynamic vertical stiffness of foundation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `vertical_stiffness_intensity`
**symbol**: $k_z^i$  
**label**: Vertical stiffness intensity  
**unit**: MN/m3  
**description**: Vertical stiffness intensity for foundation  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `vibration_constant`
**symbol**: $χ$  
**label**: Vibration constant  
**unit**: None  
**description**: Dimensionless constant for vibration for mode j  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `vibration_mode`
**symbol**: $j$  
**label**: Vibration mode  
**unit**: None  
**description**: Vibration mode for dynamic analysis  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='x' value_secondary=None color=None  
value='y' value_secondary=None color=None  
value='z' value_secondary=None color=None  
value='xx' value_secondary=None color=None  
value='yy' value_secondary=None color=None  
value='xx and yy' value_secondary=None color=None  
value='zz' value_secondary=None color=None  

### `vibration_mode_group`
**symbol**: $j_{group}$  
**label**: Vibration mode group  
**unit**: None  
**description**: Vibration mode group  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    
#### discrete_data
is_categorical: False

value='x overall' value_secondary=None color=None  
value='y overall' value_secondary=None color=None  
value='x base spring' value_secondary=None color=None  
value='y base spring' value_secondary=None color=None  
value='z' value_secondary=None color=None  
value='xx' value_secondary=None color=None  
value='yy' value_secondary=None color=None  
value='zz' value_secondary=None color=None  

### `void_ratio`
**symbol**: $e$  
**label**: Void ratio  
**unit**: None  
**description**: Void ratio of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `void_redistribution_is_significant`
**symbol**: $\text{void\_redistribution\_is\_significant}$  
**label**: Void redistribution is significant  
**unit**: None  
**description**: Applies for I&B residual shear strength calculations  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `volumetric_strain`
**symbol**: $ε_v$  
**label**: Volumetric strain  
**unit**: %  
**description**: Volumetric strain in soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `volumetric_strain_depth_weighting_factor`
**symbol**: $DF$  
**label**: Volumetric strain depth weighting factor  
**unit**: None  
**description**: Depth weighting factor for volumetric strain  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `water_content`
**symbol**: $w_c$  
**label**: Water content  
**unit**: %  
**description**: Natural water content of soil  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `water_content_liquid_limit_ratio`
**symbol**: $w_c\ /\ LL$  
**label**: Water content to liquid limit ratio  
**unit**: None  
**description**: Ratio of water content to liquid limit  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `water_content_trials`
**symbol**: $w_c$  
**label**: Water content (trials)  
**unit**: %  
**description**: Natural water content for each trial  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `water_table`
**symbol**: $z_w$  
**label**: Water table  
**unit**: m  
**description**: Depth to water table below ground surface  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `water_table_present`
**symbol**: $z_{w\ present}$  
**label**: Water table present  
**unit**: None  
**description**: Indicates presence of water table  
**data_type**: `bool`  
**corresponding_parameter_name**: `None`  
    

### `water_unit_weight`
**symbol**: $γ_w$  
**label**: Water unit weight  
**unit**: kN/m3  
**description**: Unit weight of water  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `zero_correction`
**symbol**: $F_z$  
**label**: Zero correction  
**unit**: None  
**description**: Hydrometer zero correction for deflocculating agent  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `zero_friction_length`
**symbol**: $ZFL$  
**label**: Zero-friction length  
**unit**: m  
**description**: Pile zero-friction length  
**data_type**: `float`  
**corresponding_parameter_name**: `None`  
    

### `zone_letter`
**symbol**: $\text{zone\_letter}$  
**label**: Zone letter  
**unit**: None  
**description**: UTM WGS84 zone letter  
**data_type**: `str`  
**corresponding_parameter_name**: `None`  
    

### `zone_number`
**symbol**: $\text{zone\_number}$  
**label**: Zone number  
**unit**: None  
**description**: UTM WGS84 zone number  
**data_type**: `int`  
**corresponding_parameter_name**: `None`  
    