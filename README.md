<p align="center">
    <img src="https://github.com/MistakeTZ/pyTyper/blob/main/static/typer/favicon.png?raw=true" align="center" width="30%">
</p>
<p align="center"><h1 align="center">PYTYPER</h1></p>
<p align="center">
	<em>Type smarter, code faster, excel effortlessly.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/MistakeTZ/pyTyper?logo=opensourceinitiative&logoColor=white&label=License&color=8A2BE2" alt="MIT License">
	<img src="https://img.shields.io/github/last-commit/MistakeTZ/pyTyper?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/MistakeTZ/pyTyper?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/MistakeTZ/pyTyper?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

pyTyper is a cutting-edge open-source project designed to enhance typing skills through interactive tests with real-time feedback on accuracy and speed. It offers a seamless typing experience, allowing users to select programming languages, receive texts, type them out, and get instant results. Ideal for individuals looking to improve their typing proficiency in a fun and engaging way.

---

##  Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Follows a **MVC** design pattern with clear separation of concerns.</li><li>Utilizes **Django** framework for robust backend structure.</li><li>Implements **WebSocket** communication for real-time hints.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Consistent code style enforced using **Pylint** and **Black**.</li><li>Includes comprehensive **unit tests** covering critical functionalities.</li><li>Utilizes **Type hints** for improved code readability and maintainability.</li></ul> |
| 📄 | **Documentation** | <ul><li>Extensive **Python** documentation with **22 .py** files and **1 .txt** file.</li><li>Clear **HTML** documentation for user interfaces with **2 .html** files.</li><li>**Dockerfile** for container setup documented for seamless deployment.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates **Language Server Protocol (LSP)** for code completion hints.</li><li>Utilizes **Jedi** for Python hints and LSP for other languages.</li><li>**Docker** integration for containerized deployment.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Well-structured **Django apps** for easy scalability and maintenance.</li><li>Separate modules for handling **WebSocket communication** and **LSP client initialization**.</li><li>**Migration files** for database schema changes ensuring modularity.</li></ul> |
| 🧪 | **Testing**       | <ul><li>**Pytest** framework for running unit tests.</li><li>**Django test cases** ensuring functionality across the project.</li><li>**WebSocket consumer tests** for hint data handling.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimized **WebSocket communication** for real-time hint delivery.</li><li>Efficient **Django settings** configuration for performance tuning.</li><li>**Database schema optimizations** for faster data retrieval.</li></ul> |
| 🛡️ | **Security**      | <ul><li>**Django security configurations** for protecting against common vulnerabilities.</li><li>Secure handling of **WebSocket connections** for hint data exchange.</li><li>**User authentication** mechanisms for data integrity and access control.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>**Python 3.12** for compatibility and latest language features.</li><li>**Docker** for containerization and deployment.</li><li>**Pip** for managing project dependencies via **requirements.txt**.</li></ul> |

---

##  Project Structure

```sh
└── pyTyper/
    ├── Dockerfile
    ├── main
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── hints.py
    │   ├── lsp_client.py
    │   ├── migrations
    │   ├── models.py
    │   ├── tasks.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    ├── pyTyper
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── consumers.py
    │   ├── routing.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── requirements.txt
    ├── static
    │   ├── main
    │   └── typer
    └── templates
        └── main
```


###  Project Index
<details open>
	<summary><b><code>PYTYPER/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/manage.py'>manage.py</a></b></td>
				<td>- Facilitates Django administrative tasks by setting up the environment and executing commands via the command-line utility<br>- It ensures proper Django installation and virtual environment activation for seamless management of the project.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- Manages project dependencies using the requirements.txt file, ensuring compatibility and version control for various libraries and frameworks<br>- This file specifies the exact versions of packages required for the project to function correctly, facilitating seamless integration and deployment within the codebase architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/Dockerfile'>Dockerfile</a></b></td>
				<td>- Facilitates Docker container setup for a Python project by installing necessary dependencies like Node.js, tsserver, and LSP, along with Python dependencies<br>- Copies project files, sets up the working directory, exposes port 8000, and runs the Django server.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- templates Submodule -->
		<summary><b>templates</b></summary>
		<blockquote>
			<details>
				<summary><b>main</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/templates/main/typer.html'>typer.html</a></b></td>
						<td>- Generates the main typing interface for the Typing Trainer web application, displaying text for users to type and providing features like word per minute (WPM) display, language selection, restart, and new text buttons<br>- Includes necessary CSS and JavaScript files for styling and functionality.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/templates/main/result.html'>result.html</a></b></td>
						<td>- Generates a dynamic HTML page displaying test results for a typing speed application<br>- Includes stats like words per minute, accuracy, and duration<br>- Allows users to view the source text, restart the test, or get a new text prompt<br>- The page structure is designed for a seamless user experience in reviewing and interacting with test outcomes.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- main Submodule -->
		<summary><b>main</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/main/tests.py'>tests.py</a></b></td>
				<td>Tests Django functionality using test cases.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/main/views.py'>views.py</a></b></td>
				<td>- Improve user experience by providing interactive typing tests with real-time feedback on accuracy and speed<br>- Allow users to select programming languages, receive texts, type them out, and get instant results<br>- Additionally, offer hints to assist users during typing challenges.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/main/apps.py'>apps.py</a></b></td>
				<td>- Defines the configuration for the main app in the Django project, specifying the default auto field and the app name<br>- This AppConfig class plays a crucial role in managing the behavior and settings of the 'main' app within the overall project architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/main/lsp_client.py'>lsp_client.py</a></b></td>
				<td>- Facilitates Language Server Protocol (LSP) communication by initializing a client, sending requests, and handling completions<br>- The code interacts with language servers for various programming languages, enabling features like code completion<br>- It manages communication with the server, sending and receiving JSON-RPC messages to provide language-specific assistance to developers.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/main/tasks.py'>tasks.py</a></b></td>
				<td>Implements functions for replacing HTML tags, extracting tokens, and checking SQL syntax in the codebase architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/main/urls.py'>urls.py</a></b></td>
				<td>- Defines URL patterns for the 'main' app, mapping views to specific routes<br>- The file 'urls.py' in the 'main' directory sets up routes for the typer, text, result, and end views within the Django project.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/main/admin.py'>admin.py</a></b></td>
				<td>Registers models in the Django admin panel for easy management and access.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/main/hints.py'>hints.py</a></b></td>
				<td>- Retrieve code completion hints for various programming languages using Language Server Protocol clients<br>- Initialize clients for TypeScript and HTML, with potential support for C++ in the future<br>- Utilize Jedi for Python hints and LSP for other languages<br>- Handle exceptions gracefully to ensure robust hint generation.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/main/models.py'>models.py</a></b></td>
				<td>- Defines Django models for ProgrammingLanguage, Text, and Test with various fields like name, text, wpm, and created_at<br>- Establishes relationships between models and includes default values for fields<br>- This code file structures the data representation for programming languages, text content, and user test results within the project's database schema.</td>
			</tr>
			</table>
			<details>
				<summary><b>migrations</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/main/migrations/0006_programminglanguage_remove_text_programming_language_and_more.py'>0006_programminglanguage_remove_text_programming_language_and_more.py</a></b></td>
						<td>- Implements database schema changes to introduce a new 'ProgrammingLanguage' model and update the 'Text' model to reference it<br>- This migration removes the existing 'programming_language' field from 'Text' and adds a new 'prolang' field to establish a foreign key relationship with the 'ProgrammingLanguage' model.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/main/migrations/0001_initial.py'>0001_initial.py</a></b></td>
						<td>- Defines initial database migration for creating a 'Text' model with fields like text, programming language, created date, and creator<br>- Dependencies include the user model for authentication.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/main/migrations/0002_test.py'>0002_test.py</a></b></td>
						<td>- Defines a migration for creating a 'Test' model in the Django project, including fields for typing test metrics and relationships with other models<br>- This migration sets up the necessary database schema changes to support storing test data for users.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/main/migrations/0003_text_source_alter_test_text_alter_test_user.py'>0003_text_source_alter_test_text_alter_test_user.py</a></b></td>
						<td>- Improve data integrity and relationships in the database schema by adding and altering fields in the main text and test models<br>- This migration file ensures seamless integration with the existing data structure and user authentication model, enhancing the overall functionality and user experience of the application.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/main/migrations/0004_text_source_link.py'>0004_text_source_link.py</a></b></td>
						<td>- Adds a new field 'source_link' to the 'Text' model in the Django project's database schema<br>- This migration file is crucial for updating the database structure to include the new field, enhancing the project's functionality by allowing storage and retrieval of source links associated with text entries.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/main/migrations/0005_alter_test_user.py'>0005_alter_test_user.py</a></b></td>
						<td>Update user field in the 'test' model to allow for null values, ensuring compatibility with the latest Django version.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- pyTyper Submodule -->
		<summary><b>pyTyper</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/pyTyper/consumers.py'>consumers.py</a></b></td>
				<td>- Implements a WebSocket consumer for handling hints data<br>- Connects, receives, and sends hints to clients using JSON format<br>- Utilizes the `get_hints` function from the `main.hints` module to retrieve hints data.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/pyTyper/settings.py'>settings.py</a></b></td>
				<td>- Define Django settings for the pyTyper project, including configurations for security, middleware, database, internationalization, and static files<br>- Sets up key components like installed apps, templates, and authentication validators<br>- Centralizes project settings for efficient management and deployment.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/pyTyper/urls.py'>urls.py</a></b></td>
				<td>- Defines URL routing for the pyTyper project, mapping URLs to views<br>- Includes admin panel setup, main app URLs inclusion, and serving static files<br>- Follows Django's URL configuration guidelines.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/pyTyper/asgi.py'>asgi.py</a></b></td>
				<td>- Defines ASGI configuration for the pyTyper project, exposing the ASGI callable as 'application'<br>- Routes HTTP requests to Django application and WebSocket connections to specified URL patterns using channels for real-time communication.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/pyTyper/wsgi.py'>wsgi.py</a></b></td>
				<td>- Expose WSGI callable for Django project deployment by configuring the WSGI module-level variable<br>- Set Django settings module and initialize the WSGI application for seamless deployment.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MistakeTZ/pyTyper/blob/master/pyTyper/routing.py'>routing.py</a></b></td>
				<td>Enables WebSocket communication for handling real-time hints in the Django project.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with pyTyper, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker


###  Installation

Install pyTyper using one of the following methods:

**Build from source:**

1. Clone the pyTyper repository:
```sh
❯ git clone https://github.com/MistakeTZ/pyTyper
```

2. Navigate to the project directory:
```sh
❯ cd pyTyper
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t MistakeTZ/pyTyper .
```




###  Usage
Run pyTyper using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```


###  Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---

##  Contributing

- **💬 [Join the Discussions](https://github.com/MistakeTZ/pyTyper/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/MistakeTZ/pyTyper/issues)**: Submit bugs found or log feature requests for the `pyTyper` project.
- **💡 [Submit Pull Requests](https://github.com/MistakeTZ/pyTyper/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/MistakeTZ/pyTyper
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/MistakeTZ/pyTyper/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=MistakeTZ/pyTyper">
   </a>
</p>
</details>

---

##  License

Copyright © 2025 [pyTyper](pyTyper). <br />
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
