from ansible.module_utils.basic import AnsibleModule

def add(num1,num2):
   return (num1 + num2)

def main():
    module = AnsibleModule(
        argument_spec=dict(
            input1=dict(type='float'),
            input2=dict(type='float'),
        ),
        supports_check_mode=True
    )

    x = module.params["input1"]
    y = module.params["input2"]
    res = add (x,y)

    result = dict(
        result=res,
    )

    module.exit_json(**result,changed=False)
    #module.fail_json(msg="Error occurred")


if __name__ == '__main__':
    main()
