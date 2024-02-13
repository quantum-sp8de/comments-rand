#!/usr/bin/env python3

import argparse
import os


class DefaultEnvAction(argparse.Action):
    """Custom action to set cmd arg from environ if not provided"""

    def __init__(self, env, default=None, required=False, *args, **kwargs):
        default = os.environ.get(env)

        if not default:
            required = True

        super().__init__(required=required, default=default, *args, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


def commandline_parser():
    parser = argparse.ArgumentParser(prog="comments_rand")
    parser.add_argument("url", help="youtube url")
    parser.add_argument(
        "-c",
        "--contract_account",
        help="quantum-sp8de smart contract account",
        env="Q_CONTRACT_ACCOUNT",
        action=DefaultEnvAction,
    )
    parser.add_argument(
        "-p",
        "--private_key",
        help="private key for the user in blockchain",
        env="Q_PRIVATE_KEY",
        action=DefaultEnvAction,
    )
    parser.add_argument(
        "-t",
        "--tokens_account",
        help="account of tokens in blockchain",
        env="Q_TOKENS_ACCOUNT",
        action=DefaultEnvAction,
    )
    parser.add_argument(
        "-b",
        "--chain_url",
        help="blockchain url",
        env="Q_CHAIN_URL",
        action=DefaultEnvAction,
    )
    parser.add_argument(
        "-a",
        "--user_account",
        help="user account in blockchain",
        env="Q_USER_ACCOUNT",
        action=DefaultEnvAction,
    )
    parser.add_argument(
        "-y",
        "--api_key",
        help="",
        env="Q_API_KEY",
        action=DefaultEnvAction,
    )

    args = parser.parse_args()

    return args


def main():
    args = commandline_parser()
    print(args)


if __name__ == "__main__":
    main()
