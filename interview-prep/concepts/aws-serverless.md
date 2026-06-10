# AWS Serverless Stack

A standard AWS serverless architecture combining API Gateway, Lambda, DynamoDB, S3, CloudFront, and Cognito to serve web and mobile clients. Designed as an on-ramp that stays modular enough to migrate to ECS/EKS when needed.

---

## Architecture

```
       ┌──────────┐     ┌──────────┐
       │   Web    │     │  Mobile  │
       │(Vercel/  │     │(Expo EAS)│
       │ Amplify) │     └────┬─────┘
       └────┬─────┘          │
            └────────┬───────┘
                     ↓
              ┌────────────┐       ┌──────────────┐
              │ API Gateway │──────▶│ AWS Lambda   │
              └────────────┘       └──────────────┘
                     │
          ┌──────────┼──────────┐
          ↓          ↓          ↓
    ┌──────────┐ ┌────────┐ ┌──────────┐
    │ DynamoDB │ │   S3   │ │ Cognito  │
    │(content) │ │(media) │ │  (auth)  │
    └──────────┘ └────────┘ └──────────┘
          │
    CloudFront CDN
```

---

## Components

| Component | Role |
|-----------|------|
| API Gateway | HTTP API entry point; handles CORS, throttling, auth |
| Lambda (Node.js / Python) | Stateless business logic handlers |
| DynamoDB | Single-table design (PK/SK); `PAY_PER_REQUEST` billing |
| S3 | Binary/media asset storage |
| CloudFront | CDN in front of S3; edge caching for static assets |
| Cognito | User Pool with email sign-in; app client for mobile |
| GitHub Actions | CI/CD: deploy Lambdas via AWS SAM or Serverless Framework |

---

## CDK Boilerplate (TypeScript)

Key patterns when provisioning with `aws-cdk-lib` v2.90+:

```typescript
// DynamoDB
const table = new Table(this, 'AppTable', {
  billingMode: BillingMode.PAY_PER_REQUEST,
  removalPolicy: RemovalPolicy.DESTROY,  // dev only
  partitionKey: { name: 'PK', type: AttributeType.STRING },
  sortKey: { name: 'SK', type: AttributeType.STRING },
});

// Cognito
const userPool = new UserPool(this, 'UserPool', {
  selfSignUpEnabled: true,
  signInAliases: { email: true },
});

// Lambda
const fn = new NodejsFunction(this, 'Handler', {
  entry: 'lambda/handlers/index.ts',
});

// S3 with CORS (dev)
const bucket = new Bucket(this, 'MediaBucket', {
  cors: [{ allowedMethods: [HttpMethods.GET, HttpMethods.PUT], allowedOrigins: ['*'] }],
});
```

---

## Rollout Sequence (5 days)

1. **AWS foundation** — IAM, DynamoDB, S3, CloudFront
2. **APIs** — Lambda + API Gateway + Cognito
3. **Frontend integration** — web (Vercel/Amplify) + mobile (Expo EAS)
4. **CI/CD** — GitHub Actions pipelines
5. **Monitoring** — CloudWatch dashboards, alarms, DAX if needed

---

## Best Practices

- Test APIs with Postman/Insomnia before connecting frontend
- Keep infra modular to enable future ECS/EKS migration
- Use CDK/CloudFormation to track all infra changes — no manual console changes
- Update IAM scopes to least-privilege before production
- Use Lambda Layers for shared dependencies to reduce cold start size
- Set reserved concurrency on critical Lambdas to prevent throttling

---

## Trade-offs vs Container-Based

| Dimension | Serverless (Lambda) | Containers (ECS/EKS) |
|-----------|--------------------|-----------------------|
| Cold starts | Yes (mitigate with provisioned concurrency) | No |
| Ops burden | Low | High |
| Long-running tasks | Not suitable (15 min max) | Suitable |
| Cost at scale | Can get expensive at high volume | More predictable |
| Vendor lock-in | Higher | Lower |
| Local dev | Harder to replicate | Docker Compose |

## Related

- `phases/phase-4.md` — Cloud Infrastructure study schedule (covers ECS, EKS, Terraform)
- `interview-prep/concepts/fullstack-architecture.md` — full layer map including serverless
