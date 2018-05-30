# Copyright (c) 2017 UFCG-LSD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import ConfigParser
import os
import sys


# Conf reading
config = ConfigParser.RawConfigParser()
config.read('./controller.cfg')

""" General configuration """
host = config.get("general", "host")
port = config.getint("general", "port")

""" Actuator plugins parameters """
compute_nodes_str = config.get("actuator-plugins", "compute_nodes")
compute_nodes_keypair = config.get("actuator-plugins", "key_pair")
iops_reference = config.getint("actuator-plugins", "iops_reference")
bs_reference = config.getint("actuator-plugins", "bs_reference")
default_io_cap = config.getint("actuator-plugins", "default_io_cap")
tunelling = config.get("actuator-plugins", "tunelling")
ports_str = config.get("actuator-plugins", "tunnel_ports")
actuator_port = config.get("actuator-plugins", "actuator_port")

""" Monasca configuration """
monasca_endpoint = config.get('monasca', 'monasca_endpoint')
monasca_username = config.get('monasca', 'username')
monasca_password = config.get('monasca', 'password')
monasca_auth_url = config.get('monasca', 'auth_url')
monasca_project_name = config.get('monasca', 'project_name')
monasca_api_version = config.get('monasca', 'api_version')
