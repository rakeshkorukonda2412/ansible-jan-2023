ANSIBLE_METADATA = {'metadata_version': '1.0', 
                    'status': ['stableinterface'],
                    'supported_by': 'TekTutor'}

DOCUMENTATION = '''
---
module: get_ip
version_added: 2.9
short_description: Just returns IP Address of the ansible node
description:
   - On success, returns IP address of the Ansible node
'''

from ansible.module_utils.basic import AnsibleModule
import subprocess 

def getIPAddress():
   return subprocess.check_output("hostname") 

def main():
    module = AnsibleModule(
        argument_spec=dict(
        ),
        supports_check_mode=True
    )

    result = dict(
        output=getIPAddress(),
    )

    module.exit_json(**result,changed=False)


if __name__ == '__main__':
    main()
