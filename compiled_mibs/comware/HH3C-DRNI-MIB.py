# SNMP MIB module (HH3C-DRNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-DRNI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:12 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cDrni = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176)
)
if mibBuilder.loadTexts:
    hh3cDrni.setRevisions(
        ("2020-02-23 11:01",
         "2019-04-11 09:01",
         "2018-08-14 10:21")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDrniObjects_ObjectIdentity = ObjectIdentity
hh3cDrniObjects = _Hh3cDrniObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1)
)
_Hh3cDrniBaseGroup_ObjectIdentity = ObjectIdentity
hh3cDrniBaseGroup = _Hh3cDrniBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 1)
)
_Hh3cDrniSystemMac_Type = MacAddress
_Hh3cDrniSystemMac_Object = MibScalar
hh3cDrniSystemMac = _Hh3cDrniSystemMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 1, 1),
    _Hh3cDrniSystemMac_Type()
)
hh3cDrniSystemMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniSystemMac.setStatus("current")


class _Hh3cDrniSystemPriority_Type(Integer32):
    """Custom type hh3cDrniSystemPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDrniSystemPriority_Type.__name__ = "Integer32"
_Hh3cDrniSystemPriority_Object = MibScalar
hh3cDrniSystemPriority = _Hh3cDrniSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 1, 2),
    _Hh3cDrniSystemPriority_Type()
)
hh3cDrniSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniSystemPriority.setStatus("current")


class _Hh3cDrniSystemNumber_Type(Integer32):
    """Custom type hh3cDrniSystemNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Hh3cDrniSystemNumber_Type.__name__ = "Integer32"
_Hh3cDrniSystemNumber_Object = MibScalar
hh3cDrniSystemNumber = _Hh3cDrniSystemNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 1, 3),
    _Hh3cDrniSystemNumber_Type()
)
hh3cDrniSystemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniSystemNumber.setStatus("current")


class _Hh3cDrniRestoreDelay_Type(Integer32):
    """Custom type hh3cDrniRestoreDelay based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Hh3cDrniRestoreDelay_Type.__name__ = "Integer32"
_Hh3cDrniRestoreDelay_Object = MibScalar
hh3cDrniRestoreDelay = _Hh3cDrniRestoreDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 1, 4),
    _Hh3cDrniRestoreDelay_Type()
)
hh3cDrniRestoreDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniRestoreDelay.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDrniRestoreDelay.setUnits("seconds")


class _Hh3cDrniAutoRecoveryReloadDelay_Type(Integer32):
    """Custom type hh3cDrniAutoRecoveryReloadDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(240, 3600),
    )


_Hh3cDrniAutoRecoveryReloadDelay_Type.__name__ = "Integer32"
_Hh3cDrniAutoRecoveryReloadDelay_Object = MibScalar
hh3cDrniAutoRecoveryReloadDelay = _Hh3cDrniAutoRecoveryReloadDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 1, 5),
    _Hh3cDrniAutoRecoveryReloadDelay_Type()
)
hh3cDrniAutoRecoveryReloadDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniAutoRecoveryReloadDelay.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDrniAutoRecoveryReloadDelay.setUnits("seconds")
_Hh3cDrniRoleGroup_ObjectIdentity = ObjectIdentity
hh3cDrniRoleGroup = _Hh3cDrniRoleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 2)
)


class _Hh3cDrniRoleLocalRolePriority_Type(Integer32):
    """Custom type hh3cDrniRoleLocalRolePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDrniRoleLocalRolePriority_Type.__name__ = "Integer32"
_Hh3cDrniRoleLocalRolePriority_Object = MibScalar
hh3cDrniRoleLocalRolePriority = _Hh3cDrniRoleLocalRolePriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 2, 1),
    _Hh3cDrniRoleLocalRolePriority_Type()
)
hh3cDrniRoleLocalRolePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniRoleLocalRolePriority.setStatus("current")


class _Hh3cDrniRolePeerRolePriority_Type(Integer32):
    """Custom type hh3cDrniRolePeerRolePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDrniRolePeerRolePriority_Type.__name__ = "Integer32"
_Hh3cDrniRolePeerRolePriority_Object = MibScalar
hh3cDrniRolePeerRolePriority = _Hh3cDrniRolePeerRolePriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 2, 2),
    _Hh3cDrniRolePeerRolePriority_Type()
)
hh3cDrniRolePeerRolePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDrniRolePeerRolePriority.setStatus("current")
_Hh3cDrniRoleLocalBridgeMac_Type = MacAddress
_Hh3cDrniRoleLocalBridgeMac_Object = MibScalar
hh3cDrniRoleLocalBridgeMac = _Hh3cDrniRoleLocalBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 2, 3),
    _Hh3cDrniRoleLocalBridgeMac_Type()
)
hh3cDrniRoleLocalBridgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDrniRoleLocalBridgeMac.setStatus("current")
_Hh3cDrniRolePeerBridgeMac_Type = MacAddress
_Hh3cDrniRolePeerBridgeMac_Object = MibScalar
hh3cDrniRolePeerBridgeMac = _Hh3cDrniRolePeerBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 2, 4),
    _Hh3cDrniRolePeerBridgeMac_Type()
)
hh3cDrniRolePeerBridgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDrniRolePeerBridgeMac.setStatus("current")


class _Hh3cDrniRoleLocalConfiguredRole_Type(Integer32):
    """Custom type hh3cDrniRoleLocalConfiguredRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_Hh3cDrniRoleLocalConfiguredRole_Type.__name__ = "Integer32"
_Hh3cDrniRoleLocalConfiguredRole_Object = MibScalar
hh3cDrniRoleLocalConfiguredRole = _Hh3cDrniRoleLocalConfiguredRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 2, 5),
    _Hh3cDrniRoleLocalConfiguredRole_Type()
)
hh3cDrniRoleLocalConfiguredRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDrniRoleLocalConfiguredRole.setStatus("current")


class _Hh3cDrniRolePeerConfiguredRole_Type(Integer32):
    """Custom type hh3cDrniRolePeerConfiguredRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_Hh3cDrniRolePeerConfiguredRole_Type.__name__ = "Integer32"
_Hh3cDrniRolePeerConfiguredRole_Object = MibScalar
hh3cDrniRolePeerConfiguredRole = _Hh3cDrniRolePeerConfiguredRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 2, 6),
    _Hh3cDrniRolePeerConfiguredRole_Type()
)
hh3cDrniRolePeerConfiguredRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDrniRolePeerConfiguredRole.setStatus("current")


class _Hh3cDrniRoleLocalEffectiveRole_Type(Integer32):
    """Custom type hh3cDrniRoleLocalEffectiveRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_Hh3cDrniRoleLocalEffectiveRole_Type.__name__ = "Integer32"
_Hh3cDrniRoleLocalEffectiveRole_Object = MibScalar
hh3cDrniRoleLocalEffectiveRole = _Hh3cDrniRoleLocalEffectiveRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 2, 7),
    _Hh3cDrniRoleLocalEffectiveRole_Type()
)
hh3cDrniRoleLocalEffectiveRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDrniRoleLocalEffectiveRole.setStatus("current")


class _Hh3cDrniRolePeerEffectiveRole_Type(Integer32):
    """Custom type hh3cDrniRolePeerEffectiveRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_Hh3cDrniRolePeerEffectiveRole_Type.__name__ = "Integer32"
_Hh3cDrniRolePeerEffectiveRole_Object = MibScalar
hh3cDrniRolePeerEffectiveRole = _Hh3cDrniRolePeerEffectiveRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 2, 8),
    _Hh3cDrniRolePeerEffectiveRole_Type()
)
hh3cDrniRolePeerEffectiveRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDrniRolePeerEffectiveRole.setStatus("current")
_Hh3cDrniKeepaliveGroup_ObjectIdentity = ObjectIdentity
hh3cDrniKeepaliveGroup = _Hh3cDrniKeepaliveGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 3)
)
_Hh3cDrniKeepaliveDestIpv4_Type = InetAddressIPv4
_Hh3cDrniKeepaliveDestIpv4_Object = MibScalar
hh3cDrniKeepaliveDestIpv4 = _Hh3cDrniKeepaliveDestIpv4_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 3, 1),
    _Hh3cDrniKeepaliveDestIpv4_Type()
)
hh3cDrniKeepaliveDestIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniKeepaliveDestIpv4.setStatus("current")
_Hh3cDrniKeepaliveSourceIpv4_Type = InetAddressIPv4
_Hh3cDrniKeepaliveSourceIpv4_Object = MibScalar
hh3cDrniKeepaliveSourceIpv4 = _Hh3cDrniKeepaliveSourceIpv4_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 3, 2),
    _Hh3cDrniKeepaliveSourceIpv4_Type()
)
hh3cDrniKeepaliveSourceIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniKeepaliveSourceIpv4.setStatus("current")
_Hh3cDrniKeepaliveDestIpv6_Type = InetAddressIPv6
_Hh3cDrniKeepaliveDestIpv6_Object = MibScalar
hh3cDrniKeepaliveDestIpv6 = _Hh3cDrniKeepaliveDestIpv6_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 3, 3),
    _Hh3cDrniKeepaliveDestIpv6_Type()
)
hh3cDrniKeepaliveDestIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniKeepaliveDestIpv6.setStatus("current")
_Hh3cDrniKeepaliveSourceIpv6_Type = InetAddressIPv6
_Hh3cDrniKeepaliveSourceIpv6_Object = MibScalar
hh3cDrniKeepaliveSourceIpv6 = _Hh3cDrniKeepaliveSourceIpv6_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 3, 4),
    _Hh3cDrniKeepaliveSourceIpv6_Type()
)
hh3cDrniKeepaliveSourceIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniKeepaliveSourceIpv6.setStatus("current")


class _Hh3cDrniKeepaliveUdpPort_Type(Integer32):
    """Custom type hh3cDrniKeepaliveUdpPort based on Integer32"""
    defaultValue = 6400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDrniKeepaliveUdpPort_Type.__name__ = "Integer32"
_Hh3cDrniKeepaliveUdpPort_Object = MibScalar
hh3cDrniKeepaliveUdpPort = _Hh3cDrniKeepaliveUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 3, 5),
    _Hh3cDrniKeepaliveUdpPort_Type()
)
hh3cDrniKeepaliveUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniKeepaliveUdpPort.setStatus("current")


class _Hh3cDrniKeepaliveInterval_Type(Integer32):
    """Custom type hh3cDrniKeepaliveInterval based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_Hh3cDrniKeepaliveInterval_Type.__name__ = "Integer32"
_Hh3cDrniKeepaliveInterval_Object = MibScalar
hh3cDrniKeepaliveInterval = _Hh3cDrniKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 3, 6),
    _Hh3cDrniKeepaliveInterval_Type()
)
hh3cDrniKeepaliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniKeepaliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDrniKeepaliveInterval.setUnits("milliseconds")


class _Hh3cDrniKeepaliveTimeout_Type(Integer32):
    """Custom type hh3cDrniKeepaliveTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_Hh3cDrniKeepaliveTimeout_Type.__name__ = "Integer32"
_Hh3cDrniKeepaliveTimeout_Object = MibScalar
hh3cDrniKeepaliveTimeout = _Hh3cDrniKeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 3, 7),
    _Hh3cDrniKeepaliveTimeout_Type()
)
hh3cDrniKeepaliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniKeepaliveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDrniKeepaliveTimeout.setUnits("seconds")


class _Hh3cDrniKeepaliveHoldTime_Type(Integer32):
    """Custom type hh3cDrniKeepaliveHoldTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_Hh3cDrniKeepaliveHoldTime_Type.__name__ = "Integer32"
_Hh3cDrniKeepaliveHoldTime_Object = MibScalar
hh3cDrniKeepaliveHoldTime = _Hh3cDrniKeepaliveHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 3, 8),
    _Hh3cDrniKeepaliveHoldTime_Type()
)
hh3cDrniKeepaliveHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniKeepaliveHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDrniKeepaliveHoldTime.setUnits("seconds")


class _Hh3cDrniKeepaliveLinkStatus_Type(Integer32):
    """Custom type hh3cDrniKeepaliveLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("up", 2),
          ("down", 3))
    )


_Hh3cDrniKeepaliveLinkStatus_Type.__name__ = "Integer32"
_Hh3cDrniKeepaliveLinkStatus_Object = MibScalar
hh3cDrniKeepaliveLinkStatus = _Hh3cDrniKeepaliveLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 3, 9),
    _Hh3cDrniKeepaliveLinkStatus_Type()
)
hh3cDrniKeepaliveLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDrniKeepaliveLinkStatus.setStatus("current")


class _Hh3cDrniKeepaliveVrf_Type(OctetString):
    """Custom type hh3cDrniKeepaliveVrf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cDrniKeepaliveVrf_Type.__name__ = "OctetString"
_Hh3cDrniKeepaliveVrf_Object = MibScalar
hh3cDrniKeepaliveVrf = _Hh3cDrniKeepaliveVrf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 3, 10),
    _Hh3cDrniKeepaliveVrf_Type()
)
hh3cDrniKeepaliveVrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniKeepaliveVrf.setStatus("current")
_Hh3cDrniTables_ObjectIdentity = ObjectIdentity
hh3cDrniTables = _Hh3cDrniTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4)
)
_Hh3cDrniIppTable_Object = MibTable
hh3cDrniIppTable = _Hh3cDrniIppTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cDrniIppTable.setStatus("current")
_Hh3cDrniIppEntry_Object = MibTableRow
hh3cDrniIppEntry = _Hh3cDrniIppEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 1, 1)
)
hh3cDrniIppEntry.setIndexNames(
    (0, "HH3C-DRNI-MIB", "hh3cDrniIppNumber"),
)
if mibBuilder.loadTexts:
    hh3cDrniIppEntry.setStatus("current")


class _Hh3cDrniIppNumber_Type(Integer32):
    """Custom type hh3cDrniIppNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Hh3cDrniIppNumber_Type.__name__ = "Integer32"
_Hh3cDrniIppNumber_Object = MibTableColumn
hh3cDrniIppNumber = _Hh3cDrniIppNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 1, 1, 1),
    _Hh3cDrniIppNumber_Type()
)
hh3cDrniIppNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDrniIppNumber.setStatus("current")
_Hh3cDrniIppIfIndex_Type = InterfaceIndex
_Hh3cDrniIppIfIndex_Object = MibTableColumn
hh3cDrniIppIfIndex = _Hh3cDrniIppIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 1, 1, 2),
    _Hh3cDrniIppIfIndex_Type()
)
hh3cDrniIppIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniIppIfIndex.setStatus("current")
_Hh3cDrniIppRowStatus_Type = RowStatus
_Hh3cDrniIppRowStatus_Object = MibTableColumn
hh3cDrniIppRowStatus = _Hh3cDrniIppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 1, 1, 3),
    _Hh3cDrniIppRowStatus_Type()
)
hh3cDrniIppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDrniIppRowStatus.setStatus("current")
_Hh3cDrniDrPortTable_Object = MibTable
hh3cDrniDrPortTable = _Hh3cDrniDrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cDrniDrPortTable.setStatus("current")
_Hh3cDrniDrPortEntry_Object = MibTableRow
hh3cDrniDrPortEntry = _Hh3cDrniDrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 2, 1)
)
hh3cDrniDrPortEntry.setIndexNames(
    (0, "HH3C-DRNI-MIB", "hh3cDrniDrPortDRGroupId"),
)
if mibBuilder.loadTexts:
    hh3cDrniDrPortEntry.setStatus("current")


class _Hh3cDrniDrPortDRGroupId_Type(Integer32):
    """Custom type hh3cDrniDrPortDRGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cDrniDrPortDRGroupId_Type.__name__ = "Integer32"
_Hh3cDrniDrPortDRGroupId_Object = MibTableColumn
hh3cDrniDrPortDRGroupId = _Hh3cDrniDrPortDRGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 2, 1, 1),
    _Hh3cDrniDrPortDRGroupId_Type()
)
hh3cDrniDrPortDRGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDrniDrPortDRGroupId.setStatus("current")
_Hh3cDrniDrPortIfIndex_Type = InterfaceIndex
_Hh3cDrniDrPortIfIndex_Object = MibTableColumn
hh3cDrniDrPortIfIndex = _Hh3cDrniDrPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 2, 1, 2),
    _Hh3cDrniDrPortIfIndex_Type()
)
hh3cDrniDrPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniDrPortIfIndex.setStatus("current")
_Hh3cDrniDrPortRowStatus_Type = RowStatus
_Hh3cDrniDrPortRowStatus_Object = MibTableColumn
hh3cDrniDrPortRowStatus = _Hh3cDrniDrPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 2, 1, 3),
    _Hh3cDrniDrPortRowStatus_Type()
)
hh3cDrniDrPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDrniDrPortRowStatus.setStatus("current")
_Hh3cDrniPortTable_Object = MibTable
hh3cDrniPortTable = _Hh3cDrniPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hh3cDrniPortTable.setStatus("current")
_Hh3cDrniPortEntry_Object = MibTableRow
hh3cDrniPortEntry = _Hh3cDrniPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 3, 1)
)
hh3cDrniPortEntry.setIndexNames(
    (0, "HH3C-DRNI-MIB", "hh3cDrniPortIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cDrniPortEntry.setStatus("current")
_Hh3cDrniPortIfIndex_Type = InterfaceIndex
_Hh3cDrniPortIfIndex_Object = MibTableColumn
hh3cDrniPortIfIndex = _Hh3cDrniPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 3, 1, 1),
    _Hh3cDrniPortIfIndex_Type()
)
hh3cDrniPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDrniPortIfIndex.setStatus("current")
_Hh3cDrniPortDrcpIsShortPeriod_Type = TruthValue
_Hh3cDrniPortDrcpIsShortPeriod_Object = MibTableColumn
hh3cDrniPortDrcpIsShortPeriod = _Hh3cDrniPortDrcpIsShortPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 3, 1, 2),
    _Hh3cDrniPortDrcpIsShortPeriod_Type()
)
hh3cDrniPortDrcpIsShortPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDrniPortDrcpIsShortPeriod.setStatus("current")


class _Hh3cDrniPortPortStatus_Type(Integer32):
    """Custom type hh3cDrniPortPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Hh3cDrniPortPortStatus_Type.__name__ = "Integer32"
_Hh3cDrniPortPortStatus_Object = MibTableColumn
hh3cDrniPortPortStatus = _Hh3cDrniPortPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 3, 1, 3),
    _Hh3cDrniPortPortStatus_Type()
)
hh3cDrniPortPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDrniPortPortStatus.setStatus("current")


class _Hh3cDrniPortLocalDRCPState_Type(OctetString):
    """Custom type hh3cDrniPortLocalDRCPState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_Hh3cDrniPortLocalDRCPState_Type.__name__ = "OctetString"
_Hh3cDrniPortLocalDRCPState_Object = MibTableColumn
hh3cDrniPortLocalDRCPState = _Hh3cDrniPortLocalDRCPState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 3, 1, 4),
    _Hh3cDrniPortLocalDRCPState_Type()
)
hh3cDrniPortLocalDRCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDrniPortLocalDRCPState.setStatus("current")


class _Hh3cDrniPortPeerDRCPState_Type(OctetString):
    """Custom type hh3cDrniPortPeerDRCPState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_Hh3cDrniPortPeerDRCPState_Type.__name__ = "OctetString"
_Hh3cDrniPortPeerDRCPState_Object = MibTableColumn
hh3cDrniPortPeerDRCPState = _Hh3cDrniPortPeerDRCPState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 3, 1, 5),
    _Hh3cDrniPortPeerDRCPState_Type()
)
hh3cDrniPortPeerDRCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDrniPortPeerDRCPState.setStatus("current")
_Hh3cDrniPortLocalMemberList_Type = PortList
_Hh3cDrniPortLocalMemberList_Object = MibTableColumn
hh3cDrniPortLocalMemberList = _Hh3cDrniPortLocalMemberList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 3, 1, 6),
    _Hh3cDrniPortLocalMemberList_Type()
)
hh3cDrniPortLocalMemberList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDrniPortLocalMemberList.setStatus("current")
_Hh3cDrniPortPeerMemberList_Type = PortList
_Hh3cDrniPortPeerMemberList_Object = MibTableColumn
hh3cDrniPortPeerMemberList = _Hh3cDrniPortPeerMemberList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 176, 1, 4, 3, 1, 7),
    _Hh3cDrniPortPeerMemberList_Type()
)
hh3cDrniPortPeerMemberList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDrniPortPeerMemberList.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DRNI-MIB",
    **{"hh3cDrni": hh3cDrni,
       "hh3cDrniObjects": hh3cDrniObjects,
       "hh3cDrniBaseGroup": hh3cDrniBaseGroup,
       "hh3cDrniSystemMac": hh3cDrniSystemMac,
       "hh3cDrniSystemPriority": hh3cDrniSystemPriority,
       "hh3cDrniSystemNumber": hh3cDrniSystemNumber,
       "hh3cDrniRestoreDelay": hh3cDrniRestoreDelay,
       "hh3cDrniAutoRecoveryReloadDelay": hh3cDrniAutoRecoveryReloadDelay,
       "hh3cDrniRoleGroup": hh3cDrniRoleGroup,
       "hh3cDrniRoleLocalRolePriority": hh3cDrniRoleLocalRolePriority,
       "hh3cDrniRolePeerRolePriority": hh3cDrniRolePeerRolePriority,
       "hh3cDrniRoleLocalBridgeMac": hh3cDrniRoleLocalBridgeMac,
       "hh3cDrniRolePeerBridgeMac": hh3cDrniRolePeerBridgeMac,
       "hh3cDrniRoleLocalConfiguredRole": hh3cDrniRoleLocalConfiguredRole,
       "hh3cDrniRolePeerConfiguredRole": hh3cDrniRolePeerConfiguredRole,
       "hh3cDrniRoleLocalEffectiveRole": hh3cDrniRoleLocalEffectiveRole,
       "hh3cDrniRolePeerEffectiveRole": hh3cDrniRolePeerEffectiveRole,
       "hh3cDrniKeepaliveGroup": hh3cDrniKeepaliveGroup,
       "hh3cDrniKeepaliveDestIpv4": hh3cDrniKeepaliveDestIpv4,
       "hh3cDrniKeepaliveSourceIpv4": hh3cDrniKeepaliveSourceIpv4,
       "hh3cDrniKeepaliveDestIpv6": hh3cDrniKeepaliveDestIpv6,
       "hh3cDrniKeepaliveSourceIpv6": hh3cDrniKeepaliveSourceIpv6,
       "hh3cDrniKeepaliveUdpPort": hh3cDrniKeepaliveUdpPort,
       "hh3cDrniKeepaliveInterval": hh3cDrniKeepaliveInterval,
       "hh3cDrniKeepaliveTimeout": hh3cDrniKeepaliveTimeout,
       "hh3cDrniKeepaliveHoldTime": hh3cDrniKeepaliveHoldTime,
       "hh3cDrniKeepaliveLinkStatus": hh3cDrniKeepaliveLinkStatus,
       "hh3cDrniKeepaliveVrf": hh3cDrniKeepaliveVrf,
       "hh3cDrniTables": hh3cDrniTables,
       "hh3cDrniIppTable": hh3cDrniIppTable,
       "hh3cDrniIppEntry": hh3cDrniIppEntry,
       "hh3cDrniIppNumber": hh3cDrniIppNumber,
       "hh3cDrniIppIfIndex": hh3cDrniIppIfIndex,
       "hh3cDrniIppRowStatus": hh3cDrniIppRowStatus,
       "hh3cDrniDrPortTable": hh3cDrniDrPortTable,
       "hh3cDrniDrPortEntry": hh3cDrniDrPortEntry,
       "hh3cDrniDrPortDRGroupId": hh3cDrniDrPortDRGroupId,
       "hh3cDrniDrPortIfIndex": hh3cDrniDrPortIfIndex,
       "hh3cDrniDrPortRowStatus": hh3cDrniDrPortRowStatus,
       "hh3cDrniPortTable": hh3cDrniPortTable,
       "hh3cDrniPortEntry": hh3cDrniPortEntry,
       "hh3cDrniPortIfIndex": hh3cDrniPortIfIndex,
       "hh3cDrniPortDrcpIsShortPeriod": hh3cDrniPortDrcpIsShortPeriod,
       "hh3cDrniPortPortStatus": hh3cDrniPortPortStatus,
       "hh3cDrniPortLocalDRCPState": hh3cDrniPortLocalDRCPState,
       "hh3cDrniPortPeerDRCPState": hh3cDrniPortPeerDRCPState,
       "hh3cDrniPortLocalMemberList": hh3cDrniPortLocalMemberList,
       "hh3cDrniPortPeerMemberList": hh3cDrniPortPeerMemberList}
)
