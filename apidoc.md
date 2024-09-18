# Release Notes - Version 2.5.0

## Release Date: September 18, 2024

### New Features
- **Premium Listings API**: 
  - Introduced a new API endpoint `/api/v4/locations/{locationId}/listings/premium` to fetch premium listings for a specific location.
  - The API returns detailed information about the listing's synchronization status, display status, and whether any user action is required.

- **Sync Status Enhancements**:
  - Improved sync tracking with new statuses such as `REQUIRING_ACTION`, `PENDING_APPROVAL`, and `COMPLETED` for better transparency of listing syncs.

### Improvements
- **Display Status Updates**:
  - Enhanced the `displayStatus` field with more informative messages such as `Awaiting location approval`, `Submitting to Partner`, and `Information submitted to partner; awaiting response`.

- **Action Required Field**:
  - New `actionRequired` flag added to listings, allowing users to quickly identify when manual action is necessary.

### Bug Fixes
- **Resolved Sync Failures**:
  - Fixed an issue where listing syncs were getting stuck in `IN_PROGRESS` due to intermittent partner connection issues.

# Get Premium Listings for a Location

This API fetches all the premium listings for a specified location. The location is identified by a unique ID. For example, the location ID used here is `TG9jYXRpb246MTI0MjE=`.

## API Request

- **Method**: `GET`
- **URL**: `/api/v4/locations/{locationId}/listings/premium`
  - Replace `{locationId}` with the actual location ID, such as `TG9jYXRpb246MTI0MjE=`.
  
### Example Request

```http
GET /api/v4/locations/TG9jYXRpb246MTI0MjE=/listings/premium
```

API Response
------------

The response contains information about premium listings for the specified location.

### Example Response

```
{
  "data": {
    "listingsForLocation": [
      {
        "id": "536970351",
        "site": {
          "id": "U2l0ZTo1MA==",
          "name": "Judys Book",
          "url": "judysbook.com"
        },
        "syncStatus": "IN_PROGRESS",
        "displayStatus": "Submitting to Partner",
        "actionRequired": false,
        "listingUrl": null,
        "syncIssue": null
      },
      {
        "id": "315554706",
        "site": {
          "id": "U2l0ZToxODI=",
          "name": "Bing",
          "url": "www.bing.com"
        },
        "syncStatus": "IN_PROGRESS",
        "displayStatus": "Information submitted to partner; awaiting response",
        "actionRequired": false,
        "listingUrl": null,
        "syncIssue": null
      }
    ]
  }
}
```

### Response Fields

| Field | Description |
| --- | --- |
| `id` | Unique identifier for the listing. |
| `site` | Contains details about the site where the listing exists, including site `id`, `name`, and `url`. |
| `syncStatus` | The current synchronization status of the listing (see `syncStatus` values below). |
| `displayStatus` | Describes the current state of the listing as shown to the user (see `displayStatus` values below). |
| `actionRequired` | Indicates if the user needs to take any action (`true` means action is required, `false` means no action is required). |
| `listingUrl` | The live URL of the synced listing (if available). |
| `syncIssue` | Describes any issues related to syncing (if any). |

### `syncStatus` Field

The `syncStatus` field indicates the current synchronization status of each listing. Below are the possible values:

| Value | Description |
| --- | --- |
| `IN_PROGRESS` | The listing sync is currently in progress. |
| `SYNCED` | The listing has been successfully synced. The `listingUrl` field will contain the live listing URL. |
| `FAILED` | The listing sync has failed. |
| `REQUIRING_ACTION` | The listing requires manual action to start syncing. |
| `AVAILABLE` | The listing is available for syncing. |
| `COMPLETED` | The listing sync has been completed. |
| `PENDING_APPROVAL` | The listing sync will proceed after approval. Contact customer support in case of any issues. |

### `displayStatus` Field

The `displayStatus` field provides more details on the current state of the listing as displayed to the user. Below are the possible values:

| Value | Description |
| --- | --- |
| `Awaiting location approval.` | The listing is waiting for the location approval. |
| `Submitting to Partner.` | The listing information is being submitted to a partner site. |
| `Partner experiencing issues; awaiting response.` | The partner site is having issues, and the listing is awaiting a response. |
| `Information submitted to partner; awaiting response.` | The listing information has been submitted, awaiting a response from the partner. |
| `Awaiting partner geo-code.` | The listing is waiting for the partner to return the geo-code. |
| `Facebook page connected to the account is not accessible. Please reconnect.` | The Facebook page connected to the listing is inaccessible; reconnection is needed. |
| `Insufficient permissions for Facebook page connected to the account. Please reconnect.` | There are insufficient permissions for the Facebook page, reconnection is required. |
| `Connection to the account has expired and requires renewal.` | The connection to the listing's account has expired and requires renewal. |
| `Listing connected with the GMB group is not accessible. Please reconnect.` | The Google My Business (GMB) listing is inaccessible and needs reconnection. |
| `Synced.` | The listing has been successfully synced. |
| `Listing Sync Failed.` | The listing synchronization has failed. |
| `Listing Sync In Progress.` | The listing synchronization is currently in progress. |
| `Verification Pending.` | The listing is awaiting verification. |
| `Connect your account to sync the listing.` | The listing requires an account connection to initiate syncing. |

### Action Required Field

The `actionRequired` field indicates whether the user needs to take action for the listing. The possible values are:

| Value | Description |
| --- | --- |
| `true` | User action is required to proceed. |
| `false` | No action is required from the user. |

### Notes

-   **Verified Listings**: The API response can include information about Google listings, which have an additional `verified` field to indicate whether the listing is verified (`true`) or not (`false`).
-   **Sync Issues**: If any issue occurs during the sync process, details will be populated in the `syncIssue` field for each listing.
