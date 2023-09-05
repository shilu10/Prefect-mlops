from prefect.filesystems import Azure

block = Azure(bucket_path="my-bucket/folder/")
block.save("dev")