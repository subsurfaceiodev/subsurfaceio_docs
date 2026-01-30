import re
import warnings
from subsurfaceio.parameters import PARAMETERS
from subsurfaceio.function_sequences.function_sequence import FunctionSequence
from subsurfaceio.function_sequences.function_sequences import FunctionSequences
from subsurfaceio.dashapp.config import AppInfo

from subsurfaceio.references import REFERENCES
from subsurfaceio.references.references import latex_to_unicode


def parameters_as_tex(
        parameters,
        fields: list[str] = None,
        sep: str = ' ||| ',
        include_header: bool = True,
        sort: bool = False,
        mode: str = 'inline'
):
    from subsurfaceio.latex import group_tex_list
    # https://ashki23.github.io/markdown-latex.html
    if fields is None:
        fields = ['label_with_unit', 'description']

    tex_dict = {}
    for parameter_name, parameter in parameters.items():
        parameter_text = sep.join(
            str(getattr(parameter, field)) for
            field in fields
            if getattr(parameter, field)
        )
        parameter_text = parameter_text.replace('%', '\\%').replace('#', '\\#').replace('&', '\\&').replace('$',
                                                                                                            '\\$')
        tex_dict.update({
            parameter_name: f'{parameter.symbol_tex} &= \\text{{{parameter_text}}}'
        })
    if sort:
        tex_dict = dict(sorted(tex_dict.items()))
    tex_group = list(tex_dict.values())
    if include_header:
        parameter_text_header = sep.join([x.upper() for x in fields])
        tex_group.insert(
            0, f'symbol &= \\text{{{parameter_text_header}}}'
        )
    tex_group = group_tex_list(tex_group, mode=mode, key='align')
    return tex_group


def get_source_code(file):
    from subsurfaceio.api_examples import base_path
    with open(base_path / file, 'r', encoding='utf-8') as file:
        python_code = file.read()
        return python_code


EXAMPLES_MAP = {
    'Parameters info': 'parameters.py',
    'Calculate': 'soil_classification.py',
    'In situ test interpretation CPT': 'in_situ_test_interpretation_cpt.py',
    'In situ test interpretation DMT': 'in_situ_test_interpretation_dmt.py',
    'Parametric calculation CPT': 'parametric_calculation_cpt.py',
    'Parametric calculation DMT': 'parametric_calculation_dmt.py',
    'Plot': 'plot.py',
    # 'LogPlot': 'logplot.py',
}

for example_label, example_file in EXAMPLES_MAP.items():
    with open(f'docs/api/examples/{example_file}.md', 'w', encoding='utf-8') as file:
        content = f"```py title='{example_file}'\n{get_source_code(example_file)}\n```"
        file.write(f'''---
title: {example_label}
---

{content}
''')


def sequence_to_markdown_links(
        sequence: FunctionSequence,
):
    md = []
    md.append('#### `description`\n')
    md.append(f'{sequence.description}')
    md.append('\n')

    md.append('#### `references`\n')
    for reference in sequence.references or []:
        md.append(f'* [`{reference}`](../references.md#{reference})  ')
    md.append('\n')

    md.append('#### `functions`\n')
    for function in sequence.functions:
        function_name = function.__name__
        module_ = function.__module__.rsplit('.', 1)[-1]
        md.append(f'* [`{function_name}`](../functions/{module_}.md#subsurfaceio.functions.{module_}.{function_name})  ')
    md = '\n'.join(md)
    return md


for sequence_name, sequence in FunctionSequences().as_dict.items():
    with open(f'docs/function-sequences/{sequence_name}.md', 'w', encoding='utf-8') as file:
        file.write(sequence_to_markdown_links(sequence))

md = []
for reference_id, reference in REFERENCES.items():
    md.append(f'''
### `{reference_id}`
**title**: {latex_to_unicode(reference.title)}  
**author**: {latex_to_unicode(reference.author)}  
**year**: {reference.year}  
**link**: [{reference.link}]({reference.link}){{:target="_blank"}}
''')
md = '\n'.join(md)
with open(f'docs/references.md', 'w', encoding='utf-8') as file:
    file.write(md)

md = []
for parameter_name, parameter in PARAMETERS.items():
    md.append(f'''
### `{parameter_name}`
**symbol**: ${parameter.symbol_tex}$  
**label**: {parameter.label}  
**unit**: {parameter.unit}  
**description**: {parameter.description}  
**data_type**: `{parameter.data_type}`  
**corresponding_parameter_name**: `{parameter.corresponding_parameter_name}`  
''')
    if parameter.discrete_data is not None:
        md_ = [
            f'#### discrete_data\nis_categorical: {parameter.discrete_data.is_categorical}\n'
        ]
        for x in parameter.discrete_data.data:
            md_.append(f'{x}  ')
        md.extend(md_)
    if parameter.data_bins is not None:
        md_ = [
            f'#### data_bins\n'
        ]
        for data_bin_parameter_name, data_bin in parameter.data_bins.items():
            md_.append(f'parameter_name: {data_bin_parameter_name}\n')
            for x in data_bin.root:
                md_.append(f'{x}  ')
        md.extend(md_)
md = '\n'.join(md)
with open(f'docs/parameters.md', 'w', encoding='utf-8') as file:
    file.write(md)

from subsurfaceio.reference_data import ReferenceData

md = []
for reference_data_id, reference_data in ReferenceData().as_dict.items():
    # TODO how to handle SIEVES_SI_TO_PARTICLE_SIZE_MAP
    md.append(f'#### {reference_data_id}\n')
    md.append(
        reference_data.as_markdown_table()
    )
    md.append('\n')
md = '\n'.join(md)
with open(f'docs/reference_data.md', 'w', encoding='utf-8') as file:
    file.write(md)
