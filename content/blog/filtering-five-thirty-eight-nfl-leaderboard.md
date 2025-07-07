---
title: "Filtering FiveThirtyEight's NFL Forecasting Leaderboard"
date: 2018-09-30 20:06:43
permalink: /2018/09/30/filtering-five-thirty-eight-nfl-leaderboard/
tags:
  - FiveThirtyEight
  - NFL Forecast
---

A group of friends and I have a contest going on FiveThirtyEight's [NFL Forecasting Game](https://projects.fivethirtyeight.com/2018-nfl-forecasting-game/leaderboard/) Leaderboard and they don't allow group functionality, so at the end of each week I <kbd>Ctrl + F</kbd> on the page to find each of our name's and update a spreadsheet. Instead of spending 3 minutes once a week I decided to spend 15 minutes and write something that will do it for me.

Just replace the `names` array with a list of the names in your group

    const table = document.getElementById('leaderboard-table-wrap').getElementsByTagName('tr');
    Array.from(table).forEach(function(item) {
      const names = ['Matt Busche', 'Random Dude'];
      if (names.indexOf(item.getElementsByClassName('name')[0].textContent) === -1) {
        item.closest('tr').remove();
      }
    });

As always you can use a [Bookmarklet Creator](https://mrcoles.com/bookmarklet/) to add this as a "bookmark" on your address bar to make filtering super easy.

Note: If you can't find a person, each person needs to acknowledge that they want to publically post their score by visiting the leaderboard page and clicking a link.
