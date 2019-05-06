#!/usr/bin/env python
__author__ = 'bso'

import argparse
from argparse import RawTextHelpFormatter  
import sys
import logging
import sys as _sys
import traceback
import re
from git_manager.git_access import GitAccess

log = logging.getLogger(__name__)

sys.path.append('/srv/salt')
aws_accounts = {
    '710991980648': {'region': 'us-east-1', 'target': 'development'},
    '569599628740': {'region': 'us-east-1', 'target': 'production'},
    '768554709596': {'region': 'eu-west-1', 'target': 'production'},
    '820102088136': {'region': 'eu-west-2', 'target': 'production'},
    '719404358069': {'region': 'ca-central-1', 'target': 'production'}
}
region_names = {
    'va': 'us-east-1',
    'db': 'eu-west-1',
    'lo': 'eu-west-2',
    'mo': 'ca-central-1'
}

# Used for parse version.propertiespu
# File does not contain section header and we want to be able to use pythons default ConfigParser out of box
class FakeSecHead(object):
    def __init__(self, fp):
        self.fp = fp
        self.sechead = '[fakesection]\n'

    def readline(self):
        if self.sechead:
            try:
                return self.sechead
            finally:
                self.sechead = None
        else:
            return self.fp.readline()

def get_software_version_hash(properties_file):
    import ConfigParser
    cp = ConfigParser.SafeConfigParser()
    cp.readfp(FakeSecHead(open(properties_file)))
    version_list = cp.items('fakesection')
    version_hash = dict()
    for version_info in version_list:
        version_hash[version_info[0]] = version_info[1]
    return version_hash

def log_application_revisions():
    from subprocess import Popen, PIPE
    revision_command = ['git', 'rev-parse', 'HEAD']
    diff_command = ['git', 'diff', '--name-only']
    branch_command = ['git', 'rev-parse', '--abbrev-ref', 'HEAD']

    aws_pod_home = '/srv'
    sub = Popen(revision_command, cwd=aws_pod_home, stdout=PIPE, stderr=PIPE)
    revision_stdout, stderr = sub.communicate()
    sub = Popen(branch_command, cwd=aws_pod_home, stdout=PIPE, stderr=PIPE)
    branch_stdout, stderr = sub.communicate()
    log.info("Orchestration is on revision: '%s' which is part of branch '%s'", revision_stdout.strip(),
             branch_stdout.strip())

    sub = Popen(diff_command, cwd=aws_pod_home, stdout=PIPE, stderr=PIPE)
    stdout, stderr = sub.communicate()
    if stdout:
        log.warn("There are local changes in the following files: %s" % stdout.strip())

def load_version_properties(git_repository, commit, is_development=False):
    git_manager = GitAccess(git_repository)
    if not is_development:
        git_manager.checkout(commit)
    commit = git_manager.get_commit()
    properties_path = "{}/version.properties".format(git_manager.get_repository_path())
    version_hash = get_software_version_hash(properties_path)
    version_hash['pod_version'] = "{}".format(commit)
    git_manager.log_revision()
    return version_hash

def load_infrastructure_version(git_repository, commit, is_development=False):
    git_manager = GitAccess(git_repository)
    if not is_development:
        git_manager.checkout(commit)
    commit = git_manager.get_commit()
    git_manager.log_revision()
    return git_manager.get_supported_cli_workflows(), git_manager.get_repository_path()

def load_salt_version(git_repository, commit):
    # Salt Repository Reference to master branch is
    # called 'base'
    if commit == 'base':
        commit = 'master'
    git_manager = GitAccess(git_repository)
    git_manager.checkout(commit)

def load_hiera_version(git_repository, commit, is_development=False):
    git_manager = GitAccess(git_repository)
    if not is_development:
        git_manager.checkout(commit, clean=False)
    return git_manager.get_repository_path()

###################################
# MAIN FUNCTION BEGINS HERE
###################################

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This tool enabled an administrator to automatically create and manage pods.",
        epilog="Live long and prosper, Admins!",
        formatter_class=RawTextHelpFormatter)

    from cli import mandatory_parser, advanced_parser

    mandatory_parser(parser)
    advanced_parser(parser)
    cli_args = _sys.argv[1:]  # ( Get everything after the script name)
    # We need to evaluate the CLI with basic parameters
    (config, args) = parser.parse_known_args()   # Calling the args method. 

    import logging

    logging.getLogger('sseclient').setLevel(logging.WARNING)
    logging.getLogger('boto').setLevel(logging.WARNING)
    logging.getLogger('boto3').setLevel(logging.WARNING)
    logging.getLogger('botocore').setLevel(logging.WARNING)
    logging.getLogger('requests').setLevel(logging.WARNING)
    logging.getLogger('urllib').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)

    namespace = config
    config = vars(config)
    config['commit'] = config['version']
    
    if len(config['tenant_id']) == 5:
        for mandatory_argument in ('target', 'pod_id', 'region', 'aws_account_num'):
            if not mandatory_argument in config:
                raise RuntimeError('No %s provided' % mandatory_argument)
    else:
        config['tenant_id'] = config['tenant_id'].lower()
        match = re.match(r'([a-z]{2})([a-z])([a-z]{5})(\d{2})$', config['tenant_id'],
            re.IGNORECASE)
        if match:
            region, target, config['tenant_id'], pod_id = match.groups()
            if region not in region_names:
                raise RuntimeError('Region must be one of: ' + ', '.join(region_names.keys()))
            config['region'] = region_names[region]
            if target not in ('p', 'd'):
                raise RuntimeError("Target environment must be either 'P' (for production) or 'D' (for development)")
            config['target'] = 'production' if target == 'p' else 'development'
            config['pod_id'] = str(int(pod_id))
            for aws_account_num, properties in aws_accounts.items():
                if properties['region'] == config['region'] and properties['target'] == config['target']:
                    config['aws_account_num'] = aws_account_num
                    break
            if 'aws_account_num' not in config:
                raise RuntimeError("No valid AWS account for region '%s' and target environment '%s'" % (
                    config['region'], config['target']))
        else:
            raise RuntimeError('Invalid tenant ID')

    # Load AxceleratePod Modules
    config['version'] = load_version_properties(config['version_repository'],
                                                config['version'],
                                                config['is_development'])

    # ORCH-5995: We're only loading the salt version here to verify that the referenced version exists
    load_salt_version(config['version']['salt_state_repo'],
                      config['version']['salt_state_version'])

    workflows, extraction_dir = load_infrastructure_version(config['version']['aws_infrastructure_repository'],
                                                            config['version']['aws_infrastructure_version'],
                                                            config['is_development'])
    sys.path.insert(0, extraction_dir + "/main")

    parser = argparse.ArgumentParser(
        description="This tool enabled an administrator to automatically create and manage pods.",
        epilog="Live long and prosper, Admins!",
        formatter_class=RawTextHelpFormatter)

    subparsers = parser.add_subparsers()
    module = __import__('axceleratepod.cli', fromlist=workflows)
    for workflow in workflows:
        getattr(module, workflow).configure_parser(subparsers)
    
    # We need to evaluate the CLI again with the additional parameters from the module
    (config, args) = parser.parse_known_args(args, namespace)
    workflow = config.workflow
    config = vars(config)
    config = getattr(module, workflow).get_cli_config(config)

    path_to_hiera = load_hiera_version(config['version']['hiera_repo'],
                                        config['version']['hiera_version'],
                                        config['is_development'])

    # We need the path to the logger, that's why we import in this order
    import legacy.logger

    logpath, logname = legacy.logger.setup_logger(**config)
    config['logpath'] = logpath

    log_application_revisions()

    # Use OpenStruct as global options object
    import legacy.options as options

    options.logpath = logpath

    import yaml
    import socket

    log.info("Log '{}' is available in folder '{}' inside the docker container".format(logname, logpath))
    log.info("Orchestration Host: '%s'" % (socket.gethostname()))
    log.info("PodVersion: '{}'".format(config['version']['pod_version']))
    log.info("AWSInfrastructureVersion: '{}'".format(config['version']['aws_infrastructure_version']))
    log.info("CORE Version: '{}'".format(config['version']['core_tag']))
    log.info("CORE Zip: '{}'".format(config['version']['core_version']))
    log.info("AXC5 Version: '{}'".format(config['version']['ng_tag']))
    log.info("Salt State Version: '{}'".format(config['version']['salt_state_version']))
    log.debug("Complete version information:\n%s",
             yaml.dump(config['version'],
                       default_flow_style=False,
                       explicit_start=True))
    import legacy.stacktracer
    from axceleratepod.workflow_manager.workflow_access import WorkflowAccess

    legacy.stacktracer.trace_start(logpath + logname[0:-4] + ".stack")

    # re-creating always the symlink under /srv/salt to point to the right salt folder from within the podversion
    from subprocess import Popen, PIPE
    symlink_map = [
        ['rm', '-rf', "/srv/salt"],
        ['rm', '-rf', "/srv/pillar"],
        ['rm', '-rf', "/srv/reactor"],
        ['rm', '-rf', "/srv/tops"],
        ['mkdir', '-p', "/srv/salt/client/certificate"],
        ["ln", "-sfn", "/srv/store", "/srv/puppet/store"],
        ['rm', '-rf', "/srv/puppet/environments/development/hiera"],
        ['rm', '-rf', "/srv/hiera"],
        ["ln", "-sfn", path_to_hiera, "/srv/hiera"]
    ]
    for symlink_command in symlink_map:
        sub = Popen(symlink_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = sub.communicate()
        if stderr:
            print("An error occurred during symlink creation for the salt source folder: '%s'" % stderr.strip())
            sys.exit(1)

    try:
        # Invoke Orchestration workflows
        wfa = WorkflowAccess(**config)
        wfa.execute_workflow()
    except Exception as e:

        # Write short traceback to error log (and stdout)
        from traceback import format_exception
        (exc_type, exc_value, exc_traceback) = sys.exc_info()
        logging.getLogger(__name__).error(
            'An un-handled exception was caught by orchestration\'s global exception '
            'handler. Please see the log file for more details:\n{0}: {1}\n{2}'.format(
                exc_type.__name__,
                exc_value,
                ''.join(format_exception(exc_type, exc_value, exc_traceback
                                         )).strip()
            )
        )
        # Write long traceback to debug log
        import util.verbose_traceback
        util.verbose_traceback.enable_verbose_traceback()
        log.debug(traceback.format_exc())

        # If PodsUp will directly use orchestration at some point, comment in the following
        # raise e
        import os
        os._exit(1) # Using os to make sure we actually terminate
    finally:
        legacy.stacktracer.trace_stop()

    # Exit - no error
    sys.exit(0)
