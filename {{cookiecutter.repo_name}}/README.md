# {{ cookiecutter.title }} Ancillary Material #

This ancillary material includes the software used in the associated manuscript.

**TODO**: summarize included files

{%- if "y" in cookiecutter.jupyter|lower -%}

## Creating the Software Environment ##

We assume the use of the Anaconda distribution.
To create a software environment identical to that used in our manuscript, install Anaconda and run the following commands in your favorite shell (likely bash or PowerShell):

```
$ cd anc/
$ conda env create -f environment.yml
```

The provided Juyter notebooks should use the new environment automatically.

{%- endif -%}
