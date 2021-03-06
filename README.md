# nuclipy
A simple template based vulnerability scanner (Inspired by ProjectDiscovery's [Nuclei](https://github.com/projectdiscovery/nuclei))

## Dependencies
nuclipy depends upon `python3` and the following modules `requests`, `argparse` and `PyYaml`.

## Installation
* Installation on Windows:
```
python -m pip install nuclipy
```

* Installation on Linux:
```
sudo pip3 install nuclipy
```
---
## Usage
Short from | Long form | Description 
-----------|-----------|-------------
-h  | --help        | Show the help menu 
-u  | --hostname    | Hostname to scan for vulnerabilities
-U  | --hostnames   | File containing target hostnames
-t  | --template    | Template id or path of template
-T  | --threads     | Number of threads (default=10)
-o  | --output      | Output file

## How to use templates?
You can find some templates in `templates/` directory.
*  Use a specific template
    ```sh
    python -m nuclipy -u example.com -t git-config.yaml
    ```
* Use all templates
    ```sh
    python -m nuclipy -u example.com -t all
    ```
* Save the output to a file
    ```sh
    python -m nuclipy -u example.com -t all -o nuclipy-output.txt
    ```
* Check all templates, for multiple targets
    ```sh
    python -m nuclipy -U target_hostnames.txt -t all
    ```
---
## How to write your own templates?
```yaml
id: git-config
name: Git Config Exposure
severity: medium

requests:
  - method: GET
  
    paths: 
      - "HOSTNAME/.git/config"

    patterns:
      - \[core\]
```

- `id`: id_of_the_template, usually resembles to the filename of the template without extension
- `name`: Name of the template to show in the results
- `severity`: severity of the vulnerability (`high`, `low`, `medium` or `info`)
- `requests`: Some request attributes and List of `paths` and `patterns`
    - `method`: HTTP request method (`GET` or `POST`)
    - `redirects`: Allow redirection or not (`ture` or `false`)
    - `paths`: List of paths to send requests
    - `patterns`: List of Regular Expressioins to match in the responses (with `AND` condition)
---

