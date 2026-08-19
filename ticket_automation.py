"""
AI IT Support Ticket Automation
Clean deployment module extracted from the final Colab pipeline.

This module exposes one main function:
    generate_ticket_response(ticket)
"""

def determine_category(ticket):
    """Final V5 category classification."""
    ticket = ticket.lower()

    # Normalize common product-name variations.
    # "One Drive" and "OneDrive" should be treated identically.
    ticket = ticket.replace("one drive", "onedrive")

    # MFA / authentication -> Entra ID
    # This keeps the public demo consistent with the validated
    # ticket-routing behavior used during the project.
    if any(phrase in ticket for phrase in [
        "mfa",
        "multi-factor",
        "multifactor",
        "reset my mfa",
        "reset mfa",
        "mfa authentication method",
        "mfa method",
        "authentication method"
    ]):
        return "Entra ID"

    # Device enrollment -> Intune
    if "device enrollment" in ticket or "device enrolment" in ticket:
        return "Intune"

    # Licensing
    if any(phrase in ticket for phrase in [
        "license", "licensing", "subscription"
    ]):
        return "Licensing"

    # Microsoft 365
    if any(phrase in ticket for phrase in [
        "microsoft 365", "microsoft365", "m365"
    ]):
        return "Microsoft 365"

    # Entra ID
    if any(phrase in ticket for phrase in [
        "entra id", "azure ad", "active directory", "conditional access"
    ]):
        return "Entra ID"

    if "outlook" in ticket:
        return "Outlook"

    if any(phrase in ticket for phrase in [
        "exchange online", "exchange mailbox", "exchange server"
    ]):
        return "Exchange Online"

    if "teams" in ticket:
        return "Teams"

    if "onedrive" in ticket:
        return "OneDrive"

    if "sharepoint" in ticket:
        return "SharePoint"

    if "intune" in ticket:
        return "Intune"

    if any(phrase in ticket for phrase in [
        "windows", "workstation", "laptop", "computer"
    ]):
        return "Windows"

    return "Other"


def determine_issue_type(ticket):
    """Final V4 issue-type classification."""
    ticket = ticket.lower()

    # Password / MFA first
    if any(phrase in ticket for phrase in [
        "mfa", "multi-factor", "multifactor",
        "password reset", "reset my password", "forgot my password"
    ]):
        return "Password / MFA"

    # Authentication
    if any(phrase in ticket for phrase in [
        "authentication", "authenticating", "sign in", "sign-in",
        "login", "log in", "password",
        "license has stopped working",
        "license stopped working",
        "license is not working"
    ]):
        return "Authentication"

    # Access / Permissions
    if any(phrase in ticket for phrase in [
        "cannot access", "unable to access", "access denied",
        "permission", "permissions", "access rights"
    ]):
        return "Access / Permissions"

    # Connectivity
    if any(phrase in ticket for phrase in [
        "cannot connect", "unable to connect", "not connecting",
        "connection", "disconnecting", "dropping", "network"
    ]):
        return "Connectivity"

    # Synchronization
    if any(phrase in ticket for phrase in [
        "not syncing", "not synchronized",
        "not synchronizing", "synchronization", "sync"
    ]):
        return "Synchronization"

    # Performance
    if any(phrase in ticket for phrase in [
        "slow", "slowly", "very slowly", "performance",
        "taking a long time", "long time to load", "responding slowly"
    ]):
        return "Performance"

    # Storage
    if any(phrase in ticket for phrase in [
        "storage", "storage full", "running out of storage", "space"
    ]):
        return "Storage"

    # Configuration
    if any(phrase in ticket for phrase in [
        "configure", "configuring", "configuration",
        "setup", "setting up", "settings",
        "enroll", "enrollment", "assign", "assigning", "assignment"
    ]):
        return "Configuration"

    # Application Error
    if any(phrase in ticket for phrase in [
        "application error", "app error",
        "application stopped", "application crashed", "crash"
    ]):
        return "Application Error"

    return "Other"


def determine_sentiment(ticket):
    """Final sentiment classification."""
    ticket = ticket.lower()

    negative_words = [
        "angry", "frustrated", "frustrating", "upset",
        "terrible", "worst", "hate", "annoying",
        "disappointed", "urgent", "problem", "issue",
        "error", "failed", "failing", "broken",
        "not working", "cannot", "can't", "unable",
        "rejecting", "stopped working", "not connecting",
        "not syncing", "not synchronizing", "disconnecting",
        "slow", "very slowly"
    ]

    if any(word in ticket for word in negative_words):
        return "NEGATIVE"

    return "NEUTRAL"


def determine_priority(ticket):
    """Final V5 priority classification."""
    ticket = ticket.lower()

    high_priority = [
        "cannot access", "unable to access",
        "cannot sign in", "unable to sign in",
        "cannot log in", "unable to log in",
        "password repeatedly", "keeps asking for my password",
        "authentication", "authenticating", "mfa",
        "failing", "failed", "not working", "stopped working",
        "connection rejected", "rejecting my connection",
        "cannot connect", "not connecting",
        "disconnecting", "dropping",
        "cannot enroll", "unable to enroll"
    ]

    if any(phrase in ticket for phrase in high_priority):
        return "High"

    # OneDrive synchronization failure
    if "onedrive" in ticket and any(phrase in ticket for phrase in [
        "not syncing", "not synchronizing", "not synchronized"
    ]):
        return "High"

    # Intune enrollment failure
    if "intune" in ticket and any(phrase in ticket for phrase in [
        "cannot enroll", "unable to enroll", "enrollment failure"
    ]):
        return "High"

    # License failure
    if "license" in ticket and any(phrase in ticket for phrase in [
        "stopped working", "not working", "failed",
        "failure", "expired", "no longer works"
    ]):
        return "High"

    # Medium configuration for Exchange/Teams/Intune/Entra ID
    if any(product in ticket for product in [
        "exchange", "teams", "intune", "entra id"
    ]) and any(config in ticket for config in [
        "configure", "configuring", "configuration",
        "setting up", "settings"
    ]):
        return "Medium"

    # General configuration
    if any(phrase in ticket for phrase in [
        "need help configuring", "need help setting up",
        "help configuring", "help setting up",
        "configure", "configuring", "configuration",
        "setting up", "settings"
    ]):
        return "Low"

    # Medium general issues
    if any(phrase in ticket for phrase in [
        "not syncing", "not synchronizing",
        "not synchronized", "synchronization"
    ]):
        return "Medium"

    if "license" in ticket or "licensing" in ticket:
        return "Medium"

    if any(phrase in ticket for phrase in [
        "slow", "slowly", "performance",
        "taking a long time", "long time to load"
    ]):
        return "Medium"

    if any(phrase in ticket for phrase in [
        "storage", "running out of storage", "storage full"
    ]):
        return "Medium"

    return "Low"


def determine_root_cause(ticket):
    """Determine the likely root cause / intent."""
    ticket = ticket.lower()

    if any(phrase in ticket for phrase in [
        "mfa", "multi-factor", "multifactor", "password",
        "sign in", "sign-in", "log in", "login"
    ]):
        return "Reset password or MFA"

    if any(phrase in ticket for phrase in [
        "cannot access", "unable to access",
        "access denied", "permission", "permissions"
    ]):
        return "Access or permission issue"

    if any(phrase in ticket for phrase in [
        "cannot connect", "unable to connect",
        "not connecting", "connection",
        "disconnecting", "network"
    ]):
        return "Connectivity issue"

    if any(phrase in ticket for phrase in [
        "not syncing", "not synchronizing",
        "synchronization", "sync"
    ]):
        return "Synchronization issue"

    if any(phrase in ticket for phrase in [
        "slow", "slowly", "performance", "taking a long time"
    ]):
        return "Performance issue"

    if any(phrase in ticket for phrase in [
        "storage", "running out of storage", "storage full"
    ]):
        return "Storage issue"

    if any(phrase in ticket for phrase in [
        "configure", "configuring", "configuration",
        "setup", "setting up", "settings"
    ]):
        return "Configuration request"

    if any(phrase in ticket for phrase in [
        "license", "licensing", "subscription"
    ]):
        return "Licensing issue"

    if any(phrase in ticket for phrase in [
        "application error", "app error",
        "application crashed", "crash"
    ]):
        return "Application error"

    return "General support issue"


def recommend_action(category, issue_type, priority, root_cause):
    """Return the recommended support action."""
    if issue_type == "Password / MFA":
        return "Verify the user's identity, check account status, and reset the MFA method if authorized."

    if issue_type == "Authentication":
        return "Verify the user's identity and account status, then investigate the authentication issue."

    if issue_type == "Access / Permissions":
        return "Verify the user's permissions and access rights for the affected service or resource."

    if issue_type == "Connectivity":
        return "Check the user's network connectivity and verify the affected service connection."

    if issue_type == "Synchronization":
        return "Check the synchronization status and identify any errors affecting the affected service."

    if issue_type == "Performance":
        return "Investigate the reported performance issue and check whether the affected service is experiencing degradation."

    if issue_type == "Storage":
        return "Review the user's storage usage and identify whether additional storage or cleanup is required."

    if issue_type == "Configuration":
        return "Review the current configuration and assist the user with the required configuration changes."

    if issue_type == "Application Error":
        return "Investigate the application error and review the affected application's status and configuration."

    return "Review the ticket details and investigate the reported issue before determining the appropriate troubleshooting action."


def create_response(ticket, sentiment, priority, root_cause, action):
    """Generate a concise customer-facing response."""
    response = f"""
I understand how frustrating it can be to experience this issue.

Based on your request, we'll help you with the {root_cause.lower()}.

The next step is to {action.lower()}

We'll review the issue and provide the appropriate assistance based on the findings.
"""
    return response.strip()


def calculate_quality_score(ticket, response, action):
    """Final V4 response-quality rubric (0-100)."""
    ticket_lower = ticket.lower()
    response_lower = response.lower()
    action_lower = action.lower()

    score = 0

    if response and len(response.strip()) > 0:
        score += 20

    intent_groups = {
        "configuration": ["configure", "configuring", "configuration", "configured"],
        "authentication": ["authenticate", "authentication", "authenticating", "sign in", "login", "log in"],
        "synchronization": ["sync", "syncing", "synchronizing", "synchronization"],
        "connectivity": ["connect", "connection", "connecting", "disconnecting"],
        "access": ["access", "permission", "permissions"],
        "password": ["password", "mfa"],
        "performance": ["slow", "slowly", "performance"],
        "license": ["license", "licensing"]
    }

    ticket_intents = []
    for intent, words in intent_groups.items():
        if any(word in ticket_lower for word in words):
            ticket_intents.append(intent)

    if any(
        any(word in response_lower for word in intent_groups[intent])
        for intent in ticket_intents
    ):
        score += 20

    action_words = [
        word.strip(".,!?").lower()
        for word in action_lower.split()
        if len(word.strip(".,!?")) >= 6
    ]

    if action_words:
        matches = sum(word in response_lower for word in action_words)
        if matches / len(action_words) >= 0.4:
            score += 20

    word_count = len(response.split())
    if 30 <= word_count <= 120:
        score += 20

    risky_phrases = [
        "guarantee", "guaranteed", "will definitely",
        "will be fixed", "resolved immediately",
        "within 5 minutes", "within 10 minutes"
    ]

    if not any(phrase in response_lower for phrase in risky_phrases):
        score += 20

    return score


def determine_human_review(priority, sentiment, quality_score):
    """Route high-risk or low-quality responses to a human."""
    if priority == "High":
        return "YES"

    if sentiment == "NEGATIVE" and quality_score < 75:
        return "YES"

    if quality_score < 75:
        return "YES"

    return "NO"


def generate_ticket_response(ticket):
    """
    Run the complete automation pipeline for one ticket.
    Returns a dictionary ready for display or conversion to a DataFrame.
    """
    ticket = ticket.strip()

    # Normalize common product-name variations before classification.
    ticket = ticket.replace("one drive", "onedrive")

    if not ticket:
        raise ValueError("Ticket text cannot be empty.")

    category = determine_category(ticket)
    issue_type = determine_issue_type(ticket)
    sentiment = determine_sentiment(ticket)
    priority = determine_priority(ticket)

    root_cause = determine_root_cause(ticket)

    action = recommend_action(
        category,
        issue_type,
        priority,
        root_cause
    )

    response = create_response(
        ticket=ticket,
        sentiment=sentiment,
        priority=priority,
        root_cause=root_cause,
        action=action
    )

    quality_score = calculate_quality_score(
        ticket=ticket,
        response=response,
        action=action
    )

    human_required = determine_human_review(
        priority=priority,
        sentiment=sentiment,
        quality_score=quality_score
    )

    return {
        "ticket": ticket,
        "category": category,
        "issue_type": issue_type,
        "sentiment": sentiment,
        "priority": priority,
        "root_cause": root_cause,
        "recommended_action": action,
        "customer_response": response,
        "quality_score": quality_score,
        "human_required": human_required
    }
