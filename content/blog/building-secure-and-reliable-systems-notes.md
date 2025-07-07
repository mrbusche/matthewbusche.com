---
title: Building Secure and Reliable Systems Notes
date: 2020-04-21 21:01:30
permalink: /2020/04/21/building-secure-and-reliable-systems-notes/
tags:
  - sre
  - google
---

Google released a new book, [Building Secure and Reliable Systems](https://landing.google.com/sre/books/) and it's pretty good. Everyone will want to read the first couple chapters and then after that skim the other chapters. There are tons of headers throughout the book (every other page on average), so you can easily skip to what sounds interesting.

### Reliability and Security Tradeoff: Incident Management

- You'll often want to handle security incidents with the smallest number of people who can fix the problem effectively, so the adversary isn't tipped off to the recovery effort.

### Least Privilege

- The objective of least privilege should extend through all authentication and authorization layers of the system
- Users should have the minim access needed to do their job
- This also applies to database users, you probably only need `INSERT`, `UPDATE`, and `SELECT` access in production

### Classify access based on risk

A company may need three classifications: public, sensitive, and highly sensitive.

- Public - open to anyone in the company
- Sensitive - Limited to groups with business purpose
- Highly sensitive - no permanent access

### Keep Dependencies Up to Date and Rebuild Frequently

If your dependencies are up to date, it's likely you can apply a critical patch directly instead of needing to merge with a backlog of changes or apply multiple patches.

New releases and their security patches won't make it into your environment until you rebuild. Frequently rebuilding and redeploying your environment means that you'll be ready to roll out a new version when you need to—and that an emergency rollout can pick up the latest changes

### Release Frequently Using Automated Testing

Basic SRE principles recommend cutting and rolling out releases regularly to facilitate emergency changes. By splitting one large release into many smaller ones, you ensure that each release contains fewer changes, which are therefore less likely to require rollback. For a deeper exploration of this topic, see the "virtuous cycle" depicted in [Figure 16-1 in the SRE workbook](https://landing.google.com/sre/workbook/chapters/canarying-releases/#the-virtuous-cycle-of-ci-cd).

When each release contains fewer code changes, it's easier to understand what changed and pinpoint potential issues. When you need to roll out a security change, you can be more confident about the expected outcome

### Use Containers

As these changes roll out to each task, the system seamlessly moves serving traffic to another instance; see "Case Study 4: Running Hundreds of Microservices on a Shared Platform" in [Chapter 7 of the SRE book](https://landing.google.com/sre/workbook/chapters/simplicity/). You can achieve similar results and avoid downtime while patching with blue/green deployments; see Chapter 16 in the SRE workbook.

To reduce the need for this kind of ad hoc patching, you should monitor the age of containers running in production and redeploy regularly enough to ensure that old containers aren't running. Similarly, to avoid redeploying older, unpatched images, you should enforce that only recently built containers can be deployed in production.

### SQL Injection Vulnerabilities

In Java Use the Error Prone code checker, which provides a @CompileTimeConstant annotation for parameters.

### Automated Code Inspection Tools

Error Prone for Java and Clang-Tidy for C/C++ are widely used across projects at Google. Both of these analyzers allow engineers to add custom checks. For certain types of bugs, both Error Prone and Clang-Tidy can produce suggested fixes.

### Debugging Techniques

Debugging is a skill that you can learn and practice. Chapter 12 of the SRE book offers two requirements for successful debugging:

- Know how the system is supposed to work.
- Be systematic: collect data, hypothesize causes, and test theories.

### Debugging: Record your observations and expectations

Write down what you see. Separately, write down your theories, even if you've already rejected them. Doing so has several advantages:

- It introduces structure to the investigation and helps you remember the steps you took during your investigation. When you start debugging, you don't know how long it will take to solve the issue—resolution might take five minutes or five months.
- Another debugger can read your notes, understand what you observed, and quickly participate in or take over the investigation. Your notes can help teammates avoid duplicative work, and may inspire others to think of new avenues for investigation. For more on this topic, see "Negative Results Are Magic" in Chapter 12 of the SRE book.
- In the case of potential security issues, it can be helpful to keep a log of each access and investigation step. Later, you may need to prove (sometimes in a court of law) which actions were performed by the attacker and which were performed by investigators

### Distinguish horses from zebras

When you hear hoofbeats, do you first think of horses, or zebras? Instructors sometime pose this question to medical students learning how to triage and diagnose diseases. It's a reminder that most ailments are common — most hoofbeats are caused by horses, not zebras. You can imagine why this is helpful advice for a medical student: they don't want to assume symptoms add up to a rare disease when, in fact, the condition is common and straightforward to remedy

### Reread the docs

After they found the warning message, they determined that it wasn't a zebra, it was a horse - their code had never worked.

### Debugging: Take a break

Giving yourself a bit of distance from an issue can often lead to new insights when you return to the problem. If you've been working heads-down on debugging and hit a lull, take a break: drink some water, go outside, get some exercise, or read a book. Bugs sometimes make themselves evident after a good sleep

### Security is a Team Responsibility

One example of this in practice is the way the team approaches security bugs. All engineers, including security team members, fix bugs and write code. If security teams only find and report bugs, they may lose touch with how hard it is to write bug-free code or fix bugs. This also helps mitigate the "us" versus "them" mentality that sometimes arises when security engineers don't contribute to traditional engineering tasks.

### Who Is Responsible for Security and Reliability?

Who works on security and reliability in a given organization? We believe that security and reliability should be integrated into the lifecycle of systems; therefore, they're everyone's responsibility. We'd like to challenge the myth that organizations should place the burden for these concerns solely on dedicated experts.

We encourage organizations to make reliability and security the responsibility of everyone: developers, SREs, security engineers, test engineers, tech leads, managers, project managers, tech writers, executives, and so on. That way, the nonfunctional requirements described in Chapter 4 become a focus for the whole organization throughout a system's entire lifecycle

### Reduce Fear with Risk-Reduction Mechanisms

Here are some strategies you might want to try:

- Canaries and staged rollouts
  - You can reduce fear by slowly rolling out substantial changes through small canary groups of users or systems. That way, the blast radius of an ill-fated change is small if something goes wrong.
  - Also consider going one step further, and implementing all changes via staged rollouts and canaries (see Chapter 16 in the SRE workbook). In practice, this approach has numerous benefits. For example, in Chapter 19 we discuss how the staged release cycle for Chrome balances the competing needs of speedy updates and reliability. Over time, Chrome's staged releases have fostered its reputation as a secure browser.
  - We've also found that by making staged rollouts part of a routine change process, over time, an organization comes to expect that care and diligence are applied to all changes — which builds confidence in change and reduces fear.

Dog‐fooding (or "eating your own dogfood") involves adopting a change before that change affects others. This is especially important if you're affecting the systems and processes that impact people's daily lives.

Opt in before mandatory

- A corollary to the dogfood and trusted tester strategies is making a new control optional before it becomes mandatory. This gives teams the opportunity to adopt changes on their own timeline. Complicated changes, such as new authorization controls or testing frameworks, have a cost; it can take time for an organization to fully adopt such changes, and you often need to balance these changes against other priorities. If teams know they have time to implement changes at their own pace, they may be less resistant to doing so.

### Overcommunicate and Be Transparent

When advocating for change, the means of communication can influence outcomes. As we discuss in Chapters 7 and 19, good communication is key to building buy-in and confidence in success. Giving people information and clear insight into how change is happening can reduce fear and build trust. We've found the following strategies to be successful:

- Document decisions
- When making a change, clearly document why it's happening, what success looks like, how the change will be rolled back if operating conditions deteriorate, and who to talk to in case of concerns.
- Create feedback channels
- Use dashboards
- Write frequent updates
