# authentication.conf spec

splunk_auth_conf:
  strategies:
    test_server:
      SSLEnabled: 1
      anonymous_referrals: 1
      bindDN: "cn=splunk_bind_user,ou=service_users,ou=dept,dc=domain,dc=tld"
      bindDNpassword: password
      charset: utf8
      emailAttribute: mail
      groupBaseDN: "ou=groups,ou=dept,dc=domain,dc=tld"
      groupMappingAttribute: dn
      groupMemberAttribute: member
      groupNameAttribute: cn
      host: ldap.domain.tld
      nestedGroups: 0
      network_timeout: 20
      port: 636
      realNameAttribute: displayname
      sizelimit: 1000
      timelimit: 15
      userBaseDN: "ou=users,ou=dept,dc=domain,dc=tld"
      userNameAttribute: samaccountname

  auth:
    authSettings: test_server
    authType: LDAP

  rolemaps:
    - strategy: test_server
      role: admin
      group: some_ldap_group
    - strategy: test_server
      role: user
      group: some_other_group

