# knowledge_base.py
# Microsoft Support Knowledge Base
# Official Microsoft Learn resources

MICROSOFT_ARTICLES = {
    "Entra ID": {
        "Password / MFA": [
            {"title": "How to troubleshoot Microsoft Entra sign-in errors", "url": "https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-troubleshoot-sign-in-errors"},
            {"title": "How to investigate sign-ins requiring Microsoft Entra MFA", "url": "https://learn.microsoft.com/en-us/entra/identity/monitoring-health/scenario-health-sign-ins-mfa"},
            {"title": "Troubleshoot Azure Multi-Factor Authentication issues", "url": "https://learn.microsoft.com/en-us/troubleshoot/entra/entra-id/mfa/troubleshoot-azure-mfa-issue"},
        ],
        "Authentication": [
            {"title": "How to troubleshoot Microsoft Entra sign-in errors", "url": "https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-troubleshoot-sign-in-errors"},
            {"title": "How to investigate sign-ins requiring Microsoft Entra MFA", "url": "https://learn.microsoft.com/en-us/entra/identity/monitoring-health/scenario-health-sign-ins-mfa"},
        ],
        "Configuration": [
            {"title": "Enable Microsoft Entra multifactor authentication", "url": "https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa"},
        ],
    },
    "Licensing": {
        "Configuration": [
            {"title": "Assign or unassign licenses for users in the Microsoft 365 admin center", "url": "https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/license-users-groups"},
            {"title": "Assign or unassign licenses to a group", "url": "https://learn.microsoft.com/en-us/azure/active-directory/active-directory-licensing-group-advanced"},
        ],
        "Authentication": [
            {"title": "Assign or unassign licenses for users in the Microsoft 365 admin center", "url": "https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/license-users-groups"},
        ],
    },
    "Intune": {
        "Configuration": [
            {"title": "Troubleshooting device enrollment in Intune", "url": "https://learn.microsoft.com/en-us/troubleshoot/mem/intune/device-enrollment/troubleshoot-device-enrollment-in-intune"},
            {"title": "Microsoft Intune troubleshooting", "url": "https://learn.microsoft.com/en-us/troubleshoot/mem/intune/welcome-intune"},
        ],
        "Authentication": [
            {"title": "Troubleshooting device enrollment in Intune", "url": "https://learn.microsoft.com/en-us/troubleshoot/mem/intune/device-enrollment/troubleshoot-device-enrollment-in-intune"},
        ],
        "Access / Permissions": [
            {"title": "Troubleshoot Windows device access for school or work", "url": "https://learn.microsoft.com/en-us/intune/user-help/troubleshooting/troubleshoot-device-access-windows"},
        ],
    },
    "OneDrive": {
        "Synchronization": [
            {"title": "Resolve sync issues in OneDrive for work or school", "url": "https://learn.microsoft.com/en-us/troubleshoot/sharepoint/sync/troubleshoot-sync-issues"},
        ],
        "Storage": [
            {"title": "Resolve sync issues in OneDrive for work or school", "url": "https://learn.microsoft.com/en-us/troubleshoot/sharepoint/sync/troubleshoot-sync-issues"},
        ],
        "Access / Permissions": [
            {"title": "Access Denied error when accessing a shared folder", "url": "https://learn.microsoft.com/en-us/troubleshoot/sharepoint/sharing-and-permissions/access-denied-shared-folder"},
        ],
    },
    "SharePoint": {
        "Performance": [
            {"title": "SharePoint Online performance troubleshooter", "url": "https://learn.microsoft.com/en-us/troubleshoot/sharepoint/performance/sharepoint-online-performance-troubleshooter"},
        ],
        "Access / Permissions": [
            {"title": "Unable to access SharePoint Online", "url": "https://learn.microsoft.com/en-us/troubleshoot/sharepoint/administration/sharepoint-online-inaccessible"},
            {"title": "Access Denied error when accessing a shared folder", "url": "https://learn.microsoft.com/en-us/troubleshoot/sharepoint/sharing-and-permissions/access-denied-shared-folder"},
        ],
        "Synchronization": [
            {"title": "Resolve sync issues in OneDrive for work or school", "url": "https://learn.microsoft.com/en-us/troubleshoot/sharepoint/sync/troubleshoot-sync-issues"},
        ],
    },
    "Teams": {
        "Connectivity": [
            {"title": "Troubleshoot connectivity issues with Teams client", "url": "https://learn.microsoft.com/en-us/microsoftteams/connectivity-issues"},
            {"title": "Monitor and troubleshoot Teams meetings and calls", "url": "https://learn.microsoft.com/en-us/microsoftteams/monitor-troubleshoot-teams-meetings-calls"},
        ],
        "Performance": [
            {"title": "Monitor and troubleshoot Teams meetings and calls", "url": "https://learn.microsoft.com/en-us/microsoftteams/monitor-troubleshoot-teams-meetings-calls"},
        ],
        "Configuration": [
            {"title": "Monitor and troubleshoot Teams meetings and calls", "url": "https://learn.microsoft.com/en-us/microsoftteams/monitor-troubleshoot-teams-meetings-calls"},
        ],
    },
    "Exchange Online": {
        "Connectivity": [
            {"title": "Microsoft 365: Outlook and mobile device connectivity troubleshooting resources", "url": "https://learn.microsoft.com/en-us/troubleshoot/exchange/outlook-issues/office-365-troubleshooting-resources"},
        ],
        "Authentication": [
            {"title": "Microsoft 365: Outlook and mobile device connectivity troubleshooting resources", "url": "https://learn.microsoft.com/en-us/troubleshoot/exchange/outlook-issues/office-365-troubleshooting-resources"},
        ],
        "Configuration": [
            {"title": "Microsoft 365: Outlook and mobile device connectivity troubleshooting resources", "url": "https://learn.microsoft.com/en-us/troubleshoot/exchange/outlook-issues/office-365-troubleshooting-resources"},
        ],
    },
    "Outlook": {
        "Authentication": [
            {"title": "Microsoft 365: Outlook and mobile device connectivity troubleshooting resources", "url": "https://learn.microsoft.com/en-us/troubleshoot/exchange/outlook-issues/office-365-troubleshooting-resources"},
        ],
        "Connectivity": [
            {"title": "Microsoft 365: Outlook and mobile device connectivity troubleshooting resources", "url": "https://learn.microsoft.com/en-us/troubleshoot/exchange/outlook-issues/office-365-troubleshooting-resources"},
        ],
        "Performance": [
            {"title": "Microsoft 365: Outlook and mobile device connectivity troubleshooting resources", "url": "https://learn.microsoft.com/en-us/troubleshoot/exchange/outlook-issues/office-365-troubleshooting-resources"},
        ],
    },
}

def get_microsoft_articles(category, issue_type):
    """Return up to three relevant Microsoft Learn articles."""
    category_articles = MICROSOFT_ARTICLES.get(category, {})

    if issue_type in category_articles:
        return category_articles[issue_type]

    all_articles = []
    for articles in category_articles.values():
        all_articles.extend(articles)

    unique_articles = []
    seen_urls = set()

    for article in all_articles:
        if article["url"] not in seen_urls:
            unique_articles.append(article)
            seen_urls.add(article["url"])

    return unique_articles[:3]
