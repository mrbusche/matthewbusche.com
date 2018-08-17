---
id: 285
title: Filtering Amazon Wishlist items with price drops
redirect_from:
  - /blog2/2017/05/27/filtering-amazon-wishlist-items-with-price-drops/
date: 2017-05-27T02:31:29+00:00
author: mrbusche
layout: post
permalink: /2017/05/27/filtering-amazon-wishlist-items-with-price-drops/
categories:
  - JavaScript
tags:
  - amazon wishlist
---

Amazon has recently changed their filters on wish list items so you can no longer view items with price drops (useful for books) or sort price from low to high. I wrote up some fairly crappy JavaScript that scrolls to the end of your wish list then removes all the items that don&#8217;t have &#8220;Price dropped&#8221; in the div. I sometimes need to run the code more than once to get all items to be removed, so this is far from perfect, but works for what I was intending it to do. If you have a few hundred items on your list it will take a few seconds to run the script, but each subsequent run should run pretty quick.

Update: I added this to [github](https://github.com/mrbusche/amazonPriceDrops).

<pre>function removeItemsWithoutPriceDrops() {
  var lowPrice = 999999;
  var anyRemoved = false;
  var listItems = document.getElementsByClassName('a-spacing-none g-item-sortable');

  for (var i = 0; i &lt; listItems.length; i++) { var priceDrop = listItems[i].querySelectorAll('.itemPriceDrop'); var price = listItems[i].querySelectorAll('span.a-offscreen'); if (price.length) { price = price[0].innerHTML; price = price.replace('$', ''); } else { price = 0; } if (priceDrop.length == 0 || price &gt; lowPrice) {
      listItems[i].parentElement.removeChild(listItems[i]);
      anyRemoved = true;
    }
  }

  if (anyRemoved) {
    removeItemsWithoutPriceDrops();
  }
}

removeItemsWithoutPriceDrops();
</pre>

You can also add the following code directly to a bookmark by copy and pasting the code into this [generator](https://mrcoles.com/bookmarklet/).

You can also copy this exact code into a new bookmark

    javascript:(function()%7Bfunction removeItemsWithoutPriceDrops() %7Bvar lowPrice %3D 999999%3Bvar anyRemoved %3D false%3Bvar listItems %3D document.getElementsByClassName('a-spacing-none g-item-sortable')%3Bfor (var i %3D 0%3B i &lt; listItems.length%3B i%2B%2B) %7Bvar priceDrop %3D listItems%5Bi%5D.querySelectorAll('.itemPriceDrop')%3Bvar price %3D listItems%5Bi%5D.querySelectorAll('span.a-offscreen')%3Bif (price.length) %7Bprice %3D price%5B0%5D.innerHTML%3Bprice %3D price.replace('%24'%2C '')%3B%7D else %7Bprice %3D 0%3B%7Dif (priceDrop.length %3D%3D 0 %7C%7C price &gt; lowPrice) %7BlistItems%5Bi%5D.parentElement.removeChild(listItems%5Bi%5D)%3BanyRemoved %3D true%3B%7D%7Dif (anyRemoved) %7BremoveItemsWithoutPriceDrops()%3B%7D%7DremoveItemsWithoutPriceDrops()%7D)()

If you&#8217;re having issues with your wishlist loading in all items you need to add `?sort=universal-price` to your URL. For example <https://www.amazon.com/gp/registry/wishlist/153OV2P85MJD6/?sort=universal-price>
