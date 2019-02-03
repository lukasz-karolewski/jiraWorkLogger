# Automated capex logging to jira

- visit
- login using google, 
- provide params and run 

aws cloudformation deploy --stack-name jiraWorkLogger-pipeline \
    --parameter-overrides GitHubToken=asd \
    --template-file cfn/pipeline.json \
    --capabilities CAPABILITY_IAM
    
aws cloudformation deploy --stack-name jiraWorkLogger-pipeline \
    --template-file cfn/pipeline.json \
    --capabilities CAPABILITY_IAM \
    --tags owner=asd