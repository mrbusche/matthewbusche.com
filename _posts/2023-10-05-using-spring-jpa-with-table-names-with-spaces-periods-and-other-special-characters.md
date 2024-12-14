---
title: Using Spring JPA with tables names with spaces, periods, and other special characters
date: 2023-10-05 22:09:30
tags:
  - spring
  - jpa
---

Given a non-traditional table name, how do you get Spring JPA to recognize your `@Entity` properly?

If your table name has a period such as `odd.table` You use `@Table(name="[odd].[table]")`

If your table name has a slash such as `odd/table` You use `@Table(name="[odd/table]")`

If your table name has spaces such as `table with spaces` You use `@Table(name="[table with spaces]")`

TL;DR - `[]` are your friend.
