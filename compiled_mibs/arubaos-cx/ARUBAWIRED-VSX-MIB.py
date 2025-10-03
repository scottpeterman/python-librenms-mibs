# SNMP MIB module (ARUBAWIRED-VSX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-VSX-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:34 2025
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

arubaWiredVsxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    arubaWiredVsxMIB.setRevisions(
        ("2018-09-05 00:00",
         "2018-06-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VidList(TextualConvention, OctetString):
    status = "current"
    displayHint = "512x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512



# MIB Managed Objects in the order of their OIDs

_ArubaWiredVsxConfig_ObjectIdentity = ObjectIdentity
arubaWiredVsxConfig = _ArubaWiredVsxConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1)
)
_ArubaWiredVsxIslConfig_ObjectIdentity = ObjectIdentity
arubaWiredVsxIslConfig = _ArubaWiredVsxIslConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 1)
)
_ArubaWiredVsxIslPort_Type = DisplayString
_ArubaWiredVsxIslPort_Object = MibScalar
arubaWiredVsxIslPort = _ArubaWiredVsxIslPort_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 1, 1),
    _ArubaWiredVsxIslPort_Type()
)
arubaWiredVsxIslPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredVsxIslPort.setStatus("current")


class _ArubaWiredVsxIslHelloInterval_Type(Integer32):
    """Custom type arubaWiredVsxIslHelloInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ArubaWiredVsxIslHelloInterval_Type.__name__ = "Integer32"
_ArubaWiredVsxIslHelloInterval_Object = MibScalar
arubaWiredVsxIslHelloInterval = _ArubaWiredVsxIslHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 1, 2),
    _ArubaWiredVsxIslHelloInterval_Type()
)
arubaWiredVsxIslHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredVsxIslHelloInterval.setStatus("current")


class _ArubaWiredVsxIslHoldTime_Type(Integer32):
    """Custom type arubaWiredVsxIslHoldTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ArubaWiredVsxIslHoldTime_Type.__name__ = "Integer32"
_ArubaWiredVsxIslHoldTime_Object = MibScalar
arubaWiredVsxIslHoldTime = _ArubaWiredVsxIslHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 1, 3),
    _ArubaWiredVsxIslHoldTime_Type()
)
arubaWiredVsxIslHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredVsxIslHoldTime.setStatus("current")


class _ArubaWiredVsxIslHelloTimeout_Type(Integer32):
    """Custom type arubaWiredVsxIslHelloTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_ArubaWiredVsxIslHelloTimeout_Type.__name__ = "Integer32"
_ArubaWiredVsxIslHelloTimeout_Object = MibScalar
arubaWiredVsxIslHelloTimeout = _ArubaWiredVsxIslHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 1, 4),
    _ArubaWiredVsxIslHelloTimeout_Type()
)
arubaWiredVsxIslHelloTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredVsxIslHelloTimeout.setStatus("current")
_ArubaWiredVsxIslSystemID_Type = DisplayString
_ArubaWiredVsxIslSystemID_Object = MibScalar
arubaWiredVsxIslSystemID = _ArubaWiredVsxIslSystemID_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 1, 5),
    _ArubaWiredVsxIslSystemID_Type()
)
arubaWiredVsxIslSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxIslSystemID.setStatus("current")
_ArubaWiredVsxIslPlatformName_Type = DisplayString
_ArubaWiredVsxIslPlatformName_Object = MibScalar
arubaWiredVsxIslPlatformName = _ArubaWiredVsxIslPlatformName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 1, 6),
    _ArubaWiredVsxIslPlatformName_Type()
)
arubaWiredVsxIslPlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxIslPlatformName.setStatus("current")
_ArubaWiredVsxIslSwVersion_Type = DisplayString
_ArubaWiredVsxIslSwVersion_Object = MibScalar
arubaWiredVsxIslSwVersion = _ArubaWiredVsxIslSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 1, 7),
    _ArubaWiredVsxIslSwVersion_Type()
)
arubaWiredVsxIslSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxIslSwVersion.setStatus("current")
_ArubaWiredVsxIslVIDList_Type = VidList
_ArubaWiredVsxIslVIDList_Object = MibScalar
arubaWiredVsxIslVIDList = _ArubaWiredVsxIslVIDList_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 1, 8),
    _ArubaWiredVsxIslVIDList_Type()
)
arubaWiredVsxIslVIDList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxIslVIDList.setStatus("current")
_ArubaWiredVsxKeepAliveConfig_ObjectIdentity = ObjectIdentity
arubaWiredVsxKeepAliveConfig = _ArubaWiredVsxKeepAliveConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 2)
)
_ArubaWiredVsxKeepAliveSrcIPAddrType_Type = InetAddressType
_ArubaWiredVsxKeepAliveSrcIPAddrType_Object = MibScalar
arubaWiredVsxKeepAliveSrcIPAddrType = _ArubaWiredVsxKeepAliveSrcIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 2, 1),
    _ArubaWiredVsxKeepAliveSrcIPAddrType_Type()
)
arubaWiredVsxKeepAliveSrcIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAliveSrcIPAddrType.setStatus("current")
_ArubaWiredVsxKeepAliveSrcIPAddr_Type = InetAddress
_ArubaWiredVsxKeepAliveSrcIPAddr_Object = MibScalar
arubaWiredVsxKeepAliveSrcIPAddr = _ArubaWiredVsxKeepAliveSrcIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 2, 2),
    _ArubaWiredVsxKeepAliveSrcIPAddr_Type()
)
arubaWiredVsxKeepAliveSrcIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAliveSrcIPAddr.setStatus("current")
_ArubaWiredVsxKeepAliveVrf_Type = DisplayString
_ArubaWiredVsxKeepAliveVrf_Object = MibScalar
arubaWiredVsxKeepAliveVrf = _ArubaWiredVsxKeepAliveVrf_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 2, 3),
    _ArubaWiredVsxKeepAliveVrf_Type()
)
arubaWiredVsxKeepAliveVrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAliveVrf.setStatus("current")


class _ArubaWiredVsxKeepAliveUdpPort_Type(Integer32):
    """Custom type arubaWiredVsxKeepAliveUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_ArubaWiredVsxKeepAliveUdpPort_Type.__name__ = "Integer32"
_ArubaWiredVsxKeepAliveUdpPort_Object = MibScalar
arubaWiredVsxKeepAliveUdpPort = _ArubaWiredVsxKeepAliveUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 2, 4),
    _ArubaWiredVsxKeepAliveUdpPort_Type()
)
arubaWiredVsxKeepAliveUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAliveUdpPort.setStatus("current")
_ArubaWiredVsxKeepAlivePeerIPAddrType_Type = InetAddressType
_ArubaWiredVsxKeepAlivePeerIPAddrType_Object = MibScalar
arubaWiredVsxKeepAlivePeerIPAddrType = _ArubaWiredVsxKeepAlivePeerIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 2, 5),
    _ArubaWiredVsxKeepAlivePeerIPAddrType_Type()
)
arubaWiredVsxKeepAlivePeerIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAlivePeerIPAddrType.setStatus("current")
_ArubaWiredVsxKeepAlivePeerIPAddr_Type = InetAddress
_ArubaWiredVsxKeepAlivePeerIPAddr_Object = MibScalar
arubaWiredVsxKeepAlivePeerIPAddr = _ArubaWiredVsxKeepAlivePeerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 2, 6),
    _ArubaWiredVsxKeepAlivePeerIPAddr_Type()
)
arubaWiredVsxKeepAlivePeerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAlivePeerIPAddr.setStatus("current")


class _ArubaWiredVsxKeepAliveHelloInterval_Type(Integer32):
    """Custom type arubaWiredVsxKeepAliveHelloInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ArubaWiredVsxKeepAliveHelloInterval_Type.__name__ = "Integer32"
_ArubaWiredVsxKeepAliveHelloInterval_Object = MibScalar
arubaWiredVsxKeepAliveHelloInterval = _ArubaWiredVsxKeepAliveHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 2, 7),
    _ArubaWiredVsxKeepAliveHelloInterval_Type()
)
arubaWiredVsxKeepAliveHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAliveHelloInterval.setStatus("current")


class _ArubaWiredVsxKeepAliveHelloTimeout_Type(Integer32):
    """Custom type arubaWiredVsxKeepAliveHelloTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_ArubaWiredVsxKeepAliveHelloTimeout_Type.__name__ = "Integer32"
_ArubaWiredVsxKeepAliveHelloTimeout_Object = MibScalar
arubaWiredVsxKeepAliveHelloTimeout = _ArubaWiredVsxKeepAliveHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 2, 8),
    _ArubaWiredVsxKeepAliveHelloTimeout_Type()
)
arubaWiredVsxKeepAliveHelloTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAliveHelloTimeout.setStatus("current")
_ArubaWiredVsxKeepAliveSystemID_Type = DisplayString
_ArubaWiredVsxKeepAliveSystemID_Object = MibScalar
arubaWiredVsxKeepAliveSystemID = _ArubaWiredVsxKeepAliveSystemID_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 2, 9),
    _ArubaWiredVsxKeepAliveSystemID_Type()
)
arubaWiredVsxKeepAliveSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAliveSystemID.setStatus("current")
_ArubaWiredVsxKeepAlivePlatformName_Type = DisplayString
_ArubaWiredVsxKeepAlivePlatformName_Object = MibScalar
arubaWiredVsxKeepAlivePlatformName = _ArubaWiredVsxKeepAlivePlatformName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 2, 10),
    _ArubaWiredVsxKeepAlivePlatformName_Type()
)
arubaWiredVsxKeepAlivePlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAlivePlatformName.setStatus("current")
_ArubaWiredVsxKeepAliveSwVersion_Type = DisplayString
_ArubaWiredVsxKeepAliveSwVersion_Object = MibScalar
arubaWiredVsxKeepAliveSwVersion = _ArubaWiredVsxKeepAliveSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 2, 11),
    _ArubaWiredVsxKeepAliveSwVersion_Type()
)
arubaWiredVsxKeepAliveSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAliveSwVersion.setStatus("current")
_ArubaWiredVsxAggregatorConfig_ObjectIdentity = ObjectIdentity
arubaWiredVsxAggregatorConfig = _ArubaWiredVsxAggregatorConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 3)
)
_ArubaWiredVsxAggregatorTable_Object = MibTable
arubaWiredVsxAggregatorTable = _ArubaWiredVsxAggregatorTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    arubaWiredVsxAggregatorTable.setStatus("current")
_ArubaWiredVsxAggregatorEntry_Object = MibTableRow
arubaWiredVsxAggregatorEntry = _ArubaWiredVsxAggregatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 3, 1, 1)
)
arubaWiredVsxAggregatorEntry.setIndexNames(
    (0, "ARUBAWIRED-VSX-MIB", "arubaWiredVsxAggregatorIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredVsxAggregatorEntry.setStatus("current")
_ArubaWiredVsxAggregatorIndex_Type = InterfaceIndex
_ArubaWiredVsxAggregatorIndex_Object = MibTableColumn
arubaWiredVsxAggregatorIndex = _ArubaWiredVsxAggregatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 3, 1, 1, 1),
    _ArubaWiredVsxAggregatorIndex_Type()
)
arubaWiredVsxAggregatorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredVsxAggregatorIndex.setStatus("current")


class _ArubaWiredVsxAggregatorType_Type(Integer32):
    """Custom type arubaWiredVsxAggregatorType based on Integer32"""
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


_ArubaWiredVsxAggregatorType_Type.__name__ = "Integer32"
_ArubaWiredVsxAggregatorType_Object = MibTableColumn
arubaWiredVsxAggregatorType = _ArubaWiredVsxAggregatorType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 3, 1, 1, 2),
    _ArubaWiredVsxAggregatorType_Type()
)
arubaWiredVsxAggregatorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredVsxAggregatorType.setStatus("current")
_ArubaWiredVsxVlanList_Type = VidList
_ArubaWiredVsxVlanList_Object = MibTableColumn
arubaWiredVsxVlanList = _ArubaWiredVsxVlanList_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 3, 1, 1, 3),
    _ArubaWiredVsxVlanList_Type()
)
arubaWiredVsxVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxVlanList.setStatus("current")
_ArubaWiredVsxLoopProtectEnabled_Type = TruthValue
_ArubaWiredVsxLoopProtectEnabled_Object = MibTableColumn
arubaWiredVsxLoopProtectEnabled = _ArubaWiredVsxLoopProtectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 3, 1, 1, 4),
    _ArubaWiredVsxLoopProtectEnabled_Type()
)
arubaWiredVsxLoopProtectEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxLoopProtectEnabled.setStatus("current")


class _ArubaWiredVsxLoadBalanceScheme_Type(Integer32):
    """Custom type arubaWiredVsxLoadBalanceScheme based on Integer32"""
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


_ArubaWiredVsxLoadBalanceScheme_Type.__name__ = "Integer32"
_ArubaWiredVsxLoadBalanceScheme_Object = MibTableColumn
arubaWiredVsxLoadBalanceScheme = _ArubaWiredVsxLoadBalanceScheme_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 3, 1, 1, 5),
    _ArubaWiredVsxLoadBalanceScheme_Type()
)
arubaWiredVsxLoadBalanceScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxLoadBalanceScheme.setStatus("current")


class _ArubaWiredVsxCosOverride_Type(Integer32):
    """Custom type arubaWiredVsxCosOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ArubaWiredVsxCosOverride_Type.__name__ = "Integer32"
_ArubaWiredVsxCosOverride_Object = MibTableColumn
arubaWiredVsxCosOverride = _ArubaWiredVsxCosOverride_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 3, 1, 1, 6),
    _ArubaWiredVsxCosOverride_Type()
)
arubaWiredVsxCosOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxCosOverride.setStatus("current")


class _ArubaWiredVsxDscpOverride_Type(Integer32):
    """Custom type arubaWiredVsxDscpOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ArubaWiredVsxDscpOverride_Type.__name__ = "Integer32"
_ArubaWiredVsxDscpOverride_Object = MibTableColumn
arubaWiredVsxDscpOverride = _ArubaWiredVsxDscpOverride_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 3, 1, 1, 7),
    _ArubaWiredVsxDscpOverride_Type()
)
arubaWiredVsxDscpOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxDscpOverride.setStatus("current")


class _ArubaWiredVsxQoSTrust_Type(Integer32):
    """Custom type arubaWiredVsxQoSTrust based on Integer32"""
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


_ArubaWiredVsxQoSTrust_Type.__name__ = "Integer32"
_ArubaWiredVsxQoSTrust_Object = MibTableColumn
arubaWiredVsxQoSTrust = _ArubaWiredVsxQoSTrust_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 3, 1, 1, 8),
    _ArubaWiredVsxQoSTrust_Type()
)
arubaWiredVsxQoSTrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxQoSTrust.setStatus("current")
_ArubaWiredVsxGlobalConfiguration_ObjectIdentity = ObjectIdentity
arubaWiredVsxGlobalConfiguration = _ArubaWiredVsxGlobalConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 4)
)


class _ArubaWiredVsxDeviceRole_Type(Integer32):
    """Custom type arubaWiredVsxDeviceRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("notConfigured", 3))
    )


_ArubaWiredVsxDeviceRole_Type.__name__ = "Integer32"
_ArubaWiredVsxDeviceRole_Object = MibScalar
arubaWiredVsxDeviceRole = _ArubaWiredVsxDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 4, 1),
    _ArubaWiredVsxDeviceRole_Type()
)
arubaWiredVsxDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxDeviceRole.setStatus("current")


class _ArubaWiredVsxConfigSync_Type(Integer32):
    """Custom type arubaWiredVsxConfigSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ArubaWiredVsxConfigSync_Type.__name__ = "Integer32"
_ArubaWiredVsxConfigSync_Object = MibScalar
arubaWiredVsxConfigSync = _ArubaWiredVsxConfigSync_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 1, 4, 2),
    _ArubaWiredVsxConfigSync_Type()
)
arubaWiredVsxConfigSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxConfigSync.setStatus("current")
_ArubaWiredVsxStatus_ObjectIdentity = ObjectIdentity
arubaWiredVsxStatus = _ArubaWiredVsxStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 2)
)
_ArubaWiredVsxIslStatus_ObjectIdentity = ObjectIdentity
arubaWiredVsxIslStatus = _ArubaWiredVsxIslStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 2, 1)
)


class _ArubaWiredVsxIslOperState_Type(Integer32):
    """Custom type arubaWiredVsxIslOperState based on Integer32"""
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


_ArubaWiredVsxIslOperState_Type.__name__ = "Integer32"
_ArubaWiredVsxIslOperState_Object = MibScalar
arubaWiredVsxIslOperState = _ArubaWiredVsxIslOperState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 2, 1, 1),
    _ArubaWiredVsxIslOperState_Type()
)
arubaWiredVsxIslOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxIslOperState.setStatus("current")
_ArubaWiredVsxIslPduTx_Type = Integer32
_ArubaWiredVsxIslPduTx_Object = MibScalar
arubaWiredVsxIslPduTx = _ArubaWiredVsxIslPduTx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 2, 1, 2),
    _ArubaWiredVsxIslPduTx_Type()
)
arubaWiredVsxIslPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxIslPduTx.setStatus("current")
_ArubaWiredVsxIslPduRx_Type = Integer32
_ArubaWiredVsxIslPduRx_Object = MibScalar
arubaWiredVsxIslPduRx = _ArubaWiredVsxIslPduRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 2, 1, 3),
    _ArubaWiredVsxIslPduRx_Type()
)
arubaWiredVsxIslPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxIslPduRx.setStatus("current")
_ArubaWiredVsxIslHelloTx_Type = Integer32
_ArubaWiredVsxIslHelloTx_Object = MibScalar
arubaWiredVsxIslHelloTx = _ArubaWiredVsxIslHelloTx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 2, 1, 4),
    _ArubaWiredVsxIslHelloTx_Type()
)
arubaWiredVsxIslHelloTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxIslHelloTx.setStatus("current")
_ArubaWiredVsxIslHelloRx_Type = Integer32
_ArubaWiredVsxIslHelloRx_Object = MibScalar
arubaWiredVsxIslHelloRx = _ArubaWiredVsxIslHelloRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 2, 1, 5),
    _ArubaWiredVsxIslHelloRx_Type()
)
arubaWiredVsxIslHelloRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxIslHelloRx.setStatus("current")
_ArubaWiredVsxDeviceOperSystemID_Type = DisplayString
_ArubaWiredVsxDeviceOperSystemID_Object = MibScalar
arubaWiredVsxDeviceOperSystemID = _ArubaWiredVsxDeviceOperSystemID_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 2, 1, 6),
    _ArubaWiredVsxDeviceOperSystemID_Type()
)
arubaWiredVsxDeviceOperSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxDeviceOperSystemID.setStatus("current")
_ArubaWiredVsxKeepAliveStatus_ObjectIdentity = ObjectIdentity
arubaWiredVsxKeepAliveStatus = _ArubaWiredVsxKeepAliveStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 2, 2)
)


class _ArubaWiredVsxKeepAliveOperState_Type(Integer32):
    """Custom type arubaWiredVsxKeepAliveOperState based on Integer32"""
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
        *(("init", 1),
          ("configured", 2),
          ("inSyncEstablished", 3),
          ("outofSyncEstablished", 4),
          ("initEstablished", 5),
          ("failed", 6),
          ("stopped", 7))
    )


_ArubaWiredVsxKeepAliveOperState_Type.__name__ = "Integer32"
_ArubaWiredVsxKeepAliveOperState_Object = MibScalar
arubaWiredVsxKeepAliveOperState = _ArubaWiredVsxKeepAliveOperState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 2, 2, 1),
    _ArubaWiredVsxKeepAliveOperState_Type()
)
arubaWiredVsxKeepAliveOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAliveOperState.setStatus("current")
_ArubaWiredVsxKeepAlivePacketsTx_Type = Integer32
_ArubaWiredVsxKeepAlivePacketsTx_Object = MibScalar
arubaWiredVsxKeepAlivePacketsTx = _ArubaWiredVsxKeepAlivePacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 2, 2, 2),
    _ArubaWiredVsxKeepAlivePacketsTx_Type()
)
arubaWiredVsxKeepAlivePacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAlivePacketsTx.setStatus("current")
_ArubaWiredVsxKeepAlivePacketsRx_Type = Integer32
_ArubaWiredVsxKeepAlivePacketsRx_Object = MibScalar
arubaWiredVsxKeepAlivePacketsRx = _ArubaWiredVsxKeepAlivePacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 2, 2, 3),
    _ArubaWiredVsxKeepAlivePacketsRx_Type()
)
arubaWiredVsxKeepAlivePacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAlivePacketsRx.setStatus("current")
_ArubaWiredVsxKeepAlivePacketsDrop_Type = Integer32
_ArubaWiredVsxKeepAlivePacketsDrop_Object = MibScalar
arubaWiredVsxKeepAlivePacketsDrop = _ArubaWiredVsxKeepAlivePacketsDrop_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 2, 2, 4),
    _ArubaWiredVsxKeepAlivePacketsDrop_Type()
)
arubaWiredVsxKeepAlivePacketsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAlivePacketsDrop.setStatus("current")
_ArubaWiredVsxKeepAliveTimeoutCount_Type = Integer32
_ArubaWiredVsxKeepAliveTimeoutCount_Object = MibScalar
arubaWiredVsxKeepAliveTimeoutCount = _ArubaWiredVsxKeepAliveTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 2, 2, 5),
    _ArubaWiredVsxKeepAliveTimeoutCount_Type()
)
arubaWiredVsxKeepAliveTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAliveTimeoutCount.setStatus("current")
_ArubaWiredVsxKeepAliveLastEstablishedTime_Type = TimeTicks
_ArubaWiredVsxKeepAliveLastEstablishedTime_Object = MibScalar
arubaWiredVsxKeepAliveLastEstablishedTime = _ArubaWiredVsxKeepAliveLastEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 2, 2, 6),
    _ArubaWiredVsxKeepAliveLastEstablishedTime_Type()
)
arubaWiredVsxKeepAliveLastEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAliveLastEstablishedTime.setStatus("current")
_ArubaWiredVsxKeepAliveLastFailedTime_Type = TimeTicks
_ArubaWiredVsxKeepAliveLastFailedTime_Object = MibScalar
arubaWiredVsxKeepAliveLastFailedTime = _ArubaWiredVsxKeepAliveLastFailedTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 2, 2, 7),
    _ArubaWiredVsxKeepAliveLastFailedTime_Type()
)
arubaWiredVsxKeepAliveLastFailedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsxKeepAliveLastFailedTime.setStatus("current")
_ArubaWiredVsxNotifications_ObjectIdentity = ObjectIdentity
arubaWiredVsxNotifications = _ArubaWiredVsxNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 3)
)
_ArubaWiredVsxTraps_ObjectIdentity = ObjectIdentity
arubaWiredVsxTraps = _ArubaWiredVsxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 3, 1)
)

# Managed Objects groups


# Notification objects

islUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 3, 1, 1)
)
if mibBuilder.loadTexts:
    islUp.setStatus(
        "current"
    )

islDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 3, 1, 2)
)
if mibBuilder.loadTexts:
    islDown.setStatus(
        "current"
    )

keepAliveUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 3, 1, 3)
)
if mibBuilder.loadTexts:
    keepAliveUp.setStatus(
        "current"
    )

keepAliveDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 3, 1, 4)
)
if mibBuilder.loadTexts:
    keepAliveDown.setStatus(
        "current"
    )

mclagLocalUpPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 3, 1, 5)
)
mclagLocalUpPeerUp.setObjects(
    ("ARUBAWIRED-VSX-MIB", "arubaWiredVsxAggregatorIndex")
)
if mibBuilder.loadTexts:
    mclagLocalUpPeerUp.setStatus(
        "current"
    )

mclagLocalUpPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 3, 1, 6)
)
mclagLocalUpPeerDown.setObjects(
    ("ARUBAWIRED-VSX-MIB", "arubaWiredVsxAggregatorIndex")
)
if mibBuilder.loadTexts:
    mclagLocalUpPeerDown.setStatus(
        "current"
    )

mclagLocalDownPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 3, 1, 7)
)
mclagLocalDownPeerUp.setObjects(
    ("ARUBAWIRED-VSX-MIB", "arubaWiredVsxAggregatorIndex")
)
if mibBuilder.loadTexts:
    mclagLocalDownPeerUp.setStatus(
        "current"
    )

mclagLocalDownPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7, 3, 1, 8)
)
mclagLocalDownPeerDown.setObjects(
    ("ARUBAWIRED-VSX-MIB", "arubaWiredVsxAggregatorIndex")
)
if mibBuilder.loadTexts:
    mclagLocalDownPeerDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-VSX-MIB",
    **{"VidList": VidList,
       "arubaWiredVsxMIB": arubaWiredVsxMIB,
       "arubaWiredVsxConfig": arubaWiredVsxConfig,
       "arubaWiredVsxIslConfig": arubaWiredVsxIslConfig,
       "arubaWiredVsxIslPort": arubaWiredVsxIslPort,
       "arubaWiredVsxIslHelloInterval": arubaWiredVsxIslHelloInterval,
       "arubaWiredVsxIslHoldTime": arubaWiredVsxIslHoldTime,
       "arubaWiredVsxIslHelloTimeout": arubaWiredVsxIslHelloTimeout,
       "arubaWiredVsxIslSystemID": arubaWiredVsxIslSystemID,
       "arubaWiredVsxIslPlatformName": arubaWiredVsxIslPlatformName,
       "arubaWiredVsxIslSwVersion": arubaWiredVsxIslSwVersion,
       "arubaWiredVsxIslVIDList": arubaWiredVsxIslVIDList,
       "arubaWiredVsxKeepAliveConfig": arubaWiredVsxKeepAliveConfig,
       "arubaWiredVsxKeepAliveSrcIPAddrType": arubaWiredVsxKeepAliveSrcIPAddrType,
       "arubaWiredVsxKeepAliveSrcIPAddr": arubaWiredVsxKeepAliveSrcIPAddr,
       "arubaWiredVsxKeepAliveVrf": arubaWiredVsxKeepAliveVrf,
       "arubaWiredVsxKeepAliveUdpPort": arubaWiredVsxKeepAliveUdpPort,
       "arubaWiredVsxKeepAlivePeerIPAddrType": arubaWiredVsxKeepAlivePeerIPAddrType,
       "arubaWiredVsxKeepAlivePeerIPAddr": arubaWiredVsxKeepAlivePeerIPAddr,
       "arubaWiredVsxKeepAliveHelloInterval": arubaWiredVsxKeepAliveHelloInterval,
       "arubaWiredVsxKeepAliveHelloTimeout": arubaWiredVsxKeepAliveHelloTimeout,
       "arubaWiredVsxKeepAliveSystemID": arubaWiredVsxKeepAliveSystemID,
       "arubaWiredVsxKeepAlivePlatformName": arubaWiredVsxKeepAlivePlatformName,
       "arubaWiredVsxKeepAliveSwVersion": arubaWiredVsxKeepAliveSwVersion,
       "arubaWiredVsxAggregatorConfig": arubaWiredVsxAggregatorConfig,
       "arubaWiredVsxAggregatorTable": arubaWiredVsxAggregatorTable,
       "arubaWiredVsxAggregatorEntry": arubaWiredVsxAggregatorEntry,
       "arubaWiredVsxAggregatorIndex": arubaWiredVsxAggregatorIndex,
       "arubaWiredVsxAggregatorType": arubaWiredVsxAggregatorType,
       "arubaWiredVsxVlanList": arubaWiredVsxVlanList,
       "arubaWiredVsxLoopProtectEnabled": arubaWiredVsxLoopProtectEnabled,
       "arubaWiredVsxLoadBalanceScheme": arubaWiredVsxLoadBalanceScheme,
       "arubaWiredVsxCosOverride": arubaWiredVsxCosOverride,
       "arubaWiredVsxDscpOverride": arubaWiredVsxDscpOverride,
       "arubaWiredVsxQoSTrust": arubaWiredVsxQoSTrust,
       "arubaWiredVsxGlobalConfiguration": arubaWiredVsxGlobalConfiguration,
       "arubaWiredVsxDeviceRole": arubaWiredVsxDeviceRole,
       "arubaWiredVsxConfigSync": arubaWiredVsxConfigSync,
       "arubaWiredVsxStatus": arubaWiredVsxStatus,
       "arubaWiredVsxIslStatus": arubaWiredVsxIslStatus,
       "arubaWiredVsxIslOperState": arubaWiredVsxIslOperState,
       "arubaWiredVsxIslPduTx": arubaWiredVsxIslPduTx,
       "arubaWiredVsxIslPduRx": arubaWiredVsxIslPduRx,
       "arubaWiredVsxIslHelloTx": arubaWiredVsxIslHelloTx,
       "arubaWiredVsxIslHelloRx": arubaWiredVsxIslHelloRx,
       "arubaWiredVsxDeviceOperSystemID": arubaWiredVsxDeviceOperSystemID,
       "arubaWiredVsxKeepAliveStatus": arubaWiredVsxKeepAliveStatus,
       "arubaWiredVsxKeepAliveOperState": arubaWiredVsxKeepAliveOperState,
       "arubaWiredVsxKeepAlivePacketsTx": arubaWiredVsxKeepAlivePacketsTx,
       "arubaWiredVsxKeepAlivePacketsRx": arubaWiredVsxKeepAlivePacketsRx,
       "arubaWiredVsxKeepAlivePacketsDrop": arubaWiredVsxKeepAlivePacketsDrop,
       "arubaWiredVsxKeepAliveTimeoutCount": arubaWiredVsxKeepAliveTimeoutCount,
       "arubaWiredVsxKeepAliveLastEstablishedTime": arubaWiredVsxKeepAliveLastEstablishedTime,
       "arubaWiredVsxKeepAliveLastFailedTime": arubaWiredVsxKeepAliveLastFailedTime,
       "arubaWiredVsxNotifications": arubaWiredVsxNotifications,
       "arubaWiredVsxTraps": arubaWiredVsxTraps,
       "islUp": islUp,
       "islDown": islDown,
       "keepAliveUp": keepAliveUp,
       "keepAliveDown": keepAliveDown,
       "mclagLocalUpPeerUp": mclagLocalUpPeerUp,
       "mclagLocalUpPeerDown": mclagLocalUpPeerDown,
       "mclagLocalDownPeerUp": mclagLocalDownPeerUp,
       "mclagLocalDownPeerDown": mclagLocalDownPeerDown}
)
