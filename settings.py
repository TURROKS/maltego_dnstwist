from maltego_trx.decorator_registry import TransformSetting

is_registered = TransformSetting(name='dnstwist_registered_domain',
                                 display_name='Registered',
                                 setting_type='boolean',
                                 default_value='False',
                                 global_setting=False)


