# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

This project was generated from [khiron_python_library](https://github.com/khiron/khiron_python_library), a Cookiecutter template designed for creating Python libraries with ease and efficiency.

## Features

- Easy-to-use project structure for Python libraries.
- Packaging with [Flit](https://flit.readthedocs.io/en/latest/) for simplicity and ease of use.
- Pre-configured development container setup for Visual Studio Code.
- Integrated testing setup with pytest.

## Getting Started

### Prerequisites

- Python `{{cookiecutter.python_version}}` or higher
- [Flit](https://flit.readthedocs.io/en/latest/) for packaging and publishing the library

### Setting Up the Development Environment

1. **Clone the repository**:

   `git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.git`
   `cd {{cookiecutter.project_name}}`

2. **Install dependencies**:

   Using Flit, you can install your project in editable mode along with its dependencies:

   `flit install --symlink`

3. **Open in Visual Studio Code** (if using Dev Containers):

   - Open VS Code in the project directory.
   - VS Code may prompt you to reopen the project in a container. If not, you can open the command palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS) and select "Remote-Containers: Reopen in Container".

### Running Tests

This project uses pytest for testing. Run tests with the following command:

```
pytest
```

## Project Structure

- `{{cookiecutter.library_name}}/`: The main Python package directory.
- `tests/`: Test directory for your package. Add your test files here.
- `.devcontainer/`: Configuration files for VS Code Development Containers.
- `.vscode/`: VS Code settings for the project.
- `pyproject.toml`: Project metadata and dependencies managed by Flit.

## Packaging and Distribution

This project uses Flit for packaging and distribution. To build your package and publish it to PyPI, run:

`flit publish`

Ensure you have configured your PyPI token for authentication.

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on how to submit pull requests, how to report bugs, and how to request features.

## License

This project is licensed under the `{{cookiecutter.license}}` - see the [LICENSE](LICENSE) file for details.
