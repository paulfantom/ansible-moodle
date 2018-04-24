<p><img src="https://moodle.org/logo/moodle-logo.png" alt="moodle logo" title="moodle" align="right" height="60" /></p>

# Ansible Role: moodle

[![Build Status](https://travis-ci.org/paulfantom/ansible-moodle.svg?branch=master)](https://travis-ci.org/paulfantom/ansible-moodle)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-paulfantom.moodle-blue.svg)](https://galaxy.ansible.com/paulfantom/moodle/)
[![GitHub tag](https://img.shields.io/github/tag/paulfantom/ansible-moodle.svg)](https://github.com/paulfantom/ansible-moodle/tags)

## Description

Deploy [moodle](https://moodle.org) open-source learning platform using ansible.

Installation is adapted from official moodle docs:
- [Step-by-step Installation Guide for Ubuntu](https://docs.moodle.org/34/en/Step-by-step_Installation_Guide_for_Ubuntu)
- [Nginx installation](https://docs.moodle.org/34/en/Nginx)
- [Administration via CLI](https://docs.moodle.org/34/en/Administration_via_command_line)

## Requirements

- Ansible >= 2.3

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `moodle_version` | `3.4` | Moodle package version |
| `moodle_external_url` | `http://localhost:8888` | External URL |
| `moodle_enable_av` | `True` | [Enable anti-virus](https://docs.moodle.org/34/en/Antivirus_plugins) |
| `moodle_data_dir` | `/srv/moodledata` | Location of uploaded files |
| `moodle_db` | {} | Moodle database configuration |
| `moodle_admin` | {} | Moodle admin user configuration |

## Example

### Playbook

Use it in a playbook as follows:
```yaml
- hosts: all
  become: yes
  roles:
    - paulfantom.moodle
```

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v1.25). You will have to install Docker on your system. See Get started for a Docker package suitable to for your system.
All packages you need to can be specified in one line:
```sh
pip install ansible 'ansible-lint>=3.4.15' 'molecule==1.25.0' docker 'testinfra>=1.7.0,<=1.10.1'
```
This should be similar to one listed in `.travis.yml` file in `install` section. 
After installing test suit you can run test by running
```sh
molecule test
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/stable-1.25/).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
