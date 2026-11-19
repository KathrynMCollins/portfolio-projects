# Troubleshooting

## Events arrive late

Lanternfish sends a partial batch after `flush_interval_sec` seconds. Lower it to send sooner.

## Requests are rejected as too large

Lower `batch_size`. The sink rejects requests over its size limit.
