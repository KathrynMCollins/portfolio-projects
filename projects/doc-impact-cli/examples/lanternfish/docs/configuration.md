# Configuration

Lanternfish reads `lantern.yaml` from the folder it starts in.

## Batching

| Key | Default | Description |
|:--|:--|:--|
| `batch_size` | 100 | Events sent in one request. The maximum is 500. |
| `flush_interval_sec` | 5 | Seconds to wait before sending a partial batch. |

## Inputs

List each file or glob under `inputs`. Lanternfish follows rotated files automatically.
