---
id: 57
title: Windows Media Center Reports No Signal when Recording
redirect_from:
  - /blog2/2014/12/09/windows-media-center-reports-no-signal-when-recording/
date: 2014-12-09T03:37:17+00:00
author: mrbusche
permalink: /2014/12/09/windows-media-center-reports-no-signal-when-recording/
categories:
  - windows media center
---

I was having a problem with my local ABC station working when I viewed the channel to watch a show, but every recording was failing saying &#8220;There was no TV signal when the show was scheduled to record&#8221; even if I went to the channel immediately following that error it was working. If I tried to press record on the show as it was playing it would fail and say no signal again. It turns out the problem is the antenna somehow is picking up two sources. I'm not sure why it could play the show live and not record, but here's how I fixed it.

1. Open the Program Guide
2. Right-click the problem channel
3. Choose Edit Channel
4. Choose Edit Sources &#8211; you should see two sources enabled
5. Disable one of them and try the channel again. If that doesn't work disable the other source and try the channel again.

For reference I'm using Windows 7 with an AVerMedia M780 Tuner.
