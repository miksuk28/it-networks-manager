
CREATE TABLE IF NOT EXISTS hosts (
    host_id     integer     PRIMARY KEY     NOT NULL,
    hostname    text        NOT NULL,
    name        text        UNIQUE,
    description text
);

CREATE TABLE IF NOT EXISTS vlans (
    vlan_id     integer     PRIMARY KEY     NOT NULL,
    vlan_net_id integer     NOT NULL        UNIQUE,
    ip_range    text        NOT NULL,
    name        text        UNIQUE,
    description text,
);

CREATE TABLE IF NOT EXISTS interfaces (
    iface_id    integer     PRIMARY KEY     NOT NULL,
    host_id     integer     NOT NULL,
    address     text,
    description text,
    mac         text        UNIQUE,
    FOREIGN KEY (host_id)   REFERENCES hosts (id) ON DELETE CASCADE
);