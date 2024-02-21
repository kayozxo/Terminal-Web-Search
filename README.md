# Terminal-Web-Search

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Description

Terminal-Web-Search is a command-line tool that allows users to search different popular websites like YouTube, Google, Pinterest, Twitter, Reddit, Medium, Spotify, Wikipedia, and GitHub with just one command from the terminal.

## Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Supported Websites](#supported-websites)
- [License](#license)

## Dependencies

Terminal-Web-Search relies on the following Python library:

- [coloroma](https://pypi.org/project/colorama/)

You can install it using:

```bash
pip install colorama
```

## Installation

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/your-username/Terminal-Web-Search.git
   ```

2. Open your `.bashrc` file using a text editor like Vim.

   ```bash
   vim ~/.bashrc
   ```

3. Add the following alias at the end of the `.bashrc` file.

   ```bash
   alias s='python PATH_TO_MAIN.PY_FILE'
   ```

   Note: Replace `PATH_TO_MAIN.PY_FILE` with the actual path to your main Python file.

4. Save and quit the file using Vim commands (`Esc`, `:wq`, `Enter`).

5. Source the updated `.bashrc` file.

   ```bash
   source ~/.bashrc
   ```

6. Restart your terminal.

## Usage

After completing the installation steps, you can use the following commands to perform web searches for specific websites:

- Google: `s g search_query`
- YouTube: `s yt search_query`
- Medium: `s md search_query`
- Reddit: `s rt search_query`
- Spotify: `s sp search_query`
- Pinterest: `s pt search_query`
- GitHub: `s gt search_query`
- Twitter: `s x search_query`
- Wikipedia: `s wk search_query`

Replace `search_query` with your actual search query.

## Supported Websites

Terminal-Web-Search supports the following popular websites:

- Google (`g`)
- YouTube (`yt`)
- Medium (`md`)
- Reddit (`rt`)
- Spotify (`sp`)
- Pinterest (`pt`)
- GitHub (`gt`)
- Twitter (`x`)
- Wikipedia (`wk`)

Feel free to expand this list based on your preferences and needs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
