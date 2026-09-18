# Local Intentionally Vulnerable Lab Setup

## 1. Lab Objective

Provide a deliberately vulnerable environment for controlled security learning while preserving a strict boundary around authorized systems.

## 2. Approved Lab Assets

| Asset | Address | Environment |
|---|---|---|
| LAB-01 | http://127.0.0.1:8080 | Isolated localhost |
| LAB-02 | 192.168.56.20 | Private host-only network |

These values match the supplied authorized-lab-assets.csv.

## 3. Isolation Controls

- Keep LAB-01 local to the training environment.
- Keep LAB-02 on a private host-only network.
- Do not expose the lab to the public Internet.
- Do not bridge the vulnerable VM into a production or shared network.
- Prevent outbound traffic from LAB-02.
- Take a snapshot/backup before testing.
- Use synthetic training data and lab-only credentials.

## 4. Test Identities

Use dedicated training identities only. Never reuse personal, college, work or production credentials.

Example roles:
- student-user
- student-reviewer
- student-admin

These are illustrative lab identities, not real accounts.

## 5. Pre-Test Safety Checklist

- [ ] Written authorization completed.
- [ ] LAB-01 and LAB-02 confirmed as the only approved targets.
- [ ] Lab isolation verified.
- [ ] Outbound traffic controls verified for LAB-02.
- [ ] Test window confirmed.
- [ ] Emergency contact confirmed.
- [ ] Rate limits understood.
- [ ] No real sensitive data is present.
- [ ] Snapshot/backup available.
- [ ] Stop conditions reviewed.

## 6. Post-Test Checklist

- [ ] Testing stopped at the approved end time.
- [ ] Findings recorded with required reporting fields.
- [ ] Evidence sanitized.
- [ ] Confidential evidence stored securely.
- [ ] Unnecessary evidence deleted at the defined time.
- [ ] Temporary lab credentials removed or rotated.
- [ ] Lab restored if required.
- [ ] Scope and ROE reviewed for lessons learned.
