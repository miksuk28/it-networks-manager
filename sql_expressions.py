sql = {
    "create_hosts_table":
     '''
        CREATE TABLE IF NOT EXISTS hosts (
            id          integer     PRIMARY KEY     NOT NULL,
            hostname    text        NOT NULL,
            vlan_id     integer,
            description text,
            FOREIGN KEY (vlan_id)   REFERENCES vlans (id)
        );
    ''',

    "create_vlans_table":
    '''
        CREATE TABLE IF NOT EXISTS vlans (
            id          integer     PRIMARY KEY     NOT NULL,
            vlan_id     integer     NOT NULL        UNIQUE,
            name        text        UNIQUE,
            ip_start    text        NOT NULL,
            ip_end      text        NOT NULL,
            netmask     integer     NOT NULL
            
            CHECK (netmask >= 0 AND netmask <= 32)
        );
    ''',

    "create_addresses_table":
    '''
        CREATE TABLE IF NOT EXISTS addresses (
            id          integer     PRIMARY KEY     NOT NULL,
            address     text        NOT NULL,
            netmask     integer     NOT NULL,
            host_id     integer     NOT NULL,
            FOREIGN KEY (host_id)   REFERENCES hosts (id)

            CHECK (netmask >= 0 AND netmask <= 32)
        );
    '''
}