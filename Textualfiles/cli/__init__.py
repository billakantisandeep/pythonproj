import re
import argparse
import logging

log = logging.getLogger(__name__)


def advanced_parser(parser):
    # # ADVANCED OPTIONS
    group = parser.add_argument_group('Advanced Options',
                                      'Options for debugging purposes as well as advanced usage')
    group.add_argument("--no_configure",
                       dest="no_configure",
                       action='store_true',
                       help="Set to not configure anything. Use only in development")
    group.add_argument("--uuid",
                       dest="config_uuid",
                       type=str,
                       default=None,
                       help="Specify the UUID used to load a config into the runtime")
    group.add_argument("--debug",
                       dest="debug",
                       action='store_true',
                       help="Set to enable debug logging")
    group.add_argument("--is_development",
                       dest="is_development",
                       action='store_true',
                       help="If enabled, orchestration will not refresh code in /repositories")
    group.add_argument("--consistent_build",
                       dest="consistent_build",
                       action='store_true',
                       help="If enabled, orchestration will try to pull a consistent PodVersion.")
    group.add_argument("--filter_resources",
                       dest="filter_resources",
                       type=correct_filter_resources,
                       default=[],
                       help="Accepts a list of resources that will be filtered out during the run.")
    group.add_argument("--skip_launchpad",
                       action='store_true',
                       help="If enabled, skip obtaining tenant information from Launchpad and instead retrieve it from"
                            "hiera if available.")
    group.add_argument("--salt_master",
                       dest="salt_master",
                       type=str,
                       default='http://salt-master:8000',
                       help="If any URL given, orchestration will use it as the salt master url")
    group.add_argument("--version_repository",
                       dest="version_repository",
                       default='codecommit:/v1/repos/podversion',
                       type=str)


def mandatory_parser(parser):
    # GENERALLY MANDATORY OPTIONS
    group = parser.add_argument_group('Mandatory General Parameters')
    group.add_argument("-T", "--target_environment",
                       dest="target",
                       default='development',
                       type=correct_target,
                       help="Set target where the pod shall be created. "
                            "Possible values are production, staging and development")
    group.add_argument("-I", "--tenant_id",
                       dest="tenant_id",
                       type=correct_tenant_id,
                       required=True,
                       help="Specify the id of the tenant. This has to be set for every command. "
                            "If the client code is specified orchestration will try to lookup the tenant id")
    group.add_argument("-P", "--pod_id",
                       dest="pod_id",
                       default=1,
                       type=correct_pod_id,
                       help="Specify the pod id. This id has to be between 1 and 99. This has to be set for every "
                            "command.")
    group.add_argument("-R", "--region",
                       dest="region",
                       default="us-east-1",
                       type=correct_region,
                       help="Specify the region which you wish to launch the pod into. Only a few regions are allowed,"
                            " us-east-1 and eu-west-1")
    group.add_argument("-A", "--aws_account_num",
                       dest="aws_account_num",
                       default="569599628740",
                       type=correct_account_num,
                       help="Specify the AWS account number which you wish to launch the pod into.\n"
                            "Please use one of the follow: \n"
                            " - US-EAST-1    DEV  Account: 710991980648\n"
                            " - US-EAST-1    PROD Account: 569599628740\n"
                            " - EU-WEST-1    PROD Account: 768554709596\n"
                            " - EU-WEST-2    PROD Account: 820102088136\n"
                            " - CA-CENTRAL-1 PROD Account: 719404358069\n")
    group.add_argument("-V", "--version",
                       dest="version",
                       type=correct_version,
                       required=True,
                       help="Specify the major Pod version")
    group.add_argument("--minor_version",
                       type=correct_minor_version,
                       help="deprecated; used to specify the minor Pod version")
    group.add_argument("-C", "--costcenter",
                       dest="costcenter",
                       default=None,
                       type=correct_costcenter_tag,
                       required=True,
                       help="Set the CostCenter tag")
    group.add_argument("--max_num_puppet_retries",
                       dest="max_num_puppet_retries",
                       type=correct_num_puppet_retries,
                       default=50,
                       help="Defines the max num puppet retries")

def correct_filter_resources(val):
    str_split = val.rstrip().lstrip().replace("\"","").split(",")
    return str_split

def correct_version(val):
    import re
    expr = re.compile('^[0-9A-Za-z_\-\/]*$').match
    if not expr(val):
        raise argparse.ArgumentTypeError("'%s' is not a valid major version." % val)
    return val

def correct_minor_version(val):
    raise argparse.ArgumentTypeError('--minor_version is not a supported parameter anymore')

def correct_pod_id(val):
    val = int(val)
    try:
        assert (val >= 1)
        assert (val <= 99)
    except:
        raise argparse.ArgumentTypeError("'%s' is not a valid id. It must be between 1 and 99" % val)
    return str(val)


def correct_num_puppet_retries(val):
    val = int(val)
    try:
        assert (val >= 1)
        assert (val <= 50)
    except:
        raise argparse.ArgumentTypeError("'%s' is not a valid value. It must be between 1 and 50" % val)
    return str(val)


def correct_region(val):
    if val.lower() not in ['us-east-1', 'us-west-2', 'eu-west-1', 'eu-west-2', 'ca-central-1']:
        raise argparse.ArgumentTypeError(
            "'%s' is not a region that is supported. Current supported regions are us-east-1, us-west-2, eu-west-1, eu-west-2, ca-central-1"
            % val)
    return val.lower()


def correct_account_num(val):
    if val not in ['569599628740', '710991980648', '768554709596', '820102088136', '719404358069']:
        raise argparse.ArgumentTypeError(
            "'%s' is not a supported account number. Please use one of the follow: \n"
            " - US-EAST-1    DEV  Account: 710991980648\n"
            " - US-EAST-1    PROD Account: 569599628740\n"
            " - EU-WEST-1    PROD Account: 768554709596\n"
            " - EU-WEST-2    PROD Account: 820102088136\n"
            " - CA-CENTRAL-1 PROD Account: 719404358069\n"
            % val)
    return val


def correct_tenant_id(val):
    val = val.lower()
    if re.match("^\d{5}$", val):
        return val
    else:
        return val


def correct_target(val):
    val = val.lower()
    targets = ['production', 'staging', 'development']
    if re.match("^[a-z_]*$", val):
        if val in targets:
            return val
        else:
            raise argparse.ArgumentTypeError(
                "'%s' is not a valid target name. Valid target names are '%s'" % (val, targets)
            )
    else:
        raise argparse.ArgumentTypeError(
            "'%s' is not a valid target name. must not have any special symbols in it" % val
        )


def correct_costcenter_tag(value):
    if value:
        if not re.search(r'^[\w.-]+@[\w.-]+\.\w+$', value):
            raise argparse.ArgumentTypeError("'%s' is not a valid costcenter tag. "
                                             "It has to be an email address" % value)
    return value
