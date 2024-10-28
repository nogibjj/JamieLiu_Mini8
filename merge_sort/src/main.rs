use jemalloc_ctl::stats;
use jemallocator::Jemalloc;
use rand::seq::SliceRandom;
use rand::thread_rng;
use std::fs::File;
use std::io::{BufWriter, Write};
use std::mem;
use std::time::Instant;

#[global_allocator]
static GLOBAL: Jemalloc = Jemalloc;

fn merge_sort(arr: &mut [i32]) {
    if arr.len() > 1 {
        let mid = arr.len() / 2;
        let mut left = arr[..mid].to_vec();
        let mut right = arr[mid..].to_vec();

        merge_sort(&mut left);
        merge_sort(&mut right);

        merge(arr, &left, &right);
    }
}

fn merge(arr: &mut [i32], left: &[i32], right: &[i32]) {
    let mut left_idx = 0;
    let mut right_idx = 0;
    let mut merged_idx = 0;

    while left_idx < left.len() && right_idx < right.len() {
        if left[left_idx] <= right[right_idx] {
            arr[merged_idx] = left[left_idx];
            left_idx += 1;
        } else {
            arr[merged_idx] = right[right_idx];
            right_idx += 1;
        }
        merged_idx += 1;
    }

    while left_idx < left.len() {
        arr[merged_idx] = left[left_idx];
        left_idx += 1;
        merged_idx += 1;
    }

    while right_idx < right.len() {
        arr[merged_idx] = right[right_idx];
        right_idx += 1;
        merged_idx += 1;
    }
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let sizes = [100, 1_000, 10_000, 100_000, 1_000_000];
    let file = File::create("rust_merge_sort_benchmark.csv")?;
    let mut writer = BufWriter::new(file);

    // Write the header for the CSV
    writeln!(writer, "Size,Time (s),Memory (bytes)")?;

    for &size in &sizes {
        let mut arr: Vec<i32> = (0..size).collect();
        arr.shuffle(&mut thread_rng());

        // Measure memory before sorting
        let allocated_before = stats::allocated::read().unwrap();

        let start = Instant::now();
        merge_sort(&mut arr);
        let duration = start.elapsed();

        // Measure memory after sorting
        let allocated_after = stats::allocated::read().unwrap();
        let memory_usage = allocated_after - allocated_before;

        // Calculate the memory usage based on vector capacity
        let vec_memory = mem::size_of_val(&arr) + arr.capacity() * mem::size_of::<i32>();

        // Use the larger of the calculated memory usage and jemalloc measurement as an approximation.
        let peak_memory = std::cmp::max(memory_usage, vec_memory);

        // Write the result to the CSV
        writeln!(
            writer,
            "{},{:.6},{:?}",
            size,
            duration.as_secs_f64(),
            peak_memory
        )?;
    }

    println!("Benchmark results saved to rust_merge_sort_benchmark.csv");
    Ok(())
}
