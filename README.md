# API Documentation Setup Guide

---

## Workflow:

### YAML Management
- All API documentation components are stored in a GitHub repository.
- Each API component (e.g., Locations, Listings, User Management) has its own YAML file, making it easier to manage updates individually.

### Automatic Updates via GitHub Actions
- When a writer updates a YAML file and commits to the GitHub repository, GitHub Actions are triggered.
- The workflow in GitHub Actions executes a script that:
  - Calls the relevant Apidog API.
  - Updates the YAML file in all projects within Apidog.
- This ensures that changes made in the YAML are reflected across all project documentation instantly.

### Steps for Updating API Documentation:

#### Content Writer’s Action:
1. Open the specific component YAML file in GitHub.
2. Update the necessary content (e.g., endpoints, descriptions, examples).
3. Commit the changes to the repository.

#### Background process:
1. GitHub Actions detect the change.
2. A script is executed, calling the Apidog API/ Playwright actions to update the relevant project documentation.
3. Documentation is updated across all whitelabeled projects automatically.

---

### Handling New Components
- If a new component YAML file is created:
  - The content writer creates the new YAML file in the GitHub repository.
  - Upon committing the new file, GitHub Actions trigger an update across all projects in Apidog, adding the new component documentation to every project.

---

### Creating a New Whitelabeled Project
1. When a client requests API documentation, the following steps occur:
   - A Playwright script is triggered to:
     1. Create a new project for the client in Apidog.
     2. Store the newly generated Project ID in our system.
     3. Upload all YAML files to Apidog for the project.

2. In the Synup platform:
   - A new custom domain screen will be introduced (similar to Agency or Scantool settings) where the API documentation's custom domain can be added.
   - The custom domain is set up for the project in Apidog:
     - The custom domain is tied to the base settings under the project, so there's only one underlying API document, ensuring that updates are applied across all clients.
     - Apidog provides a CNAME, which is displayed to the client.
     - The client configures their DNS with the CNAME for their custom domain.

---

### Handling Delinquent Accounts
- If an account becomes delinquent, the system automatically unpublishes the API documentation for that account.
- This is managed through a Playwright script that interacts with Apidog and removes the API documentation when triggered by account status changes.

---

### Handling Logo and Company Name Updates:
- **Updating Branding:**
  - If a client updates their logo or company name (and they have previously requested API documentation), the Playwright script will be triggered to:
    - Update the logo and company name details in Apidog automatically.

---

### Handling Script Failures by Setting Up Slack Notifications & Retries
- Notification on Slack after 2 retries.

---

## Key Concepts:
- **Main Public API Documentation:** This Synup API documentation is visible to the public.
- **Whitelabeled API Documentation:** Custom API documentation projects with branding adjustments.
- **Component-wise YAML Files:** API documentation is organized into component-specific YAML files, maintained in GitHub.
