"""CIF to XYZ 변환 스크립트 (VMD용)"""

from pathlib import Path
from ase.io import read, write

structures_dir = Path(r'c:\cement_final\structures')
vmd_dir = structures_dir / 'vmd'
vmd_dir.mkdir(exist_ok=True)

# 주요 파일만 변환
key_files = [
    'C3S_optimized.cif',
    'C3S_hydration_initial.cif',
    'FlyAshC_optimized.cif',
    'FlyAshC_hydration.cif',
    'EAFSlag_optimized.cif',
    'EAFSlag_hydration.cif',
    'WasteGlass_optimized.cif',
    'SteelSlag_optimized.cif',
]

print('Converting CIF to XYZ for VMD...')
print('='*50)

for cif_name in key_files:
    cif_path = structures_dir / cif_name
    if cif_path.exists():
        atoms = read(cif_path)
        xyz_name = cif_name.replace('.cif', '.xyz')
        xyz_path = vmd_dir / xyz_name
        write(xyz_path, atoms)
        print(f'[OK] {cif_name} -> {xyz_name}')
    else:
        print(f'[SKIP] Not found: {cif_name}')

print('='*50)
print(f'\nFiles saved to: {vmd_dir}')
print('\nVMD에서 열기:')
print('File -> New Molecule -> Browse -> .xyz 파일 선택')
