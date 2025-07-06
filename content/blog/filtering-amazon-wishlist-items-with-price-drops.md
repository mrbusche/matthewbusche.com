---
id: 285
title: Filtering Amazon Wishlist items with price drops
date: 2017-05-27T02:31:29+00:00
author: mrbusche
permalink: /2017/05/27/filtering-amazon-wishlist-items-with-price-drops/
categories:
  - javascript
tags:
  - amazon wishlist
---

Amazon has recently changed their filters on wish list items so you can no longer view items with price drops (useful for books) or sort price from low to high. I wrote up some fairly crappy JavaScript that scrolls to the end of your wish list then removes all the items that don't have &#8220;Price dropped&#8221; in the div. I sometimes need to run the code more than once to get all items to be removed, so this is far from perfect, but works for what I was intending it to do. If you have a few hundred items on your list it will take a few seconds to run the script, but each subsequent run should run pretty quick.

Update: I added this to [github](https://github.com/mrbusche/amazonPriceDrops).

Update 2: I created a Spring Boot app that allows you to set your [Amazon wishlist URL and a price drop percentage](https://github.com/mrbusche/amazon-price-checker) or price to alert you on. You'll need to fork the app and update to change values. You'll get emails when your triggers are hit.

```javascript
javascript: (function () {
	function removeItemsWithoutPriceDrops() {
		const lowPrice = 999999;
		const priceDropMin = 1;
		let anyRemoved = false;
		const listItems = document.getElementsByClassName('a-spacing-none g-item-sortable');

		for (var i = 0; i < listItems.length; i++) {
			let priceDropSpan = listItems[i].querySelectorAll('span.a-size-base.a-color-base');
			let priceDrop = priceDropSpan.length > 0 ? priceDropSpan[0].innerText.startsWith('Price dropped') : false;
			let price = priceDrop ? listItems[i].querySelectorAll('span.a-offscreen') : 0;
			let priceDropPercent = priceDropSpan.length > 0 ? priceDropSpan[0].innerText : '';
			priceDropPercent = priceDropPercent.replace('Price dropped', '').replace('% since added', '');
			if (!priceDrop || price > lowPrice || parseInt(priceDropPercent) < priceDropMin) {
				listItems[i].parentElement.removeChild(listItems[i]);
				anyRemoved = true;
			}
		}

		if (anyRemoved) {
			removeItemsWithoutPriceDrops();
		}
	}

	removeItemsWithoutPriceDrops();
})();
```

You can copy and paste the above code directly into a new bookmark.

If you're having issues with your wishlist loading in all items you need to add `?sort=universal-price` to your URL. For example <https://www.amazon.com/gp/registry/wishlist/153OV2P85MJD6/?sort=universal-price>
