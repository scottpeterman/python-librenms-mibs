# SNMP MIB module (NETSCREEN-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\screenos\NETSCREEN-TRAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:25:12 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(netscreenTrap,
 netscreenTrapInfo) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenTrap",
    "netscreenTrapInfo")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

netscreenTrapMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 2, 0)
)
if mibBuilder.loadTexts:
    netscreenTrapMibModule.setRevisions(
        ("2008-03-17 00:00",
         "2005-10-17 00:00",
         "2005-03-03 00:00",
         "2004-09-10 00:00",
         "2004-05-03 00:00",
         "2004-03-03 00:00",
         "2004-01-23 00:00",
         "2001-09-28 00:00",
         "2000-08-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _NetscreenTrapType_Type(Integer32):
    """Custom type netscreenTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              101,
              102,
              103,
              105,
              110,
              111,
              112,
              113,
              114,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              414,
              415,
              416,
              417,
              418,
              419,
              420,
              421,
              422,
              423,
              424,
              425,
              426,
              427,
              428,
              429,
              430,
              431,
              432,
              433,
              434,
              435,
              436,
              441,
              442,
              443,
              554,
              600,
              601,
              602,
              700,
              701,
              702,
              703,
              705,
              706,
              751,
              752,
              800,
              801,
              802,
              803,
              804,
              805,
              806,
              850)
        )
    )
    namedValues = NamedValues(
        *(("traffic-sec", 1),
          ("traffic-min", 2),
          ("multi-auth-fail", 3),
          ("winnuke", 4),
          ("syn-attack", 5),
          ("tear-drop", 6),
          ("ping-death", 7),
          ("ip-spoofing", 8),
          ("ip-src-route", 9),
          ("land", 10),
          ("icmp-flood", 11),
          ("udp-flood", 12),
          ("illegal-cms-svr", 13),
          ("url-block-srv", 14),
          ("high-availability", 15),
          ("port-scan", 16),
          ("addr-sweep", 17),
          ("deny-policy", 18),
          ("device-dead", 19),
          ("low-memory", 20),
          ("dns-srv-down", 21),
          ("generic-HW-fail", 22),
          ("lb-srv-down", 23),
          ("log-full", 24),
          ("x509", 25),
          ("vpn-ike", 26),
          ("admin", 27),
          ("sme", 28),
          ("dhcp", 29),
          ("cpu-usage-high", 30),
          ("ip-conflict", 31),
          ("attact-malicious-url", 32),
          ("session-threshold", 33),
          ("ssh-alarm", 34),
          ("audit-storage", 35),
          ("memory-normal", 36),
          ("cpu-usage-normal", 37),
          ("rxbd-low-alarm", 39),
          ("vpn-tunnel-up", 40),
          ("vpn-tunnel-down", 41),
          ("vpn-replay-attack", 42),
          ("vpn-l2tp-tunnel-remove", 43),
          ("vpn-l2tp-tunnel-remove-err", 44),
          ("vpn-l2tp-call-remove", 45),
          ("vpn-l2tp-call-remove-err", 46),
          ("vpn-ias-too-many", 47),
          ("vpn-ias-over-threshold", 48),
          ("vpn-ias-under-threshold", 49),
          ("vpn-ias-ike-error", 50),
          ("allocated-session-threshold", 51),
          ("av-csp-alarm", 52),
          ("av-alarm", 53),
          ("apppry-alarm", 54),
          ("nsrp-rto-up", 60),
          ("nsrp-rto-down", 61),
          ("nsrp-trackip-success", 62),
          ("nsrp-trackip-failed", 63),
          ("nsrp-trackip-failover", 64),
          ("nsrp-inconsistent-configuration", 65),
          ("trackip-status", 66),
          ("nsrp-vsd-init", 70),
          ("nsrp-vsd-master", 71),
          ("nsrp-vsd-pbackup", 72),
          ("nsrp-vsd-backup", 73),
          ("nsrp-vsd-ineligible", 74),
          ("nsrp-vsd-inoperable", 75),
          ("nsrp-vsd-req-hearbeat-2nd", 76),
          ("nsrp-vsd-reply-2nd", 77),
          ("nsrp-rto-duplicated", 78),
          ("ip-dup-master", 79),
          ("di-heap-create-fail", 80),
          ("mem-alloc-fail", 81),
          ("vrrp-status-alarm", 82),
          ("sccp-alarm", 83),
          ("mgcp-reinit", 84),
          ("mlfr-alarm", 85),
          ("fr-alarm", 86),
          ("cisco-hdlc-alarm", 87),
          ("pppow-alarm", 88),
          ("h323-alarm", 89),
          ("isdn-alarm", 90),
          ("interface-backup", 91),
          ("wan-card-function", 92),
          ("usb-device-operation", 93),
          ("interface-failure", 94),
          ("ppp-no-ip-cfg", 95),
          ("ppp-no-ip-in-pool", 96),
          ("ip-addr-event", 101),
          ("dip-util-raise", 102),
          ("dip-util-clear", 103),
          ("dot1x-alarm", 105),
          ("vpn-ias-radius-error", 110),
          ("vpn-ikeid-enum-attack", 111),
          ("vpn-softlimit-reached", 112),
          ("vpn-ikedos-attack", 113),
          ("vpn-acvpn-profile-error", 114),
          ("route-sys-entry-ex", 200),
          ("route-vr-entry-ex", 201),
          ("route-ospf-hello-flood", 202),
          ("route-ospf-lsa-flood", 203),
          ("route-rip-update-flood", 204),
          ("route-alarm", 205),
          ("ospf-flood", 206),
          ("rip-flood", 207),
          ("bgp-established", 208),
          ("bgp-backwardtransition", 209),
          ("ospf-virtifstatechange", 210),
          ("ospf-nbrstatechange", 211),
          ("ospf-virtnbrstatechange", 212),
          ("ospf-ifconfigerror", 213),
          ("ospf-virtifconfigerror", 214),
          ("ospf-ifauthfailure", 215),
          ("ospf-virtifauthfailure", 216),
          ("ospf-ifrxbadpacket", 217),
          ("ospf-virtifrxbadpacket", 218),
          ("ospf-txretransmit", 219),
          ("ospf-virtiftxretransmit", 220),
          ("ospf-originatelsa", 221),
          ("ospf-maxagelsa", 222),
          ("ospf-lsdboverflow", 223),
          ("ospf-lsdbapproachingoverflow", 224),
          ("ospf-ifstatechange", 225),
          ("bgp-alarm", 226),
          ("ripng-flood", 227),
          ("route-ripng-update-flood", 228),
          ("pbr-alarm", 229),
          ("nhrp-alarm", 230),
          ("ospfv3-alarm", 231),
          ("ids-component", 400),
          ("ids-icmp-flood", 401),
          ("ids-udp-flood", 402),
          ("ids-winnuke", 403),
          ("ids-port-scan", 404),
          ("ids-addr-sweep", 405),
          ("ids-tear-drop", 406),
          ("ids-syn", 407),
          ("ids-ip-spoofing", 408),
          ("ids-ping-death", 409),
          ("ids-ip-source-route", 410),
          ("ids-land", 411),
          ("syn-frag-attack", 412),
          ("tcp-without-flag", 413),
          ("unknow-ip-packet", 414),
          ("bad-ip-option", 415),
          ("ip-option-record", 416),
          ("ip-option-timestamp", 417),
          ("ip-option-scht", 418),
          ("ip-option-lsr", 419),
          ("ip-option-ssr", 420),
          ("ip-option-stream", 421),
          ("icmp-fragment", 422),
          ("too-large-icmp", 423),
          ("tcp-syn-fin", 424),
          ("tcp-fin-no-ack", 425),
          ("tcp-mal-url", 426),
          ("tcp-sess-mal-num", 427),
          ("ids-tcp-syn-ack-ack", 428),
          ("ids-ip-block-frag", 429),
          ("dst-ip-session-limit", 430),
          ("ids-block-zip", 431),
          ("ids-block-jar", 432),
          ("ids-block-exe", 433),
          ("ids-block-activex", 434),
          ("tcp-syn-mac", 435),
          ("ids-nac-attack", 436),
          ("ids-icmp-ping-id-zero", 441),
          ("tcp-sweep", 442),
          ("udp-sweep", 443),
          ("av-scan-mgr", 554),
          ("mcast-base", 600),
          ("mcore-alarm", 601),
          ("spim-alarm", 602),
          ("sm-base", 700),
          ("sm-down", 701),
          ("sm-packet-drop", 702),
          ("sm-overload", 703),
          ("sm-cpu-unresponsive", 705),
          ("sm-policy-abnormal", 706),
          ("switch", 751),
          ("sfp", 752),
          ("cpu-limit-s2f-forced", 800),
          ("cpu-limit-s2f-auto", 801),
          ("cpu-limit-f2s-forced", 802),
          ("cpu-limit-f2s-timeout", 803),
          ("cpu-limit-f2s-auto", 804),
          ("sec-potential-voilation", 805),
          ("flow-sess-cache", 806),
          ("vsys-session-limit", 850))
    )


_NetscreenTrapType_Type.__name__ = "Integer32"
_NetscreenTrapType_Object = MibScalar
netscreenTrapType = _NetscreenTrapType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 2, 1),
    _NetscreenTrapType_Type()
)
netscreenTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    netscreenTrapType.setStatus("current")


class _NetscreenTrapDesc_Type(DisplayString):
    """Custom type netscreenTrapDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetscreenTrapDesc_Type.__name__ = "DisplayString"
_NetscreenTrapDesc_Object = MibScalar
netscreenTrapDesc = _NetscreenTrapDesc_Object(
    (1, 3, 6, 1, 4, 1, 3224, 2, 3),
    _NetscreenTrapDesc_Type()
)
netscreenTrapDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    netscreenTrapDesc.setStatus("current")

# Managed Objects groups


# Notification objects

netscreenTrapHw = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 0, 100)
)
netscreenTrapHw.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"))
)
if mibBuilder.loadTexts:
    netscreenTrapHw.setStatus(
        "current"
    )

netscreenTrapFw = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 0, 200)
)
netscreenTrapFw.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"))
)
if mibBuilder.loadTexts:
    netscreenTrapFw.setStatus(
        "current"
    )

netscreenTrapSw = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 0, 300)
)
netscreenTrapSw.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"))
)
if mibBuilder.loadTexts:
    netscreenTrapSw.setStatus(
        "current"
    )

netscreenTrapTrf = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 0, 400)
)
netscreenTrapTrf.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"))
)
if mibBuilder.loadTexts:
    netscreenTrapTrf.setStatus(
        "current"
    )

netscreenTrapVpn = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 0, 500)
)
netscreenTrapVpn.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"))
)
if mibBuilder.loadTexts:
    netscreenTrapVpn.setStatus(
        "current"
    )

netscreenTrapNsrp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 0, 600)
)
netscreenTrapNsrp.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"))
)
if mibBuilder.loadTexts:
    netscreenTrapNsrp.setStatus(
        "current"
    )

netscreenTrapGPRO = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 0, 700)
)
netscreenTrapGPRO.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"))
)
if mibBuilder.loadTexts:
    netscreenTrapGPRO.setStatus(
        "current"
    )

netscreenTrapDrp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 0, 800)
)
netscreenTrapDrp.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"))
)
if mibBuilder.loadTexts:
    netscreenTrapDrp.setStatus(
        "current"
    )

netscreenTrapIFFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 0, 900)
)
netscreenTrapIFFailover.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"))
)
if mibBuilder.loadTexts:
    netscreenTrapIFFailover.setStatus(
        "current"
    )

netscreenTrapIDPAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 0, 1000)
)
netscreenTrapIDPAttack.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"))
)
if mibBuilder.loadTexts:
    netscreenTrapIDPAttack.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-TRAP-MIB",
    **{"netscreenTrapHw": netscreenTrapHw,
       "netscreenTrapFw": netscreenTrapFw,
       "netscreenTrapSw": netscreenTrapSw,
       "netscreenTrapTrf": netscreenTrapTrf,
       "netscreenTrapVpn": netscreenTrapVpn,
       "netscreenTrapNsrp": netscreenTrapNsrp,
       "netscreenTrapGPRO": netscreenTrapGPRO,
       "netscreenTrapDrp": netscreenTrapDrp,
       "netscreenTrapIFFailover": netscreenTrapIFFailover,
       "netscreenTrapIDPAttack": netscreenTrapIDPAttack,
       "netscreenTrapMibModule": netscreenTrapMibModule,
       "netscreenTrapType": netscreenTrapType,
       "netscreenTrapDesc": netscreenTrapDesc}
)
