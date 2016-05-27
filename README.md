## ghettoDNS
justin parus

### what it does
* pulls public ip and emails it using smtp
* uses correct msg format and can send to multiple recipients

### plan to improve
* run using APScheduler to check ip daily and only send when it changes
  - first use blocking scheduler
  - then use background scheduler
* implement as a proper daemon

### additional notes
* if using gmail smpt must change account security setting to allow 'less secure apps' to sign in
* can be modified to use SSL if preferred over TLS
