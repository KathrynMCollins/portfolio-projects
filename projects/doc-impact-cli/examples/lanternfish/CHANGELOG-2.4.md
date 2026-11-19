# Lanternfish 2.4.0

## Changed

- Renamed the `flush_interval_sec` setting to `flush_interval_seconds`. The old key still
  works as an alias and logs a deprecation warning.
- Raised the maximum `batch_size` from 500 to 2000 events.
- Refactored the internal send buffer as a ring buffer. No settings or output change.

## Added

- The cloud sink now supports OAuth 2.0 client credentials as well as API tokens. Set
  `auth.method: oauth` with `auth.client_id` and `auth.client_secret`. Released in 2.4.0.
- Windows on ARM builds, published to the beta channel only. Not yet in the stable installer.

## Removed

- Removed the `--follow` flag from `lanternfish tail`. Use `lanternfish watch` instead.

## Fixed

- Fixed a spelling mistake in the startup log line.
