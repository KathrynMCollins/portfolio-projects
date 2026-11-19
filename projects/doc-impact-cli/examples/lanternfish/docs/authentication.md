# Authenticate to the cloud sink

The cloud sink accepts one method: an API token.

## Create a token

Create a token in the cloud console under **Settings > Tokens**.

## Add the token to your configuration

```yaml
sink:
  type: cloud
  token: ${LANTERNFISH_TOKEN}
```

Keep the token in an environment variable, not in the file itself.
