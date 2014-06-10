# Ruby Encoder

Adds an encoding comment to the top of every valid Ruby, if it doesn't already have it.  That's it.

```
# encoding: utf-8
```

## Configuring

You may configure two things:

- The valid ruby extension(s) that should get the encoding comment.  By default, this is `*.rb`.
- The actual encoding.  By default this is `utf-8`.

See Preferences -> Package Settings -> Ruby Encoder -> Default Settings for more information.
