from transformato.testsystems import mutate_toluene_to_methane_cc, mutate_2_CPI_to_7_CPI_cc, mutate_2_methylfuran_to_methane_cc, mutate_2_methylindole_to_methane_cc, mutate_ethane_to_methane_cc, mutate_methane_to_methane_cc, mutate_methanol_to_methane_cc, mutate_neopentane_to_methane_cc
from transformato.utils import run_simulation, postprocessing
from transformato import load_config_yaml

############################################
# USER-DEFINED
############################################
engine = 'openMM'
base = '.'
############################################
############################################

for name in ['toluene', 'ethane', 'methanol', 'neopentane', 'methane', '2-methylindole', '2-methylfuran', '2-CPI', '7-CPI']:

    if name == 'toluene':
        conf_name = 'toluene-methane-rsfe.yaml'
        fn = mutate_toluene_to_methane_cc
    elif name == '2-CPI':
        conf_name = '2-CPI-7-CPI-rsfe.yaml'
        fn = mutate_2_CPI_to_7_CPI_cc
    elif name == '7-CPI':
        conf_name = '2-CPI-7-CPI-rsfe.yaml'
        fn = mutate_2_CPI_to_7_CPI_cc
    elif name == '2-methylfuran':
        conf_name = '2-methylfuran-methane-rsfe.yaml'
        fn = mutate_2_methylfuran_to_methane_cc
    elif name == '2-methylindole':
        conf_name = '2-methylindole-methane-rsfe.yaml'
        fn = mutate_2_methylindole_to_methane_cc
    elif name == 'methanol':
        conf_name = 'methanol-methane-rsfe.yaml'
        fn = mutate_methanol_to_methane_cc
    elif name == 'ethane':
        conf_name = 'ethane-methane-rsfe.yaml'
        fn = mutate_ethane_to_methane_cc
    elif name == 'neopentane':
        conf_name = 'neopentane-methane-rsfe.yaml'
        fn = mutate_neopentane_to_methane_cc
    elif name == 'methane':
        conf_name = 'ethane-methane-rsfe.yaml'
        fn = mutate_ethane_to_methane_cc
    else:
        raise RuntimeError('Only methane, ethane, methanol, 2-methylindole, 2-methylfuran, 2-CPI, 7-CPI, toluene or neopentane are allowed.')

    configuration = load_config_yaml(
        config=f"{base}/config/{conf_name}",
        input_dir=f'{base}',
        output_dir='.',
    )

    output_files_to_cc = fn(configuration=configuration)
    run_simulation(output_files_to_cc, engine=engine)
    postprocessing(configuration, name=name, engine=engine, max_snapshots=600)
