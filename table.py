import pandas as pd


def read_results(file_path):
    """
    Reads a CSV file and returns a DataFrame.
    """
    return pd.read_csv(file_path)


def generate_comparison_table(python_file, rust_file):
    """
    Reads the results from Python and Rust CSV files, and generates a comparison table.
    """
    df_python = read_results(python_file)
    df_rust = read_results(rust_file)

    # Merge the two DataFrames on the 'Size' column
    comparison = pd.merge(df_python, df_rust, on="Size", suffixes=("_Python", "_Rust"))

    # Calculate speed difference and memory savings
    comparison["Speed Difference (Python/Rust)"] = (
        comparison["Time (s)_Python"] / comparison["Time (s)_Rust"]
    )

    comparison["Memory Savings (%)"] = (
        (comparison["Memory (bytes)_Python"] - comparison["Memory (bytes)_Rust"])
        / comparison["Memory (bytes)_Python"]
    ) * 100

    # Save the comparison to a new CSV file
    comparison.to_csv("comparison_results.csv", index=False)
    print(comparison)


if __name__ == "__main__":
    # Replace with the paths to your CSV files
    python_file = "python_merge_sort_benchmark.csv"
    rust_file = "merge_sort/rust_merge_sort_benchmark.csv"
    generate_comparison_table(python_file, rust_file)
