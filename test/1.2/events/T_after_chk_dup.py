# © 2021-2023 Intel Corporation
# SPDX-License-Identifier: MPL-2.0

from os.path import join
import subprocess
from simicsutils.host import batch_suffix

cpu = SIM_create_object("clock", "clock", [["freq_mhz", 1]])
obj.queue = cpu
obj.alttest = 1

SIM_write_configuration_to_file(testname + ".chkp", Sim_Save_Nobundle)

subprocess.check_call(
    [f'{conf.sim.project}/bin/simics{batch_suffix()}'] +
    ["-batch-mode", "-quiet", "-no-copyright", "-core", "-werror",
     '-py3k-warnings',
     '-project', conf.sim.project,
     "-L", scratchdir,
     "-c", testname + ".chkp",
     "-p", join(basedir, "T_"+testname+".cont.py")])
