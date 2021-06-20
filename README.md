# ansible-ini2yaml

- [ansible-ini2yaml](#ansible-ini2yaml)
  - [Usage](#usage)
  - [Disclamer](#disclamer)
  - [Contribute](#contribute)
  - [Submit Feedback](#submit-feedback)

## Usage

The file that will be converted needs to be passed as a argument, and the script will print the converted yaml, so if you want to save it to another file, just do a output redirect to it.

```
python ini2yaml.py example.ini > example.yaml
```

The `example.yaml` file will contains:

```yaml
all:
  children:
    ungrouped:
      hosts:
        prototype:
          ansible_host: host
          prototype_vhost_domain: prototype.app.host
          prototype_port: 8080
          ssl: true
    enonic:
      hosts:
        review:
          ansible_host: host
          enonic_vhost_domain: review.enonic.host
          enonic_port: 8080
          ssl: true
        master:
          ansible_host: host
          enonic_vhost_domain: master.enonic.host
          enonic_port: 8081
          ssl: true
      vars:
        enonic_ci: true
        enonic_ci_version: 7.6
        npm_install: false
        gulp: true
        gulp_arguments: build
        minio: true
        gdrive: true
    local:
      hosts:
        localhost:
          ansible_connection: local
          ansible_python_interpreter: /usr/bin/env python3
      vars:
        enonic_supassword: 123password
        enonic_repo: '""'
        prototype_local_port: 8080
        prototype_node_version: 8.2.1
  vars:
    project_name: test-app
    project_shortname: test-app
    project_app_name: com.app.test
    project_path: output
    project_gdrive_name: TEST
    enonic: true
    enonic_xp_folder: true
    enonic_version: 7.5.0
    enonic_smtp: true
    enonic_environment: prod
    enonic_jar_path: jars
    sonarqube: false
    sonarqube_url: http://sonarqube.link
    sonarqube_project_key: sonarqube:key
    sonarqube_token: <sonarqube-token>
    sonarqube_branch: master
    prototype: false
    prototype_php_version: 7.2
```

## Disclamer

Support for groups of groups (or childrens of childrens) was not implemented yet, but feel free to submit a PR.

## Contribute

Contributions are always welcome!
If you need some light, read some of the following guides: 
- [The beginner's guide to contributing to a GitHub project](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/)
- [First Contributions](https://github.com/firstcontributions/first-contributions)
- [How to contribute to open source](https://github.com/freeCodeCamp/how-to-contribute-to-open-source)
- [How to contribute to a project on Github](https://gist.github.com/MarcDiethelm/7303312)

## Submit Feedback

Be free to [open an issue](https://github.com/DaviPtrs/enonic-operator-k8s/issues/new/choose) telling your experience, suggesting new features or asking questions (there's no stupid questions, but make sure that yours cannot be answered by just reading the docs)

You can also find me on LinkedIn [/in/davipetris](https://www.linkedin.com/in/davipetris/)