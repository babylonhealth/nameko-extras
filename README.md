# nameko-extras

Some extra functionality for nameko.


### Installation

```bash
pip install nameko-extras
```


## Logging config from file

Logging may be configured from a file through the ``--logging-config-file`` option.

```bash
nameko_extras run <module>[:<ServiceClass>] --config ./foobar.yaml --logging-config-file ./logging.conf
```

## Autoreloading

For autoreloading simply add this key to your nameko config file.

```yaml
AUTORELOAD: true
```

And instead of running your service with the `nameko run` command, use `nameko_extras run`.
