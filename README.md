# WEB-LOG-ATTACK-DETECTION

# Web Log Attack Detection

## Scenario
A web server experienced repeated requests targeting sensitive endpoints such as /admin, /login, and configuration files.

## Detection
Logs were analyzed to identify scanning behavior based on request frequency and HTTP response codes.

## Analysis
The IP 91.45.22.10 attempted multiple requests to restricted endpoints within a short time window, indicating reconnaissance activity.

## Decision
Activity classified as potential web reconnaissance or attack preparation phase.

## Response
- IP flagged for monitoring
- WAF rule recommended
- Rate limiting suggested
