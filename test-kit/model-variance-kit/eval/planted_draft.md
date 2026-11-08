# Configure alert enrichment

Alert enrichment adds context to incoming alerts — owner, service, and region — before correlation runs. It is designed to make incidents easier to route.

Let's take a look at how it works. Enrichment rules match tag values and add new tags. Rules are robust and run in order. It's important to note that a change to a rule applies to new alerts only.

You need Admin permissions to edit enrichment rules. The Harness integration also sends tags that rules can match, e.g. a deployment ID.

To create a rule:

1. Open the **Enrichment** page.
2. You click **New Rule**.
3. Enter a tag name and a match condition. The rule takes effect in 5–10 minutes.
4. Click **Save**.

By following these steps, you can leverage your existing tags to seamlessly enrich every alert. *Rules are evaluated top to bottom.*

```bash
curl -X GET https://api.example.com/v2.1/enrichments -H "Authorization: Bearer <your_api_key>" --max-time 5-10
```

Read-only users can view rules but cannot edit them.
