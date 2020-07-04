class Config:
    #AWS Information
    ACCESS_KEY = 'ASIATGXXZBAPZ4OQIJXM'
    SECRET_KEY = 'NtfNi1W5sEVwUNihuKjlXuW9/iKkhBwhjzEZ9Oay'
    SESSION_TOKEN = "FwoGZXIvYXdzEAUaDGXnA4eYItSRA9pZ1yLHAb3rlIcRVrtGCqIPriQ04vomSQOCtzujKlqiIucHvwCcOPWdjcBDqTaKbOBvvo7yokPQz0Sz77Y/JGZMNmT8A+Hb1fKNg4bVCHZH95p7a8T4+bxyCIJ6a0vivWDAEpfcXOxXpvp8Z79/dIjjsvT8YVg1tY6KmFtteA8TFxAYzjvSYG1M5RYjeMQbes+mis0B0fLsRBT/pUS/940Zr52eH8oqnL7N80L4ULK2/l7NKw0M5hgf6kY8C6RQAPj6aM65MHRxF1BhagIo4dKB+AUyLVV1PSYyedRZhZ39WE7YoMjpoTAF5xfQe5jZ1MpDgF/THKHS4MIBvy4JDM6Hiw=="
    INSTANCE_ID = 'i-0b3788755662f9630'
    ec2_region = "us-east-1"
    ec2_amis = ['ami-09d95fab7fff3776c']
    ec2_keypair = 'MCKey'
    ec2_secgroups = ['minecraft-server']
    ec2_instancetype = 't2.medium'

    #SSH Key Path
    SSH_KEY_FILE_PATH = '~/.ssh/MCKey.pem'
    SERVER_PASSWORD='KELEonbronze96'
    #Server Memory Size
    #This is default to no memory specification but can be: '-Xmx1024M -Xms1024M ' (KEEP TRAILING SPACE)
    MEMORY_ALLOCATION='' 