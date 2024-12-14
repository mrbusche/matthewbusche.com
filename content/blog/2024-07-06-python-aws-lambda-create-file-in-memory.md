---
title: Python AWS Lambda Create file in memory
date: 2024-07-06 16:09:30
tags:
  - python
  - lambda
---

If you need to create a file in a Lambda you need to write the file to `/tmp` because it is otherwise a read-only file system. But if you're emailing a file there's no need to write the file to the file system, with some minor alterations you can speed up the process and keep the file only in memory.

Current code

```python
csv_file = 'your_file.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for item in my_data:
        writer.writerow(item)

    return csv_file
```

New code

```python
buffer = io.StringIO()
writer = csv.DictWriter(buffer, fieldnames=headers)
writer.writeheader()
for item in my_data:
    writer.writerow(item)

return buffer
```

and also a small tweak to your email script

Current code

```python
attachment = MIMEBase('application', 'octet-stream')
attachment.set_payload(open(csv_file, 'rb').read())
```

New code

```python
attachment = MIMEBase('application', 'octet-stream')
attachment.set_payload(csv_file.getvalue())
```
