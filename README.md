# AI-Driven Computational Design of Carbon-Neutral Cement Binders

> **Personal Challenge 2026**  
> Computational Materials Science Research Project

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![CHGNet](https://img.shields.io/badge/CHGNet-v0.4+-green.svg)](https://github.com/CederGroupHub/chgnet)
[![MatterGen](https://img.shields.io/badge/MatterGen-MS%20Research-purple.svg)](https://github.com/microsoft/mattergen)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Table of Contents

- [Overview](#overview)
- [Key Results](#key-results)
- [Research Pipeline](#research-pipeline)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results Summary](#results-summary)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---

## Overview

This project applies **machine learning potentials (MLPs)** and **generative AI** to accelerate the discovery of **carbon-neutral cement binders**. We combine:

1. **CHGNet** - Universal neural network potential for atomistic simulations
2. **MatterGen** - Microsoft's generative AI for novel material discovery

### Key Achievements

| Metric | Value |
|--------|-------|
| **Industrial Waste Candidates Screened** | 16 |
| **Top Candidates Identified** | 5 (FlyAshC, EAFSlag, WasteGlass, CopperSlag, SteelSlag) |
| **AI-Generated Structures** | 32 (26 valid compositions) |
| **Maximum CO2 Reduction** | 90% |
| **Best AI Structure** | Ca2Si2O6 (E/atom = -7.82 eV) |

---

## Key Results

### Top 5 Industrial Waste Candidates

| Rank | Material | Score | CO2 Reduction |
|:----:|----------|:-----:|:-------------:|
| 1 | FlyAshC | 90.3 | 85% |
| 2 | EAFSlag | 89.4 | 75% |
| 3 | WasteGlass | 84.7 | 75% |
| 4 | CopperSlag | 79.0 | 75% |
| 5 | SteelSlag | 78.9 | 75% |

### MatterGen AI-Generated Top Structures

| Rank | Composition | E/atom (eV) | Source |
|:----:|-------------|:-----------:|--------|
| 1 | Ca2Si2O6 | -7.817 | Phase 2 (Ca-Si-O) |
| 2 | Ca4Si4O12 | -7.772 | Phase 2 (Ca-Si-O) |
| 3 | Al2Ca2FeSiO8 | -7.727 | Phase 1 (Ca-Si-Al-Fe-O) |
| 4 | Ca3Si2O7 | -7.651 | Phase 2 (Ca-Si-O) |
| 5 | CaFe2SiO4 | -7.592 | Phase 1 (Ca-Si-Al-Fe-O) |

---

## Research Pipeline

```
+------------------+     +------------------+     +------------------+
|   INPUT DATA     |     |   CHGNet         |     |   VALIDATION     |
|                  | --> |   Screening      | --> |   & Comparison   |
| - C3S Reference  |     | - Optimization   |     | - Energy         |
| - 16 Industrial  |     | - MD Simulation  |     | - Stability      |
|   Waste          |     | - CSH Formation  |     | - CO2 Reduction  |
+------------------+     +------------------+     +------------------+
                               |
                               v
                    +------------------+
                    |   MatterGen      |
                    |   AI Generation  |
                    | - 32 Structures  |
                    | - Novel Compos.  |
                    +------------------+
```

### Workflow Stages

1. **Structure Analysis** - C3S baseline characterization
2. **Hydration Simulation** - MD simulations of C-S-H formation
3. **Industrial Waste Screening** - 16 candidates evaluated
4. **MatterGen Generation** - AI-driven structure discovery
5. **Validation & Comparison** - CHGNet energy calculations

---

## Project Structure

```
cement_final/
├── notebooks/pipeline/           # Jupyter notebooks (main workflow)
│   ├── 01_Setup_Validation.ipynb    # Environment setup
│   ├── 02_Baseline_Reference.ipynb  # C3S baseline
│   ├── 03_Candidate_Database.ipynb  # Candidate structures
│   ├── 04_Screening_Pipeline.ipynb  # CHGNet screening
│   ├── 05_Results_Analysis.ipynb    # Results analysis
│   ├── 06_Paper_Figures.ipynb       # Publication figures
│   ├── 07_Visualization_Test.ipynb  # Visualization tests
│   ├── 08_MatterGen_Generation.ipynb  # MatterGen structure generation
│   ├── 09_MatterGen_Validation.ipynb  # MatterGen validation
│   ├── 10_MatterGen_Hydration.ipynb   # MatterGen hydration simulation
│   ├── 11_Final_Comparison.ipynb      # Final comparison
│   └── 12_Final_Figures.ipynb         # Final paper figures
│
├── structures/                   # Crystal structure files
│   ├── C3S_*.cif                # C3S structures
│   └── mattergen_optimized/     # Optimized MatterGen structures
│
├── data/
│   ├── mattergen/               # MatterGen generated structures
│   └── results/                 # Analysis results (JSON, CSV)
│
├── figures/
│   └── paper/                   # Publication-ready figures (Fig1-7)
│
├── trajectories/                # MD trajectory files
├── docs/                        # Documentation
├── src/                         # Source code modules
├── mattergen/                   # MatterGen repository (cloned)
├── environment.yml              # Conda environment
└── README.md                    # This file
```

---

## Installation

### Prerequisites

- Python 3.10+
- CUDA 11.8+ (for GPU acceleration)
- 16GB+ RAM recommended

### Setup

```bash
# Clone repository
git clone https://github.com/yourusername/cement-research.git
cd cement-research

# Create environment
conda env create -f environment.yml
conda activate cement_final

# Verify installation
python -c "from chgnet.model import CHGNet; print('CHGNet OK')"
```

### MatterGen Setup (Optional)

For AI structure generation:

```bash
# Clone MatterGen
git clone https://github.com/microsoft/mattergen.git
cd mattergen

# Install (in base environment)
pip install -e .

# Download checkpoints
git lfs pull
```

---

## Usage

### Quick Start

```bash
# Activate environment
conda activate cement_final

# Launch Jupyter
jupyter notebook

# Run notebooks in order: 01 -> 12
```

### Key Notebooks

| Notebook | Description | Environment |
|----------|-------------|-------------|
| 01-07 | CHGNet screening pipeline | cement_final |
| 08 | MatterGen structure generation | base |
| 09-12 | Validation and analysis | cement_final |

---

## Results Summary

### Performance Metrics

| Phase | Structures | Valid | Best Score |
|-------|:----------:|:-----:|:----------:|
| Industrial Waste Screening | 16 | 16 | 90.3 |
| MatterGen Generation | 32 | 26 | -7.82 eV/atom |
| Combined Candidates | 10 | 10 | - |

### CO2 Reduction Potential

- **Industrial Waste (Top 5)**: 75-85% reduction
- **MatterGen Structures**: 90% reduction (no clinker)

### Computation Time

- CHGNet optimization: ~2 min/structure (GPU)
- MD simulation (2 ps): ~10 min (GPU)
- MatterGen generation: ~5 min/batch (GPU)

---

## Figures

All publication-ready figures are in `figures/paper/`:

| Figure | Description |
|--------|-------------|
| Fig1 | Pipeline Overview |
| Fig2 | Screening Results |
| Fig3 | Top 5 Comparison |
| Fig4 | Molecular Analysis |
| Fig5 | Complete Pipeline (with MatterGen) |
| Fig6 | MatterGen vs Industrial Waste |
| Fig7 | Recommendations |

---

## Acknowledgments

- **CHGNet Team** - Universal neural network potential
- **Microsoft Research** - MatterGen generative AI
- **Materials Project** - DFT reference data
- **ASE Team** - Atomic Simulation Environment

---

## Citation

```bibtex
@misc{cement_ai_2026,
  title={AI-Driven Computational Design of Carbon-Neutral Cement Binders},
  author={Your Name},
  year={2026},
  howpublished={Personal Challenge 2026}
}
```

---

## License

MIT License - see [LICENSE](LICENSE) for details.

---

**Last Updated**: January 29, 2026  
**Version**: 1.0.0  
**Status**: Complete
