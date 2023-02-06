from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            message=dict(type='str'),
        ),
        supports_check_mode=True
    )

    result = dict(
        greeting=module.params['message'],
    )

    module.exit_json(**result,changed=True)
    #module.fail_json(msg="Error occurred")


if __name__ == '__main__':
    main()
