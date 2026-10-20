---
tags: [tool]
---

# Cargo


The basic format of a Rust Cargo command is: `cargo [options] [subcommand] [arguments]`

Here's a breakdown of each component:

- `cargo`: This is the command-line tool for managing Rust projects and dependencies.
- `options`: These are optional flags that modify the behavior of the Cargo command.
- `subcommand`: This is the specific action or operation you want Cargo to perform, such as `build`, `run`, `test`, `doc`, etc.
- `arguments`: These are additional parameters or arguments that you may provide to the Cargo subcommand, such as the name of a package, a file path, or other configuration options.

Here's a table listing some common Cargo options and subcommands:

| Command | Description |
| --- | --- |
| `cargo build` | Compile the current project. |
| `cargo run` | Compile and run the current project. |
| `cargo test` | Run tests in the current project. |
| `cargo bench` | Run benchmarks in the current project. |
| `cargo doc` | Generate documentation for the current project. |
| `cargo clean` | Remove the target directory. |
| `cargo new <project_name>` | Create a new Rust project. |
| `cargo init` | Initialize a new Rust project in an existing directory. |
| `cargo update` | Update dependencies as specified in the `Cargo.lock` file. |
| `cargo publish` | Publish a package to the [crates.io](http://crates.io/) registry. |
| `cargo install <crate>` | Install a Rust binary crate. |
| `cargo uninstall <crate>` | Uninstall a Rust binary crate. |
| `cargo search <query>` | Search for crates on [crates.io](http://crates.io/). |
| `cargo check` | Check the current project for errors without building it. |
| `cargo fmt` | Format Rust code using `rustfmt`. |
| `cargo clippy` | Run the `clippy` linter to catch common mistakes and style issues. |

These are just a selection of the many options and subcommands available in Cargo. You can explore more by running `cargo --help` or `cargo <subcommand> --help` in your terminal.

## Flags (Options)

> The **Rust Package Manager** and build system, offers a variety of flags that you can use to customize its behavior when compiling packages, running tests, or performing other tasks.
> 

> To provide a **more complete** table of common cargo flags across various **subcommands** in Rust, I'll include additional details and cover more **subcommands**. Cargo supports a wide range of commands, each with its own options and flags.
> 

| Flag Name | Description | Subcommand Usage |
| --- | --- | --- |
| `--name` | Sets the name of the package. | `cargo init`, `cargo new` |
| `--vcs` | Initializes a new VCS repository for the given VCS type. | `cargo init`, `cargo new` |
| `--lib` | Initializes a library instead of a binary. | `cargo init`, `cargo new` |
| `--bin` | Initializes a binary instead of a library. | `cargo init`, `cargo new` |
| `--edition` | Specifies the Rust edition to use (e.g., 2018, 2021). | `cargo init`, `cargo new` |
| `--offline` | Runs the command without accessing the network. | `cargo build`, `cargo run`, `cargo update` |
| `--verbose` | Uses verbose output. | All subcommands |
| `--release` | Builds artifacts in release mode, with optimizations. | `cargo build`, `cargo run` |
| `--features` | Enables specified package features. | `cargo build`, `cargo run`, `cargo check`, `cargo test` |
| `--all-features` | Enables all package features. | `cargo build`, `cargo run`, `cargo check`, `cargo test` |
| `--no-default-features` | Does not include the default features of the package. | `cargo build`, `cargo run`, `cargo check`, `cargo test` |
| `--target` | Specifies a target platform for the command. | `cargo build`, `cargo run`, `cargo check`, `cargo test` |
| `--jobs` | Limits the number of parallel jobs, overriding config. | `cargo build`, `cargo run`, `cargo test` |
| `--color` | Controls when colored output is used. | All subcommands |
| `--frozen` | Requires that Cargo.lock and cache are up to date. | All subcommands |
| `--locked` | Prevents updates to Cargo.lock. | All subcommands |
| `--exclude` | Excludes specified packages from the operation. | `cargo build`, `cargo update`, `cargo test` |
| `--package` or `-p` | Specifies a package to operate on in a workspace. | `cargo build`, `cargo run`, `cargo check`, `cargo test` |
| `--manifest-path` | Path to the manifest to execute the command on. | All subcommands |
| `--quiet` | Suppresses extra output from Cargo. | All subcommands |

This expanded table covers a broader range of subcommands and flags you might encounter while using Cargo in your Rust projects. This should provide a comprehensive guide to the available options and help you manage your Rust packages more effectively.

## References

- [The Cargo Book](https://doc.rust-lang.org/cargo/)
- …