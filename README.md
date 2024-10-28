# JamieLiu_Mini8
[![python_CI](https://github.com/nogibjj/JamieLiu_Mini8/actions/workflows/python_CI.yml/badge.svg)](https://github.com/nogibjj/JamieLiu_Mini8/actions/workflows/python_CI.yml)
[![rust_CI](https://github.com/nogibjj/JamieLiu_Mini8/actions/workflows/rust_CI.yml/badge.svg)](https://github.com/nogibjj/JamieLiu_Mini8/actions/workflows/rust_CI.yml)


## Merge Sort Performance Comparison: Python vs. Rust

This project presents a performance comparison between Python and Rust implementations of the Merge Sort algorithm, focusing on execution time and memory usage. By evaluating both languages across input sizes ranging from 100 to 1,000,000 elements, the analysis highlights how each language scales with increasing data volume. The results demonstrate Rust's superior efficiency in handling larger datasets, making it a strong choice for computationally intensive tasks.


## Setup

### Prerequisites

- Python 3.9 or later
- Rust (stable, version 1.56.0 or later)
- `cargo` (Rust package manager)

### Python Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Python Tests**:
   ```bash
   python -m unittest test_main.py
   ```


### Rust Setup

1. **Build the Rust Project**:
   ```bash
   cargo build --release
   ```

2. **Run Rust Benchmarks**:
   ```bash
   cargo run --release
   ```

This will generate the necessary CSV files containing benchmark results for both Python and Rust implementations.

### Generate the Comparison Table

After running the benchmarks, generate the comparison table using the provided Python script:

```bash
python table.py
```

This command will produce a `comparison_results.csv` file, which compares the time and memory usage between the Python and Rust implementations.




## Result Table

| Size     | Time (s)_Python | Memory (bytes)_Python | Time (s)_Rust | Memory (bytes)_Rust | Speed Difference (Python/Rust) | Memory Savings (%) |
|----------|-----------------|----------------------|---------------|--------------------|-------------------------------|--------------------|
| 100      | 0.000917        | 6,994                | 0.000017      | 424                | 53.94                         | 93.94              |
| 1,000    | 0.012328        | 18,808               | 0.000068      | 4,024              | 181.29                        | 78.60              |
| 10,000   | 0.175810        | 169,368              | 0.000760      | 40,024             | 231.33                        | 76.37              |
| 100,000  | 2.261680        | 1,727,496            | 0.015217      | 400,024            | 148.63                        | 76.84              |
| 1,000,000 | 28.106427      | 16,783,864           | 0.105738      | 4,000,024          | 265.81                        | 76.17              |

### Analysis

- **Speed Improvement**:
  - The Rust implementation shows significant speed improvements over Python across all input sizes. 
  - The **Speed Difference (Python/Rust)** column demonstrates that Rust is faster by a factor of `53.94x` for `100` elements, and up to `265.81x` for `1,000,000` elements. This advantage increases with input size, highlighting Rust's efficiency in handling large-scale computations.

- **Memory Usage**:
  - Rust’s memory usage is much lower compared to Python. 
  - The **Memory Savings (%)** demonstrates that memory savings range from `93.94%` for smaller inputs to around `76%` for larger ones. Rust remains consistently more memory-efficient 


## Binary Download Link
https://github.com/nogibjj/JamieLiu_Mini8/actions/runs/11547589318/artifacts/2110482070