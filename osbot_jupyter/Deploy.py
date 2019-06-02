from osbot_aws.Globals import Globals
from osbot_aws.apis.Lambda import Lambda
from osbot_aws.helpers.Lambda_Package import Lambda_Package
from pbx_gs_python_utils.utils.Dev import Dev
from pbx_gs_python_utils.utils.Files import Files


class Deploy:

    def __init__(self, lambda_name):
        self.bot_name = 'oss_bot'
        self.profile_name = 'gs-detect-aws'  # 654386450934
        self.region_name = 'eu-west-2'

        Globals.aws_session_profile_name = self.profile_name
        Globals.aws_session_region_name = self.region_name


        self.account_id = '654386450934'
        #self.role_lambdas = "arn:aws:iam::{0}:role/service-role/osbot-lambdas".format(self.account_id)
        self.s3_bucket_lambdas = '{0}-lambdas'.format(self.bot_name).replace('_', '-')

        self.package         = Lambda_Package(lambda_name)
        #self.tmp_s3_bucket = 'gs-lambda-tests'
        self.tmp_s3_bucket = self.s3_bucket_lambdas
        self.tmp_s3_key    = 'unit_tests/lambdas/{0}.zip'.format(lambda_name)



        self.setup()

    def setup(self):
        self.package.tmp_s3_bucket = self.tmp_s3_bucket
        (self.package._lambda.set_s3_bucket(self.tmp_s3_bucket)
                             .set_s3_key   (self.tmp_s3_key))



    def deploy(self, delete_before=False):
        if delete_before:
            self.package.delete()
        self.package.update_code()
        #code_folder = Files.path_combine(__file__,'..')
        #self.package.add_folder(code_folder)
        #self.package.add_root_folder()
        #self.package.add_pbx_gs_python_utils()
        #return self.package.update()