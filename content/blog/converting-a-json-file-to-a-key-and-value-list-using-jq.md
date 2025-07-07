---
title: Converting a JSON file to a key and value list using jq
date: 2023-03-14 22:09:30
permalink: /2023/03/15/converting-a-json-file-to-a-key-and-value-list-using-jq/
tags:
  - jq
---

Given a JSON file named `data.json`

```json
{
	"name": "Matt",
	"job": "Engineer"
}
```

You can output the keys and values using the following

```shell
jq -r 'to_entries|map("\(.key)=\(.value|tostring)")|.[]' data.json > file.txt
```

`file.txt` contains

```
name=Matt
job=Engineer
```

You can upper case the key, by piping `ascii_upcase` to `.key`

```shell
jq -r 'to_entries|map("\(.key|ascii_upcase)=\(.value|tostring)")|.[]' data.json > file.txt
```

`file.txt` now contains

```
NAME=Matt
JOB=Engineer
```

You can also prepend text to the keys as well, here we'll prepend `WOW_` to each key

```shell
jq -r 'to_entries|map("WOW_\(.key|ascii_upcase)=\(.value|tostring)")|.[]' data.json > file.txt
```

`file.txt` now contains

```
WOW_NAME=Matt
WOW_JOB=Engineer
```
