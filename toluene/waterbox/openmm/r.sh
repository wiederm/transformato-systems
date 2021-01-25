set init = step3_charmm2omm
set cnt = 1
set istep = step4_equilibration
set input = step5_production
set istep = step5_${cnt}
python -u openmm_run.py -i ${input}.inp -t toppar.str -p ${init}.psf -c ${init}.crd  -odcd ${istep}.dcd 
