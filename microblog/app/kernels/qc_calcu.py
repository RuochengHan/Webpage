import psi4

def qc_psi4(atom1, atom2, distance, charge, spin, method, basis, cores, mem):
  psi4.set_memory(str(mem)+'GB')
  psi4.core.set_output_file('output.dat', False)

  numpy_memory = float(mem)

  mol = psi4.geometry(
  charge + ' ' + spin + '\n' +
  atom1 + ' 0 0 0\n' +
  atom2 + ' ' + str(distance) + ' 0 0\n'
  'symmetry c1')
  
  psi4_io = psi4.core.IOManager.shared_object()
  psi4_io.set_default_path('/scratch/ruhan/psi4')

  psi4.set_num_threads(int(cores))
  psi4.set_options({'basis': basis,
                  'scf_type': 'direct',
                  'reference': 'uhf',
                  'freeze_core': 'false',
                  'soscf': 'true',
                  'e_convergence': 1e-6,
                  'd_convergence': 1e-6})

  energy = psi4.energy(method)
  psi4_io.psiclean()

  return round(energy, 8)


