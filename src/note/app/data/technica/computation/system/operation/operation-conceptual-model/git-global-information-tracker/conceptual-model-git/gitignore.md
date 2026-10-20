# Gitignore


The `.gitignore` file is used in Git repositories to specify which files or directories should be ignored and not tracked by Git. It helps prevent files like build artifacts, logs, and other non-essential files from being included in the version control system. Here’s the basic specification for a `.gitignore` file:

1. **File or Directory Patterns**: Each line in a `.gitignore` file represents a pattern that specifies files or directories to ignore. You can use the following syntax:
    - To ignore a specific file: `filename.ext`
    - To ignore all files with a certain extension: `.ext`
    - To ignore a directory and its contents: `/directoryname/`
    - To ignore all files and directories with a certain name: `name/`
    - To ignore files in a specific directory: `directoryname/*.ext`
2. **Comments**: Lines starting with `#` are treated as comments and are ignored by Git. You can add comments to explain the purpose of specific patterns.
3. **Negation**: You can use `!` before a pattern to negate it. For example, if you ignore all `.log` files but want to include a specific one, you can use `!specific.log`.
4. **Whitespace**: Whitespace at the beginning or end of a pattern is ignored, but it’s treated as part of the pattern if it occurs in the middle.

Example `.gitignore` file:

```
# Ignore compiled code
*.class

# Ignore logs
*.log

# Ignore the build directory
/build/

# Include a specific log file
!error.log

# Ignore temporary files
*.tmp

# Ignore all files in the "temp" directory
/temp/
```

Remember that you can have multiple `.gitignore` files in different directories within your Git repository, and Git will apply the rules recursively. Patterns in more specific `.gitignore` files can override patterns in more general ones.

Also, note that patterns in `.gitignore` files should be relative to the location of the `.gitignore` file itself. If you want to ignore files or directories globally for the entire repository, you can place a `.gitignore` file at the root of the repository.