# SNMP MIB module (ARUBAWIRED-MCLAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-MCLAG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:13 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

arubaWiredMclagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    arubaWiredMclagMIB.setRevisions(
        ("2018-05-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VidList(TextualConvention, OctetString):
    status = "obsolete"
    displayHint = "512x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512



# MIB Managed Objects in the order of their OIDs

_ArubaWiredMclagConfig_ObjectIdentity = ObjectIdentity
arubaWiredMclagConfig = _ArubaWiredMclagConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1)
)
_ArubaWiredMclagIslConfig_ObjectIdentity = ObjectIdentity
arubaWiredMclagIslConfig = _ArubaWiredMclagIslConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 1)
)
_ArubaWiredMclagIslPort_Type = InterfaceIndex
_ArubaWiredMclagIslPort_Object = MibScalar
arubaWiredMclagIslPort = _ArubaWiredMclagIslPort_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 1, 1),
    _ArubaWiredMclagIslPort_Type()
)
arubaWiredMclagIslPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMclagIslPort.setStatus("obsolete")


class _ArubaWiredMclagIslHelloInterval_Type(Integer32):
    """Custom type arubaWiredMclagIslHelloInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ArubaWiredMclagIslHelloInterval_Type.__name__ = "Integer32"
_ArubaWiredMclagIslHelloInterval_Object = MibScalar
arubaWiredMclagIslHelloInterval = _ArubaWiredMclagIslHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 1, 2),
    _ArubaWiredMclagIslHelloInterval_Type()
)
arubaWiredMclagIslHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMclagIslHelloInterval.setStatus("obsolete")


class _ArubaWiredMclagIslHoldTime_Type(Integer32):
    """Custom type arubaWiredMclagIslHoldTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ArubaWiredMclagIslHoldTime_Type.__name__ = "Integer32"
_ArubaWiredMclagIslHoldTime_Object = MibScalar
arubaWiredMclagIslHoldTime = _ArubaWiredMclagIslHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 1, 3),
    _ArubaWiredMclagIslHoldTime_Type()
)
arubaWiredMclagIslHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMclagIslHoldTime.setStatus("obsolete")


class _ArubaWiredMclagIslHelloTimeout_Type(Integer32):
    """Custom type arubaWiredMclagIslHelloTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_ArubaWiredMclagIslHelloTimeout_Type.__name__ = "Integer32"
_ArubaWiredMclagIslHelloTimeout_Object = MibScalar
arubaWiredMclagIslHelloTimeout = _ArubaWiredMclagIslHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 1, 4),
    _ArubaWiredMclagIslHelloTimeout_Type()
)
arubaWiredMclagIslHelloTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMclagIslHelloTimeout.setStatus("obsolete")


class _ArubaWiredMclagIslDevicePriority_Type(Integer32):
    """Custom type arubaWiredMclagIslDevicePriority based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ArubaWiredMclagIslDevicePriority_Type.__name__ = "Integer32"
_ArubaWiredMclagIslDevicePriority_Object = MibScalar
arubaWiredMclagIslDevicePriority = _ArubaWiredMclagIslDevicePriority_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 1, 5),
    _ArubaWiredMclagIslDevicePriority_Type()
)
arubaWiredMclagIslDevicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMclagIslDevicePriority.setStatus("obsolete")
_ArubaWiredMclagIslSystemID_Type = DisplayString
_ArubaWiredMclagIslSystemID_Object = MibScalar
arubaWiredMclagIslSystemID = _ArubaWiredMclagIslSystemID_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 1, 6),
    _ArubaWiredMclagIslSystemID_Type()
)
arubaWiredMclagIslSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagIslSystemID.setStatus("obsolete")
_ArubaWiredMclagIslPlatformName_Type = DisplayString
_ArubaWiredMclagIslPlatformName_Object = MibScalar
arubaWiredMclagIslPlatformName = _ArubaWiredMclagIslPlatformName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 1, 7),
    _ArubaWiredMclagIslPlatformName_Type()
)
arubaWiredMclagIslPlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagIslPlatformName.setStatus("obsolete")
_ArubaWiredMclagIslSwVersion_Type = DisplayString
_ArubaWiredMclagIslSwVersion_Object = MibScalar
arubaWiredMclagIslSwVersion = _ArubaWiredMclagIslSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 1, 8),
    _ArubaWiredMclagIslSwVersion_Type()
)
arubaWiredMclagIslSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagIslSwVersion.setStatus("obsolete")
_ArubaWiredMclagIslVIDList_Type = VidList
_ArubaWiredMclagIslVIDList_Object = MibScalar
arubaWiredMclagIslVIDList = _ArubaWiredMclagIslVIDList_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 1, 9),
    _ArubaWiredMclagIslVIDList_Type()
)
arubaWiredMclagIslVIDList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagIslVIDList.setStatus("obsolete")
_ArubaWiredMclagKeepAliveConfig_ObjectIdentity = ObjectIdentity
arubaWiredMclagKeepAliveConfig = _ArubaWiredMclagKeepAliveConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 2)
)
_ArubaWiredMclagKeepAliveSrcIPAddrType_Type = InetAddressType
_ArubaWiredMclagKeepAliveSrcIPAddrType_Object = MibScalar
arubaWiredMclagKeepAliveSrcIPAddrType = _ArubaWiredMclagKeepAliveSrcIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 2, 1),
    _ArubaWiredMclagKeepAliveSrcIPAddrType_Type()
)
arubaWiredMclagKeepAliveSrcIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAliveSrcIPAddrType.setStatus("obsolete")
_ArubaWiredMclagKeepAliveSrcIPAddr_Type = InetAddress
_ArubaWiredMclagKeepAliveSrcIPAddr_Object = MibScalar
arubaWiredMclagKeepAliveSrcIPAddr = _ArubaWiredMclagKeepAliveSrcIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 2, 2),
    _ArubaWiredMclagKeepAliveSrcIPAddr_Type()
)
arubaWiredMclagKeepAliveSrcIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAliveSrcIPAddr.setStatus("obsolete")
_ArubaWiredMclagKeepAliveVrf_Type = DisplayString
_ArubaWiredMclagKeepAliveVrf_Object = MibScalar
arubaWiredMclagKeepAliveVrf = _ArubaWiredMclagKeepAliveVrf_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 2, 3),
    _ArubaWiredMclagKeepAliveVrf_Type()
)
arubaWiredMclagKeepAliveVrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAliveVrf.setStatus("obsolete")


class _ArubaWiredMclagKeepAliveUdpPort_Type(Integer32):
    """Custom type arubaWiredMclagKeepAliveUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_ArubaWiredMclagKeepAliveUdpPort_Type.__name__ = "Integer32"
_ArubaWiredMclagKeepAliveUdpPort_Object = MibScalar
arubaWiredMclagKeepAliveUdpPort = _ArubaWiredMclagKeepAliveUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 2, 4),
    _ArubaWiredMclagKeepAliveUdpPort_Type()
)
arubaWiredMclagKeepAliveUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAliveUdpPort.setStatus("obsolete")
_ArubaWiredMclagKeepAlivePeerIPAddrType_Type = InetAddressType
_ArubaWiredMclagKeepAlivePeerIPAddrType_Object = MibScalar
arubaWiredMclagKeepAlivePeerIPAddrType = _ArubaWiredMclagKeepAlivePeerIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 2, 5),
    _ArubaWiredMclagKeepAlivePeerIPAddrType_Type()
)
arubaWiredMclagKeepAlivePeerIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAlivePeerIPAddrType.setStatus("obsolete")
_ArubaWiredMclagKeepAlivePeerIPAddr_Type = InetAddress
_ArubaWiredMclagKeepAlivePeerIPAddr_Object = MibScalar
arubaWiredMclagKeepAlivePeerIPAddr = _ArubaWiredMclagKeepAlivePeerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 2, 6),
    _ArubaWiredMclagKeepAlivePeerIPAddr_Type()
)
arubaWiredMclagKeepAlivePeerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAlivePeerIPAddr.setStatus("obsolete")


class _ArubaWiredMclagKeepAliveHelloInterval_Type(Integer32):
    """Custom type arubaWiredMclagKeepAliveHelloInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ArubaWiredMclagKeepAliveHelloInterval_Type.__name__ = "Integer32"
_ArubaWiredMclagKeepAliveHelloInterval_Object = MibScalar
arubaWiredMclagKeepAliveHelloInterval = _ArubaWiredMclagKeepAliveHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 2, 7),
    _ArubaWiredMclagKeepAliveHelloInterval_Type()
)
arubaWiredMclagKeepAliveHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAliveHelloInterval.setStatus("obsolete")


class _ArubaWiredMclagKeepAliveHelloTimeout_Type(Integer32):
    """Custom type arubaWiredMclagKeepAliveHelloTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_ArubaWiredMclagKeepAliveHelloTimeout_Type.__name__ = "Integer32"
_ArubaWiredMclagKeepAliveHelloTimeout_Object = MibScalar
arubaWiredMclagKeepAliveHelloTimeout = _ArubaWiredMclagKeepAliveHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 2, 8),
    _ArubaWiredMclagKeepAliveHelloTimeout_Type()
)
arubaWiredMclagKeepAliveHelloTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAliveHelloTimeout.setStatus("obsolete")


class _ArubaWiredMclagKeepAliveDevicePriority_Type(Integer32):
    """Custom type arubaWiredMclagKeepAliveDevicePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ArubaWiredMclagKeepAliveDevicePriority_Type.__name__ = "Integer32"
_ArubaWiredMclagKeepAliveDevicePriority_Object = MibScalar
arubaWiredMclagKeepAliveDevicePriority = _ArubaWiredMclagKeepAliveDevicePriority_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 2, 9),
    _ArubaWiredMclagKeepAliveDevicePriority_Type()
)
arubaWiredMclagKeepAliveDevicePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAliveDevicePriority.setStatus("obsolete")
_ArubaWiredMclagKeepAliveSystemID_Type = DisplayString
_ArubaWiredMclagKeepAliveSystemID_Object = MibScalar
arubaWiredMclagKeepAliveSystemID = _ArubaWiredMclagKeepAliveSystemID_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 2, 10),
    _ArubaWiredMclagKeepAliveSystemID_Type()
)
arubaWiredMclagKeepAliveSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAliveSystemID.setStatus("obsolete")
_ArubaWiredMclagKeepAlivePlatformName_Type = DisplayString
_ArubaWiredMclagKeepAlivePlatformName_Object = MibScalar
arubaWiredMclagKeepAlivePlatformName = _ArubaWiredMclagKeepAlivePlatformName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 2, 11),
    _ArubaWiredMclagKeepAlivePlatformName_Type()
)
arubaWiredMclagKeepAlivePlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAlivePlatformName.setStatus("obsolete")
_ArubaWiredMclagKeepAliveSwVersion_Type = DisplayString
_ArubaWiredMclagKeepAliveSwVersion_Object = MibScalar
arubaWiredMclagKeepAliveSwVersion = _ArubaWiredMclagKeepAliveSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 2, 12),
    _ArubaWiredMclagKeepAliveSwVersion_Type()
)
arubaWiredMclagKeepAliveSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAliveSwVersion.setStatus("obsolete")
_ArubaWiredMclagAggregatorConfig_ObjectIdentity = ObjectIdentity
arubaWiredMclagAggregatorConfig = _ArubaWiredMclagAggregatorConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 3)
)
_ArubaWiredMclagAggregatorTable_Object = MibTable
arubaWiredMclagAggregatorTable = _ArubaWiredMclagAggregatorTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    arubaWiredMclagAggregatorTable.setStatus("obsolete")
_ArubaWiredMclagAggregatorEntry_Object = MibTableRow
arubaWiredMclagAggregatorEntry = _ArubaWiredMclagAggregatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 3, 1, 1)
)
arubaWiredMclagAggregatorEntry.setIndexNames(
    (0, "ARUBAWIRED-MCLAG-MIB", "arubaWiredMclagAggregatorIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredMclagAggregatorEntry.setStatus("obsolete")
_ArubaWiredMclagAggregatorIndex_Type = InterfaceIndex
_ArubaWiredMclagAggregatorIndex_Object = MibTableColumn
arubaWiredMclagAggregatorIndex = _ArubaWiredMclagAggregatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 3, 1, 1, 1),
    _ArubaWiredMclagAggregatorIndex_Type()
)
arubaWiredMclagAggregatorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMclagAggregatorIndex.setStatus("obsolete")


class _ArubaWiredMclagAggregatorType_Type(Integer32):
    """Custom type arubaWiredMclagAggregatorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("point2Point", 1),
          ("multiChassis", 2))
    )


_ArubaWiredMclagAggregatorType_Type.__name__ = "Integer32"
_ArubaWiredMclagAggregatorType_Object = MibTableColumn
arubaWiredMclagAggregatorType = _ArubaWiredMclagAggregatorType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 3, 1, 1, 2),
    _ArubaWiredMclagAggregatorType_Type()
)
arubaWiredMclagAggregatorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredMclagAggregatorType.setStatus("obsolete")
_ArubaWiredMclagVlanList_Type = VidList
_ArubaWiredMclagVlanList_Object = MibTableColumn
arubaWiredMclagVlanList = _ArubaWiredMclagVlanList_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 3, 1, 1, 3),
    _ArubaWiredMclagVlanList_Type()
)
arubaWiredMclagVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagVlanList.setStatus("obsolete")
_ArubaWiredMclagLoopProtectEnabled_Type = TruthValue
_ArubaWiredMclagLoopProtectEnabled_Object = MibTableColumn
arubaWiredMclagLoopProtectEnabled = _ArubaWiredMclagLoopProtectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 3, 1, 1, 4),
    _ArubaWiredMclagLoopProtectEnabled_Type()
)
arubaWiredMclagLoopProtectEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagLoopProtectEnabled.setStatus("obsolete")


class _ArubaWiredMclagLoadBalanceScheme_Type(Integer32):
    """Custom type arubaWiredMclagLoadBalanceScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2-Src-Dst", 1),
          ("l3-Src-Dst", 2),
          ("l4-Src-Dst", 3))
    )


_ArubaWiredMclagLoadBalanceScheme_Type.__name__ = "Integer32"
_ArubaWiredMclagLoadBalanceScheme_Object = MibTableColumn
arubaWiredMclagLoadBalanceScheme = _ArubaWiredMclagLoadBalanceScheme_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 3, 1, 1, 5),
    _ArubaWiredMclagLoadBalanceScheme_Type()
)
arubaWiredMclagLoadBalanceScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagLoadBalanceScheme.setStatus("obsolete")


class _ArubaWiredMclagCosOverride_Type(Integer32):
    """Custom type arubaWiredMclagCosOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ArubaWiredMclagCosOverride_Type.__name__ = "Integer32"
_ArubaWiredMclagCosOverride_Object = MibTableColumn
arubaWiredMclagCosOverride = _ArubaWiredMclagCosOverride_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 3, 1, 1, 6),
    _ArubaWiredMclagCosOverride_Type()
)
arubaWiredMclagCosOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagCosOverride.setStatus("obsolete")


class _ArubaWiredMclagDscpOverride_Type(Integer32):
    """Custom type arubaWiredMclagDscpOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ArubaWiredMclagDscpOverride_Type.__name__ = "Integer32"
_ArubaWiredMclagDscpOverride_Object = MibTableColumn
arubaWiredMclagDscpOverride = _ArubaWiredMclagDscpOverride_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 3, 1, 1, 7),
    _ArubaWiredMclagDscpOverride_Type()
)
arubaWiredMclagDscpOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagDscpOverride.setStatus("obsolete")


class _ArubaWiredMclagQoSTrust_Type(Integer32):
    """Custom type arubaWiredMclagQoSTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("dscp", 2))
    )


_ArubaWiredMclagQoSTrust_Type.__name__ = "Integer32"
_ArubaWiredMclagQoSTrust_Object = MibTableColumn
arubaWiredMclagQoSTrust = _ArubaWiredMclagQoSTrust_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 1, 3, 1, 1, 8),
    _ArubaWiredMclagQoSTrust_Type()
)
arubaWiredMclagQoSTrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagQoSTrust.setStatus("obsolete")
_ArubaWiredMclagStatus_ObjectIdentity = ObjectIdentity
arubaWiredMclagStatus = _ArubaWiredMclagStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2)
)
_ArubaWiredMclagIslStatus_ObjectIdentity = ObjectIdentity
arubaWiredMclagIslStatus = _ArubaWiredMclagIslStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2, 1)
)


class _ArubaWiredMclagIslOperState_Type(Integer32):
    """Custom type arubaWiredMclagIslOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("outSync", 2),
          ("inSync", 3))
    )


_ArubaWiredMclagIslOperState_Type.__name__ = "Integer32"
_ArubaWiredMclagIslOperState_Object = MibScalar
arubaWiredMclagIslOperState = _ArubaWiredMclagIslOperState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2, 1, 1),
    _ArubaWiredMclagIslOperState_Type()
)
arubaWiredMclagIslOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagIslOperState.setStatus("obsolete")
_ArubaWiredMclagIslPduTx_Type = Integer32
_ArubaWiredMclagIslPduTx_Object = MibScalar
arubaWiredMclagIslPduTx = _ArubaWiredMclagIslPduTx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2, 1, 2),
    _ArubaWiredMclagIslPduTx_Type()
)
arubaWiredMclagIslPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagIslPduTx.setStatus("obsolete")
_ArubaWiredMclagIslPduRx_Type = Integer32
_ArubaWiredMclagIslPduRx_Object = MibScalar
arubaWiredMclagIslPduRx = _ArubaWiredMclagIslPduRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2, 1, 3),
    _ArubaWiredMclagIslPduRx_Type()
)
arubaWiredMclagIslPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagIslPduRx.setStatus("obsolete")
_ArubaWiredMclagIslHelloTx_Type = Integer32
_ArubaWiredMclagIslHelloTx_Object = MibScalar
arubaWiredMclagIslHelloTx = _ArubaWiredMclagIslHelloTx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2, 1, 4),
    _ArubaWiredMclagIslHelloTx_Type()
)
arubaWiredMclagIslHelloTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagIslHelloTx.setStatus("obsolete")
_ArubaWiredMclagIslHelloRx_Type = Integer32
_ArubaWiredMclagIslHelloRx_Object = MibScalar
arubaWiredMclagIslHelloRx = _ArubaWiredMclagIslHelloRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2, 1, 5),
    _ArubaWiredMclagIslHelloRx_Type()
)
arubaWiredMclagIslHelloRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagIslHelloRx.setStatus("obsolete")


class _ArubaWiredMclagDeviceOperRole_Type(Integer32):
    """Custom type arubaWiredMclagDeviceOperRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_ArubaWiredMclagDeviceOperRole_Type.__name__ = "Integer32"
_ArubaWiredMclagDeviceOperRole_Object = MibScalar
arubaWiredMclagDeviceOperRole = _ArubaWiredMclagDeviceOperRole_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2, 1, 6),
    _ArubaWiredMclagDeviceOperRole_Type()
)
arubaWiredMclagDeviceOperRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagDeviceOperRole.setStatus("obsolete")
_ArubaWiredMclagDeviceOperSystemID_Type = DisplayString
_ArubaWiredMclagDeviceOperSystemID_Object = MibScalar
arubaWiredMclagDeviceOperSystemID = _ArubaWiredMclagDeviceOperSystemID_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2, 1, 7),
    _ArubaWiredMclagDeviceOperSystemID_Type()
)
arubaWiredMclagDeviceOperSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagDeviceOperSystemID.setStatus("obsolete")
_ArubaWiredMclagKeepAliveStatus_ObjectIdentity = ObjectIdentity
arubaWiredMclagKeepAliveStatus = _ArubaWiredMclagKeepAliveStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2, 2)
)


class _ArubaWiredMclagKeepAliveOperState_Type(Integer32):
    """Custom type arubaWiredMclagKeepAliveOperState based on Integer32"""
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
        *(("initialized", 1),
          ("configured", 2),
          ("established", 3),
          ("failed", 4),
          ("stopped", 5))
    )


_ArubaWiredMclagKeepAliveOperState_Type.__name__ = "Integer32"
_ArubaWiredMclagKeepAliveOperState_Object = MibScalar
arubaWiredMclagKeepAliveOperState = _ArubaWiredMclagKeepAliveOperState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2, 2, 1),
    _ArubaWiredMclagKeepAliveOperState_Type()
)
arubaWiredMclagKeepAliveOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAliveOperState.setStatus("obsolete")
_ArubaWiredMclagKeepAlivePacketsTx_Type = Integer32
_ArubaWiredMclagKeepAlivePacketsTx_Object = MibScalar
arubaWiredMclagKeepAlivePacketsTx = _ArubaWiredMclagKeepAlivePacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2, 2, 2),
    _ArubaWiredMclagKeepAlivePacketsTx_Type()
)
arubaWiredMclagKeepAlivePacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAlivePacketsTx.setStatus("obsolete")
_ArubaWiredMclagKeepAlivePacketsRx_Type = Integer32
_ArubaWiredMclagKeepAlivePacketsRx_Object = MibScalar
arubaWiredMclagKeepAlivePacketsRx = _ArubaWiredMclagKeepAlivePacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2, 2, 3),
    _ArubaWiredMclagKeepAlivePacketsRx_Type()
)
arubaWiredMclagKeepAlivePacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAlivePacketsRx.setStatus("obsolete")
_ArubaWiredMclagKeepAlivePacketsDrop_Type = Integer32
_ArubaWiredMclagKeepAlivePacketsDrop_Object = MibScalar
arubaWiredMclagKeepAlivePacketsDrop = _ArubaWiredMclagKeepAlivePacketsDrop_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2, 2, 4),
    _ArubaWiredMclagKeepAlivePacketsDrop_Type()
)
arubaWiredMclagKeepAlivePacketsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAlivePacketsDrop.setStatus("obsolete")
_ArubaWiredMclagKeepAliveTimeoutCount_Type = Integer32
_ArubaWiredMclagKeepAliveTimeoutCount_Object = MibScalar
arubaWiredMclagKeepAliveTimeoutCount = _ArubaWiredMclagKeepAliveTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2, 2, 5),
    _ArubaWiredMclagKeepAliveTimeoutCount_Type()
)
arubaWiredMclagKeepAliveTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAliveTimeoutCount.setStatus("obsolete")
_ArubaWiredMclagKeepAliveLastEstablishedTime_Type = TimeTicks
_ArubaWiredMclagKeepAliveLastEstablishedTime_Object = MibScalar
arubaWiredMclagKeepAliveLastEstablishedTime = _ArubaWiredMclagKeepAliveLastEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2, 2, 6),
    _ArubaWiredMclagKeepAliveLastEstablishedTime_Type()
)
arubaWiredMclagKeepAliveLastEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAliveLastEstablishedTime.setStatus("obsolete")
_ArubaWiredMclagKeepAliveLastFailedTime_Type = TimeTicks
_ArubaWiredMclagKeepAliveLastFailedTime_Object = MibScalar
arubaWiredMclagKeepAliveLastFailedTime = _ArubaWiredMclagKeepAliveLastFailedTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2, 2, 2, 7),
    _ArubaWiredMclagKeepAliveLastFailedTime_Type()
)
arubaWiredMclagKeepAliveLastFailedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMclagKeepAliveLastFailedTime.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-MCLAG-MIB",
    **{"VidList": VidList,
       "arubaWiredMclagMIB": arubaWiredMclagMIB,
       "arubaWiredMclagConfig": arubaWiredMclagConfig,
       "arubaWiredMclagIslConfig": arubaWiredMclagIslConfig,
       "arubaWiredMclagIslPort": arubaWiredMclagIslPort,
       "arubaWiredMclagIslHelloInterval": arubaWiredMclagIslHelloInterval,
       "arubaWiredMclagIslHoldTime": arubaWiredMclagIslHoldTime,
       "arubaWiredMclagIslHelloTimeout": arubaWiredMclagIslHelloTimeout,
       "arubaWiredMclagIslDevicePriority": arubaWiredMclagIslDevicePriority,
       "arubaWiredMclagIslSystemID": arubaWiredMclagIslSystemID,
       "arubaWiredMclagIslPlatformName": arubaWiredMclagIslPlatformName,
       "arubaWiredMclagIslSwVersion": arubaWiredMclagIslSwVersion,
       "arubaWiredMclagIslVIDList": arubaWiredMclagIslVIDList,
       "arubaWiredMclagKeepAliveConfig": arubaWiredMclagKeepAliveConfig,
       "arubaWiredMclagKeepAliveSrcIPAddrType": arubaWiredMclagKeepAliveSrcIPAddrType,
       "arubaWiredMclagKeepAliveSrcIPAddr": arubaWiredMclagKeepAliveSrcIPAddr,
       "arubaWiredMclagKeepAliveVrf": arubaWiredMclagKeepAliveVrf,
       "arubaWiredMclagKeepAliveUdpPort": arubaWiredMclagKeepAliveUdpPort,
       "arubaWiredMclagKeepAlivePeerIPAddrType": arubaWiredMclagKeepAlivePeerIPAddrType,
       "arubaWiredMclagKeepAlivePeerIPAddr": arubaWiredMclagKeepAlivePeerIPAddr,
       "arubaWiredMclagKeepAliveHelloInterval": arubaWiredMclagKeepAliveHelloInterval,
       "arubaWiredMclagKeepAliveHelloTimeout": arubaWiredMclagKeepAliveHelloTimeout,
       "arubaWiredMclagKeepAliveDevicePriority": arubaWiredMclagKeepAliveDevicePriority,
       "arubaWiredMclagKeepAliveSystemID": arubaWiredMclagKeepAliveSystemID,
       "arubaWiredMclagKeepAlivePlatformName": arubaWiredMclagKeepAlivePlatformName,
       "arubaWiredMclagKeepAliveSwVersion": arubaWiredMclagKeepAliveSwVersion,
       "arubaWiredMclagAggregatorConfig": arubaWiredMclagAggregatorConfig,
       "arubaWiredMclagAggregatorTable": arubaWiredMclagAggregatorTable,
       "arubaWiredMclagAggregatorEntry": arubaWiredMclagAggregatorEntry,
       "arubaWiredMclagAggregatorIndex": arubaWiredMclagAggregatorIndex,
       "arubaWiredMclagAggregatorType": arubaWiredMclagAggregatorType,
       "arubaWiredMclagVlanList": arubaWiredMclagVlanList,
       "arubaWiredMclagLoopProtectEnabled": arubaWiredMclagLoopProtectEnabled,
       "arubaWiredMclagLoadBalanceScheme": arubaWiredMclagLoadBalanceScheme,
       "arubaWiredMclagCosOverride": arubaWiredMclagCosOverride,
       "arubaWiredMclagDscpOverride": arubaWiredMclagDscpOverride,
       "arubaWiredMclagQoSTrust": arubaWiredMclagQoSTrust,
       "arubaWiredMclagStatus": arubaWiredMclagStatus,
       "arubaWiredMclagIslStatus": arubaWiredMclagIslStatus,
       "arubaWiredMclagIslOperState": arubaWiredMclagIslOperState,
       "arubaWiredMclagIslPduTx": arubaWiredMclagIslPduTx,
       "arubaWiredMclagIslPduRx": arubaWiredMclagIslPduRx,
       "arubaWiredMclagIslHelloTx": arubaWiredMclagIslHelloTx,
       "arubaWiredMclagIslHelloRx": arubaWiredMclagIslHelloRx,
       "arubaWiredMclagDeviceOperRole": arubaWiredMclagDeviceOperRole,
       "arubaWiredMclagDeviceOperSystemID": arubaWiredMclagDeviceOperSystemID,
       "arubaWiredMclagKeepAliveStatus": arubaWiredMclagKeepAliveStatus,
       "arubaWiredMclagKeepAliveOperState": arubaWiredMclagKeepAliveOperState,
       "arubaWiredMclagKeepAlivePacketsTx": arubaWiredMclagKeepAlivePacketsTx,
       "arubaWiredMclagKeepAlivePacketsRx": arubaWiredMclagKeepAlivePacketsRx,
       "arubaWiredMclagKeepAlivePacketsDrop": arubaWiredMclagKeepAlivePacketsDrop,
       "arubaWiredMclagKeepAliveTimeoutCount": arubaWiredMclagKeepAliveTimeoutCount,
       "arubaWiredMclagKeepAliveLastEstablishedTime": arubaWiredMclagKeepAliveLastEstablishedTime,
       "arubaWiredMclagKeepAliveLastFailedTime": arubaWiredMclagKeepAliveLastFailedTime}
)
