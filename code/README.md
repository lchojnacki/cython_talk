# Cython vs Python benchmarks 🐍

## Description 🚀

This project benchmarks various algorithms implemented in both Python and
Cython, providing a performance comparison to highlight execution speed
differences.

## Requirements 📌

This project requires the following dependencies:
- [`uv`](https://github.com/astral-sh/uv) - required to easily set up the
  Python environment
- [`just`](https://github.com/casey/just) (installed via `apt`) - required to run predefined benchmark commands
- `libomp-dev` (installed via `apt`) - required for enabling multithreading
  support

## Installation 🛠️

Note: The installation instructions are written for Debian-based Linux
distributions and have been tested on Ubuntu 24.04 and Pop!_OS 22.04.

### 1. Install `just` and `libomp-dev`
```sh
sudo apt update && sudo apt install -y just libomp-dev
```

### 2. Install `uv`
Follow the official installation guide for `uv`:
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Usage ⏱️

To use the benchmark suite, run the following commands:

- **Build Cython versions:**
  ```sh
  just build
  ```
- **Validate output consistency between Python and Cython implementations:**
  ```sh
  just validate <benchmark name>
  ```
- **Run the benchmark tests:**
  ```sh
  just run <benchmark name>
  ```

### Available Benchmarks 🎯
- **loop** - Compares the performance of a `for` loop.
- **pi** - Benchmarks the Nilakantha algorithm for calculating π.
- **allocation** - Demonstrates how `malloc` can be utilized in Cython.
- **lettercount** - Compares the performance of opening and reading a text file.

To see the full list of available benchmarks, run:
```sh
just list-benchmarks
```

### Add a New Benchmark 🆕

To add a new benchmark, simply run the following command:
```sh
just new <benchmark name>
```

This will automatically create the necessary directories and files in both the
`src` (Python) and `cython` directories, as well as update the `setup.py`
to include the new benchmark and enable its compilation.
