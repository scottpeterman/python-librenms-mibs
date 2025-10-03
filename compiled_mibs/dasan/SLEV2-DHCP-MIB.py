# SNMP MIB module (SLEV2-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLEV2-DHCP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:09 2025
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

(sleV2Mgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleV2Mgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleV2Dhcp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6)
)


# Types definitions



class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleV2DhcpBase_ObjectIdentity = ObjectIdentity
sleV2DhcpBase = _SleV2DhcpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 1)
)
_SleV2Dhcp4_ObjectIdentity = ObjectIdentity
sleV2Dhcp4 = _SleV2Dhcp4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2)
)
_SleV2Dhcp4Base_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Base = _SleV2Dhcp4Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1)
)
_SleV2Dhcp4Info_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Info = _SleV2Dhcp4Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1)
)


class _SleV2Dhcp4ServiceActivity_Type(Integer32):
    """Custom type sleV2Dhcp4ServiceActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Dhcp4ServiceActivity_Type.__name__ = "Integer32"
_SleV2Dhcp4ServiceActivity_Object = MibScalar
sleV2Dhcp4ServiceActivity = _SleV2Dhcp4ServiceActivity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 1),
    _SleV2Dhcp4ServiceActivity_Type()
)
sleV2Dhcp4ServiceActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ServiceActivity.setStatus("current")
_SleV2Dhcp4DatabaseURL_Type = IpAddress
_SleV2Dhcp4DatabaseURL_Object = MibScalar
sleV2Dhcp4DatabaseURL = _SleV2Dhcp4DatabaseURL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 2),
    _SleV2Dhcp4DatabaseURL_Type()
)
sleV2Dhcp4DatabaseURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4DatabaseURL.setStatus("current")


class _SleV2Dhcp4DatabaseInterval_Type(Integer32):
    """Custom type sleV2Dhcp4DatabaseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Dhcp4DatabaseInterval_Type.__name__ = "Integer32"
_SleV2Dhcp4DatabaseInterval_Object = MibScalar
sleV2Dhcp4DatabaseInterval = _SleV2Dhcp4DatabaseInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 3),
    _SleV2Dhcp4DatabaseInterval_Type()
)
sleV2Dhcp4DatabaseInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4DatabaseInterval.setStatus("current")


class _SleV2Dhcp4ArpPingFlag_Type(Integer32):
    """Custom type sleV2Dhcp4ArpPingFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ping", 0),
          ("arp", 1))
    )


_SleV2Dhcp4ArpPingFlag_Type.__name__ = "Integer32"
_SleV2Dhcp4ArpPingFlag_Object = MibScalar
sleV2Dhcp4ArpPingFlag = _SleV2Dhcp4ArpPingFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 4),
    _SleV2Dhcp4ArpPingFlag_Type()
)
sleV2Dhcp4ArpPingFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ArpPingFlag.setStatus("current")


class _SleV2Dhcp4ArpRetransmits_Type(Integer32):
    """Custom type sleV2Dhcp4ArpRetransmits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_SleV2Dhcp4ArpRetransmits_Type.__name__ = "Integer32"
_SleV2Dhcp4ArpRetransmits_Object = MibScalar
sleV2Dhcp4ArpRetransmits = _SleV2Dhcp4ArpRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 5),
    _SleV2Dhcp4ArpRetransmits_Type()
)
sleV2Dhcp4ArpRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ArpRetransmits.setStatus("current")


class _SleV2Dhcp4ArpTimeout_Type(Integer32):
    """Custom type sleV2Dhcp4ArpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_SleV2Dhcp4ArpTimeout_Type.__name__ = "Integer32"
_SleV2Dhcp4ArpTimeout_Object = MibScalar
sleV2Dhcp4ArpTimeout = _SleV2Dhcp4ArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 6),
    _SleV2Dhcp4ArpTimeout_Type()
)
sleV2Dhcp4ArpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ArpTimeout.setStatus("current")


class _SleV2Dhcp4PingRetransmits_Type(Integer32):
    """Custom type sleV2Dhcp4PingRetransmits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_SleV2Dhcp4PingRetransmits_Type.__name__ = "Integer32"
_SleV2Dhcp4PingRetransmits_Object = MibScalar
sleV2Dhcp4PingRetransmits = _SleV2Dhcp4PingRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 7),
    _SleV2Dhcp4PingRetransmits_Type()
)
sleV2Dhcp4PingRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PingRetransmits.setStatus("current")


class _SleV2Dhcp4PingTimeout_Type(Integer32):
    """Custom type sleV2Dhcp4PingTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_SleV2Dhcp4PingTimeout_Type.__name__ = "Integer32"
_SleV2Dhcp4PingTimeout_Object = MibScalar
sleV2Dhcp4PingTimeout = _SleV2Dhcp4PingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 8),
    _SleV2Dhcp4PingTimeout_Type()
)
sleV2Dhcp4PingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PingTimeout.setStatus("current")


class _SleV2Dhcp4ClassUsage_Type(Integer32):
    """Custom type sleV2Dhcp4ClassUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Dhcp4ClassUsage_Type.__name__ = "Integer32"
_SleV2Dhcp4ClassUsage_Object = MibScalar
sleV2Dhcp4ClassUsage = _SleV2Dhcp4ClassUsage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 9),
    _SleV2Dhcp4ClassUsage_Type()
)
sleV2Dhcp4ClassUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassUsage.setStatus("current")


class _SleV2Dhcp4SmartRelayUsage_Type(Integer32):
    """Custom type sleV2Dhcp4SmartRelayUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Dhcp4SmartRelayUsage_Type.__name__ = "Integer32"
_SleV2Dhcp4SmartRelayUsage_Object = MibScalar
sleV2Dhcp4SmartRelayUsage = _SleV2Dhcp4SmartRelayUsage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 10),
    _SleV2Dhcp4SmartRelayUsage_Type()
)
sleV2Dhcp4SmartRelayUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4SmartRelayUsage.setStatus("current")


class _SleV2Dhcp4Option82Usage_Type(Integer32):
    """Custom type sleV2Dhcp4Option82Usage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Dhcp4Option82Usage_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82Usage_Object = MibScalar
sleV2Dhcp4Option82Usage = _SleV2Dhcp4Option82Usage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 11),
    _SleV2Dhcp4Option82Usage_Type()
)
sleV2Dhcp4Option82Usage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82Usage.setStatus("current")


class _SleV2Dhcp4Option82Drop_Type(Integer32):
    """Custom type sleV2Dhcp4Option82Drop based on Integer32"""
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
          ("normal", 1),
          ("option82", 2))
    )


_SleV2Dhcp4Option82Drop_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82Drop_Object = MibScalar
sleV2Dhcp4Option82Drop = _SleV2Dhcp4Option82Drop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 12),
    _SleV2Dhcp4Option82Drop_Type()
)
sleV2Dhcp4Option82Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82Drop.setStatus("current")


class _SleV2Dhcp4Option82Policy_Type(Integer32):
    """Custom type sleV2Dhcp4Option82Policy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("keep", 0),
          ("replace", 1))
    )


_SleV2Dhcp4Option82Policy_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82Policy_Object = MibScalar
sleV2Dhcp4Option82Policy = _SleV2Dhcp4Option82Policy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 13),
    _SleV2Dhcp4Option82Policy_Type()
)
sleV2Dhcp4Option82Policy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82Policy.setStatus("current")


class _SleV2Dhcp4Option82TrustDefault_Type(Integer32):
    """Custom type sleV2Dhcp4Option82TrustDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_SleV2Dhcp4Option82TrustDefault_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82TrustDefault_Object = MibScalar
sleV2Dhcp4Option82TrustDefault = _SleV2Dhcp4Option82TrustDefault_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 14),
    _SleV2Dhcp4Option82TrustDefault_Type()
)
sleV2Dhcp4Option82TrustDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82TrustDefault.setStatus("current")


class _SleV2Dhcp4Option82SystemRemoteType_Type(Integer32):
    """Custom type sleV2Dhcp4Option82SystemRemoteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ipaddress", 1),
          ("hex", 2),
          ("text", 3),
          ("host", 4),
          ("index", 5),
          ("option", 6),
          ("undef", 255))
    )


_SleV2Dhcp4Option82SystemRemoteType_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82SystemRemoteType_Object = MibScalar
sleV2Dhcp4Option82SystemRemoteType = _SleV2Dhcp4Option82SystemRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 15),
    _SleV2Dhcp4Option82SystemRemoteType_Type()
)
sleV2Dhcp4Option82SystemRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82SystemRemoteType.setStatus("current")


class _SleV2Dhcp4Option82SystemRemoteId_Type(OctetString):
    """Custom type sleV2Dhcp4Option82SystemRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4Option82SystemRemoteId_Type.__name__ = "OctetString"
_SleV2Dhcp4Option82SystemRemoteId_Object = MibScalar
sleV2Dhcp4Option82SystemRemoteId = _SleV2Dhcp4Option82SystemRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 16),
    _SleV2Dhcp4Option82SystemRemoteId_Type()
)
sleV2Dhcp4Option82SystemRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82SystemRemoteId.setStatus("current")


class _SleV2Dhcp4DatabaseKey_Type(Integer32):
    """Custom type sleV2Dhcp4DatabaseKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clientid", 0),
          ("hwaddress", 1))
    )


_SleV2Dhcp4DatabaseKey_Type.__name__ = "Integer32"
_SleV2Dhcp4DatabaseKey_Object = MibScalar
sleV2Dhcp4DatabaseKey = _SleV2Dhcp4DatabaseKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 17),
    _SleV2Dhcp4DatabaseKey_Type()
)
sleV2Dhcp4DatabaseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4DatabaseKey.setStatus("current")


class _SleV2Dhcp4DebugStatus_Type(Bits):
    """Custom type sleV2Dhcp4DebugStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugFilter", 0),
          ("debugLease", 1),
          ("debugPacket", 2),
          ("debugServices", 3))
    )

_SleV2Dhcp4DebugStatus_Type.__name__ = "Bits"
_SleV2Dhcp4DebugStatus_Object = MibScalar
sleV2Dhcp4DebugStatus = _SleV2Dhcp4DebugStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 18),
    _SleV2Dhcp4DebugStatus_Type()
)
sleV2Dhcp4DebugStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4DebugStatus.setStatus("current")


class _SleV2Dhcp4AuthArpTime_Type(Integer32):
    """Custom type sleV2Dhcp4AuthArpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483637),
    )


_SleV2Dhcp4AuthArpTime_Type.__name__ = "Integer32"
_SleV2Dhcp4AuthArpTime_Object = MibScalar
sleV2Dhcp4AuthArpTime = _SleV2Dhcp4AuthArpTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 19),
    _SleV2Dhcp4AuthArpTime_Type()
)
sleV2Dhcp4AuthArpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4AuthArpTime.setStatus("current")
if mibBuilder.loadTexts:
    sleV2Dhcp4AuthArpTime.setUnits("second")
_SleV2Dhcp4AuthArpLeft_Type = Unsigned32
_SleV2Dhcp4AuthArpLeft_Object = MibScalar
sleV2Dhcp4AuthArpLeft = _SleV2Dhcp4AuthArpLeft_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 20),
    _SleV2Dhcp4AuthArpLeft_Type()
)
sleV2Dhcp4AuthArpLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4AuthArpLeft.setStatus("current")
if mibBuilder.loadTexts:
    sleV2Dhcp4AuthArpLeft.setUnits("second")
_SleV2Dhcp4ClientHardwareAddress_Type = Boolean
_SleV2Dhcp4ClientHardwareAddress_Object = MibScalar
sleV2Dhcp4ClientHardwareAddress = _SleV2Dhcp4ClientHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 21),
    _SleV2Dhcp4ClientHardwareAddress_Type()
)
sleV2Dhcp4ClientHardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientHardwareAddress.setStatus("current")


class _SleV2Dhcp4PEStatus_Type(Integer32):
    """Custom type sleV2Dhcp4PEStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Dhcp4PEStatus_Type.__name__ = "Integer32"
_SleV2Dhcp4PEStatus_Object = MibScalar
sleV2Dhcp4PEStatus = _SleV2Dhcp4PEStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 22),
    _SleV2Dhcp4PEStatus_Type()
)
sleV2Dhcp4PEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEStatus.setStatus("current")


class _SleV2Dhcp4AuthArpReadyTime_Type(Integer32):
    """Custom type sleV2Dhcp4AuthArpReadyTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483637),
    )


_SleV2Dhcp4AuthArpReadyTime_Type.__name__ = "Integer32"
_SleV2Dhcp4AuthArpReadyTime_Object = MibScalar
sleV2Dhcp4AuthArpReadyTime = _SleV2Dhcp4AuthArpReadyTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 23),
    _SleV2Dhcp4AuthArpReadyTime_Type()
)
sleV2Dhcp4AuthArpReadyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4AuthArpReadyTime.setStatus("current")


class _SleV2Dhcp4AuthArpRemainTime_Type(Integer32):
    """Custom type sleV2Dhcp4AuthArpRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483637),
    )


_SleV2Dhcp4AuthArpRemainTime_Type.__name__ = "Integer32"
_SleV2Dhcp4AuthArpRemainTime_Object = MibScalar
sleV2Dhcp4AuthArpRemainTime = _SleV2Dhcp4AuthArpRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 24),
    _SleV2Dhcp4AuthArpRemainTime_Type()
)
sleV2Dhcp4AuthArpRemainTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4AuthArpRemainTime.setStatus("current")


class _SleV2Dhcp4Option82SystemRemoteOption_Type(OctetString):
    """Custom type sleV2Dhcp4Option82SystemRemoteOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SleV2Dhcp4Option82SystemRemoteOption_Type.__name__ = "OctetString"
_SleV2Dhcp4Option82SystemRemoteOption_Object = MibScalar
sleV2Dhcp4Option82SystemRemoteOption = _SleV2Dhcp4Option82SystemRemoteOption_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 25),
    _SleV2Dhcp4Option82SystemRemoteOption_Type()
)
sleV2Dhcp4Option82SystemRemoteOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82SystemRemoteOption.setStatus("current")


class _SleV2Dhcp4Option82SystemCircuitPortType_Type(Integer32):
    """Custom type sleV2Dhcp4Option82SystemCircuitPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("physical", 1),
          ("logical", 2))
    )


_SleV2Dhcp4Option82SystemCircuitPortType_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82SystemCircuitPortType_Object = MibScalar
sleV2Dhcp4Option82SystemCircuitPortType = _SleV2Dhcp4Option82SystemCircuitPortType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 1, 26),
    _SleV2Dhcp4Option82SystemCircuitPortType_Type()
)
sleV2Dhcp4Option82SystemCircuitPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82SystemCircuitPortType.setStatus("current")
_SleV2Dhcp4Control_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Control = _SleV2Dhcp4Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2)
)


class _SleV2Dhcp4ControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4ControlRequest based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("setDhcpServiceActivity", 1),
          ("setDhcpDatabaseProfile", 2),
          ("setDhcpArpPingProfile", 3),
          ("setDhcpClassState", 4),
          ("setDhcpSmartRelayState", 5),
          ("setDhcpOption82State", 6),
          ("setDhcpOption82Policy", 7),
          ("setDhcpOption82TrustDefault", 8),
          ("setDhcpOption82SystemRemoteId", 9),
          ("setDhcpDatabaseKey", 10),
          ("setDhcpDebugStatus", 11),
          ("setDhcpAuthArpTime", 12),
          ("setDhcpClientHardwareAddress", 13),
          ("setDhcpPEStatus", 14),
          ("setDhcpOption82SystemRemoteOption", 15),
          ("setDhcpOption82SystemCircuitIdPortType", 16))
    )


_SleV2Dhcp4ControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlRequest_Object = MibScalar
sleV2Dhcp4ControlRequest = _SleV2Dhcp4ControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 1),
    _SleV2Dhcp4ControlRequest_Type()
)
sleV2Dhcp4ControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlRequest.setStatus("current")
_SleV2Dhcp4ControlStatus_Type = SleControlStatusType
_SleV2Dhcp4ControlStatus_Object = MibScalar
sleV2Dhcp4ControlStatus = _SleV2Dhcp4ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 2),
    _SleV2Dhcp4ControlStatus_Type()
)
sleV2Dhcp4ControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlStatus.setStatus("current")
_SleV2Dhcp4ControlTimer_Type = Gauge32
_SleV2Dhcp4ControlTimer_Object = MibScalar
sleV2Dhcp4ControlTimer = _SleV2Dhcp4ControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 3),
    _SleV2Dhcp4ControlTimer_Type()
)
sleV2Dhcp4ControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlTimer.setStatus("current")
_SleV2Dhcp4ControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4ControlTimeStamp_Object = MibScalar
sleV2Dhcp4ControlTimeStamp = _SleV2Dhcp4ControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 4),
    _SleV2Dhcp4ControlTimeStamp_Type()
)
sleV2Dhcp4ControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlTimeStamp.setStatus("current")
_SleV2Dhcp4ControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4ControlReqResult_Object = MibScalar
sleV2Dhcp4ControlReqResult = _SleV2Dhcp4ControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 5),
    _SleV2Dhcp4ControlReqResult_Type()
)
sleV2Dhcp4ControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlReqResult.setStatus("current")


class _SleV2Dhcp4ControlServiceActivity_Type(Integer32):
    """Custom type sleV2Dhcp4ControlServiceActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Dhcp4ControlServiceActivity_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlServiceActivity_Object = MibScalar
sleV2Dhcp4ControlServiceActivity = _SleV2Dhcp4ControlServiceActivity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 6),
    _SleV2Dhcp4ControlServiceActivity_Type()
)
sleV2Dhcp4ControlServiceActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlServiceActivity.setStatus("current")
_SleV2Dhcp4ControlDatabaseURL_Type = IpAddress
_SleV2Dhcp4ControlDatabaseURL_Object = MibScalar
sleV2Dhcp4ControlDatabaseURL = _SleV2Dhcp4ControlDatabaseURL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 7),
    _SleV2Dhcp4ControlDatabaseURL_Type()
)
sleV2Dhcp4ControlDatabaseURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlDatabaseURL.setStatus("current")


class _SleV2Dhcp4ControlDatabaseInterval_Type(Integer32):
    """Custom type sleV2Dhcp4ControlDatabaseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Dhcp4ControlDatabaseInterval_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlDatabaseInterval_Object = MibScalar
sleV2Dhcp4ControlDatabaseInterval = _SleV2Dhcp4ControlDatabaseInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 8),
    _SleV2Dhcp4ControlDatabaseInterval_Type()
)
sleV2Dhcp4ControlDatabaseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlDatabaseInterval.setStatus("current")


class _SleV2Dhcp4ControlArpPingFlag_Type(Integer32):
    """Custom type sleV2Dhcp4ControlArpPingFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ping", 0),
          ("arp", 1))
    )


_SleV2Dhcp4ControlArpPingFlag_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlArpPingFlag_Object = MibScalar
sleV2Dhcp4ControlArpPingFlag = _SleV2Dhcp4ControlArpPingFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 9),
    _SleV2Dhcp4ControlArpPingFlag_Type()
)
sleV2Dhcp4ControlArpPingFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlArpPingFlag.setStatus("current")


class _SleV2Dhcp4ControlArpRetransmits_Type(Integer32):
    """Custom type sleV2Dhcp4ControlArpRetransmits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_SleV2Dhcp4ControlArpRetransmits_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlArpRetransmits_Object = MibScalar
sleV2Dhcp4ControlArpRetransmits = _SleV2Dhcp4ControlArpRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 10),
    _SleV2Dhcp4ControlArpRetransmits_Type()
)
sleV2Dhcp4ControlArpRetransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlArpRetransmits.setStatus("current")


class _SleV2Dhcp4ControlArpTimeout_Type(Integer32):
    """Custom type sleV2Dhcp4ControlArpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_SleV2Dhcp4ControlArpTimeout_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlArpTimeout_Object = MibScalar
sleV2Dhcp4ControlArpTimeout = _SleV2Dhcp4ControlArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 11),
    _SleV2Dhcp4ControlArpTimeout_Type()
)
sleV2Dhcp4ControlArpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlArpTimeout.setStatus("current")


class _SleV2Dhcp4ControlPingRetransmits_Type(Integer32):
    """Custom type sleV2Dhcp4ControlPingRetransmits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_SleV2Dhcp4ControlPingRetransmits_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlPingRetransmits_Object = MibScalar
sleV2Dhcp4ControlPingRetransmits = _SleV2Dhcp4ControlPingRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 12),
    _SleV2Dhcp4ControlPingRetransmits_Type()
)
sleV2Dhcp4ControlPingRetransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlPingRetransmits.setStatus("current")


class _SleV2Dhcp4ControlPingTimeout_Type(Integer32):
    """Custom type sleV2Dhcp4ControlPingTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_SleV2Dhcp4ControlPingTimeout_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlPingTimeout_Object = MibScalar
sleV2Dhcp4ControlPingTimeout = _SleV2Dhcp4ControlPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 13),
    _SleV2Dhcp4ControlPingTimeout_Type()
)
sleV2Dhcp4ControlPingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlPingTimeout.setStatus("current")


class _SleV2Dhcp4ControlClassUsage_Type(Integer32):
    """Custom type sleV2Dhcp4ControlClassUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Dhcp4ControlClassUsage_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlClassUsage_Object = MibScalar
sleV2Dhcp4ControlClassUsage = _SleV2Dhcp4ControlClassUsage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 14),
    _SleV2Dhcp4ControlClassUsage_Type()
)
sleV2Dhcp4ControlClassUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlClassUsage.setStatus("current")


class _SleV2Dhcp4ControlSmartRelayUsage_Type(Integer32):
    """Custom type sleV2Dhcp4ControlSmartRelayUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Dhcp4ControlSmartRelayUsage_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlSmartRelayUsage_Object = MibScalar
sleV2Dhcp4ControlSmartRelayUsage = _SleV2Dhcp4ControlSmartRelayUsage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 15),
    _SleV2Dhcp4ControlSmartRelayUsage_Type()
)
sleV2Dhcp4ControlSmartRelayUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlSmartRelayUsage.setStatus("current")


class _SleV2Dhcp4ControlOption82Usage_Type(Integer32):
    """Custom type sleV2Dhcp4ControlOption82Usage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Dhcp4ControlOption82Usage_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlOption82Usage_Object = MibScalar
sleV2Dhcp4ControlOption82Usage = _SleV2Dhcp4ControlOption82Usage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 16),
    _SleV2Dhcp4ControlOption82Usage_Type()
)
sleV2Dhcp4ControlOption82Usage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlOption82Usage.setStatus("current")


class _SleV2Dhcp4ControlOption82Drop_Type(Integer32):
    """Custom type sleV2Dhcp4ControlOption82Drop based on Integer32"""
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
          ("normal", 1),
          ("option82", 2))
    )


_SleV2Dhcp4ControlOption82Drop_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlOption82Drop_Object = MibScalar
sleV2Dhcp4ControlOption82Drop = _SleV2Dhcp4ControlOption82Drop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 17),
    _SleV2Dhcp4ControlOption82Drop_Type()
)
sleV2Dhcp4ControlOption82Drop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlOption82Drop.setStatus("current")


class _SleV2Dhcp4ControlOption82Policy_Type(Integer32):
    """Custom type sleV2Dhcp4ControlOption82Policy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("keep", 0),
          ("replace", 1))
    )


_SleV2Dhcp4ControlOption82Policy_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlOption82Policy_Object = MibScalar
sleV2Dhcp4ControlOption82Policy = _SleV2Dhcp4ControlOption82Policy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 18),
    _SleV2Dhcp4ControlOption82Policy_Type()
)
sleV2Dhcp4ControlOption82Policy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlOption82Policy.setStatus("current")


class _SleV2Dhcp4ControlOption82TrustDefault_Type(Integer32):
    """Custom type sleV2Dhcp4ControlOption82TrustDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_SleV2Dhcp4ControlOption82TrustDefault_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlOption82TrustDefault_Object = MibScalar
sleV2Dhcp4ControlOption82TrustDefault = _SleV2Dhcp4ControlOption82TrustDefault_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 19),
    _SleV2Dhcp4ControlOption82TrustDefault_Type()
)
sleV2Dhcp4ControlOption82TrustDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlOption82TrustDefault.setStatus("current")


class _SleV2Dhcp4ControlOption82SystemRemoteType_Type(Integer32):
    """Custom type sleV2Dhcp4ControlOption82SystemRemoteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ipaddress", 1),
          ("hex", 2),
          ("text", 3),
          ("host", 4),
          ("index", 5),
          ("option", 6),
          ("undef", 255))
    )


_SleV2Dhcp4ControlOption82SystemRemoteType_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlOption82SystemRemoteType_Object = MibScalar
sleV2Dhcp4ControlOption82SystemRemoteType = _SleV2Dhcp4ControlOption82SystemRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 20),
    _SleV2Dhcp4ControlOption82SystemRemoteType_Type()
)
sleV2Dhcp4ControlOption82SystemRemoteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlOption82SystemRemoteType.setStatus("current")


class _SleV2Dhcp4ControlOption82SystemRemoteId_Type(OctetString):
    """Custom type sleV2Dhcp4ControlOption82SystemRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4ControlOption82SystemRemoteId_Type.__name__ = "OctetString"
_SleV2Dhcp4ControlOption82SystemRemoteId_Object = MibScalar
sleV2Dhcp4ControlOption82SystemRemoteId = _SleV2Dhcp4ControlOption82SystemRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 21),
    _SleV2Dhcp4ControlOption82SystemRemoteId_Type()
)
sleV2Dhcp4ControlOption82SystemRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlOption82SystemRemoteId.setStatus("current")


class _SleV2Dhcp4ControlDatabaseKey_Type(Integer32):
    """Custom type sleV2Dhcp4ControlDatabaseKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clientid", 0),
          ("hwaddress", 1))
    )


_SleV2Dhcp4ControlDatabaseKey_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlDatabaseKey_Object = MibScalar
sleV2Dhcp4ControlDatabaseKey = _SleV2Dhcp4ControlDatabaseKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 22),
    _SleV2Dhcp4ControlDatabaseKey_Type()
)
sleV2Dhcp4ControlDatabaseKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlDatabaseKey.setStatus("current")


class _SleV2Dhcp4ControlDebugStatus_Type(Bits):
    """Custom type sleV2Dhcp4ControlDebugStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugFilter", 0),
          ("debugLease", 1),
          ("debugPacket", 2),
          ("debugServices", 3))
    )

_SleV2Dhcp4ControlDebugStatus_Type.__name__ = "Bits"
_SleV2Dhcp4ControlDebugStatus_Object = MibScalar
sleV2Dhcp4ControlDebugStatus = _SleV2Dhcp4ControlDebugStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 23),
    _SleV2Dhcp4ControlDebugStatus_Type()
)
sleV2Dhcp4ControlDebugStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlDebugStatus.setStatus("current")


class _SleV2Dhcp4ControlAuthArpTime_Type(Integer32):
    """Custom type sleV2Dhcp4ControlAuthArpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483637),
    )


_SleV2Dhcp4ControlAuthArpTime_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlAuthArpTime_Object = MibScalar
sleV2Dhcp4ControlAuthArpTime = _SleV2Dhcp4ControlAuthArpTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 24),
    _SleV2Dhcp4ControlAuthArpTime_Type()
)
sleV2Dhcp4ControlAuthArpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlAuthArpTime.setStatus("current")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlAuthArpTime.setUnits("second")
_SleV2Dhcp4ControlClientHardwareAddress_Type = Boolean
_SleV2Dhcp4ControlClientHardwareAddress_Object = MibScalar
sleV2Dhcp4ControlClientHardwareAddress = _SleV2Dhcp4ControlClientHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 25),
    _SleV2Dhcp4ControlClientHardwareAddress_Type()
)
sleV2Dhcp4ControlClientHardwareAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlClientHardwareAddress.setStatus("current")


class _SleV2Dhcp4ControlPEStatus_Type(Integer32):
    """Custom type sleV2Dhcp4ControlPEStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Dhcp4ControlPEStatus_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlPEStatus_Object = MibScalar
sleV2Dhcp4ControlPEStatus = _SleV2Dhcp4ControlPEStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 26),
    _SleV2Dhcp4ControlPEStatus_Type()
)
sleV2Dhcp4ControlPEStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlPEStatus.setStatus("current")


class _SleV2Dhcp4ControlAuthArpReadyTime_Type(Integer32):
    """Custom type sleV2Dhcp4ControlAuthArpReadyTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483637),
    )


_SleV2Dhcp4ControlAuthArpReadyTime_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlAuthArpReadyTime_Object = MibScalar
sleV2Dhcp4ControlAuthArpReadyTime = _SleV2Dhcp4ControlAuthArpReadyTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 27),
    _SleV2Dhcp4ControlAuthArpReadyTime_Type()
)
sleV2Dhcp4ControlAuthArpReadyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlAuthArpReadyTime.setStatus("current")


class _SleV2Dhcp4ControlOption82SystemRemoteOption_Type(OctetString):
    """Custom type sleV2Dhcp4ControlOption82SystemRemoteOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SleV2Dhcp4ControlOption82SystemRemoteOption_Type.__name__ = "OctetString"
_SleV2Dhcp4ControlOption82SystemRemoteOption_Object = MibScalar
sleV2Dhcp4ControlOption82SystemRemoteOption = _SleV2Dhcp4ControlOption82SystemRemoteOption_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 28),
    _SleV2Dhcp4ControlOption82SystemRemoteOption_Type()
)
sleV2Dhcp4ControlOption82SystemRemoteOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlOption82SystemRemoteOption.setStatus("current")


class _SleV2Dhcp4ControlOption82SystemCircuitPortType_Type(Integer32):
    """Custom type sleV2Dhcp4ControlOption82SystemCircuitPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("physical", 1),
          ("logical", 2))
    )


_SleV2Dhcp4ControlOption82SystemCircuitPortType_Type.__name__ = "Integer32"
_SleV2Dhcp4ControlOption82SystemCircuitPortType_Object = MibScalar
sleV2Dhcp4ControlOption82SystemCircuitPortType = _SleV2Dhcp4ControlOption82SystemCircuitPortType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 2, 29),
    _SleV2Dhcp4ControlOption82SystemCircuitPortType_Type()
)
sleV2Dhcp4ControlOption82SystemCircuitPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ControlOption82SystemCircuitPortType.setStatus("current")
_SleV2Dhcp4Notification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Notification = _SleV2Dhcp4Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3)
)
_SleV2Dhcp4Pool_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Pool = _SleV2Dhcp4Pool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2)
)
_SleV2Dhcp4PoolBase_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PoolBase = _SleV2Dhcp4PoolBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1)
)
_SleV2Dhcp4PoolTable_Object = MibTable
sleV2Dhcp4PoolTable = _SleV2Dhcp4PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolTable.setStatus("current")
_SleV2Dhcp4PoolEntry_Object = MibTableRow
sleV2Dhcp4PoolEntry = _SleV2Dhcp4PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1, 1)
)
sleV2Dhcp4PoolEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PoolIndex"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolEntry.setStatus("current")


class _SleV2Dhcp4PoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4PoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4PoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4PoolIndex_Object = MibTableColumn
sleV2Dhcp4PoolIndex = _SleV2Dhcp4PoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1, 1, 1),
    _SleV2Dhcp4PoolIndex_Type()
)
sleV2Dhcp4PoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolIndex.setStatus("current")


class _SleV2Dhcp4PoolName_Type(OctetString):
    """Custom type sleV2Dhcp4PoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4PoolName_Type.__name__ = "OctetString"
_SleV2Dhcp4PoolName_Object = MibTableColumn
sleV2Dhcp4PoolName = _SleV2Dhcp4PoolName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1, 1, 2),
    _SleV2Dhcp4PoolName_Type()
)
sleV2Dhcp4PoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolName.setStatus("current")


class _SleV2Dhcp4PoolDefaultLeaseTime_Type(Integer32):
    """Custom type sleV2Dhcp4PoolDefaultLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483637),
    )


_SleV2Dhcp4PoolDefaultLeaseTime_Type.__name__ = "Integer32"
_SleV2Dhcp4PoolDefaultLeaseTime_Object = MibTableColumn
sleV2Dhcp4PoolDefaultLeaseTime = _SleV2Dhcp4PoolDefaultLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1, 1, 3),
    _SleV2Dhcp4PoolDefaultLeaseTime_Type()
)
sleV2Dhcp4PoolDefaultLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolDefaultLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolDefaultLeaseTime.setUnits("second")


class _SleV2Dhcp4PoolMaxLeaseTime_Type(Integer32):
    """Custom type sleV2Dhcp4PoolMaxLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483637),
    )


_SleV2Dhcp4PoolMaxLeaseTime_Type.__name__ = "Integer32"
_SleV2Dhcp4PoolMaxLeaseTime_Object = MibTableColumn
sleV2Dhcp4PoolMaxLeaseTime = _SleV2Dhcp4PoolMaxLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1, 1, 4),
    _SleV2Dhcp4PoolMaxLeaseTime_Type()
)
sleV2Dhcp4PoolMaxLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolMaxLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolMaxLeaseTime.setUnits("second")


class _SleV2Dhcp4PoolDomainName_Type(OctetString):
    """Custom type sleV2Dhcp4PoolDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4PoolDomainName_Type.__name__ = "OctetString"
_SleV2Dhcp4PoolDomainName_Object = MibTableColumn
sleV2Dhcp4PoolDomainName = _SleV2Dhcp4PoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1, 1, 5),
    _SleV2Dhcp4PoolDomainName_Type()
)
sleV2Dhcp4PoolDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolDomainName.setStatus("current")
_SleV2Dhcp4PoolSummaryTotal_Type = Unsigned32
_SleV2Dhcp4PoolSummaryTotal_Object = MibTableColumn
sleV2Dhcp4PoolSummaryTotal = _SleV2Dhcp4PoolSummaryTotal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1, 1, 6),
    _SleV2Dhcp4PoolSummaryTotal_Type()
)
sleV2Dhcp4PoolSummaryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolSummaryTotal.setStatus("current")
_SleV2Dhcp4PoolSummaryAllocated_Type = Unsigned32
_SleV2Dhcp4PoolSummaryAllocated_Object = MibTableColumn
sleV2Dhcp4PoolSummaryAllocated = _SleV2Dhcp4PoolSummaryAllocated_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1, 1, 7),
    _SleV2Dhcp4PoolSummaryAllocated_Type()
)
sleV2Dhcp4PoolSummaryAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolSummaryAllocated.setStatus("current")
_SleV2Dhcp4PoolSummaryBound_Type = Unsigned32
_SleV2Dhcp4PoolSummaryBound_Object = MibTableColumn
sleV2Dhcp4PoolSummaryBound = _SleV2Dhcp4PoolSummaryBound_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1, 1, 8),
    _SleV2Dhcp4PoolSummaryBound_Type()
)
sleV2Dhcp4PoolSummaryBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolSummaryBound.setStatus("current")
_SleV2Dhcp4PoolSummaryOffered_Type = Unsigned32
_SleV2Dhcp4PoolSummaryOffered_Object = MibTableColumn
sleV2Dhcp4PoolSummaryOffered = _SleV2Dhcp4PoolSummaryOffered_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1, 1, 9),
    _SleV2Dhcp4PoolSummaryOffered_Type()
)
sleV2Dhcp4PoolSummaryOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolSummaryOffered.setStatus("current")
_SleV2Dhcp4PoolSummaryFixed_Type = Unsigned32
_SleV2Dhcp4PoolSummaryFixed_Object = MibTableColumn
sleV2Dhcp4PoolSummaryFixed = _SleV2Dhcp4PoolSummaryFixed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1, 1, 10),
    _SleV2Dhcp4PoolSummaryFixed_Type()
)
sleV2Dhcp4PoolSummaryFixed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolSummaryFixed.setStatus("current")
_SleV2Dhcp4PoolSummaryAbandon_Type = Unsigned32
_SleV2Dhcp4PoolSummaryAbandon_Object = MibTableColumn
sleV2Dhcp4PoolSummaryAbandon = _SleV2Dhcp4PoolSummaryAbandon_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1, 1, 11),
    _SleV2Dhcp4PoolSummaryAbandon_Type()
)
sleV2Dhcp4PoolSummaryAbandon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolSummaryAbandon.setStatus("current")
_SleV2Dhcp4PoolSummaryAvailable_Type = Unsigned32
_SleV2Dhcp4PoolSummaryAvailable_Object = MibTableColumn
sleV2Dhcp4PoolSummaryAvailable = _SleV2Dhcp4PoolSummaryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1, 1, 12),
    _SleV2Dhcp4PoolSummaryAvailable_Type()
)
sleV2Dhcp4PoolSummaryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolSummaryAvailable.setStatus("current")


class _SleV2Dhcp4PoolMeritDumpPath_Type(OctetString):
    """Custom type sleV2Dhcp4PoolMeritDumpPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleV2Dhcp4PoolMeritDumpPath_Type.__name__ = "OctetString"
_SleV2Dhcp4PoolMeritDumpPath_Object = MibTableColumn
sleV2Dhcp4PoolMeritDumpPath = _SleV2Dhcp4PoolMeritDumpPath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1, 1, 13),
    _SleV2Dhcp4PoolMeritDumpPath_Type()
)
sleV2Dhcp4PoolMeritDumpPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolMeritDumpPath.setStatus("current")


class _SleV2Dhcp4PoolRootPath_Type(OctetString):
    """Custom type sleV2Dhcp4PoolRootPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleV2Dhcp4PoolRootPath_Type.__name__ = "OctetString"
_SleV2Dhcp4PoolRootPath_Object = MibTableColumn
sleV2Dhcp4PoolRootPath = _SleV2Dhcp4PoolRootPath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1, 1, 14),
    _SleV2Dhcp4PoolRootPath_Type()
)
sleV2Dhcp4PoolRootPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolRootPath.setStatus("current")
_SleV2Dhcp4PoolSummaryNetwork_Type = Unsigned32
_SleV2Dhcp4PoolSummaryNetwork_Object = MibTableColumn
sleV2Dhcp4PoolSummaryNetwork = _SleV2Dhcp4PoolSummaryNetwork_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 1, 1, 15),
    _SleV2Dhcp4PoolSummaryNetwork_Type()
)
sleV2Dhcp4PoolSummaryNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolSummaryNetwork.setStatus("current")
_SleV2Dhcp4PoolControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PoolControl = _SleV2Dhcp4PoolControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 2)
)


class _SleV2Dhcp4PoolControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4PoolControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("createDhcpPool", 1),
          ("destroyDhcpPool", 2),
          ("setPoolDhcpLeaseTimeProfile", 3),
          ("setPoolDhcpDomainName", 4),
          ("setPoolDhcpOriginProfile", 5),
          ("setPoolDhcpMeritDumpPath", 6),
          ("setPoolDhcpRootPath", 7))
    )


_SleV2Dhcp4PoolControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4PoolControlRequest_Object = MibScalar
sleV2Dhcp4PoolControlRequest = _SleV2Dhcp4PoolControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 2, 1),
    _SleV2Dhcp4PoolControlRequest_Type()
)
sleV2Dhcp4PoolControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolControlRequest.setStatus("current")
_SleV2Dhcp4PoolControlStatus_Type = SleControlStatusType
_SleV2Dhcp4PoolControlStatus_Object = MibScalar
sleV2Dhcp4PoolControlStatus = _SleV2Dhcp4PoolControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 2, 2),
    _SleV2Dhcp4PoolControlStatus_Type()
)
sleV2Dhcp4PoolControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolControlStatus.setStatus("current")
_SleV2Dhcp4PoolControlTimer_Type = Gauge32
_SleV2Dhcp4PoolControlTimer_Object = MibScalar
sleV2Dhcp4PoolControlTimer = _SleV2Dhcp4PoolControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 2, 3),
    _SleV2Dhcp4PoolControlTimer_Type()
)
sleV2Dhcp4PoolControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolControlTimer.setStatus("current")
_SleV2Dhcp4PoolControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4PoolControlTimeStamp_Object = MibScalar
sleV2Dhcp4PoolControlTimeStamp = _SleV2Dhcp4PoolControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 2, 4),
    _SleV2Dhcp4PoolControlTimeStamp_Type()
)
sleV2Dhcp4PoolControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolControlTimeStamp.setStatus("current")
_SleV2Dhcp4PoolControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4PoolControlReqResult_Object = MibScalar
sleV2Dhcp4PoolControlReqResult = _SleV2Dhcp4PoolControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 2, 5),
    _SleV2Dhcp4PoolControlReqResult_Type()
)
sleV2Dhcp4PoolControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolControlReqResult.setStatus("current")


class _SleV2Dhcp4PoolControlIndex_Type(Integer32):
    """Custom type sleV2Dhcp4PoolControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4PoolControlIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4PoolControlIndex_Object = MibScalar
sleV2Dhcp4PoolControlIndex = _SleV2Dhcp4PoolControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 2, 6),
    _SleV2Dhcp4PoolControlIndex_Type()
)
sleV2Dhcp4PoolControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolControlIndex.setStatus("current")


class _SleV2Dhcp4PoolControlName_Type(OctetString):
    """Custom type sleV2Dhcp4PoolControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4PoolControlName_Type.__name__ = "OctetString"
_SleV2Dhcp4PoolControlName_Object = MibScalar
sleV2Dhcp4PoolControlName = _SleV2Dhcp4PoolControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 2, 7),
    _SleV2Dhcp4PoolControlName_Type()
)
sleV2Dhcp4PoolControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolControlName.setStatus("current")


class _SleV2Dhcp4PoolControlDefaultLeaseTime_Type(Integer32):
    """Custom type sleV2Dhcp4PoolControlDefaultLeaseTime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483637),
    )


_SleV2Dhcp4PoolControlDefaultLeaseTime_Type.__name__ = "Integer32"
_SleV2Dhcp4PoolControlDefaultLeaseTime_Object = MibScalar
sleV2Dhcp4PoolControlDefaultLeaseTime = _SleV2Dhcp4PoolControlDefaultLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 2, 8),
    _SleV2Dhcp4PoolControlDefaultLeaseTime_Type()
)
sleV2Dhcp4PoolControlDefaultLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolControlDefaultLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolControlDefaultLeaseTime.setUnits("second")


class _SleV2Dhcp4PoolControlMaxLeaseTime_Type(Integer32):
    """Custom type sleV2Dhcp4PoolControlMaxLeaseTime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483637),
    )


_SleV2Dhcp4PoolControlMaxLeaseTime_Type.__name__ = "Integer32"
_SleV2Dhcp4PoolControlMaxLeaseTime_Object = MibScalar
sleV2Dhcp4PoolControlMaxLeaseTime = _SleV2Dhcp4PoolControlMaxLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 2, 9),
    _SleV2Dhcp4PoolControlMaxLeaseTime_Type()
)
sleV2Dhcp4PoolControlMaxLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolControlMaxLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolControlMaxLeaseTime.setUnits("second")


class _SleV2Dhcp4PoolControlDomainName_Type(OctetString):
    """Custom type sleV2Dhcp4PoolControlDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4PoolControlDomainName_Type.__name__ = "OctetString"
_SleV2Dhcp4PoolControlDomainName_Object = MibScalar
sleV2Dhcp4PoolControlDomainName = _SleV2Dhcp4PoolControlDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 2, 10),
    _SleV2Dhcp4PoolControlDomainName_Type()
)
sleV2Dhcp4PoolControlDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolControlDomainName.setStatus("current")
_SleV2Dhcp4PoolControlOriginURL_Type = IpAddress
_SleV2Dhcp4PoolControlOriginURL_Object = MibScalar
sleV2Dhcp4PoolControlOriginURL = _SleV2Dhcp4PoolControlOriginURL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 2, 11),
    _SleV2Dhcp4PoolControlOriginURL_Type()
)
sleV2Dhcp4PoolControlOriginURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolControlOriginURL.setStatus("current")


class _SleV2Dhcp4PoolControlOriginFileName_Type(OctetString):
    """Custom type sleV2Dhcp4PoolControlOriginFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4PoolControlOriginFileName_Type.__name__ = "OctetString"
_SleV2Dhcp4PoolControlOriginFileName_Object = MibScalar
sleV2Dhcp4PoolControlOriginFileName = _SleV2Dhcp4PoolControlOriginFileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 2, 12),
    _SleV2Dhcp4PoolControlOriginFileName_Type()
)
sleV2Dhcp4PoolControlOriginFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolControlOriginFileName.setStatus("current")


class _SleV2Dhcp4PoolControlMeritDumpPath_Type(OctetString):
    """Custom type sleV2Dhcp4PoolControlMeritDumpPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleV2Dhcp4PoolControlMeritDumpPath_Type.__name__ = "OctetString"
_SleV2Dhcp4PoolControlMeritDumpPath_Object = MibScalar
sleV2Dhcp4PoolControlMeritDumpPath = _SleV2Dhcp4PoolControlMeritDumpPath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 2, 13),
    _SleV2Dhcp4PoolControlMeritDumpPath_Type()
)
sleV2Dhcp4PoolControlMeritDumpPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolControlMeritDumpPath.setStatus("current")


class _SleV2Dhcp4PoolControlRootPath_Type(OctetString):
    """Custom type sleV2Dhcp4PoolControlRootPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleV2Dhcp4PoolControlRootPath_Type.__name__ = "OctetString"
_SleV2Dhcp4PoolControlRootPath_Object = MibScalar
sleV2Dhcp4PoolControlRootPath = _SleV2Dhcp4PoolControlRootPath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 2, 14),
    _SleV2Dhcp4PoolControlRootPath_Type()
)
sleV2Dhcp4PoolControlRootPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolControlRootPath.setStatus("current")
_SleV2Dhcp4PoolNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PoolNotification = _SleV2Dhcp4PoolNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 3)
)
_SleV2Dhcp4Network_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Network = _SleV2Dhcp4Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2)
)
_SleV2Dhcp4NetworkTable_Object = MibTable
sleV2Dhcp4NetworkTable = _SleV2Dhcp4NetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4NetworkTable.setStatus("current")
_SleV2Dhcp4NetworkEntry_Object = MibTableRow
sleV2Dhcp4NetworkEntry = _SleV2Dhcp4NetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2, 1, 1)
)
sleV2Dhcp4NetworkEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PoolIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkAddress"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkMask"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4NetworkEntry.setStatus("current")
_SleV2Dhcp4NetworkAddress_Type = IpAddress
_SleV2Dhcp4NetworkAddress_Object = MibTableColumn
sleV2Dhcp4NetworkAddress = _SleV2Dhcp4NetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2, 1, 1, 1),
    _SleV2Dhcp4NetworkAddress_Type()
)
sleV2Dhcp4NetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4NetworkAddress.setStatus("current")


class _SleV2Dhcp4NetworkMask_Type(Integer32):
    """Custom type sleV2Dhcp4NetworkMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleV2Dhcp4NetworkMask_Type.__name__ = "Integer32"
_SleV2Dhcp4NetworkMask_Object = MibTableColumn
sleV2Dhcp4NetworkMask = _SleV2Dhcp4NetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2, 1, 1, 2),
    _SleV2Dhcp4NetworkMask_Type()
)
sleV2Dhcp4NetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4NetworkMask.setStatus("current")
_SleV2Dhcp4NetworkControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4NetworkControl = _SleV2Dhcp4NetworkControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2, 2)
)


class _SleV2Dhcp4NetworkControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4NetworkControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcpNetwork", 1),
          ("destroyDhcpNetwork", 2))
    )


_SleV2Dhcp4NetworkControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4NetworkControlRequest_Object = MibScalar
sleV2Dhcp4NetworkControlRequest = _SleV2Dhcp4NetworkControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2, 2, 1),
    _SleV2Dhcp4NetworkControlRequest_Type()
)
sleV2Dhcp4NetworkControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4NetworkControlRequest.setStatus("current")
_SleV2Dhcp4NetworkControlStatus_Type = SleControlStatusType
_SleV2Dhcp4NetworkControlStatus_Object = MibScalar
sleV2Dhcp4NetworkControlStatus = _SleV2Dhcp4NetworkControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2, 2, 2),
    _SleV2Dhcp4NetworkControlStatus_Type()
)
sleV2Dhcp4NetworkControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4NetworkControlStatus.setStatus("current")
_SleV2Dhcp4NetworkControlTimer_Type = Gauge32
_SleV2Dhcp4NetworkControlTimer_Object = MibScalar
sleV2Dhcp4NetworkControlTimer = _SleV2Dhcp4NetworkControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2, 2, 3),
    _SleV2Dhcp4NetworkControlTimer_Type()
)
sleV2Dhcp4NetworkControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4NetworkControlTimer.setStatus("current")
_SleV2Dhcp4NetworkControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4NetworkControlTimeStamp_Object = MibScalar
sleV2Dhcp4NetworkControlTimeStamp = _SleV2Dhcp4NetworkControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2, 2, 4),
    _SleV2Dhcp4NetworkControlTimeStamp_Type()
)
sleV2Dhcp4NetworkControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4NetworkControlTimeStamp.setStatus("current")
_SleV2Dhcp4NetworkControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4NetworkControlReqResult_Object = MibScalar
sleV2Dhcp4NetworkControlReqResult = _SleV2Dhcp4NetworkControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2, 2, 5),
    _SleV2Dhcp4NetworkControlReqResult_Type()
)
sleV2Dhcp4NetworkControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4NetworkControlReqResult.setStatus("current")


class _SleV2Dhcp4NetworkControlPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4NetworkControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4NetworkControlPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4NetworkControlPoolIndex_Object = MibScalar
sleV2Dhcp4NetworkControlPoolIndex = _SleV2Dhcp4NetworkControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2, 2, 6),
    _SleV2Dhcp4NetworkControlPoolIndex_Type()
)
sleV2Dhcp4NetworkControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4NetworkControlPoolIndex.setStatus("current")
_SleV2Dhcp4NetworkControlAddress_Type = IpAddress
_SleV2Dhcp4NetworkControlAddress_Object = MibScalar
sleV2Dhcp4NetworkControlAddress = _SleV2Dhcp4NetworkControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2, 2, 7),
    _SleV2Dhcp4NetworkControlAddress_Type()
)
sleV2Dhcp4NetworkControlAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4NetworkControlAddress.setStatus("current")


class _SleV2Dhcp4NetworkControlMask_Type(Integer32):
    """Custom type sleV2Dhcp4NetworkControlMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleV2Dhcp4NetworkControlMask_Type.__name__ = "Integer32"
_SleV2Dhcp4NetworkControlMask_Object = MibScalar
sleV2Dhcp4NetworkControlMask = _SleV2Dhcp4NetworkControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2, 2, 8),
    _SleV2Dhcp4NetworkControlMask_Type()
)
sleV2Dhcp4NetworkControlMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4NetworkControlMask.setStatus("current")
_SleV2Dhcp4NetworkNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4NetworkNotification = _SleV2Dhcp4NetworkNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2, 3)
)
_SleV2Dhcp4Range_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Range = _SleV2Dhcp4Range_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3)
)
_SleV2Dhcp4RangeTable_Object = MibTable
sleV2Dhcp4RangeTable = _SleV2Dhcp4RangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RangeTable.setStatus("current")
_SleV2Dhcp4RangeEntry_Object = MibTableRow
sleV2Dhcp4RangeEntry = _SleV2Dhcp4RangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3, 1, 1)
)
sleV2Dhcp4RangeEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PoolIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4RangeStart"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4RangeEnd"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RangeEntry.setStatus("current")
_SleV2Dhcp4RangeStart_Type = IpAddress
_SleV2Dhcp4RangeStart_Object = MibTableColumn
sleV2Dhcp4RangeStart = _SleV2Dhcp4RangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3, 1, 1, 1),
    _SleV2Dhcp4RangeStart_Type()
)
sleV2Dhcp4RangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RangeStart.setStatus("current")
_SleV2Dhcp4RangeEnd_Type = IpAddress
_SleV2Dhcp4RangeEnd_Object = MibTableColumn
sleV2Dhcp4RangeEnd = _SleV2Dhcp4RangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3, 1, 1, 2),
    _SleV2Dhcp4RangeEnd_Type()
)
sleV2Dhcp4RangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RangeEnd.setStatus("current")
_SleV2Dhcp4RangeControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RangeControl = _SleV2Dhcp4RangeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3, 2)
)


class _SleV2Dhcp4RangeControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4RangeControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcpRange", 1),
          ("destroyDhcpRange", 2))
    )


_SleV2Dhcp4RangeControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4RangeControlRequest_Object = MibScalar
sleV2Dhcp4RangeControlRequest = _SleV2Dhcp4RangeControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3, 2, 1),
    _SleV2Dhcp4RangeControlRequest_Type()
)
sleV2Dhcp4RangeControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RangeControlRequest.setStatus("current")
_SleV2Dhcp4RangeControlStatus_Type = SleControlStatusType
_SleV2Dhcp4RangeControlStatus_Object = MibScalar
sleV2Dhcp4RangeControlStatus = _SleV2Dhcp4RangeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3, 2, 2),
    _SleV2Dhcp4RangeControlStatus_Type()
)
sleV2Dhcp4RangeControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RangeControlStatus.setStatus("current")
_SleV2Dhcp4RangeControlTimer_Type = Gauge32
_SleV2Dhcp4RangeControlTimer_Object = MibScalar
sleV2Dhcp4RangeControlTimer = _SleV2Dhcp4RangeControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3, 2, 3),
    _SleV2Dhcp4RangeControlTimer_Type()
)
sleV2Dhcp4RangeControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RangeControlTimer.setStatus("current")
_SleV2Dhcp4RangeControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4RangeControlTimeStamp_Object = MibScalar
sleV2Dhcp4RangeControlTimeStamp = _SleV2Dhcp4RangeControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3, 2, 4),
    _SleV2Dhcp4RangeControlTimeStamp_Type()
)
sleV2Dhcp4RangeControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RangeControlTimeStamp.setStatus("current")
_SleV2Dhcp4RangeControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4RangeControlReqResult_Object = MibScalar
sleV2Dhcp4RangeControlReqResult = _SleV2Dhcp4RangeControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3, 2, 5),
    _SleV2Dhcp4RangeControlReqResult_Type()
)
sleV2Dhcp4RangeControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RangeControlReqResult.setStatus("current")


class _SleV2Dhcp4RangeControlPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4RangeControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4RangeControlPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4RangeControlPoolIndex_Object = MibScalar
sleV2Dhcp4RangeControlPoolIndex = _SleV2Dhcp4RangeControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3, 2, 6),
    _SleV2Dhcp4RangeControlPoolIndex_Type()
)
sleV2Dhcp4RangeControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RangeControlPoolIndex.setStatus("current")
_SleV2Dhcp4RangeControlStart_Type = IpAddress
_SleV2Dhcp4RangeControlStart_Object = MibScalar
sleV2Dhcp4RangeControlStart = _SleV2Dhcp4RangeControlStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3, 2, 7),
    _SleV2Dhcp4RangeControlStart_Type()
)
sleV2Dhcp4RangeControlStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RangeControlStart.setStatus("current")
_SleV2Dhcp4RangeControlEnd_Type = IpAddress
_SleV2Dhcp4RangeControlEnd_Object = MibScalar
sleV2Dhcp4RangeControlEnd = _SleV2Dhcp4RangeControlEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3, 2, 8),
    _SleV2Dhcp4RangeControlEnd_Type()
)
sleV2Dhcp4RangeControlEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RangeControlEnd.setStatus("current")
_SleV2Dhcp4RangeNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RangeNotification = _SleV2Dhcp4RangeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3, 3)
)
_SleV2Dhcp4Fixed_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Fixed = _SleV2Dhcp4Fixed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4)
)
_SleV2Dhcp4FixedTable_Object = MibTable
sleV2Dhcp4FixedTable = _SleV2Dhcp4FixedTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4FixedTable.setStatus("current")
_SleV2Dhcp4FixedEntry_Object = MibTableRow
sleV2Dhcp4FixedEntry = _SleV2Dhcp4FixedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4, 1, 1)
)
sleV2Dhcp4FixedEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PoolIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4FixedMac"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4FixedAddress"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4FixedEntry.setStatus("current")
_SleV2Dhcp4FixedMac_Type = MacAddress
_SleV2Dhcp4FixedMac_Object = MibTableColumn
sleV2Dhcp4FixedMac = _SleV2Dhcp4FixedMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4, 1, 1, 1),
    _SleV2Dhcp4FixedMac_Type()
)
sleV2Dhcp4FixedMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4FixedMac.setStatus("current")
_SleV2Dhcp4FixedAddress_Type = IpAddress
_SleV2Dhcp4FixedAddress_Object = MibTableColumn
sleV2Dhcp4FixedAddress = _SleV2Dhcp4FixedAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4, 1, 1, 2),
    _SleV2Dhcp4FixedAddress_Type()
)
sleV2Dhcp4FixedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4FixedAddress.setStatus("current")
_SleV2Dhcp4FixedControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4FixedControl = _SleV2Dhcp4FixedControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4, 2)
)


class _SleV2Dhcp4FixedControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4FixedControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcpFixed", 1),
          ("destroyDhcpFixed", 2))
    )


_SleV2Dhcp4FixedControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4FixedControlRequest_Object = MibScalar
sleV2Dhcp4FixedControlRequest = _SleV2Dhcp4FixedControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4, 2, 1),
    _SleV2Dhcp4FixedControlRequest_Type()
)
sleV2Dhcp4FixedControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4FixedControlRequest.setStatus("current")
_SleV2Dhcp4FixedControlStatus_Type = SleControlStatusType
_SleV2Dhcp4FixedControlStatus_Object = MibScalar
sleV2Dhcp4FixedControlStatus = _SleV2Dhcp4FixedControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4, 2, 2),
    _SleV2Dhcp4FixedControlStatus_Type()
)
sleV2Dhcp4FixedControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4FixedControlStatus.setStatus("current")
_SleV2Dhcp4FixedControlTimer_Type = Gauge32
_SleV2Dhcp4FixedControlTimer_Object = MibScalar
sleV2Dhcp4FixedControlTimer = _SleV2Dhcp4FixedControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4, 2, 3),
    _SleV2Dhcp4FixedControlTimer_Type()
)
sleV2Dhcp4FixedControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4FixedControlTimer.setStatus("current")
_SleV2Dhcp4FixedControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4FixedControlTimeStamp_Object = MibScalar
sleV2Dhcp4FixedControlTimeStamp = _SleV2Dhcp4FixedControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4, 2, 4),
    _SleV2Dhcp4FixedControlTimeStamp_Type()
)
sleV2Dhcp4FixedControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4FixedControlTimeStamp.setStatus("current")
_SleV2Dhcp4FixedControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4FixedControlReqResult_Object = MibScalar
sleV2Dhcp4FixedControlReqResult = _SleV2Dhcp4FixedControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4, 2, 5),
    _SleV2Dhcp4FixedControlReqResult_Type()
)
sleV2Dhcp4FixedControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4FixedControlReqResult.setStatus("current")


class _SleV2Dhcp4FixedControlPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4FixedControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4FixedControlPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4FixedControlPoolIndex_Object = MibScalar
sleV2Dhcp4FixedControlPoolIndex = _SleV2Dhcp4FixedControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4, 2, 6),
    _SleV2Dhcp4FixedControlPoolIndex_Type()
)
sleV2Dhcp4FixedControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4FixedControlPoolIndex.setStatus("current")
_SleV2Dhcp4FixedControlAddress_Type = IpAddress
_SleV2Dhcp4FixedControlAddress_Object = MibScalar
sleV2Dhcp4FixedControlAddress = _SleV2Dhcp4FixedControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4, 2, 7),
    _SleV2Dhcp4FixedControlAddress_Type()
)
sleV2Dhcp4FixedControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4FixedControlAddress.setStatus("current")
_SleV2Dhcp4FixedControlMac_Type = MacAddress
_SleV2Dhcp4FixedControlMac_Object = MibScalar
sleV2Dhcp4FixedControlMac = _SleV2Dhcp4FixedControlMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4, 2, 8),
    _SleV2Dhcp4FixedControlMac_Type()
)
sleV2Dhcp4FixedControlMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4FixedControlMac.setStatus("current")
_SleV2Dhcp4FixedNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4FixedNotification = _SleV2Dhcp4FixedNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4, 3)
)
_SleV2Dhcp4Dns_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Dns = _SleV2Dhcp4Dns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5)
)
_SleV2Dhcp4DnsTable_Object = MibTable
sleV2Dhcp4DnsTable = _SleV2Dhcp4DnsTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4DnsTable.setStatus("current")
_SleV2Dhcp4DnsEntry_Object = MibTableRow
sleV2Dhcp4DnsEntry = _SleV2Dhcp4DnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5, 1, 1)
)
sleV2Dhcp4DnsEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PoolIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4DnsIndex"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4DnsEntry.setStatus("current")


class _SleV2Dhcp4DnsIndex_Type(Integer32):
    """Custom type sleV2Dhcp4DnsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleV2Dhcp4DnsIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4DnsIndex_Object = MibTableColumn
sleV2Dhcp4DnsIndex = _SleV2Dhcp4DnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5, 1, 1, 1),
    _SleV2Dhcp4DnsIndex_Type()
)
sleV2Dhcp4DnsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4DnsIndex.setStatus("current")
_SleV2Dhcp4DnsAddress_Type = IpAddress
_SleV2Dhcp4DnsAddress_Object = MibTableColumn
sleV2Dhcp4DnsAddress = _SleV2Dhcp4DnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5, 1, 1, 2),
    _SleV2Dhcp4DnsAddress_Type()
)
sleV2Dhcp4DnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4DnsAddress.setStatus("current")
_SleV2Dhcp4DnsControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4DnsControl = _SleV2Dhcp4DnsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5, 2)
)


class _SleV2Dhcp4DnsControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4DnsControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcpDns", 1),
          ("destroyDhcpDns", 2))
    )


_SleV2Dhcp4DnsControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4DnsControlRequest_Object = MibScalar
sleV2Dhcp4DnsControlRequest = _SleV2Dhcp4DnsControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5, 2, 1),
    _SleV2Dhcp4DnsControlRequest_Type()
)
sleV2Dhcp4DnsControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4DnsControlRequest.setStatus("current")
_SleV2Dhcp4DnsControlStatus_Type = SleControlStatusType
_SleV2Dhcp4DnsControlStatus_Object = MibScalar
sleV2Dhcp4DnsControlStatus = _SleV2Dhcp4DnsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5, 2, 2),
    _SleV2Dhcp4DnsControlStatus_Type()
)
sleV2Dhcp4DnsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4DnsControlStatus.setStatus("current")
_SleV2Dhcp4DnsControlTimer_Type = Gauge32
_SleV2Dhcp4DnsControlTimer_Object = MibScalar
sleV2Dhcp4DnsControlTimer = _SleV2Dhcp4DnsControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5, 2, 3),
    _SleV2Dhcp4DnsControlTimer_Type()
)
sleV2Dhcp4DnsControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4DnsControlTimer.setStatus("current")
_SleV2Dhcp4DnsControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4DnsControlTimeStamp_Object = MibScalar
sleV2Dhcp4DnsControlTimeStamp = _SleV2Dhcp4DnsControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5, 2, 4),
    _SleV2Dhcp4DnsControlTimeStamp_Type()
)
sleV2Dhcp4DnsControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4DnsControlTimeStamp.setStatus("current")
_SleV2Dhcp4DnsControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4DnsControlReqResult_Object = MibScalar
sleV2Dhcp4DnsControlReqResult = _SleV2Dhcp4DnsControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5, 2, 5),
    _SleV2Dhcp4DnsControlReqResult_Type()
)
sleV2Dhcp4DnsControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4DnsControlReqResult.setStatus("current")


class _SleV2Dhcp4DnsControlPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4DnsControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4DnsControlPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4DnsControlPoolIndex_Object = MibScalar
sleV2Dhcp4DnsControlPoolIndex = _SleV2Dhcp4DnsControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5, 2, 6),
    _SleV2Dhcp4DnsControlPoolIndex_Type()
)
sleV2Dhcp4DnsControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4DnsControlPoolIndex.setStatus("current")


class _SleV2Dhcp4DnsControlIndex_Type(Integer32):
    """Custom type sleV2Dhcp4DnsControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )


_SleV2Dhcp4DnsControlIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4DnsControlIndex_Object = MibScalar
sleV2Dhcp4DnsControlIndex = _SleV2Dhcp4DnsControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5, 2, 7),
    _SleV2Dhcp4DnsControlIndex_Type()
)
sleV2Dhcp4DnsControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4DnsControlIndex.setStatus("current")
_SleV2Dhcp4DnsControlAddress_Type = IpAddress
_SleV2Dhcp4DnsControlAddress_Object = MibScalar
sleV2Dhcp4DnsControlAddress = _SleV2Dhcp4DnsControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5, 2, 8),
    _SleV2Dhcp4DnsControlAddress_Type()
)
sleV2Dhcp4DnsControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4DnsControlAddress.setStatus("current")
_SleV2Dhcp4DnsNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4DnsNotification = _SleV2Dhcp4DnsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5, 3)
)
_SleV2Dhcp4DefaultGateway_ObjectIdentity = ObjectIdentity
sleV2Dhcp4DefaultGateway = _SleV2Dhcp4DefaultGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6)
)
_SleV2Dhcp4DefaultGatewayTable_Object = MibTable
sleV2Dhcp4DefaultGatewayTable = _SleV2Dhcp4DefaultGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4DefaultGatewayTable.setStatus("current")
_SleV2Dhcp4DefaultGatewayEntry_Object = MibTableRow
sleV2Dhcp4DefaultGatewayEntry = _SleV2Dhcp4DefaultGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6, 1, 1)
)
sleV2Dhcp4DefaultGatewayEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PoolIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayIndex"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4DefaultGatewayEntry.setStatus("current")


class _SleV2Dhcp4DefaultGatewayIndex_Type(Integer32):
    """Custom type sleV2Dhcp4DefaultGatewayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleV2Dhcp4DefaultGatewayIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4DefaultGatewayIndex_Object = MibTableColumn
sleV2Dhcp4DefaultGatewayIndex = _SleV2Dhcp4DefaultGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6, 1, 1, 1),
    _SleV2Dhcp4DefaultGatewayIndex_Type()
)
sleV2Dhcp4DefaultGatewayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4DefaultGatewayIndex.setStatus("current")
_SleV2Dhcp4DefaultGatewayAddress_Type = IpAddress
_SleV2Dhcp4DefaultGatewayAddress_Object = MibTableColumn
sleV2Dhcp4DefaultGatewayAddress = _SleV2Dhcp4DefaultGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6, 1, 1, 2),
    _SleV2Dhcp4DefaultGatewayAddress_Type()
)
sleV2Dhcp4DefaultGatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4DefaultGatewayAddress.setStatus("current")
_SleV2Dhcp4DefaultGatewayControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4DefaultGatewayControl = _SleV2Dhcp4DefaultGatewayControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6, 2)
)


class _SleV2Dhcp4DefaultGatewayControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4DefaultGatewayControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcpDefaultGateway", 1),
          ("destroyDhcpDefaultGateway", 2))
    )


_SleV2Dhcp4DefaultGatewayControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4DefaultGatewayControlRequest_Object = MibScalar
sleV2Dhcp4DefaultGatewayControlRequest = _SleV2Dhcp4DefaultGatewayControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6, 2, 1),
    _SleV2Dhcp4DefaultGatewayControlRequest_Type()
)
sleV2Dhcp4DefaultGatewayControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4DefaultGatewayControlRequest.setStatus("current")
_SleV2Dhcp4DefaultGatewayControlStatus_Type = SleControlStatusType
_SleV2Dhcp4DefaultGatewayControlStatus_Object = MibScalar
sleV2Dhcp4DefaultGatewayControlStatus = _SleV2Dhcp4DefaultGatewayControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6, 2, 2),
    _SleV2Dhcp4DefaultGatewayControlStatus_Type()
)
sleV2Dhcp4DefaultGatewayControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4DefaultGatewayControlStatus.setStatus("current")
_SleV2Dhcp4DefaultGatewayControlTimer_Type = Gauge32
_SleV2Dhcp4DefaultGatewayControlTimer_Object = MibScalar
sleV2Dhcp4DefaultGatewayControlTimer = _SleV2Dhcp4DefaultGatewayControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6, 2, 3),
    _SleV2Dhcp4DefaultGatewayControlTimer_Type()
)
sleV2Dhcp4DefaultGatewayControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4DefaultGatewayControlTimer.setStatus("current")
_SleV2Dhcp4DefaultGatewayControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4DefaultGatewayControlTimeStamp_Object = MibScalar
sleV2Dhcp4DefaultGatewayControlTimeStamp = _SleV2Dhcp4DefaultGatewayControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6, 2, 4),
    _SleV2Dhcp4DefaultGatewayControlTimeStamp_Type()
)
sleV2Dhcp4DefaultGatewayControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4DefaultGatewayControlTimeStamp.setStatus("current")
_SleV2Dhcp4DefaultGatewayControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4DefaultGatewayControlReqResult_Object = MibScalar
sleV2Dhcp4DefaultGatewayControlReqResult = _SleV2Dhcp4DefaultGatewayControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6, 2, 5),
    _SleV2Dhcp4DefaultGatewayControlReqResult_Type()
)
sleV2Dhcp4DefaultGatewayControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4DefaultGatewayControlReqResult.setStatus("current")


class _SleV2Dhcp4DefaultGatewayControlPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4DefaultGatewayControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4DefaultGatewayControlPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4DefaultGatewayControlPoolIndex_Object = MibScalar
sleV2Dhcp4DefaultGatewayControlPoolIndex = _SleV2Dhcp4DefaultGatewayControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6, 2, 6),
    _SleV2Dhcp4DefaultGatewayControlPoolIndex_Type()
)
sleV2Dhcp4DefaultGatewayControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4DefaultGatewayControlPoolIndex.setStatus("current")


class _SleV2Dhcp4DefaultGatewayControlIndex_Type(Integer32):
    """Custom type sleV2Dhcp4DefaultGatewayControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )


_SleV2Dhcp4DefaultGatewayControlIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4DefaultGatewayControlIndex_Object = MibScalar
sleV2Dhcp4DefaultGatewayControlIndex = _SleV2Dhcp4DefaultGatewayControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6, 2, 7),
    _SleV2Dhcp4DefaultGatewayControlIndex_Type()
)
sleV2Dhcp4DefaultGatewayControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4DefaultGatewayControlIndex.setStatus("current")
_SleV2Dhcp4DefaultGatewayControlAddress_Type = IpAddress
_SleV2Dhcp4DefaultGatewayControlAddress_Object = MibScalar
sleV2Dhcp4DefaultGatewayControlAddress = _SleV2Dhcp4DefaultGatewayControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6, 2, 8),
    _SleV2Dhcp4DefaultGatewayControlAddress_Type()
)
sleV2Dhcp4DefaultGatewayControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4DefaultGatewayControlAddress.setStatus("current")
_SleV2Dhcp4DefaultGatewayNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4DefaultGatewayNotification = _SleV2Dhcp4DefaultGatewayNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6, 3)
)
_SleV2Dhcp4Option_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Option = _SleV2Dhcp4Option_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7)
)
_SleV2Dhcp4OptionTable_Object = MibTable
sleV2Dhcp4OptionTable = _SleV2Dhcp4OptionTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionTable.setStatus("current")
_SleV2Dhcp4OptionEntry_Object = MibTableRow
sleV2Dhcp4OptionEntry = _SleV2Dhcp4OptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 1, 1)
)
sleV2Dhcp4OptionEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PoolIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4OptionCode"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4OptionInstance"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionEntry.setStatus("current")


class _SleV2Dhcp4OptionCode_Type(Integer32):
    """Custom type sleV2Dhcp4OptionCode based on Integer32"""
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
              38,
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
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76)
        )
    )
    namedValues = NamedValues(
        *(("subnetMask", 1),
          ("timeOffset", 2),
          ("router", 3),
          ("timeServer", 4),
          ("nameServer", 5),
          ("domainNameServer", 6),
          ("logServer", 7),
          ("cookieServer", 8),
          ("lprServer", 9),
          ("impressServer", 10),
          ("resourceLocationServer", 11),
          ("hostName", 12),
          ("bootFileSize", 13),
          ("meritFile", 14),
          ("domainName", 15),
          ("swapServer", 16),
          ("rootPath", 17),
          ("extensionsPath", 18),
          ("ipForwardState", 19),
          ("nonLocalSourceRoutingState", 20),
          ("policyFilter", 21),
          ("maximumDatagramReassemblySize", 22),
          ("defaultIpTimeToLive", 23),
          ("pathMtuAgingTimeout", 24),
          ("pathMtuPlateauTable", 25),
          ("interfaceMtu", 26),
          ("allSubnetsAreLocal", 27),
          ("broadcastAddress", 28),
          ("performMaskDiscovery", 29),
          ("maskSupplier", 30),
          ("performRouterDiscovery", 31),
          ("routerSolicitationAddress", 32),
          ("staticRoute", 33),
          ("trailerEncapsulation", 34),
          ("arpCacheTimeout", 35),
          ("ethernetEncapsulationOption", 36),
          ("tcpDefaultTtl", 37),
          ("tcpKeepaliveInterval", 38),
          ("tcpKeepaliveGarbage", 39),
          ("nisDomain", 40),
          ("nisServers", 41),
          ("networkTimeProtocolServers", 42),
          ("vendorSpecificInformation", 43),
          ("netbiosOverTcpIpNameServer", 44),
          ("netbiosOverTcpIpDatagramDistributionServer", 45),
          ("netbiosOverTcpIpNodeType", 46),
          ("netbiosOverTcpIpScope", 47),
          ("xWindowSystemFontServer", 48),
          ("xWindowSystemDisplayManager", 49),
          ("requestedIpAddress", 50),
          ("ipAddressLeaseTime", 51),
          ("optionOverload", 52),
          ("dhcpMessageType", 53),
          ("serverIdentifier", 54),
          ("parameterRequestList", 55),
          ("message", 56),
          ("maximumDhcpMessageSize", 57),
          ("renewalTimeValue", 58),
          ("rebindingTimeValue", 59),
          ("vendorClassIdentifier", 60),
          ("clientIdentifier", 61),
          ("nisPlusDomain", 64),
          ("nisPlusServers", 65),
          ("tftpServerName", 66),
          ("bootFileName", 67),
          ("mobileIpHomeAgent", 68),
          ("smtpServer", 69),
          ("pop3Server", 70),
          ("nntpServer", 71),
          ("wwwServer", 72),
          ("defaultFingerServer", 73),
          ("ircServer", 74),
          ("streetTalkServer", 75),
          ("stdaServer", 76))
    )


_SleV2Dhcp4OptionCode_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionCode_Object = MibTableColumn
sleV2Dhcp4OptionCode = _SleV2Dhcp4OptionCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 1, 1, 1),
    _SleV2Dhcp4OptionCode_Type()
)
sleV2Dhcp4OptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionCode.setStatus("current")


class _SleV2Dhcp4OptionInstance_Type(Integer32):
    """Custom type sleV2Dhcp4OptionInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleV2Dhcp4OptionInstance_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionInstance_Object = MibTableColumn
sleV2Dhcp4OptionInstance = _SleV2Dhcp4OptionInstance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 1, 1, 2),
    _SleV2Dhcp4OptionInstance_Type()
)
sleV2Dhcp4OptionInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionInstance.setStatus("current")


class _SleV2Dhcp4OptionType_Type(Integer32):
    """Custom type sleV2Dhcp4OptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipaddress", 1),
          ("hex", 2),
          ("text", 3))
    )


_SleV2Dhcp4OptionType_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionType_Object = MibTableColumn
sleV2Dhcp4OptionType = _SleV2Dhcp4OptionType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 1, 1, 3),
    _SleV2Dhcp4OptionType_Type()
)
sleV2Dhcp4OptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionType.setStatus("current")


class _SleV2Dhcp4OptionValue_Type(OctetString):
    """Custom type sleV2Dhcp4OptionValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4OptionValue_Type.__name__ = "OctetString"
_SleV2Dhcp4OptionValue_Object = MibTableColumn
sleV2Dhcp4OptionValue = _SleV2Dhcp4OptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 1, 1, 4),
    _SleV2Dhcp4OptionValue_Type()
)
sleV2Dhcp4OptionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionValue.setStatus("current")
_SleV2Dhcp4OptionControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4OptionControl = _SleV2Dhcp4OptionControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 2)
)


class _SleV2Dhcp4OptionControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4OptionControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcpOption", 1),
          ("destoryDhcpOption", 2))
    )


_SleV2Dhcp4OptionControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionControlRequest_Object = MibScalar
sleV2Dhcp4OptionControlRequest = _SleV2Dhcp4OptionControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 2, 1),
    _SleV2Dhcp4OptionControlRequest_Type()
)
sleV2Dhcp4OptionControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionControlRequest.setStatus("current")
_SleV2Dhcp4OptionControlStatus_Type = SleControlStatusType
_SleV2Dhcp4OptionControlStatus_Object = MibScalar
sleV2Dhcp4OptionControlStatus = _SleV2Dhcp4OptionControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 2, 2),
    _SleV2Dhcp4OptionControlStatus_Type()
)
sleV2Dhcp4OptionControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionControlStatus.setStatus("current")
_SleV2Dhcp4OptionControlTimer_Type = Gauge32
_SleV2Dhcp4OptionControlTimer_Object = MibScalar
sleV2Dhcp4OptionControlTimer = _SleV2Dhcp4OptionControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 2, 3),
    _SleV2Dhcp4OptionControlTimer_Type()
)
sleV2Dhcp4OptionControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionControlTimer.setStatus("current")
_SleV2Dhcp4OptionControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4OptionControlTimeStamp_Object = MibScalar
sleV2Dhcp4OptionControlTimeStamp = _SleV2Dhcp4OptionControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 2, 4),
    _SleV2Dhcp4OptionControlTimeStamp_Type()
)
sleV2Dhcp4OptionControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionControlTimeStamp.setStatus("current")
_SleV2Dhcp4OptionControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4OptionControlReqResult_Object = MibScalar
sleV2Dhcp4OptionControlReqResult = _SleV2Dhcp4OptionControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 2, 5),
    _SleV2Dhcp4OptionControlReqResult_Type()
)
sleV2Dhcp4OptionControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionControlReqResult.setStatus("current")


class _SleV2Dhcp4OptionControlPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4OptionControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4OptionControlPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionControlPoolIndex_Object = MibScalar
sleV2Dhcp4OptionControlPoolIndex = _SleV2Dhcp4OptionControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 2, 6),
    _SleV2Dhcp4OptionControlPoolIndex_Type()
)
sleV2Dhcp4OptionControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionControlPoolIndex.setStatus("current")


class _SleV2Dhcp4OptionControlCode_Type(Integer32):
    """Custom type sleV2Dhcp4OptionControlCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              5,
              7,
              8,
              9,
              10,
              11,
              16,
              17,
              19,
              20,
              21,
              22,
              23,
              24,
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
              38,
              39,
              40,
              41,
              42,
              48,
              49,
              64,
              65,
              66,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76)
        )
    )
    namedValues = NamedValues(
        *(("timeOffset", 2),
          ("timeServer", 4),
          ("nameServer", 5),
          ("logServer", 7),
          ("cookieServer", 8),
          ("lprServer", 9),
          ("impressServer", 10),
          ("resourceLocationServer", 11),
          ("swapServer", 16),
          ("rootPath", 17),
          ("ipForwardState", 19),
          ("nonLocalSourceRoutingState", 20),
          ("policyFilter", 21),
          ("maximumDatagramReassemblySize", 22),
          ("defaultIpTimeToLive", 23),
          ("pathMtuAgingTimeout", 24),
          ("interfaceMtu", 26),
          ("allSubnetsAreLocal", 27),
          ("broadcastAddress", 28),
          ("performMaskDiscovery", 29),
          ("maskSupplier", 30),
          ("performRouterDiscovery", 31),
          ("routerSolicitationAddress", 32),
          ("staticRoute", 33),
          ("trailerEncapsulation", 34),
          ("arpCacheTimeout", 35),
          ("ethernetEncapsulationOption", 36),
          ("tcpDefaultTtl", 37),
          ("tcpKeepaliveInterval", 38),
          ("tcpKeepaliveGarbage", 39),
          ("nisDomain", 40),
          ("nisServers", 41),
          ("networkTimeProtocolServers", 42),
          ("xWindowSystemFontServer", 48),
          ("xWindowSystemDisplayManager", 49),
          ("nisPlusDomain", 64),
          ("nisPlusServers", 65),
          ("tftpServerName", 66),
          ("mobileIpHomeAgent", 68),
          ("smtpServer", 69),
          ("pop3Server", 70),
          ("nntpServer", 71),
          ("wwwServer", 72),
          ("defaultFingerServer", 73),
          ("ircServer", 74),
          ("streetTalkServer", 75),
          ("stdaServer", 76))
    )


_SleV2Dhcp4OptionControlCode_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionControlCode_Object = MibScalar
sleV2Dhcp4OptionControlCode = _SleV2Dhcp4OptionControlCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 2, 7),
    _SleV2Dhcp4OptionControlCode_Type()
)
sleV2Dhcp4OptionControlCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionControlCode.setStatus("current")


class _SleV2Dhcp4OptionControlInstance_Type(Integer32):
    """Custom type sleV2Dhcp4OptionControlInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )


_SleV2Dhcp4OptionControlInstance_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionControlInstance_Object = MibScalar
sleV2Dhcp4OptionControlInstance = _SleV2Dhcp4OptionControlInstance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 2, 8),
    _SleV2Dhcp4OptionControlInstance_Type()
)
sleV2Dhcp4OptionControlInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionControlInstance.setStatus("current")


class _SleV2Dhcp4OptionControlType_Type(Integer32):
    """Custom type sleV2Dhcp4OptionControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipaddress", 1),
          ("hex", 2),
          ("text", 3))
    )


_SleV2Dhcp4OptionControlType_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionControlType_Object = MibScalar
sleV2Dhcp4OptionControlType = _SleV2Dhcp4OptionControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 2, 9),
    _SleV2Dhcp4OptionControlType_Type()
)
sleV2Dhcp4OptionControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionControlType.setStatus("current")


class _SleV2Dhcp4OptionControlValue_Type(OctetString):
    """Custom type sleV2Dhcp4OptionControlValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4OptionControlValue_Type.__name__ = "OctetString"
_SleV2Dhcp4OptionControlValue_Object = MibScalar
sleV2Dhcp4OptionControlValue = _SleV2Dhcp4OptionControlValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 2, 10),
    _SleV2Dhcp4OptionControlValue_Type()
)
sleV2Dhcp4OptionControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionControlValue.setStatus("current")
_SleV2Dhcp4OptionNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4OptionNotification = _SleV2Dhcp4OptionNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 3)
)
_SleV2Dhcp4Logs_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Logs = _SleV2Dhcp4Logs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8)
)
_SleV2Dhcp4LogsTable_Object = MibTable
sleV2Dhcp4LogsTable = _SleV2Dhcp4LogsTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4LogsTable.setStatus("current")
_SleV2Dhcp4LogsEntry_Object = MibTableRow
sleV2Dhcp4LogsEntry = _SleV2Dhcp4LogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8, 1, 1)
)
sleV2Dhcp4LogsEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PoolIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4LogsIndex"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4LogsEntry.setStatus("current")


class _SleV2Dhcp4LogsIndex_Type(Integer32):
    """Custom type sleV2Dhcp4LogsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SleV2Dhcp4LogsIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4LogsIndex_Object = MibTableColumn
sleV2Dhcp4LogsIndex = _SleV2Dhcp4LogsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8, 1, 1, 1),
    _SleV2Dhcp4LogsIndex_Type()
)
sleV2Dhcp4LogsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LogsIndex.setStatus("current")
_SleV2Dhcp4LogsAddress_Type = IpAddress
_SleV2Dhcp4LogsAddress_Object = MibTableColumn
sleV2Dhcp4LogsAddress = _SleV2Dhcp4LogsAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8, 1, 1, 2),
    _SleV2Dhcp4LogsAddress_Type()
)
sleV2Dhcp4LogsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LogsAddress.setStatus("current")
_SleV2Dhcp4LogsControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4LogsControl = _SleV2Dhcp4LogsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8, 2)
)


class _SleV2Dhcp4LogsControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4LogsControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcpLogs", 1),
          ("destroyDhcpLogs", 2))
    )


_SleV2Dhcp4LogsControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4LogsControlRequest_Object = MibScalar
sleV2Dhcp4LogsControlRequest = _SleV2Dhcp4LogsControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8, 2, 1),
    _SleV2Dhcp4LogsControlRequest_Type()
)
sleV2Dhcp4LogsControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4LogsControlRequest.setStatus("current")
_SleV2Dhcp4LogsControlStatus_Type = SleControlStatusType
_SleV2Dhcp4LogsControlStatus_Object = MibScalar
sleV2Dhcp4LogsControlStatus = _SleV2Dhcp4LogsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8, 2, 2),
    _SleV2Dhcp4LogsControlStatus_Type()
)
sleV2Dhcp4LogsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LogsControlStatus.setStatus("current")
_SleV2Dhcp4LogsControlTimer_Type = Gauge32
_SleV2Dhcp4LogsControlTimer_Object = MibScalar
sleV2Dhcp4LogsControlTimer = _SleV2Dhcp4LogsControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8, 2, 3),
    _SleV2Dhcp4LogsControlTimer_Type()
)
sleV2Dhcp4LogsControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4LogsControlTimer.setStatus("current")
_SleV2Dhcp4LogsControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4LogsControlTimeStamp_Object = MibScalar
sleV2Dhcp4LogsControlTimeStamp = _SleV2Dhcp4LogsControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8, 2, 4),
    _SleV2Dhcp4LogsControlTimeStamp_Type()
)
sleV2Dhcp4LogsControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LogsControlTimeStamp.setStatus("current")
_SleV2Dhcp4LogsControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4LogsControlReqResult_Object = MibScalar
sleV2Dhcp4LogsControlReqResult = _SleV2Dhcp4LogsControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8, 2, 5),
    _SleV2Dhcp4LogsControlReqResult_Type()
)
sleV2Dhcp4LogsControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LogsControlReqResult.setStatus("current")


class _SleV2Dhcp4LogsControlPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4LogsControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4LogsControlPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4LogsControlPoolIndex_Object = MibScalar
sleV2Dhcp4LogsControlPoolIndex = _SleV2Dhcp4LogsControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8, 2, 6),
    _SleV2Dhcp4LogsControlPoolIndex_Type()
)
sleV2Dhcp4LogsControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4LogsControlPoolIndex.setStatus("current")


class _SleV2Dhcp4LogsControlIndex_Type(Integer32):
    """Custom type sleV2Dhcp4LogsControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 3),
    )


_SleV2Dhcp4LogsControlIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4LogsControlIndex_Object = MibScalar
sleV2Dhcp4LogsControlIndex = _SleV2Dhcp4LogsControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8, 2, 7),
    _SleV2Dhcp4LogsControlIndex_Type()
)
sleV2Dhcp4LogsControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4LogsControlIndex.setStatus("current")
_SleV2Dhcp4LogsControlAddress_Type = IpAddress
_SleV2Dhcp4LogsControlAddress_Object = MibScalar
sleV2Dhcp4LogsControlAddress = _SleV2Dhcp4LogsControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8, 2, 8),
    _SleV2Dhcp4LogsControlAddress_Type()
)
sleV2Dhcp4LogsControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4LogsControlAddress.setStatus("current")
_SleV2Dhcp4LogsNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4LogsNotification = _SleV2Dhcp4LogsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8, 3)
)
_SleV2Dhcp4Ntp_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Ntp = _SleV2Dhcp4Ntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9)
)
_SleV2Dhcp4NtpTable_Object = MibTable
sleV2Dhcp4NtpTable = _SleV2Dhcp4NtpTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4NtpTable.setStatus("current")
_SleV2Dhcp4NtpEntry_Object = MibTableRow
sleV2Dhcp4NtpEntry = _SleV2Dhcp4NtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9, 1, 1)
)
sleV2Dhcp4NtpEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PoolIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4NtpIndex"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4NtpEntry.setStatus("current")


class _SleV2Dhcp4NtpIndex_Type(Integer32):
    """Custom type sleV2Dhcp4NtpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SleV2Dhcp4NtpIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4NtpIndex_Object = MibTableColumn
sleV2Dhcp4NtpIndex = _SleV2Dhcp4NtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9, 1, 1, 1),
    _SleV2Dhcp4NtpIndex_Type()
)
sleV2Dhcp4NtpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4NtpIndex.setStatus("current")
_SleV2Dhcp4NtpAddress_Type = IpAddress
_SleV2Dhcp4NtpAddress_Object = MibTableColumn
sleV2Dhcp4NtpAddress = _SleV2Dhcp4NtpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9, 1, 1, 2),
    _SleV2Dhcp4NtpAddress_Type()
)
sleV2Dhcp4NtpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4NtpAddress.setStatus("current")
_SleV2Dhcp4NtpControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4NtpControl = _SleV2Dhcp4NtpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9, 2)
)


class _SleV2Dhcp4NtpControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4NtpControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcpNtp", 1),
          ("destroyDhcpNtp", 2))
    )


_SleV2Dhcp4NtpControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4NtpControlRequest_Object = MibScalar
sleV2Dhcp4NtpControlRequest = _SleV2Dhcp4NtpControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9, 2, 1),
    _SleV2Dhcp4NtpControlRequest_Type()
)
sleV2Dhcp4NtpControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4NtpControlRequest.setStatus("current")
_SleV2Dhcp4NtpControlStatus_Type = SleControlStatusType
_SleV2Dhcp4NtpControlStatus_Object = MibScalar
sleV2Dhcp4NtpControlStatus = _SleV2Dhcp4NtpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9, 2, 2),
    _SleV2Dhcp4NtpControlStatus_Type()
)
sleV2Dhcp4NtpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4NtpControlStatus.setStatus("current")
_SleV2Dhcp4NtpControlTimer_Type = Gauge32
_SleV2Dhcp4NtpControlTimer_Object = MibScalar
sleV2Dhcp4NtpControlTimer = _SleV2Dhcp4NtpControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9, 2, 3),
    _SleV2Dhcp4NtpControlTimer_Type()
)
sleV2Dhcp4NtpControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4NtpControlTimer.setStatus("current")
_SleV2Dhcp4NtpControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4NtpControlTimeStamp_Object = MibScalar
sleV2Dhcp4NtpControlTimeStamp = _SleV2Dhcp4NtpControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9, 2, 4),
    _SleV2Dhcp4NtpControlTimeStamp_Type()
)
sleV2Dhcp4NtpControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4NtpControlTimeStamp.setStatus("current")
_SleV2Dhcp4NtpControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4NtpControlReqResult_Object = MibScalar
sleV2Dhcp4NtpControlReqResult = _SleV2Dhcp4NtpControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9, 2, 5),
    _SleV2Dhcp4NtpControlReqResult_Type()
)
sleV2Dhcp4NtpControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4NtpControlReqResult.setStatus("current")


class _SleV2Dhcp4NtpControlPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4NtpControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4NtpControlPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4NtpControlPoolIndex_Object = MibScalar
sleV2Dhcp4NtpControlPoolIndex = _SleV2Dhcp4NtpControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9, 2, 6),
    _SleV2Dhcp4NtpControlPoolIndex_Type()
)
sleV2Dhcp4NtpControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4NtpControlPoolIndex.setStatus("current")


class _SleV2Dhcp4NtpControlIndex_Type(Integer32):
    """Custom type sleV2Dhcp4NtpControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 3),
    )


_SleV2Dhcp4NtpControlIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4NtpControlIndex_Object = MibScalar
sleV2Dhcp4NtpControlIndex = _SleV2Dhcp4NtpControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9, 2, 7),
    _SleV2Dhcp4NtpControlIndex_Type()
)
sleV2Dhcp4NtpControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4NtpControlIndex.setStatus("current")
_SleV2Dhcp4NtpControlAddress_Type = IpAddress
_SleV2Dhcp4NtpControlAddress_Object = MibScalar
sleV2Dhcp4NtpControlAddress = _SleV2Dhcp4NtpControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9, 2, 8),
    _SleV2Dhcp4NtpControlAddress_Type()
)
sleV2Dhcp4NtpControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4NtpControlAddress.setStatus("current")
_SleV2Dhcp4NtpNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4NtpNotification = _SleV2Dhcp4NtpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9, 3)
)
_SleV2Dhcp4PE_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PE = _SleV2Dhcp4PE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10)
)
_SleV2Dhcp4PEVendor_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PEVendor = _SleV2Dhcp4PEVendor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1)
)
_SleV2Dhcp4PEVendorTable_Object = MibTable
sleV2Dhcp4PEVendorTable = _SleV2Dhcp4PEVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorTable.setStatus("current")
_SleV2Dhcp4PEVendorEntry_Object = MibTableRow
sleV2Dhcp4PEVendorEntry = _SleV2Dhcp4PEVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 1, 1)
)
sleV2Dhcp4PEVendorEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorPoolIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorIfIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorID"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorStart"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorEntry.setStatus("current")


class _SleV2Dhcp4PEVendorPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4PEVendorPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4PEVendorPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4PEVendorPoolIndex_Object = MibTableColumn
sleV2Dhcp4PEVendorPoolIndex = _SleV2Dhcp4PEVendorPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 1, 1, 1),
    _SleV2Dhcp4PEVendorPoolIndex_Type()
)
sleV2Dhcp4PEVendorPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorPoolIndex.setStatus("current")


class _SleV2Dhcp4PEVendorIfIndex_Type(Integer32):
    """Custom type sleV2Dhcp4PEVendorIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_SleV2Dhcp4PEVendorIfIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4PEVendorIfIndex_Object = MibTableColumn
sleV2Dhcp4PEVendorIfIndex = _SleV2Dhcp4PEVendorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 1, 1, 2),
    _SleV2Dhcp4PEVendorIfIndex_Type()
)
sleV2Dhcp4PEVendorIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorIfIndex.setStatus("current")


class _SleV2Dhcp4PEVendorID_Type(OctetString):
    """Custom type sleV2Dhcp4PEVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleV2Dhcp4PEVendorID_Type.__name__ = "OctetString"
_SleV2Dhcp4PEVendorID_Object = MibTableColumn
sleV2Dhcp4PEVendorID = _SleV2Dhcp4PEVendorID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 1, 1, 3),
    _SleV2Dhcp4PEVendorID_Type()
)
sleV2Dhcp4PEVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorID.setStatus("current")
_SleV2Dhcp4PEVendorStart_Type = IpAddress
_SleV2Dhcp4PEVendorStart_Object = MibTableColumn
sleV2Dhcp4PEVendorStart = _SleV2Dhcp4PEVendorStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 1, 1, 4),
    _SleV2Dhcp4PEVendorStart_Type()
)
sleV2Dhcp4PEVendorStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorStart.setStatus("current")
_SleV2Dhcp4PEVendorEnd_Type = IpAddress
_SleV2Dhcp4PEVendorEnd_Object = MibTableColumn
sleV2Dhcp4PEVendorEnd = _SleV2Dhcp4PEVendorEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 1, 1, 5),
    _SleV2Dhcp4PEVendorEnd_Type()
)
sleV2Dhcp4PEVendorEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorEnd.setStatus("current")
_SleV2Dhcp4PEVendorControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PEVendorControl = _SleV2Dhcp4PEVendorControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 2)
)


class _SleV2Dhcp4PEVendorControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4PEVendorControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createPEVendorEntry", 1),
          ("destroyPEVendorEntry", 2),
          ("destroyPEVendorEntryAll", 3))
    )


_SleV2Dhcp4PEVendorControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4PEVendorControlRequest_Object = MibScalar
sleV2Dhcp4PEVendorControlRequest = _SleV2Dhcp4PEVendorControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 2, 1),
    _SleV2Dhcp4PEVendorControlRequest_Type()
)
sleV2Dhcp4PEVendorControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorControlRequest.setStatus("current")
_SleV2Dhcp4PEVendorControlStatus_Type = SleControlStatusType
_SleV2Dhcp4PEVendorControlStatus_Object = MibScalar
sleV2Dhcp4PEVendorControlStatus = _SleV2Dhcp4PEVendorControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 2, 2),
    _SleV2Dhcp4PEVendorControlStatus_Type()
)
sleV2Dhcp4PEVendorControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorControlStatus.setStatus("current")
_SleV2Dhcp4PEVendorControlTimer_Type = Gauge32
_SleV2Dhcp4PEVendorControlTimer_Object = MibScalar
sleV2Dhcp4PEVendorControlTimer = _SleV2Dhcp4PEVendorControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 2, 3),
    _SleV2Dhcp4PEVendorControlTimer_Type()
)
sleV2Dhcp4PEVendorControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorControlTimer.setStatus("current")
_SleV2Dhcp4PEVendorControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4PEVendorControlTimeStamp_Object = MibScalar
sleV2Dhcp4PEVendorControlTimeStamp = _SleV2Dhcp4PEVendorControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 2, 4),
    _SleV2Dhcp4PEVendorControlTimeStamp_Type()
)
sleV2Dhcp4PEVendorControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorControlTimeStamp.setStatus("current")
_SleV2Dhcp4PEVendorControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4PEVendorControlReqResult_Object = MibScalar
sleV2Dhcp4PEVendorControlReqResult = _SleV2Dhcp4PEVendorControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 2, 5),
    _SleV2Dhcp4PEVendorControlReqResult_Type()
)
sleV2Dhcp4PEVendorControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorControlReqResult.setStatus("current")


class _SleV2Dhcp4PEVendorControlPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4PEVendorControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4PEVendorControlPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4PEVendorControlPoolIndex_Object = MibScalar
sleV2Dhcp4PEVendorControlPoolIndex = _SleV2Dhcp4PEVendorControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 2, 6),
    _SleV2Dhcp4PEVendorControlPoolIndex_Type()
)
sleV2Dhcp4PEVendorControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorControlPoolIndex.setStatus("current")


class _SleV2Dhcp4PEVendorControlIfIndex_Type(Integer32):
    """Custom type sleV2Dhcp4PEVendorControlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_SleV2Dhcp4PEVendorControlIfIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4PEVendorControlIfIndex_Object = MibScalar
sleV2Dhcp4PEVendorControlIfIndex = _SleV2Dhcp4PEVendorControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 2, 7),
    _SleV2Dhcp4PEVendorControlIfIndex_Type()
)
sleV2Dhcp4PEVendorControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorControlIfIndex.setStatus("current")


class _SleV2Dhcp4PEVendorControlVendorID_Type(OctetString):
    """Custom type sleV2Dhcp4PEVendorControlVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleV2Dhcp4PEVendorControlVendorID_Type.__name__ = "OctetString"
_SleV2Dhcp4PEVendorControlVendorID_Object = MibScalar
sleV2Dhcp4PEVendorControlVendorID = _SleV2Dhcp4PEVendorControlVendorID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 2, 8),
    _SleV2Dhcp4PEVendorControlVendorID_Type()
)
sleV2Dhcp4PEVendorControlVendorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorControlVendorID.setStatus("current")
_SleV2Dhcp4PEVendorControlStart_Type = IpAddress
_SleV2Dhcp4PEVendorControlStart_Object = MibScalar
sleV2Dhcp4PEVendorControlStart = _SleV2Dhcp4PEVendorControlStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 2, 9),
    _SleV2Dhcp4PEVendorControlStart_Type()
)
sleV2Dhcp4PEVendorControlStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorControlStart.setStatus("current")
_SleV2Dhcp4PEVendorControlEnd_Type = IpAddress
_SleV2Dhcp4PEVendorControlEnd_Object = MibScalar
sleV2Dhcp4PEVendorControlEnd = _SleV2Dhcp4PEVendorControlEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 2, 10),
    _SleV2Dhcp4PEVendorControlEnd_Type()
)
sleV2Dhcp4PEVendorControlEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorControlEnd.setStatus("current")
_SleV2Dhcp4PEVendorNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PEVendorNotification = _SleV2Dhcp4PEVendorNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 3)
)
_SleV2Dhcp4PEAddress_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PEAddress = _SleV2Dhcp4PEAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2)
)
_SleV2Dhcp4PEAddressTable_Object = MibTable
sleV2Dhcp4PEAddressTable = _SleV2Dhcp4PEAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressTable.setStatus("current")
_SleV2Dhcp4PEAddressEntry_Object = MibTableRow
sleV2Dhcp4PEAddressEntry = _SleV2Dhcp4PEAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 1, 1)
)
sleV2Dhcp4PEAddressEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressPoolIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressIfIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressStart"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressEntry.setStatus("current")


class _SleV2Dhcp4PEAddressPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4PEAddressPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4PEAddressPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4PEAddressPoolIndex_Object = MibTableColumn
sleV2Dhcp4PEAddressPoolIndex = _SleV2Dhcp4PEAddressPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 1, 1, 1),
    _SleV2Dhcp4PEAddressPoolIndex_Type()
)
sleV2Dhcp4PEAddressPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressPoolIndex.setStatus("current")


class _SleV2Dhcp4PEAddressIfIndex_Type(Integer32):
    """Custom type sleV2Dhcp4PEAddressIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_SleV2Dhcp4PEAddressIfIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4PEAddressIfIndex_Object = MibTableColumn
sleV2Dhcp4PEAddressIfIndex = _SleV2Dhcp4PEAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 1, 1, 2),
    _SleV2Dhcp4PEAddressIfIndex_Type()
)
sleV2Dhcp4PEAddressIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressIfIndex.setStatus("current")
_SleV2Dhcp4PEAddressStart_Type = IpAddress
_SleV2Dhcp4PEAddressStart_Object = MibTableColumn
sleV2Dhcp4PEAddressStart = _SleV2Dhcp4PEAddressStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 1, 1, 3),
    _SleV2Dhcp4PEAddressStart_Type()
)
sleV2Dhcp4PEAddressStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressStart.setStatus("current")
_SleV2Dhcp4PEAddressEnd_Type = IpAddress
_SleV2Dhcp4PEAddressEnd_Object = MibTableColumn
sleV2Dhcp4PEAddressEnd = _SleV2Dhcp4PEAddressEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 1, 1, 4),
    _SleV2Dhcp4PEAddressEnd_Type()
)
sleV2Dhcp4PEAddressEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressEnd.setStatus("current")
_SleV2Dhcp4PEAddressControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PEAddressControl = _SleV2Dhcp4PEAddressControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 2)
)


class _SleV2Dhcp4PEAddressControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4PEAddressControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createPEAddressEntry", 1),
          ("destroyPEAddressEntry", 2),
          ("destroyPEAddressEntryAll", 3))
    )


_SleV2Dhcp4PEAddressControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4PEAddressControlRequest_Object = MibScalar
sleV2Dhcp4PEAddressControlRequest = _SleV2Dhcp4PEAddressControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 2, 1),
    _SleV2Dhcp4PEAddressControlRequest_Type()
)
sleV2Dhcp4PEAddressControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressControlRequest.setStatus("current")
_SleV2Dhcp4PEAddressControlStatus_Type = SleControlStatusType
_SleV2Dhcp4PEAddressControlStatus_Object = MibScalar
sleV2Dhcp4PEAddressControlStatus = _SleV2Dhcp4PEAddressControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 2, 2),
    _SleV2Dhcp4PEAddressControlStatus_Type()
)
sleV2Dhcp4PEAddressControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressControlStatus.setStatus("current")
_SleV2Dhcp4PEAddressControlTimer_Type = Gauge32
_SleV2Dhcp4PEAddressControlTimer_Object = MibScalar
sleV2Dhcp4PEAddressControlTimer = _SleV2Dhcp4PEAddressControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 2, 3),
    _SleV2Dhcp4PEAddressControlTimer_Type()
)
sleV2Dhcp4PEAddressControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressControlTimer.setStatus("current")
_SleV2Dhcp4PEAddressControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4PEAddressControlTimeStamp_Object = MibScalar
sleV2Dhcp4PEAddressControlTimeStamp = _SleV2Dhcp4PEAddressControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 2, 4),
    _SleV2Dhcp4PEAddressControlTimeStamp_Type()
)
sleV2Dhcp4PEAddressControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressControlTimeStamp.setStatus("current")
_SleV2Dhcp4PEAddressControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4PEAddressControlReqResult_Object = MibScalar
sleV2Dhcp4PEAddressControlReqResult = _SleV2Dhcp4PEAddressControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 2, 5),
    _SleV2Dhcp4PEAddressControlReqResult_Type()
)
sleV2Dhcp4PEAddressControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressControlReqResult.setStatus("current")


class _SleV2Dhcp4PEAddressControlPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4PEAddressControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4PEAddressControlPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4PEAddressControlPoolIndex_Object = MibScalar
sleV2Dhcp4PEAddressControlPoolIndex = _SleV2Dhcp4PEAddressControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 2, 6),
    _SleV2Dhcp4PEAddressControlPoolIndex_Type()
)
sleV2Dhcp4PEAddressControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressControlPoolIndex.setStatus("current")


class _SleV2Dhcp4PEAddressControlIfIndex_Type(Integer32):
    """Custom type sleV2Dhcp4PEAddressControlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_SleV2Dhcp4PEAddressControlIfIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4PEAddressControlIfIndex_Object = MibScalar
sleV2Dhcp4PEAddressControlIfIndex = _SleV2Dhcp4PEAddressControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 2, 7),
    _SleV2Dhcp4PEAddressControlIfIndex_Type()
)
sleV2Dhcp4PEAddressControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressControlIfIndex.setStatus("current")
_SleV2Dhcp4PEAddressControlStart_Type = IpAddress
_SleV2Dhcp4PEAddressControlStart_Object = MibScalar
sleV2Dhcp4PEAddressControlStart = _SleV2Dhcp4PEAddressControlStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 2, 8),
    _SleV2Dhcp4PEAddressControlStart_Type()
)
sleV2Dhcp4PEAddressControlStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressControlStart.setStatus("current")
_SleV2Dhcp4PEAddressControlEnd_Type = IpAddress
_SleV2Dhcp4PEAddressControlEnd_Object = MibScalar
sleV2Dhcp4PEAddressControlEnd = _SleV2Dhcp4PEAddressControlEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 2, 9),
    _SleV2Dhcp4PEAddressControlEnd_Type()
)
sleV2Dhcp4PEAddressControlEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressControlEnd.setStatus("current")
_SleV2Dhcp4PEAddressNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PEAddressNotification = _SleV2Dhcp4PEAddressNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 3)
)
_SleV2Dhcp4PENonPE_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PENonPE = _SleV2Dhcp4PENonPE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3)
)
_SleV2Dhcp4PENonPETable_Object = MibTable
sleV2Dhcp4PENonPETable = _SleV2Dhcp4PENonPETable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PENonPETable.setStatus("current")
_SleV2Dhcp4PENonPEEntry_Object = MibTableRow
sleV2Dhcp4PENonPEEntry = _SleV2Dhcp4PENonPEEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 1, 1)
)
sleV2Dhcp4PENonPEEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEPoolIndex"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PENonPEEntry.setStatus("current")


class _SleV2Dhcp4PENonPEPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4PENonPEPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4PENonPEPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4PENonPEPoolIndex_Object = MibTableColumn
sleV2Dhcp4PENonPEPoolIndex = _SleV2Dhcp4PENonPEPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 1, 1, 1),
    _SleV2Dhcp4PENonPEPoolIndex_Type()
)
sleV2Dhcp4PENonPEPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PENonPEPoolIndex.setStatus("current")
_SleV2Dhcp4PENonPEStart_Type = IpAddress
_SleV2Dhcp4PENonPEStart_Object = MibTableColumn
sleV2Dhcp4PENonPEStart = _SleV2Dhcp4PENonPEStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 1, 1, 2),
    _SleV2Dhcp4PENonPEStart_Type()
)
sleV2Dhcp4PENonPEStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PENonPEStart.setStatus("current")
_SleV2Dhcp4PENonPEEnd_Type = IpAddress
_SleV2Dhcp4PENonPEEnd_Object = MibTableColumn
sleV2Dhcp4PENonPEEnd = _SleV2Dhcp4PENonPEEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 1, 1, 3),
    _SleV2Dhcp4PENonPEEnd_Type()
)
sleV2Dhcp4PENonPEEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PENonPEEnd.setStatus("current")
_SleV2Dhcp4PENonPEControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PENonPEControl = _SleV2Dhcp4PENonPEControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 2)
)


class _SleV2Dhcp4PENonPEControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4PENonPEControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createPENonPEEntry", 1),
          ("destroyPENonPEEntry", 2))
    )


_SleV2Dhcp4PENonPEControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4PENonPEControlRequest_Object = MibScalar
sleV2Dhcp4PENonPEControlRequest = _SleV2Dhcp4PENonPEControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 2, 1),
    _SleV2Dhcp4PENonPEControlRequest_Type()
)
sleV2Dhcp4PENonPEControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PENonPEControlRequest.setStatus("current")
_SleV2Dhcp4PENonPEControlStatus_Type = SleControlStatusType
_SleV2Dhcp4PENonPEControlStatus_Object = MibScalar
sleV2Dhcp4PENonPEControlStatus = _SleV2Dhcp4PENonPEControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 2, 2),
    _SleV2Dhcp4PENonPEControlStatus_Type()
)
sleV2Dhcp4PENonPEControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PENonPEControlStatus.setStatus("current")
_SleV2Dhcp4PENonPEControlTimer_Type = Gauge32
_SleV2Dhcp4PENonPEControlTimer_Object = MibScalar
sleV2Dhcp4PENonPEControlTimer = _SleV2Dhcp4PENonPEControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 2, 3),
    _SleV2Dhcp4PENonPEControlTimer_Type()
)
sleV2Dhcp4PENonPEControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PENonPEControlTimer.setStatus("current")
_SleV2Dhcp4PENonPEControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4PENonPEControlTimeStamp_Object = MibScalar
sleV2Dhcp4PENonPEControlTimeStamp = _SleV2Dhcp4PENonPEControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 2, 4),
    _SleV2Dhcp4PENonPEControlTimeStamp_Type()
)
sleV2Dhcp4PENonPEControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PENonPEControlTimeStamp.setStatus("current")
_SleV2Dhcp4PENonPEControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4PENonPEControlReqResult_Object = MibScalar
sleV2Dhcp4PENonPEControlReqResult = _SleV2Dhcp4PENonPEControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 2, 5),
    _SleV2Dhcp4PENonPEControlReqResult_Type()
)
sleV2Dhcp4PENonPEControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PENonPEControlReqResult.setStatus("current")


class _SleV2Dhcp4PENonPEControlPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4PENonPEControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4PENonPEControlPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4PENonPEControlPoolIndex_Object = MibScalar
sleV2Dhcp4PENonPEControlPoolIndex = _SleV2Dhcp4PENonPEControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 2, 6),
    _SleV2Dhcp4PENonPEControlPoolIndex_Type()
)
sleV2Dhcp4PENonPEControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PENonPEControlPoolIndex.setStatus("current")
_SleV2Dhcp4PENonPEControlStart_Type = IpAddress
_SleV2Dhcp4PENonPEControlStart_Object = MibScalar
sleV2Dhcp4PENonPEControlStart = _SleV2Dhcp4PENonPEControlStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 2, 7),
    _SleV2Dhcp4PENonPEControlStart_Type()
)
sleV2Dhcp4PENonPEControlStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PENonPEControlStart.setStatus("current")
_SleV2Dhcp4PENonPEControlEnd_Type = IpAddress
_SleV2Dhcp4PENonPEControlEnd_Object = MibScalar
sleV2Dhcp4PENonPEControlEnd = _SleV2Dhcp4PENonPEControlEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 2, 8),
    _SleV2Dhcp4PENonPEControlEnd_Type()
)
sleV2Dhcp4PENonPEControlEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PENonPEControlEnd.setStatus("current")
_SleV2Dhcp4PENonPENotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PENonPENotification = _SleV2Dhcp4PENonPENotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 3)
)
_SleV2Dhcp4Option82_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Option82 = _SleV2Dhcp4Option82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3)
)
_SleV2Dhcp4Option82Port_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Option82Port = _SleV2Dhcp4Option82Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1)
)
_SleV2Dhcp4Option82PortTable_Object = MibTable
sleV2Dhcp4Option82PortTable = _SleV2Dhcp4Option82PortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortTable.setStatus("current")
_SleV2Dhcp4Option82PortEntry_Object = MibTableRow
sleV2Dhcp4Option82PortEntry = _SleV2Dhcp4Option82PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 1, 1)
)
sleV2Dhcp4Option82PortEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortIndex"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortEntry.setStatus("current")


class _SleV2Dhcp4Option82PortIndex_Type(Integer32):
    """Custom type sleV2Dhcp4Option82PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4Option82PortIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82PortIndex_Object = MibTableColumn
sleV2Dhcp4Option82PortIndex = _SleV2Dhcp4Option82PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 1, 1, 1),
    _SleV2Dhcp4Option82PortIndex_Type()
)
sleV2Dhcp4Option82PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortIndex.setStatus("current")


class _SleV2Dhcp4Option82PortCircuitType_Type(Integer32):
    """Custom type sleV2Dhcp4Option82PortCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("index", 1),
          ("hex", 2),
          ("text", 3),
          ("option", 4))
    )


_SleV2Dhcp4Option82PortCircuitType_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82PortCircuitType_Object = MibTableColumn
sleV2Dhcp4Option82PortCircuitType = _SleV2Dhcp4Option82PortCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 1, 1, 2),
    _SleV2Dhcp4Option82PortCircuitType_Type()
)
sleV2Dhcp4Option82PortCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortCircuitType.setStatus("current")


class _SleV2Dhcp4Option82PortCircuitId_Type(OctetString):
    """Custom type sleV2Dhcp4Option82PortCircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4Option82PortCircuitId_Type.__name__ = "OctetString"
_SleV2Dhcp4Option82PortCircuitId_Object = MibTableColumn
sleV2Dhcp4Option82PortCircuitId = _SleV2Dhcp4Option82PortCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 1, 1, 3),
    _SleV2Dhcp4Option82PortCircuitId_Type()
)
sleV2Dhcp4Option82PortCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortCircuitId.setStatus("current")


class _SleV2Dhcp4Option82PortTrustState_Type(Integer32):
    """Custom type sleV2Dhcp4Option82PortTrustState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("normal", 1),
          ("option82", 2),
          ("all", 3))
    )


_SleV2Dhcp4Option82PortTrustState_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82PortTrustState_Object = MibTableColumn
sleV2Dhcp4Option82PortTrustState = _SleV2Dhcp4Option82PortTrustState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 1, 1, 4),
    _SleV2Dhcp4Option82PortTrustState_Type()
)
sleV2Dhcp4Option82PortTrustState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortTrustState.setStatus("current")


class _SleV2Dhcp4Option82PortPolicy_Type(Integer32):
    """Custom type sleV2Dhcp4Option82PortPolicy based on Integer32"""
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
          ("keep", 1),
          ("replace", 2))
    )


_SleV2Dhcp4Option82PortPolicy_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82PortPolicy_Object = MibTableColumn
sleV2Dhcp4Option82PortPolicy = _SleV2Dhcp4Option82PortPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 1, 1, 5),
    _SleV2Dhcp4Option82PortPolicy_Type()
)
sleV2Dhcp4Option82PortPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortPolicy.setStatus("current")


class _SleV2Dhcp4Option82PortPolicyDrop_Type(Integer32):
    """Custom type sleV2Dhcp4Option82PortPolicyDrop based on Integer32"""
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
          ("normal", 1),
          ("option82", 2))
    )


_SleV2Dhcp4Option82PortPolicyDrop_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82PortPolicyDrop_Object = MibTableColumn
sleV2Dhcp4Option82PortPolicyDrop = _SleV2Dhcp4Option82PortPolicyDrop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 1, 1, 6),
    _SleV2Dhcp4Option82PortPolicyDrop_Type()
)
sleV2Dhcp4Option82PortPolicyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortPolicyDrop.setStatus("current")
_SleV2Dhcp4Option82PortControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Option82PortControl = _SleV2Dhcp4Option82PortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 2)
)


class _SleV2Dhcp4Option82PortControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4Option82PortControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("setDhcpOption82PortCircuitId", 1),
          ("setDhcpOption82PortTrustState", 2),
          ("clearDhcpOption82PortCircuitId", 3),
          ("setDhcpOption82PortPolicy", 4))
    )


_SleV2Dhcp4Option82PortControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82PortControlRequest_Object = MibScalar
sleV2Dhcp4Option82PortControlRequest = _SleV2Dhcp4Option82PortControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 2, 1),
    _SleV2Dhcp4Option82PortControlRequest_Type()
)
sleV2Dhcp4Option82PortControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortControlRequest.setStatus("current")
_SleV2Dhcp4Option82PortControlStatus_Type = SleControlStatusType
_SleV2Dhcp4Option82PortControlStatus_Object = MibScalar
sleV2Dhcp4Option82PortControlStatus = _SleV2Dhcp4Option82PortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 2, 2),
    _SleV2Dhcp4Option82PortControlStatus_Type()
)
sleV2Dhcp4Option82PortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortControlStatus.setStatus("current")
_SleV2Dhcp4Option82PortControlTimer_Type = Gauge32
_SleV2Dhcp4Option82PortControlTimer_Object = MibScalar
sleV2Dhcp4Option82PortControlTimer = _SleV2Dhcp4Option82PortControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 2, 3),
    _SleV2Dhcp4Option82PortControlTimer_Type()
)
sleV2Dhcp4Option82PortControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortControlTimer.setStatus("current")
_SleV2Dhcp4Option82PortControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4Option82PortControlTimeStamp_Object = MibScalar
sleV2Dhcp4Option82PortControlTimeStamp = _SleV2Dhcp4Option82PortControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 2, 4),
    _SleV2Dhcp4Option82PortControlTimeStamp_Type()
)
sleV2Dhcp4Option82PortControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortControlTimeStamp.setStatus("current")
_SleV2Dhcp4Option82PortControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4Option82PortControlReqResult_Object = MibScalar
sleV2Dhcp4Option82PortControlReqResult = _SleV2Dhcp4Option82PortControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 2, 5),
    _SleV2Dhcp4Option82PortControlReqResult_Type()
)
sleV2Dhcp4Option82PortControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortControlReqResult.setStatus("current")


class _SleV2Dhcp4Option82PortControlIndex_Type(Integer32):
    """Custom type sleV2Dhcp4Option82PortControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4Option82PortControlIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82PortControlIndex_Object = MibScalar
sleV2Dhcp4Option82PortControlIndex = _SleV2Dhcp4Option82PortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 2, 6),
    _SleV2Dhcp4Option82PortControlIndex_Type()
)
sleV2Dhcp4Option82PortControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortControlIndex.setStatus("current")


class _SleV2Dhcp4Option82PortControlCircuitType_Type(Integer32):
    """Custom type sleV2Dhcp4Option82PortControlCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("index", 1),
          ("hex", 2),
          ("text", 3),
          ("option", 4))
    )


_SleV2Dhcp4Option82PortControlCircuitType_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82PortControlCircuitType_Object = MibScalar
sleV2Dhcp4Option82PortControlCircuitType = _SleV2Dhcp4Option82PortControlCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 2, 7),
    _SleV2Dhcp4Option82PortControlCircuitType_Type()
)
sleV2Dhcp4Option82PortControlCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortControlCircuitType.setStatus("current")


class _SleV2Dhcp4Option82PortControlCircuitId_Type(OctetString):
    """Custom type sleV2Dhcp4Option82PortControlCircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4Option82PortControlCircuitId_Type.__name__ = "OctetString"
_SleV2Dhcp4Option82PortControlCircuitId_Object = MibScalar
sleV2Dhcp4Option82PortControlCircuitId = _SleV2Dhcp4Option82PortControlCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 2, 8),
    _SleV2Dhcp4Option82PortControlCircuitId_Type()
)
sleV2Dhcp4Option82PortControlCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortControlCircuitId.setStatus("current")


class _SleV2Dhcp4Option82PortControlTrustState_Type(Integer32):
    """Custom type sleV2Dhcp4Option82PortControlTrustState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("normal", 1),
          ("option82", 2),
          ("all", 3))
    )


_SleV2Dhcp4Option82PortControlTrustState_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82PortControlTrustState_Object = MibScalar
sleV2Dhcp4Option82PortControlTrustState = _SleV2Dhcp4Option82PortControlTrustState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 2, 9),
    _SleV2Dhcp4Option82PortControlTrustState_Type()
)
sleV2Dhcp4Option82PortControlTrustState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortControlTrustState.setStatus("current")


class _SleV2Dhcp4Option82PortControlPolicy_Type(Integer32):
    """Custom type sleV2Dhcp4Option82PortControlPolicy based on Integer32"""
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
          ("keep", 1),
          ("replace", 2))
    )


_SleV2Dhcp4Option82PortControlPolicy_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82PortControlPolicy_Object = MibScalar
sleV2Dhcp4Option82PortControlPolicy = _SleV2Dhcp4Option82PortControlPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 2, 10),
    _SleV2Dhcp4Option82PortControlPolicy_Type()
)
sleV2Dhcp4Option82PortControlPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortControlPolicy.setStatus("current")


class _SleV2Dhcp4Option82PortControlPolicyDrop_Type(Integer32):
    """Custom type sleV2Dhcp4Option82PortControlPolicyDrop based on Integer32"""
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
          ("normal", 1),
          ("option82", 2))
    )


_SleV2Dhcp4Option82PortControlPolicyDrop_Type.__name__ = "Integer32"
_SleV2Dhcp4Option82PortControlPolicyDrop_Object = MibScalar
sleV2Dhcp4Option82PortControlPolicyDrop = _SleV2Dhcp4Option82PortControlPolicyDrop_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 2, 11),
    _SleV2Dhcp4Option82PortControlPolicyDrop_Type()
)
sleV2Dhcp4Option82PortControlPolicyDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortControlPolicyDrop.setStatus("current")
_SleV2Dhcp4Option82PortNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Option82PortNotification = _SleV2Dhcp4Option82PortNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 3)
)
_SleV2Dhcp4RelayInfo_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RelayInfo = _SleV2Dhcp4RelayInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2)
)
_SleV2Dhcp4Remote_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Remote = _SleV2Dhcp4Remote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1)
)
_SleV2Dhcp4RemoteTable_Object = MibTable
sleV2Dhcp4RemoteTable = _SleV2Dhcp4RemoteTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteTable.setStatus("current")
_SleV2Dhcp4RemoteEntry_Object = MibTableRow
sleV2Dhcp4RemoteEntry = _SleV2Dhcp4RemoteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 1, 1)
)
sleV2Dhcp4RemoteEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteId"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteEntry.setStatus("current")


class _SleV2Dhcp4RemoteId_Type(OctetString):
    """Custom type sleV2Dhcp4RemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4RemoteId_Type.__name__ = "OctetString"
_SleV2Dhcp4RemoteId_Object = MibTableColumn
sleV2Dhcp4RemoteId = _SleV2Dhcp4RemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 1, 1, 1),
    _SleV2Dhcp4RemoteId_Type()
)
sleV2Dhcp4RemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteId.setStatus("current")


class _SleV2Dhcp4RemoteType_Type(Integer32):
    """Custom type sleV2Dhcp4RemoteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ipaddress", 1),
          ("hex", 2),
          ("text", 3),
          ("index", 5))
    )


_SleV2Dhcp4RemoteType_Type.__name__ = "Integer32"
_SleV2Dhcp4RemoteType_Object = MibTableColumn
sleV2Dhcp4RemoteType = _SleV2Dhcp4RemoteType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 1, 1, 2),
    _SleV2Dhcp4RemoteType_Type()
)
sleV2Dhcp4RemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteType.setStatus("current")


class _SleV2Dhcp4RemoteClass_Type(OctetString):
    """Custom type sleV2Dhcp4RemoteClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4RemoteClass_Type.__name__ = "OctetString"
_SleV2Dhcp4RemoteClass_Object = MibTableColumn
sleV2Dhcp4RemoteClass = _SleV2Dhcp4RemoteClass_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 1, 1, 3),
    _SleV2Dhcp4RemoteClass_Type()
)
sleV2Dhcp4RemoteClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteClass.setStatus("current")
_SleV2Dhcp4RemoteTrust_Type = Boolean
_SleV2Dhcp4RemoteTrust_Object = MibTableColumn
sleV2Dhcp4RemoteTrust = _SleV2Dhcp4RemoteTrust_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 1, 1, 4),
    _SleV2Dhcp4RemoteTrust_Type()
)
sleV2Dhcp4RemoteTrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteTrust.setStatus("current")


class _SleV2Dhcp4RemoteLeaseLimit_Type(Integer32):
    """Custom type sleV2Dhcp4RemoteLeaseLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Dhcp4RemoteLeaseLimit_Type.__name__ = "Integer32"
_SleV2Dhcp4RemoteLeaseLimit_Object = MibTableColumn
sleV2Dhcp4RemoteLeaseLimit = _SleV2Dhcp4RemoteLeaseLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 1, 1, 5),
    _SleV2Dhcp4RemoteLeaseLimit_Type()
)
sleV2Dhcp4RemoteLeaseLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteLeaseLimit.setStatus("current")


class _SleV2Dhcp4RemoteLeaseCnt_Type(Integer32):
    """Custom type sleV2Dhcp4RemoteLeaseCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Dhcp4RemoteLeaseCnt_Type.__name__ = "Integer32"
_SleV2Dhcp4RemoteLeaseCnt_Object = MibTableColumn
sleV2Dhcp4RemoteLeaseCnt = _SleV2Dhcp4RemoteLeaseCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 1, 1, 6),
    _SleV2Dhcp4RemoteLeaseCnt_Type()
)
sleV2Dhcp4RemoteLeaseCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteLeaseCnt.setStatus("current")
_SleV2Dhcp4RemoteControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RemoteControl = _SleV2Dhcp4RemoteControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 2)
)


class _SleV2Dhcp4RemoteControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4RemoteControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("createDhcpRemote", 1),
          ("destroyDhcpRemote", 2),
          ("setDhcpRemote", 3),
          ("clearDhcpRemotes", 4))
    )


_SleV2Dhcp4RemoteControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4RemoteControlRequest_Object = MibScalar
sleV2Dhcp4RemoteControlRequest = _SleV2Dhcp4RemoteControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 2, 1),
    _SleV2Dhcp4RemoteControlRequest_Type()
)
sleV2Dhcp4RemoteControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteControlRequest.setStatus("current")
_SleV2Dhcp4RemoteControlStatus_Type = SleControlStatusType
_SleV2Dhcp4RemoteControlStatus_Object = MibScalar
sleV2Dhcp4RemoteControlStatus = _SleV2Dhcp4RemoteControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 2, 2),
    _SleV2Dhcp4RemoteControlStatus_Type()
)
sleV2Dhcp4RemoteControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteControlStatus.setStatus("current")
_SleV2Dhcp4RemoteControlTimer_Type = Gauge32
_SleV2Dhcp4RemoteControlTimer_Object = MibScalar
sleV2Dhcp4RemoteControlTimer = _SleV2Dhcp4RemoteControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 2, 3),
    _SleV2Dhcp4RemoteControlTimer_Type()
)
sleV2Dhcp4RemoteControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteControlTimer.setStatus("current")
_SleV2Dhcp4RemoteControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4RemoteControlTimeStamp_Object = MibScalar
sleV2Dhcp4RemoteControlTimeStamp = _SleV2Dhcp4RemoteControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 2, 4),
    _SleV2Dhcp4RemoteControlTimeStamp_Type()
)
sleV2Dhcp4RemoteControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteControlTimeStamp.setStatus("current")
_SleV2Dhcp4RemoteControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4RemoteControlReqResult_Object = MibScalar
sleV2Dhcp4RemoteControlReqResult = _SleV2Dhcp4RemoteControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 2, 5),
    _SleV2Dhcp4RemoteControlReqResult_Type()
)
sleV2Dhcp4RemoteControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteControlReqResult.setStatus("current")


class _SleV2Dhcp4RemoteControlId_Type(OctetString):
    """Custom type sleV2Dhcp4RemoteControlId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4RemoteControlId_Type.__name__ = "OctetString"
_SleV2Dhcp4RemoteControlId_Object = MibScalar
sleV2Dhcp4RemoteControlId = _SleV2Dhcp4RemoteControlId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 2, 6),
    _SleV2Dhcp4RemoteControlId_Type()
)
sleV2Dhcp4RemoteControlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteControlId.setStatus("current")


class _SleV2Dhcp4RemoteControlType_Type(Integer32):
    """Custom type sleV2Dhcp4RemoteControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ipaddress", 1),
          ("hex", 2),
          ("text", 3),
          ("index", 5))
    )


_SleV2Dhcp4RemoteControlType_Type.__name__ = "Integer32"
_SleV2Dhcp4RemoteControlType_Object = MibScalar
sleV2Dhcp4RemoteControlType = _SleV2Dhcp4RemoteControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 2, 7),
    _SleV2Dhcp4RemoteControlType_Type()
)
sleV2Dhcp4RemoteControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteControlType.setStatus("current")


class _SleV2Dhcp4RemoteControlClass_Type(OctetString):
    """Custom type sleV2Dhcp4RemoteControlClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4RemoteControlClass_Type.__name__ = "OctetString"
_SleV2Dhcp4RemoteControlClass_Object = MibScalar
sleV2Dhcp4RemoteControlClass = _SleV2Dhcp4RemoteControlClass_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 2, 8),
    _SleV2Dhcp4RemoteControlClass_Type()
)
sleV2Dhcp4RemoteControlClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteControlClass.setStatus("current")
_SleV2Dhcp4RemoteControlTrust_Type = Boolean
_SleV2Dhcp4RemoteControlTrust_Object = MibScalar
sleV2Dhcp4RemoteControlTrust = _SleV2Dhcp4RemoteControlTrust_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 2, 9),
    _SleV2Dhcp4RemoteControlTrust_Type()
)
sleV2Dhcp4RemoteControlTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteControlTrust.setStatus("current")


class _SleV4Dhcp4RemoteControlLeaseLimit_Type(Integer32):
    """Custom type sleV4Dhcp4RemoteControlLeaseLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483637),
    )


_SleV4Dhcp4RemoteControlLeaseLimit_Type.__name__ = "Integer32"
_SleV4Dhcp4RemoteControlLeaseLimit_Object = MibScalar
sleV4Dhcp4RemoteControlLeaseLimit = _SleV4Dhcp4RemoteControlLeaseLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 2, 10),
    _SleV4Dhcp4RemoteControlLeaseLimit_Type()
)
sleV4Dhcp4RemoteControlLeaseLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV4Dhcp4RemoteControlLeaseLimit.setStatus("current")
_SleV2Dhcp4RemoteNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RemoteNotification = _SleV2Dhcp4RemoteNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 3)
)
_SleV2Dhcp4RCircuit_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RCircuit = _SleV2Dhcp4RCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2)
)
_SleV2Dhcp4RCircuitTable_Object = MibTable
sleV2Dhcp4RCircuitTable = _SleV2Dhcp4RCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitTable.setStatus("current")
_SleV2Dhcp4RCircuitEntry_Object = MibTableRow
sleV2Dhcp4RCircuitEntry = _SleV2Dhcp4RCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 1, 1)
)
sleV2Dhcp4RCircuitEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteId"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitId"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitEntry.setStatus("current")


class _SleV2Dhcp4RCircuitId_Type(OctetString):
    """Custom type sleV2Dhcp4RCircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4RCircuitId_Type.__name__ = "OctetString"
_SleV2Dhcp4RCircuitId_Object = MibTableColumn
sleV2Dhcp4RCircuitId = _SleV2Dhcp4RCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 1, 1, 1),
    _SleV2Dhcp4RCircuitId_Type()
)
sleV2Dhcp4RCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitId.setStatus("current")


class _SleV2Dhcp4RCircuitType_Type(Integer32):
    """Custom type sleV2Dhcp4RCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("index", 1),
          ("hex", 2),
          ("text", 3))
    )


_SleV2Dhcp4RCircuitType_Type.__name__ = "Integer32"
_SleV2Dhcp4RCircuitType_Object = MibTableColumn
sleV2Dhcp4RCircuitType = _SleV2Dhcp4RCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 1, 1, 2),
    _SleV2Dhcp4RCircuitType_Type()
)
sleV2Dhcp4RCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitType.setStatus("current")


class _SleV2Dhcp4RCircuitClass_Type(OctetString):
    """Custom type sleV2Dhcp4RCircuitClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4RCircuitClass_Type.__name__ = "OctetString"
_SleV2Dhcp4RCircuitClass_Object = MibTableColumn
sleV2Dhcp4RCircuitClass = _SleV2Dhcp4RCircuitClass_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 1, 1, 3),
    _SleV2Dhcp4RCircuitClass_Type()
)
sleV2Dhcp4RCircuitClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitClass.setStatus("current")


class _SleV2Dhcp4RCircuitLeaseLimit_Type(Integer32):
    """Custom type sleV2Dhcp4RCircuitLeaseLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Dhcp4RCircuitLeaseLimit_Type.__name__ = "Integer32"
_SleV2Dhcp4RCircuitLeaseLimit_Object = MibTableColumn
sleV2Dhcp4RCircuitLeaseLimit = _SleV2Dhcp4RCircuitLeaseLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 1, 1, 4),
    _SleV2Dhcp4RCircuitLeaseLimit_Type()
)
sleV2Dhcp4RCircuitLeaseLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitLeaseLimit.setStatus("current")


class _SleV2Dhcp4RCircuitLeaseCnt_Type(Integer32):
    """Custom type sleV2Dhcp4RCircuitLeaseCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Dhcp4RCircuitLeaseCnt_Type.__name__ = "Integer32"
_SleV2Dhcp4RCircuitLeaseCnt_Object = MibTableColumn
sleV2Dhcp4RCircuitLeaseCnt = _SleV2Dhcp4RCircuitLeaseCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 1, 1, 5),
    _SleV2Dhcp4RCircuitLeaseCnt_Type()
)
sleV2Dhcp4RCircuitLeaseCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitLeaseCnt.setStatus("current")
_SleV2Dhcp4RCircuitControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RCircuitControl = _SleV2Dhcp4RCircuitControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 2)
)


class _SleV2Dhcp4RCircuitControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4RCircuitControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("createDhcpRemoteCircuit", 1),
          ("destroyDhcpRemoteCircuit", 2),
          ("clearDhcpRemoteCircuits", 3),
          ("setDhcpRemoteCircuit", 4))
    )


_SleV2Dhcp4RCircuitControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4RCircuitControlRequest_Object = MibScalar
sleV2Dhcp4RCircuitControlRequest = _SleV2Dhcp4RCircuitControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 2, 1),
    _SleV2Dhcp4RCircuitControlRequest_Type()
)
sleV2Dhcp4RCircuitControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitControlRequest.setStatus("current")
_SleV2Dhcp4RCircuitControlStatus_Type = SleControlStatusType
_SleV2Dhcp4RCircuitControlStatus_Object = MibScalar
sleV2Dhcp4RCircuitControlStatus = _SleV2Dhcp4RCircuitControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 2, 2),
    _SleV2Dhcp4RCircuitControlStatus_Type()
)
sleV2Dhcp4RCircuitControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitControlStatus.setStatus("current")
_SleV2Dhcp4RCircuitControlTimer_Type = Gauge32
_SleV2Dhcp4RCircuitControlTimer_Object = MibScalar
sleV2Dhcp4RCircuitControlTimer = _SleV2Dhcp4RCircuitControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 2, 3),
    _SleV2Dhcp4RCircuitControlTimer_Type()
)
sleV2Dhcp4RCircuitControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitControlTimer.setStatus("current")
_SleV2Dhcp4RCircuitControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4RCircuitControlTimeStamp_Object = MibScalar
sleV2Dhcp4RCircuitControlTimeStamp = _SleV2Dhcp4RCircuitControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 2, 4),
    _SleV2Dhcp4RCircuitControlTimeStamp_Type()
)
sleV2Dhcp4RCircuitControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitControlTimeStamp.setStatus("current")
_SleV2Dhcp4RCircuitControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4RCircuitControlReqResult_Object = MibScalar
sleV2Dhcp4RCircuitControlReqResult = _SleV2Dhcp4RCircuitControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 2, 5),
    _SleV2Dhcp4RCircuitControlReqResult_Type()
)
sleV2Dhcp4RCircuitControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitControlReqResult.setStatus("current")


class _SleV2Dhcp4RCircuitControlRemote_Type(OctetString):
    """Custom type sleV2Dhcp4RCircuitControlRemote based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4RCircuitControlRemote_Type.__name__ = "OctetString"
_SleV2Dhcp4RCircuitControlRemote_Object = MibScalar
sleV2Dhcp4RCircuitControlRemote = _SleV2Dhcp4RCircuitControlRemote_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 2, 6),
    _SleV2Dhcp4RCircuitControlRemote_Type()
)
sleV2Dhcp4RCircuitControlRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitControlRemote.setStatus("current")


class _SleV2Dhcp4RCircuitControlId_Type(OctetString):
    """Custom type sleV2Dhcp4RCircuitControlId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4RCircuitControlId_Type.__name__ = "OctetString"
_SleV2Dhcp4RCircuitControlId_Object = MibScalar
sleV2Dhcp4RCircuitControlId = _SleV2Dhcp4RCircuitControlId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 2, 7),
    _SleV2Dhcp4RCircuitControlId_Type()
)
sleV2Dhcp4RCircuitControlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitControlId.setStatus("current")


class _SleV2Dhcp4RCircuitControlType_Type(Integer32):
    """Custom type sleV2Dhcp4RCircuitControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("index", 1),
          ("hex", 2),
          ("text", 3))
    )


_SleV2Dhcp4RCircuitControlType_Type.__name__ = "Integer32"
_SleV2Dhcp4RCircuitControlType_Object = MibScalar
sleV2Dhcp4RCircuitControlType = _SleV2Dhcp4RCircuitControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 2, 8),
    _SleV2Dhcp4RCircuitControlType_Type()
)
sleV2Dhcp4RCircuitControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitControlType.setStatus("current")


class _SleV2Dhcp4RCircuitControlClass_Type(OctetString):
    """Custom type sleV2Dhcp4RCircuitControlClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4RCircuitControlClass_Type.__name__ = "OctetString"
_SleV2Dhcp4RCircuitControlClass_Object = MibScalar
sleV2Dhcp4RCircuitControlClass = _SleV2Dhcp4RCircuitControlClass_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 2, 9),
    _SleV2Dhcp4RCircuitControlClass_Type()
)
sleV2Dhcp4RCircuitControlClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitControlClass.setStatus("current")


class _SleV2Dhcp4RCircuitControlLeaseLimit_Type(Integer32):
    """Custom type sleV2Dhcp4RCircuitControlLeaseLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Dhcp4RCircuitControlLeaseLimit_Type.__name__ = "Integer32"
_SleV2Dhcp4RCircuitControlLeaseLimit_Object = MibScalar
sleV2Dhcp4RCircuitControlLeaseLimit = _SleV2Dhcp4RCircuitControlLeaseLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 2, 10),
    _SleV2Dhcp4RCircuitControlLeaseLimit_Type()
)
sleV2Dhcp4RCircuitControlLeaseLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitControlLeaseLimit.setStatus("current")
_SleV2Dhcp4RCircuitNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RCircuitNotification = _SleV2Dhcp4RCircuitNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 3)
)
_SleV2Dhcp4Class_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Class = _SleV2Dhcp4Class_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3)
)
_SleV2Dhcp4ClassBase_ObjectIdentity = ObjectIdentity
sleV2Dhcp4ClassBase = _SleV2Dhcp4ClassBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 1)
)
_SleV2Dhcp4ClassTable_Object = MibTable
sleV2Dhcp4ClassTable = _SleV2Dhcp4ClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassTable.setStatus("current")
_SleV2Dhcp4ClassEntry_Object = MibTableRow
sleV2Dhcp4ClassEntry = _SleV2Dhcp4ClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 1, 1, 1)
)
sleV2Dhcp4ClassEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4ClassName"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassEntry.setStatus("current")


class _SleV2Dhcp4ClassName_Type(OctetString):
    """Custom type sleV2Dhcp4ClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4ClassName_Type.__name__ = "OctetString"
_SleV2Dhcp4ClassName_Object = MibTableColumn
sleV2Dhcp4ClassName = _SleV2Dhcp4ClassName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 1, 1, 1, 1),
    _SleV2Dhcp4ClassName_Type()
)
sleV2Dhcp4ClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassName.setStatus("current")
_SleV2Dhcp4ClassControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4ClassControl = _SleV2Dhcp4ClassControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 1, 2)
)


class _SleV2Dhcp4ClassControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4ClassControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcpClass", 1),
          ("destroyDhcpClass", 2))
    )


_SleV2Dhcp4ClassControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4ClassControlRequest_Object = MibScalar
sleV2Dhcp4ClassControlRequest = _SleV2Dhcp4ClassControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 1, 2, 1),
    _SleV2Dhcp4ClassControlRequest_Type()
)
sleV2Dhcp4ClassControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassControlRequest.setStatus("current")
_SleV2Dhcp4ClassControlStatus_Type = SleControlStatusType
_SleV2Dhcp4ClassControlStatus_Object = MibScalar
sleV2Dhcp4ClassControlStatus = _SleV2Dhcp4ClassControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 1, 2, 2),
    _SleV2Dhcp4ClassControlStatus_Type()
)
sleV2Dhcp4ClassControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassControlStatus.setStatus("current")
_SleV2Dhcp4ClassControlTimer_Type = Gauge32
_SleV2Dhcp4ClassControlTimer_Object = MibScalar
sleV2Dhcp4ClassControlTimer = _SleV2Dhcp4ClassControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 1, 2, 3),
    _SleV2Dhcp4ClassControlTimer_Type()
)
sleV2Dhcp4ClassControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassControlTimer.setStatus("current")
_SleV2Dhcp4ClassControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4ClassControlTimeStamp_Object = MibScalar
sleV2Dhcp4ClassControlTimeStamp = _SleV2Dhcp4ClassControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 1, 2, 4),
    _SleV2Dhcp4ClassControlTimeStamp_Type()
)
sleV2Dhcp4ClassControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassControlTimeStamp.setStatus("current")
_SleV2Dhcp4ClassControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4ClassControlReqResult_Object = MibScalar
sleV2Dhcp4ClassControlReqResult = _SleV2Dhcp4ClassControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 1, 2, 5),
    _SleV2Dhcp4ClassControlReqResult_Type()
)
sleV2Dhcp4ClassControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassControlReqResult.setStatus("current")


class _SleV2Dhcp4ClassControlName_Type(OctetString):
    """Custom type sleV2Dhcp4ClassControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4ClassControlName_Type.__name__ = "OctetString"
_SleV2Dhcp4ClassControlName_Object = MibScalar
sleV2Dhcp4ClassControlName = _SleV2Dhcp4ClassControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 1, 2, 6),
    _SleV2Dhcp4ClassControlName_Type()
)
sleV2Dhcp4ClassControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassControlName.setStatus("current")
_SleV2Dhcp4ClassNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4ClassNotification = _SleV2Dhcp4ClassNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 1, 3)
)
_SleV2Dhcp4CRCMap_ObjectIdentity = ObjectIdentity
sleV2Dhcp4CRCMap = _SleV2Dhcp4CRCMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2)
)
_SleV2Dhcp4CRCMapTable_Object = MibTable
sleV2Dhcp4CRCMapTable = _SleV2Dhcp4CRCMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4CRCMapTable.setStatus("current")
_SleV2Dhcp4CRCMapEntry_Object = MibTableRow
sleV2Dhcp4CRCMapEntry = _SleV2Dhcp4CRCMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2, 1, 1)
)
sleV2Dhcp4CRCMapEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapClass"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapRemote"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapCircuit"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4CRCMapEntry.setStatus("current")


class _SleV2Dhcp4CRCMapClass_Type(OctetString):
    """Custom type sleV2Dhcp4CRCMapClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4CRCMapClass_Type.__name__ = "OctetString"
_SleV2Dhcp4CRCMapClass_Object = MibTableColumn
sleV2Dhcp4CRCMapClass = _SleV2Dhcp4CRCMapClass_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2, 1, 1, 1),
    _SleV2Dhcp4CRCMapClass_Type()
)
sleV2Dhcp4CRCMapClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4CRCMapClass.setStatus("current")


class _SleV2Dhcp4CRCMapRemote_Type(OctetString):
    """Custom type sleV2Dhcp4CRCMapRemote based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4CRCMapRemote_Type.__name__ = "OctetString"
_SleV2Dhcp4CRCMapRemote_Object = MibTableColumn
sleV2Dhcp4CRCMapRemote = _SleV2Dhcp4CRCMapRemote_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2, 1, 1, 2),
    _SleV2Dhcp4CRCMapRemote_Type()
)
sleV2Dhcp4CRCMapRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4CRCMapRemote.setStatus("current")


class _SleV2Dhcp4CRCMapCircuit_Type(OctetString):
    """Custom type sleV2Dhcp4CRCMapCircuit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4CRCMapCircuit_Type.__name__ = "OctetString"
_SleV2Dhcp4CRCMapCircuit_Object = MibTableColumn
sleV2Dhcp4CRCMapCircuit = _SleV2Dhcp4CRCMapCircuit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2, 1, 1, 3),
    _SleV2Dhcp4CRCMapCircuit_Type()
)
sleV2Dhcp4CRCMapCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4CRCMapCircuit.setStatus("current")
_SleV2Dhcp4CRCMapControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4CRCMapControl = _SleV2Dhcp4CRCMapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2, 2)
)


class _SleV2Dhcp4CRCMapControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4CRCMapControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearDhcpClassMapCircuits", 1),
          ("clearDhcpClassMapRemotes", 2))
    )


_SleV2Dhcp4CRCMapControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4CRCMapControlRequest_Object = MibScalar
sleV2Dhcp4CRCMapControlRequest = _SleV2Dhcp4CRCMapControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2, 2, 1),
    _SleV2Dhcp4CRCMapControlRequest_Type()
)
sleV2Dhcp4CRCMapControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4CRCMapControlRequest.setStatus("current")
_SleV2Dhcp4CRCMapControlStatus_Type = SleControlStatusType
_SleV2Dhcp4CRCMapControlStatus_Object = MibScalar
sleV2Dhcp4CRCMapControlStatus = _SleV2Dhcp4CRCMapControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2, 2, 2),
    _SleV2Dhcp4CRCMapControlStatus_Type()
)
sleV2Dhcp4CRCMapControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4CRCMapControlStatus.setStatus("current")
_SleV2Dhcp4CRCMapControlTimer_Type = Gauge32
_SleV2Dhcp4CRCMapControlTimer_Object = MibScalar
sleV2Dhcp4CRCMapControlTimer = _SleV2Dhcp4CRCMapControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2, 2, 3),
    _SleV2Dhcp4CRCMapControlTimer_Type()
)
sleV2Dhcp4CRCMapControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4CRCMapControlTimer.setStatus("current")
_SleV2Dhcp4CRCMapControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4CRCMapControlTimeStamp_Object = MibScalar
sleV2Dhcp4CRCMapControlTimeStamp = _SleV2Dhcp4CRCMapControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2, 2, 4),
    _SleV2Dhcp4CRCMapControlTimeStamp_Type()
)
sleV2Dhcp4CRCMapControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4CRCMapControlTimeStamp.setStatus("current")
_SleV2Dhcp4CRCMapControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4CRCMapControlReqResult_Object = MibScalar
sleV2Dhcp4CRCMapControlReqResult = _SleV2Dhcp4CRCMapControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2, 2, 5),
    _SleV2Dhcp4CRCMapControlReqResult_Type()
)
sleV2Dhcp4CRCMapControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4CRCMapControlReqResult.setStatus("current")


class _SleV2Dhcp4CRCMapControlClass_Type(OctetString):
    """Custom type sleV2Dhcp4CRCMapControlClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4CRCMapControlClass_Type.__name__ = "OctetString"
_SleV2Dhcp4CRCMapControlClass_Object = MibScalar
sleV2Dhcp4CRCMapControlClass = _SleV2Dhcp4CRCMapControlClass_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2, 2, 6),
    _SleV2Dhcp4CRCMapControlClass_Type()
)
sleV2Dhcp4CRCMapControlClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4CRCMapControlClass.setStatus("current")


class _SleV2Dhcp4CRCMapControlRemote_Type(OctetString):
    """Custom type sleV2Dhcp4CRCMapControlRemote based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4CRCMapControlRemote_Type.__name__ = "OctetString"
_SleV2Dhcp4CRCMapControlRemote_Object = MibScalar
sleV2Dhcp4CRCMapControlRemote = _SleV2Dhcp4CRCMapControlRemote_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2, 2, 7),
    _SleV2Dhcp4CRCMapControlRemote_Type()
)
sleV2Dhcp4CRCMapControlRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4CRCMapControlRemote.setStatus("current")
_SleV2Dhcp4CRCMapNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4CRCMapNotification = _SleV2Dhcp4CRCMapNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2, 3)
)
_SleV2Dhcp4ClassRange_ObjectIdentity = ObjectIdentity
sleV2Dhcp4ClassRange = _SleV2Dhcp4ClassRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3)
)
_SleV2Dhcp4ClassRangeTable_Object = MibTable
sleV2Dhcp4ClassRangeTable = _SleV2Dhcp4ClassRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassRangeTable.setStatus("current")
_SleV2Dhcp4ClassRangeEntry_Object = MibTableRow
sleV2Dhcp4ClassRangeEntry = _SleV2Dhcp4ClassRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 1, 1)
)
sleV2Dhcp4ClassRangeEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PoolIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4ClassName"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeStart"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeEnd"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassRangeEntry.setStatus("current")
_SleV2Dhcp4ClassRangeStart_Type = IpAddress
_SleV2Dhcp4ClassRangeStart_Object = MibTableColumn
sleV2Dhcp4ClassRangeStart = _SleV2Dhcp4ClassRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 1, 1, 1),
    _SleV2Dhcp4ClassRangeStart_Type()
)
sleV2Dhcp4ClassRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassRangeStart.setStatus("current")
_SleV2Dhcp4ClassRangeEnd_Type = IpAddress
_SleV2Dhcp4ClassRangeEnd_Object = MibTableColumn
sleV2Dhcp4ClassRangeEnd = _SleV2Dhcp4ClassRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 1, 1, 2),
    _SleV2Dhcp4ClassRangeEnd_Type()
)
sleV2Dhcp4ClassRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassRangeEnd.setStatus("current")
_SleV2Dhcp4ClassRangeControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4ClassRangeControl = _SleV2Dhcp4ClassRangeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 2)
)


class _SleV2Dhcp4ClassRangeControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4ClassRangeControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcpClassRange", 1),
          ("destoryDhcpClassRange", 2))
    )


_SleV2Dhcp4ClassRangeControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4ClassRangeControlRequest_Object = MibScalar
sleV2Dhcp4ClassRangeControlRequest = _SleV2Dhcp4ClassRangeControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 2, 1),
    _SleV2Dhcp4ClassRangeControlRequest_Type()
)
sleV2Dhcp4ClassRangeControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassRangeControlRequest.setStatus("current")
_SleV2Dhcp4ClassRangeControlStatus_Type = SleControlStatusType
_SleV2Dhcp4ClassRangeControlStatus_Object = MibScalar
sleV2Dhcp4ClassRangeControlStatus = _SleV2Dhcp4ClassRangeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 2, 2),
    _SleV2Dhcp4ClassRangeControlStatus_Type()
)
sleV2Dhcp4ClassRangeControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassRangeControlStatus.setStatus("current")
_SleV2Dhcp4ClassRangeControlTimer_Type = Gauge32
_SleV2Dhcp4ClassRangeControlTimer_Object = MibScalar
sleV2Dhcp4ClassRangeControlTimer = _SleV2Dhcp4ClassRangeControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 2, 3),
    _SleV2Dhcp4ClassRangeControlTimer_Type()
)
sleV2Dhcp4ClassRangeControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassRangeControlTimer.setStatus("current")
_SleV2Dhcp4ClassRangeControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4ClassRangeControlTimeStamp_Object = MibScalar
sleV2Dhcp4ClassRangeControlTimeStamp = _SleV2Dhcp4ClassRangeControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 2, 4),
    _SleV2Dhcp4ClassRangeControlTimeStamp_Type()
)
sleV2Dhcp4ClassRangeControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassRangeControlTimeStamp.setStatus("current")
_SleV2Dhcp4ClassRangeControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4ClassRangeControlReqResult_Object = MibScalar
sleV2Dhcp4ClassRangeControlReqResult = _SleV2Dhcp4ClassRangeControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 2, 5),
    _SleV2Dhcp4ClassRangeControlReqResult_Type()
)
sleV2Dhcp4ClassRangeControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassRangeControlReqResult.setStatus("current")


class _SleV2Dhcp4ClassRangeControlPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4ClassRangeControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4ClassRangeControlPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4ClassRangeControlPoolIndex_Object = MibScalar
sleV2Dhcp4ClassRangeControlPoolIndex = _SleV2Dhcp4ClassRangeControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 2, 6),
    _SleV2Dhcp4ClassRangeControlPoolIndex_Type()
)
sleV2Dhcp4ClassRangeControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassRangeControlPoolIndex.setStatus("current")


class _SleV2Dhcp4ClassRangeControlName_Type(OctetString):
    """Custom type sleV2Dhcp4ClassRangeControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4ClassRangeControlName_Type.__name__ = "OctetString"
_SleV2Dhcp4ClassRangeControlName_Object = MibScalar
sleV2Dhcp4ClassRangeControlName = _SleV2Dhcp4ClassRangeControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 2, 7),
    _SleV2Dhcp4ClassRangeControlName_Type()
)
sleV2Dhcp4ClassRangeControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassRangeControlName.setStatus("current")
_SleV2Dhcp4ClassRangeControlStart_Type = IpAddress
_SleV2Dhcp4ClassRangeControlStart_Object = MibScalar
sleV2Dhcp4ClassRangeControlStart = _SleV2Dhcp4ClassRangeControlStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 2, 8),
    _SleV2Dhcp4ClassRangeControlStart_Type()
)
sleV2Dhcp4ClassRangeControlStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassRangeControlStart.setStatus("current")
_SleV2Dhcp4ClassRangeControlEnd_Type = IpAddress
_SleV2Dhcp4ClassRangeControlEnd_Object = MibScalar
sleV2Dhcp4ClassRangeControlEnd = _SleV2Dhcp4ClassRangeControlEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 2, 9),
    _SleV2Dhcp4ClassRangeControlEnd_Type()
)
sleV2Dhcp4ClassRangeControlEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassRangeControlEnd.setStatus("current")
_SleV2Dhcp4ClassRangeNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4ClassRangeNotification = _SleV2Dhcp4ClassRangeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 3)
)
_SleV2Dhcp4OptionFormat_ObjectIdentity = ObjectIdentity
sleV2Dhcp4OptionFormat = _SleV2Dhcp4OptionFormat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4)
)
_SleV2Dhcp4OptionFormatBase_ObjectIdentity = ObjectIdentity
sleV2Dhcp4OptionFormatBase = _SleV2Dhcp4OptionFormatBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 1)
)
_SleV2Dhcp4OptionFormatTable_Object = MibTable
sleV2Dhcp4OptionFormatTable = _SleV2Dhcp4OptionFormatTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatTable.setStatus("current")
_SleV2Dhcp4OptionFormatEntry_Object = MibTableRow
sleV2Dhcp4OptionFormatEntry = _SleV2Dhcp4OptionFormatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 1, 1, 1)
)
sleV2Dhcp4OptionFormatEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatName"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatEntry.setStatus("current")


class _SleV2Dhcp4OptionFormatName_Type(OctetString):
    """Custom type sleV2Dhcp4OptionFormatName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SleV2Dhcp4OptionFormatName_Type.__name__ = "OctetString"
_SleV2Dhcp4OptionFormatName_Object = MibTableColumn
sleV2Dhcp4OptionFormatName = _SleV2Dhcp4OptionFormatName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 1, 1, 1, 1),
    _SleV2Dhcp4OptionFormatName_Type()
)
sleV2Dhcp4OptionFormatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatName.setStatus("current")
_SleV2Dhcp4OptionFormatControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4OptionFormatControl = _SleV2Dhcp4OptionFormatControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 1, 2)
)


class _SleV2Dhcp4OptionFormatControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4OptionFormatControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createOptionFormat", 1),
          ("destroyOptionFormat", 2))
    )


_SleV2Dhcp4OptionFormatControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionFormatControlRequest_Object = MibScalar
sleV2Dhcp4OptionFormatControlRequest = _SleV2Dhcp4OptionFormatControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 1, 2, 1),
    _SleV2Dhcp4OptionFormatControlRequest_Type()
)
sleV2Dhcp4OptionFormatControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatControlRequest.setStatus("current")
_SleV2Dhcp4OptionFormatControlStatus_Type = SleControlStatusType
_SleV2Dhcp4OptionFormatControlStatus_Object = MibScalar
sleV2Dhcp4OptionFormatControlStatus = _SleV2Dhcp4OptionFormatControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 1, 2, 2),
    _SleV2Dhcp4OptionFormatControlStatus_Type()
)
sleV2Dhcp4OptionFormatControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatControlStatus.setStatus("current")
_SleV2Dhcp4OptionFormatControlTimer_Type = Gauge32
_SleV2Dhcp4OptionFormatControlTimer_Object = MibScalar
sleV2Dhcp4OptionFormatControlTimer = _SleV2Dhcp4OptionFormatControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 1, 2, 3),
    _SleV2Dhcp4OptionFormatControlTimer_Type()
)
sleV2Dhcp4OptionFormatControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatControlTimer.setStatus("current")
_SleV2Dhcp4OptionFormatControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4OptionFormatControlTimeStamp_Object = MibScalar
sleV2Dhcp4OptionFormatControlTimeStamp = _SleV2Dhcp4OptionFormatControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 1, 2, 4),
    _SleV2Dhcp4OptionFormatControlTimeStamp_Type()
)
sleV2Dhcp4OptionFormatControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatControlTimeStamp.setStatus("current")
_SleV2Dhcp4OptionFormatControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4OptionFormatControlReqResult_Object = MibScalar
sleV2Dhcp4OptionFormatControlReqResult = _SleV2Dhcp4OptionFormatControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 1, 2, 5),
    _SleV2Dhcp4OptionFormatControlReqResult_Type()
)
sleV2Dhcp4OptionFormatControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatControlReqResult.setStatus("current")


class _SleV2Dhcp4OptionFormatControlName_Type(OctetString):
    """Custom type sleV2Dhcp4OptionFormatControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4OptionFormatControlName_Type.__name__ = "OctetString"
_SleV2Dhcp4OptionFormatControlName_Object = MibScalar
sleV2Dhcp4OptionFormatControlName = _SleV2Dhcp4OptionFormatControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 1, 2, 6),
    _SleV2Dhcp4OptionFormatControlName_Type()
)
sleV2Dhcp4OptionFormatControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatControlName.setStatus("current")
_SleV2Dhcp4OptionFormatNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4OptionFormatNotification = _SleV2Dhcp4OptionFormatNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 1, 3)
)
_SleV2Dhcp4OptionFormatAttribute_ObjectIdentity = ObjectIdentity
sleV2Dhcp4OptionFormatAttribute = _SleV2Dhcp4OptionFormatAttribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2)
)
_SleV2Dhcp4OptionFormatAttrTable_Object = MibTable
sleV2Dhcp4OptionFormatAttrTable = _SleV2Dhcp4OptionFormatAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrTable.setStatus("current")
_SleV2Dhcp4OptionFormatAttrEntry_Object = MibTableRow
sleV2Dhcp4OptionFormatAttrEntry = _SleV2Dhcp4OptionFormatAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 1, 1)
)
sleV2Dhcp4OptionFormatAttrEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatName"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrID"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrEntry.setStatus("current")


class _SleV2Dhcp4OptionFormatAttrID_Type(Integer32):
    """Custom type sleV2Dhcp4OptionFormatAttrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleV2Dhcp4OptionFormatAttrID_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionFormatAttrID_Object = MibTableColumn
sleV2Dhcp4OptionFormatAttrID = _SleV2Dhcp4OptionFormatAttrID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 1, 1, 1),
    _SleV2Dhcp4OptionFormatAttrID_Type()
)
sleV2Dhcp4OptionFormatAttrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrID.setStatus("current")


class _SleV2Dhcp4OptionFormatAttrLength_Type(Integer32):
    """Custom type sleV2Dhcp4OptionFormatAttrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 64),
    )


_SleV2Dhcp4OptionFormatAttrLength_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionFormatAttrLength_Object = MibTableColumn
sleV2Dhcp4OptionFormatAttrLength = _SleV2Dhcp4OptionFormatAttrLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 1, 1, 2),
    _SleV2Dhcp4OptionFormatAttrLength_Type()
)
sleV2Dhcp4OptionFormatAttrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrLength.setStatus("current")


class _SleV2Dhcp4OptionFormatAttrHiddenLength_Type(Integer32):
    """Custom type sleV2Dhcp4OptionFormatAttrHiddenLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 64),
    )


_SleV2Dhcp4OptionFormatAttrHiddenLength_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionFormatAttrHiddenLength_Object = MibTableColumn
sleV2Dhcp4OptionFormatAttrHiddenLength = _SleV2Dhcp4OptionFormatAttrHiddenLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 1, 1, 3),
    _SleV2Dhcp4OptionFormatAttrHiddenLength_Type()
)
sleV2Dhcp4OptionFormatAttrHiddenLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrHiddenLength.setStatus("current")


class _SleV2Dhcp4OptionFormatAttrType_Type(Integer32):
    """Custom type sleV2Dhcp4OptionFormatAttrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SleV2Dhcp4OptionFormatAttrType_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionFormatAttrType_Object = MibTableColumn
sleV2Dhcp4OptionFormatAttrType = _SleV2Dhcp4OptionFormatAttrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 1, 1, 4),
    _SleV2Dhcp4OptionFormatAttrType_Type()
)
sleV2Dhcp4OptionFormatAttrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrType.setStatus("current")


class _SleV2Dhcp4OptionFormatAttrVarType_Type(Integer32):
    """Custom type sleV2Dhcp4OptionFormatAttrVarType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("hex", 1),
          ("ifIp", 2),
          ("index", 3),
          ("ip", 4),
          ("string", 5))
    )


_SleV2Dhcp4OptionFormatAttrVarType_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionFormatAttrVarType_Object = MibTableColumn
sleV2Dhcp4OptionFormatAttrVarType = _SleV2Dhcp4OptionFormatAttrVarType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 1, 1, 5),
    _SleV2Dhcp4OptionFormatAttrVarType_Type()
)
sleV2Dhcp4OptionFormatAttrVarType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrVarType.setStatus("current")


class _SleV2Dhcp4OptionFormatAttrVarValue_Type(OctetString):
    """Custom type sleV2Dhcp4OptionFormatAttrVarValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleV2Dhcp4OptionFormatAttrVarValue_Type.__name__ = "OctetString"
_SleV2Dhcp4OptionFormatAttrVarValue_Object = MibTableColumn
sleV2Dhcp4OptionFormatAttrVarValue = _SleV2Dhcp4OptionFormatAttrVarValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 1, 1, 6),
    _SleV2Dhcp4OptionFormatAttrVarValue_Type()
)
sleV2Dhcp4OptionFormatAttrVarValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrVarValue.setStatus("current")
_SleV2Dhcp4OptionFormatAttrControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4OptionFormatAttrControl = _SleV2Dhcp4OptionFormatAttrControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 2)
)


class _SleV2Dhcp4OptionFormatAttrControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4OptionFormatAttrControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addOptionFormatAttr", 1),
          ("deleteOptionFormatAttr", 2),
          ("modifyOptionFormatAttr", 3))
    )


_SleV2Dhcp4OptionFormatAttrControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionFormatAttrControlRequest_Object = MibScalar
sleV2Dhcp4OptionFormatAttrControlRequest = _SleV2Dhcp4OptionFormatAttrControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 2, 1),
    _SleV2Dhcp4OptionFormatAttrControlRequest_Type()
)
sleV2Dhcp4OptionFormatAttrControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrControlRequest.setStatus("current")
_SleV2Dhcp4OptionFormatAttrControlStatus_Type = SleControlStatusType
_SleV2Dhcp4OptionFormatAttrControlStatus_Object = MibScalar
sleV2Dhcp4OptionFormatAttrControlStatus = _SleV2Dhcp4OptionFormatAttrControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 2, 2),
    _SleV2Dhcp4OptionFormatAttrControlStatus_Type()
)
sleV2Dhcp4OptionFormatAttrControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrControlStatus.setStatus("current")
_SleV2Dhcp4OptionFormatAttrControlTimer_Type = Gauge32
_SleV2Dhcp4OptionFormatAttrControlTimer_Object = MibScalar
sleV2Dhcp4OptionFormatAttrControlTimer = _SleV2Dhcp4OptionFormatAttrControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 2, 3),
    _SleV2Dhcp4OptionFormatAttrControlTimer_Type()
)
sleV2Dhcp4OptionFormatAttrControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrControlTimer.setStatus("current")
_SleV2Dhcp4OptionFormatAttrControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4OptionFormatAttrControlTimeStamp_Object = MibScalar
sleV2Dhcp4OptionFormatAttrControlTimeStamp = _SleV2Dhcp4OptionFormatAttrControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 2, 4),
    _SleV2Dhcp4OptionFormatAttrControlTimeStamp_Type()
)
sleV2Dhcp4OptionFormatAttrControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrControlTimeStamp.setStatus("current")
_SleV2Dhcp4OptionFormatAttrControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4OptionFormatAttrControlReqResult_Object = MibScalar
sleV2Dhcp4OptionFormatAttrControlReqResult = _SleV2Dhcp4OptionFormatAttrControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 2, 5),
    _SleV2Dhcp4OptionFormatAttrControlReqResult_Type()
)
sleV2Dhcp4OptionFormatAttrControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrControlReqResult.setStatus("current")


class _SleV2Dhcp4OptionFormatAttrControlName_Type(OctetString):
    """Custom type sleV2Dhcp4OptionFormatAttrControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SleV2Dhcp4OptionFormatAttrControlName_Type.__name__ = "OctetString"
_SleV2Dhcp4OptionFormatAttrControlName_Object = MibScalar
sleV2Dhcp4OptionFormatAttrControlName = _SleV2Dhcp4OptionFormatAttrControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 2, 6),
    _SleV2Dhcp4OptionFormatAttrControlName_Type()
)
sleV2Dhcp4OptionFormatAttrControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrControlName.setStatus("current")


class _SleV2Dhcp4OptionFormatAttrControlID_Type(Integer32):
    """Custom type sleV2Dhcp4OptionFormatAttrControlID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SleV2Dhcp4OptionFormatAttrControlID_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionFormatAttrControlID_Object = MibScalar
sleV2Dhcp4OptionFormatAttrControlID = _SleV2Dhcp4OptionFormatAttrControlID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 2, 7),
    _SleV2Dhcp4OptionFormatAttrControlID_Type()
)
sleV2Dhcp4OptionFormatAttrControlID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrControlID.setStatus("current")


class _SleV2Dhcp4OptionFormatAttrControlLength_Type(Integer32):
    """Custom type sleV2Dhcp4OptionFormatAttrControlLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 64),
    )


_SleV2Dhcp4OptionFormatAttrControlLength_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionFormatAttrControlLength_Object = MibScalar
sleV2Dhcp4OptionFormatAttrControlLength = _SleV2Dhcp4OptionFormatAttrControlLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 2, 8),
    _SleV2Dhcp4OptionFormatAttrControlLength_Type()
)
sleV2Dhcp4OptionFormatAttrControlLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrControlLength.setStatus("current")


class _SleV2Dhcp4OptionFormatAttrControlHiddenLength_Type(Integer32):
    """Custom type sleV2Dhcp4OptionFormatAttrControlHiddenLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 64),
    )


_SleV2Dhcp4OptionFormatAttrControlHiddenLength_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionFormatAttrControlHiddenLength_Object = MibScalar
sleV2Dhcp4OptionFormatAttrControlHiddenLength = _SleV2Dhcp4OptionFormatAttrControlHiddenLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 2, 9),
    _SleV2Dhcp4OptionFormatAttrControlHiddenLength_Type()
)
sleV2Dhcp4OptionFormatAttrControlHiddenLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrControlHiddenLength.setStatus("current")


class _SleV2Dhcp4OptionFormatAttrControlType_Type(Integer32):
    """Custom type sleV2Dhcp4OptionFormatAttrControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SleV2Dhcp4OptionFormatAttrControlType_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionFormatAttrControlType_Object = MibScalar
sleV2Dhcp4OptionFormatAttrControlType = _SleV2Dhcp4OptionFormatAttrControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 2, 10),
    _SleV2Dhcp4OptionFormatAttrControlType_Type()
)
sleV2Dhcp4OptionFormatAttrControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrControlType.setStatus("current")


class _SleV2Dhcp4OptionFormatAttrControlVarType_Type(Integer32):
    """Custom type sleV2Dhcp4OptionFormatAttrControlVarType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("hex", 1),
          ("ifIp", 2),
          ("index", 3),
          ("ip", 4),
          ("string", 5))
    )


_SleV2Dhcp4OptionFormatAttrControlVarType_Type.__name__ = "Integer32"
_SleV2Dhcp4OptionFormatAttrControlVarType_Object = MibScalar
sleV2Dhcp4OptionFormatAttrControlVarType = _SleV2Dhcp4OptionFormatAttrControlVarType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 2, 11),
    _SleV2Dhcp4OptionFormatAttrControlVarType_Type()
)
sleV2Dhcp4OptionFormatAttrControlVarType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrControlVarType.setStatus("current")


class _SleV2Dhcp4OptionFormatAttrControlVarValue_Type(OctetString):
    """Custom type sleV2Dhcp4OptionFormatAttrControlVarValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleV2Dhcp4OptionFormatAttrControlVarValue_Type.__name__ = "OctetString"
_SleV2Dhcp4OptionFormatAttrControlVarValue_Object = MibScalar
sleV2Dhcp4OptionFormatAttrControlVarValue = _SleV2Dhcp4OptionFormatAttrControlVarValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 2, 12),
    _SleV2Dhcp4OptionFormatAttrControlVarValue_Type()
)
sleV2Dhcp4OptionFormatAttrControlVarValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrControlVarValue.setStatus("current")
_SleV2Dhcp4OptionFormatAttrNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4OptionFormatAttrNotification = _SleV2Dhcp4OptionFormatAttrNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 3)
)
_SleV2Dhcp4Filter_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Filter = _SleV2Dhcp4Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4)
)
_SleV2Dhcp4FilterPort_ObjectIdentity = ObjectIdentity
sleV2Dhcp4FilterPort = _SleV2Dhcp4FilterPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 1)
)
_SleV2Dhcp4FilterPortTable_Object = MibTable
sleV2Dhcp4FilterPortTable = _SleV2Dhcp4FilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterPortTable.setStatus("current")
_SleV2Dhcp4FilterPortEntry_Object = MibTableRow
sleV2Dhcp4FilterPortEntry = _SleV2Dhcp4FilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 1, 1, 1)
)
sleV2Dhcp4FilterPortEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4FilterPortIndex"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterPortEntry.setStatus("current")


class _SleV2Dhcp4FilterPortIndex_Type(Integer32):
    """Custom type sleV2Dhcp4FilterPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4FilterPortIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4FilterPortIndex_Object = MibTableColumn
sleV2Dhcp4FilterPortIndex = _SleV2Dhcp4FilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 1, 1, 1, 1),
    _SleV2Dhcp4FilterPortIndex_Type()
)
sleV2Dhcp4FilterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterPortIndex.setStatus("current")


class _SleV2Dhcp4FilterPortState_Type(Integer32):
    """Custom type sleV2Dhcp4FilterPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Dhcp4FilterPortState_Type.__name__ = "Integer32"
_SleV2Dhcp4FilterPortState_Object = MibTableColumn
sleV2Dhcp4FilterPortState = _SleV2Dhcp4FilterPortState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 1, 1, 1, 2),
    _SleV2Dhcp4FilterPortState_Type()
)
sleV2Dhcp4FilterPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterPortState.setStatus("current")
_SleV2Dhcp4FilterPortControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4FilterPortControl = _SleV2Dhcp4FilterPortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 1, 2)
)


class _SleV2Dhcp4FilterPortControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4FilterPortControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setDhcpFilterPortMode", 1)
    )


_SleV2Dhcp4FilterPortControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4FilterPortControlRequest_Object = MibScalar
sleV2Dhcp4FilterPortControlRequest = _SleV2Dhcp4FilterPortControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 1, 2, 1),
    _SleV2Dhcp4FilterPortControlRequest_Type()
)
sleV2Dhcp4FilterPortControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterPortControlRequest.setStatus("current")
_SleV2Dhcp4FilterPortControlStatus_Type = SleControlStatusType
_SleV2Dhcp4FilterPortControlStatus_Object = MibScalar
sleV2Dhcp4FilterPortControlStatus = _SleV2Dhcp4FilterPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 1, 2, 2),
    _SleV2Dhcp4FilterPortControlStatus_Type()
)
sleV2Dhcp4FilterPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterPortControlStatus.setStatus("current")
_SleV2Dhcp4FilterPortControlTimer_Type = Gauge32
_SleV2Dhcp4FilterPortControlTimer_Object = MibScalar
sleV2Dhcp4FilterPortControlTimer = _SleV2Dhcp4FilterPortControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 1, 2, 3),
    _SleV2Dhcp4FilterPortControlTimer_Type()
)
sleV2Dhcp4FilterPortControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterPortControlTimer.setStatus("current")
_SleV2Dhcp4FilterPortControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4FilterPortControlTimeStamp_Object = MibScalar
sleV2Dhcp4FilterPortControlTimeStamp = _SleV2Dhcp4FilterPortControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 1, 2, 4),
    _SleV2Dhcp4FilterPortControlTimeStamp_Type()
)
sleV2Dhcp4FilterPortControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterPortControlTimeStamp.setStatus("current")
_SleV2Dhcp4FilterPortControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4FilterPortControlReqResult_Object = MibScalar
sleV2Dhcp4FilterPortControlReqResult = _SleV2Dhcp4FilterPortControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 1, 2, 5),
    _SleV2Dhcp4FilterPortControlReqResult_Type()
)
sleV2Dhcp4FilterPortControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterPortControlReqResult.setStatus("current")


class _SleV2Dhcp4FilterPortControlIndex_Type(Integer32):
    """Custom type sleV2Dhcp4FilterPortControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4FilterPortControlIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4FilterPortControlIndex_Object = MibScalar
sleV2Dhcp4FilterPortControlIndex = _SleV2Dhcp4FilterPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 1, 2, 6),
    _SleV2Dhcp4FilterPortControlIndex_Type()
)
sleV2Dhcp4FilterPortControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterPortControlIndex.setStatus("current")


class _SleV2Dhcp4FilterPortControlState_Type(Integer32):
    """Custom type sleV2Dhcp4FilterPortControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Dhcp4FilterPortControlState_Type.__name__ = "Integer32"
_SleV2Dhcp4FilterPortControlState_Object = MibScalar
sleV2Dhcp4FilterPortControlState = _SleV2Dhcp4FilterPortControlState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 1, 2, 7),
    _SleV2Dhcp4FilterPortControlState_Type()
)
sleV2Dhcp4FilterPortControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterPortControlState.setStatus("current")
_SleV2Dhcp4FilterPortNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4FilterPortNotification = _SleV2Dhcp4FilterPortNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 1, 3)
)
_SleV2Dhcp4FilterAddress_ObjectIdentity = ObjectIdentity
sleV2Dhcp4FilterAddress = _SleV2Dhcp4FilterAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 2)
)
_SleV2Dhcp4FilterAddressTable_Object = MibTable
sleV2Dhcp4FilterAddressTable = _SleV2Dhcp4FilterAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterAddressTable.setStatus("current")
_SleV2Dhcp4FilterAddressEntry_Object = MibTableRow
sleV2Dhcp4FilterAddressEntry = _SleV2Dhcp4FilterAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 2, 1, 1)
)
sleV2Dhcp4FilterAddressEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressMac"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterAddressEntry.setStatus("current")
_SleV2Dhcp4FilterAddressMac_Type = MacAddress
_SleV2Dhcp4FilterAddressMac_Object = MibTableColumn
sleV2Dhcp4FilterAddressMac = _SleV2Dhcp4FilterAddressMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 2, 1, 1, 1),
    _SleV2Dhcp4FilterAddressMac_Type()
)
sleV2Dhcp4FilterAddressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterAddressMac.setStatus("current")


class _SleV2Dhcp4FilterAddressType_Type(Bits):
    """Custom type sleV2Dhcp4FilterAddressType based on Bits"""
    namedValues = NamedValues(
        *(("discover", 0),
          ("offer", 1),
          ("request", 2),
          ("decline", 3),
          ("ack", 4),
          ("nak", 5),
          ("release", 6),
          ("inform", 7))
    )

_SleV2Dhcp4FilterAddressType_Type.__name__ = "Bits"
_SleV2Dhcp4FilterAddressType_Object = MibTableColumn
sleV2Dhcp4FilterAddressType = _SleV2Dhcp4FilterAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 2, 1, 1, 2),
    _SleV2Dhcp4FilterAddressType_Type()
)
sleV2Dhcp4FilterAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterAddressType.setStatus("current")
_SleV2Dhcp4FilterAddressControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4FilterAddressControl = _SleV2Dhcp4FilterAddressControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 2, 2)
)


class _SleV2Dhcp4FilterAddressControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4FilterAddressControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDhcpFilterAddress", 1),
          ("destroyDhcpFilterAddress", 2))
    )


_SleV2Dhcp4FilterAddressControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4FilterAddressControlRequest_Object = MibScalar
sleV2Dhcp4FilterAddressControlRequest = _SleV2Dhcp4FilterAddressControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 2, 2, 1),
    _SleV2Dhcp4FilterAddressControlRequest_Type()
)
sleV2Dhcp4FilterAddressControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterAddressControlRequest.setStatus("current")
_SleV2Dhcp4FilterAddressControlStatus_Type = SleControlStatusType
_SleV2Dhcp4FilterAddressControlStatus_Object = MibScalar
sleV2Dhcp4FilterAddressControlStatus = _SleV2Dhcp4FilterAddressControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 2, 2, 2),
    _SleV2Dhcp4FilterAddressControlStatus_Type()
)
sleV2Dhcp4FilterAddressControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterAddressControlStatus.setStatus("current")
_SleV2Dhcp4FilterAddressControlTimer_Type = Gauge32
_SleV2Dhcp4FilterAddressControlTimer_Object = MibScalar
sleV2Dhcp4FilterAddressControlTimer = _SleV2Dhcp4FilterAddressControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 2, 2, 3),
    _SleV2Dhcp4FilterAddressControlTimer_Type()
)
sleV2Dhcp4FilterAddressControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterAddressControlTimer.setStatus("current")
_SleV2Dhcp4FilterAddressControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4FilterAddressControlTimeStamp_Object = MibScalar
sleV2Dhcp4FilterAddressControlTimeStamp = _SleV2Dhcp4FilterAddressControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 2, 2, 4),
    _SleV2Dhcp4FilterAddressControlTimeStamp_Type()
)
sleV2Dhcp4FilterAddressControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterAddressControlTimeStamp.setStatus("current")
_SleV2Dhcp4FilterAddressControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4FilterAddressControlReqResult_Object = MibScalar
sleV2Dhcp4FilterAddressControlReqResult = _SleV2Dhcp4FilterAddressControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 2, 2, 5),
    _SleV2Dhcp4FilterAddressControlReqResult_Type()
)
sleV2Dhcp4FilterAddressControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterAddressControlReqResult.setStatus("current")
_SleV2Dhcp4FilterAddressControlMac_Type = MacAddress
_SleV2Dhcp4FilterAddressControlMac_Object = MibScalar
sleV2Dhcp4FilterAddressControlMac = _SleV2Dhcp4FilterAddressControlMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 2, 2, 6),
    _SleV2Dhcp4FilterAddressControlMac_Type()
)
sleV2Dhcp4FilterAddressControlMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterAddressControlMac.setStatus("current")


class _SleV2Dhcp4FilterAddressControlType_Type(Bits):
    """Custom type sleV2Dhcp4FilterAddressControlType based on Bits"""
    namedValues = NamedValues(
        *(("discover", 0),
          ("offer", 1),
          ("request", 2),
          ("decline", 3),
          ("ack", 4),
          ("nak", 5),
          ("release", 6),
          ("inform", 7))
    )

_SleV2Dhcp4FilterAddressControlType_Type.__name__ = "Bits"
_SleV2Dhcp4FilterAddressControlType_Object = MibScalar
sleV2Dhcp4FilterAddressControlType = _SleV2Dhcp4FilterAddressControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 2, 2, 7),
    _SleV2Dhcp4FilterAddressControlType_Type()
)
sleV2Dhcp4FilterAddressControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterAddressControlType.setStatus("current")
_SleV2Dhcp4FilterAddressNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4FilterAddressNotification = _SleV2Dhcp4FilterAddressNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 2, 3)
)
_SleV2Dhcp4Illegal_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Illegal = _SleV2Dhcp4Illegal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 3)
)
_SleV2Dhcp4IllegalTable_Object = MibTable
sleV2Dhcp4IllegalTable = _SleV2Dhcp4IllegalTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4IllegalTable.setStatus("current")
_SleV2Dhcp4IllegalEntry_Object = MibTableRow
sleV2Dhcp4IllegalEntry = _SleV2Dhcp4IllegalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 3, 1, 1)
)
sleV2Dhcp4IllegalEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4IllegalAddress"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4IllegalMac"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4IllegalEntry.setStatus("current")
_SleV2Dhcp4IllegalAddress_Type = IpAddress
_SleV2Dhcp4IllegalAddress_Object = MibTableColumn
sleV2Dhcp4IllegalAddress = _SleV2Dhcp4IllegalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 3, 1, 1, 1),
    _SleV2Dhcp4IllegalAddress_Type()
)
sleV2Dhcp4IllegalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4IllegalAddress.setStatus("current")
_SleV2Dhcp4IllegalMac_Type = MacAddress
_SleV2Dhcp4IllegalMac_Object = MibTableColumn
sleV2Dhcp4IllegalMac = _SleV2Dhcp4IllegalMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 3, 1, 1, 2),
    _SleV2Dhcp4IllegalMac_Type()
)
sleV2Dhcp4IllegalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4IllegalMac.setStatus("current")
_SleV2Dhcp4IllegalTime_Type = Unsigned32
_SleV2Dhcp4IllegalTime_Object = MibTableColumn
sleV2Dhcp4IllegalTime = _SleV2Dhcp4IllegalTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 3, 1, 1, 3),
    _SleV2Dhcp4IllegalTime_Type()
)
sleV2Dhcp4IllegalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4IllegalTime.setStatus("current")
_SleV2Dhcp4IllegalControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4IllegalControl = _SleV2Dhcp4IllegalControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 3, 2)
)


class _SleV2Dhcp4IllegalControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4IllegalControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearIllegal", 1)
    )


_SleV2Dhcp4IllegalControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4IllegalControlRequest_Object = MibScalar
sleV2Dhcp4IllegalControlRequest = _SleV2Dhcp4IllegalControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 3, 2, 1),
    _SleV2Dhcp4IllegalControlRequest_Type()
)
sleV2Dhcp4IllegalControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4IllegalControlRequest.setStatus("current")
_SleV2Dhcp4IllegalControlStatus_Type = SleControlStatusType
_SleV2Dhcp4IllegalControlStatus_Object = MibScalar
sleV2Dhcp4IllegalControlStatus = _SleV2Dhcp4IllegalControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 3, 2, 2),
    _SleV2Dhcp4IllegalControlStatus_Type()
)
sleV2Dhcp4IllegalControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4IllegalControlStatus.setStatus("current")
_SleV2Dhcp4IllegalControlTimer_Type = Gauge32
_SleV2Dhcp4IllegalControlTimer_Object = MibScalar
sleV2Dhcp4IllegalControlTimer = _SleV2Dhcp4IllegalControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 3, 2, 3),
    _SleV2Dhcp4IllegalControlTimer_Type()
)
sleV2Dhcp4IllegalControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4IllegalControlTimer.setStatus("current")
_SleV2Dhcp4IllegalControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4IllegalControlTimeStamp_Object = MibScalar
sleV2Dhcp4IllegalControlTimeStamp = _SleV2Dhcp4IllegalControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 3, 2, 4),
    _SleV2Dhcp4IllegalControlTimeStamp_Type()
)
sleV2Dhcp4IllegalControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4IllegalControlTimeStamp.setStatus("current")
_SleV2Dhcp4IllegalControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4IllegalControlReqResult_Object = MibScalar
sleV2Dhcp4IllegalControlReqResult = _SleV2Dhcp4IllegalControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 3, 2, 5),
    _SleV2Dhcp4IllegalControlReqResult_Type()
)
sleV2Dhcp4IllegalControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4IllegalControlReqResult.setStatus("current")
_SleV2Dhcp4IllegalNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4IllegalNotification = _SleV2Dhcp4IllegalNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 3, 3)
)
_SleV2Dhcp4Stats_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Stats = _SleV2Dhcp4Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5)
)
_SleV2Dhcp4PacketStats_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PacketStats = _SleV2Dhcp4PacketStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1)
)
_SleV2Dhcp4PacketStatsInfo_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PacketStatsInfo = _SleV2Dhcp4PacketStatsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1)
)
_SleV2Dhcp4PacketStatsReceived_Type = Unsigned32
_SleV2Dhcp4PacketStatsReceived_Object = MibScalar
sleV2Dhcp4PacketStatsReceived = _SleV2Dhcp4PacketStatsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 1),
    _SleV2Dhcp4PacketStatsReceived_Type()
)
sleV2Dhcp4PacketStatsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsReceived.setStatus("current")
_SleV2Dhcp4PacketStatsSent_Type = Unsigned32
_SleV2Dhcp4PacketStatsSent_Object = MibScalar
sleV2Dhcp4PacketStatsSent = _SleV2Dhcp4PacketStatsSent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 2),
    _SleV2Dhcp4PacketStatsSent_Type()
)
sleV2Dhcp4PacketStatsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsSent.setStatus("current")
_SleV2Dhcp4PacketStatsReceivedErrors_Type = Unsigned32
_SleV2Dhcp4PacketStatsReceivedErrors_Object = MibScalar
sleV2Dhcp4PacketStatsReceivedErrors = _SleV2Dhcp4PacketStatsReceivedErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 3),
    _SleV2Dhcp4PacketStatsReceivedErrors_Type()
)
sleV2Dhcp4PacketStatsReceivedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsReceivedErrors.setStatus("current")
_SleV2Dhcp4PacketStatsSentErrors_Type = Unsigned32
_SleV2Dhcp4PacketStatsSentErrors_Object = MibScalar
sleV2Dhcp4PacketStatsSentErrors = _SleV2Dhcp4PacketStatsSentErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 4),
    _SleV2Dhcp4PacketStatsSentErrors_Type()
)
sleV2Dhcp4PacketStatsSentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsSentErrors.setStatus("current")
_SleV2Dhcp4PacketStatsBootpReceivedRequests_Type = Unsigned32
_SleV2Dhcp4PacketStatsBootpReceivedRequests_Object = MibScalar
sleV2Dhcp4PacketStatsBootpReceivedRequests = _SleV2Dhcp4PacketStatsBootpReceivedRequests_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 5),
    _SleV2Dhcp4PacketStatsBootpReceivedRequests_Type()
)
sleV2Dhcp4PacketStatsBootpReceivedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsBootpReceivedRequests.setStatus("current")
_SleV2Dhcp4PacketStatsBootpReceivedReplies_Type = Unsigned32
_SleV2Dhcp4PacketStatsBootpReceivedReplies_Object = MibScalar
sleV2Dhcp4PacketStatsBootpReceivedReplies = _SleV2Dhcp4PacketStatsBootpReceivedReplies_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 6),
    _SleV2Dhcp4PacketStatsBootpReceivedReplies_Type()
)
sleV2Dhcp4PacketStatsBootpReceivedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsBootpReceivedReplies.setStatus("current")
_SleV2Dhcp4PacketStatsBootpSentRequests_Type = Unsigned32
_SleV2Dhcp4PacketStatsBootpSentRequests_Object = MibScalar
sleV2Dhcp4PacketStatsBootpSentRequests = _SleV2Dhcp4PacketStatsBootpSentRequests_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 7),
    _SleV2Dhcp4PacketStatsBootpSentRequests_Type()
)
sleV2Dhcp4PacketStatsBootpSentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsBootpSentRequests.setStatus("current")
_SleV2Dhcp4PacketStatsBootpSentReplies_Type = Unsigned32
_SleV2Dhcp4PacketStatsBootpSentReplies_Object = MibScalar
sleV2Dhcp4PacketStatsBootpSentReplies = _SleV2Dhcp4PacketStatsBootpSentReplies_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 8),
    _SleV2Dhcp4PacketStatsBootpSentReplies_Type()
)
sleV2Dhcp4PacketStatsBootpSentReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsBootpSentReplies.setStatus("current")
_SleV2Dhcp4PacketStatsReceivedDiscover_Type = Unsigned32
_SleV2Dhcp4PacketStatsReceivedDiscover_Object = MibScalar
sleV2Dhcp4PacketStatsReceivedDiscover = _SleV2Dhcp4PacketStatsReceivedDiscover_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 9),
    _SleV2Dhcp4PacketStatsReceivedDiscover_Type()
)
sleV2Dhcp4PacketStatsReceivedDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsReceivedDiscover.setStatus("current")
_SleV2Dhcp4PacketStatsReceivedRequest_Type = Unsigned32
_SleV2Dhcp4PacketStatsReceivedRequest_Object = MibScalar
sleV2Dhcp4PacketStatsReceivedRequest = _SleV2Dhcp4PacketStatsReceivedRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 10),
    _SleV2Dhcp4PacketStatsReceivedRequest_Type()
)
sleV2Dhcp4PacketStatsReceivedRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsReceivedRequest.setStatus("current")
_SleV2Dhcp4PacketStatsReceivedRelease_Type = Unsigned32
_SleV2Dhcp4PacketStatsReceivedRelease_Object = MibScalar
sleV2Dhcp4PacketStatsReceivedRelease = _SleV2Dhcp4PacketStatsReceivedRelease_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 11),
    _SleV2Dhcp4PacketStatsReceivedRelease_Type()
)
sleV2Dhcp4PacketStatsReceivedRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsReceivedRelease.setStatus("current")
_SleV2Dhcp4PacketStatscReceivedInform_Type = Unsigned32
_SleV2Dhcp4PacketStatscReceivedInform_Object = MibScalar
sleV2Dhcp4PacketStatscReceivedInform = _SleV2Dhcp4PacketStatscReceivedInform_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 12),
    _SleV2Dhcp4PacketStatscReceivedInform_Type()
)
sleV2Dhcp4PacketStatscReceivedInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatscReceivedInform.setStatus("current")
_SleV2Dhcp4PacketStatsReceivedDecline_Type = Unsigned32
_SleV2Dhcp4PacketStatsReceivedDecline_Object = MibScalar
sleV2Dhcp4PacketStatsReceivedDecline = _SleV2Dhcp4PacketStatsReceivedDecline_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 13),
    _SleV2Dhcp4PacketStatsReceivedDecline_Type()
)
sleV2Dhcp4PacketStatsReceivedDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsReceivedDecline.setStatus("current")
_SleV2Dhcp4PacketStatsSentOffer_Type = Unsigned32
_SleV2Dhcp4PacketStatsSentOffer_Object = MibScalar
sleV2Dhcp4PacketStatsSentOffer = _SleV2Dhcp4PacketStatsSentOffer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 14),
    _SleV2Dhcp4PacketStatsSentOffer_Type()
)
sleV2Dhcp4PacketStatsSentOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsSentOffer.setStatus("current")
_SleV2Dhcp4PacketStatsSentAck_Type = Unsigned32
_SleV2Dhcp4PacketStatsSentAck_Object = MibScalar
sleV2Dhcp4PacketStatsSentAck = _SleV2Dhcp4PacketStatsSentAck_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 15),
    _SleV2Dhcp4PacketStatsSentAck_Type()
)
sleV2Dhcp4PacketStatsSentAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsSentAck.setStatus("current")
_SleV2Dhcp4PacketStatsSentNak_Type = Unsigned32
_SleV2Dhcp4PacketStatsSentNak_Object = MibScalar
sleV2Dhcp4PacketStatsSentNak = _SleV2Dhcp4PacketStatsSentNak_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 16),
    _SleV2Dhcp4PacketStatsSentNak_Type()
)
sleV2Dhcp4PacketStatsSentNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsSentNak.setStatus("current")
_SleV2Dhcp4SummaryPoolCnt_Type = Unsigned32
_SleV2Dhcp4SummaryPoolCnt_Object = MibScalar
sleV2Dhcp4SummaryPoolCnt = _SleV2Dhcp4SummaryPoolCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 17),
    _SleV2Dhcp4SummaryPoolCnt_Type()
)
sleV2Dhcp4SummaryPoolCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4SummaryPoolCnt.setStatus("current")
_SleV2Dhcp4SummaryTotal_Type = Unsigned32
_SleV2Dhcp4SummaryTotal_Object = MibScalar
sleV2Dhcp4SummaryTotal = _SleV2Dhcp4SummaryTotal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 18),
    _SleV2Dhcp4SummaryTotal_Type()
)
sleV2Dhcp4SummaryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4SummaryTotal.setStatus("current")
_SleV2Dhcp4SummaryAvailable_Type = Unsigned32
_SleV2Dhcp4SummaryAvailable_Object = MibScalar
sleV2Dhcp4SummaryAvailable = _SleV2Dhcp4SummaryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 19),
    _SleV2Dhcp4SummaryAvailable_Type()
)
sleV2Dhcp4SummaryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4SummaryAvailable.setStatus("current")
_SleV2Dhcp4SummaryAbandon_Type = Unsigned32
_SleV2Dhcp4SummaryAbandon_Object = MibScalar
sleV2Dhcp4SummaryAbandon = _SleV2Dhcp4SummaryAbandon_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 20),
    _SleV2Dhcp4SummaryAbandon_Type()
)
sleV2Dhcp4SummaryAbandon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4SummaryAbandon.setStatus("current")
_SleV2Dhcp4SummaryBound_Type = Unsigned32
_SleV2Dhcp4SummaryBound_Object = MibScalar
sleV2Dhcp4SummaryBound = _SleV2Dhcp4SummaryBound_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 21),
    _SleV2Dhcp4SummaryBound_Type()
)
sleV2Dhcp4SummaryBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4SummaryBound.setStatus("current")
_SleV2Dhcp4SummaryOffered_Type = Unsigned32
_SleV2Dhcp4SummaryOffered_Object = MibScalar
sleV2Dhcp4SummaryOffered = _SleV2Dhcp4SummaryOffered_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 22),
    _SleV2Dhcp4SummaryOffered_Type()
)
sleV2Dhcp4SummaryOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4SummaryOffered.setStatus("current")
_SleV2Dhcp4SummaryFixed_Type = Unsigned32
_SleV2Dhcp4SummaryFixed_Object = MibScalar
sleV2Dhcp4SummaryFixed = _SleV2Dhcp4SummaryFixed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 23),
    _SleV2Dhcp4SummaryFixed_Type()
)
sleV2Dhcp4SummaryFixed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4SummaryFixed.setStatus("current")
_SleV2Dhcp4SummaryAllocated_Type = Unsigned32
_SleV2Dhcp4SummaryAllocated_Object = MibScalar
sleV2Dhcp4SummaryAllocated = _SleV2Dhcp4SummaryAllocated_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 1, 24),
    _SleV2Dhcp4SummaryAllocated_Type()
)
sleV2Dhcp4SummaryAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4SummaryAllocated.setStatus("current")
_SleV2Dhcp4PacketStatsControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PacketStatsControl = _SleV2Dhcp4PacketStatsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 2)
)


class _SleV2Dhcp4PacketStatsControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4PacketStatsControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearDhcpPacketStats", 1)
    )


_SleV2Dhcp4PacketStatsControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4PacketStatsControlRequest_Object = MibScalar
sleV2Dhcp4PacketStatsControlRequest = _SleV2Dhcp4PacketStatsControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 2, 1),
    _SleV2Dhcp4PacketStatsControlRequest_Type()
)
sleV2Dhcp4PacketStatsControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsControlRequest.setStatus("current")
_SleV2Dhcp4PacketStatsControlStatus_Type = SleControlStatusType
_SleV2Dhcp4PacketStatsControlStatus_Object = MibScalar
sleV2Dhcp4PacketStatsControlStatus = _SleV2Dhcp4PacketStatsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 2, 2),
    _SleV2Dhcp4PacketStatsControlStatus_Type()
)
sleV2Dhcp4PacketStatsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsControlStatus.setStatus("current")
_SleV2Dhcp4PacketStatsControlTimer_Type = Gauge32
_SleV2Dhcp4PacketStatsControlTimer_Object = MibScalar
sleV2Dhcp4PacketStatsControlTimer = _SleV2Dhcp4PacketStatsControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 2, 3),
    _SleV2Dhcp4PacketStatsControlTimer_Type()
)
sleV2Dhcp4PacketStatsControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsControlTimer.setStatus("current")
_SleV2Dhcp4PacketStatsControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4PacketStatsControlTimeStamp_Object = MibScalar
sleV2Dhcp4PacketStatsControlTimeStamp = _SleV2Dhcp4PacketStatsControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 2, 4),
    _SleV2Dhcp4PacketStatsControlTimeStamp_Type()
)
sleV2Dhcp4PacketStatsControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsControlTimeStamp.setStatus("current")
_SleV2Dhcp4PacketStatsControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4PacketStatsControlReqResult_Object = MibScalar
sleV2Dhcp4PacketStatsControlReqResult = _SleV2Dhcp4PacketStatsControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 2, 5),
    _SleV2Dhcp4PacketStatsControlReqResult_Type()
)
sleV2Dhcp4PacketStatsControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsControlReqResult.setStatus("current")
_SleV2Dhcp4PacketStatsNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PacketStatsNotification = _SleV2Dhcp4PacketStatsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 3)
)
_SleV2Dhcp4Leased_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Leased = _SleV2Dhcp4Leased_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2)
)
_SleV2Dhcp4LeasedTable_Object = MibTable
sleV2Dhcp4LeasedTable = _SleV2Dhcp4LeasedTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedTable.setStatus("current")
_SleV2Dhcp4LeasedEntry_Object = MibTableRow
sleV2Dhcp4LeasedEntry = _SleV2Dhcp4LeasedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 1, 1)
)
sleV2Dhcp4LeasedEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedAddress"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedEntry.setStatus("current")
_SleV2Dhcp4LeasedAddress_Type = IpAddress
_SleV2Dhcp4LeasedAddress_Object = MibTableColumn
sleV2Dhcp4LeasedAddress = _SleV2Dhcp4LeasedAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 1, 1, 1),
    _SleV2Dhcp4LeasedAddress_Type()
)
sleV2Dhcp4LeasedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedAddress.setStatus("current")


class _SleV2Dhcp4LeasedPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4LeasedPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4LeasedPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4LeasedPoolIndex_Object = MibTableColumn
sleV2Dhcp4LeasedPoolIndex = _SleV2Dhcp4LeasedPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 1, 1, 2),
    _SleV2Dhcp4LeasedPoolIndex_Type()
)
sleV2Dhcp4LeasedPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedPoolIndex.setStatus("current")


class _SleV2Dhcp4LeasedStatus_Type(Integer32):
    """Custom type sleV2Dhcp4LeasedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("offered", 2),
          ("bound", 3),
          ("abandon", 4),
          ("free", 5))
    )


_SleV2Dhcp4LeasedStatus_Type.__name__ = "Integer32"
_SleV2Dhcp4LeasedStatus_Object = MibTableColumn
sleV2Dhcp4LeasedStatus = _SleV2Dhcp4LeasedStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 1, 1, 3),
    _SleV2Dhcp4LeasedStatus_Type()
)
sleV2Dhcp4LeasedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedStatus.setStatus("current")
_SleV2Dhcp4LeasedMac_Type = MacAddress
_SleV2Dhcp4LeasedMac_Object = MibTableColumn
sleV2Dhcp4LeasedMac = _SleV2Dhcp4LeasedMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 1, 1, 4),
    _SleV2Dhcp4LeasedMac_Type()
)
sleV2Dhcp4LeasedMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedMac.setStatus("current")


class _SleV2Dhcp4LeasedHostName_Type(OctetString):
    """Custom type sleV2Dhcp4LeasedHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4LeasedHostName_Type.__name__ = "OctetString"
_SleV2Dhcp4LeasedHostName_Object = MibTableColumn
sleV2Dhcp4LeasedHostName = _SleV2Dhcp4LeasedHostName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 1, 1, 5),
    _SleV2Dhcp4LeasedHostName_Type()
)
sleV2Dhcp4LeasedHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedHostName.setStatus("current")


class _SleV2Dhcp4LeasedClientId_Type(OctetString):
    """Custom type sleV2Dhcp4LeasedClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4LeasedClientId_Type.__name__ = "OctetString"
_SleV2Dhcp4LeasedClientId_Object = MibTableColumn
sleV2Dhcp4LeasedClientId = _SleV2Dhcp4LeasedClientId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 1, 1, 6),
    _SleV2Dhcp4LeasedClientId_Type()
)
sleV2Dhcp4LeasedClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedClientId.setStatus("current")


class _SleV2Dhcp4LeasedRemoteId_Type(OctetString):
    """Custom type sleV2Dhcp4LeasedRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4LeasedRemoteId_Type.__name__ = "OctetString"
_SleV2Dhcp4LeasedRemoteId_Object = MibTableColumn
sleV2Dhcp4LeasedRemoteId = _SleV2Dhcp4LeasedRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 1, 1, 7),
    _SleV2Dhcp4LeasedRemoteId_Type()
)
sleV2Dhcp4LeasedRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedRemoteId.setStatus("current")


class _SleV2Dhcp4LeasedCircuitId_Type(OctetString):
    """Custom type sleV2Dhcp4LeasedCircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4LeasedCircuitId_Type.__name__ = "OctetString"
_SleV2Dhcp4LeasedCircuitId_Object = MibTableColumn
sleV2Dhcp4LeasedCircuitId = _SleV2Dhcp4LeasedCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 1, 1, 8),
    _SleV2Dhcp4LeasedCircuitId_Type()
)
sleV2Dhcp4LeasedCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedCircuitId.setStatus("current")
_SleV2Dhcp4LeasedStartTime_Type = Unsigned32
_SleV2Dhcp4LeasedStartTime_Object = MibTableColumn
sleV2Dhcp4LeasedStartTime = _SleV2Dhcp4LeasedStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 1, 1, 9),
    _SleV2Dhcp4LeasedStartTime_Type()
)
sleV2Dhcp4LeasedStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedStartTime.setStatus("current")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedStartTime.setUnits("second")
_SleV2Dhcp4LeasedFinishTime_Type = Unsigned32
_SleV2Dhcp4LeasedFinishTime_Object = MibTableColumn
sleV2Dhcp4LeasedFinishTime = _SleV2Dhcp4LeasedFinishTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 1, 1, 10),
    _SleV2Dhcp4LeasedFinishTime_Type()
)
sleV2Dhcp4LeasedFinishTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedFinishTime.setStatus("current")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedFinishTime.setUnits("second")
_SleV2Dhcp4LeasedControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4LeasedControl = _SleV2Dhcp4LeasedControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 2)
)


class _SleV2Dhcp4LeasedControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4LeasedControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clearDhcpLeasedAddress", 1),
          ("clearDhcpLeaseNetwork", 2),
          ("clearDhcpLeasePool", 3),
          ("clearDhcpLeaseAll", 4))
    )


_SleV2Dhcp4LeasedControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4LeasedControlRequest_Object = MibScalar
sleV2Dhcp4LeasedControlRequest = _SleV2Dhcp4LeasedControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 2, 1),
    _SleV2Dhcp4LeasedControlRequest_Type()
)
sleV2Dhcp4LeasedControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedControlRequest.setStatus("current")
_SleV2Dhcp4LeasedControlStatus_Type = SleControlStatusType
_SleV2Dhcp4LeasedControlStatus_Object = MibScalar
sleV2Dhcp4LeasedControlStatus = _SleV2Dhcp4LeasedControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 2, 2),
    _SleV2Dhcp4LeasedControlStatus_Type()
)
sleV2Dhcp4LeasedControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedControlStatus.setStatus("current")
_SleV2Dhcp4LeasedControlTimer_Type = Gauge32
_SleV2Dhcp4LeasedControlTimer_Object = MibScalar
sleV2Dhcp4LeasedControlTimer = _SleV2Dhcp4LeasedControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 2, 3),
    _SleV2Dhcp4LeasedControlTimer_Type()
)
sleV2Dhcp4LeasedControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedControlTimer.setStatus("current")
_SleV2Dhcp4LeasedControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4LeasedControlTimeStamp_Object = MibScalar
sleV2Dhcp4LeasedControlTimeStamp = _SleV2Dhcp4LeasedControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 2, 4),
    _SleV2Dhcp4LeasedControlTimeStamp_Type()
)
sleV2Dhcp4LeasedControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedControlTimeStamp.setStatus("current")
_SleV2Dhcp4LeasedControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4LeasedControlReqResult_Object = MibScalar
sleV2Dhcp4LeasedControlReqResult = _SleV2Dhcp4LeasedControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 2, 5),
    _SleV2Dhcp4LeasedControlReqResult_Type()
)
sleV2Dhcp4LeasedControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedControlReqResult.setStatus("current")
_SleV2Dhcp4LeasedControlAddress_Type = IpAddress
_SleV2Dhcp4LeasedControlAddress_Object = MibScalar
sleV2Dhcp4LeasedControlAddress = _SleV2Dhcp4LeasedControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 2, 6),
    _SleV2Dhcp4LeasedControlAddress_Type()
)
sleV2Dhcp4LeasedControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedControlAddress.setStatus("current")


class _SleV2Dhcp4LeasedControlMask_Type(Integer32):
    """Custom type sleV2Dhcp4LeasedControlMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleV2Dhcp4LeasedControlMask_Type.__name__ = "Integer32"
_SleV2Dhcp4LeasedControlMask_Object = MibScalar
sleV2Dhcp4LeasedControlMask = _SleV2Dhcp4LeasedControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 2, 7),
    _SleV2Dhcp4LeasedControlMask_Type()
)
sleV2Dhcp4LeasedControlMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedControlMask.setStatus("current")


class _SleV2Dhcp4LeasedControlPoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4LeasedControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4LeasedControlPoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4LeasedControlPoolIndex_Object = MibScalar
sleV2Dhcp4LeasedControlPoolIndex = _SleV2Dhcp4LeasedControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 2, 8),
    _SleV2Dhcp4LeasedControlPoolIndex_Type()
)
sleV2Dhcp4LeasedControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedControlPoolIndex.setStatus("current")
_SleV2Dhcp4LeasedNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4LeasedNotification = _SleV2Dhcp4LeasedNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 3)
)
_SleV2Dhcp4PacketStatsPort_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PacketStatsPort = _SleV2Dhcp4PacketStatsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 3)
)
_SleV2Dhcp4PacketStatsPortTable_Object = MibTable
sleV2Dhcp4PacketStatsPortTable = _SleV2Dhcp4PacketStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsPortTable.setStatus("current")
_SleV2Dhcp4PacketStatsPortEntry_Object = MibTableRow
sleV2Dhcp4PacketStatsPortEntry = _SleV2Dhcp4PacketStatsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 3, 1, 1)
)
sleV2Dhcp4PacketStatsPortEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsPortIndex"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsPortEntry.setStatus("current")
_SleV2Dhcp4PacketStatsPortIndex_Type = InterfaceIndex
_SleV2Dhcp4PacketStatsPortIndex_Object = MibTableColumn
sleV2Dhcp4PacketStatsPortIndex = _SleV2Dhcp4PacketStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 3, 1, 1, 1),
    _SleV2Dhcp4PacketStatsPortIndex_Type()
)
sleV2Dhcp4PacketStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsPortIndex.setStatus("current")
_SleV2Dhcp4PacketStatsPortReceived_Type = Counter32
_SleV2Dhcp4PacketStatsPortReceived_Object = MibTableColumn
sleV2Dhcp4PacketStatsPortReceived = _SleV2Dhcp4PacketStatsPortReceived_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 3, 1, 1, 2),
    _SleV2Dhcp4PacketStatsPortReceived_Type()
)
sleV2Dhcp4PacketStatsPortReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsPortReceived.setStatus("current")
_SleV2Dhcp4PacketStatsPortSent_Type = Counter32
_SleV2Dhcp4PacketStatsPortSent_Object = MibTableColumn
sleV2Dhcp4PacketStatsPortSent = _SleV2Dhcp4PacketStatsPortSent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 3, 1, 1, 3),
    _SleV2Dhcp4PacketStatsPortSent_Type()
)
sleV2Dhcp4PacketStatsPortSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsPortSent.setStatus("current")
_SleV2Dhcp4PacketStatsPortReceivedError_Type = Counter32
_SleV2Dhcp4PacketStatsPortReceivedError_Object = MibTableColumn
sleV2Dhcp4PacketStatsPortReceivedError = _SleV2Dhcp4PacketStatsPortReceivedError_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 3, 1, 1, 4),
    _SleV2Dhcp4PacketStatsPortReceivedError_Type()
)
sleV2Dhcp4PacketStatsPortReceivedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsPortReceivedError.setStatus("current")
_SleV2Dhcp4PacketStatsPortSentError_Type = Counter32
_SleV2Dhcp4PacketStatsPortSentError_Object = MibTableColumn
sleV2Dhcp4PacketStatsPortSentError = _SleV2Dhcp4PacketStatsPortSentError_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 3, 1, 1, 5),
    _SleV2Dhcp4PacketStatsPortSentError_Type()
)
sleV2Dhcp4PacketStatsPortSentError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsPortSentError.setStatus("current")
_SleV2Dhcp4PacketStatsPortReceivedDiscover_Type = Counter32
_SleV2Dhcp4PacketStatsPortReceivedDiscover_Object = MibTableColumn
sleV2Dhcp4PacketStatsPortReceivedDiscover = _SleV2Dhcp4PacketStatsPortReceivedDiscover_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 3, 1, 1, 6),
    _SleV2Dhcp4PacketStatsPortReceivedDiscover_Type()
)
sleV2Dhcp4PacketStatsPortReceivedDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsPortReceivedDiscover.setStatus("current")
_SleV2Dhcp4PacketStatsPortReceivedRequest_Type = Counter32
_SleV2Dhcp4PacketStatsPortReceivedRequest_Object = MibTableColumn
sleV2Dhcp4PacketStatsPortReceivedRequest = _SleV2Dhcp4PacketStatsPortReceivedRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 3, 1, 1, 7),
    _SleV2Dhcp4PacketStatsPortReceivedRequest_Type()
)
sleV2Dhcp4PacketStatsPortReceivedRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsPortReceivedRequest.setStatus("current")
_SleV2Dhcp4PacketStatsPortReceivedRelease_Type = Counter32
_SleV2Dhcp4PacketStatsPortReceivedRelease_Object = MibTableColumn
sleV2Dhcp4PacketStatsPortReceivedRelease = _SleV2Dhcp4PacketStatsPortReceivedRelease_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 3, 1, 1, 8),
    _SleV2Dhcp4PacketStatsPortReceivedRelease_Type()
)
sleV2Dhcp4PacketStatsPortReceivedRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsPortReceivedRelease.setStatus("current")
_SleV2Dhcp4PacketStatsPortReceivedInform_Type = Counter32
_SleV2Dhcp4PacketStatsPortReceivedInform_Object = MibTableColumn
sleV2Dhcp4PacketStatsPortReceivedInform = _SleV2Dhcp4PacketStatsPortReceivedInform_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 3, 1, 1, 9),
    _SleV2Dhcp4PacketStatsPortReceivedInform_Type()
)
sleV2Dhcp4PacketStatsPortReceivedInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsPortReceivedInform.setStatus("current")
_SleV2Dhcp4PacketStatsPortReceivedDecline_Type = Counter32
_SleV2Dhcp4PacketStatsPortReceivedDecline_Object = MibTableColumn
sleV2Dhcp4PacketStatsPortReceivedDecline = _SleV2Dhcp4PacketStatsPortReceivedDecline_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 3, 1, 1, 10),
    _SleV2Dhcp4PacketStatsPortReceivedDecline_Type()
)
sleV2Dhcp4PacketStatsPortReceivedDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsPortReceivedDecline.setStatus("current")
_SleV2Dhcp4PacketStatsPortSentOffer_Type = Counter32
_SleV2Dhcp4PacketStatsPortSentOffer_Object = MibTableColumn
sleV2Dhcp4PacketStatsPortSentOffer = _SleV2Dhcp4PacketStatsPortSentOffer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 3, 1, 1, 11),
    _SleV2Dhcp4PacketStatsPortSentOffer_Type()
)
sleV2Dhcp4PacketStatsPortSentOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsPortSentOffer.setStatus("current")
_SleV2Dhcp4PacketStatsPortSentAck_Type = Counter32
_SleV2Dhcp4PacketStatsPortSentAck_Object = MibTableColumn
sleV2Dhcp4PacketStatsPortSentAck = _SleV2Dhcp4PacketStatsPortSentAck_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 3, 1, 1, 12),
    _SleV2Dhcp4PacketStatsPortSentAck_Type()
)
sleV2Dhcp4PacketStatsPortSentAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsPortSentAck.setStatus("current")
_SleV2Dhcp4PacketStatsPortSentNak_Type = Counter32
_SleV2Dhcp4PacketStatsPortSentNak_Object = MibTableColumn
sleV2Dhcp4PacketStatsPortSentNak = _SleV2Dhcp4PacketStatsPortSentNak_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 3, 1, 1, 13),
    _SleV2Dhcp4PacketStatsPortSentNak_Type()
)
sleV2Dhcp4PacketStatsPortSentNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsPortSentNak.setStatus("current")
_SleV2Dhcp4State_ObjectIdentity = ObjectIdentity
sleV2Dhcp4State = _SleV2Dhcp4State_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4)
)
_SleV2Dhcp4StateTable_Object = MibTable
sleV2Dhcp4StateTable = _SleV2Dhcp4StateTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4StateTable.setStatus("current")
_SleV2Dhcp4StateEntry_Object = MibTableRow
sleV2Dhcp4StateEntry = _SleV2Dhcp4StateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 1, 1)
)
sleV2Dhcp4StateEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4StateIndex"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4StateEntry.setStatus("current")


class _SleV2Dhcp4StateIndex_Type(Integer32):
    """Custom type sleV2Dhcp4StateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bound", 1),
          ("offer", 2),
          ("abandon", 3),
          ("free", 4))
    )


_SleV2Dhcp4StateIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4StateIndex_Object = MibTableColumn
sleV2Dhcp4StateIndex = _SleV2Dhcp4StateIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 1, 1, 1),
    _SleV2Dhcp4StateIndex_Type()
)
sleV2Dhcp4StateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4StateIndex.setStatus("current")
_SleV2Dhcp4StateTotal_Type = Unsigned32
_SleV2Dhcp4StateTotal_Object = MibTableColumn
sleV2Dhcp4StateTotal = _SleV2Dhcp4StateTotal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 1, 1, 2),
    _SleV2Dhcp4StateTotal_Type()
)
sleV2Dhcp4StateTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4StateTotal.setStatus("current")
_SleV2Dhcp4StateFixed_Type = Unsigned32
_SleV2Dhcp4StateFixed_Object = MibTableColumn
sleV2Dhcp4StateFixed = _SleV2Dhcp4StateFixed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 1, 1, 3),
    _SleV2Dhcp4StateFixed_Type()
)
sleV2Dhcp4StateFixed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4StateFixed.setStatus("current")
_SleV2Dhcp4StateDynamic_Type = Unsigned32
_SleV2Dhcp4StateDynamic_Object = MibTableColumn
sleV2Dhcp4StateDynamic = _SleV2Dhcp4StateDynamic_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 1, 1, 4),
    _SleV2Dhcp4StateDynamic_Type()
)
sleV2Dhcp4StateDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4StateDynamic.setStatus("current")
_SleV2Dhcp4StatePEntry_Type = Unsigned32
_SleV2Dhcp4StatePEntry_Object = MibTableColumn
sleV2Dhcp4StatePEntry = _SleV2Dhcp4StatePEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 1, 1, 5),
    _SleV2Dhcp4StatePEntry_Type()
)
sleV2Dhcp4StatePEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4StatePEntry.setStatus("current")
_SleV2Dhcp4StatePoolTable_Object = MibTable
sleV2Dhcp4StatePoolTable = _SleV2Dhcp4StatePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 2)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4StatePoolTable.setStatus("current")
_SleV2Dhcp4StatePoolEntry_Object = MibTableRow
sleV2Dhcp4StatePoolEntry = _SleV2Dhcp4StatePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 2, 1)
)
sleV2Dhcp4StatePoolEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PoolIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4StateIndex"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4StatePoolEntry.setStatus("current")
_SleV2Dhcp4StatePoolTotal_Type = Unsigned32
_SleV2Dhcp4StatePoolTotal_Object = MibTableColumn
sleV2Dhcp4StatePoolTotal = _SleV2Dhcp4StatePoolTotal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 2, 1, 1),
    _SleV2Dhcp4StatePoolTotal_Type()
)
sleV2Dhcp4StatePoolTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4StatePoolTotal.setStatus("current")
_SleV2Dhcp4StatePoolFixed_Type = Unsigned32
_SleV2Dhcp4StatePoolFixed_Object = MibTableColumn
sleV2Dhcp4StatePoolFixed = _SleV2Dhcp4StatePoolFixed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 2, 1, 2),
    _SleV2Dhcp4StatePoolFixed_Type()
)
sleV2Dhcp4StatePoolFixed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4StatePoolFixed.setStatus("current")
_SleV2Dhcp4StatePoolDynamic_Type = Unsigned32
_SleV2Dhcp4StatePoolDynamic_Object = MibTableColumn
sleV2Dhcp4StatePoolDynamic = _SleV2Dhcp4StatePoolDynamic_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 2, 1, 3),
    _SleV2Dhcp4StatePoolDynamic_Type()
)
sleV2Dhcp4StatePoolDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4StatePoolDynamic.setStatus("current")
_SleV2Dhcp4StatePoolPEntry_Type = Unsigned32
_SleV2Dhcp4StatePoolPEntry_Object = MibTableColumn
sleV2Dhcp4StatePoolPEntry = _SleV2Dhcp4StatePoolPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 2, 1, 4),
    _SleV2Dhcp4StatePoolPEntry_Type()
)
sleV2Dhcp4StatePoolPEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4StatePoolPEntry.setStatus("current")
_SleV2Dhcp4StateBindTable_Object = MibTable
sleV2Dhcp4StateBindTable = _SleV2Dhcp4StateBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 3)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4StateBindTable.setStatus("current")
_SleV2Dhcp4StateBindEntry_Object = MibTableRow
sleV2Dhcp4StateBindEntry = _SleV2Dhcp4StateBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 3, 1)
)
sleV2Dhcp4StateBindEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4StateBindIpAddress"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4StateBindEntry.setStatus("current")
_SleV2Dhcp4StateBindIpAddress_Type = IpAddress
_SleV2Dhcp4StateBindIpAddress_Object = MibTableColumn
sleV2Dhcp4StateBindIpAddress = _SleV2Dhcp4StateBindIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 3, 1, 1),
    _SleV2Dhcp4StateBindIpAddress_Type()
)
sleV2Dhcp4StateBindIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4StateBindIpAddress.setStatus("current")
_SleV2Dhcp4StateBindPoolIndex_Type = Integer32
_SleV2Dhcp4StateBindPoolIndex_Object = MibTableColumn
sleV2Dhcp4StateBindPoolIndex = _SleV2Dhcp4StateBindPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 3, 1, 2),
    _SleV2Dhcp4StateBindPoolIndex_Type()
)
sleV2Dhcp4StateBindPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4StateBindPoolIndex.setStatus("current")
_SleV2Dhcp4StateBindMac_Type = MacAddress
_SleV2Dhcp4StateBindMac_Object = MibTableColumn
sleV2Dhcp4StateBindMac = _SleV2Dhcp4StateBindMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 3, 1, 3),
    _SleV2Dhcp4StateBindMac_Type()
)
sleV2Dhcp4StateBindMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4StateBindMac.setStatus("current")


class _SleV2Dhcp4StateBindState_Type(Integer32):
    """Custom type sleV2Dhcp4StateBindState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bound", 1),
          ("offer", 2),
          ("abandon", 3),
          ("free", 4))
    )


_SleV2Dhcp4StateBindState_Type.__name__ = "Integer32"
_SleV2Dhcp4StateBindState_Object = MibTableColumn
sleV2Dhcp4StateBindState = _SleV2Dhcp4StateBindState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 3, 1, 4),
    _SleV2Dhcp4StateBindState_Type()
)
sleV2Dhcp4StateBindState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4StateBindState.setStatus("current")


class _SleV2Dhcp4StateBindType_Type(Integer32):
    """Custom type sleV2Dhcp4StateBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("dynamic", 2),
          ("portentry", 3))
    )


_SleV2Dhcp4StateBindType_Type.__name__ = "Integer32"
_SleV2Dhcp4StateBindType_Object = MibTableColumn
sleV2Dhcp4StateBindType = _SleV2Dhcp4StateBindType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 3, 1, 5),
    _SleV2Dhcp4StateBindType_Type()
)
sleV2Dhcp4StateBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4StateBindType.setStatus("current")
_SleV2Dhcp4StateBindExpiration_Type = OctetString
_SleV2Dhcp4StateBindExpiration_Object = MibTableColumn
sleV2Dhcp4StateBindExpiration = _SleV2Dhcp4StateBindExpiration_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 3, 1, 6),
    _SleV2Dhcp4StateBindExpiration_Type()
)
sleV2Dhcp4StateBindExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4StateBindExpiration.setStatus("current")
_SleV2Dhcp4StateBindPort_Type = Integer32
_SleV2Dhcp4StateBindPort_Object = MibTableColumn
sleV2Dhcp4StateBindPort = _SleV2Dhcp4StateBindPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 4, 3, 1, 7),
    _SleV2Dhcp4StateBindPort_Type()
)
sleV2Dhcp4StateBindPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4StateBindPort.setStatus("current")
_SleV2Dhcp4Snooping_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Snooping = _SleV2Dhcp4Snooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6)
)
_SleV2Ds4Base_ObjectIdentity = ObjectIdentity
sleV2Ds4Base = _SleV2Ds4Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1)
)
_SleV2Ds4Info_ObjectIdentity = ObjectIdentity
sleV2Ds4Info = _SleV2Ds4Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 1)
)


class _SleV2Ds4Activity_Type(Integer32):
    """Custom type sleV2Ds4Activity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_SleV2Ds4Activity_Type.__name__ = "Integer32"
_SleV2Ds4Activity_Object = MibScalar
sleV2Ds4Activity = _SleV2Ds4Activity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 1, 1),
    _SleV2Ds4Activity_Type()
)
sleV2Ds4Activity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4Activity.setStatus("current")


class _SleV2Ds4VerifyMacState_Type(Integer32):
    """Custom type sleV2Ds4VerifyMacState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Ds4VerifyMacState_Type.__name__ = "Integer32"
_SleV2Ds4VerifyMacState_Object = MibScalar
sleV2Ds4VerifyMacState = _SleV2Ds4VerifyMacState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 1, 2),
    _SleV2Ds4VerifyMacState_Type()
)
sleV2Ds4VerifyMacState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4VerifyMacState.setStatus("current")
_SleV2Ds4DatabaseURL_Type = IpAddress
_SleV2Ds4DatabaseURL_Object = MibScalar
sleV2Ds4DatabaseURL = _SleV2Ds4DatabaseURL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 1, 3),
    _SleV2Ds4DatabaseURL_Type()
)
sleV2Ds4DatabaseURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4DatabaseURL.setStatus("current")


class _SleV2Ds4DatabaseInterval_Type(Integer32):
    """Custom type sleV2Ds4DatabaseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Ds4DatabaseInterval_Type.__name__ = "Integer32"
_SleV2Ds4DatabaseInterval_Object = MibScalar
sleV2Ds4DatabaseInterval = _SleV2Ds4DatabaseInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 1, 4),
    _SleV2Ds4DatabaseInterval_Type()
)
sleV2Ds4DatabaseInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4DatabaseInterval.setStatus("current")


class _SleV2Ds4ArpInspectionTime_Type(Integer32):
    """Custom type sleV2Ds4ArpInspectionTime based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483637),
    )


_SleV2Ds4ArpInspectionTime_Type.__name__ = "Integer32"
_SleV2Ds4ArpInspectionTime_Object = MibScalar
sleV2Ds4ArpInspectionTime = _SleV2Ds4ArpInspectionTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 1, 5),
    _SleV2Ds4ArpInspectionTime_Type()
)
sleV2Ds4ArpInspectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4ArpInspectionTime.setStatus("current")
if mibBuilder.loadTexts:
    sleV2Ds4ArpInspectionTime.setUnits("sec")


class _SleV2Ds4LimitRateDiscover_Type(Integer32):
    """Custom type sleV2Ds4LimitRateDiscover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32767),
    )


_SleV2Ds4LimitRateDiscover_Type.__name__ = "Integer32"
_SleV2Ds4LimitRateDiscover_Object = MibScalar
sleV2Ds4LimitRateDiscover = _SleV2Ds4LimitRateDiscover_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 1, 6),
    _SleV2Ds4LimitRateDiscover_Type()
)
sleV2Ds4LimitRateDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4LimitRateDiscover.setStatus("current")


class _SleV2Ds4LimitRateRequest_Type(Integer32):
    """Custom type sleV2Ds4LimitRateRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32767),
    )


_SleV2Ds4LimitRateRequest_Type.__name__ = "Integer32"
_SleV2Ds4LimitRateRequest_Object = MibScalar
sleV2Ds4LimitRateRequest = _SleV2Ds4LimitRateRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 1, 7),
    _SleV2Ds4LimitRateRequest_Type()
)
sleV2Ds4LimitRateRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4LimitRateRequest.setStatus("current")


class _SleV2Ds4InformationOption_Type(Integer32):
    """Custom type sleV2Ds4InformationOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Ds4InformationOption_Type.__name__ = "Integer32"
_SleV2Ds4InformationOption_Object = MibScalar
sleV2Ds4InformationOption = _SleV2Ds4InformationOption_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 1, 8),
    _SleV2Ds4InformationOption_Type()
)
sleV2Ds4InformationOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4InformationOption.setStatus("current")
_SleV2Ds4Control_ObjectIdentity = ObjectIdentity
sleV2Ds4Control = _SleV2Ds4Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 2)
)


class _SleV2Ds4ControlRequest_Type(Integer32):
    """Custom type sleV2Ds4ControlRequest based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("setDsActivity", 1),
          ("setDsVerifyMacState", 2),
          ("setDsDatabaseProfile", 3),
          ("renewDsDatabase", 4),
          ("setDsArpInspectionTime", 5),
          ("setDsLimitRateDiscover", 6),
          ("setDsLimitRateRequest", 7),
          ("setDsInformationOption", 8))
    )


_SleV2Ds4ControlRequest_Type.__name__ = "Integer32"
_SleV2Ds4ControlRequest_Object = MibScalar
sleV2Ds4ControlRequest = _SleV2Ds4ControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 2, 1),
    _SleV2Ds4ControlRequest_Type()
)
sleV2Ds4ControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4ControlRequest.setStatus("current")
_SleV2Ds4ControlStatus_Type = SleControlStatusType
_SleV2Ds4ControlStatus_Object = MibScalar
sleV2Ds4ControlStatus = _SleV2Ds4ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 2, 2),
    _SleV2Ds4ControlStatus_Type()
)
sleV2Ds4ControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4ControlStatus.setStatus("current")
_SleV2Ds4ControlTimer_Type = Gauge32
_SleV2Ds4ControlTimer_Object = MibScalar
sleV2Ds4ControlTimer = _SleV2Ds4ControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 2, 3),
    _SleV2Ds4ControlTimer_Type()
)
sleV2Ds4ControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4ControlTimer.setStatus("current")
_SleV2Ds4ControlTimeStamp_Type = TimeTicks
_SleV2Ds4ControlTimeStamp_Object = MibScalar
sleV2Ds4ControlTimeStamp = _SleV2Ds4ControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 2, 4),
    _SleV2Ds4ControlTimeStamp_Type()
)
sleV2Ds4ControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4ControlTimeStamp.setStatus("current")
_SleV2Ds4ControlReqResult_Type = SleControlRequestResultType
_SleV2Ds4ControlReqResult_Object = MibScalar
sleV2Ds4ControlReqResult = _SleV2Ds4ControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 2, 5),
    _SleV2Ds4ControlReqResult_Type()
)
sleV2Ds4ControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4ControlReqResult.setStatus("current")


class _SleV2Ds4ControlActivity_Type(Integer32):
    """Custom type sleV2Ds4ControlActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_SleV2Ds4ControlActivity_Type.__name__ = "Integer32"
_SleV2Ds4ControlActivity_Object = MibScalar
sleV2Ds4ControlActivity = _SleV2Ds4ControlActivity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 2, 6),
    _SleV2Ds4ControlActivity_Type()
)
sleV2Ds4ControlActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4ControlActivity.setStatus("current")


class _SleV2Ds4ControlVerifyMacState_Type(Integer32):
    """Custom type sleV2Ds4ControlVerifyMacState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Ds4ControlVerifyMacState_Type.__name__ = "Integer32"
_SleV2Ds4ControlVerifyMacState_Object = MibScalar
sleV2Ds4ControlVerifyMacState = _SleV2Ds4ControlVerifyMacState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 2, 7),
    _SleV2Ds4ControlVerifyMacState_Type()
)
sleV2Ds4ControlVerifyMacState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4ControlVerifyMacState.setStatus("current")
_SleV2Ds4ControlDatabaseURL_Type = IpAddress
_SleV2Ds4ControlDatabaseURL_Object = MibScalar
sleV2Ds4ControlDatabaseURL = _SleV2Ds4ControlDatabaseURL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 2, 8),
    _SleV2Ds4ControlDatabaseURL_Type()
)
sleV2Ds4ControlDatabaseURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4ControlDatabaseURL.setStatus("current")


class _SleV2Ds4ControlDatabaseInterval_Type(Integer32):
    """Custom type sleV2Ds4ControlDatabaseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Ds4ControlDatabaseInterval_Type.__name__ = "Integer32"
_SleV2Ds4ControlDatabaseInterval_Object = MibScalar
sleV2Ds4ControlDatabaseInterval = _SleV2Ds4ControlDatabaseInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 2, 9),
    _SleV2Ds4ControlDatabaseInterval_Type()
)
sleV2Ds4ControlDatabaseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4ControlDatabaseInterval.setStatus("current")


class _SleV2Ds4ControlArpInspectionTime_Type(Integer32):
    """Custom type sleV2Ds4ControlArpInspectionTime based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483637),
    )


_SleV2Ds4ControlArpInspectionTime_Type.__name__ = "Integer32"
_SleV2Ds4ControlArpInspectionTime_Object = MibScalar
sleV2Ds4ControlArpInspectionTime = _SleV2Ds4ControlArpInspectionTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 2, 10),
    _SleV2Ds4ControlArpInspectionTime_Type()
)
sleV2Ds4ControlArpInspectionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4ControlArpInspectionTime.setStatus("current")
if mibBuilder.loadTexts:
    sleV2Ds4ControlArpInspectionTime.setUnits("sec")


class _SleV2Ds4ControlLimitRateDiscover_Type(Integer32):
    """Custom type sleV2Ds4ControlLimitRateDiscover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32767),
    )


_SleV2Ds4ControlLimitRateDiscover_Type.__name__ = "Integer32"
_SleV2Ds4ControlLimitRateDiscover_Object = MibScalar
sleV2Ds4ControlLimitRateDiscover = _SleV2Ds4ControlLimitRateDiscover_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 2, 11),
    _SleV2Ds4ControlLimitRateDiscover_Type()
)
sleV2Ds4ControlLimitRateDiscover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4ControlLimitRateDiscover.setStatus("current")


class _SleV2Ds4ControlLimitRateRequest_Type(Integer32):
    """Custom type sleV2Ds4ControlLimitRateRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32767),
    )


_SleV2Ds4ControlLimitRateRequest_Type.__name__ = "Integer32"
_SleV2Ds4ControlLimitRateRequest_Object = MibScalar
sleV2Ds4ControlLimitRateRequest = _SleV2Ds4ControlLimitRateRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 2, 12),
    _SleV2Ds4ControlLimitRateRequest_Type()
)
sleV2Ds4ControlLimitRateRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4ControlLimitRateRequest.setStatus("current")


class _SleV2Ds4ControlInformationOption_Type(Integer32):
    """Custom type sleV2Ds4ControlInformationOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Ds4ControlInformationOption_Type.__name__ = "Integer32"
_SleV2Ds4ControlInformationOption_Object = MibScalar
sleV2Ds4ControlInformationOption = _SleV2Ds4ControlInformationOption_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 2, 13),
    _SleV2Ds4ControlInformationOption_Type()
)
sleV2Ds4ControlInformationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4ControlInformationOption.setStatus("current")
_SleV2Ds4Notification_ObjectIdentity = ObjectIdentity
sleV2Ds4Notification = _SleV2Ds4Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 3)
)
_SleV2Ds4Vlan_ObjectIdentity = ObjectIdentity
sleV2Ds4Vlan = _SleV2Ds4Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 2)
)
_SleV2Ds4VlanTable_Object = MibTable
sleV2Ds4VlanTable = _SleV2Ds4VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2Ds4VlanTable.setStatus("current")
_SleV2Ds4VlanEntry_Object = MibTableRow
sleV2Ds4VlanEntry = _SleV2Ds4VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 2, 1, 1)
)
sleV2Ds4VlanEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Ds4VlanIndex"),
)
if mibBuilder.loadTexts:
    sleV2Ds4VlanEntry.setStatus("current")


class _SleV2Ds4VlanIndex_Type(Integer32):
    """Custom type sleV2Ds4VlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleV2Ds4VlanIndex_Type.__name__ = "Integer32"
_SleV2Ds4VlanIndex_Object = MibTableColumn
sleV2Ds4VlanIndex = _SleV2Ds4VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 2, 1, 1, 1),
    _SleV2Ds4VlanIndex_Type()
)
sleV2Ds4VlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4VlanIndex.setStatus("current")


class _SleV2Ds4VlanState_Type(Integer32):
    """Custom type sleV2Ds4VlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Ds4VlanState_Type.__name__ = "Integer32"
_SleV2Ds4VlanState_Object = MibTableColumn
sleV2Ds4VlanState = _SleV2Ds4VlanState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 2, 1, 1, 2),
    _SleV2Ds4VlanState_Type()
)
sleV2Ds4VlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4VlanState.setStatus("current")
_SleV2Ds4VlanControl_ObjectIdentity = ObjectIdentity
sleV2Ds4VlanControl = _SleV2Ds4VlanControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 2, 2)
)


class _SleV2Ds4VlanControlRequest_Type(Integer32):
    """Custom type sleV2Ds4VlanControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setDsVlanState", 1)
    )


_SleV2Ds4VlanControlRequest_Type.__name__ = "Integer32"
_SleV2Ds4VlanControlRequest_Object = MibScalar
sleV2Ds4VlanControlRequest = _SleV2Ds4VlanControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 2, 2, 1),
    _SleV2Ds4VlanControlRequest_Type()
)
sleV2Ds4VlanControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4VlanControlRequest.setStatus("current")
_SleV2Ds4VlanControlStatus_Type = SleControlStatusType
_SleV2Ds4VlanControlStatus_Object = MibScalar
sleV2Ds4VlanControlStatus = _SleV2Ds4VlanControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 2, 2, 2),
    _SleV2Ds4VlanControlStatus_Type()
)
sleV2Ds4VlanControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4VlanControlStatus.setStatus("current")
_SleV2Ds4VlanControlTimer_Type = Gauge32
_SleV2Ds4VlanControlTimer_Object = MibScalar
sleV2Ds4VlanControlTimer = _SleV2Ds4VlanControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 2, 2, 3),
    _SleV2Ds4VlanControlTimer_Type()
)
sleV2Ds4VlanControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4VlanControlTimer.setStatus("current")
_SleV2Ds4VlanControlTimeStamp_Type = TimeTicks
_SleV2Ds4VlanControlTimeStamp_Object = MibScalar
sleV2Ds4VlanControlTimeStamp = _SleV2Ds4VlanControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 2, 2, 4),
    _SleV2Ds4VlanControlTimeStamp_Type()
)
sleV2Ds4VlanControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4VlanControlTimeStamp.setStatus("current")
_SleV2Ds4VlanControlReqResult_Type = SleControlRequestResultType
_SleV2Ds4VlanControlReqResult_Object = MibScalar
sleV2Ds4VlanControlReqResult = _SleV2Ds4VlanControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 2, 2, 5),
    _SleV2Ds4VlanControlReqResult_Type()
)
sleV2Ds4VlanControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4VlanControlReqResult.setStatus("current")


class _SleV2Ds4VlanControlIndex_Type(Integer32):
    """Custom type sleV2Ds4VlanControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleV2Ds4VlanControlIndex_Type.__name__ = "Integer32"
_SleV2Ds4VlanControlIndex_Object = MibScalar
sleV2Ds4VlanControlIndex = _SleV2Ds4VlanControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 2, 2, 6),
    _SleV2Ds4VlanControlIndex_Type()
)
sleV2Ds4VlanControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4VlanControlIndex.setStatus("current")


class _SleV2Ds4VlanControlState_Type(Integer32):
    """Custom type sleV2Ds4VlanControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Ds4VlanControlState_Type.__name__ = "Integer32"
_SleV2Ds4VlanControlState_Object = MibScalar
sleV2Ds4VlanControlState = _SleV2Ds4VlanControlState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 2, 2, 7),
    _SleV2Ds4VlanControlState_Type()
)
sleV2Ds4VlanControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4VlanControlState.setStatus("current")
_SleV2Ds4VlanNotification_ObjectIdentity = ObjectIdentity
sleV2Ds4VlanNotification = _SleV2Ds4VlanNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 2, 3)
)
_SleV2Ds4Port_ObjectIdentity = ObjectIdentity
sleV2Ds4Port = _SleV2Ds4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3)
)
_SleV2Ds4PortTable_Object = MibTable
sleV2Ds4PortTable = _SleV2Ds4PortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    sleV2Ds4PortTable.setStatus("current")
_SleV2Ds4PortEntry_Object = MibTableRow
sleV2Ds4PortEntry = _SleV2Ds4PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 1, 1)
)
sleV2Ds4PortEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Ds4PortIndex"),
)
if mibBuilder.loadTexts:
    sleV2Ds4PortEntry.setStatus("current")


class _SleV2Ds4PortIndex_Type(Integer32):
    """Custom type sleV2Ds4PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Ds4PortIndex_Type.__name__ = "Integer32"
_SleV2Ds4PortIndex_Object = MibTableColumn
sleV2Ds4PortIndex = _SleV2Ds4PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 1, 1, 1),
    _SleV2Ds4PortIndex_Type()
)
sleV2Ds4PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4PortIndex.setStatus("current")


class _SleV2Ds4PortTrustState_Type(Integer32):
    """Custom type sleV2Ds4PortTrustState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Ds4PortTrustState_Type.__name__ = "Integer32"
_SleV2Ds4PortTrustState_Object = MibTableColumn
sleV2Ds4PortTrustState = _SleV2Ds4PortTrustState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 1, 1, 2),
    _SleV2Ds4PortTrustState_Type()
)
sleV2Ds4PortTrustState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4PortTrustState.setStatus("current")


class _SleV2Ds4PortLimitRate_Type(Integer32):
    """Custom type sleV2Ds4PortLimitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_SleV2Ds4PortLimitRate_Type.__name__ = "Integer32"
_SleV2Ds4PortLimitRate_Object = MibTableColumn
sleV2Ds4PortLimitRate = _SleV2Ds4PortLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 1, 1, 3),
    _SleV2Ds4PortLimitRate_Type()
)
sleV2Ds4PortLimitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4PortLimitRate.setStatus("current")


class _SleV2Ds4PortLimitLease_Type(Integer32):
    """Custom type sleV2Ds4PortLimitLease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Ds4PortLimitLease_Type.__name__ = "Integer32"
_SleV2Ds4PortLimitLease_Object = MibTableColumn
sleV2Ds4PortLimitLease = _SleV2Ds4PortLimitLease_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 1, 1, 4),
    _SleV2Ds4PortLimitLease_Type()
)
sleV2Ds4PortLimitLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4PortLimitLease.setStatus("current")


class _SleV2Ds4PortSrcGuardState_Type(Integer32):
    """Custom type sleV2Ds4PortSrcGuardState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("ipEnable", 1),
          ("ipMacEnable", 2))
    )


_SleV2Ds4PortSrcGuardState_Type.__name__ = "Integer32"
_SleV2Ds4PortSrcGuardState_Object = MibTableColumn
sleV2Ds4PortSrcGuardState = _SleV2Ds4PortSrcGuardState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 1, 1, 5),
    _SleV2Ds4PortSrcGuardState_Type()
)
sleV2Ds4PortSrcGuardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4PortSrcGuardState.setStatus("current")


class _SleV2Ds4PortTimeout_Type(Integer32):
    """Custom type sleV2Ds4PortTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483637),
    )


_SleV2Ds4PortTimeout_Type.__name__ = "Integer32"
_SleV2Ds4PortTimeout_Object = MibTableColumn
sleV2Ds4PortTimeout = _SleV2Ds4PortTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 1, 1, 6),
    _SleV2Ds4PortTimeout_Type()
)
sleV2Ds4PortTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4PortTimeout.setStatus("current")


class _SleV2Ds4PortStatus_Type(Integer32):
    """Custom type sleV2Ds4PortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("diable", 2))
    )


_SleV2Ds4PortStatus_Type.__name__ = "Integer32"
_SleV2Ds4PortStatus_Object = MibTableColumn
sleV2Ds4PortStatus = _SleV2Ds4PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 1, 1, 7),
    _SleV2Ds4PortStatus_Type()
)
sleV2Ds4PortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4PortStatus.setStatus("current")


class _SleV2Ds4PortFilterMode_Type(Integer32):
    """Custom type sleV2Ds4PortFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("permit", 1),
          ("bypass", 2),
          ("filter", 3))
    )


_SleV2Ds4PortFilterMode_Type.__name__ = "Integer32"
_SleV2Ds4PortFilterMode_Object = MibTableColumn
sleV2Ds4PortFilterMode = _SleV2Ds4PortFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 1, 1, 8),
    _SleV2Ds4PortFilterMode_Type()
)
sleV2Ds4PortFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4PortFilterMode.setStatus("current")


class _SleV2Ds4PortFilterDelayTimer_Type(Integer32):
    """Custom type sleV2Ds4PortFilterDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Ds4PortFilterDelayTimer_Type.__name__ = "Integer32"
_SleV2Ds4PortFilterDelayTimer_Object = MibTableColumn
sleV2Ds4PortFilterDelayTimer = _SleV2Ds4PortFilterDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 1, 1, 9),
    _SleV2Ds4PortFilterDelayTimer_Type()
)
sleV2Ds4PortFilterDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4PortFilterDelayTimer.setStatus("current")


class _SleV2Ds4PortFilterDelayCounter_Type(Integer32):
    """Custom type sleV2Ds4PortFilterDelayCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Ds4PortFilterDelayCounter_Type.__name__ = "Integer32"
_SleV2Ds4PortFilterDelayCounter_Object = MibTableColumn
sleV2Ds4PortFilterDelayCounter = _SleV2Ds4PortFilterDelayCounter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 1, 1, 10),
    _SleV2Ds4PortFilterDelayCounter_Type()
)
sleV2Ds4PortFilterDelayCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4PortFilterDelayCounter.setStatus("current")


class _SleV2Ds4PortTrustFilterEgressBcastReqState_Type(Integer32):
    """Custom type sleV2Ds4PortTrustFilterEgressBcastReqState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Ds4PortTrustFilterEgressBcastReqState_Type.__name__ = "Integer32"
_SleV2Ds4PortTrustFilterEgressBcastReqState_Object = MibTableColumn
sleV2Ds4PortTrustFilterEgressBcastReqState = _SleV2Ds4PortTrustFilterEgressBcastReqState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 1, 1, 11),
    _SleV2Ds4PortTrustFilterEgressBcastReqState_Type()
)
sleV2Ds4PortTrustFilterEgressBcastReqState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4PortTrustFilterEgressBcastReqState.setStatus("current")
_SleV2Ds4PortControl_ObjectIdentity = ObjectIdentity
sleV2Ds4PortControl = _SleV2Ds4PortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2)
)


class _SleV2Ds4PortControlRequest_Type(Integer32):
    """Custom type sleV2Ds4PortControlRequest based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("setDsPortTrustState", 1),
          ("setDsPortLimitProfile", 2),
          ("setDsPortSrcGuardState", 3),
          ("setDsPortTimeout", 4),
          ("setDsPortStatus", 5),
          ("setDsPortFilterMode", 6),
          ("setDsPortFilterDelay", 7),
          ("setDsPortTrustFilterEgressBcastReqState", 8))
    )


_SleV2Ds4PortControlRequest_Type.__name__ = "Integer32"
_SleV2Ds4PortControlRequest_Object = MibScalar
sleV2Ds4PortControlRequest = _SleV2Ds4PortControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2, 1),
    _SleV2Ds4PortControlRequest_Type()
)
sleV2Ds4PortControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4PortControlRequest.setStatus("current")
_SleV2Ds4PortControlStatus_Type = SleControlStatusType
_SleV2Ds4PortControlStatus_Object = MibScalar
sleV2Ds4PortControlStatus = _SleV2Ds4PortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2, 2),
    _SleV2Ds4PortControlStatus_Type()
)
sleV2Ds4PortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4PortControlStatus.setStatus("current")
_SleV2Ds4PortControlTimer_Type = Gauge32
_SleV2Ds4PortControlTimer_Object = MibScalar
sleV2Ds4PortControlTimer = _SleV2Ds4PortControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2, 3),
    _SleV2Ds4PortControlTimer_Type()
)
sleV2Ds4PortControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4PortControlTimer.setStatus("current")
_SleV2Ds4PortControlTimeStamp_Type = TimeTicks
_SleV2Ds4PortControlTimeStamp_Object = MibScalar
sleV2Ds4PortControlTimeStamp = _SleV2Ds4PortControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2, 4),
    _SleV2Ds4PortControlTimeStamp_Type()
)
sleV2Ds4PortControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4PortControlTimeStamp.setStatus("current")
_SleV2Ds4PortControlReqResult_Type = SleControlRequestResultType
_SleV2Ds4PortControlReqResult_Object = MibScalar
sleV2Ds4PortControlReqResult = _SleV2Ds4PortControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2, 5),
    _SleV2Ds4PortControlReqResult_Type()
)
sleV2Ds4PortControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4PortControlReqResult.setStatus("current")


class _SleV2Ds4PortControlIndex_Type(Integer32):
    """Custom type sleV2Ds4PortControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Ds4PortControlIndex_Type.__name__ = "Integer32"
_SleV2Ds4PortControlIndex_Object = MibScalar
sleV2Ds4PortControlIndex = _SleV2Ds4PortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2, 6),
    _SleV2Ds4PortControlIndex_Type()
)
sleV2Ds4PortControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4PortControlIndex.setStatus("current")


class _SleV2Ds4PortControlTrustState_Type(Integer32):
    """Custom type sleV2Ds4PortControlTrustState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Ds4PortControlTrustState_Type.__name__ = "Integer32"
_SleV2Ds4PortControlTrustState_Object = MibScalar
sleV2Ds4PortControlTrustState = _SleV2Ds4PortControlTrustState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2, 7),
    _SleV2Ds4PortControlTrustState_Type()
)
sleV2Ds4PortControlTrustState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4PortControlTrustState.setStatus("current")


class _SleV2Ds4PortControlLimitRate_Type(Integer32):
    """Custom type sleV2Ds4PortControlLimitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_SleV2Ds4PortControlLimitRate_Type.__name__ = "Integer32"
_SleV2Ds4PortControlLimitRate_Object = MibScalar
sleV2Ds4PortControlLimitRate = _SleV2Ds4PortControlLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2, 8),
    _SleV2Ds4PortControlLimitRate_Type()
)
sleV2Ds4PortControlLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4PortControlLimitRate.setStatus("current")


class _SleV2Ds4PortControlLimitLease_Type(Integer32):
    """Custom type sleV2Ds4PortControlLimitLease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Ds4PortControlLimitLease_Type.__name__ = "Integer32"
_SleV2Ds4PortControlLimitLease_Object = MibScalar
sleV2Ds4PortControlLimitLease = _SleV2Ds4PortControlLimitLease_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2, 9),
    _SleV2Ds4PortControlLimitLease_Type()
)
sleV2Ds4PortControlLimitLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4PortControlLimitLease.setStatus("current")


class _SleV2Ds4PortControlSrcGuardState_Type(Integer32):
    """Custom type sleV2Ds4PortControlSrcGuardState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("ipEnable", 1),
          ("ipMacEnable", 2))
    )


_SleV2Ds4PortControlSrcGuardState_Type.__name__ = "Integer32"
_SleV2Ds4PortControlSrcGuardState_Object = MibScalar
sleV2Ds4PortControlSrcGuardState = _SleV2Ds4PortControlSrcGuardState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2, 10),
    _SleV2Ds4PortControlSrcGuardState_Type()
)
sleV2Ds4PortControlSrcGuardState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4PortControlSrcGuardState.setStatus("current")


class _SleV2Ds4PortControlTimeout_Type(Integer32):
    """Custom type sleV2Ds4PortControlTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483637),
    )


_SleV2Ds4PortControlTimeout_Type.__name__ = "Integer32"
_SleV2Ds4PortControlTimeout_Object = MibScalar
sleV2Ds4PortControlTimeout = _SleV2Ds4PortControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2, 11),
    _SleV2Ds4PortControlTimeout_Type()
)
sleV2Ds4PortControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4PortControlTimeout.setStatus("current")


class _SleV2Ds4PortControlPStatus_Type(Integer32):
    """Custom type sleV2Ds4PortControlPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleV2Ds4PortControlPStatus_Type.__name__ = "Integer32"
_SleV2Ds4PortControlPStatus_Object = MibScalar
sleV2Ds4PortControlPStatus = _SleV2Ds4PortControlPStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2, 12),
    _SleV2Ds4PortControlPStatus_Type()
)
sleV2Ds4PortControlPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4PortControlPStatus.setStatus("current")


class _SleV2Ds4PortControlFilterMode_Type(Integer32):
    """Custom type sleV2Ds4PortControlFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("permit", 1),
          ("bypass", 2),
          ("filter", 3))
    )


_SleV2Ds4PortControlFilterMode_Type.__name__ = "Integer32"
_SleV2Ds4PortControlFilterMode_Object = MibScalar
sleV2Ds4PortControlFilterMode = _SleV2Ds4PortControlFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2, 13),
    _SleV2Ds4PortControlFilterMode_Type()
)
sleV2Ds4PortControlFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4PortControlFilterMode.setStatus("current")


class _SleV2Ds4PortControlFilterDelayTimer_Type(Integer32):
    """Custom type sleV2Ds4PortControlFilterDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Ds4PortControlFilterDelayTimer_Type.__name__ = "Integer32"
_SleV2Ds4PortControlFilterDelayTimer_Object = MibScalar
sleV2Ds4PortControlFilterDelayTimer = _SleV2Ds4PortControlFilterDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2, 14),
    _SleV2Ds4PortControlFilterDelayTimer_Type()
)
sleV2Ds4PortControlFilterDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4PortControlFilterDelayTimer.setStatus("current")


class _SleV2Ds4PortControlFilterDelayCounter_Type(Integer32):
    """Custom type sleV2Ds4PortControlFilterDelayCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Ds4PortControlFilterDelayCounter_Type.__name__ = "Integer32"
_SleV2Ds4PortControlFilterDelayCounter_Object = MibScalar
sleV2Ds4PortControlFilterDelayCounter = _SleV2Ds4PortControlFilterDelayCounter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2, 15),
    _SleV2Ds4PortControlFilterDelayCounter_Type()
)
sleV2Ds4PortControlFilterDelayCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4PortControlFilterDelayCounter.setStatus("current")


class _SleV2Ds4PortControlTrustFilterEgressBcastReqState_Type(Integer32):
    """Custom type sleV2Ds4PortControlTrustFilterEgressBcastReqState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Ds4PortControlTrustFilterEgressBcastReqState_Type.__name__ = "Integer32"
_SleV2Ds4PortControlTrustFilterEgressBcastReqState_Object = MibScalar
sleV2Ds4PortControlTrustFilterEgressBcastReqState = _SleV2Ds4PortControlTrustFilterEgressBcastReqState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 2, 16),
    _SleV2Ds4PortControlTrustFilterEgressBcastReqState_Type()
)
sleV2Ds4PortControlTrustFilterEgressBcastReqState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4PortControlTrustFilterEgressBcastReqState.setStatus("current")
_SleV2Ds4PortNotification_ObjectIdentity = ObjectIdentity
sleV2Ds4PortNotification = _SleV2Ds4PortNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 3)
)
_SleV2Ds4Bindings_ObjectIdentity = ObjectIdentity
sleV2Ds4Bindings = _SleV2Ds4Bindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4)
)
_SleV2Ds4BindingsTable_Object = MibTable
sleV2Ds4BindingsTable = _SleV2Ds4BindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 1)
)
if mibBuilder.loadTexts:
    sleV2Ds4BindingsTable.setStatus("current")
_SleV2Ds4BindingsEntry_Object = MibTableRow
sleV2Ds4BindingsEntry = _SleV2Ds4BindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 1, 1)
)
sleV2Ds4BindingsEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Ds4BindingsPortIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Ds4BindingsAddress"),
)
if mibBuilder.loadTexts:
    sleV2Ds4BindingsEntry.setStatus("current")


class _SleV2Ds4BindingsVlanIndex_Type(Integer32):
    """Custom type sleV2Ds4BindingsVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleV2Ds4BindingsVlanIndex_Type.__name__ = "Integer32"
_SleV2Ds4BindingsVlanIndex_Object = MibTableColumn
sleV2Ds4BindingsVlanIndex = _SleV2Ds4BindingsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 1, 1, 1),
    _SleV2Ds4BindingsVlanIndex_Type()
)
sleV2Ds4BindingsVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsVlanIndex.setStatus("current")


class _SleV2Ds4BindingsPortIndex_Type(Integer32):
    """Custom type sleV2Ds4BindingsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Ds4BindingsPortIndex_Type.__name__ = "Integer32"
_SleV2Ds4BindingsPortIndex_Object = MibTableColumn
sleV2Ds4BindingsPortIndex = _SleV2Ds4BindingsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 1, 1, 2),
    _SleV2Ds4BindingsPortIndex_Type()
)
sleV2Ds4BindingsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsPortIndex.setStatus("current")
_SleV2Ds4BindingsAddress_Type = IpAddress
_SleV2Ds4BindingsAddress_Object = MibTableColumn
sleV2Ds4BindingsAddress = _SleV2Ds4BindingsAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 1, 1, 3),
    _SleV2Ds4BindingsAddress_Type()
)
sleV2Ds4BindingsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsAddress.setStatus("current")
_SleV2Ds4BindingsMac_Type = MacAddress
_SleV2Ds4BindingsMac_Object = MibTableColumn
sleV2Ds4BindingsMac = _SleV2Ds4BindingsMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 1, 1, 4),
    _SleV2Ds4BindingsMac_Type()
)
sleV2Ds4BindingsMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsMac.setStatus("current")


class _SleV2Ds4BindingsType_Type(Bits):
    """Custom type sleV2Ds4BindingsType based on Bits"""
    namedValues = NamedValues(
        *(("dhcpDynamic", 0),
          ("srcGuardStatic", 1))
    )

_SleV2Ds4BindingsType_Type.__name__ = "Bits"
_SleV2Ds4BindingsType_Object = MibTableColumn
sleV2Ds4BindingsType = _SleV2Ds4BindingsType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 1, 1, 5),
    _SleV2Ds4BindingsType_Type()
)
sleV2Ds4BindingsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsType.setStatus("current")


class _SleV2Ds4BindingsState_Type(Integer32):
    """Custom type sleV2Ds4BindingsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Ds4BindingsState_Type.__name__ = "Integer32"
_SleV2Ds4BindingsState_Object = MibTableColumn
sleV2Ds4BindingsState = _SleV2Ds4BindingsState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 1, 1, 6),
    _SleV2Ds4BindingsState_Type()
)
sleV2Ds4BindingsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsState.setStatus("current")


class _SleV2Ds4BindingsLeasedTime_Type(Integer32):
    """Custom type sleV2Ds4BindingsLeasedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Ds4BindingsLeasedTime_Type.__name__ = "Integer32"
_SleV2Ds4BindingsLeasedTime_Object = MibTableColumn
sleV2Ds4BindingsLeasedTime = _SleV2Ds4BindingsLeasedTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 1, 1, 7),
    _SleV2Ds4BindingsLeasedTime_Type()
)
sleV2Ds4BindingsLeasedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsLeasedTime.setStatus("current")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsLeasedTime.setUnits("second")
_SleV2Ds4BindingsMaskLen_Type = Integer32
_SleV2Ds4BindingsMaskLen_Object = MibTableColumn
sleV2Ds4BindingsMaskLen = _SleV2Ds4BindingsMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 1, 1, 8),
    _SleV2Ds4BindingsMaskLen_Type()
)
sleV2Ds4BindingsMaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsMaskLen.setStatus("current")
_SleV2Ds4BindingsControl_ObjectIdentity = ObjectIdentity
sleV2Ds4BindingsControl = _SleV2Ds4BindingsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 2)
)


class _SleV2Ds4BindingsControlRequest_Type(Integer32):
    """Custom type sleV2Ds4BindingsControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createDsBinding", 1),
          ("destroyDsBinding", 2),
          ("clearDsBinding", 3))
    )


_SleV2Ds4BindingsControlRequest_Type.__name__ = "Integer32"
_SleV2Ds4BindingsControlRequest_Object = MibScalar
sleV2Ds4BindingsControlRequest = _SleV2Ds4BindingsControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 2, 1),
    _SleV2Ds4BindingsControlRequest_Type()
)
sleV2Ds4BindingsControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsControlRequest.setStatus("current")
_SleV2Ds4BindingsControlStatus_Type = SleControlStatusType
_SleV2Ds4BindingsControlStatus_Object = MibScalar
sleV2Ds4BindingsControlStatus = _SleV2Ds4BindingsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 2, 2),
    _SleV2Ds4BindingsControlStatus_Type()
)
sleV2Ds4BindingsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsControlStatus.setStatus("current")
_SleV2Ds4BindingsControlTimer_Type = Gauge32
_SleV2Ds4BindingsControlTimer_Object = MibScalar
sleV2Ds4BindingsControlTimer = _SleV2Ds4BindingsControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 2, 3),
    _SleV2Ds4BindingsControlTimer_Type()
)
sleV2Ds4BindingsControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsControlTimer.setStatus("current")
_SleV2Ds4BindingsControlTimeStamp_Type = TimeTicks
_SleV2Ds4BindingsControlTimeStamp_Object = MibScalar
sleV2Ds4BindingsControlTimeStamp = _SleV2Ds4BindingsControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 2, 4),
    _SleV2Ds4BindingsControlTimeStamp_Type()
)
sleV2Ds4BindingsControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsControlTimeStamp.setStatus("current")
_SleV2Ds4BindingsControlReqResult_Type = SleControlRequestResultType
_SleV2Ds4BindingsControlReqResult_Object = MibScalar
sleV2Ds4BindingsControlReqResult = _SleV2Ds4BindingsControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 2, 5),
    _SleV2Ds4BindingsControlReqResult_Type()
)
sleV2Ds4BindingsControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsControlReqResult.setStatus("current")


class _SleV2Ds4BindingsControlVlanIndex_Type(Integer32):
    """Custom type sleV2Ds4BindingsControlVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleV2Ds4BindingsControlVlanIndex_Type.__name__ = "Integer32"
_SleV2Ds4BindingsControlVlanIndex_Object = MibScalar
sleV2Ds4BindingsControlVlanIndex = _SleV2Ds4BindingsControlVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 2, 6),
    _SleV2Ds4BindingsControlVlanIndex_Type()
)
sleV2Ds4BindingsControlVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsControlVlanIndex.setStatus("current")


class _SleV2Ds4BindingsControlPortIndex_Type(Integer32):
    """Custom type sleV2Ds4BindingsControlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Ds4BindingsControlPortIndex_Type.__name__ = "Integer32"
_SleV2Ds4BindingsControlPortIndex_Object = MibScalar
sleV2Ds4BindingsControlPortIndex = _SleV2Ds4BindingsControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 2, 7),
    _SleV2Ds4BindingsControlPortIndex_Type()
)
sleV2Ds4BindingsControlPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsControlPortIndex.setStatus("current")
_SleV2Ds4BindingsControlAddress_Type = IpAddress
_SleV2Ds4BindingsControlAddress_Object = MibScalar
sleV2Ds4BindingsControlAddress = _SleV2Ds4BindingsControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 2, 8),
    _SleV2Ds4BindingsControlAddress_Type()
)
sleV2Ds4BindingsControlAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsControlAddress.setStatus("current")
_SleV2Ds4BindingsControlMac_Type = MacAddress
_SleV2Ds4BindingsControlMac_Object = MibScalar
sleV2Ds4BindingsControlMac = _SleV2Ds4BindingsControlMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 2, 9),
    _SleV2Ds4BindingsControlMac_Type()
)
sleV2Ds4BindingsControlMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsControlMac.setStatus("current")


class _SleV2Ds4BindingsControlType_Type(Bits):
    """Custom type sleV2Ds4BindingsControlType based on Bits"""
    namedValues = NamedValues(
        *(("dhcpDynamic", 0),
          ("srcGuardStatic", 1))
    )

_SleV2Ds4BindingsControlType_Type.__name__ = "Bits"
_SleV2Ds4BindingsControlType_Object = MibScalar
sleV2Ds4BindingsControlType = _SleV2Ds4BindingsControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 2, 10),
    _SleV2Ds4BindingsControlType_Type()
)
sleV2Ds4BindingsControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsControlType.setStatus("current")


class _SleV2Ds4BindingsControlLeasedTime_Type(Integer32):
    """Custom type sleV2Ds4BindingsControlLeasedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483637),
    )


_SleV2Ds4BindingsControlLeasedTime_Type.__name__ = "Integer32"
_SleV2Ds4BindingsControlLeasedTime_Object = MibScalar
sleV2Ds4BindingsControlLeasedTime = _SleV2Ds4BindingsControlLeasedTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 2, 11),
    _SleV2Ds4BindingsControlLeasedTime_Type()
)
sleV2Ds4BindingsControlLeasedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsControlLeasedTime.setStatus("current")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsControlLeasedTime.setUnits("second")
_SleV2Ds4BindingsControlMaskLen_Type = Integer32
_SleV2Ds4BindingsControlMaskLen_Object = MibScalar
sleV2Ds4BindingsControlMaskLen = _SleV2Ds4BindingsControlMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 2, 12),
    _SleV2Ds4BindingsControlMaskLen_Type()
)
sleV2Ds4BindingsControlMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4BindingsControlMaskLen.setStatus("current")
_SleV2Ds4BindingsNotification_ObjectIdentity = ObjectIdentity
sleV2Ds4BindingsNotification = _SleV2Ds4BindingsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 3)
)
_SleV2Ds4VlanInfoOpt_ObjectIdentity = ObjectIdentity
sleV2Ds4VlanInfoOpt = _SleV2Ds4VlanInfoOpt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 5)
)
_SleV2Ds4VlanInfoOptTable_Object = MibTable
sleV2Ds4VlanInfoOptTable = _SleV2Ds4VlanInfoOptTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 5, 1)
)
if mibBuilder.loadTexts:
    sleV2Ds4VlanInfoOptTable.setStatus("current")
_SleV2Ds4VlanInfoOptEntry_Object = MibTableRow
sleV2Ds4VlanInfoOptEntry = _SleV2Ds4VlanInfoOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 5, 1, 1)
)
sleV2Ds4VlanInfoOptEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Ds4VlanInfoOptIndex"),
)
if mibBuilder.loadTexts:
    sleV2Ds4VlanInfoOptEntry.setStatus("current")


class _SleV2Ds4VlanInfoOptIndex_Type(Integer32):
    """Custom type sleV2Ds4VlanInfoOptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleV2Ds4VlanInfoOptIndex_Type.__name__ = "Integer32"
_SleV2Ds4VlanInfoOptIndex_Object = MibTableColumn
sleV2Ds4VlanInfoOptIndex = _SleV2Ds4VlanInfoOptIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 5, 1, 1, 1),
    _SleV2Ds4VlanInfoOptIndex_Type()
)
sleV2Ds4VlanInfoOptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4VlanInfoOptIndex.setStatus("current")


class _SleV2Ds4VlanInfoOptState_Type(Integer32):
    """Custom type sleV2Ds4VlanInfoOptState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Ds4VlanInfoOptState_Type.__name__ = "Integer32"
_SleV2Ds4VlanInfoOptState_Object = MibTableColumn
sleV2Ds4VlanInfoOptState = _SleV2Ds4VlanInfoOptState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 5, 1, 1, 2),
    _SleV2Ds4VlanInfoOptState_Type()
)
sleV2Ds4VlanInfoOptState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4VlanInfoOptState.setStatus("current")
_SleV2Ds4VlanInforOptControl_ObjectIdentity = ObjectIdentity
sleV2Ds4VlanInforOptControl = _SleV2Ds4VlanInforOptControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 5, 2)
)


class _SleV2Ds4VlanInfoOptControlRequest_Type(Integer32):
    """Custom type sleV2Ds4VlanInfoOptControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setDsVlanInfoOptState", 1)
    )


_SleV2Ds4VlanInfoOptControlRequest_Type.__name__ = "Integer32"
_SleV2Ds4VlanInfoOptControlRequest_Object = MibScalar
sleV2Ds4VlanInfoOptControlRequest = _SleV2Ds4VlanInfoOptControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 5, 2, 1),
    _SleV2Ds4VlanInfoOptControlRequest_Type()
)
sleV2Ds4VlanInfoOptControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4VlanInfoOptControlRequest.setStatus("current")
_SleV2Ds4VlanInfoOptControlStatus_Type = SleControlStatusType
_SleV2Ds4VlanInfoOptControlStatus_Object = MibScalar
sleV2Ds4VlanInfoOptControlStatus = _SleV2Ds4VlanInfoOptControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 5, 2, 2),
    _SleV2Ds4VlanInfoOptControlStatus_Type()
)
sleV2Ds4VlanInfoOptControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4VlanInfoOptControlStatus.setStatus("current")
_SleV2Ds4VlanInfoOptControlTimer_Type = Gauge32
_SleV2Ds4VlanInfoOptControlTimer_Object = MibScalar
sleV2Ds4VlanInfoOptControlTimer = _SleV2Ds4VlanInfoOptControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 5, 2, 3),
    _SleV2Ds4VlanInfoOptControlTimer_Type()
)
sleV2Ds4VlanInfoOptControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4VlanInfoOptControlTimer.setStatus("current")
_SleV2Ds4VlanInfoOptControlTimeStamp_Type = TimeTicks
_SleV2Ds4VlanInfoOptControlTimeStamp_Object = MibScalar
sleV2Ds4VlanInfoOptControlTimeStamp = _SleV2Ds4VlanInfoOptControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 5, 2, 4),
    _SleV2Ds4VlanInfoOptControlTimeStamp_Type()
)
sleV2Ds4VlanInfoOptControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4VlanInfoOptControlTimeStamp.setStatus("current")
_SleV2Ds4VlanInfoOptControlReqResult_Type = SleControlRequestResultType
_SleV2Ds4VlanInfoOptControlReqResult_Object = MibScalar
sleV2Ds4VlanInfoOptControlReqResult = _SleV2Ds4VlanInfoOptControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 5, 2, 5),
    _SleV2Ds4VlanInfoOptControlReqResult_Type()
)
sleV2Ds4VlanInfoOptControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4VlanInfoOptControlReqResult.setStatus("current")


class _SleV2Ds4VlanInfoOptControlIndex_Type(Integer32):
    """Custom type sleV2Ds4VlanInfoOptControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleV2Ds4VlanInfoOptControlIndex_Type.__name__ = "Integer32"
_SleV2Ds4VlanInfoOptControlIndex_Object = MibScalar
sleV2Ds4VlanInfoOptControlIndex = _SleV2Ds4VlanInfoOptControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 5, 2, 6),
    _SleV2Ds4VlanInfoOptControlIndex_Type()
)
sleV2Ds4VlanInfoOptControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4VlanInfoOptControlIndex.setStatus("current")


class _SleV2Ds4VlanInfoOptControlState_Type(Integer32):
    """Custom type sleV2Ds4VlanInfoOptControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Ds4VlanInfoOptControlState_Type.__name__ = "Integer32"
_SleV2Ds4VlanInfoOptControlState_Object = MibScalar
sleV2Ds4VlanInfoOptControlState = _SleV2Ds4VlanInfoOptControlState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 5, 2, 7),
    _SleV2Ds4VlanInfoOptControlState_Type()
)
sleV2Ds4VlanInfoOptControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4VlanInfoOptControlState.setStatus("current")
_SleV2Ds4VlanInfoOptNotification_ObjectIdentity = ObjectIdentity
sleV2Ds4VlanInfoOptNotification = _SleV2Ds4VlanInfoOptNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 5, 3)
)
_SleV2Ds4OptCode_ObjectIdentity = ObjectIdentity
sleV2Ds4OptCode = _SleV2Ds4OptCode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6)
)
_SleV2Ds4OptCodeTable_Object = MibTable
sleV2Ds4OptCodeTable = _SleV2Ds4OptCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 1)
)
if mibBuilder.loadTexts:
    sleV2Ds4OptCodeTable.setStatus("current")
_SleV2Ds4OptCodeEntry_Object = MibTableRow
sleV2Ds4OptCodeEntry = _SleV2Ds4OptCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 1, 1)
)
sleV2Ds4OptCodeEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Ds4OptCodeIfIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Ds4OptCodeNum"),
)
if mibBuilder.loadTexts:
    sleV2Ds4OptCodeEntry.setStatus("current")


class _SleV2Ds4OptCodeIfIndex_Type(Integer32):
    """Custom type sleV2Ds4OptCodeIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleV2Ds4OptCodeIfIndex_Type.__name__ = "Integer32"
_SleV2Ds4OptCodeIfIndex_Object = MibTableColumn
sleV2Ds4OptCodeIfIndex = _SleV2Ds4OptCodeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 1, 1, 1),
    _SleV2Ds4OptCodeIfIndex_Type()
)
sleV2Ds4OptCodeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4OptCodeIfIndex.setStatus("current")


class _SleV2Ds4OptCodeNum_Type(Integer32):
    """Custom type sleV2Ds4OptCodeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_SleV2Ds4OptCodeNum_Type.__name__ = "Integer32"
_SleV2Ds4OptCodeNum_Object = MibTableColumn
sleV2Ds4OptCodeNum = _SleV2Ds4OptCodeNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 1, 1, 2),
    _SleV2Ds4OptCodeNum_Type()
)
sleV2Ds4OptCodeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4OptCodeNum.setStatus("current")
_SleV2Ds4OptCodeFormat_Type = OctetString
_SleV2Ds4OptCodeFormat_Object = MibTableColumn
sleV2Ds4OptCodeFormat = _SleV2Ds4OptCodeFormat_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 1, 1, 3),
    _SleV2Ds4OptCodeFormat_Type()
)
sleV2Ds4OptCodeFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4OptCodeFormat.setStatus("current")


class _SleV2Ds4OptCodePolicy_Type(Integer32):
    """Custom type sleV2Ds4OptCodePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("replace", 0),
          ("keep", 1))
    )


_SleV2Ds4OptCodePolicy_Type.__name__ = "Integer32"
_SleV2Ds4OptCodePolicy_Object = MibTableColumn
sleV2Ds4OptCodePolicy = _SleV2Ds4OptCodePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 1, 1, 4),
    _SleV2Ds4OptCodePolicy_Type()
)
sleV2Ds4OptCodePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4OptCodePolicy.setStatus("current")
_SleV2Ds4OptCodeControl_ObjectIdentity = ObjectIdentity
sleV2Ds4OptCodeControl = _SleV2Ds4OptCodeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 2)
)


class _SleV2Ds4OptCodeControlRequest_Type(Integer32):
    """Custom type sleV2Ds4OptCodeControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setDsPortOptCodeFormat", 1),
          ("setDsPortOptCodePolicy", 2),
          ("destroyDsPortOptCode", 3))
    )


_SleV2Ds4OptCodeControlRequest_Type.__name__ = "Integer32"
_SleV2Ds4OptCodeControlRequest_Object = MibScalar
sleV2Ds4OptCodeControlRequest = _SleV2Ds4OptCodeControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 2, 1),
    _SleV2Ds4OptCodeControlRequest_Type()
)
sleV2Ds4OptCodeControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4OptCodeControlRequest.setStatus("current")
_SleV2Ds4OptCodeControlStatus_Type = SleControlStatusType
_SleV2Ds4OptCodeControlStatus_Object = MibScalar
sleV2Ds4OptCodeControlStatus = _SleV2Ds4OptCodeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 2, 2),
    _SleV2Ds4OptCodeControlStatus_Type()
)
sleV2Ds4OptCodeControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4OptCodeControlStatus.setStatus("current")
_SleV2Ds4OptCodeControlTimer_Type = Gauge32
_SleV2Ds4OptCodeControlTimer_Object = MibScalar
sleV2Ds4OptCodeControlTimer = _SleV2Ds4OptCodeControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 2, 3),
    _SleV2Ds4OptCodeControlTimer_Type()
)
sleV2Ds4OptCodeControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4OptCodeControlTimer.setStatus("current")
_SleV2Ds4OptCodeControlTimeStamp_Type = TimeTicks
_SleV2Ds4OptCodeControlTimeStamp_Object = MibScalar
sleV2Ds4OptCodeControlTimeStamp = _SleV2Ds4OptCodeControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 2, 4),
    _SleV2Ds4OptCodeControlTimeStamp_Type()
)
sleV2Ds4OptCodeControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4OptCodeControlTimeStamp.setStatus("current")
_SleV2Ds4OptCodeControlReqResult_Type = SleControlRequestResultType
_SleV2Ds4OptCodeControlReqResult_Object = MibScalar
sleV2Ds4OptCodeControlReqResult = _SleV2Ds4OptCodeControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 2, 5),
    _SleV2Ds4OptCodeControlReqResult_Type()
)
sleV2Ds4OptCodeControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Ds4OptCodeControlReqResult.setStatus("current")
_SleV2Ds4OptCodeControlIfIndex_Type = Integer32
_SleV2Ds4OptCodeControlIfIndex_Object = MibScalar
sleV2Ds4OptCodeControlIfIndex = _SleV2Ds4OptCodeControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 2, 6),
    _SleV2Ds4OptCodeControlIfIndex_Type()
)
sleV2Ds4OptCodeControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4OptCodeControlIfIndex.setStatus("current")


class _SleV2Ds4OptCodeControlNum_Type(Integer32):
    """Custom type sleV2Ds4OptCodeControlNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_SleV2Ds4OptCodeControlNum_Type.__name__ = "Integer32"
_SleV2Ds4OptCodeControlNum_Object = MibScalar
sleV2Ds4OptCodeControlNum = _SleV2Ds4OptCodeControlNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 2, 7),
    _SleV2Ds4OptCodeControlNum_Type()
)
sleV2Ds4OptCodeControlNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4OptCodeControlNum.setStatus("current")
_SleV2Ds4OptCodeControlFormat_Type = OctetString
_SleV2Ds4OptCodeControlFormat_Object = MibScalar
sleV2Ds4OptCodeControlFormat = _SleV2Ds4OptCodeControlFormat_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 2, 8),
    _SleV2Ds4OptCodeControlFormat_Type()
)
sleV2Ds4OptCodeControlFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4OptCodeControlFormat.setStatus("current")


class _SleV2Ds4OptCodeControlPolicy_Type(Integer32):
    """Custom type sleV2Ds4OptCodeControlPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("replace", 0),
          ("keep", 1))
    )


_SleV2Ds4OptCodeControlPolicy_Type.__name__ = "Integer32"
_SleV2Ds4OptCodeControlPolicy_Object = MibScalar
sleV2Ds4OptCodeControlPolicy = _SleV2Ds4OptCodeControlPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 2, 9),
    _SleV2Ds4OptCodeControlPolicy_Type()
)
sleV2Ds4OptCodeControlPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Ds4OptCodeControlPolicy.setStatus("current")
_SleV2Ds4OptCodeNotification_ObjectIdentity = ObjectIdentity
sleV2Ds4OptCodeNotification = _SleV2Ds4OptCodeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 3)
)
_SleV2Dhcp4Relay_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Relay = _SleV2Dhcp4Relay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7)
)
_SleV2Dhcp4RelayInterface_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RelayInterface = _SleV2Dhcp4RelayInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1)
)
_SleV2Dhcp4RelayIfTable_Object = MibTable
sleV2Dhcp4RelayIfTable = _SleV2Dhcp4RelayIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIfTable.setStatus("current")
_SleV2Dhcp4RelayIfEntry_Object = MibTableRow
sleV2Dhcp4RelayIfEntry = _SleV2Dhcp4RelayIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 1, 1)
)
sleV2Dhcp4RelayIfEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfIndex"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIfEntry.setStatus("current")


class _SleV2Dhcp4RelayIfIndex_Type(Integer32):
    """Custom type sleV2Dhcp4RelayIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleV2Dhcp4RelayIfIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4RelayIfIndex_Object = MibTableColumn
sleV2Dhcp4RelayIfIndex = _SleV2Dhcp4RelayIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 1, 1, 1),
    _SleV2Dhcp4RelayIfIndex_Type()
)
sleV2Dhcp4RelayIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIfIndex.setStatus("current")


class _SleV2Dhcp4RelayIfSimpleOpt82AdminState_Type(Integer32):
    """Custom type sleV2Dhcp4RelayIfSimpleOpt82AdminState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Dhcp4RelayIfSimpleOpt82AdminState_Type.__name__ = "Integer32"
_SleV2Dhcp4RelayIfSimpleOpt82AdminState_Object = MibTableColumn
sleV2Dhcp4RelayIfSimpleOpt82AdminState = _SleV2Dhcp4RelayIfSimpleOpt82AdminState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 1, 1, 2),
    _SleV2Dhcp4RelayIfSimpleOpt82AdminState_Type()
)
sleV2Dhcp4RelayIfSimpleOpt82AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIfSimpleOpt82AdminState.setStatus("current")


class _SleV2Dhcp4RelayIfSimpleOpt82OperState_Type(Integer32):
    """Custom type sleV2Dhcp4RelayIfSimpleOpt82OperState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SleV2Dhcp4RelayIfSimpleOpt82OperState_Type.__name__ = "Integer32"
_SleV2Dhcp4RelayIfSimpleOpt82OperState_Object = MibTableColumn
sleV2Dhcp4RelayIfSimpleOpt82OperState = _SleV2Dhcp4RelayIfSimpleOpt82OperState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 1, 1, 3),
    _SleV2Dhcp4RelayIfSimpleOpt82OperState_Type()
)
sleV2Dhcp4RelayIfSimpleOpt82OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIfSimpleOpt82OperState.setStatus("current")


class _SleV2Dhcp4RelayIfMaxHops_Type(Integer32):
    """Custom type sleV2Dhcp4RelayIfMaxHops based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SleV2Dhcp4RelayIfMaxHops_Type.__name__ = "Integer32"
_SleV2Dhcp4RelayIfMaxHops_Object = MibTableColumn
sleV2Dhcp4RelayIfMaxHops = _SleV2Dhcp4RelayIfMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 1, 1, 4),
    _SleV2Dhcp4RelayIfMaxHops_Type()
)
sleV2Dhcp4RelayIfMaxHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIfMaxHops.setStatus("current")
_SleV2Dhcp4RelayIfControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RelayIfControl = _SleV2Dhcp4RelayIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 2)
)


class _SleV2Dhcp4RelayIfControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4RelayIfControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setDhcpSimplifiedOpt82State", 1),
          ("setDhcpRelayMaxHops", 2))
    )


_SleV2Dhcp4RelayIfControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4RelayIfControlRequest_Object = MibScalar
sleV2Dhcp4RelayIfControlRequest = _SleV2Dhcp4RelayIfControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 2, 1),
    _SleV2Dhcp4RelayIfControlRequest_Type()
)
sleV2Dhcp4RelayIfControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIfControlRequest.setStatus("current")
_SleV2Dhcp4RelayIfControlStatus_Type = SleControlStatusType
_SleV2Dhcp4RelayIfControlStatus_Object = MibScalar
sleV2Dhcp4RelayIfControlStatus = _SleV2Dhcp4RelayIfControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 2, 2),
    _SleV2Dhcp4RelayIfControlStatus_Type()
)
sleV2Dhcp4RelayIfControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIfControlStatus.setStatus("current")
_SleV2Dhcp4RelayIfControlTimer_Type = Gauge32
_SleV2Dhcp4RelayIfControlTimer_Object = MibScalar
sleV2Dhcp4RelayIfControlTimer = _SleV2Dhcp4RelayIfControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 2, 3),
    _SleV2Dhcp4RelayIfControlTimer_Type()
)
sleV2Dhcp4RelayIfControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIfControlTimer.setStatus("current")
_SleV2Dhcp4RelayIfControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4RelayIfControlTimeStamp_Object = MibScalar
sleV2Dhcp4RelayIfControlTimeStamp = _SleV2Dhcp4RelayIfControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 2, 4),
    _SleV2Dhcp4RelayIfControlTimeStamp_Type()
)
sleV2Dhcp4RelayIfControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIfControlTimeStamp.setStatus("current")
_SleV2Dhcp4RelayIfControllReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4RelayIfControllReqResult_Object = MibScalar
sleV2Dhcp4RelayIfControllReqResult = _SleV2Dhcp4RelayIfControllReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 2, 5),
    _SleV2Dhcp4RelayIfControllReqResult_Type()
)
sleV2Dhcp4RelayIfControllReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIfControllReqResult.setStatus("current")


class _SleV2Dhcp4RelayIfControlIndex_Type(Integer32):
    """Custom type sleV2Dhcp4RelayIfControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleV2Dhcp4RelayIfControlIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4RelayIfControlIndex_Object = MibScalar
sleV2Dhcp4RelayIfControlIndex = _SleV2Dhcp4RelayIfControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 2, 6),
    _SleV2Dhcp4RelayIfControlIndex_Type()
)
sleV2Dhcp4RelayIfControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIfControlIndex.setStatus("current")


class _SleV2Dhcp4RelayIfControlSimpleOpt82AdminState_Type(Integer32):
    """Custom type sleV2Dhcp4RelayIfControlSimpleOpt82AdminState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Dhcp4RelayIfControlSimpleOpt82AdminState_Type.__name__ = "Integer32"
_SleV2Dhcp4RelayIfControlSimpleOpt82AdminState_Object = MibScalar
sleV2Dhcp4RelayIfControlSimpleOpt82AdminState = _SleV2Dhcp4RelayIfControlSimpleOpt82AdminState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 2, 7),
    _SleV2Dhcp4RelayIfControlSimpleOpt82AdminState_Type()
)
sleV2Dhcp4RelayIfControlSimpleOpt82AdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIfControlSimpleOpt82AdminState.setStatus("current")


class _SleV2Dhcp4RelayIfControlMaxHops_Type(Integer32):
    """Custom type sleV2Dhcp4RelayIfControlMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SleV2Dhcp4RelayIfControlMaxHops_Type.__name__ = "Integer32"
_SleV2Dhcp4RelayIfControlMaxHops_Object = MibScalar
sleV2Dhcp4RelayIfControlMaxHops = _SleV2Dhcp4RelayIfControlMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 2, 8),
    _SleV2Dhcp4RelayIfControlMaxHops_Type()
)
sleV2Dhcp4RelayIfControlMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIfControlMaxHops.setStatus("current")
_SleV2Dhcp4RelayIfNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RelayIfNotification = _SleV2Dhcp4RelayIfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 3)
)
_SleV2Dhcp4RelayHelper_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RelayHelper = _SleV2Dhcp4RelayHelper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2)
)
_SleV2Dhcp4RelayHelperTable_Object = MibTable
sleV2Dhcp4RelayHelperTable = _SleV2Dhcp4RelayHelperTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperTable.setStatus("current")
_SleV2Dhcp4RelayHelperEntry_Object = MibTableRow
sleV2Dhcp4RelayHelperEntry = _SleV2Dhcp4RelayHelperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 1, 1)
)
sleV2Dhcp4RelayHelperEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperOui"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperAddress"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperEntry.setStatus("current")


class _SleV2Dhcp4RelayHelperOui_Type(OctetString):
    """Custom type sleV2Dhcp4RelayHelperOui based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_SleV2Dhcp4RelayHelperOui_Type.__name__ = "OctetString"
_SleV2Dhcp4RelayHelperOui_Object = MibTableColumn
sleV2Dhcp4RelayHelperOui = _SleV2Dhcp4RelayHelperOui_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 1, 1, 1),
    _SleV2Dhcp4RelayHelperOui_Type()
)
sleV2Dhcp4RelayHelperOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperOui.setStatus("current")
_SleV2Dhcp4RelayHelperAddress_Type = IpAddress
_SleV2Dhcp4RelayHelperAddress_Object = MibTableColumn
sleV2Dhcp4RelayHelperAddress = _SleV2Dhcp4RelayHelperAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 1, 1, 2),
    _SleV2Dhcp4RelayHelperAddress_Type()
)
sleV2Dhcp4RelayHelperAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperAddress.setStatus("current")


class _SleV2Dhcp4RelayHelperType_Type(Integer32):
    """Custom type sleV2Dhcp4RelayHelperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("unknown", 0)
    )


_SleV2Dhcp4RelayHelperType_Type.__name__ = "Integer32"
_SleV2Dhcp4RelayHelperType_Object = MibTableColumn
sleV2Dhcp4RelayHelperType = _SleV2Dhcp4RelayHelperType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 1, 1, 3),
    _SleV2Dhcp4RelayHelperType_Type()
)
sleV2Dhcp4RelayHelperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperType.setStatus("current")
_SleV2Dhcp4RelayHelperControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RelayHelperControl = _SleV2Dhcp4RelayHelperControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 2)
)


class _SleV2Dhcp4RelayHelperControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4RelayHelperControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createDhcpRelayHelperEntry", 1),
          ("destroyDhcpRelayHelperEntry", 2),
          ("clearDhcpRelayHelperEntry", 3))
    )


_SleV2Dhcp4RelayHelperControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4RelayHelperControlRequest_Object = MibScalar
sleV2Dhcp4RelayHelperControlRequest = _SleV2Dhcp4RelayHelperControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 2, 1),
    _SleV2Dhcp4RelayHelperControlRequest_Type()
)
sleV2Dhcp4RelayHelperControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperControlRequest.setStatus("current")
_SleV2Dhcp4RelayHelperControlStatus_Type = SleControlStatusType
_SleV2Dhcp4RelayHelperControlStatus_Object = MibScalar
sleV2Dhcp4RelayHelperControlStatus = _SleV2Dhcp4RelayHelperControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 2, 2),
    _SleV2Dhcp4RelayHelperControlStatus_Type()
)
sleV2Dhcp4RelayHelperControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperControlStatus.setStatus("current")
_SleV2Dhcp4RelayHelperControlTimer_Type = Gauge32
_SleV2Dhcp4RelayHelperControlTimer_Object = MibScalar
sleV2Dhcp4RelayHelperControlTimer = _SleV2Dhcp4RelayHelperControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 2, 3),
    _SleV2Dhcp4RelayHelperControlTimer_Type()
)
sleV2Dhcp4RelayHelperControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperControlTimer.setStatus("current")
_SleV2Dhcp4RelayHelperControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4RelayHelperControlTimeStamp_Object = MibScalar
sleV2Dhcp4RelayHelperControlTimeStamp = _SleV2Dhcp4RelayHelperControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 2, 4),
    _SleV2Dhcp4RelayHelperControlTimeStamp_Type()
)
sleV2Dhcp4RelayHelperControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperControlTimeStamp.setStatus("current")
_SleV2Dhcp4RelayHelperControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4RelayHelperControlReqResult_Object = MibScalar
sleV2Dhcp4RelayHelperControlReqResult = _SleV2Dhcp4RelayHelperControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 2, 5),
    _SleV2Dhcp4RelayHelperControlReqResult_Type()
)
sleV2Dhcp4RelayHelperControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperControlReqResult.setStatus("current")


class _SleV2Dhcp4RelayHelperControlIfIndex_Type(Integer32):
    """Custom type sleV2Dhcp4RelayHelperControlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleV2Dhcp4RelayHelperControlIfIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4RelayHelperControlIfIndex_Object = MibScalar
sleV2Dhcp4RelayHelperControlIfIndex = _SleV2Dhcp4RelayHelperControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 2, 6),
    _SleV2Dhcp4RelayHelperControlIfIndex_Type()
)
sleV2Dhcp4RelayHelperControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperControlIfIndex.setStatus("current")


class _SleV2Dhcp4RelayHelperControlOui_Type(OctetString):
    """Custom type sleV2Dhcp4RelayHelperControlOui based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_SleV2Dhcp4RelayHelperControlOui_Type.__name__ = "OctetString"
_SleV2Dhcp4RelayHelperControlOui_Object = MibScalar
sleV2Dhcp4RelayHelperControlOui = _SleV2Dhcp4RelayHelperControlOui_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 2, 7),
    _SleV2Dhcp4RelayHelperControlOui_Type()
)
sleV2Dhcp4RelayHelperControlOui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperControlOui.setStatus("current")
_SleV2Dhcp4RelayHelperControlAddress_Type = IpAddress
_SleV2Dhcp4RelayHelperControlAddress_Object = MibScalar
sleV2Dhcp4RelayHelperControlAddress = _SleV2Dhcp4RelayHelperControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 2, 8),
    _SleV2Dhcp4RelayHelperControlAddress_Type()
)
sleV2Dhcp4RelayHelperControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperControlAddress.setStatus("current")


class _SleV2Dhcp4RelayHelperControlType_Type(Integer32):
    """Custom type sleV2Dhcp4RelayHelperControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("unknown", 0)
    )


_SleV2Dhcp4RelayHelperControlType_Type.__name__ = "Integer32"
_SleV2Dhcp4RelayHelperControlType_Object = MibScalar
sleV2Dhcp4RelayHelperControlType = _SleV2Dhcp4RelayHelperControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 2, 9),
    _SleV2Dhcp4RelayHelperControlType_Type()
)
sleV2Dhcp4RelayHelperControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperControlType.setStatus("current")
_SleV2Dhcp4RelayHelperNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RelayHelperNotification = _SleV2Dhcp4RelayHelperNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 3)
)
_SleV2Dhcp4RelayStats_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RelayStats = _SleV2Dhcp4RelayStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3)
)
_SleV2Dhcp4RelayIntrStatsTable_Object = MibTable
sleV2Dhcp4RelayIntrStatsTable = _SleV2Dhcp4RelayIntrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrStatsTable.setStatus("current")
_SleV2Dhcp4RelayIntrStatsEntry_Object = MibTableRow
sleV2Dhcp4RelayIntrStatsEntry = _SleV2Dhcp4RelayIntrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1)
)
sleV2Dhcp4RelayIntrStatsEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrIndex"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrStatsEntry.setStatus("current")


class _SleV2Dhcp4RelayIntrIndex_Type(Integer32):
    """Custom type sleV2Dhcp4RelayIntrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleV2Dhcp4RelayIntrIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4RelayIntrIndex_Object = MibTableColumn
sleV2Dhcp4RelayIntrIndex = _SleV2Dhcp4RelayIntrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 1),
    _SleV2Dhcp4RelayIntrIndex_Type()
)
sleV2Dhcp4RelayIntrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrIndex.setStatus("current")
_SleV2Dhcp4RelayIntrRcvd_Type = Counter32
_SleV2Dhcp4RelayIntrRcvd_Object = MibTableColumn
sleV2Dhcp4RelayIntrRcvd = _SleV2Dhcp4RelayIntrRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 2),
    _SleV2Dhcp4RelayIntrRcvd_Type()
)
sleV2Dhcp4RelayIntrRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrRcvd.setStatus("current")
_SleV2Dhcp4RelayIntrSent_Type = Gauge32
_SleV2Dhcp4RelayIntrSent_Object = MibTableColumn
sleV2Dhcp4RelayIntrSent = _SleV2Dhcp4RelayIntrSent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 3),
    _SleV2Dhcp4RelayIntrSent_Type()
)
sleV2Dhcp4RelayIntrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrSent.setStatus("current")
_SleV2Dhcp4RelayIntrRcvdErrors_Type = Counter32
_SleV2Dhcp4RelayIntrRcvdErrors_Object = MibTableColumn
sleV2Dhcp4RelayIntrRcvdErrors = _SleV2Dhcp4RelayIntrRcvdErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 4),
    _SleV2Dhcp4RelayIntrRcvdErrors_Type()
)
sleV2Dhcp4RelayIntrRcvdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrRcvdErrors.setStatus("current")
_SleV2Dhcp4RelayIntrSentErrors_Type = Counter32
_SleV2Dhcp4RelayIntrSentErrors_Object = MibTableColumn
sleV2Dhcp4RelayIntrSentErrors = _SleV2Dhcp4RelayIntrSentErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 5),
    _SleV2Dhcp4RelayIntrSentErrors_Type()
)
sleV2Dhcp4RelayIntrSentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrSentErrors.setStatus("current")
_SleV2Dhcp4RelayIntrRcvdBootpRequest_Type = Counter32
_SleV2Dhcp4RelayIntrRcvdBootpRequest_Object = MibTableColumn
sleV2Dhcp4RelayIntrRcvdBootpRequest = _SleV2Dhcp4RelayIntrRcvdBootpRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 6),
    _SleV2Dhcp4RelayIntrRcvdBootpRequest_Type()
)
sleV2Dhcp4RelayIntrRcvdBootpRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrRcvdBootpRequest.setStatus("current")
_SleV2Dhcp4RelayIntrRcvdBootpReply_Type = Counter32
_SleV2Dhcp4RelayIntrRcvdBootpReply_Object = MibTableColumn
sleV2Dhcp4RelayIntrRcvdBootpReply = _SleV2Dhcp4RelayIntrRcvdBootpReply_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 7),
    _SleV2Dhcp4RelayIntrRcvdBootpReply_Type()
)
sleV2Dhcp4RelayIntrRcvdBootpReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrRcvdBootpReply.setStatus("current")
_SleV2Dhcp4RelayIntrSentBootpRequest_Type = Counter32
_SleV2Dhcp4RelayIntrSentBootpRequest_Object = MibTableColumn
sleV2Dhcp4RelayIntrSentBootpRequest = _SleV2Dhcp4RelayIntrSentBootpRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 8),
    _SleV2Dhcp4RelayIntrSentBootpRequest_Type()
)
sleV2Dhcp4RelayIntrSentBootpRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrSentBootpRequest.setStatus("current")
_SleV2Dhcp4RelayIntrSentBootpReply_Type = Counter32
_SleV2Dhcp4RelayIntrSentBootpReply_Object = MibTableColumn
sleV2Dhcp4RelayIntrSentBootpReply = _SleV2Dhcp4RelayIntrSentBootpReply_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 9),
    _SleV2Dhcp4RelayIntrSentBootpReply_Type()
)
sleV2Dhcp4RelayIntrSentBootpReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrSentBootpReply.setStatus("current")
_SleV2Dhcp4RelayIntrRcvdDiscover_Type = Counter32
_SleV2Dhcp4RelayIntrRcvdDiscover_Object = MibTableColumn
sleV2Dhcp4RelayIntrRcvdDiscover = _SleV2Dhcp4RelayIntrRcvdDiscover_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 10),
    _SleV2Dhcp4RelayIntrRcvdDiscover_Type()
)
sleV2Dhcp4RelayIntrRcvdDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrRcvdDiscover.setStatus("current")
_SleV2Dhcp4RelayIntrRcvdRequest_Type = Counter32
_SleV2Dhcp4RelayIntrRcvdRequest_Object = MibTableColumn
sleV2Dhcp4RelayIntrRcvdRequest = _SleV2Dhcp4RelayIntrRcvdRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 11),
    _SleV2Dhcp4RelayIntrRcvdRequest_Type()
)
sleV2Dhcp4RelayIntrRcvdRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrRcvdRequest.setStatus("current")
_SleV2Dhcp4RelayIntrRcvdRelease_Type = Counter32
_SleV2Dhcp4RelayIntrRcvdRelease_Object = MibTableColumn
sleV2Dhcp4RelayIntrRcvdRelease = _SleV2Dhcp4RelayIntrRcvdRelease_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 12),
    _SleV2Dhcp4RelayIntrRcvdRelease_Type()
)
sleV2Dhcp4RelayIntrRcvdRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrRcvdRelease.setStatus("current")
_SleV2Dhcp4RelayIntrRcvdInform_Type = Counter32
_SleV2Dhcp4RelayIntrRcvdInform_Object = MibTableColumn
sleV2Dhcp4RelayIntrRcvdInform = _SleV2Dhcp4RelayIntrRcvdInform_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 13),
    _SleV2Dhcp4RelayIntrRcvdInform_Type()
)
sleV2Dhcp4RelayIntrRcvdInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrRcvdInform.setStatus("current")
_SleV2Dhcp4RelayIntrRcvdDecline_Type = Counter32
_SleV2Dhcp4RelayIntrRcvdDecline_Object = MibTableColumn
sleV2Dhcp4RelayIntrRcvdDecline = _SleV2Dhcp4RelayIntrRcvdDecline_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 14),
    _SleV2Dhcp4RelayIntrRcvdDecline_Type()
)
sleV2Dhcp4RelayIntrRcvdDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrRcvdDecline.setStatus("current")
_SleV2Dhcp4RelayIntrSentDiscover_Type = Counter32
_SleV2Dhcp4RelayIntrSentDiscover_Object = MibTableColumn
sleV2Dhcp4RelayIntrSentDiscover = _SleV2Dhcp4RelayIntrSentDiscover_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 15),
    _SleV2Dhcp4RelayIntrSentDiscover_Type()
)
sleV2Dhcp4RelayIntrSentDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrSentDiscover.setStatus("current")
_SleV2Dhcp4RelayIntrSentRequest_Type = Counter32
_SleV2Dhcp4RelayIntrSentRequest_Object = MibTableColumn
sleV2Dhcp4RelayIntrSentRequest = _SleV2Dhcp4RelayIntrSentRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 16),
    _SleV2Dhcp4RelayIntrSentRequest_Type()
)
sleV2Dhcp4RelayIntrSentRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrSentRequest.setStatus("current")
_SleV2Dhcp4RelayIntrSentRelease_Type = Counter32
_SleV2Dhcp4RelayIntrSentRelease_Object = MibTableColumn
sleV2Dhcp4RelayIntrSentRelease = _SleV2Dhcp4RelayIntrSentRelease_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 17),
    _SleV2Dhcp4RelayIntrSentRelease_Type()
)
sleV2Dhcp4RelayIntrSentRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrSentRelease.setStatus("current")
_SleV2Dhcp4RelayIntrSentInform_Type = Counter32
_SleV2Dhcp4RelayIntrSentInform_Object = MibTableColumn
sleV2Dhcp4RelayIntrSentInform = _SleV2Dhcp4RelayIntrSentInform_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 18),
    _SleV2Dhcp4RelayIntrSentInform_Type()
)
sleV2Dhcp4RelayIntrSentInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrSentInform.setStatus("current")
_SleV2Dhcp4RelayIntrSentDecline_Type = Counter32
_SleV2Dhcp4RelayIntrSentDecline_Object = MibTableColumn
sleV2Dhcp4RelayIntrSentDecline = _SleV2Dhcp4RelayIntrSentDecline_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 19),
    _SleV2Dhcp4RelayIntrSentDecline_Type()
)
sleV2Dhcp4RelayIntrSentDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrSentDecline.setStatus("current")
_SleV2Dhcp4RelayIntrRcvdOffer_Type = Counter32
_SleV2Dhcp4RelayIntrRcvdOffer_Object = MibTableColumn
sleV2Dhcp4RelayIntrRcvdOffer = _SleV2Dhcp4RelayIntrRcvdOffer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 20),
    _SleV2Dhcp4RelayIntrRcvdOffer_Type()
)
sleV2Dhcp4RelayIntrRcvdOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrRcvdOffer.setStatus("current")
_SleV2Dhcp4RelayIntrRcvdAck_Type = Counter32
_SleV2Dhcp4RelayIntrRcvdAck_Object = MibTableColumn
sleV2Dhcp4RelayIntrRcvdAck = _SleV2Dhcp4RelayIntrRcvdAck_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 21),
    _SleV2Dhcp4RelayIntrRcvdAck_Type()
)
sleV2Dhcp4RelayIntrRcvdAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrRcvdAck.setStatus("current")
_SleV2Dhcp4RelayIntrRcvdNack_Type = Counter32
_SleV2Dhcp4RelayIntrRcvdNack_Object = MibTableColumn
sleV2Dhcp4RelayIntrRcvdNack = _SleV2Dhcp4RelayIntrRcvdNack_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 22),
    _SleV2Dhcp4RelayIntrRcvdNack_Type()
)
sleV2Dhcp4RelayIntrRcvdNack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrRcvdNack.setStatus("current")
_SleV2Dhcp4RelayIntrSentOffer_Type = Counter32
_SleV2Dhcp4RelayIntrSentOffer_Object = MibTableColumn
sleV2Dhcp4RelayIntrSentOffer = _SleV2Dhcp4RelayIntrSentOffer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 23),
    _SleV2Dhcp4RelayIntrSentOffer_Type()
)
sleV2Dhcp4RelayIntrSentOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrSentOffer.setStatus("current")
_SleV2Dhcp4RelayIntrSentAck_Type = Counter32
_SleV2Dhcp4RelayIntrSentAck_Object = MibTableColumn
sleV2Dhcp4RelayIntrSentAck = _SleV2Dhcp4RelayIntrSentAck_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 24),
    _SleV2Dhcp4RelayIntrSentAck_Type()
)
sleV2Dhcp4RelayIntrSentAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrSentAck.setStatus("current")
_SleV2Dhcp4RelayIntrSentNack_Type = Counter32
_SleV2Dhcp4RelayIntrSentNack_Object = MibTableColumn
sleV2Dhcp4RelayIntrSentNack = _SleV2Dhcp4RelayIntrSentNack_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 1, 1, 25),
    _SleV2Dhcp4RelayIntrSentNack_Type()
)
sleV2Dhcp4RelayIntrSentNack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrSentNack.setStatus("current")
_SleV2Dhcp4RelayIntrStatsControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RelayIntrStatsControl = _SleV2Dhcp4RelayIntrStatsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 2)
)


class _SleV2Dhcp4RelayIntrStatsControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4RelayIntrStatsControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearRelayStats", 1)
    )


_SleV2Dhcp4RelayIntrStatsControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4RelayIntrStatsControlRequest_Object = MibScalar
sleV2Dhcp4RelayIntrStatsControlRequest = _SleV2Dhcp4RelayIntrStatsControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 2, 1),
    _SleV2Dhcp4RelayIntrStatsControlRequest_Type()
)
sleV2Dhcp4RelayIntrStatsControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrStatsControlRequest.setStatus("current")
_SleV2Dhcp4RelayIntrStatsControlStatus_Type = SleControlStatusType
_SleV2Dhcp4RelayIntrStatsControlStatus_Object = MibScalar
sleV2Dhcp4RelayIntrStatsControlStatus = _SleV2Dhcp4RelayIntrStatsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 2, 2),
    _SleV2Dhcp4RelayIntrStatsControlStatus_Type()
)
sleV2Dhcp4RelayIntrStatsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrStatsControlStatus.setStatus("current")
_SleV2Dhcp4RelayIntrStatsControlTimer_Type = Gauge32
_SleV2Dhcp4RelayIntrStatsControlTimer_Object = MibScalar
sleV2Dhcp4RelayIntrStatsControlTimer = _SleV2Dhcp4RelayIntrStatsControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 2, 3),
    _SleV2Dhcp4RelayIntrStatsControlTimer_Type()
)
sleV2Dhcp4RelayIntrStatsControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrStatsControlTimer.setStatus("current")
_SleV2Dhcp4RelayIntrStatsControITimeStamp_Type = TimeTicks
_SleV2Dhcp4RelayIntrStatsControITimeStamp_Object = MibScalar
sleV2Dhcp4RelayIntrStatsControITimeStamp = _SleV2Dhcp4RelayIntrStatsControITimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 2, 4),
    _SleV2Dhcp4RelayIntrStatsControITimeStamp_Type()
)
sleV2Dhcp4RelayIntrStatsControITimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrStatsControITimeStamp.setStatus("current")
_SleV2Dhcp4RelayIntrStatsControIResult_Type = SleControlRequestResultType
_SleV2Dhcp4RelayIntrStatsControIResult_Object = MibScalar
sleV2Dhcp4RelayIntrStatsControIResult = _SleV2Dhcp4RelayIntrStatsControIResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 2, 5),
    _SleV2Dhcp4RelayIntrStatsControIResult_Type()
)
sleV2Dhcp4RelayIntrStatsControIResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrStatsControIResult.setStatus("current")
_SleV2Dhcp4RelayIntrStatsControIndex_Type = Integer32
_SleV2Dhcp4RelayIntrStatsControIndex_Object = MibScalar
sleV2Dhcp4RelayIntrStatsControIndex = _SleV2Dhcp4RelayIntrStatsControIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 2, 6),
    _SleV2Dhcp4RelayIntrStatsControIndex_Type()
)
sleV2Dhcp4RelayIntrStatsControIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIntrStatsControIndex.setStatus("current")
_SleV2Dhcp4RelayIntrStatsNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4RelayIntrStatsNotification = _SleV2Dhcp4RelayIntrStatsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 3)
)
_SleV2Dhcp4Client_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Client = _SleV2Dhcp4Client_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8)
)
_SleV2Dhcp4ClientInterface_ObjectIdentity = ObjectIdentity
sleV2Dhcp4ClientInterface = _SleV2Dhcp4ClientInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1)
)
_SleV2Dhcp4ClientIfTable_Object = MibTable
sleV2Dhcp4ClientIfTable = _SleV2Dhcp4ClientIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfTable.setStatus("current")
_SleV2Dhcp4ClientIfEntry_Object = MibTableRow
sleV2Dhcp4ClientIfEntry = _SleV2Dhcp4ClientIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1, 1)
)
sleV2Dhcp4ClientIfEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfIndex"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfEntry.setStatus("current")


class _SleV2Dhcp4ClientIfIndex_Type(Integer32):
    """Custom type sleV2Dhcp4ClientIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleV2Dhcp4ClientIfIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientIfIndex_Object = MibTableColumn
sleV2Dhcp4ClientIfIndex = _SleV2Dhcp4ClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1, 1, 1),
    _SleV2Dhcp4ClientIfIndex_Type()
)
sleV2Dhcp4ClientIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfIndex.setStatus("current")


class _SleV2Dhcp4ClientIfActivity_Type(Integer32):
    """Custom type sleV2Dhcp4ClientIfActivity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Dhcp4ClientIfActivity_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientIfActivity_Object = MibTableColumn
sleV2Dhcp4ClientIfActivity = _SleV2Dhcp4ClientIfActivity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1, 1, 2),
    _SleV2Dhcp4ClientIfActivity_Type()
)
sleV2Dhcp4ClientIfActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfActivity.setStatus("current")
_SleV2Dhcp4ClientIfAddress_Type = IpAddress
_SleV2Dhcp4ClientIfAddress_Object = MibTableColumn
sleV2Dhcp4ClientIfAddress = _SleV2Dhcp4ClientIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1, 1, 3),
    _SleV2Dhcp4ClientIfAddress_Type()
)
sleV2Dhcp4ClientIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfAddress.setStatus("current")
_SleV2Dhcp4ClientIfMask_Type = IpAddress
_SleV2Dhcp4ClientIfMask_Object = MibTableColumn
sleV2Dhcp4ClientIfMask = _SleV2Dhcp4ClientIfMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1, 1, 4),
    _SleV2Dhcp4ClientIfMask_Type()
)
sleV2Dhcp4ClientIfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfMask.setStatus("current")
_SleV2Dhcp4ClientIfServer_Type = IpAddress
_SleV2Dhcp4ClientIfServer_Object = MibTableColumn
sleV2Dhcp4ClientIfServer = _SleV2Dhcp4ClientIfServer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1, 1, 5),
    _SleV2Dhcp4ClientIfServer_Type()
)
sleV2Dhcp4ClientIfServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfServer.setStatus("current")


class _SleV2Dhcp4ClientIfHostName_Type(OctetString):
    """Custom type sleV2Dhcp4ClientIfHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4ClientIfHostName_Type.__name__ = "OctetString"
_SleV2Dhcp4ClientIfHostName_Object = MibTableColumn
sleV2Dhcp4ClientIfHostName = _SleV2Dhcp4ClientIfHostName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1, 1, 6),
    _SleV2Dhcp4ClientIfHostName_Type()
)
sleV2Dhcp4ClientIfHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfHostName.setStatus("current")


class _SleV2Dhcp4ClientIfRequestFlag_Type(Bits):
    """Custom type sleV2Dhcp4ClientIfRequestFlag based on Bits"""
    namedValues = NamedValues(
        *(("unused0", 0),
          ("subnetMask", 1),
          ("timeOffset", 2),
          ("router", 3),
          ("timeServer", 4),
          ("nameServer", 5),
          ("domainNameServer", 6),
          ("logServer", 7),
          ("cookieServer", 8),
          ("lprServer", 9),
          ("impressServer", 10),
          ("resourceLocationServer", 11),
          ("hostName", 12),
          ("bootFileSize", 13),
          ("meritFile", 14),
          ("domainName", 15),
          ("swapServer", 16),
          ("rootPath", 17),
          ("extensionsPath", 18),
          ("ipForwardState", 19),
          ("nonLocalSourceRoutingState", 20),
          ("policyFilter", 21),
          ("maximumDatagramReassemblySize", 22),
          ("defaultIpTimeToLive", 23),
          ("pathMtuAgingTimeout", 24),
          ("pathMtuPlateauTable", 25),
          ("interfaceMtu", 26),
          ("allSubnetsAreLocal", 27),
          ("broadcastAddress", 28),
          ("performMaskDiscovery", 29),
          ("maskSupplier", 30),
          ("performRouterDiscovery", 31),
          ("routerSolicitationAddress", 32),
          ("staticRoute", 33),
          ("trailerEncapsulation", 34),
          ("arpCacheTimeout", 35),
          ("ethernetEncapsulationOption", 36),
          ("tcpDefaultTtl", 37),
          ("tcpKeepaliveInterval", 38),
          ("tcpKeepaliveGarbage", 39),
          ("nisDomain", 40),
          ("nisServers", 41),
          ("networkTimeProtocolServers", 42),
          ("vendorSpecificInformation", 43),
          ("netbiosOverTcpIpNameServer", 44),
          ("netbiosOverTcpIpDatagramDistributionServer", 45),
          ("netbiosOverTcpIpNodeType", 46),
          ("netbiosOverTcpIpScope", 47),
          ("xWindowSystemFontServer", 48),
          ("xWindowSystemDisplayManager", 49),
          ("requestedIpAddress", 50),
          ("ipAddressLeaseTime", 51),
          ("optionOverload", 52),
          ("dhcpMessageType", 53),
          ("serverIdentifier", 54),
          ("unused55", 55),
          ("message", 56),
          ("maximumDhcpMessageSize", 57),
          ("renewalTimeValue", 58),
          ("rebindingTimeValue", 59),
          ("vendorClassIdentifier", 60),
          ("clientIdentifier", 61),
          ("undefined62", 62),
          ("undefined63", 63),
          ("nisPlusDomain", 64),
          ("nisPlusServers", 65),
          ("tftpServerName", 66),
          ("bootFileName", 67),
          ("mobileIpHomeAgent", 68),
          ("smtpServer", 69),
          ("pop3Server", 70),
          ("nntpServer", 71),
          ("wwwServer", 72),
          ("defaultFingerServer", 73),
          ("ircServer", 74),
          ("streetTalkServer", 75),
          ("stdaServer", 76))
    )

_SleV2Dhcp4ClientIfRequestFlag_Type.__name__ = "Bits"
_SleV2Dhcp4ClientIfRequestFlag_Object = MibTableColumn
sleV2Dhcp4ClientIfRequestFlag = _SleV2Dhcp4ClientIfRequestFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1, 1, 7),
    _SleV2Dhcp4ClientIfRequestFlag_Type()
)
sleV2Dhcp4ClientIfRequestFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfRequestFlag.setStatus("current")


class _SleV2Dhcp4ClientIfClientType_Type(Integer32):
    """Custom type sleV2Dhcp4ClientIfClientType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("text", 0),
          ("hex", 1))
    )


_SleV2Dhcp4ClientIfClientType_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientIfClientType_Object = MibTableColumn
sleV2Dhcp4ClientIfClientType = _SleV2Dhcp4ClientIfClientType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1, 1, 8),
    _SleV2Dhcp4ClientIfClientType_Type()
)
sleV2Dhcp4ClientIfClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfClientType.setStatus("current")


class _SleV2Dhcp4ClientIfClientId_Type(OctetString):
    """Custom type sleV2Dhcp4ClientIfClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4ClientIfClientId_Type.__name__ = "OctetString"
_SleV2Dhcp4ClientIfClientId_Object = MibTableColumn
sleV2Dhcp4ClientIfClientId = _SleV2Dhcp4ClientIfClientId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1, 1, 9),
    _SleV2Dhcp4ClientIfClientId_Type()
)
sleV2Dhcp4ClientIfClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfClientId.setStatus("current")


class _SleV2Dhcp4ClientIfClassType_Type(Integer32):
    """Custom type sleV2Dhcp4ClientIfClassType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("text", 0),
          ("hex", 1))
    )


_SleV2Dhcp4ClientIfClassType_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientIfClassType_Object = MibTableColumn
sleV2Dhcp4ClientIfClassType = _SleV2Dhcp4ClientIfClassType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1, 1, 10),
    _SleV2Dhcp4ClientIfClassType_Type()
)
sleV2Dhcp4ClientIfClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfClassType.setStatus("current")


class _SleV2Dhcp4ClientIfClassId_Type(OctetString):
    """Custom type sleV2Dhcp4ClientIfClassId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4ClientIfClassId_Type.__name__ = "OctetString"
_SleV2Dhcp4ClientIfClassId_Object = MibTableColumn
sleV2Dhcp4ClientIfClassId = _SleV2Dhcp4ClientIfClassId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1, 1, 11),
    _SleV2Dhcp4ClientIfClassId_Type()
)
sleV2Dhcp4ClientIfClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfClassId.setStatus("current")


class _SleV2Dhcp4ClientIfLeasetime_Type(Integer32):
    """Custom type sleV2Dhcp4ClientIfLeasetime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 2147483637),
    )


_SleV2Dhcp4ClientIfLeasetime_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientIfLeasetime_Object = MibTableColumn
sleV2Dhcp4ClientIfLeasetime = _SleV2Dhcp4ClientIfLeasetime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1, 1, 12),
    _SleV2Dhcp4ClientIfLeasetime_Type()
)
sleV2Dhcp4ClientIfLeasetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfLeasetime.setStatus("current")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfLeasetime.setUnits("second")
_SleV2Dhcp4ClientIfExpired_Type = Unsigned32
_SleV2Dhcp4ClientIfExpired_Object = MibTableColumn
sleV2Dhcp4ClientIfExpired = _SleV2Dhcp4ClientIfExpired_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1, 1, 13),
    _SleV2Dhcp4ClientIfExpired_Type()
)
sleV2Dhcp4ClientIfExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfExpired.setStatus("current")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfExpired.setUnits("second")


class _SleV2Dhcp4ClientIfState_Type(Integer32):
    """Custom type sleV2Dhcp4ClientIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("halt", 0),
          ("init", 1),
          ("request", 3),
          ("bound", 4),
          ("renew", 5),
          ("rebind", 6),
          ("nonactive", 255))
    )


_SleV2Dhcp4ClientIfState_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientIfState_Object = MibTableColumn
sleV2Dhcp4ClientIfState = _SleV2Dhcp4ClientIfState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1, 1, 14),
    _SleV2Dhcp4ClientIfState_Type()
)
sleV2Dhcp4ClientIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfState.setStatus("current")


class _SleV2Dhcp4ClientIfLeasetimeOption_Type(Integer32):
    """Custom type sleV2Dhcp4ClientIfLeasetimeOption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("used", 1))
    )


_SleV2Dhcp4ClientIfLeasetimeOption_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientIfLeasetimeOption_Object = MibTableColumn
sleV2Dhcp4ClientIfLeasetimeOption = _SleV2Dhcp4ClientIfLeasetimeOption_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 1, 1, 15),
    _SleV2Dhcp4ClientIfLeasetimeOption_Type()
)
sleV2Dhcp4ClientIfLeasetimeOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfLeasetimeOption.setStatus("current")
_SleV2Dhcp4ClientIfControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4ClientIfControl = _SleV2Dhcp4ClientIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 2)
)


class _SleV2Dhcp4ClientIfControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4ClientIfControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("setDhcpClientActivity", 1),
          ("setDhcpClientProfile", 2),
          ("renewDhcpClientAddress", 3),
          ("releaseDhcpClientAddress", 4),
          ("setDhcpClientLeasetimeOption", 5))
    )


_SleV2Dhcp4ClientIfControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientIfControlRequest_Object = MibScalar
sleV2Dhcp4ClientIfControlRequest = _SleV2Dhcp4ClientIfControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 2, 1),
    _SleV2Dhcp4ClientIfControlRequest_Type()
)
sleV2Dhcp4ClientIfControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfControlRequest.setStatus("current")
_SleV2Dhcp4ClientIfControlStatus_Type = SleControlStatusType
_SleV2Dhcp4ClientIfControlStatus_Object = MibScalar
sleV2Dhcp4ClientIfControlStatus = _SleV2Dhcp4ClientIfControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 2, 2),
    _SleV2Dhcp4ClientIfControlStatus_Type()
)
sleV2Dhcp4ClientIfControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfControlStatus.setStatus("current")
_SleV2Dhcp4ClientIfControlTimer_Type = Gauge32
_SleV2Dhcp4ClientIfControlTimer_Object = MibScalar
sleV2Dhcp4ClientIfControlTimer = _SleV2Dhcp4ClientIfControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 2, 3),
    _SleV2Dhcp4ClientIfControlTimer_Type()
)
sleV2Dhcp4ClientIfControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfControlTimer.setStatus("current")
_SleV2Dhcp4ClientIfControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4ClientIfControlTimeStamp_Object = MibScalar
sleV2Dhcp4ClientIfControlTimeStamp = _SleV2Dhcp4ClientIfControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 2, 4),
    _SleV2Dhcp4ClientIfControlTimeStamp_Type()
)
sleV2Dhcp4ClientIfControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfControlTimeStamp.setStatus("current")
_SleV2Dhcp4ClientIfControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4ClientIfControlReqResult_Object = MibScalar
sleV2Dhcp4ClientIfControlReqResult = _SleV2Dhcp4ClientIfControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 2, 5),
    _SleV2Dhcp4ClientIfControlReqResult_Type()
)
sleV2Dhcp4ClientIfControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfControlReqResult.setStatus("current")


class _SleV2Dhcp4ClientIfControlIndex_Type(Integer32):
    """Custom type sleV2Dhcp4ClientIfControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleV2Dhcp4ClientIfControlIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientIfControlIndex_Object = MibScalar
sleV2Dhcp4ClientIfControlIndex = _SleV2Dhcp4ClientIfControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 2, 6),
    _SleV2Dhcp4ClientIfControlIndex_Type()
)
sleV2Dhcp4ClientIfControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfControlIndex.setStatus("current")


class _SleV2Dhcp4ClientIfControlActivity_Type(Integer32):
    """Custom type sleV2Dhcp4ClientIfControlActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2Dhcp4ClientIfControlActivity_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientIfControlActivity_Object = MibScalar
sleV2Dhcp4ClientIfControlActivity = _SleV2Dhcp4ClientIfControlActivity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 2, 7),
    _SleV2Dhcp4ClientIfControlActivity_Type()
)
sleV2Dhcp4ClientIfControlActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfControlActivity.setStatus("current")


class _SleV2Dhcp4ClientIfControlHostName_Type(OctetString):
    """Custom type sleV2Dhcp4ClientIfControlHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4ClientIfControlHostName_Type.__name__ = "OctetString"
_SleV2Dhcp4ClientIfControlHostName_Object = MibScalar
sleV2Dhcp4ClientIfControlHostName = _SleV2Dhcp4ClientIfControlHostName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 2, 8),
    _SleV2Dhcp4ClientIfControlHostName_Type()
)
sleV2Dhcp4ClientIfControlHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfControlHostName.setStatus("current")


class _SleV2Dhcp4ClientIfControlRequestFlag_Type(Bits):
    """Custom type sleV2Dhcp4ClientIfControlRequestFlag based on Bits"""
    namedValues = NamedValues(
        *(("unused0", 0),
          ("subnetMask", 1),
          ("timeOffset", 2),
          ("router", 3),
          ("timeServer", 4),
          ("nameServer", 5),
          ("domainNameServer", 6),
          ("logServer", 7),
          ("cookieServer", 8),
          ("lprServer", 9),
          ("impressServer", 10),
          ("resourceLocationServer", 11),
          ("hostName", 12),
          ("bootFileSize", 13),
          ("meritFile", 14),
          ("domainName", 15),
          ("swapServer", 16),
          ("rootPath", 17),
          ("extensionsPath", 18),
          ("ipForwardState", 19),
          ("nonLocalSourceRoutingState", 20),
          ("policyFilter", 21),
          ("maximumDatagramReassemblySize", 22),
          ("defaultIpTimeToLive", 23),
          ("pathMtuAgingTimeout", 24),
          ("pathMtuPlateauTable", 25),
          ("interfaceMtu", 26),
          ("allSubnetsAreLocal", 27),
          ("broadcastAddress", 28),
          ("performMaskDiscovery", 29),
          ("maskSupplier", 30),
          ("performRouterDiscovery", 31),
          ("routerSolicitationAddress", 32),
          ("staticRoute", 33),
          ("trailerEncapsulation", 34),
          ("arpCacheTimeout", 35),
          ("ethernetEncapsulationOption", 36),
          ("tcpDefaultTtl", 37),
          ("tcpKeepaliveInterval", 38),
          ("tcpKeepaliveGarbage", 39),
          ("nisDomain", 40),
          ("nisServers", 41),
          ("networkTimeProtocolServers", 42),
          ("vendorSpecificInformation", 43),
          ("netbiosOverTcpIpNameServer", 44),
          ("netbiosOverTcpIpDatagramDistributionServer", 45),
          ("netbiosOverTcpIpNodeType", 46),
          ("netbiosOverTcpIpScope", 47),
          ("xWindowSystemFontServer", 48),
          ("xWindowSystemDisplayManager", 49),
          ("requestedIpAddress", 50),
          ("ipAddressLeaseTime", 51),
          ("optionOverload", 52),
          ("dhcpMessageType", 53),
          ("serverIdentifier", 54),
          ("unused55", 55),
          ("message", 56),
          ("maximumDhcpMessageSize", 57),
          ("renewalTimeValue", 58),
          ("rebindingTimeValue", 59),
          ("vendorClassIdentifier", 60),
          ("clientIdentifier", 61),
          ("undefined62", 62),
          ("undefined63", 63),
          ("nisPlusDomain", 64),
          ("nisPlusServers", 65),
          ("tftpServerName", 66),
          ("bootFileName", 67),
          ("mobileIpHomeAgent", 68),
          ("smtpServer", 69),
          ("pop3Server", 70),
          ("nntpServer", 71),
          ("wwwServer", 72),
          ("defaultFingerServer", 73),
          ("ircServer", 74),
          ("streetTalkServer", 75),
          ("stdaServer", 76))
    )

_SleV2Dhcp4ClientIfControlRequestFlag_Type.__name__ = "Bits"
_SleV2Dhcp4ClientIfControlRequestFlag_Object = MibScalar
sleV2Dhcp4ClientIfControlRequestFlag = _SleV2Dhcp4ClientIfControlRequestFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 2, 9),
    _SleV2Dhcp4ClientIfControlRequestFlag_Type()
)
sleV2Dhcp4ClientIfControlRequestFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfControlRequestFlag.setStatus("current")


class _SleV2Dhcp4ClientIfControlClientType_Type(Integer32):
    """Custom type sleV2Dhcp4ClientIfControlClientType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("text", 0),
          ("hex", 1))
    )


_SleV2Dhcp4ClientIfControlClientType_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientIfControlClientType_Object = MibScalar
sleV2Dhcp4ClientIfControlClientType = _SleV2Dhcp4ClientIfControlClientType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 2, 10),
    _SleV2Dhcp4ClientIfControlClientType_Type()
)
sleV2Dhcp4ClientIfControlClientType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfControlClientType.setStatus("current")


class _SleV2Dhcp4ClientIfControlClientId_Type(OctetString):
    """Custom type sleV2Dhcp4ClientIfControlClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4ClientIfControlClientId_Type.__name__ = "OctetString"
_SleV2Dhcp4ClientIfControlClientId_Object = MibScalar
sleV2Dhcp4ClientIfControlClientId = _SleV2Dhcp4ClientIfControlClientId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 2, 11),
    _SleV2Dhcp4ClientIfControlClientId_Type()
)
sleV2Dhcp4ClientIfControlClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfControlClientId.setStatus("current")


class _SleV2Dhcp4ClientIfControlClassType_Type(Integer32):
    """Custom type sleV2Dhcp4ClientIfControlClassType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("text", 0),
          ("hex", 1))
    )


_SleV2Dhcp4ClientIfControlClassType_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientIfControlClassType_Object = MibScalar
sleV2Dhcp4ClientIfControlClassType = _SleV2Dhcp4ClientIfControlClassType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 2, 12),
    _SleV2Dhcp4ClientIfControlClassType_Type()
)
sleV2Dhcp4ClientIfControlClassType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfControlClassType.setStatus("current")


class _SleV2Dhcp4ClientIfControlClassId_Type(OctetString):
    """Custom type sleV2Dhcp4ClientIfControlClassId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4ClientIfControlClassId_Type.__name__ = "OctetString"
_SleV2Dhcp4ClientIfControlClassId_Object = MibScalar
sleV2Dhcp4ClientIfControlClassId = _SleV2Dhcp4ClientIfControlClassId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 2, 13),
    _SleV2Dhcp4ClientIfControlClassId_Type()
)
sleV2Dhcp4ClientIfControlClassId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfControlClassId.setStatus("current")


class _SleV2Dhcp4ClientIfControlLeasetime_Type(Integer32):
    """Custom type sleV2Dhcp4ClientIfControlLeasetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 2147483637),
    )


_SleV2Dhcp4ClientIfControlLeasetime_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientIfControlLeasetime_Object = MibScalar
sleV2Dhcp4ClientIfControlLeasetime = _SleV2Dhcp4ClientIfControlLeasetime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 2, 14),
    _SleV2Dhcp4ClientIfControlLeasetime_Type()
)
sleV2Dhcp4ClientIfControlLeasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfControlLeasetime.setStatus("current")


class _SleV2Dhcp4ClientIfControlLeasetimeOption_Type(Integer32):
    """Custom type sleV2Dhcp4ClientIfControlLeasetimeOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("used", 1))
    )


_SleV2Dhcp4ClientIfControlLeasetimeOption_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientIfControlLeasetimeOption_Object = MibScalar
sleV2Dhcp4ClientIfControlLeasetimeOption = _SleV2Dhcp4ClientIfControlLeasetimeOption_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 2, 15),
    _SleV2Dhcp4ClientIfControlLeasetimeOption_Type()
)
sleV2Dhcp4ClientIfControlLeasetimeOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfControlLeasetimeOption.setStatus("current")
_SleV2Dhcp4ClientIfNotification_ObjectIdentity = ObjectIdentity
sleV2Dhcp4ClientIfNotification = _SleV2Dhcp4ClientIfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 3)
)
_SleV2Dhcp4ClientOption_ObjectIdentity = ObjectIdentity
sleV2Dhcp4ClientOption = _SleV2Dhcp4ClientOption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 2)
)
_SleV2Dhcp4ClientOptionTable_Object = MibTable
sleV2Dhcp4ClientOptionTable = _SleV2Dhcp4ClientOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientOptionTable.setStatus("current")
_SleV2Dhcp4ClientOptionEntry_Object = MibTableRow
sleV2Dhcp4ClientOptionEntry = _SleV2Dhcp4ClientOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 2, 1, 1)
)
sleV2Dhcp4ClientOptionEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4OptionCode"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4OptionInstance"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientOptionEntry.setStatus("current")


class _SleV2Dhcp4ClientOptionCode_Type(Integer32):
    """Custom type sleV2Dhcp4ClientOptionCode based on Integer32"""
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
              38,
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
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76)
        )
    )
    namedValues = NamedValues(
        *(("subnetMask", 1),
          ("timeOffset", 2),
          ("router", 3),
          ("timeServer", 4),
          ("nameServer", 5),
          ("domainNameServer", 6),
          ("logServer", 7),
          ("cookieServer", 8),
          ("lprServer", 9),
          ("impressServer", 10),
          ("resourceLocationServer", 11),
          ("hostName", 12),
          ("bootFileSize", 13),
          ("meritFile", 14),
          ("domainName", 15),
          ("swapServer", 16),
          ("rootPath", 17),
          ("extensionsPath", 18),
          ("ipForwardState", 19),
          ("nonLocalSourceRoutingState", 20),
          ("policyFilter", 21),
          ("maximumDatagramReassemblySize", 22),
          ("defaultIpTimeToLive", 23),
          ("pathMtuAgingTimeout", 24),
          ("pathMtuPlateauTable", 25),
          ("interfaceMtu", 26),
          ("allSubnetsAreLocal", 27),
          ("broadcastAddress", 28),
          ("performMaskDiscovery", 29),
          ("maskSupplier", 30),
          ("performRouterDiscovery", 31),
          ("routerSolicitationAddress", 32),
          ("staticRoute", 33),
          ("trailerEncapsulation", 34),
          ("arpCacheTimeout", 35),
          ("ethernetEncapsulationOption", 36),
          ("tcpDefaultTtl", 37),
          ("tcpKeepaliveInterval", 38),
          ("tcpKeepaliveGarbage", 39),
          ("nisDomain", 40),
          ("nisServers", 41),
          ("networkTimeProtocolServers", 42),
          ("vendorSpecificInformation", 43),
          ("netbiosOverTcpIpNameServer", 44),
          ("netbiosOverTcpIpDatagramDistributionServer", 45),
          ("netbiosOverTcpIpNodeType", 46),
          ("netbiosOverTcpIpScope", 47),
          ("xWindowSystemFontServer", 48),
          ("xWindowSystemDisplayManager", 49),
          ("requestedIpAddress", 50),
          ("ipAddressLeaseTime", 51),
          ("optionOverload", 52),
          ("dhcpMessageType", 53),
          ("serverIdentifier", 54),
          ("parameterRequestList", 55),
          ("message", 56),
          ("maximumDhcpMessageSize", 57),
          ("renewalTimeValue", 58),
          ("rebindingTimeValue", 59),
          ("vendorClassIdentifier", 60),
          ("clientIdentifier", 61),
          ("nisPlusDomain", 64),
          ("nisPlusServers", 65),
          ("tftpServerName", 66),
          ("bootFileName", 67),
          ("mobileIpHomeAgent", 68),
          ("smtpServer", 69),
          ("pop3Server", 70),
          ("nntpServer", 71),
          ("wwwServer", 72),
          ("defaultFingerServer", 73),
          ("ircServer", 74),
          ("streetTalkServer", 75),
          ("stdaServer", 76))
    )


_SleV2Dhcp4ClientOptionCode_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientOptionCode_Object = MibTableColumn
sleV2Dhcp4ClientOptionCode = _SleV2Dhcp4ClientOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 2, 1, 1, 1),
    _SleV2Dhcp4ClientOptionCode_Type()
)
sleV2Dhcp4ClientOptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientOptionCode.setStatus("current")


class _SleV2Dhcp4ClientOptionInstance_Type(Integer32):
    """Custom type sleV2Dhcp4ClientOptionInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleV2Dhcp4ClientOptionInstance_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientOptionInstance_Object = MibTableColumn
sleV2Dhcp4ClientOptionInstance = _SleV2Dhcp4ClientOptionInstance_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 2, 1, 1, 2),
    _SleV2Dhcp4ClientOptionInstance_Type()
)
sleV2Dhcp4ClientOptionInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientOptionInstance.setStatus("current")


class _SleV2Dhcp4ClientOptionType_Type(Integer32):
    """Custom type sleV2Dhcp4ClientOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipaddress", 1),
          ("hex", 2),
          ("text", 3))
    )


_SleV2Dhcp4ClientOptionType_Type.__name__ = "Integer32"
_SleV2Dhcp4ClientOptionType_Object = MibTableColumn
sleV2Dhcp4ClientOptionType = _SleV2Dhcp4ClientOptionType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 2, 1, 1, 3),
    _SleV2Dhcp4ClientOptionType_Type()
)
sleV2Dhcp4ClientOptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientOptionType.setStatus("current")


class _SleV2Dhcp4ClientOptionValue_Type(OctetString):
    """Custom type sleV2Dhcp4ClientOptionValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4ClientOptionValue_Type.__name__ = "OctetString"
_SleV2Dhcp4ClientOptionValue_Object = MibTableColumn
sleV2Dhcp4ClientOptionValue = _SleV2Dhcp4ClientOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 2, 1, 1, 4),
    _SleV2Dhcp4ClientOptionValue_Type()
)
sleV2Dhcp4ClientOptionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientOptionValue.setStatus("current")
_SleV2Dhcp4Port_ObjectIdentity = ObjectIdentity
sleV2Dhcp4Port = _SleV2Dhcp4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9)
)
_SleV2Dhcp4PortLease_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PortLease = _SleV2Dhcp4PortLease_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1)
)
_SleV2Dhcp4PortLeaseTable_Object = MibTable
sleV2Dhcp4PortLeaseTable = _SleV2Dhcp4PortLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PortLeaseTable.setStatus("current")
_SleV2Dhcp4PortLeaseEntry_Object = MibTableRow
sleV2Dhcp4PortLeaseEntry = _SleV2Dhcp4PortLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 1, 1)
)
sleV2Dhcp4PortLeaseEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PortLeaseIndex"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PortLeaseEntry.setStatus("current")
_SleV2Dhcp4PortLeaseIndex_Type = InterfaceIndex
_SleV2Dhcp4PortLeaseIndex_Object = MibTableColumn
sleV2Dhcp4PortLeaseIndex = _SleV2Dhcp4PortLeaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 1, 1, 1),
    _SleV2Dhcp4PortLeaseIndex_Type()
)
sleV2Dhcp4PortLeaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortLeaseIndex.setStatus("current")


class _SleV2Dhcp4PortLeaseLimit_Type(Integer32):
    """Custom type sleV2Dhcp4PortLeaseLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 256),
    )


_SleV2Dhcp4PortLeaseLimit_Type.__name__ = "Integer32"
_SleV2Dhcp4PortLeaseLimit_Object = MibTableColumn
sleV2Dhcp4PortLeaseLimit = _SleV2Dhcp4PortLeaseLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 1, 1, 2),
    _SleV2Dhcp4PortLeaseLimit_Type()
)
sleV2Dhcp4PortLeaseLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortLeaseLimit.setStatus("current")
_SleV2Dhcp4PortLeaseCount_Type = Integer32
_SleV2Dhcp4PortLeaseCount_Object = MibTableColumn
sleV2Dhcp4PortLeaseCount = _SleV2Dhcp4PortLeaseCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 1, 1, 3),
    _SleV2Dhcp4PortLeaseCount_Type()
)
sleV2Dhcp4PortLeaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortLeaseCount.setStatus("current")
_SleV2Dhcp4PortAddrLeaseTable_Object = MibTable
sleV2Dhcp4PortAddrLeaseTable = _SleV2Dhcp4PortAddrLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 2)
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PortAddrLeaseTable.setStatus("current")
_SleV2Dhcp4PortAddrLeaseEntry_Object = MibTableRow
sleV2Dhcp4PortAddrLeaseEntry = _SleV2Dhcp4PortAddrLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 2, 1)
)
sleV2Dhcp4PortAddrLeaseEntry.setIndexNames(
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PortAddrtLeaseIndex"),
    (0, "SLEV2-DHCP-MIB", "sleV2Dhcp4PortAddrLeaseAddress"),
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PortAddrLeaseEntry.setStatus("current")
_SleV2Dhcp4PortAddrtLeaseIndex_Type = InterfaceIndex
_SleV2Dhcp4PortAddrtLeaseIndex_Object = MibTableColumn
sleV2Dhcp4PortAddrtLeaseIndex = _SleV2Dhcp4PortAddrtLeaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 2, 1, 1),
    _SleV2Dhcp4PortAddrtLeaseIndex_Type()
)
sleV2Dhcp4PortAddrtLeaseIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortAddrtLeaseIndex.setStatus("current")
_SleV2Dhcp4PortAddrLeaseAddress_Type = IpAddress
_SleV2Dhcp4PortAddrLeaseAddress_Object = MibTableColumn
sleV2Dhcp4PortAddrLeaseAddress = _SleV2Dhcp4PortAddrLeaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 2, 1, 2),
    _SleV2Dhcp4PortAddrLeaseAddress_Type()
)
sleV2Dhcp4PortAddrLeaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortAddrLeaseAddress.setStatus("current")


class _SleV2Dhcp4PortAddrLeasePoolIndex_Type(Integer32):
    """Custom type sleV2Dhcp4PortAddrLeasePoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2Dhcp4PortAddrLeasePoolIndex_Type.__name__ = "Integer32"
_SleV2Dhcp4PortAddrLeasePoolIndex_Object = MibTableColumn
sleV2Dhcp4PortAddrLeasePoolIndex = _SleV2Dhcp4PortAddrLeasePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 2, 1, 3),
    _SleV2Dhcp4PortAddrLeasePoolIndex_Type()
)
sleV2Dhcp4PortAddrLeasePoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortAddrLeasePoolIndex.setStatus("current")


class _SleV2Dhcp4PortAddrLeaseStatus_Type(Integer32):
    """Custom type sleV2Dhcp4PortAddrLeaseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("offered", 2),
          ("bound", 3),
          ("abandon", 4),
          ("free", 5))
    )


_SleV2Dhcp4PortAddrLeaseStatus_Type.__name__ = "Integer32"
_SleV2Dhcp4PortAddrLeaseStatus_Object = MibTableColumn
sleV2Dhcp4PortAddrLeaseStatus = _SleV2Dhcp4PortAddrLeaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 2, 1, 4),
    _SleV2Dhcp4PortAddrLeaseStatus_Type()
)
sleV2Dhcp4PortAddrLeaseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortAddrLeaseStatus.setStatus("current")
_SleV2Dhcp4PortAddrLeaseMac_Type = MacAddress
_SleV2Dhcp4PortAddrLeaseMac_Object = MibTableColumn
sleV2Dhcp4PortAddrLeaseMac = _SleV2Dhcp4PortAddrLeaseMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 2, 1, 5),
    _SleV2Dhcp4PortAddrLeaseMac_Type()
)
sleV2Dhcp4PortAddrLeaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortAddrLeaseMac.setStatus("current")


class _SleV2Dhcp4PortAddrLeaseHostName_Type(OctetString):
    """Custom type sleV2Dhcp4PortAddrLeaseHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4PortAddrLeaseHostName_Type.__name__ = "OctetString"
_SleV2Dhcp4PortAddrLeaseHostName_Object = MibTableColumn
sleV2Dhcp4PortAddrLeaseHostName = _SleV2Dhcp4PortAddrLeaseHostName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 2, 1, 6),
    _SleV2Dhcp4PortAddrLeaseHostName_Type()
)
sleV2Dhcp4PortAddrLeaseHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortAddrLeaseHostName.setStatus("current")


class _SleV2Dhcp4PortAddrLeaseClientId_Type(OctetString):
    """Custom type sleV2Dhcp4PortAddrLeaseClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SleV2Dhcp4PortAddrLeaseClientId_Type.__name__ = "OctetString"
_SleV2Dhcp4PortAddrLeaseClientId_Object = MibTableColumn
sleV2Dhcp4PortAddrLeaseClientId = _SleV2Dhcp4PortAddrLeaseClientId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 2, 1, 7),
    _SleV2Dhcp4PortAddrLeaseClientId_Type()
)
sleV2Dhcp4PortAddrLeaseClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortAddrLeaseClientId.setStatus("current")


class _SleV2Dhcp4PortAddrLeaseRemoteId_Type(OctetString):
    """Custom type sleV2Dhcp4PortAddrLeaseRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4PortAddrLeaseRemoteId_Type.__name__ = "OctetString"
_SleV2Dhcp4PortAddrLeaseRemoteId_Object = MibTableColumn
sleV2Dhcp4PortAddrLeaseRemoteId = _SleV2Dhcp4PortAddrLeaseRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 2, 1, 8),
    _SleV2Dhcp4PortAddrLeaseRemoteId_Type()
)
sleV2Dhcp4PortAddrLeaseRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortAddrLeaseRemoteId.setStatus("current")


class _SleV2Dhcp4PortAddrLeaseCircuitId_Type(OctetString):
    """Custom type sleV2Dhcp4PortAddrLeaseCircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_SleV2Dhcp4PortAddrLeaseCircuitId_Type.__name__ = "OctetString"
_SleV2Dhcp4PortAddrLeaseCircuitId_Object = MibTableColumn
sleV2Dhcp4PortAddrLeaseCircuitId = _SleV2Dhcp4PortAddrLeaseCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 2, 1, 9),
    _SleV2Dhcp4PortAddrLeaseCircuitId_Type()
)
sleV2Dhcp4PortAddrLeaseCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortAddrLeaseCircuitId.setStatus("current")
_SleV2Dhcp4PortAddrLeaseStartTime_Type = Unsigned32
_SleV2Dhcp4PortAddrLeaseStartTime_Object = MibTableColumn
sleV2Dhcp4PortAddrLeaseStartTime = _SleV2Dhcp4PortAddrLeaseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 2, 1, 10),
    _SleV2Dhcp4PortAddrLeaseStartTime_Type()
)
sleV2Dhcp4PortAddrLeaseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortAddrLeaseStartTime.setStatus("current")
_SleV2Dhcp4PortAddrLeaseFinishTime_Type = Unsigned32
_SleV2Dhcp4PortAddrLeaseFinishTime_Object = MibTableColumn
sleV2Dhcp4PortAddrLeaseFinishTime = _SleV2Dhcp4PortAddrLeaseFinishTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 2, 1, 11),
    _SleV2Dhcp4PortAddrLeaseFinishTime_Type()
)
sleV2Dhcp4PortAddrLeaseFinishTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortAddrLeaseFinishTime.setStatus("current")
_SleV2Dhcp4PortLeaseControl_ObjectIdentity = ObjectIdentity
sleV2Dhcp4PortLeaseControl = _SleV2Dhcp4PortLeaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 3)
)


class _SleV2Dhcp4PortLeaseControlRequest_Type(Integer32):
    """Custom type sleV2Dhcp4PortLeaseControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setDhcp4PortLeaseLimit", 1)
    )


_SleV2Dhcp4PortLeaseControlRequest_Type.__name__ = "Integer32"
_SleV2Dhcp4PortLeaseControlRequest_Object = MibScalar
sleV2Dhcp4PortLeaseControlRequest = _SleV2Dhcp4PortLeaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 3, 1),
    _SleV2Dhcp4PortLeaseControlRequest_Type()
)
sleV2Dhcp4PortLeaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortLeaseControlRequest.setStatus("current")
_SleV2Dhcp4PortLeaseControlStatus_Type = SleControlStatusType
_SleV2Dhcp4PortLeaseControlStatus_Object = MibScalar
sleV2Dhcp4PortLeaseControlStatus = _SleV2Dhcp4PortLeaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 3, 2),
    _SleV2Dhcp4PortLeaseControlStatus_Type()
)
sleV2Dhcp4PortLeaseControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortLeaseControlStatus.setStatus("current")
_SleV2Dhcp4PortLeaseControlTimer_Type = Gauge32
_SleV2Dhcp4PortLeaseControlTimer_Object = MibScalar
sleV2Dhcp4PortLeaseControlTimer = _SleV2Dhcp4PortLeaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 3, 3),
    _SleV2Dhcp4PortLeaseControlTimer_Type()
)
sleV2Dhcp4PortLeaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortLeaseControlTimer.setStatus("current")
_SleV2Dhcp4PortLeaseControlTimeStamp_Type = TimeTicks
_SleV2Dhcp4PortLeaseControlTimeStamp_Object = MibScalar
sleV2Dhcp4PortLeaseControlTimeStamp = _SleV2Dhcp4PortLeaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 3, 4),
    _SleV2Dhcp4PortLeaseControlTimeStamp_Type()
)
sleV2Dhcp4PortLeaseControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortLeaseControlTimeStamp.setStatus("current")
_SleV2Dhcp4PortLeaseControlReqResult_Type = SleControlRequestResultType
_SleV2Dhcp4PortLeaseControlReqResult_Object = MibScalar
sleV2Dhcp4PortLeaseControlReqResult = _SleV2Dhcp4PortLeaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 3, 5),
    _SleV2Dhcp4PortLeaseControlReqResult_Type()
)
sleV2Dhcp4PortLeaseControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortLeaseControlReqResult.setStatus("current")
_SleV2Dhcp4PortLeaseControlIndex_Type = InterfaceIndex
_SleV2Dhcp4PortLeaseControlIndex_Object = MibScalar
sleV2Dhcp4PortLeaseControlIndex = _SleV2Dhcp4PortLeaseControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 3, 6),
    _SleV2Dhcp4PortLeaseControlIndex_Type()
)
sleV2Dhcp4PortLeaseControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortLeaseControlIndex.setStatus("current")


class _SleV2Dhcp4PortLeaseControlLimit_Type(Integer32):
    """Custom type sleV2Dhcp4PortLeaseControlLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 256),
    )


_SleV2Dhcp4PortLeaseControlLimit_Type.__name__ = "Integer32"
_SleV2Dhcp4PortLeaseControlLimit_Object = MibScalar
sleV2Dhcp4PortLeaseControlLimit = _SleV2Dhcp4PortLeaseControlLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 3, 7),
    _SleV2Dhcp4PortLeaseControlLimit_Type()
)
sleV2Dhcp4PortLeaseControlLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2Dhcp4PortLeaseControlLimit.setStatus("current")
_SleV2DhcpPortLeaseNotification_ObjectIdentity = ObjectIdentity
sleV2DhcpPortLeaseNotification = _SleV2DhcpPortLeaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 4)
)
_SleV2Dhcp6_ObjectIdentity = ObjectIdentity
sleV2Dhcp6 = _SleV2Dhcp6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 3)
)

# Managed Objects groups

sleV2DhcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 4)
)
sleV2DhcpGroup.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeEnd"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlEnd"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlIfIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DatabaseURL"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DatabaseInterval"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PingTimeout"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82Policy"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82SystemRemoteId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlDatabaseURL"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlDatabaseInterval"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlPingTimeout"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlOption82Policy"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlOption82SystemRemoteId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolDefaultLeaseTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolMaxLeaseTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolDomainName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolSummaryTotal"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolSummaryAllocated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolSummaryBound"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolSummaryOffered"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolSummaryFixed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolSummaryAbandon"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolSummaryAvailable"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlDefaultLeaseTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlMaxLeaseTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlDomainName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlOriginURL"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlOriginFileName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkMask"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlMask"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeEnd"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlEnd"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedMac"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsControlIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayControlIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionCode"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionInstance"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionValue"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlCode"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlInstance"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlValue"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82TrustDefault"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterPortControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterPortControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterPortControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterPortControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterPortControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterPortControlIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressMac"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlMac"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsReceived"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsSent"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsReceivedErrors"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsSentErrors"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsBootpReceivedRequests"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsBootpReceivedReplies"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsBootpSentRequests"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsBootpSentReplies"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsReceivedDiscover"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsReceivedRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsReceivedRelease"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatscReceivedInform"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsReceivedDecline"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsSentOffer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsSentAck"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsSentNak"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DatabaseKey"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DebugStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4AuthArpTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4AuthArpLeft"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4SummaryPoolCnt"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4SummaryTotal"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4SummaryAvailable"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4SummaryAbandon"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4SummaryBound"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4SummaryOffered"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4SummaryFixed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlDatabaseKey"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlDebugStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4IllegalMac"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4IllegalTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4IllegalControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4IllegalControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4IllegalControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4IllegalControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4IllegalControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassControlName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlOption82TrustDefault"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlMac"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ServiceActivity"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassUsage"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4SmartRelayUsage"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82Usage"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlClassUsage"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlSmartRelayUsage"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlOption82Usage"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsControlAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayControlAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterPortState"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterPortControlState"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfActivity"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfMask"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfServer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfClientType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfClientId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfClassType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfClassId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfLeasetime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfExpired"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfState"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlClientType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlClientId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlClassType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlClassId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlLeasetime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientOptionCode"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientOptionInstance"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientOptionType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientOptionValue"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82SystemRemoteType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlOption82SystemRemoteType"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4Activity"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VerifyMacState"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4DatabaseURL"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4DatabaseInterval"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlActivity"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlVerifyMacState"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlDatabaseURL"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlDatabaseInterval"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanState"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanControlState"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortTrustState"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortLimitRate"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortLimitLease"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortSrcGuardState"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlTrustState"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlLimitRate"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlLimitLease"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlSrcGuardState"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsVlanIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsPortIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsMac"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsType"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsLeasedTime"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlVlanIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlPortIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlMac"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4IllegalAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlServiceActivity"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlRequestFlag"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlHostName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfRequestFlag"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfHostName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlAuthArpTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlActivity"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsState"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedMac"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedHostName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedClientId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedRemoteId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedCircuitId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedStartTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedFinishTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlMask"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanControlIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfControllReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfControlIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterPortIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlLeasedTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortCircuitType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortCircuitId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortTrustState"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlCircuitType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlCircuitId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlTrustState"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfSimpleOpt82AdminState"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfSimpleOpt82OperState"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperOui"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlOui"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfControlSimpleOpt82AdminState"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapClass"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapRemote"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapCircuit"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapControlClass"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapControlRemote"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82Drop"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlOption82Drop"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteClass"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteTrust"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlClass"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlTrust"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitClass"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlRemote"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientHardwareAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlClientHardwareAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolMeritDumpPath"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolRootPath"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlMeritDumpPath"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlRootPath"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsControlIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsControlAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpControlIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpControlAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortTimeout"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlTimeout"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlPStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsMaskLen"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlMaskLen"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortFilterMode"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortFilterDelayTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortFilterDelayCounter"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlFilterMode"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlFilterDelayTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlFilterDelayCounter"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortLeaseIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortLeaseLimit"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortLeaseCount"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortLeaseControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortLeaseControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortLeaseControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortLeaseControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortLeaseControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortLeaseControlIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortLeaseControlLimit"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsPortReceived"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsPortSent"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsPortReceivedError"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsPortSentError"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsPortReceivedDiscover"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsPortReceivedRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsPortReceivedRelease"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsPortReceivedInform"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsPortReceivedDecline"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsPortSentOffer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsPortSentAck"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsPortSentNak"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsPortIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlPEStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorIfIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorID"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorEnd"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlIfIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlVendorID"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlEnd"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressIfIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressEnd"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlEnd"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEEnd"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlEnd"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlClass"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ArpPingFlag"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ArpRetransmits"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ArpTimeout"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PingRetransmits"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlArpPingFlag"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlArpRetransmits"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlArpTimeout"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlPingRetransmits"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortAddrtLeaseIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortAddrLeaseAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortAddrLeasePoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortAddrLeaseStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortAddrLeaseMac"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortAddrLeaseHostName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortAddrLeaseClientId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortAddrLeaseRemoteId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortAddrLeaseCircuitId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortAddrLeaseStartTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortAddrLeaseFinishTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlIfIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolSummaryNetwork"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4SummaryAllocated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4StateIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4StateTotal"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4StateFixed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4StateDynamic"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4StatePEntry"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4StateBindIpAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4StateBindMac"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4StateBindState"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4StateBindType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4StateBindExpiration"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4StateBindPort"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4StatePoolTotal"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4StatePoolFixed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4StatePoolDynamic"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4StatePoolPEntry"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4StateBindPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteLeaseLimit"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteLeaseCnt"),
        ("SLEV2-DHCP-MIB", "sleV4Dhcp4RemoteControlLeaseLimit"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitLeaseLimit"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitLeaseCnt"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlLeaseLimit"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfMaxHops"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfControlMaxHops"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfLeasetimeOption"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlLeasetimeOption"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlType"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ArpInspectionTime"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlArpInspectionTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrRcvd"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrSent"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrRcvdErrors"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrSentErrors"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrRcvdBootpRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrRcvdBootpReply"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrSentBootpRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrSentBootpReply"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrRcvdDiscover"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrRcvdRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrRcvdRelease"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrRcvdInform"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrRcvdDecline"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrSentDiscover"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrSentRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrSentRelease"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrSentInform"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrSentDecline"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrRcvdOffer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrRcvdAck"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrRcvdNack"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrSentOffer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrSentAck"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrSentNack"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrStatsControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrStatsControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrStatsControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrStatsControITimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrStatsControIResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrStatsControIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82SystemRemoteOption"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlOption82SystemRemoteOption"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatControlName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrID"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrLength"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrHiddenLength"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrVarType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrVarValue"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlID"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlLength"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlHiddenLength"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlVarType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlVarValue"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortPolicy"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortPolicyDrop"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlPolicy"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlPolicyDrop"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82SystemCircuitPortType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlOption82SystemCircuitPortType"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4LimitRateDiscover"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4LimitRateRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlLimitRateDiscover"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlLimitRateRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4InformationOption"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlInformationOption"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanInfoOptState"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4AuthArpReadyTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4AuthArpRemainTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlAuthArpReadyTime"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanInfoOptControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanInfoOptControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanInfoOptControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanInfoOptControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanInfoOptControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanInfoOptControlIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortTrustFilterEgressBcastReqState"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlTrustFilterEgressBcastReqState"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeIfIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeNum"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeFormat"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodePolicy"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlStatus"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlIfIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlNum"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlFormat"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlPolicy"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanInfoOptControlState"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanInfoOptIndex"))
)
if mibBuilder.loadTexts:
    sleV2DhcpGroup.setStatus("current")


# Notification objects

sleV2Dhcp4ServiceActivityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3, 1)
)
sleV2Dhcp4ServiceActivityChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ServiceActivity"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ServiceActivityChanged.setStatus(
        "current"
    )

sleV2Dhcp4DatabaseProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3, 2)
)
sleV2Dhcp4DatabaseProfileChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DatabaseURL"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DatabaseInterval"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4DatabaseProfileChanged.setStatus(
        "current"
    )

sleV2Dhcp4ArpPingProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3, 3)
)
sleV2Dhcp4ArpPingProfileChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ArpPingFlag"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ArpRetransmits"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ArpTimeout"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PingRetransmits"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PingTimeout"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ArpPingProfileChanged.setStatus(
        "current"
    )

sleV2Dhcp4ClassUsageChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3, 4)
)
sleV2Dhcp4ClassUsageChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassUsage"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassUsageChanged.setStatus(
        "current"
    )

sleV2Dhcp4SmartRelayUsageChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3, 5)
)
sleV2Dhcp4SmartRelayUsageChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4SmartRelayUsage"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4SmartRelayUsageChanged.setStatus(
        "current"
    )

sleV2Dhcp4Option82UsageChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3, 6)
)
sleV2Dhcp4Option82UsageChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82Usage"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82UsageChanged.setStatus(
        "current"
    )

sleV2Dhcp4Option82PolicyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3, 7)
)
sleV2Dhcp4Option82PolicyChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82Drop"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82Policy"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PolicyChanged.setStatus(
        "current"
    )

sleV2Dhcp4Option82TrustDefaultChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3, 8)
)
sleV2Dhcp4Option82TrustDefaultChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82TrustDefault"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82TrustDefaultChanged.setStatus(
        "current"
    )

sleV2Dhcp4Option82SystemRemoteIdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3, 9)
)
sleV2Dhcp4Option82SystemRemoteIdChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82SystemRemoteId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82SystemRemoteType"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82SystemRemoteIdChanged.setStatus(
        "current"
    )

sleV2Dhcp4DatabaseKeyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3, 10)
)
sleV2Dhcp4DatabaseKeyChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DatabaseKey"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4DatabaseKeyChanged.setStatus(
        "current"
    )

sleV2Dhcp4DebugStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3, 11)
)
sleV2Dhcp4DebugStatusChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DebugStatus"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4DebugStatusChanged.setStatus(
        "current"
    )

sleV2Dhcp4AuthoArpTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3, 12)
)
sleV2Dhcp4AuthoArpTimeChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4AuthArpTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4AuthArpReadyTime"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4AuthoArpTimeChanged.setStatus(
        "current"
    )

sleV2Dhcp4ClientHardwareAddressChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3, 13)
)
sleV2Dhcp4ClientHardwareAddressChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlClientHardwareAddress"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientHardwareAddressChanged.setStatus(
        "current"
    )

sleV2Dhcp4PEStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3, 14)
)
sleV2Dhcp4PEStatusChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlPEStatus"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PEStatusChanged.setStatus(
        "current"
    )

sleV2Dhcp4Option82SystemRemoteOptionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3, 15)
)
sleV2Dhcp4Option82SystemRemoteOptionChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlOption82SystemRemoteOption"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82SystemRemoteOptionChanged.setStatus(
        "current"
    )

sleV2DhcpOption82SystemCirucitIdPortTypeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 1, 3, 16)
)
sleV2DhcpOption82SystemCirucitIdPortTypeChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ControlOption82SystemCircuitPortType"))
)
if mibBuilder.loadTexts:
    sleV2DhcpOption82SystemCirucitIdPortTypeChanged.setStatus(
        "current"
    )

sleV2Dhcp4PoolCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 3, 1)
)
sleV2Dhcp4PoolCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolDefaultLeaseTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolMaxLeaseTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolDomainName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolMeritDumpPath"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolRootPath"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolCreated.setStatus(
        "current"
    )

sleV2Dhcp4PoolDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 3, 2)
)
sleV2Dhcp4PoolDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlIndex"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4PoolLeaseTimeProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 3, 3)
)
sleV2Dhcp4PoolLeaseTimeProfileChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolDefaultLeaseTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolMaxLeaseTime"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolLeaseTimeProfileChanged.setStatus(
        "current"
    )

sleV2Dhcp4PoolDomainNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 3, 4)
)
sleV2Dhcp4PoolDomainNameChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolDomainName"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolDomainNameChanged.setStatus(
        "current"
    )

sleV2Dhcp4PoolOriginProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 3, 5)
)
sleV2Dhcp4PoolOriginProfileChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlOriginURL"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlOriginFileName"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolOriginProfileChanged.setStatus(
        "current"
    )

sleV2Dhcp4PoolMeritDumpPathChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 3, 6)
)
sleV2Dhcp4PoolMeritDumpPathChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolMeritDumpPath"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolMeritDumpPathChanged.setStatus(
        "current"
    )

sleV2Dhcp4PoolRootPathChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 1, 3, 7)
)
sleV2Dhcp4PoolRootPathChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolRootPath"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PoolRootPathChanged.setStatus(
        "current"
    )

sleV2Dhcp4NetworkCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2, 3, 1)
)
sleV2Dhcp4NetworkCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlMask"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4NetworkCreated.setStatus(
        "current"
    )

sleV2Dhcp4NetworkDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 2, 3, 2)
)
sleV2Dhcp4NetworkDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkControlMask"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4NetworkDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4RangeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3, 3, 1)
)
sleV2Dhcp4RangeCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlEnd"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RangeCreated.setStatus(
        "current"
    )

sleV2Dhcp4RangeDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 3, 3, 2)
)
sleV2Dhcp4RangeDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeControlEnd"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RangeDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4FixedCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4, 3, 1)
)
sleV2Dhcp4FixedCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlMac"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4FixedCreated.setStatus(
        "current"
    )

sleV2Dhcp4FixedDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 4, 3, 2)
)
sleV2Dhcp4FixedDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedControlMac"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4FixedDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4DnsCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5, 3, 1)
)
sleV2Dhcp4DnsCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsAddress"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4DnsCreated.setStatus(
        "current"
    )

sleV2Dhcp4DnsDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 5, 3, 2)
)
sleV2Dhcp4DnsDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsControlIndex"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4DnsDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4DefaultGatewayCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6, 3, 1)
)
sleV2Dhcp4DefaultGatewayCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayAddress"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4DefaultGatewayCreated.setStatus(
        "current"
    )

sleV2Dhcp4DefaultGatewayDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 6, 3, 2)
)
sleV2Dhcp4DefaultGatewayDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayControlIndex"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4DefaultGatewayDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4OptionCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 3, 1)
)
sleV2Dhcp4OptionCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionValue"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionCreated.setStatus(
        "current"
    )

sleV2Dhcp4OptionDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 7, 3, 2)
)
sleV2Dhcp4OptionDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlCode"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionControlInstance"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4LogsCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8, 3, 1)
)
sleV2Dhcp4LogsCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsAddress"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4LogsCreated.setStatus(
        "current"
    )

sleV2Dhcp4LogsDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 8, 3, 2)
)
sleV2Dhcp4LogsDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsControlIndex"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4LogsDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4NtpCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9, 3, 1)
)
sleV2Dhcp4NtpCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpAddress"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4NtpCreated.setStatus(
        "current"
    )

sleV2Dhcp4NtpDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 9, 3, 2)
)
sleV2Dhcp4NtpDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpControlIndex"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4NtpDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4PEVendorCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 3, 1)
)
sleV2Dhcp4PEVendorCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlIfIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlVendorID"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlEnd"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorCreated.setStatus(
        "current"
    )

sleV2Dhcp4PEVendorDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 3, 2)
)
sleV2Dhcp4PEVendorDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlIfIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlVendorID"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlEnd"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4PEVendorAllDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 1, 3, 3)
)
sleV2Dhcp4PEVendorAllDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorControlIfIndex"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PEVendorAllDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4PEAddressCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 3, 1)
)
sleV2Dhcp4PEAddressCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlIfIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlEnd"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressCreated.setStatus(
        "current"
    )

sleV2Dhcp4PEAddressDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 3, 2)
)
sleV2Dhcp4PEAddressDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlIfIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlEnd"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4PEAddressAllDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 2, 3, 3)
)
sleV2Dhcp4PEAddressAllDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressControlIfIndex"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PEAddressAllDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4PENonPECreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 3, 1)
)
sleV2Dhcp4PENonPECreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlEnd"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PENonPECreated.setStatus(
        "current"
    )

sleV2Dhcp4PENonPEDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 2, 10, 3, 3, 2)
)
sleV2Dhcp4PENonPEDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEControlEnd"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PENonPEDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4Option82PortCircuitIdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 3, 1)
)
sleV2Dhcp4Option82PortCircuitIdChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortCircuitType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortCircuitId"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortCircuitIdChanged.setStatus(
        "current"
    )

sleV2Dhcp4Option82PortTrustStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 3, 2)
)
sleV2Dhcp4Option82PortTrustStateChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortTrustState"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortTrustStateChanged.setStatus(
        "current"
    )

sleV2Dhcp4Option82PortCircuitIdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 3, 3)
)
sleV2Dhcp4Option82PortCircuitIdCleared.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortCircuitType"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortCircuitIdCleared.setStatus(
        "current"
    )

sleV2Dhcp4Option82PortPolicyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 1, 3, 4)
)
sleV2Dhcp4Option82PortPolicyChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortPolicy"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortPolicyDrop"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4Option82PortPolicyChanged.setStatus(
        "current"
    )

sleV2Dhcp4RemoteCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 3, 1)
)
sleV2Dhcp4RemoteCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV4Dhcp4RemoteControlLeaseLimit"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteClass"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteTrust"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteCreated.setStatus(
        "current"
    )

sleV2Dhcp4RemoteDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 3, 2)
)
sleV2Dhcp4RemoteDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlId"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4RemoteChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 3, 3)
)
sleV2Dhcp4RemoteChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV4Dhcp4RemoteControlLeaseLimit"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteClass"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteTrust"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteChanged.setStatus(
        "current"
    )

sleV2Dhcp4RemoteCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 1, 3, 4)
)
sleV2Dhcp4RemoteCleared.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RemoteCleared.setStatus(
        "current"
    )

sleV2Dhcp4RCircuitCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 3, 1)
)
sleV2Dhcp4RCircuitCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitLeaseLimit"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitClass"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitCreated.setStatus(
        "current"
    )

sleV2Dhcp4RCircuitDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 3, 2)
)
sleV2Dhcp4RCircuitDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlRemote"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlId"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4RCircuitCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 3, 3)
)
sleV2Dhcp4RCircuitCleared.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlRemote"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitCleared.setStatus(
        "current"
    )

sleV2Dhcp4RCircuitChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 2, 2, 3, 4)
)
sleV2Dhcp4RCircuitChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitControlRemote"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitLeaseLimit"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RCircuitChanged.setStatus(
        "current"
    )

sleV2Dhcp4ClassCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 1, 3, 1)
)
sleV2Dhcp4ClassCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassControlName"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassCreated.setStatus(
        "current"
    )

sleV2Dhcp4ClassDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 1, 3, 2)
)
sleV2Dhcp4ClassDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassControlName"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4CRCMapCircuitCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2, 3, 1)
)
sleV2Dhcp4CRCMapCircuitCleared.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapControlClass"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapControlRemote"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4CRCMapCircuitCleared.setStatus(
        "current"
    )

sleV2Dhcp4CRCMapRemoteCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 2, 3, 2)
)
sleV2Dhcp4CRCMapRemoteCleared.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapControlClass"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4CRCMapRemoteCleared.setStatus(
        "current"
    )

sleV2Dhcp4ClassRangeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 3, 1)
)
sleV2Dhcp4ClassRangeCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlEnd"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassRangeCreated.setStatus(
        "current"
    )

sleV2Dhcp4ClassRangeDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 3, 3, 3, 2)
)
sleV2Dhcp4ClassRangeDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlPoolIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlStart"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeControlEnd"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClassRangeDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4OptionFormatCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 1, 3, 1)
)
sleV2Dhcp4OptionFormatCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatControlName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatCreated.setStatus(
        "current"
    )

sleV2Dhcp4OptionFormatDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 1, 3, 2)
)
sleV2Dhcp4OptionFormatDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatControlName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatControlTimeStamp"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4OptionFormatAttrAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 3, 1)
)
sleV2Dhcp4OptionFormatAttrAdded.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlVarValue"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlVarType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlHiddenLength"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlLength"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlID"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrAdded.setStatus(
        "current"
    )

sleV2Dhcp4OptionFormatAttrDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 3, 2)
)
sleV2Dhcp4OptionFormatAttrDeleted.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlID"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrDeleted.setStatus(
        "current"
    )

sleV2Dhcp4OptionFormatAttrModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 3, 4, 2, 3, 3)
)
sleV2Dhcp4OptionFormatAttrModified.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlID"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlLength"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlHiddenLength"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlVarType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrControlVarValue"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4OptionFormatAttrModified.setStatus(
        "current"
    )

sleV2Dhcp4FilterPortStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 1, 3, 1)
)
sleV2Dhcp4FilterPortStateChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterPortControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterPortControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterPortControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterPortState"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterPortStateChanged.setStatus(
        "current"
    )

sleV2Dhcp4FilterAddressCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 2, 3, 1)
)
sleV2Dhcp4FilterAddressCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlMac"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlType"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterAddressCreated.setStatus(
        "current"
    )

sleV2Dhcp4FilterAddressDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 2, 3, 2)
)
sleV2Dhcp4FilterAddressDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlMac"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressControlType"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4FilterAddressDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4IllegalCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 4, 3, 3, 1)
)
sleV2Dhcp4IllegalCleared.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4IllegalControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4IllegalControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4IllegalControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4IllegalCleared.setStatus(
        "current"
    )

sleV2Dhcp4PacketStatsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 1, 3, 1)
)
sleV2Dhcp4PacketStatsCleared.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PacketStatsCleared.setStatus(
        "current"
    )

sleV2Dhcp4LeasedAddressCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 3, 1)
)
sleV2Dhcp4LeasedAddressCleared.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlAddress"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedAddressCleared.setStatus(
        "current"
    )

sleV2Dhcp4LeasedNetworkCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 3, 2)
)
sleV2Dhcp4LeasedNetworkCleared.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlMask"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedNetworkCleared.setStatus(
        "current"
    )

sleV2Dhcp4LeasedPoolCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 3, 3)
)
sleV2Dhcp4LeasedPoolCleared.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlPoolIndex"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedPoolCleared.setStatus(
        "current"
    )

sleV2Dhcp4LeasedAllCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 5, 2, 3, 4)
)
sleV2Dhcp4LeasedAllCleared.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4LeasedAllCleared.setStatus(
        "current"
    )

sleV2Ds4ActivityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 3, 1)
)
sleV2Ds4ActivityChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4Activity"))
)
if mibBuilder.loadTexts:
    sleV2Ds4ActivityChanged.setStatus(
        "current"
    )

sleV2Ds4VerifyMacStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 3, 2)
)
sleV2Ds4VerifyMacStateChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VerifyMacState"))
)
if mibBuilder.loadTexts:
    sleV2Ds4VerifyMacStateChanged.setStatus(
        "current"
    )

sleV2Ds4DatabaseProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 3, 3)
)
sleV2Ds4DatabaseProfileChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4DatabaseURL"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4DatabaseInterval"))
)
if mibBuilder.loadTexts:
    sleV2Ds4DatabaseProfileChanged.setStatus(
        "current"
    )

sleV2Ds4DatabaseRenewed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 3, 4)
)
sleV2Ds4DatabaseRenewed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlDatabaseURL"))
)
if mibBuilder.loadTexts:
    sleV2Ds4DatabaseRenewed.setStatus(
        "current"
    )

sleV2Ds4ArpInspectionTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 3, 5)
)
sleV2Ds4ArpInspectionTimeChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ArpInspectionTime"))
)
if mibBuilder.loadTexts:
    sleV2Ds4ArpInspectionTimeChanged.setStatus(
        "current"
    )

sleV2Ds4LimitRateDiscoverChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 3, 6)
)
sleV2Ds4LimitRateDiscoverChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlLimitRateDiscover"))
)
if mibBuilder.loadTexts:
    sleV2Ds4LimitRateDiscoverChanged.setStatus(
        "current"
    )

sleV2Ds4LimitRateRequestChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 3, 7)
)
sleV2Ds4LimitRateRequestChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlLimitRateRequest"))
)
if mibBuilder.loadTexts:
    sleV2Ds4LimitRateRequestChanged.setStatus(
        "current"
    )

sleV2Ds4InformationOptionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 1, 3, 8)
)
sleV2Ds4InformationOptionChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4ControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ControlInformationOption"))
)
if mibBuilder.loadTexts:
    sleV2Ds4InformationOptionChanged.setStatus(
        "current"
    )

sleV2Ds4VlanStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 2, 3, 1)
)
sleV2Ds4VlanStateChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4VlanControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanState"))
)
if mibBuilder.loadTexts:
    sleV2Ds4VlanStateChanged.setStatus(
        "current"
    )

sleV2Ds4PortTrustStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 3, 1)
)
sleV2Ds4PortTrustStateChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4PortControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortTrustState"))
)
if mibBuilder.loadTexts:
    sleV2Ds4PortTrustStateChanged.setStatus(
        "current"
    )

sleV2Ds4PortLimitProfileChagned = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 3, 2)
)
sleV2Ds4PortLimitProfileChagned.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4PortControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortLimitLease"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortLimitRate"))
)
if mibBuilder.loadTexts:
    sleV2Ds4PortLimitProfileChagned.setStatus(
        "current"
    )

sleV2Ds4PortSrcGuardStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 3, 3)
)
sleV2Ds4PortSrcGuardStateChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4PortControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortSrcGuardState"))
)
if mibBuilder.loadTexts:
    sleV2Ds4PortSrcGuardStateChanged.setStatus(
        "current"
    )

sleV2Ds4PortTimeoutChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 3, 4)
)
sleV2Ds4PortTimeoutChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4PortControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortTimeout"))
)
if mibBuilder.loadTexts:
    sleV2Ds4PortTimeoutChanged.setStatus(
        "current"
    )

sleV2Ds4PortStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 3, 5)
)
sleV2Ds4PortStatusChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4PortControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlPStatus"))
)
if mibBuilder.loadTexts:
    sleV2Ds4PortStatusChanged.setStatus(
        "current"
    )

sleV2Ds4PortFilterModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 3, 6)
)
sleV2Ds4PortFilterModeChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4PortControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortFilterMode"))
)
if mibBuilder.loadTexts:
    sleV2Ds4PortFilterModeChanged.setStatus(
        "current"
    )

sleV2Ds4PortFilterDelayChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 3, 7)
)
sleV2Ds4PortFilterDelayChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4PortControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortFilterDelayTimer"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortFilterDelayCounter"))
)
if mibBuilder.loadTexts:
    sleV2Ds4PortFilterDelayChanged.setStatus(
        "current"
    )

sleV2Ds4PortTrustFilterEgressBcastReqStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 3, 3, 8)
)
sleV2Ds4PortTrustFilterEgressBcastReqStateChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4PortControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortControlTrustFilterEgressBcastReqState"))
)
if mibBuilder.loadTexts:
    sleV2Ds4PortTrustFilterEgressBcastReqStateChanged.setStatus(
        "current"
    )

sleV2Ds4BindingsCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 3, 1)
)
sleV2Ds4BindingsCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsVlanIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsType"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsMac"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsLeasedTime"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsMaskLen"))
)
if mibBuilder.loadTexts:
    sleV2Ds4BindingsCreated.setStatus(
        "current"
    )

sleV2Ds4BindingsDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 3, 2)
)
sleV2Ds4BindingsDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlPortIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlAddress"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlType"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlMaskLen"))
)
if mibBuilder.loadTexts:
    sleV2Ds4BindingsDestroyed.setStatus(
        "current"
    )

sleV2Ds4BindingsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 4, 3, 3)
)
sleV2Ds4BindingsCleared.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlPortIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsControlType"))
)
if mibBuilder.loadTexts:
    sleV2Ds4BindingsCleared.setStatus(
        "current"
    )

sleV2Ds4VlanInfoOptStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 5, 3, 1)
)
sleV2Ds4VlanInfoOptStateChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4VlanInfoOptControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanInfoOptControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanInfoOptControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanInfoOptState"))
)
if mibBuilder.loadTexts:
    sleV2Ds4VlanInfoOptStateChanged.setStatus(
        "current"
    )

sleV2Ds4OptCodeFormatChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 3, 1)
)
sleV2Ds4OptCodeFormatChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeFormat"))
)
if mibBuilder.loadTexts:
    sleV2Ds4OptCodeFormatChanged.setStatus(
        "current"
    )

sleV2Ds4OptCodePolicyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 3, 2)
)
sleV2Ds4OptCodePolicyChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodePolicy"))
)
if mibBuilder.loadTexts:
    sleV2Ds4OptCodePolicyChanged.setStatus(
        "current"
    )

sleV2Ds4OptCodeDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 6, 6, 3, 3)
)
sleV2Ds4OptCodeDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeControlTimeStamp"))
)
if mibBuilder.loadTexts:
    sleV2Ds4OptCodeDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4RelayIfSimpleOpt82AdminStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 3, 1)
)
sleV2Dhcp4RelayIfSimpleOpt82AdminStateChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfControllReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfSimpleOpt82AdminState"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIfSimpleOpt82AdminStateChanged.setStatus(
        "current"
    )

sleV2Dhcp4RelayIfMaxHopsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 1, 3, 2)
)
sleV2Dhcp4RelayIfMaxHopsChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfMaxHops"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfControllReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfSimpleOpt82AdminState"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayIfMaxHopsChanged.setStatus(
        "current"
    )

sleV2Dhcp4RelayHelperCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 3, 1)
)
sleV2Dhcp4RelayHelperCreated.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperType"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperCreated.setStatus(
        "current"
    )

sleV2Dhcp4RelayHelperDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 3, 2)
)
sleV2Dhcp4RelayHelperDestroyed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlIfIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlOui"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlAddress"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperDestroyed.setStatus(
        "current"
    )

sleV2Dhcp4RelayHelperCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 2, 3, 3)
)
sleV2Dhcp4RelayHelperCleared.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlIfIndex"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperControlOui"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayHelperCleared.setStatus(
        "current"
    )

sleV2Dhcp4RelayintrStatsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 7, 3, 3, 1)
)
sleV2Dhcp4RelayintrStatsCleared.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrStatsControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrStatsControITimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrStatsControIResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIntrStatsControIndex"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4RelayintrStatsCleared.setStatus(
        "current"
    )

sleV2Dhcp4ClientIfActivityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 3, 1)
)
sleV2Dhcp4ClientIfActivityChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfActivity"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfActivityChanged.setStatus(
        "current"
    )

sleV2Dhcp4ClientIfProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 3, 2)
)
sleV2Dhcp4ClientIfProfileChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfHostName"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfRequestFlag"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfClientType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfClientId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfClassType"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfClassId"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfLeasetime"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfProfileChanged.setStatus(
        "current"
    )

sleV2Dhcp4ClientIfRenewed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 3, 3)
)
sleV2Dhcp4ClientIfRenewed.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlIndex"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfRenewed.setStatus(
        "current"
    )

sleV2Dhcp4ClientIfReleased = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 3, 4)
)
sleV2Dhcp4ClientIfReleased.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlIndex"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfReleased.setStatus(
        "current"
    )

sleV2Dhcp4ClientIfLeasetimeOptionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 8, 1, 3, 5)
)
sleV2Dhcp4ClientIfLeasetimeOptionChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfControlIndex"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4ClientIfLeasetimeOptionChanged.setStatus(
        "current"
    )

sleV2Dhcp4PortLeaseLimitChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 2, 9, 1, 4, 1)
)
sleV2Dhcp4PortLeaseLimitChanged.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4PortLeaseControlRequest"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortLeaseControlTimeStamp"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortLeaseControlReqResult"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortLeaseLimit"))
)
if mibBuilder.loadTexts:
    sleV2Dhcp4PortLeaseLimitChanged.setStatus(
        "current"
    )


# Notifications groups

sleV2DhcpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 102, 6, 5)
)
sleV2DhcpNotificationGroup.setObjects(
      *(("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedAddressCleared"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedNetworkCleared"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedPoolCleared"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LeasedAllCleared"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ServiceActivityChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassUsageChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4SmartRelayUsageChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82UsageChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterPortStateChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DatabaseProfileChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PolicyChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82SystemRemoteIdChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolLeaseTimeProfileChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolDomainNameChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolOriginProfileChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NetworkDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RangeDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FixedDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DnsDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DefaultGatewayCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82TrustDefaultChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4FilterAddressDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PacketStatsCleared"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DatabaseKeyChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4DebugStatusChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4IllegalCleared"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4AuthoArpTimeChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfReleased"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfRenewed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfProfileChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ActivityChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VerifyMacStateChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4DatabaseProfileChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanStateChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortTrustStateChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortLimitProfileChagned"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortSrcGuardStateChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfActivityChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4DatabaseRenewed"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortCircuitIdChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortTrustStateChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfSimpleOpt82AdminStateChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4BindingsCleared"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayHelperCleared"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapCircuitCleared"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4CRCMapRemoteCleared"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClassRangeDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RemoteCleared"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientHardwareAddressChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolMeritDumpPathChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4LogsDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4NtpDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortTimeoutChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortStatusChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortFilterModeChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortFilterDelayChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PortLeaseLimitChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEStatusChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEVendorAllDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PEAddressAllDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPECreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PENonPEDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayIfMaxHopsChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ClientIfLeasetimeOptionChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4ArpInspectionTimeChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RelayintrStatsCleared"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82SystemRemoteOptionChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortCircuitIdCleared"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatCreated"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrAdded"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrDeleted"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4OptionFormatAttrModified"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4Option82PortPolicyChanged"),
        ("SLEV2-DHCP-MIB", "sleV2DhcpOption82SystemCirucitIdPortTypeChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4LimitRateDiscoverChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4LimitRateRequestChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4InformationOptionChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4VlanInfoOptStateChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4PortTrustFilterEgressBcastReqStateChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeFormatChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodePolicyChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Ds4OptCodeDestroyed"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4RCircuitCleared"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4ArpPingProfileChanged"),
        ("SLEV2-DHCP-MIB", "sleV2Dhcp4PoolRootPathChanged"))
)
if mibBuilder.loadTexts:
    sleV2DhcpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLEV2-DHCP-MIB",
    **{"Boolean": Boolean,
       "sleV2Dhcp": sleV2Dhcp,
       "sleV2DhcpBase": sleV2DhcpBase,
       "sleV2Dhcp4": sleV2Dhcp4,
       "sleV2Dhcp4Base": sleV2Dhcp4Base,
       "sleV2Dhcp4Info": sleV2Dhcp4Info,
       "sleV2Dhcp4ServiceActivity": sleV2Dhcp4ServiceActivity,
       "sleV2Dhcp4DatabaseURL": sleV2Dhcp4DatabaseURL,
       "sleV2Dhcp4DatabaseInterval": sleV2Dhcp4DatabaseInterval,
       "sleV2Dhcp4ArpPingFlag": sleV2Dhcp4ArpPingFlag,
       "sleV2Dhcp4ArpRetransmits": sleV2Dhcp4ArpRetransmits,
       "sleV2Dhcp4ArpTimeout": sleV2Dhcp4ArpTimeout,
       "sleV2Dhcp4PingRetransmits": sleV2Dhcp4PingRetransmits,
       "sleV2Dhcp4PingTimeout": sleV2Dhcp4PingTimeout,
       "sleV2Dhcp4ClassUsage": sleV2Dhcp4ClassUsage,
       "sleV2Dhcp4SmartRelayUsage": sleV2Dhcp4SmartRelayUsage,
       "sleV2Dhcp4Option82Usage": sleV2Dhcp4Option82Usage,
       "sleV2Dhcp4Option82Drop": sleV2Dhcp4Option82Drop,
       "sleV2Dhcp4Option82Policy": sleV2Dhcp4Option82Policy,
       "sleV2Dhcp4Option82TrustDefault": sleV2Dhcp4Option82TrustDefault,
       "sleV2Dhcp4Option82SystemRemoteType": sleV2Dhcp4Option82SystemRemoteType,
       "sleV2Dhcp4Option82SystemRemoteId": sleV2Dhcp4Option82SystemRemoteId,
       "sleV2Dhcp4DatabaseKey": sleV2Dhcp4DatabaseKey,
       "sleV2Dhcp4DebugStatus": sleV2Dhcp4DebugStatus,
       "sleV2Dhcp4AuthArpTime": sleV2Dhcp4AuthArpTime,
       "sleV2Dhcp4AuthArpLeft": sleV2Dhcp4AuthArpLeft,
       "sleV2Dhcp4ClientHardwareAddress": sleV2Dhcp4ClientHardwareAddress,
       "sleV2Dhcp4PEStatus": sleV2Dhcp4PEStatus,
       "sleV2Dhcp4AuthArpReadyTime": sleV2Dhcp4AuthArpReadyTime,
       "sleV2Dhcp4AuthArpRemainTime": sleV2Dhcp4AuthArpRemainTime,
       "sleV2Dhcp4Option82SystemRemoteOption": sleV2Dhcp4Option82SystemRemoteOption,
       "sleV2Dhcp4Option82SystemCircuitPortType": sleV2Dhcp4Option82SystemCircuitPortType,
       "sleV2Dhcp4Control": sleV2Dhcp4Control,
       "sleV2Dhcp4ControlRequest": sleV2Dhcp4ControlRequest,
       "sleV2Dhcp4ControlStatus": sleV2Dhcp4ControlStatus,
       "sleV2Dhcp4ControlTimer": sleV2Dhcp4ControlTimer,
       "sleV2Dhcp4ControlTimeStamp": sleV2Dhcp4ControlTimeStamp,
       "sleV2Dhcp4ControlReqResult": sleV2Dhcp4ControlReqResult,
       "sleV2Dhcp4ControlServiceActivity": sleV2Dhcp4ControlServiceActivity,
       "sleV2Dhcp4ControlDatabaseURL": sleV2Dhcp4ControlDatabaseURL,
       "sleV2Dhcp4ControlDatabaseInterval": sleV2Dhcp4ControlDatabaseInterval,
       "sleV2Dhcp4ControlArpPingFlag": sleV2Dhcp4ControlArpPingFlag,
       "sleV2Dhcp4ControlArpRetransmits": sleV2Dhcp4ControlArpRetransmits,
       "sleV2Dhcp4ControlArpTimeout": sleV2Dhcp4ControlArpTimeout,
       "sleV2Dhcp4ControlPingRetransmits": sleV2Dhcp4ControlPingRetransmits,
       "sleV2Dhcp4ControlPingTimeout": sleV2Dhcp4ControlPingTimeout,
       "sleV2Dhcp4ControlClassUsage": sleV2Dhcp4ControlClassUsage,
       "sleV2Dhcp4ControlSmartRelayUsage": sleV2Dhcp4ControlSmartRelayUsage,
       "sleV2Dhcp4ControlOption82Usage": sleV2Dhcp4ControlOption82Usage,
       "sleV2Dhcp4ControlOption82Drop": sleV2Dhcp4ControlOption82Drop,
       "sleV2Dhcp4ControlOption82Policy": sleV2Dhcp4ControlOption82Policy,
       "sleV2Dhcp4ControlOption82TrustDefault": sleV2Dhcp4ControlOption82TrustDefault,
       "sleV2Dhcp4ControlOption82SystemRemoteType": sleV2Dhcp4ControlOption82SystemRemoteType,
       "sleV2Dhcp4ControlOption82SystemRemoteId": sleV2Dhcp4ControlOption82SystemRemoteId,
       "sleV2Dhcp4ControlDatabaseKey": sleV2Dhcp4ControlDatabaseKey,
       "sleV2Dhcp4ControlDebugStatus": sleV2Dhcp4ControlDebugStatus,
       "sleV2Dhcp4ControlAuthArpTime": sleV2Dhcp4ControlAuthArpTime,
       "sleV2Dhcp4ControlClientHardwareAddress": sleV2Dhcp4ControlClientHardwareAddress,
       "sleV2Dhcp4ControlPEStatus": sleV2Dhcp4ControlPEStatus,
       "sleV2Dhcp4ControlAuthArpReadyTime": sleV2Dhcp4ControlAuthArpReadyTime,
       "sleV2Dhcp4ControlOption82SystemRemoteOption": sleV2Dhcp4ControlOption82SystemRemoteOption,
       "sleV2Dhcp4ControlOption82SystemCircuitPortType": sleV2Dhcp4ControlOption82SystemCircuitPortType,
       "sleV2Dhcp4Notification": sleV2Dhcp4Notification,
       "sleV2Dhcp4ServiceActivityChanged": sleV2Dhcp4ServiceActivityChanged,
       "sleV2Dhcp4DatabaseProfileChanged": sleV2Dhcp4DatabaseProfileChanged,
       "sleV2Dhcp4ArpPingProfileChanged": sleV2Dhcp4ArpPingProfileChanged,
       "sleV2Dhcp4ClassUsageChanged": sleV2Dhcp4ClassUsageChanged,
       "sleV2Dhcp4SmartRelayUsageChanged": sleV2Dhcp4SmartRelayUsageChanged,
       "sleV2Dhcp4Option82UsageChanged": sleV2Dhcp4Option82UsageChanged,
       "sleV2Dhcp4Option82PolicyChanged": sleV2Dhcp4Option82PolicyChanged,
       "sleV2Dhcp4Option82TrustDefaultChanged": sleV2Dhcp4Option82TrustDefaultChanged,
       "sleV2Dhcp4Option82SystemRemoteIdChanged": sleV2Dhcp4Option82SystemRemoteIdChanged,
       "sleV2Dhcp4DatabaseKeyChanged": sleV2Dhcp4DatabaseKeyChanged,
       "sleV2Dhcp4DebugStatusChanged": sleV2Dhcp4DebugStatusChanged,
       "sleV2Dhcp4AuthoArpTimeChanged": sleV2Dhcp4AuthoArpTimeChanged,
       "sleV2Dhcp4ClientHardwareAddressChanged": sleV2Dhcp4ClientHardwareAddressChanged,
       "sleV2Dhcp4PEStatusChanged": sleV2Dhcp4PEStatusChanged,
       "sleV2Dhcp4Option82SystemRemoteOptionChanged": sleV2Dhcp4Option82SystemRemoteOptionChanged,
       "sleV2DhcpOption82SystemCirucitIdPortTypeChanged": sleV2DhcpOption82SystemCirucitIdPortTypeChanged,
       "sleV2Dhcp4Pool": sleV2Dhcp4Pool,
       "sleV2Dhcp4PoolBase": sleV2Dhcp4PoolBase,
       "sleV2Dhcp4PoolTable": sleV2Dhcp4PoolTable,
       "sleV2Dhcp4PoolEntry": sleV2Dhcp4PoolEntry,
       "sleV2Dhcp4PoolIndex": sleV2Dhcp4PoolIndex,
       "sleV2Dhcp4PoolName": sleV2Dhcp4PoolName,
       "sleV2Dhcp4PoolDefaultLeaseTime": sleV2Dhcp4PoolDefaultLeaseTime,
       "sleV2Dhcp4PoolMaxLeaseTime": sleV2Dhcp4PoolMaxLeaseTime,
       "sleV2Dhcp4PoolDomainName": sleV2Dhcp4PoolDomainName,
       "sleV2Dhcp4PoolSummaryTotal": sleV2Dhcp4PoolSummaryTotal,
       "sleV2Dhcp4PoolSummaryAllocated": sleV2Dhcp4PoolSummaryAllocated,
       "sleV2Dhcp4PoolSummaryBound": sleV2Dhcp4PoolSummaryBound,
       "sleV2Dhcp4PoolSummaryOffered": sleV2Dhcp4PoolSummaryOffered,
       "sleV2Dhcp4PoolSummaryFixed": sleV2Dhcp4PoolSummaryFixed,
       "sleV2Dhcp4PoolSummaryAbandon": sleV2Dhcp4PoolSummaryAbandon,
       "sleV2Dhcp4PoolSummaryAvailable": sleV2Dhcp4PoolSummaryAvailable,
       "sleV2Dhcp4PoolMeritDumpPath": sleV2Dhcp4PoolMeritDumpPath,
       "sleV2Dhcp4PoolRootPath": sleV2Dhcp4PoolRootPath,
       "sleV2Dhcp4PoolSummaryNetwork": sleV2Dhcp4PoolSummaryNetwork,
       "sleV2Dhcp4PoolControl": sleV2Dhcp4PoolControl,
       "sleV2Dhcp4PoolControlRequest": sleV2Dhcp4PoolControlRequest,
       "sleV2Dhcp4PoolControlStatus": sleV2Dhcp4PoolControlStatus,
       "sleV2Dhcp4PoolControlTimer": sleV2Dhcp4PoolControlTimer,
       "sleV2Dhcp4PoolControlTimeStamp": sleV2Dhcp4PoolControlTimeStamp,
       "sleV2Dhcp4PoolControlReqResult": sleV2Dhcp4PoolControlReqResult,
       "sleV2Dhcp4PoolControlIndex": sleV2Dhcp4PoolControlIndex,
       "sleV2Dhcp4PoolControlName": sleV2Dhcp4PoolControlName,
       "sleV2Dhcp4PoolControlDefaultLeaseTime": sleV2Dhcp4PoolControlDefaultLeaseTime,
       "sleV2Dhcp4PoolControlMaxLeaseTime": sleV2Dhcp4PoolControlMaxLeaseTime,
       "sleV2Dhcp4PoolControlDomainName": sleV2Dhcp4PoolControlDomainName,
       "sleV2Dhcp4PoolControlOriginURL": sleV2Dhcp4PoolControlOriginURL,
       "sleV2Dhcp4PoolControlOriginFileName": sleV2Dhcp4PoolControlOriginFileName,
       "sleV2Dhcp4PoolControlMeritDumpPath": sleV2Dhcp4PoolControlMeritDumpPath,
       "sleV2Dhcp4PoolControlRootPath": sleV2Dhcp4PoolControlRootPath,
       "sleV2Dhcp4PoolNotification": sleV2Dhcp4PoolNotification,
       "sleV2Dhcp4PoolCreated": sleV2Dhcp4PoolCreated,
       "sleV2Dhcp4PoolDestroyed": sleV2Dhcp4PoolDestroyed,
       "sleV2Dhcp4PoolLeaseTimeProfileChanged": sleV2Dhcp4PoolLeaseTimeProfileChanged,
       "sleV2Dhcp4PoolDomainNameChanged": sleV2Dhcp4PoolDomainNameChanged,
       "sleV2Dhcp4PoolOriginProfileChanged": sleV2Dhcp4PoolOriginProfileChanged,
       "sleV2Dhcp4PoolMeritDumpPathChanged": sleV2Dhcp4PoolMeritDumpPathChanged,
       "sleV2Dhcp4PoolRootPathChanged": sleV2Dhcp4PoolRootPathChanged,
       "sleV2Dhcp4Network": sleV2Dhcp4Network,
       "sleV2Dhcp4NetworkTable": sleV2Dhcp4NetworkTable,
       "sleV2Dhcp4NetworkEntry": sleV2Dhcp4NetworkEntry,
       "sleV2Dhcp4NetworkAddress": sleV2Dhcp4NetworkAddress,
       "sleV2Dhcp4NetworkMask": sleV2Dhcp4NetworkMask,
       "sleV2Dhcp4NetworkControl": sleV2Dhcp4NetworkControl,
       "sleV2Dhcp4NetworkControlRequest": sleV2Dhcp4NetworkControlRequest,
       "sleV2Dhcp4NetworkControlStatus": sleV2Dhcp4NetworkControlStatus,
       "sleV2Dhcp4NetworkControlTimer": sleV2Dhcp4NetworkControlTimer,
       "sleV2Dhcp4NetworkControlTimeStamp": sleV2Dhcp4NetworkControlTimeStamp,
       "sleV2Dhcp4NetworkControlReqResult": sleV2Dhcp4NetworkControlReqResult,
       "sleV2Dhcp4NetworkControlPoolIndex": sleV2Dhcp4NetworkControlPoolIndex,
       "sleV2Dhcp4NetworkControlAddress": sleV2Dhcp4NetworkControlAddress,
       "sleV2Dhcp4NetworkControlMask": sleV2Dhcp4NetworkControlMask,
       "sleV2Dhcp4NetworkNotification": sleV2Dhcp4NetworkNotification,
       "sleV2Dhcp4NetworkCreated": sleV2Dhcp4NetworkCreated,
       "sleV2Dhcp4NetworkDestroyed": sleV2Dhcp4NetworkDestroyed,
       "sleV2Dhcp4Range": sleV2Dhcp4Range,
       "sleV2Dhcp4RangeTable": sleV2Dhcp4RangeTable,
       "sleV2Dhcp4RangeEntry": sleV2Dhcp4RangeEntry,
       "sleV2Dhcp4RangeStart": sleV2Dhcp4RangeStart,
       "sleV2Dhcp4RangeEnd": sleV2Dhcp4RangeEnd,
       "sleV2Dhcp4RangeControl": sleV2Dhcp4RangeControl,
       "sleV2Dhcp4RangeControlRequest": sleV2Dhcp4RangeControlRequest,
       "sleV2Dhcp4RangeControlStatus": sleV2Dhcp4RangeControlStatus,
       "sleV2Dhcp4RangeControlTimer": sleV2Dhcp4RangeControlTimer,
       "sleV2Dhcp4RangeControlTimeStamp": sleV2Dhcp4RangeControlTimeStamp,
       "sleV2Dhcp4RangeControlReqResult": sleV2Dhcp4RangeControlReqResult,
       "sleV2Dhcp4RangeControlPoolIndex": sleV2Dhcp4RangeControlPoolIndex,
       "sleV2Dhcp4RangeControlStart": sleV2Dhcp4RangeControlStart,
       "sleV2Dhcp4RangeControlEnd": sleV2Dhcp4RangeControlEnd,
       "sleV2Dhcp4RangeNotification": sleV2Dhcp4RangeNotification,
       "sleV2Dhcp4RangeCreated": sleV2Dhcp4RangeCreated,
       "sleV2Dhcp4RangeDestroyed": sleV2Dhcp4RangeDestroyed,
       "sleV2Dhcp4Fixed": sleV2Dhcp4Fixed,
       "sleV2Dhcp4FixedTable": sleV2Dhcp4FixedTable,
       "sleV2Dhcp4FixedEntry": sleV2Dhcp4FixedEntry,
       "sleV2Dhcp4FixedMac": sleV2Dhcp4FixedMac,
       "sleV2Dhcp4FixedAddress": sleV2Dhcp4FixedAddress,
       "sleV2Dhcp4FixedControl": sleV2Dhcp4FixedControl,
       "sleV2Dhcp4FixedControlRequest": sleV2Dhcp4FixedControlRequest,
       "sleV2Dhcp4FixedControlStatus": sleV2Dhcp4FixedControlStatus,
       "sleV2Dhcp4FixedControlTimer": sleV2Dhcp4FixedControlTimer,
       "sleV2Dhcp4FixedControlTimeStamp": sleV2Dhcp4FixedControlTimeStamp,
       "sleV2Dhcp4FixedControlReqResult": sleV2Dhcp4FixedControlReqResult,
       "sleV2Dhcp4FixedControlPoolIndex": sleV2Dhcp4FixedControlPoolIndex,
       "sleV2Dhcp4FixedControlAddress": sleV2Dhcp4FixedControlAddress,
       "sleV2Dhcp4FixedControlMac": sleV2Dhcp4FixedControlMac,
       "sleV2Dhcp4FixedNotification": sleV2Dhcp4FixedNotification,
       "sleV2Dhcp4FixedCreated": sleV2Dhcp4FixedCreated,
       "sleV2Dhcp4FixedDestroyed": sleV2Dhcp4FixedDestroyed,
       "sleV2Dhcp4Dns": sleV2Dhcp4Dns,
       "sleV2Dhcp4DnsTable": sleV2Dhcp4DnsTable,
       "sleV2Dhcp4DnsEntry": sleV2Dhcp4DnsEntry,
       "sleV2Dhcp4DnsIndex": sleV2Dhcp4DnsIndex,
       "sleV2Dhcp4DnsAddress": sleV2Dhcp4DnsAddress,
       "sleV2Dhcp4DnsControl": sleV2Dhcp4DnsControl,
       "sleV2Dhcp4DnsControlRequest": sleV2Dhcp4DnsControlRequest,
       "sleV2Dhcp4DnsControlStatus": sleV2Dhcp4DnsControlStatus,
       "sleV2Dhcp4DnsControlTimer": sleV2Dhcp4DnsControlTimer,
       "sleV2Dhcp4DnsControlTimeStamp": sleV2Dhcp4DnsControlTimeStamp,
       "sleV2Dhcp4DnsControlReqResult": sleV2Dhcp4DnsControlReqResult,
       "sleV2Dhcp4DnsControlPoolIndex": sleV2Dhcp4DnsControlPoolIndex,
       "sleV2Dhcp4DnsControlIndex": sleV2Dhcp4DnsControlIndex,
       "sleV2Dhcp4DnsControlAddress": sleV2Dhcp4DnsControlAddress,
       "sleV2Dhcp4DnsNotification": sleV2Dhcp4DnsNotification,
       "sleV2Dhcp4DnsCreated": sleV2Dhcp4DnsCreated,
       "sleV2Dhcp4DnsDestroyed": sleV2Dhcp4DnsDestroyed,
       "sleV2Dhcp4DefaultGateway": sleV2Dhcp4DefaultGateway,
       "sleV2Dhcp4DefaultGatewayTable": sleV2Dhcp4DefaultGatewayTable,
       "sleV2Dhcp4DefaultGatewayEntry": sleV2Dhcp4DefaultGatewayEntry,
       "sleV2Dhcp4DefaultGatewayIndex": sleV2Dhcp4DefaultGatewayIndex,
       "sleV2Dhcp4DefaultGatewayAddress": sleV2Dhcp4DefaultGatewayAddress,
       "sleV2Dhcp4DefaultGatewayControl": sleV2Dhcp4DefaultGatewayControl,
       "sleV2Dhcp4DefaultGatewayControlRequest": sleV2Dhcp4DefaultGatewayControlRequest,
       "sleV2Dhcp4DefaultGatewayControlStatus": sleV2Dhcp4DefaultGatewayControlStatus,
       "sleV2Dhcp4DefaultGatewayControlTimer": sleV2Dhcp4DefaultGatewayControlTimer,
       "sleV2Dhcp4DefaultGatewayControlTimeStamp": sleV2Dhcp4DefaultGatewayControlTimeStamp,
       "sleV2Dhcp4DefaultGatewayControlReqResult": sleV2Dhcp4DefaultGatewayControlReqResult,
       "sleV2Dhcp4DefaultGatewayControlPoolIndex": sleV2Dhcp4DefaultGatewayControlPoolIndex,
       "sleV2Dhcp4DefaultGatewayControlIndex": sleV2Dhcp4DefaultGatewayControlIndex,
       "sleV2Dhcp4DefaultGatewayControlAddress": sleV2Dhcp4DefaultGatewayControlAddress,
       "sleV2Dhcp4DefaultGatewayNotification": sleV2Dhcp4DefaultGatewayNotification,
       "sleV2Dhcp4DefaultGatewayCreated": sleV2Dhcp4DefaultGatewayCreated,
       "sleV2Dhcp4DefaultGatewayDestroyed": sleV2Dhcp4DefaultGatewayDestroyed,
       "sleV2Dhcp4Option": sleV2Dhcp4Option,
       "sleV2Dhcp4OptionTable": sleV2Dhcp4OptionTable,
       "sleV2Dhcp4OptionEntry": sleV2Dhcp4OptionEntry,
       "sleV2Dhcp4OptionCode": sleV2Dhcp4OptionCode,
       "sleV2Dhcp4OptionInstance": sleV2Dhcp4OptionInstance,
       "sleV2Dhcp4OptionType": sleV2Dhcp4OptionType,
       "sleV2Dhcp4OptionValue": sleV2Dhcp4OptionValue,
       "sleV2Dhcp4OptionControl": sleV2Dhcp4OptionControl,
       "sleV2Dhcp4OptionControlRequest": sleV2Dhcp4OptionControlRequest,
       "sleV2Dhcp4OptionControlStatus": sleV2Dhcp4OptionControlStatus,
       "sleV2Dhcp4OptionControlTimer": sleV2Dhcp4OptionControlTimer,
       "sleV2Dhcp4OptionControlTimeStamp": sleV2Dhcp4OptionControlTimeStamp,
       "sleV2Dhcp4OptionControlReqResult": sleV2Dhcp4OptionControlReqResult,
       "sleV2Dhcp4OptionControlPoolIndex": sleV2Dhcp4OptionControlPoolIndex,
       "sleV2Dhcp4OptionControlCode": sleV2Dhcp4OptionControlCode,
       "sleV2Dhcp4OptionControlInstance": sleV2Dhcp4OptionControlInstance,
       "sleV2Dhcp4OptionControlType": sleV2Dhcp4OptionControlType,
       "sleV2Dhcp4OptionControlValue": sleV2Dhcp4OptionControlValue,
       "sleV2Dhcp4OptionNotification": sleV2Dhcp4OptionNotification,
       "sleV2Dhcp4OptionCreated": sleV2Dhcp4OptionCreated,
       "sleV2Dhcp4OptionDestroyed": sleV2Dhcp4OptionDestroyed,
       "sleV2Dhcp4Logs": sleV2Dhcp4Logs,
       "sleV2Dhcp4LogsTable": sleV2Dhcp4LogsTable,
       "sleV2Dhcp4LogsEntry": sleV2Dhcp4LogsEntry,
       "sleV2Dhcp4LogsIndex": sleV2Dhcp4LogsIndex,
       "sleV2Dhcp4LogsAddress": sleV2Dhcp4LogsAddress,
       "sleV2Dhcp4LogsControl": sleV2Dhcp4LogsControl,
       "sleV2Dhcp4LogsControlRequest": sleV2Dhcp4LogsControlRequest,
       "sleV2Dhcp4LogsControlStatus": sleV2Dhcp4LogsControlStatus,
       "sleV2Dhcp4LogsControlTimer": sleV2Dhcp4LogsControlTimer,
       "sleV2Dhcp4LogsControlTimeStamp": sleV2Dhcp4LogsControlTimeStamp,
       "sleV2Dhcp4LogsControlReqResult": sleV2Dhcp4LogsControlReqResult,
       "sleV2Dhcp4LogsControlPoolIndex": sleV2Dhcp4LogsControlPoolIndex,
       "sleV2Dhcp4LogsControlIndex": sleV2Dhcp4LogsControlIndex,
       "sleV2Dhcp4LogsControlAddress": sleV2Dhcp4LogsControlAddress,
       "sleV2Dhcp4LogsNotification": sleV2Dhcp4LogsNotification,
       "sleV2Dhcp4LogsCreated": sleV2Dhcp4LogsCreated,
       "sleV2Dhcp4LogsDestroyed": sleV2Dhcp4LogsDestroyed,
       "sleV2Dhcp4Ntp": sleV2Dhcp4Ntp,
       "sleV2Dhcp4NtpTable": sleV2Dhcp4NtpTable,
       "sleV2Dhcp4NtpEntry": sleV2Dhcp4NtpEntry,
       "sleV2Dhcp4NtpIndex": sleV2Dhcp4NtpIndex,
       "sleV2Dhcp4NtpAddress": sleV2Dhcp4NtpAddress,
       "sleV2Dhcp4NtpControl": sleV2Dhcp4NtpControl,
       "sleV2Dhcp4NtpControlRequest": sleV2Dhcp4NtpControlRequest,
       "sleV2Dhcp4NtpControlStatus": sleV2Dhcp4NtpControlStatus,
       "sleV2Dhcp4NtpControlTimer": sleV2Dhcp4NtpControlTimer,
       "sleV2Dhcp4NtpControlTimeStamp": sleV2Dhcp4NtpControlTimeStamp,
       "sleV2Dhcp4NtpControlReqResult": sleV2Dhcp4NtpControlReqResult,
       "sleV2Dhcp4NtpControlPoolIndex": sleV2Dhcp4NtpControlPoolIndex,
       "sleV2Dhcp4NtpControlIndex": sleV2Dhcp4NtpControlIndex,
       "sleV2Dhcp4NtpControlAddress": sleV2Dhcp4NtpControlAddress,
       "sleV2Dhcp4NtpNotification": sleV2Dhcp4NtpNotification,
       "sleV2Dhcp4NtpCreated": sleV2Dhcp4NtpCreated,
       "sleV2Dhcp4NtpDestroyed": sleV2Dhcp4NtpDestroyed,
       "sleV2Dhcp4PE": sleV2Dhcp4PE,
       "sleV2Dhcp4PEVendor": sleV2Dhcp4PEVendor,
       "sleV2Dhcp4PEVendorTable": sleV2Dhcp4PEVendorTable,
       "sleV2Dhcp4PEVendorEntry": sleV2Dhcp4PEVendorEntry,
       "sleV2Dhcp4PEVendorPoolIndex": sleV2Dhcp4PEVendorPoolIndex,
       "sleV2Dhcp4PEVendorIfIndex": sleV2Dhcp4PEVendorIfIndex,
       "sleV2Dhcp4PEVendorID": sleV2Dhcp4PEVendorID,
       "sleV2Dhcp4PEVendorStart": sleV2Dhcp4PEVendorStart,
       "sleV2Dhcp4PEVendorEnd": sleV2Dhcp4PEVendorEnd,
       "sleV2Dhcp4PEVendorControl": sleV2Dhcp4PEVendorControl,
       "sleV2Dhcp4PEVendorControlRequest": sleV2Dhcp4PEVendorControlRequest,
       "sleV2Dhcp4PEVendorControlStatus": sleV2Dhcp4PEVendorControlStatus,
       "sleV2Dhcp4PEVendorControlTimer": sleV2Dhcp4PEVendorControlTimer,
       "sleV2Dhcp4PEVendorControlTimeStamp": sleV2Dhcp4PEVendorControlTimeStamp,
       "sleV2Dhcp4PEVendorControlReqResult": sleV2Dhcp4PEVendorControlReqResult,
       "sleV2Dhcp4PEVendorControlPoolIndex": sleV2Dhcp4PEVendorControlPoolIndex,
       "sleV2Dhcp4PEVendorControlIfIndex": sleV2Dhcp4PEVendorControlIfIndex,
       "sleV2Dhcp4PEVendorControlVendorID": sleV2Dhcp4PEVendorControlVendorID,
       "sleV2Dhcp4PEVendorControlStart": sleV2Dhcp4PEVendorControlStart,
       "sleV2Dhcp4PEVendorControlEnd": sleV2Dhcp4PEVendorControlEnd,
       "sleV2Dhcp4PEVendorNotification": sleV2Dhcp4PEVendorNotification,
       "sleV2Dhcp4PEVendorCreated": sleV2Dhcp4PEVendorCreated,
       "sleV2Dhcp4PEVendorDestroyed": sleV2Dhcp4PEVendorDestroyed,
       "sleV2Dhcp4PEVendorAllDestroyed": sleV2Dhcp4PEVendorAllDestroyed,
       "sleV2Dhcp4PEAddress": sleV2Dhcp4PEAddress,
       "sleV2Dhcp4PEAddressTable": sleV2Dhcp4PEAddressTable,
       "sleV2Dhcp4PEAddressEntry": sleV2Dhcp4PEAddressEntry,
       "sleV2Dhcp4PEAddressPoolIndex": sleV2Dhcp4PEAddressPoolIndex,
       "sleV2Dhcp4PEAddressIfIndex": sleV2Dhcp4PEAddressIfIndex,
       "sleV2Dhcp4PEAddressStart": sleV2Dhcp4PEAddressStart,
       "sleV2Dhcp4PEAddressEnd": sleV2Dhcp4PEAddressEnd,
       "sleV2Dhcp4PEAddressControl": sleV2Dhcp4PEAddressControl,
       "sleV2Dhcp4PEAddressControlRequest": sleV2Dhcp4PEAddressControlRequest,
       "sleV2Dhcp4PEAddressControlStatus": sleV2Dhcp4PEAddressControlStatus,
       "sleV2Dhcp4PEAddressControlTimer": sleV2Dhcp4PEAddressControlTimer,
       "sleV2Dhcp4PEAddressControlTimeStamp": sleV2Dhcp4PEAddressControlTimeStamp,
       "sleV2Dhcp4PEAddressControlReqResult": sleV2Dhcp4PEAddressControlReqResult,
       "sleV2Dhcp4PEAddressControlPoolIndex": sleV2Dhcp4PEAddressControlPoolIndex,
       "sleV2Dhcp4PEAddressControlIfIndex": sleV2Dhcp4PEAddressControlIfIndex,
       "sleV2Dhcp4PEAddressControlStart": sleV2Dhcp4PEAddressControlStart,
       "sleV2Dhcp4PEAddressControlEnd": sleV2Dhcp4PEAddressControlEnd,
       "sleV2Dhcp4PEAddressNotification": sleV2Dhcp4PEAddressNotification,
       "sleV2Dhcp4PEAddressCreated": sleV2Dhcp4PEAddressCreated,
       "sleV2Dhcp4PEAddressDestroyed": sleV2Dhcp4PEAddressDestroyed,
       "sleV2Dhcp4PEAddressAllDestroyed": sleV2Dhcp4PEAddressAllDestroyed,
       "sleV2Dhcp4PENonPE": sleV2Dhcp4PENonPE,
       "sleV2Dhcp4PENonPETable": sleV2Dhcp4PENonPETable,
       "sleV2Dhcp4PENonPEEntry": sleV2Dhcp4PENonPEEntry,
       "sleV2Dhcp4PENonPEPoolIndex": sleV2Dhcp4PENonPEPoolIndex,
       "sleV2Dhcp4PENonPEStart": sleV2Dhcp4PENonPEStart,
       "sleV2Dhcp4PENonPEEnd": sleV2Dhcp4PENonPEEnd,
       "sleV2Dhcp4PENonPEControl": sleV2Dhcp4PENonPEControl,
       "sleV2Dhcp4PENonPEControlRequest": sleV2Dhcp4PENonPEControlRequest,
       "sleV2Dhcp4PENonPEControlStatus": sleV2Dhcp4PENonPEControlStatus,
       "sleV2Dhcp4PENonPEControlTimer": sleV2Dhcp4PENonPEControlTimer,
       "sleV2Dhcp4PENonPEControlTimeStamp": sleV2Dhcp4PENonPEControlTimeStamp,
       "sleV2Dhcp4PENonPEControlReqResult": sleV2Dhcp4PENonPEControlReqResult,
       "sleV2Dhcp4PENonPEControlPoolIndex": sleV2Dhcp4PENonPEControlPoolIndex,
       "sleV2Dhcp4PENonPEControlStart": sleV2Dhcp4PENonPEControlStart,
       "sleV2Dhcp4PENonPEControlEnd": sleV2Dhcp4PENonPEControlEnd,
       "sleV2Dhcp4PENonPENotification": sleV2Dhcp4PENonPENotification,
       "sleV2Dhcp4PENonPECreated": sleV2Dhcp4PENonPECreated,
       "sleV2Dhcp4PENonPEDestroyed": sleV2Dhcp4PENonPEDestroyed,
       "sleV2Dhcp4Option82": sleV2Dhcp4Option82,
       "sleV2Dhcp4Option82Port": sleV2Dhcp4Option82Port,
       "sleV2Dhcp4Option82PortTable": sleV2Dhcp4Option82PortTable,
       "sleV2Dhcp4Option82PortEntry": sleV2Dhcp4Option82PortEntry,
       "sleV2Dhcp4Option82PortIndex": sleV2Dhcp4Option82PortIndex,
       "sleV2Dhcp4Option82PortCircuitType": sleV2Dhcp4Option82PortCircuitType,
       "sleV2Dhcp4Option82PortCircuitId": sleV2Dhcp4Option82PortCircuitId,
       "sleV2Dhcp4Option82PortTrustState": sleV2Dhcp4Option82PortTrustState,
       "sleV2Dhcp4Option82PortPolicy": sleV2Dhcp4Option82PortPolicy,
       "sleV2Dhcp4Option82PortPolicyDrop": sleV2Dhcp4Option82PortPolicyDrop,
       "sleV2Dhcp4Option82PortControl": sleV2Dhcp4Option82PortControl,
       "sleV2Dhcp4Option82PortControlRequest": sleV2Dhcp4Option82PortControlRequest,
       "sleV2Dhcp4Option82PortControlStatus": sleV2Dhcp4Option82PortControlStatus,
       "sleV2Dhcp4Option82PortControlTimer": sleV2Dhcp4Option82PortControlTimer,
       "sleV2Dhcp4Option82PortControlTimeStamp": sleV2Dhcp4Option82PortControlTimeStamp,
       "sleV2Dhcp4Option82PortControlReqResult": sleV2Dhcp4Option82PortControlReqResult,
       "sleV2Dhcp4Option82PortControlIndex": sleV2Dhcp4Option82PortControlIndex,
       "sleV2Dhcp4Option82PortControlCircuitType": sleV2Dhcp4Option82PortControlCircuitType,
       "sleV2Dhcp4Option82PortControlCircuitId": sleV2Dhcp4Option82PortControlCircuitId,
       "sleV2Dhcp4Option82PortControlTrustState": sleV2Dhcp4Option82PortControlTrustState,
       "sleV2Dhcp4Option82PortControlPolicy": sleV2Dhcp4Option82PortControlPolicy,
       "sleV2Dhcp4Option82PortControlPolicyDrop": sleV2Dhcp4Option82PortControlPolicyDrop,
       "sleV2Dhcp4Option82PortNotification": sleV2Dhcp4Option82PortNotification,
       "sleV2Dhcp4Option82PortCircuitIdChanged": sleV2Dhcp4Option82PortCircuitIdChanged,
       "sleV2Dhcp4Option82PortTrustStateChanged": sleV2Dhcp4Option82PortTrustStateChanged,
       "sleV2Dhcp4Option82PortCircuitIdCleared": sleV2Dhcp4Option82PortCircuitIdCleared,
       "sleV2Dhcp4Option82PortPolicyChanged": sleV2Dhcp4Option82PortPolicyChanged,
       "sleV2Dhcp4RelayInfo": sleV2Dhcp4RelayInfo,
       "sleV2Dhcp4Remote": sleV2Dhcp4Remote,
       "sleV2Dhcp4RemoteTable": sleV2Dhcp4RemoteTable,
       "sleV2Dhcp4RemoteEntry": sleV2Dhcp4RemoteEntry,
       "sleV2Dhcp4RemoteId": sleV2Dhcp4RemoteId,
       "sleV2Dhcp4RemoteType": sleV2Dhcp4RemoteType,
       "sleV2Dhcp4RemoteClass": sleV2Dhcp4RemoteClass,
       "sleV2Dhcp4RemoteTrust": sleV2Dhcp4RemoteTrust,
       "sleV2Dhcp4RemoteLeaseLimit": sleV2Dhcp4RemoteLeaseLimit,
       "sleV2Dhcp4RemoteLeaseCnt": sleV2Dhcp4RemoteLeaseCnt,
       "sleV2Dhcp4RemoteControl": sleV2Dhcp4RemoteControl,
       "sleV2Dhcp4RemoteControlRequest": sleV2Dhcp4RemoteControlRequest,
       "sleV2Dhcp4RemoteControlStatus": sleV2Dhcp4RemoteControlStatus,
       "sleV2Dhcp4RemoteControlTimer": sleV2Dhcp4RemoteControlTimer,
       "sleV2Dhcp4RemoteControlTimeStamp": sleV2Dhcp4RemoteControlTimeStamp,
       "sleV2Dhcp4RemoteControlReqResult": sleV2Dhcp4RemoteControlReqResult,
       "sleV2Dhcp4RemoteControlId": sleV2Dhcp4RemoteControlId,
       "sleV2Dhcp4RemoteControlType": sleV2Dhcp4RemoteControlType,
       "sleV2Dhcp4RemoteControlClass": sleV2Dhcp4RemoteControlClass,
       "sleV2Dhcp4RemoteControlTrust": sleV2Dhcp4RemoteControlTrust,
       "sleV4Dhcp4RemoteControlLeaseLimit": sleV4Dhcp4RemoteControlLeaseLimit,
       "sleV2Dhcp4RemoteNotification": sleV2Dhcp4RemoteNotification,
       "sleV2Dhcp4RemoteCreated": sleV2Dhcp4RemoteCreated,
       "sleV2Dhcp4RemoteDestroyed": sleV2Dhcp4RemoteDestroyed,
       "sleV2Dhcp4RemoteChanged": sleV2Dhcp4RemoteChanged,
       "sleV2Dhcp4RemoteCleared": sleV2Dhcp4RemoteCleared,
       "sleV2Dhcp4RCircuit": sleV2Dhcp4RCircuit,
       "sleV2Dhcp4RCircuitTable": sleV2Dhcp4RCircuitTable,
       "sleV2Dhcp4RCircuitEntry": sleV2Dhcp4RCircuitEntry,
       "sleV2Dhcp4RCircuitId": sleV2Dhcp4RCircuitId,
       "sleV2Dhcp4RCircuitType": sleV2Dhcp4RCircuitType,
       "sleV2Dhcp4RCircuitClass": sleV2Dhcp4RCircuitClass,
       "sleV2Dhcp4RCircuitLeaseLimit": sleV2Dhcp4RCircuitLeaseLimit,
       "sleV2Dhcp4RCircuitLeaseCnt": sleV2Dhcp4RCircuitLeaseCnt,
       "sleV2Dhcp4RCircuitControl": sleV2Dhcp4RCircuitControl,
       "sleV2Dhcp4RCircuitControlRequest": sleV2Dhcp4RCircuitControlRequest,
       "sleV2Dhcp4RCircuitControlStatus": sleV2Dhcp4RCircuitControlStatus,
       "sleV2Dhcp4RCircuitControlTimer": sleV2Dhcp4RCircuitControlTimer,
       "sleV2Dhcp4RCircuitControlTimeStamp": sleV2Dhcp4RCircuitControlTimeStamp,
       "sleV2Dhcp4RCircuitControlReqResult": sleV2Dhcp4RCircuitControlReqResult,
       "sleV2Dhcp4RCircuitControlRemote": sleV2Dhcp4RCircuitControlRemote,
       "sleV2Dhcp4RCircuitControlId": sleV2Dhcp4RCircuitControlId,
       "sleV2Dhcp4RCircuitControlType": sleV2Dhcp4RCircuitControlType,
       "sleV2Dhcp4RCircuitControlClass": sleV2Dhcp4RCircuitControlClass,
       "sleV2Dhcp4RCircuitControlLeaseLimit": sleV2Dhcp4RCircuitControlLeaseLimit,
       "sleV2Dhcp4RCircuitNotification": sleV2Dhcp4RCircuitNotification,
       "sleV2Dhcp4RCircuitCreated": sleV2Dhcp4RCircuitCreated,
       "sleV2Dhcp4RCircuitDestroyed": sleV2Dhcp4RCircuitDestroyed,
       "sleV2Dhcp4RCircuitCleared": sleV2Dhcp4RCircuitCleared,
       "sleV2Dhcp4RCircuitChanged": sleV2Dhcp4RCircuitChanged,
       "sleV2Dhcp4Class": sleV2Dhcp4Class,
       "sleV2Dhcp4ClassBase": sleV2Dhcp4ClassBase,
       "sleV2Dhcp4ClassTable": sleV2Dhcp4ClassTable,
       "sleV2Dhcp4ClassEntry": sleV2Dhcp4ClassEntry,
       "sleV2Dhcp4ClassName": sleV2Dhcp4ClassName,
       "sleV2Dhcp4ClassControl": sleV2Dhcp4ClassControl,
       "sleV2Dhcp4ClassControlRequest": sleV2Dhcp4ClassControlRequest,
       "sleV2Dhcp4ClassControlStatus": sleV2Dhcp4ClassControlStatus,
       "sleV2Dhcp4ClassControlTimer": sleV2Dhcp4ClassControlTimer,
       "sleV2Dhcp4ClassControlTimeStamp": sleV2Dhcp4ClassControlTimeStamp,
       "sleV2Dhcp4ClassControlReqResult": sleV2Dhcp4ClassControlReqResult,
       "sleV2Dhcp4ClassControlName": sleV2Dhcp4ClassControlName,
       "sleV2Dhcp4ClassNotification": sleV2Dhcp4ClassNotification,
       "sleV2Dhcp4ClassCreated": sleV2Dhcp4ClassCreated,
       "sleV2Dhcp4ClassDestroyed": sleV2Dhcp4ClassDestroyed,
       "sleV2Dhcp4CRCMap": sleV2Dhcp4CRCMap,
       "sleV2Dhcp4CRCMapTable": sleV2Dhcp4CRCMapTable,
       "sleV2Dhcp4CRCMapEntry": sleV2Dhcp4CRCMapEntry,
       "sleV2Dhcp4CRCMapClass": sleV2Dhcp4CRCMapClass,
       "sleV2Dhcp4CRCMapRemote": sleV2Dhcp4CRCMapRemote,
       "sleV2Dhcp4CRCMapCircuit": sleV2Dhcp4CRCMapCircuit,
       "sleV2Dhcp4CRCMapControl": sleV2Dhcp4CRCMapControl,
       "sleV2Dhcp4CRCMapControlRequest": sleV2Dhcp4CRCMapControlRequest,
       "sleV2Dhcp4CRCMapControlStatus": sleV2Dhcp4CRCMapControlStatus,
       "sleV2Dhcp4CRCMapControlTimer": sleV2Dhcp4CRCMapControlTimer,
       "sleV2Dhcp4CRCMapControlTimeStamp": sleV2Dhcp4CRCMapControlTimeStamp,
       "sleV2Dhcp4CRCMapControlReqResult": sleV2Dhcp4CRCMapControlReqResult,
       "sleV2Dhcp4CRCMapControlClass": sleV2Dhcp4CRCMapControlClass,
       "sleV2Dhcp4CRCMapControlRemote": sleV2Dhcp4CRCMapControlRemote,
       "sleV2Dhcp4CRCMapNotification": sleV2Dhcp4CRCMapNotification,
       "sleV2Dhcp4CRCMapCircuitCleared": sleV2Dhcp4CRCMapCircuitCleared,
       "sleV2Dhcp4CRCMapRemoteCleared": sleV2Dhcp4CRCMapRemoteCleared,
       "sleV2Dhcp4ClassRange": sleV2Dhcp4ClassRange,
       "sleV2Dhcp4ClassRangeTable": sleV2Dhcp4ClassRangeTable,
       "sleV2Dhcp4ClassRangeEntry": sleV2Dhcp4ClassRangeEntry,
       "sleV2Dhcp4ClassRangeStart": sleV2Dhcp4ClassRangeStart,
       "sleV2Dhcp4ClassRangeEnd": sleV2Dhcp4ClassRangeEnd,
       "sleV2Dhcp4ClassRangeControl": sleV2Dhcp4ClassRangeControl,
       "sleV2Dhcp4ClassRangeControlRequest": sleV2Dhcp4ClassRangeControlRequest,
       "sleV2Dhcp4ClassRangeControlStatus": sleV2Dhcp4ClassRangeControlStatus,
       "sleV2Dhcp4ClassRangeControlTimer": sleV2Dhcp4ClassRangeControlTimer,
       "sleV2Dhcp4ClassRangeControlTimeStamp": sleV2Dhcp4ClassRangeControlTimeStamp,
       "sleV2Dhcp4ClassRangeControlReqResult": sleV2Dhcp4ClassRangeControlReqResult,
       "sleV2Dhcp4ClassRangeControlPoolIndex": sleV2Dhcp4ClassRangeControlPoolIndex,
       "sleV2Dhcp4ClassRangeControlName": sleV2Dhcp4ClassRangeControlName,
       "sleV2Dhcp4ClassRangeControlStart": sleV2Dhcp4ClassRangeControlStart,
       "sleV2Dhcp4ClassRangeControlEnd": sleV2Dhcp4ClassRangeControlEnd,
       "sleV2Dhcp4ClassRangeNotification": sleV2Dhcp4ClassRangeNotification,
       "sleV2Dhcp4ClassRangeCreated": sleV2Dhcp4ClassRangeCreated,
       "sleV2Dhcp4ClassRangeDestroyed": sleV2Dhcp4ClassRangeDestroyed,
       "sleV2Dhcp4OptionFormat": sleV2Dhcp4OptionFormat,
       "sleV2Dhcp4OptionFormatBase": sleV2Dhcp4OptionFormatBase,
       "sleV2Dhcp4OptionFormatTable": sleV2Dhcp4OptionFormatTable,
       "sleV2Dhcp4OptionFormatEntry": sleV2Dhcp4OptionFormatEntry,
       "sleV2Dhcp4OptionFormatName": sleV2Dhcp4OptionFormatName,
       "sleV2Dhcp4OptionFormatControl": sleV2Dhcp4OptionFormatControl,
       "sleV2Dhcp4OptionFormatControlRequest": sleV2Dhcp4OptionFormatControlRequest,
       "sleV2Dhcp4OptionFormatControlStatus": sleV2Dhcp4OptionFormatControlStatus,
       "sleV2Dhcp4OptionFormatControlTimer": sleV2Dhcp4OptionFormatControlTimer,
       "sleV2Dhcp4OptionFormatControlTimeStamp": sleV2Dhcp4OptionFormatControlTimeStamp,
       "sleV2Dhcp4OptionFormatControlReqResult": sleV2Dhcp4OptionFormatControlReqResult,
       "sleV2Dhcp4OptionFormatControlName": sleV2Dhcp4OptionFormatControlName,
       "sleV2Dhcp4OptionFormatNotification": sleV2Dhcp4OptionFormatNotification,
       "sleV2Dhcp4OptionFormatCreated": sleV2Dhcp4OptionFormatCreated,
       "sleV2Dhcp4OptionFormatDestroyed": sleV2Dhcp4OptionFormatDestroyed,
       "sleV2Dhcp4OptionFormatAttribute": sleV2Dhcp4OptionFormatAttribute,
       "sleV2Dhcp4OptionFormatAttrTable": sleV2Dhcp4OptionFormatAttrTable,
       "sleV2Dhcp4OptionFormatAttrEntry": sleV2Dhcp4OptionFormatAttrEntry,
       "sleV2Dhcp4OptionFormatAttrID": sleV2Dhcp4OptionFormatAttrID,
       "sleV2Dhcp4OptionFormatAttrLength": sleV2Dhcp4OptionFormatAttrLength,
       "sleV2Dhcp4OptionFormatAttrHiddenLength": sleV2Dhcp4OptionFormatAttrHiddenLength,
       "sleV2Dhcp4OptionFormatAttrType": sleV2Dhcp4OptionFormatAttrType,
       "sleV2Dhcp4OptionFormatAttrVarType": sleV2Dhcp4OptionFormatAttrVarType,
       "sleV2Dhcp4OptionFormatAttrVarValue": sleV2Dhcp4OptionFormatAttrVarValue,
       "sleV2Dhcp4OptionFormatAttrControl": sleV2Dhcp4OptionFormatAttrControl,
       "sleV2Dhcp4OptionFormatAttrControlRequest": sleV2Dhcp4OptionFormatAttrControlRequest,
       "sleV2Dhcp4OptionFormatAttrControlStatus": sleV2Dhcp4OptionFormatAttrControlStatus,
       "sleV2Dhcp4OptionFormatAttrControlTimer": sleV2Dhcp4OptionFormatAttrControlTimer,
       "sleV2Dhcp4OptionFormatAttrControlTimeStamp": sleV2Dhcp4OptionFormatAttrControlTimeStamp,
       "sleV2Dhcp4OptionFormatAttrControlReqResult": sleV2Dhcp4OptionFormatAttrControlReqResult,
       "sleV2Dhcp4OptionFormatAttrControlName": sleV2Dhcp4OptionFormatAttrControlName,
       "sleV2Dhcp4OptionFormatAttrControlID": sleV2Dhcp4OptionFormatAttrControlID,
       "sleV2Dhcp4OptionFormatAttrControlLength": sleV2Dhcp4OptionFormatAttrControlLength,
       "sleV2Dhcp4OptionFormatAttrControlHiddenLength": sleV2Dhcp4OptionFormatAttrControlHiddenLength,
       "sleV2Dhcp4OptionFormatAttrControlType": sleV2Dhcp4OptionFormatAttrControlType,
       "sleV2Dhcp4OptionFormatAttrControlVarType": sleV2Dhcp4OptionFormatAttrControlVarType,
       "sleV2Dhcp4OptionFormatAttrControlVarValue": sleV2Dhcp4OptionFormatAttrControlVarValue,
       "sleV2Dhcp4OptionFormatAttrNotification": sleV2Dhcp4OptionFormatAttrNotification,
       "sleV2Dhcp4OptionFormatAttrAdded": sleV2Dhcp4OptionFormatAttrAdded,
       "sleV2Dhcp4OptionFormatAttrDeleted": sleV2Dhcp4OptionFormatAttrDeleted,
       "sleV2Dhcp4OptionFormatAttrModified": sleV2Dhcp4OptionFormatAttrModified,
       "sleV2Dhcp4Filter": sleV2Dhcp4Filter,
       "sleV2Dhcp4FilterPort": sleV2Dhcp4FilterPort,
       "sleV2Dhcp4FilterPortTable": sleV2Dhcp4FilterPortTable,
       "sleV2Dhcp4FilterPortEntry": sleV2Dhcp4FilterPortEntry,
       "sleV2Dhcp4FilterPortIndex": sleV2Dhcp4FilterPortIndex,
       "sleV2Dhcp4FilterPortState": sleV2Dhcp4FilterPortState,
       "sleV2Dhcp4FilterPortControl": sleV2Dhcp4FilterPortControl,
       "sleV2Dhcp4FilterPortControlRequest": sleV2Dhcp4FilterPortControlRequest,
       "sleV2Dhcp4FilterPortControlStatus": sleV2Dhcp4FilterPortControlStatus,
       "sleV2Dhcp4FilterPortControlTimer": sleV2Dhcp4FilterPortControlTimer,
       "sleV2Dhcp4FilterPortControlTimeStamp": sleV2Dhcp4FilterPortControlTimeStamp,
       "sleV2Dhcp4FilterPortControlReqResult": sleV2Dhcp4FilterPortControlReqResult,
       "sleV2Dhcp4FilterPortControlIndex": sleV2Dhcp4FilterPortControlIndex,
       "sleV2Dhcp4FilterPortControlState": sleV2Dhcp4FilterPortControlState,
       "sleV2Dhcp4FilterPortNotification": sleV2Dhcp4FilterPortNotification,
       "sleV2Dhcp4FilterPortStateChanged": sleV2Dhcp4FilterPortStateChanged,
       "sleV2Dhcp4FilterAddress": sleV2Dhcp4FilterAddress,
       "sleV2Dhcp4FilterAddressTable": sleV2Dhcp4FilterAddressTable,
       "sleV2Dhcp4FilterAddressEntry": sleV2Dhcp4FilterAddressEntry,
       "sleV2Dhcp4FilterAddressMac": sleV2Dhcp4FilterAddressMac,
       "sleV2Dhcp4FilterAddressType": sleV2Dhcp4FilterAddressType,
       "sleV2Dhcp4FilterAddressControl": sleV2Dhcp4FilterAddressControl,
       "sleV2Dhcp4FilterAddressControlRequest": sleV2Dhcp4FilterAddressControlRequest,
       "sleV2Dhcp4FilterAddressControlStatus": sleV2Dhcp4FilterAddressControlStatus,
       "sleV2Dhcp4FilterAddressControlTimer": sleV2Dhcp4FilterAddressControlTimer,
       "sleV2Dhcp4FilterAddressControlTimeStamp": sleV2Dhcp4FilterAddressControlTimeStamp,
       "sleV2Dhcp4FilterAddressControlReqResult": sleV2Dhcp4FilterAddressControlReqResult,
       "sleV2Dhcp4FilterAddressControlMac": sleV2Dhcp4FilterAddressControlMac,
       "sleV2Dhcp4FilterAddressControlType": sleV2Dhcp4FilterAddressControlType,
       "sleV2Dhcp4FilterAddressNotification": sleV2Dhcp4FilterAddressNotification,
       "sleV2Dhcp4FilterAddressCreated": sleV2Dhcp4FilterAddressCreated,
       "sleV2Dhcp4FilterAddressDestroyed": sleV2Dhcp4FilterAddressDestroyed,
       "sleV2Dhcp4Illegal": sleV2Dhcp4Illegal,
       "sleV2Dhcp4IllegalTable": sleV2Dhcp4IllegalTable,
       "sleV2Dhcp4IllegalEntry": sleV2Dhcp4IllegalEntry,
       "sleV2Dhcp4IllegalAddress": sleV2Dhcp4IllegalAddress,
       "sleV2Dhcp4IllegalMac": sleV2Dhcp4IllegalMac,
       "sleV2Dhcp4IllegalTime": sleV2Dhcp4IllegalTime,
       "sleV2Dhcp4IllegalControl": sleV2Dhcp4IllegalControl,
       "sleV2Dhcp4IllegalControlRequest": sleV2Dhcp4IllegalControlRequest,
       "sleV2Dhcp4IllegalControlStatus": sleV2Dhcp4IllegalControlStatus,
       "sleV2Dhcp4IllegalControlTimer": sleV2Dhcp4IllegalControlTimer,
       "sleV2Dhcp4IllegalControlTimeStamp": sleV2Dhcp4IllegalControlTimeStamp,
       "sleV2Dhcp4IllegalControlReqResult": sleV2Dhcp4IllegalControlReqResult,
       "sleV2Dhcp4IllegalNotification": sleV2Dhcp4IllegalNotification,
       "sleV2Dhcp4IllegalCleared": sleV2Dhcp4IllegalCleared,
       "sleV2Dhcp4Stats": sleV2Dhcp4Stats,
       "sleV2Dhcp4PacketStats": sleV2Dhcp4PacketStats,
       "sleV2Dhcp4PacketStatsInfo": sleV2Dhcp4PacketStatsInfo,
       "sleV2Dhcp4PacketStatsReceived": sleV2Dhcp4PacketStatsReceived,
       "sleV2Dhcp4PacketStatsSent": sleV2Dhcp4PacketStatsSent,
       "sleV2Dhcp4PacketStatsReceivedErrors": sleV2Dhcp4PacketStatsReceivedErrors,
       "sleV2Dhcp4PacketStatsSentErrors": sleV2Dhcp4PacketStatsSentErrors,
       "sleV2Dhcp4PacketStatsBootpReceivedRequests": sleV2Dhcp4PacketStatsBootpReceivedRequests,
       "sleV2Dhcp4PacketStatsBootpReceivedReplies": sleV2Dhcp4PacketStatsBootpReceivedReplies,
       "sleV2Dhcp4PacketStatsBootpSentRequests": sleV2Dhcp4PacketStatsBootpSentRequests,
       "sleV2Dhcp4PacketStatsBootpSentReplies": sleV2Dhcp4PacketStatsBootpSentReplies,
       "sleV2Dhcp4PacketStatsReceivedDiscover": sleV2Dhcp4PacketStatsReceivedDiscover,
       "sleV2Dhcp4PacketStatsReceivedRequest": sleV2Dhcp4PacketStatsReceivedRequest,
       "sleV2Dhcp4PacketStatsReceivedRelease": sleV2Dhcp4PacketStatsReceivedRelease,
       "sleV2Dhcp4PacketStatscReceivedInform": sleV2Dhcp4PacketStatscReceivedInform,
       "sleV2Dhcp4PacketStatsReceivedDecline": sleV2Dhcp4PacketStatsReceivedDecline,
       "sleV2Dhcp4PacketStatsSentOffer": sleV2Dhcp4PacketStatsSentOffer,
       "sleV2Dhcp4PacketStatsSentAck": sleV2Dhcp4PacketStatsSentAck,
       "sleV2Dhcp4PacketStatsSentNak": sleV2Dhcp4PacketStatsSentNak,
       "sleV2Dhcp4SummaryPoolCnt": sleV2Dhcp4SummaryPoolCnt,
       "sleV2Dhcp4SummaryTotal": sleV2Dhcp4SummaryTotal,
       "sleV2Dhcp4SummaryAvailable": sleV2Dhcp4SummaryAvailable,
       "sleV2Dhcp4SummaryAbandon": sleV2Dhcp4SummaryAbandon,
       "sleV2Dhcp4SummaryBound": sleV2Dhcp4SummaryBound,
       "sleV2Dhcp4SummaryOffered": sleV2Dhcp4SummaryOffered,
       "sleV2Dhcp4SummaryFixed": sleV2Dhcp4SummaryFixed,
       "sleV2Dhcp4SummaryAllocated": sleV2Dhcp4SummaryAllocated,
       "sleV2Dhcp4PacketStatsControl": sleV2Dhcp4PacketStatsControl,
       "sleV2Dhcp4PacketStatsControlRequest": sleV2Dhcp4PacketStatsControlRequest,
       "sleV2Dhcp4PacketStatsControlStatus": sleV2Dhcp4PacketStatsControlStatus,
       "sleV2Dhcp4PacketStatsControlTimer": sleV2Dhcp4PacketStatsControlTimer,
       "sleV2Dhcp4PacketStatsControlTimeStamp": sleV2Dhcp4PacketStatsControlTimeStamp,
       "sleV2Dhcp4PacketStatsControlReqResult": sleV2Dhcp4PacketStatsControlReqResult,
       "sleV2Dhcp4PacketStatsNotification": sleV2Dhcp4PacketStatsNotification,
       "sleV2Dhcp4PacketStatsCleared": sleV2Dhcp4PacketStatsCleared,
       "sleV2Dhcp4Leased": sleV2Dhcp4Leased,
       "sleV2Dhcp4LeasedTable": sleV2Dhcp4LeasedTable,
       "sleV2Dhcp4LeasedEntry": sleV2Dhcp4LeasedEntry,
       "sleV2Dhcp4LeasedAddress": sleV2Dhcp4LeasedAddress,
       "sleV2Dhcp4LeasedPoolIndex": sleV2Dhcp4LeasedPoolIndex,
       "sleV2Dhcp4LeasedStatus": sleV2Dhcp4LeasedStatus,
       "sleV2Dhcp4LeasedMac": sleV2Dhcp4LeasedMac,
       "sleV2Dhcp4LeasedHostName": sleV2Dhcp4LeasedHostName,
       "sleV2Dhcp4LeasedClientId": sleV2Dhcp4LeasedClientId,
       "sleV2Dhcp4LeasedRemoteId": sleV2Dhcp4LeasedRemoteId,
       "sleV2Dhcp4LeasedCircuitId": sleV2Dhcp4LeasedCircuitId,
       "sleV2Dhcp4LeasedStartTime": sleV2Dhcp4LeasedStartTime,
       "sleV2Dhcp4LeasedFinishTime": sleV2Dhcp4LeasedFinishTime,
       "sleV2Dhcp4LeasedControl": sleV2Dhcp4LeasedControl,
       "sleV2Dhcp4LeasedControlRequest": sleV2Dhcp4LeasedControlRequest,
       "sleV2Dhcp4LeasedControlStatus": sleV2Dhcp4LeasedControlStatus,
       "sleV2Dhcp4LeasedControlTimer": sleV2Dhcp4LeasedControlTimer,
       "sleV2Dhcp4LeasedControlTimeStamp": sleV2Dhcp4LeasedControlTimeStamp,
       "sleV2Dhcp4LeasedControlReqResult": sleV2Dhcp4LeasedControlReqResult,
       "sleV2Dhcp4LeasedControlAddress": sleV2Dhcp4LeasedControlAddress,
       "sleV2Dhcp4LeasedControlMask": sleV2Dhcp4LeasedControlMask,
       "sleV2Dhcp4LeasedControlPoolIndex": sleV2Dhcp4LeasedControlPoolIndex,
       "sleV2Dhcp4LeasedNotification": sleV2Dhcp4LeasedNotification,
       "sleV2Dhcp4LeasedAddressCleared": sleV2Dhcp4LeasedAddressCleared,
       "sleV2Dhcp4LeasedNetworkCleared": sleV2Dhcp4LeasedNetworkCleared,
       "sleV2Dhcp4LeasedPoolCleared": sleV2Dhcp4LeasedPoolCleared,
       "sleV2Dhcp4LeasedAllCleared": sleV2Dhcp4LeasedAllCleared,
       "sleV2Dhcp4PacketStatsPort": sleV2Dhcp4PacketStatsPort,
       "sleV2Dhcp4PacketStatsPortTable": sleV2Dhcp4PacketStatsPortTable,
       "sleV2Dhcp4PacketStatsPortEntry": sleV2Dhcp4PacketStatsPortEntry,
       "sleV2Dhcp4PacketStatsPortIndex": sleV2Dhcp4PacketStatsPortIndex,
       "sleV2Dhcp4PacketStatsPortReceived": sleV2Dhcp4PacketStatsPortReceived,
       "sleV2Dhcp4PacketStatsPortSent": sleV2Dhcp4PacketStatsPortSent,
       "sleV2Dhcp4PacketStatsPortReceivedError": sleV2Dhcp4PacketStatsPortReceivedError,
       "sleV2Dhcp4PacketStatsPortSentError": sleV2Dhcp4PacketStatsPortSentError,
       "sleV2Dhcp4PacketStatsPortReceivedDiscover": sleV2Dhcp4PacketStatsPortReceivedDiscover,
       "sleV2Dhcp4PacketStatsPortReceivedRequest": sleV2Dhcp4PacketStatsPortReceivedRequest,
       "sleV2Dhcp4PacketStatsPortReceivedRelease": sleV2Dhcp4PacketStatsPortReceivedRelease,
       "sleV2Dhcp4PacketStatsPortReceivedInform": sleV2Dhcp4PacketStatsPortReceivedInform,
       "sleV2Dhcp4PacketStatsPortReceivedDecline": sleV2Dhcp4PacketStatsPortReceivedDecline,
       "sleV2Dhcp4PacketStatsPortSentOffer": sleV2Dhcp4PacketStatsPortSentOffer,
       "sleV2Dhcp4PacketStatsPortSentAck": sleV2Dhcp4PacketStatsPortSentAck,
       "sleV2Dhcp4PacketStatsPortSentNak": sleV2Dhcp4PacketStatsPortSentNak,
       "sleV2Dhcp4State": sleV2Dhcp4State,
       "sleV2Dhcp4StateTable": sleV2Dhcp4StateTable,
       "sleV2Dhcp4StateEntry": sleV2Dhcp4StateEntry,
       "sleV2Dhcp4StateIndex": sleV2Dhcp4StateIndex,
       "sleV2Dhcp4StateTotal": sleV2Dhcp4StateTotal,
       "sleV2Dhcp4StateFixed": sleV2Dhcp4StateFixed,
       "sleV2Dhcp4StateDynamic": sleV2Dhcp4StateDynamic,
       "sleV2Dhcp4StatePEntry": sleV2Dhcp4StatePEntry,
       "sleV2Dhcp4StatePoolTable": sleV2Dhcp4StatePoolTable,
       "sleV2Dhcp4StatePoolEntry": sleV2Dhcp4StatePoolEntry,
       "sleV2Dhcp4StatePoolTotal": sleV2Dhcp4StatePoolTotal,
       "sleV2Dhcp4StatePoolFixed": sleV2Dhcp4StatePoolFixed,
       "sleV2Dhcp4StatePoolDynamic": sleV2Dhcp4StatePoolDynamic,
       "sleV2Dhcp4StatePoolPEntry": sleV2Dhcp4StatePoolPEntry,
       "sleV2Dhcp4StateBindTable": sleV2Dhcp4StateBindTable,
       "sleV2Dhcp4StateBindEntry": sleV2Dhcp4StateBindEntry,
       "sleV2Dhcp4StateBindIpAddress": sleV2Dhcp4StateBindIpAddress,
       "sleV2Dhcp4StateBindPoolIndex": sleV2Dhcp4StateBindPoolIndex,
       "sleV2Dhcp4StateBindMac": sleV2Dhcp4StateBindMac,
       "sleV2Dhcp4StateBindState": sleV2Dhcp4StateBindState,
       "sleV2Dhcp4StateBindType": sleV2Dhcp4StateBindType,
       "sleV2Dhcp4StateBindExpiration": sleV2Dhcp4StateBindExpiration,
       "sleV2Dhcp4StateBindPort": sleV2Dhcp4StateBindPort,
       "sleV2Dhcp4Snooping": sleV2Dhcp4Snooping,
       "sleV2Ds4Base": sleV2Ds4Base,
       "sleV2Ds4Info": sleV2Ds4Info,
       "sleV2Ds4Activity": sleV2Ds4Activity,
       "sleV2Ds4VerifyMacState": sleV2Ds4VerifyMacState,
       "sleV2Ds4DatabaseURL": sleV2Ds4DatabaseURL,
       "sleV2Ds4DatabaseInterval": sleV2Ds4DatabaseInterval,
       "sleV2Ds4ArpInspectionTime": sleV2Ds4ArpInspectionTime,
       "sleV2Ds4LimitRateDiscover": sleV2Ds4LimitRateDiscover,
       "sleV2Ds4LimitRateRequest": sleV2Ds4LimitRateRequest,
       "sleV2Ds4InformationOption": sleV2Ds4InformationOption,
       "sleV2Ds4Control": sleV2Ds4Control,
       "sleV2Ds4ControlRequest": sleV2Ds4ControlRequest,
       "sleV2Ds4ControlStatus": sleV2Ds4ControlStatus,
       "sleV2Ds4ControlTimer": sleV2Ds4ControlTimer,
       "sleV2Ds4ControlTimeStamp": sleV2Ds4ControlTimeStamp,
       "sleV2Ds4ControlReqResult": sleV2Ds4ControlReqResult,
       "sleV2Ds4ControlActivity": sleV2Ds4ControlActivity,
       "sleV2Ds4ControlVerifyMacState": sleV2Ds4ControlVerifyMacState,
       "sleV2Ds4ControlDatabaseURL": sleV2Ds4ControlDatabaseURL,
       "sleV2Ds4ControlDatabaseInterval": sleV2Ds4ControlDatabaseInterval,
       "sleV2Ds4ControlArpInspectionTime": sleV2Ds4ControlArpInspectionTime,
       "sleV2Ds4ControlLimitRateDiscover": sleV2Ds4ControlLimitRateDiscover,
       "sleV2Ds4ControlLimitRateRequest": sleV2Ds4ControlLimitRateRequest,
       "sleV2Ds4ControlInformationOption": sleV2Ds4ControlInformationOption,
       "sleV2Ds4Notification": sleV2Ds4Notification,
       "sleV2Ds4ActivityChanged": sleV2Ds4ActivityChanged,
       "sleV2Ds4VerifyMacStateChanged": sleV2Ds4VerifyMacStateChanged,
       "sleV2Ds4DatabaseProfileChanged": sleV2Ds4DatabaseProfileChanged,
       "sleV2Ds4DatabaseRenewed": sleV2Ds4DatabaseRenewed,
       "sleV2Ds4ArpInspectionTimeChanged": sleV2Ds4ArpInspectionTimeChanged,
       "sleV2Ds4LimitRateDiscoverChanged": sleV2Ds4LimitRateDiscoverChanged,
       "sleV2Ds4LimitRateRequestChanged": sleV2Ds4LimitRateRequestChanged,
       "sleV2Ds4InformationOptionChanged": sleV2Ds4InformationOptionChanged,
       "sleV2Ds4Vlan": sleV2Ds4Vlan,
       "sleV2Ds4VlanTable": sleV2Ds4VlanTable,
       "sleV2Ds4VlanEntry": sleV2Ds4VlanEntry,
       "sleV2Ds4VlanIndex": sleV2Ds4VlanIndex,
       "sleV2Ds4VlanState": sleV2Ds4VlanState,
       "sleV2Ds4VlanControl": sleV2Ds4VlanControl,
       "sleV2Ds4VlanControlRequest": sleV2Ds4VlanControlRequest,
       "sleV2Ds4VlanControlStatus": sleV2Ds4VlanControlStatus,
       "sleV2Ds4VlanControlTimer": sleV2Ds4VlanControlTimer,
       "sleV2Ds4VlanControlTimeStamp": sleV2Ds4VlanControlTimeStamp,
       "sleV2Ds4VlanControlReqResult": sleV2Ds4VlanControlReqResult,
       "sleV2Ds4VlanControlIndex": sleV2Ds4VlanControlIndex,
       "sleV2Ds4VlanControlState": sleV2Ds4VlanControlState,
       "sleV2Ds4VlanNotification": sleV2Ds4VlanNotification,
       "sleV2Ds4VlanStateChanged": sleV2Ds4VlanStateChanged,
       "sleV2Ds4Port": sleV2Ds4Port,
       "sleV2Ds4PortTable": sleV2Ds4PortTable,
       "sleV2Ds4PortEntry": sleV2Ds4PortEntry,
       "sleV2Ds4PortIndex": sleV2Ds4PortIndex,
       "sleV2Ds4PortTrustState": sleV2Ds4PortTrustState,
       "sleV2Ds4PortLimitRate": sleV2Ds4PortLimitRate,
       "sleV2Ds4PortLimitLease": sleV2Ds4PortLimitLease,
       "sleV2Ds4PortSrcGuardState": sleV2Ds4PortSrcGuardState,
       "sleV2Ds4PortTimeout": sleV2Ds4PortTimeout,
       "sleV2Ds4PortStatus": sleV2Ds4PortStatus,
       "sleV2Ds4PortFilterMode": sleV2Ds4PortFilterMode,
       "sleV2Ds4PortFilterDelayTimer": sleV2Ds4PortFilterDelayTimer,
       "sleV2Ds4PortFilterDelayCounter": sleV2Ds4PortFilterDelayCounter,
       "sleV2Ds4PortTrustFilterEgressBcastReqState": sleV2Ds4PortTrustFilterEgressBcastReqState,
       "sleV2Ds4PortControl": sleV2Ds4PortControl,
       "sleV2Ds4PortControlRequest": sleV2Ds4PortControlRequest,
       "sleV2Ds4PortControlStatus": sleV2Ds4PortControlStatus,
       "sleV2Ds4PortControlTimer": sleV2Ds4PortControlTimer,
       "sleV2Ds4PortControlTimeStamp": sleV2Ds4PortControlTimeStamp,
       "sleV2Ds4PortControlReqResult": sleV2Ds4PortControlReqResult,
       "sleV2Ds4PortControlIndex": sleV2Ds4PortControlIndex,
       "sleV2Ds4PortControlTrustState": sleV2Ds4PortControlTrustState,
       "sleV2Ds4PortControlLimitRate": sleV2Ds4PortControlLimitRate,
       "sleV2Ds4PortControlLimitLease": sleV2Ds4PortControlLimitLease,
       "sleV2Ds4PortControlSrcGuardState": sleV2Ds4PortControlSrcGuardState,
       "sleV2Ds4PortControlTimeout": sleV2Ds4PortControlTimeout,
       "sleV2Ds4PortControlPStatus": sleV2Ds4PortControlPStatus,
       "sleV2Ds4PortControlFilterMode": sleV2Ds4PortControlFilterMode,
       "sleV2Ds4PortControlFilterDelayTimer": sleV2Ds4PortControlFilterDelayTimer,
       "sleV2Ds4PortControlFilterDelayCounter": sleV2Ds4PortControlFilterDelayCounter,
       "sleV2Ds4PortControlTrustFilterEgressBcastReqState": sleV2Ds4PortControlTrustFilterEgressBcastReqState,
       "sleV2Ds4PortNotification": sleV2Ds4PortNotification,
       "sleV2Ds4PortTrustStateChanged": sleV2Ds4PortTrustStateChanged,
       "sleV2Ds4PortLimitProfileChagned": sleV2Ds4PortLimitProfileChagned,
       "sleV2Ds4PortSrcGuardStateChanged": sleV2Ds4PortSrcGuardStateChanged,
       "sleV2Ds4PortTimeoutChanged": sleV2Ds4PortTimeoutChanged,
       "sleV2Ds4PortStatusChanged": sleV2Ds4PortStatusChanged,
       "sleV2Ds4PortFilterModeChanged": sleV2Ds4PortFilterModeChanged,
       "sleV2Ds4PortFilterDelayChanged": sleV2Ds4PortFilterDelayChanged,
       "sleV2Ds4PortTrustFilterEgressBcastReqStateChanged": sleV2Ds4PortTrustFilterEgressBcastReqStateChanged,
       "sleV2Ds4Bindings": sleV2Ds4Bindings,
       "sleV2Ds4BindingsTable": sleV2Ds4BindingsTable,
       "sleV2Ds4BindingsEntry": sleV2Ds4BindingsEntry,
       "sleV2Ds4BindingsVlanIndex": sleV2Ds4BindingsVlanIndex,
       "sleV2Ds4BindingsPortIndex": sleV2Ds4BindingsPortIndex,
       "sleV2Ds4BindingsAddress": sleV2Ds4BindingsAddress,
       "sleV2Ds4BindingsMac": sleV2Ds4BindingsMac,
       "sleV2Ds4BindingsType": sleV2Ds4BindingsType,
       "sleV2Ds4BindingsState": sleV2Ds4BindingsState,
       "sleV2Ds4BindingsLeasedTime": sleV2Ds4BindingsLeasedTime,
       "sleV2Ds4BindingsMaskLen": sleV2Ds4BindingsMaskLen,
       "sleV2Ds4BindingsControl": sleV2Ds4BindingsControl,
       "sleV2Ds4BindingsControlRequest": sleV2Ds4BindingsControlRequest,
       "sleV2Ds4BindingsControlStatus": sleV2Ds4BindingsControlStatus,
       "sleV2Ds4BindingsControlTimer": sleV2Ds4BindingsControlTimer,
       "sleV2Ds4BindingsControlTimeStamp": sleV2Ds4BindingsControlTimeStamp,
       "sleV2Ds4BindingsControlReqResult": sleV2Ds4BindingsControlReqResult,
       "sleV2Ds4BindingsControlVlanIndex": sleV2Ds4BindingsControlVlanIndex,
       "sleV2Ds4BindingsControlPortIndex": sleV2Ds4BindingsControlPortIndex,
       "sleV2Ds4BindingsControlAddress": sleV2Ds4BindingsControlAddress,
       "sleV2Ds4BindingsControlMac": sleV2Ds4BindingsControlMac,
       "sleV2Ds4BindingsControlType": sleV2Ds4BindingsControlType,
       "sleV2Ds4BindingsControlLeasedTime": sleV2Ds4BindingsControlLeasedTime,
       "sleV2Ds4BindingsControlMaskLen": sleV2Ds4BindingsControlMaskLen,
       "sleV2Ds4BindingsNotification": sleV2Ds4BindingsNotification,
       "sleV2Ds4BindingsCreated": sleV2Ds4BindingsCreated,
       "sleV2Ds4BindingsDestroyed": sleV2Ds4BindingsDestroyed,
       "sleV2Ds4BindingsCleared": sleV2Ds4BindingsCleared,
       "sleV2Ds4VlanInfoOpt": sleV2Ds4VlanInfoOpt,
       "sleV2Ds4VlanInfoOptTable": sleV2Ds4VlanInfoOptTable,
       "sleV2Ds4VlanInfoOptEntry": sleV2Ds4VlanInfoOptEntry,
       "sleV2Ds4VlanInfoOptIndex": sleV2Ds4VlanInfoOptIndex,
       "sleV2Ds4VlanInfoOptState": sleV2Ds4VlanInfoOptState,
       "sleV2Ds4VlanInforOptControl": sleV2Ds4VlanInforOptControl,
       "sleV2Ds4VlanInfoOptControlRequest": sleV2Ds4VlanInfoOptControlRequest,
       "sleV2Ds4VlanInfoOptControlStatus": sleV2Ds4VlanInfoOptControlStatus,
       "sleV2Ds4VlanInfoOptControlTimer": sleV2Ds4VlanInfoOptControlTimer,
       "sleV2Ds4VlanInfoOptControlTimeStamp": sleV2Ds4VlanInfoOptControlTimeStamp,
       "sleV2Ds4VlanInfoOptControlReqResult": sleV2Ds4VlanInfoOptControlReqResult,
       "sleV2Ds4VlanInfoOptControlIndex": sleV2Ds4VlanInfoOptControlIndex,
       "sleV2Ds4VlanInfoOptControlState": sleV2Ds4VlanInfoOptControlState,
       "sleV2Ds4VlanInfoOptNotification": sleV2Ds4VlanInfoOptNotification,
       "sleV2Ds4VlanInfoOptStateChanged": sleV2Ds4VlanInfoOptStateChanged,
       "sleV2Ds4OptCode": sleV2Ds4OptCode,
       "sleV2Ds4OptCodeTable": sleV2Ds4OptCodeTable,
       "sleV2Ds4OptCodeEntry": sleV2Ds4OptCodeEntry,
       "sleV2Ds4OptCodeIfIndex": sleV2Ds4OptCodeIfIndex,
       "sleV2Ds4OptCodeNum": sleV2Ds4OptCodeNum,
       "sleV2Ds4OptCodeFormat": sleV2Ds4OptCodeFormat,
       "sleV2Ds4OptCodePolicy": sleV2Ds4OptCodePolicy,
       "sleV2Ds4OptCodeControl": sleV2Ds4OptCodeControl,
       "sleV2Ds4OptCodeControlRequest": sleV2Ds4OptCodeControlRequest,
       "sleV2Ds4OptCodeControlStatus": sleV2Ds4OptCodeControlStatus,
       "sleV2Ds4OptCodeControlTimer": sleV2Ds4OptCodeControlTimer,
       "sleV2Ds4OptCodeControlTimeStamp": sleV2Ds4OptCodeControlTimeStamp,
       "sleV2Ds4OptCodeControlReqResult": sleV2Ds4OptCodeControlReqResult,
       "sleV2Ds4OptCodeControlIfIndex": sleV2Ds4OptCodeControlIfIndex,
       "sleV2Ds4OptCodeControlNum": sleV2Ds4OptCodeControlNum,
       "sleV2Ds4OptCodeControlFormat": sleV2Ds4OptCodeControlFormat,
       "sleV2Ds4OptCodeControlPolicy": sleV2Ds4OptCodeControlPolicy,
       "sleV2Ds4OptCodeNotification": sleV2Ds4OptCodeNotification,
       "sleV2Ds4OptCodeFormatChanged": sleV2Ds4OptCodeFormatChanged,
       "sleV2Ds4OptCodePolicyChanged": sleV2Ds4OptCodePolicyChanged,
       "sleV2Ds4OptCodeDestroyed": sleV2Ds4OptCodeDestroyed,
       "sleV2Dhcp4Relay": sleV2Dhcp4Relay,
       "sleV2Dhcp4RelayInterface": sleV2Dhcp4RelayInterface,
       "sleV2Dhcp4RelayIfTable": sleV2Dhcp4RelayIfTable,
       "sleV2Dhcp4RelayIfEntry": sleV2Dhcp4RelayIfEntry,
       "sleV2Dhcp4RelayIfIndex": sleV2Dhcp4RelayIfIndex,
       "sleV2Dhcp4RelayIfSimpleOpt82AdminState": sleV2Dhcp4RelayIfSimpleOpt82AdminState,
       "sleV2Dhcp4RelayIfSimpleOpt82OperState": sleV2Dhcp4RelayIfSimpleOpt82OperState,
       "sleV2Dhcp4RelayIfMaxHops": sleV2Dhcp4RelayIfMaxHops,
       "sleV2Dhcp4RelayIfControl": sleV2Dhcp4RelayIfControl,
       "sleV2Dhcp4RelayIfControlRequest": sleV2Dhcp4RelayIfControlRequest,
       "sleV2Dhcp4RelayIfControlStatus": sleV2Dhcp4RelayIfControlStatus,
       "sleV2Dhcp4RelayIfControlTimer": sleV2Dhcp4RelayIfControlTimer,
       "sleV2Dhcp4RelayIfControlTimeStamp": sleV2Dhcp4RelayIfControlTimeStamp,
       "sleV2Dhcp4RelayIfControllReqResult": sleV2Dhcp4RelayIfControllReqResult,
       "sleV2Dhcp4RelayIfControlIndex": sleV2Dhcp4RelayIfControlIndex,
       "sleV2Dhcp4RelayIfControlSimpleOpt82AdminState": sleV2Dhcp4RelayIfControlSimpleOpt82AdminState,
       "sleV2Dhcp4RelayIfControlMaxHops": sleV2Dhcp4RelayIfControlMaxHops,
       "sleV2Dhcp4RelayIfNotification": sleV2Dhcp4RelayIfNotification,
       "sleV2Dhcp4RelayIfSimpleOpt82AdminStateChanged": sleV2Dhcp4RelayIfSimpleOpt82AdminStateChanged,
       "sleV2Dhcp4RelayIfMaxHopsChanged": sleV2Dhcp4RelayIfMaxHopsChanged,
       "sleV2Dhcp4RelayHelper": sleV2Dhcp4RelayHelper,
       "sleV2Dhcp4RelayHelperTable": sleV2Dhcp4RelayHelperTable,
       "sleV2Dhcp4RelayHelperEntry": sleV2Dhcp4RelayHelperEntry,
       "sleV2Dhcp4RelayHelperOui": sleV2Dhcp4RelayHelperOui,
       "sleV2Dhcp4RelayHelperAddress": sleV2Dhcp4RelayHelperAddress,
       "sleV2Dhcp4RelayHelperType": sleV2Dhcp4RelayHelperType,
       "sleV2Dhcp4RelayHelperControl": sleV2Dhcp4RelayHelperControl,
       "sleV2Dhcp4RelayHelperControlRequest": sleV2Dhcp4RelayHelperControlRequest,
       "sleV2Dhcp4RelayHelperControlStatus": sleV2Dhcp4RelayHelperControlStatus,
       "sleV2Dhcp4RelayHelperControlTimer": sleV2Dhcp4RelayHelperControlTimer,
       "sleV2Dhcp4RelayHelperControlTimeStamp": sleV2Dhcp4RelayHelperControlTimeStamp,
       "sleV2Dhcp4RelayHelperControlReqResult": sleV2Dhcp4RelayHelperControlReqResult,
       "sleV2Dhcp4RelayHelperControlIfIndex": sleV2Dhcp4RelayHelperControlIfIndex,
       "sleV2Dhcp4RelayHelperControlOui": sleV2Dhcp4RelayHelperControlOui,
       "sleV2Dhcp4RelayHelperControlAddress": sleV2Dhcp4RelayHelperControlAddress,
       "sleV2Dhcp4RelayHelperControlType": sleV2Dhcp4RelayHelperControlType,
       "sleV2Dhcp4RelayHelperNotification": sleV2Dhcp4RelayHelperNotification,
       "sleV2Dhcp4RelayHelperCreated": sleV2Dhcp4RelayHelperCreated,
       "sleV2Dhcp4RelayHelperDestroyed": sleV2Dhcp4RelayHelperDestroyed,
       "sleV2Dhcp4RelayHelperCleared": sleV2Dhcp4RelayHelperCleared,
       "sleV2Dhcp4RelayStats": sleV2Dhcp4RelayStats,
       "sleV2Dhcp4RelayIntrStatsTable": sleV2Dhcp4RelayIntrStatsTable,
       "sleV2Dhcp4RelayIntrStatsEntry": sleV2Dhcp4RelayIntrStatsEntry,
       "sleV2Dhcp4RelayIntrIndex": sleV2Dhcp4RelayIntrIndex,
       "sleV2Dhcp4RelayIntrRcvd": sleV2Dhcp4RelayIntrRcvd,
       "sleV2Dhcp4RelayIntrSent": sleV2Dhcp4RelayIntrSent,
       "sleV2Dhcp4RelayIntrRcvdErrors": sleV2Dhcp4RelayIntrRcvdErrors,
       "sleV2Dhcp4RelayIntrSentErrors": sleV2Dhcp4RelayIntrSentErrors,
       "sleV2Dhcp4RelayIntrRcvdBootpRequest": sleV2Dhcp4RelayIntrRcvdBootpRequest,
       "sleV2Dhcp4RelayIntrRcvdBootpReply": sleV2Dhcp4RelayIntrRcvdBootpReply,
       "sleV2Dhcp4RelayIntrSentBootpRequest": sleV2Dhcp4RelayIntrSentBootpRequest,
       "sleV2Dhcp4RelayIntrSentBootpReply": sleV2Dhcp4RelayIntrSentBootpReply,
       "sleV2Dhcp4RelayIntrRcvdDiscover": sleV2Dhcp4RelayIntrRcvdDiscover,
       "sleV2Dhcp4RelayIntrRcvdRequest": sleV2Dhcp4RelayIntrRcvdRequest,
       "sleV2Dhcp4RelayIntrRcvdRelease": sleV2Dhcp4RelayIntrRcvdRelease,
       "sleV2Dhcp4RelayIntrRcvdInform": sleV2Dhcp4RelayIntrRcvdInform,
       "sleV2Dhcp4RelayIntrRcvdDecline": sleV2Dhcp4RelayIntrRcvdDecline,
       "sleV2Dhcp4RelayIntrSentDiscover": sleV2Dhcp4RelayIntrSentDiscover,
       "sleV2Dhcp4RelayIntrSentRequest": sleV2Dhcp4RelayIntrSentRequest,
       "sleV2Dhcp4RelayIntrSentRelease": sleV2Dhcp4RelayIntrSentRelease,
       "sleV2Dhcp4RelayIntrSentInform": sleV2Dhcp4RelayIntrSentInform,
       "sleV2Dhcp4RelayIntrSentDecline": sleV2Dhcp4RelayIntrSentDecline,
       "sleV2Dhcp4RelayIntrRcvdOffer": sleV2Dhcp4RelayIntrRcvdOffer,
       "sleV2Dhcp4RelayIntrRcvdAck": sleV2Dhcp4RelayIntrRcvdAck,
       "sleV2Dhcp4RelayIntrRcvdNack": sleV2Dhcp4RelayIntrRcvdNack,
       "sleV2Dhcp4RelayIntrSentOffer": sleV2Dhcp4RelayIntrSentOffer,
       "sleV2Dhcp4RelayIntrSentAck": sleV2Dhcp4RelayIntrSentAck,
       "sleV2Dhcp4RelayIntrSentNack": sleV2Dhcp4RelayIntrSentNack,
       "sleV2Dhcp4RelayIntrStatsControl": sleV2Dhcp4RelayIntrStatsControl,
       "sleV2Dhcp4RelayIntrStatsControlRequest": sleV2Dhcp4RelayIntrStatsControlRequest,
       "sleV2Dhcp4RelayIntrStatsControlStatus": sleV2Dhcp4RelayIntrStatsControlStatus,
       "sleV2Dhcp4RelayIntrStatsControlTimer": sleV2Dhcp4RelayIntrStatsControlTimer,
       "sleV2Dhcp4RelayIntrStatsControITimeStamp": sleV2Dhcp4RelayIntrStatsControITimeStamp,
       "sleV2Dhcp4RelayIntrStatsControIResult": sleV2Dhcp4RelayIntrStatsControIResult,
       "sleV2Dhcp4RelayIntrStatsControIndex": sleV2Dhcp4RelayIntrStatsControIndex,
       "sleV2Dhcp4RelayIntrStatsNotification": sleV2Dhcp4RelayIntrStatsNotification,
       "sleV2Dhcp4RelayintrStatsCleared": sleV2Dhcp4RelayintrStatsCleared,
       "sleV2Dhcp4Client": sleV2Dhcp4Client,
       "sleV2Dhcp4ClientInterface": sleV2Dhcp4ClientInterface,
       "sleV2Dhcp4ClientIfTable": sleV2Dhcp4ClientIfTable,
       "sleV2Dhcp4ClientIfEntry": sleV2Dhcp4ClientIfEntry,
       "sleV2Dhcp4ClientIfIndex": sleV2Dhcp4ClientIfIndex,
       "sleV2Dhcp4ClientIfActivity": sleV2Dhcp4ClientIfActivity,
       "sleV2Dhcp4ClientIfAddress": sleV2Dhcp4ClientIfAddress,
       "sleV2Dhcp4ClientIfMask": sleV2Dhcp4ClientIfMask,
       "sleV2Dhcp4ClientIfServer": sleV2Dhcp4ClientIfServer,
       "sleV2Dhcp4ClientIfHostName": sleV2Dhcp4ClientIfHostName,
       "sleV2Dhcp4ClientIfRequestFlag": sleV2Dhcp4ClientIfRequestFlag,
       "sleV2Dhcp4ClientIfClientType": sleV2Dhcp4ClientIfClientType,
       "sleV2Dhcp4ClientIfClientId": sleV2Dhcp4ClientIfClientId,
       "sleV2Dhcp4ClientIfClassType": sleV2Dhcp4ClientIfClassType,
       "sleV2Dhcp4ClientIfClassId": sleV2Dhcp4ClientIfClassId,
       "sleV2Dhcp4ClientIfLeasetime": sleV2Dhcp4ClientIfLeasetime,
       "sleV2Dhcp4ClientIfExpired": sleV2Dhcp4ClientIfExpired,
       "sleV2Dhcp4ClientIfState": sleV2Dhcp4ClientIfState,
       "sleV2Dhcp4ClientIfLeasetimeOption": sleV2Dhcp4ClientIfLeasetimeOption,
       "sleV2Dhcp4ClientIfControl": sleV2Dhcp4ClientIfControl,
       "sleV2Dhcp4ClientIfControlRequest": sleV2Dhcp4ClientIfControlRequest,
       "sleV2Dhcp4ClientIfControlStatus": sleV2Dhcp4ClientIfControlStatus,
       "sleV2Dhcp4ClientIfControlTimer": sleV2Dhcp4ClientIfControlTimer,
       "sleV2Dhcp4ClientIfControlTimeStamp": sleV2Dhcp4ClientIfControlTimeStamp,
       "sleV2Dhcp4ClientIfControlReqResult": sleV2Dhcp4ClientIfControlReqResult,
       "sleV2Dhcp4ClientIfControlIndex": sleV2Dhcp4ClientIfControlIndex,
       "sleV2Dhcp4ClientIfControlActivity": sleV2Dhcp4ClientIfControlActivity,
       "sleV2Dhcp4ClientIfControlHostName": sleV2Dhcp4ClientIfControlHostName,
       "sleV2Dhcp4ClientIfControlRequestFlag": sleV2Dhcp4ClientIfControlRequestFlag,
       "sleV2Dhcp4ClientIfControlClientType": sleV2Dhcp4ClientIfControlClientType,
       "sleV2Dhcp4ClientIfControlClientId": sleV2Dhcp4ClientIfControlClientId,
       "sleV2Dhcp4ClientIfControlClassType": sleV2Dhcp4ClientIfControlClassType,
       "sleV2Dhcp4ClientIfControlClassId": sleV2Dhcp4ClientIfControlClassId,
       "sleV2Dhcp4ClientIfControlLeasetime": sleV2Dhcp4ClientIfControlLeasetime,
       "sleV2Dhcp4ClientIfControlLeasetimeOption": sleV2Dhcp4ClientIfControlLeasetimeOption,
       "sleV2Dhcp4ClientIfNotification": sleV2Dhcp4ClientIfNotification,
       "sleV2Dhcp4ClientIfActivityChanged": sleV2Dhcp4ClientIfActivityChanged,
       "sleV2Dhcp4ClientIfProfileChanged": sleV2Dhcp4ClientIfProfileChanged,
       "sleV2Dhcp4ClientIfRenewed": sleV2Dhcp4ClientIfRenewed,
       "sleV2Dhcp4ClientIfReleased": sleV2Dhcp4ClientIfReleased,
       "sleV2Dhcp4ClientIfLeasetimeOptionChanged": sleV2Dhcp4ClientIfLeasetimeOptionChanged,
       "sleV2Dhcp4ClientOption": sleV2Dhcp4ClientOption,
       "sleV2Dhcp4ClientOptionTable": sleV2Dhcp4ClientOptionTable,
       "sleV2Dhcp4ClientOptionEntry": sleV2Dhcp4ClientOptionEntry,
       "sleV2Dhcp4ClientOptionCode": sleV2Dhcp4ClientOptionCode,
       "sleV2Dhcp4ClientOptionInstance": sleV2Dhcp4ClientOptionInstance,
       "sleV2Dhcp4ClientOptionType": sleV2Dhcp4ClientOptionType,
       "sleV2Dhcp4ClientOptionValue": sleV2Dhcp4ClientOptionValue,
       "sleV2Dhcp4Port": sleV2Dhcp4Port,
       "sleV2Dhcp4PortLease": sleV2Dhcp4PortLease,
       "sleV2Dhcp4PortLeaseTable": sleV2Dhcp4PortLeaseTable,
       "sleV2Dhcp4PortLeaseEntry": sleV2Dhcp4PortLeaseEntry,
       "sleV2Dhcp4PortLeaseIndex": sleV2Dhcp4PortLeaseIndex,
       "sleV2Dhcp4PortLeaseLimit": sleV2Dhcp4PortLeaseLimit,
       "sleV2Dhcp4PortLeaseCount": sleV2Dhcp4PortLeaseCount,
       "sleV2Dhcp4PortAddrLeaseTable": sleV2Dhcp4PortAddrLeaseTable,
       "sleV2Dhcp4PortAddrLeaseEntry": sleV2Dhcp4PortAddrLeaseEntry,
       "sleV2Dhcp4PortAddrtLeaseIndex": sleV2Dhcp4PortAddrtLeaseIndex,
       "sleV2Dhcp4PortAddrLeaseAddress": sleV2Dhcp4PortAddrLeaseAddress,
       "sleV2Dhcp4PortAddrLeasePoolIndex": sleV2Dhcp4PortAddrLeasePoolIndex,
       "sleV2Dhcp4PortAddrLeaseStatus": sleV2Dhcp4PortAddrLeaseStatus,
       "sleV2Dhcp4PortAddrLeaseMac": sleV2Dhcp4PortAddrLeaseMac,
       "sleV2Dhcp4PortAddrLeaseHostName": sleV2Dhcp4PortAddrLeaseHostName,
       "sleV2Dhcp4PortAddrLeaseClientId": sleV2Dhcp4PortAddrLeaseClientId,
       "sleV2Dhcp4PortAddrLeaseRemoteId": sleV2Dhcp4PortAddrLeaseRemoteId,
       "sleV2Dhcp4PortAddrLeaseCircuitId": sleV2Dhcp4PortAddrLeaseCircuitId,
       "sleV2Dhcp4PortAddrLeaseStartTime": sleV2Dhcp4PortAddrLeaseStartTime,
       "sleV2Dhcp4PortAddrLeaseFinishTime": sleV2Dhcp4PortAddrLeaseFinishTime,
       "sleV2Dhcp4PortLeaseControl": sleV2Dhcp4PortLeaseControl,
       "sleV2Dhcp4PortLeaseControlRequest": sleV2Dhcp4PortLeaseControlRequest,
       "sleV2Dhcp4PortLeaseControlStatus": sleV2Dhcp4PortLeaseControlStatus,
       "sleV2Dhcp4PortLeaseControlTimer": sleV2Dhcp4PortLeaseControlTimer,
       "sleV2Dhcp4PortLeaseControlTimeStamp": sleV2Dhcp4PortLeaseControlTimeStamp,
       "sleV2Dhcp4PortLeaseControlReqResult": sleV2Dhcp4PortLeaseControlReqResult,
       "sleV2Dhcp4PortLeaseControlIndex": sleV2Dhcp4PortLeaseControlIndex,
       "sleV2Dhcp4PortLeaseControlLimit": sleV2Dhcp4PortLeaseControlLimit,
       "sleV2DhcpPortLeaseNotification": sleV2DhcpPortLeaseNotification,
       "sleV2Dhcp4PortLeaseLimitChanged": sleV2Dhcp4PortLeaseLimitChanged,
       "sleV2Dhcp6": sleV2Dhcp6,
       "sleV2DhcpGroup": sleV2DhcpGroup,
       "sleV2DhcpNotificationGroup": sleV2DhcpNotificationGroup}
)
