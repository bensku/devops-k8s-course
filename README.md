# Devops with Kubernetes

## 3.06: DBaaS vs DIY
Based on what I've seen, managed (open source) databases are much more expensive
than self-hosting. The idea, I suppose, is that developer time is expensive,
so any service that requires less of it to manage is often very much worth it.

Installing a database is not difficult in itself - I did it for this course in
half a hour or so. Installing a database that is configured for high throughput
may be a little more difficult. Implementing high availability in face of
arbitrary hardware failures is *tricky* and any failure may make your setup
not-so-available. The latter also goes for backups - calling `pg_dump` is easy,
but you should presumably also test those backups. Add minute- or second-level
point-of-time recovery, and it too becomes very complicated.

Then there are upgrades. Like your application's dependencies, the database
it stores to needs to be kept up to date. Unlike most web applications,
databases typically use persistent disk-based storage. If an update goes
sideways, you'll probably need to rollback from backups (which you surely have?).
Zero-downtime updates often *cannot* be done with just a rolling release, but
require database-specific wrangling.

A good DBA should be able to take care of all this. However, if you lack one,
using a DBaaS service might be more cost-effective than learning-by-doing
everything yourself. Unlike a DBA, it won't tell you why your queries are slow
(let alone fix them for you), but it is better than nothing. Also, if something
goes terribly wrong, chances are the managed database comes with *some* kind of
human-provided support that can help you.

All in all, if there is money on line, I'd *usually* use a managed database.
For hobby projects where I don't care about availability (or pay myself for my time),
self-hosting is the way to go.