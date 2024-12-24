---
title: Resolving glibc errors with python module
date: 2023-10-18 22:09:30
tags:
  - python
---

We recently switched out our lambda build image to a debian based image and started receiving errors around glibc.

```shell
[ERROR] Runtime.ImportModuleError. Unable to import module 'app':
/lib64/lib.so.6: version 'GLIBC_2.28' not found
(required by /var/task/cryptography/hazmat/bidnings/_rust.abi3.so)
```

After some googling we realized pip chooses the correct wheel for us and since we were running pip on a different machine than we were running our Python program on, we needed to let pip know about this.

RHEL/CentOS are using [manylinux2014](https://peps.python.org/pep-0599/) which is what we need to pass to `pip`

```shell
--platform manylinux2014_x86_64
```

Additionally we [do not want to use source packages](https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-only-binary), so we had to pass

```shell
 --only-binary=:all:
```

Our final command ended up being

```shell
python3 -m pip install --platform manylinux2014_x86_64 --only-binary=:all: -r requirements.txt
```
