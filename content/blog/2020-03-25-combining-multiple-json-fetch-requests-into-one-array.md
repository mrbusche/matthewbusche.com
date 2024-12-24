---
title: 'Combining multiple json fetch requests into one array'
date: 2020-03-25 21:04:30
tags:
  - json
  - fetch
  - flat
  - promise
---

Have been working on a project where I need to combine multiple JSON files into one array. The code below will take an array of URLs and combine them into one array.

Once all the fetch requests have been completed and converted to json you'll have an equal number of arrays. Using `Array.prototype.flat()` combines all the arrays into a single array.

    let finalResult;
    const urls = ['a', 'b', 'c', 'd', 'e', 'f', 'g'];
    Promise.all(
    urls.map(url =>
        fetch('json/' + url + '.json')
            .then(e => e.json())
        )
    ).then(data => {
        finalResult = data.flat();
    });
