# Security evaluation for moving an internal knowledge base to a docs platform

**Type:** Case study: a security and evaluation handoff written for security and leadership reviewers
**When:** September 2026
**Author:** Kathryn Collins
**Tools:** a git-based docs platform (evaluated), an internal wiki, a component content management system
**Prepared for:** Content management and technical writing roles

## What this shows

Turning a tooling proposal into a document a security team can decide on: the scope stated first, each access option with its fit, recommendations with the reason behind them, a checklist that must pass before launch, and the questions only the security team can answer. It also shows a disclosure judgment: it recommends keeping public and internal content on separate platforms, so that nothing reaches the public without human review.

Portfolio note: the vendor, internal space names, domains and team names are generalized.

## The question

The team proposed moving internal-only documentation (release guides and technical guides) from the internal wiki to a git-based docs platform, to bring the docs experience closer to the product. The platform had no connector for the wiki, so the move would be manual: export, inventory, convert and rebuild the navigation. Security needed to sign off before any internal content went live. The public docs site and its publishing pipeline were out of scope.

## Recommendations in the handoff

**Keep public and internal docs on separate platforms.** The platform can mix public and gated pages on one site. Our public docs require a human review step in the publishing system before anything goes live. This platform publishes on merge, so one site for both would risk unreviewed content shipping publicly.

**Require single sign-on before any internal content goes live.**

| Access method | Fit for this use |
| --- | --- |
| Private authentication (organization login) | Baseline: restricts to organization members |
| Password | Recommended against: a shared secret with no per-user audit trail |
| OAuth or SSO tied to our identity provider | Recommended: supports group-based access |
| Signed tokens (JWT) | Only if the docs are embedded behind an existing app with its own login |

Authentication works only on a custom subdomain, not on a path under the main site, so the subdomain had to be confirmed before the build.

**Self-hosting as the target state.** Self-hosting keeps content inside our own infrastructure but takes longer to set up, and some integrations stay cloud-only either way. Given how sensitive some internal content is, I recommended self-hosting as the end state and cloud hosting with SSO only as a time-boxed pilot.

**Treat the source repository as part of the security boundary.** A site marked private does not protect a public repository behind it. The repository had to be private and owned by the organization, the platform's deploy key scoped to that repository only, and branch protection enabled on main. If self-hosted, the repository could stay on a self-managed git server, or sit behind an internally owned proxy if repository credentials could not go to a third party.

**Scope the AI assistant, and review the cloud-only integrations.** The platform's AI assistant can read the internal wiki and chat channels as context; its connections should be scoped to approved spaces, not left open by default. The cloud-only integrations are each a path for data to leave the perimeter, so each needed individual review and approval, or exclusion. Search-engine exclusion (noindex and robots rules) had to be verified during setup, not assumed from authentication being on.

## Pre-launch checklist

The handoff ended with a checklist that had to pass before launch:

- Hosting model confirmed (cloud pilot or self-hosted) and signed off by security
- Repository private, organization-owned, deploy key scoped
- SSO configured against our identity provider; password access disabled
- Custom subdomain confirmed
- Group-based access mapped to the right internal audiences
- Cloud-only integrations reviewed, and disabled unless approved
- The AI assistant's wiki and chat connections scoped to approved spaces, or disabled
- Search-engine exclusion verified before launch
- Content inventory flags sensitive pages for a restricted access tier, with that access group defined and tested

## Open questions handed to security

1. Does this content need self-hosting from day one, or is a time-boxed cloud pilot with SSO acceptable?
2. Which identity provider and group structure should map to the platform's access groups?
3. Who owns approval of the AI assistant's connections to the wiki and chat?

## Limitations

- This is an evaluation and handoff, not a security sign-off. The recommendations in it were for the security team to accept or change.
- The migration had not gone ahead at the time of writing.
