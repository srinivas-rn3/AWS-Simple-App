import boto3
conn = boto3.client('rds',region_name='us-east-1')

response = conn.create_db_instance(
        AllocatedStorage=10,
        DBName="test",
        DBInstanceIdentifier="simple-app-rds-instance",
        DBInstanceClass="db.t2.micro",
        Engine="mysql",
        MasterUsername="root",
        MasterUserPassword="pass1234",
        Port=3306,
        VpcSecurityGroupIds=["sg-7fa4d512"],
    )

print (response)
