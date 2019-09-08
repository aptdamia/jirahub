# This config contains custom settings for all keys

import re

c.jira.server = "https://test.jira.server"
c.jira.project_key = "TEST"
c.jira.github_issue_url_field = "custom_github_issue_url"
c.jira.jirahub_metadata_field = "custom_jirahub_metadata"
c.jira.closed_statuses = ["Closed", "Done"]
c.jira.close_status = "Done"
c.jira.reopen_status = "Ready"
c.jira.open_status = "Open"
c.jira.max_retries = 5
c.jira.issue_filter = lambda issue: True
c.jira.sync_comments = True
c.jira.sync_status = True
c.jira.sync_labels = True
c.jira.sync_milestones = True
c.jira.issue_title_formatter = lambda issue, title: "From GitHub: " + title
c.jira.issue_body_formatter = lambda issue, body: "Check out this great GitHub issue:\n\n" + body
c.jira.comment_body_formatter = lambda issue, comment, body: "Check out this great GitHub comment:\n\n" + body
c.jira.redact_patterns.append(re.compile(r"(?<=secret GitHub data: ).+?\b"))


def jira_issue_create_hook(issue, fields):
    fields["issue_type"] = "Bug"
    return fields


c.jira.before_issue_create.append(jira_issue_create_hook)

c.github.repository = "testing/test-repo"
c.github.max_retries = 10
c.github.issue_filter = lambda _: True
c.github.sync_comments = True
c.github.sync_status = True
c.github.sync_labels = True
c.github.sync_milestones = True
c.github.issue_title_formatter = lambda issue, title: "From JIRA: " + title
c.github.issue_body_formatter = lambda issue, body: "Check out this great JIRA issue:\n\n" + body
c.github.comment_body_formatter = lambda issue, comment, body: "Check out this great JIRA comment:\n\n" + body
c.github.redact_patterns.append(re.compile(r"(?<=secret JIRA data: ).+?\b"))


def github_issue_create_hook(_, fields):
    fields["labels"] = ["jirahub"]
    return fields


c.github.before_issue_create.append(github_issue_create_hook)
