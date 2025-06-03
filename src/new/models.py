from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Job(BaseModel):

    # # Metadata
    # name: str
    # description: Optional[str] = None
    # key: str

    # # Run configuration
    # executable: Optional[str] # todo: add default - calmmage python env at ~/.calmmage/dev-env/bin/python
    path: str # required
    # env_file: Optional[str]= None # todo: add default - .env
    # cwd: Optional[str] = None# todo: add default - path to job
    # args: Optional[list[str]] = None


class JobRun(BaseModel):
    job: Job

    # # timestamp
    # start_time: datetime
    # end_time: Optional[datetime] = None

    # # output
    # return_code: Optional[int] = None
    # stdout: Optional[str] = None
    # stderr: Optional[str] = None