# SNMP MIB module (TN-IPMC-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-IPMC-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:41 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnIpmcSnoopingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TnIpmcType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("igmp", 1),
          ("mld", 2),
          ("unknown", 4))
    )



class TnIpmcVersion(TextualConvention, Integer32):
    status = "current"
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
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3),
          ("unknown", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TnIpmcSnoopingMibNotifications_ObjectIdentity = ObjectIdentity
tnIpmcSnoopingMibNotifications = _TnIpmcSnoopingMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 1)
)
_TnIpmcSnoopingMibObjects_ObjectIdentity = ObjectIdentity
tnIpmcSnoopingMibObjects = _TnIpmcSnoopingMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2)
)
_TnIpmcSnoopingMgmt_ObjectIdentity = ObjectIdentity
tnIpmcSnoopingMgmt = _TnIpmcSnoopingMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1)
)
_TnSystemCfgInfo_ObjectIdentity = ObjectIdentity
tnSystemCfgInfo = _TnSystemCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 1)
)
_TnSystemCfgTable_Object = MibTable
tnSystemCfgTable = _TnSystemCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnSystemCfgTable.setStatus("current")
_TnSystemCfgEntry_Object = MibTableRow
tnSystemCfgEntry = _TnSystemCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 1, 1, 1)
)
tnSystemCfgEntry.setIndexNames(
    (0, "TN-IPMC-SNOOPING-MIB", "tnIpmcSnoopingType"),
)
if mibBuilder.loadTexts:
    tnSystemCfgEntry.setStatus("current")
_TnIpmcSnoopingType_Type = TnIpmcType
_TnIpmcSnoopingType_Object = MibTableColumn
tnIpmcSnoopingType = _TnIpmcSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 1, 1, 1, 1),
    _TnIpmcSnoopingType_Type()
)
tnIpmcSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpmcSnoopingType.setStatus("current")
_TnIpmcSnoopingEnabled_Type = TruthValue
_TnIpmcSnoopingEnabled_Object = MibTableColumn
tnIpmcSnoopingEnabled = _TnIpmcSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 1, 1, 1, 2),
    _TnIpmcSnoopingEnabled_Type()
)
tnIpmcSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpmcSnoopingEnabled.setStatus("current")
_TnIpmcSnoopingFloodingEnabled_Type = TruthValue
_TnIpmcSnoopingFloodingEnabled_Object = MibTableColumn
tnIpmcSnoopingFloodingEnabled = _TnIpmcSnoopingFloodingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 1, 1, 1, 3),
    _TnIpmcSnoopingFloodingEnabled_Type()
)
tnIpmcSnoopingFloodingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpmcSnoopingFloodingEnabled.setStatus("current")
_TnIpmcSnoopingLeaveProxyEnabled_Type = TruthValue
_TnIpmcSnoopingLeaveProxyEnabled_Object = MibTableColumn
tnIpmcSnoopingLeaveProxyEnabled = _TnIpmcSnoopingLeaveProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 1, 1, 1, 4),
    _TnIpmcSnoopingLeaveProxyEnabled_Type()
)
tnIpmcSnoopingLeaveProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpmcSnoopingLeaveProxyEnabled.setStatus("current")
_TnIpmcSnoopingProxyEnabled_Type = TruthValue
_TnIpmcSnoopingProxyEnabled_Object = MibTableColumn
tnIpmcSnoopingProxyEnabled = _TnIpmcSnoopingProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 1, 1, 1, 5),
    _TnIpmcSnoopingProxyEnabled_Type()
)
tnIpmcSnoopingProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpmcSnoopingProxyEnabled.setStatus("current")
_TnIpmcSnoopingSsmRange_Type = InetAddress
_TnIpmcSnoopingSsmRange_Object = MibTableColumn
tnIpmcSnoopingSsmRange = _TnIpmcSnoopingSsmRange_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 1, 1, 1, 6),
    _TnIpmcSnoopingSsmRange_Type()
)
tnIpmcSnoopingSsmRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpmcSnoopingSsmRange.setStatus("current")
_TnIpmcSnoopingSsmRangePrefix_Type = InetAddressPrefixLength
_TnIpmcSnoopingSsmRangePrefix_Object = MibTableColumn
tnIpmcSnoopingSsmRangePrefix = _TnIpmcSnoopingSsmRangePrefix_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 1, 1, 1, 7),
    _TnIpmcSnoopingSsmRangePrefix_Type()
)
tnIpmcSnoopingSsmRangePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpmcSnoopingSsmRangePrefix.setStatus("current")
_TnIpmcSnoopingStatisticClear_Type = TruthValue
_TnIpmcSnoopingStatisticClear_Object = MibTableColumn
tnIpmcSnoopingStatisticClear = _TnIpmcSnoopingStatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 1, 1, 1, 8),
    _TnIpmcSnoopingStatisticClear_Type()
)
tnIpmcSnoopingStatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpmcSnoopingStatisticClear.setStatus("current")
_TnPortCfgInfo_ObjectIdentity = ObjectIdentity
tnPortCfgInfo = _TnPortCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 2)
)
_TnPortCfgTable_Object = MibTable
tnPortCfgTable = _TnPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnPortCfgTable.setStatus("current")
_TnPortCfgEntry_Object = MibTableRow
tnPortCfgEntry = _TnPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 2, 1, 1)
)
tnPortCfgEntry.setIndexNames(
    (0, "TN-IPMC-SNOOPING-MIB", "tnIpmcSnoopingType"),
    (0, "TN-IPMC-SNOOPING-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPortCfgEntry.setStatus("current")
_TnPortRoutePortEnabled_Type = TruthValue
_TnPortRoutePortEnabled_Object = MibTableColumn
tnPortRoutePortEnabled = _TnPortRoutePortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 2, 1, 1, 1),
    _TnPortRoutePortEnabled_Type()
)
tnPortRoutePortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortRoutePortEnabled.setStatus("current")
_TnPortFastLeaveEnabled_Type = TruthValue
_TnPortFastLeaveEnabled_Object = MibTableColumn
tnPortFastLeaveEnabled = _TnPortFastLeaveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 2, 1, 1, 2),
    _TnPortFastLeaveEnabled_Type()
)
tnPortFastLeaveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortFastLeaveEnabled.setStatus("current")


class _TnPortThrottling_Type(Unsigned32):
    """Custom type tnPortThrottling based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TnPortThrottling_Type.__name__ = "Unsigned32"
_TnPortThrottling_Object = MibTableColumn
tnPortThrottling = _TnPortThrottling_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 2, 1, 1, 3),
    _TnPortThrottling_Type()
)
tnPortThrottling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortThrottling.setStatus("current")
_TnVlanCfgInfo_ObjectIdentity = ObjectIdentity
tnVlanCfgInfo = _TnVlanCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 3)
)
_TnVlanCfgTable_Object = MibTable
tnVlanCfgTable = _TnVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tnVlanCfgTable.setStatus("current")
_TnVlanCfgEntry_Object = MibTableRow
tnVlanCfgEntry = _TnVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 3, 1, 1)
)
tnVlanCfgEntry.setIndexNames(
    (0, "TN-IPMC-SNOOPING-MIB", "tnIpmcSnoopingType"),
    (0, "TN-IPMC-SNOOPING-MIB", "tnVlanIndex"),
)
if mibBuilder.loadTexts:
    tnVlanCfgEntry.setStatus("current")
_TnVlanIndex_Type = VlanId
_TnVlanIndex_Object = MibTableColumn
tnVlanIndex = _TnVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 3, 1, 1, 1),
    _TnVlanIndex_Type()
)
tnVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVlanIndex.setStatus("current")
_TnVlanIpmcSnoopingEnabled_Type = TruthValue
_TnVlanIpmcSnoopingEnabled_Object = MibTableColumn
tnVlanIpmcSnoopingEnabled = _TnVlanIpmcSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 3, 1, 1, 2),
    _TnVlanIpmcSnoopingEnabled_Type()
)
tnVlanIpmcSnoopingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanIpmcSnoopingEnabled.setStatus("current")
_TnVlanIpmcQuerierEnabled_Type = TruthValue
_TnVlanIpmcQuerierEnabled_Object = MibTableColumn
tnVlanIpmcQuerierEnabled = _TnVlanIpmcQuerierEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 3, 1, 1, 3),
    _TnVlanIpmcQuerierEnabled_Type()
)
tnVlanIpmcQuerierEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanIpmcQuerierEnabled.setStatus("current")


class _TnVlanIpmcCompatibility_Type(Integer32):
    """Custom type tnVlanIpmcCompatibility based on Integer32"""
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
        *(("ipmc-auto", 0),
          ("ipmc-v1", 1),
          ("ipmc-v2", 2),
          ("ipmc-v3", 3))
    )


_TnVlanIpmcCompatibility_Type.__name__ = "Integer32"
_TnVlanIpmcCompatibility_Object = MibTableColumn
tnVlanIpmcCompatibility = _TnVlanIpmcCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 3, 1, 1, 4),
    _TnVlanIpmcCompatibility_Type()
)
tnVlanIpmcCompatibility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanIpmcCompatibility.setStatus("current")


class _TnVlanIpmcSnoopingRV_Type(Unsigned32):
    """Custom type tnVlanIpmcSnoopingRV based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnVlanIpmcSnoopingRV_Type.__name__ = "Unsigned32"
_TnVlanIpmcSnoopingRV_Object = MibTableColumn
tnVlanIpmcSnoopingRV = _TnVlanIpmcSnoopingRV_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 3, 1, 1, 5),
    _TnVlanIpmcSnoopingRV_Type()
)
tnVlanIpmcSnoopingRV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanIpmcSnoopingRV.setStatus("current")


class _TnVlanIpmcSnoopingQI_Type(Unsigned32):
    """Custom type tnVlanIpmcSnoopingQI based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31744),
    )


_TnVlanIpmcSnoopingQI_Type.__name__ = "Unsigned32"
_TnVlanIpmcSnoopingQI_Object = MibTableColumn
tnVlanIpmcSnoopingQI = _TnVlanIpmcSnoopingQI_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 3, 1, 1, 6),
    _TnVlanIpmcSnoopingQI_Type()
)
tnVlanIpmcSnoopingQI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanIpmcSnoopingQI.setStatus("current")
if mibBuilder.loadTexts:
    tnVlanIpmcSnoopingQI.setUnits("seconds")


class _TnVlanIpmcSnoopingQRI_Type(Unsigned32):
    """Custom type tnVlanIpmcSnoopingQRI based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31744),
    )


_TnVlanIpmcSnoopingQRI_Type.__name__ = "Unsigned32"
_TnVlanIpmcSnoopingQRI_Object = MibTableColumn
tnVlanIpmcSnoopingQRI = _TnVlanIpmcSnoopingQRI_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 3, 1, 1, 7),
    _TnVlanIpmcSnoopingQRI_Type()
)
tnVlanIpmcSnoopingQRI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanIpmcSnoopingQRI.setStatus("current")
if mibBuilder.loadTexts:
    tnVlanIpmcSnoopingQRI.setUnits("deciseconds")


class _TnVlanIpmcSnoopingLLQI_Type(Unsigned32):
    """Custom type tnVlanIpmcSnoopingLLQI based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31744),
    )


_TnVlanIpmcSnoopingLLQI_Type.__name__ = "Unsigned32"
_TnVlanIpmcSnoopingLLQI_Object = MibTableColumn
tnVlanIpmcSnoopingLLQI = _TnVlanIpmcSnoopingLLQI_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 3, 1, 1, 8),
    _TnVlanIpmcSnoopingLLQI_Type()
)
tnVlanIpmcSnoopingLLQI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanIpmcSnoopingLLQI.setStatus("current")
if mibBuilder.loadTexts:
    tnVlanIpmcSnoopingLLQI.setUnits("deciseconds")


class _TnVlanIpmcSnoopingURI_Type(Unsigned32):
    """Custom type tnVlanIpmcSnoopingURI based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31744),
    )


_TnVlanIpmcSnoopingURI_Type.__name__ = "Unsigned32"
_TnVlanIpmcSnoopingURI_Object = MibTableColumn
tnVlanIpmcSnoopingURI = _TnVlanIpmcSnoopingURI_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 3, 1, 1, 9),
    _TnVlanIpmcSnoopingURI_Type()
)
tnVlanIpmcSnoopingURI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanIpmcSnoopingURI.setStatus("current")
if mibBuilder.loadTexts:
    tnVlanIpmcSnoopingURI.setUnits("seconds")
_TnVlanIpmcRowStatus_Type = RowStatus
_TnVlanIpmcRowStatus_Object = MibTableColumn
tnVlanIpmcRowStatus = _TnVlanIpmcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 3, 1, 1, 10),
    _TnVlanIpmcRowStatus_Type()
)
tnVlanIpmcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVlanIpmcRowStatus.setStatus("current")
_TnPortFilterCfgInfo_ObjectIdentity = ObjectIdentity
tnPortFilterCfgInfo = _TnPortFilterCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 4)
)
_TnPortFilterCfgTable_Object = MibTable
tnPortFilterCfgTable = _TnPortFilterCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tnPortFilterCfgTable.setStatus("current")
_TnPortFilterCfgEntry_Object = MibTableRow
tnPortFilterCfgEntry = _TnPortFilterCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 4, 1, 1)
)
tnPortFilterCfgEntry.setIndexNames(
    (0, "TN-IPMC-SNOOPING-MIB", "tnIpmcSnoopingType"),
    (0, "TN-IPMC-SNOOPING-MIB", "tnPortFilterIfIndex"),
    (0, "TN-IPMC-SNOOPING-MIB", "tnPortFilterIpmcIp"),
)
if mibBuilder.loadTexts:
    tnPortFilterCfgEntry.setStatus("current")
_TnPortFilterIfIndex_Type = Unsigned32
_TnPortFilterIfIndex_Object = MibTableColumn
tnPortFilterIfIndex = _TnPortFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 4, 1, 1, 1),
    _TnPortFilterIfIndex_Type()
)
tnPortFilterIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPortFilterIfIndex.setStatus("current")
_TnPortFilterIpmcIp_Type = InetAddress
_TnPortFilterIpmcIp_Object = MibTableColumn
tnPortFilterIpmcIp = _TnPortFilterIpmcIp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 4, 1, 1, 2),
    _TnPortFilterIpmcIp_Type()
)
tnPortFilterIpmcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPortFilterIpmcIp.setStatus("current")
_TnPortFilterRowStatus_Type = RowStatus
_TnPortFilterRowStatus_Object = MibTableColumn
tnPortFilterRowStatus = _TnPortFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 4, 1, 1, 3),
    _TnPortFilterRowStatus_Type()
)
tnPortFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortFilterRowStatus.setStatus("current")
_TnPortStatusInfo_ObjectIdentity = ObjectIdentity
tnPortStatusInfo = _TnPortStatusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 5)
)
_TnPortStatusTable_Object = MibTable
tnPortStatusTable = _TnPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tnPortStatusTable.setStatus("current")
_TnPortStatusEntry_Object = MibTableRow
tnPortStatusEntry = _TnPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 5, 1, 1)
)
tnPortStatusEntry.setIndexNames(
    (0, "TN-IPMC-SNOOPING-MIB", "tnIpmcSnoopingType"),
    (0, "TN-IPMC-SNOOPING-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPortStatusEntry.setStatus("current")
_TnPortStatusRouteEnabled_Type = TruthValue
_TnPortStatusRouteEnabled_Object = MibTableColumn
tnPortStatusRouteEnabled = _TnPortStatusRouteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 5, 1, 1, 1),
    _TnPortStatusRouteEnabled_Type()
)
tnPortStatusRouteEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortStatusRouteEnabled.setStatus("current")
_TnVlanStatisticInfo_ObjectIdentity = ObjectIdentity
tnVlanStatisticInfo = _TnVlanStatisticInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 6)
)
_TnVlanStatisticTable_Object = MibTable
tnVlanStatisticTable = _TnVlanStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tnVlanStatisticTable.setStatus("current")
_TnVlanStatisticEntry_Object = MibTableRow
tnVlanStatisticEntry = _TnVlanStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 6, 1, 1)
)
tnVlanStatisticEntry.setIndexNames(
    (0, "TN-IPMC-SNOOPING-MIB", "tnIpmcSnoopingType"),
    (0, "TN-IPMC-SNOOPING-MIB", "tnVlanStatisticVlanID"),
)
if mibBuilder.loadTexts:
    tnVlanStatisticEntry.setStatus("current")
_TnVlanStatisticVlanID_Type = VlanId
_TnVlanStatisticVlanID_Object = MibTableColumn
tnVlanStatisticVlanID = _TnVlanStatisticVlanID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 6, 1, 1, 1),
    _TnVlanStatisticVlanID_Type()
)
tnVlanStatisticVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVlanStatisticVlanID.setStatus("current")
_TnVlanStatisticQuerierVersion_Type = TnIpmcVersion
_TnVlanStatisticQuerierVersion_Object = MibTableColumn
tnVlanStatisticQuerierVersion = _TnVlanStatisticQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 6, 1, 1, 2),
    _TnVlanStatisticQuerierVersion_Type()
)
tnVlanStatisticQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVlanStatisticQuerierVersion.setStatus("current")
_TnVlanStatisticHostVersion_Type = TnIpmcVersion
_TnVlanStatisticHostVersion_Object = MibTableColumn
tnVlanStatisticHostVersion = _TnVlanStatisticHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 6, 1, 1, 3),
    _TnVlanStatisticHostVersion_Type()
)
tnVlanStatisticHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVlanStatisticHostVersion.setStatus("current")


class _TnVlanStatisticQuerierState_Type(Integer32):
    """Custom type tnVlanStatisticQuerierState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("active", 1),
          ("idle", 2))
    )


_TnVlanStatisticQuerierState_Type.__name__ = "Integer32"
_TnVlanStatisticQuerierState_Object = MibTableColumn
tnVlanStatisticQuerierState = _TnVlanStatisticQuerierState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 6, 1, 1, 4),
    _TnVlanStatisticQuerierState_Type()
)
tnVlanStatisticQuerierState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVlanStatisticQuerierState.setStatus("current")
_TnVlanStatisticQuerierTx_Type = Counter32
_TnVlanStatisticQuerierTx_Object = MibTableColumn
tnVlanStatisticQuerierTx = _TnVlanStatisticQuerierTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 6, 1, 1, 5),
    _TnVlanStatisticQuerierTx_Type()
)
tnVlanStatisticQuerierTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVlanStatisticQuerierTx.setStatus("current")
_TnVlanStatisticQuerierRx_Type = Counter32
_TnVlanStatisticQuerierRx_Object = MibTableColumn
tnVlanStatisticQuerierRx = _TnVlanStatisticQuerierRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 6, 1, 1, 6),
    _TnVlanStatisticQuerierRx_Type()
)
tnVlanStatisticQuerierRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVlanStatisticQuerierRx.setStatus("current")
_TnVlanStatisticV1ReportsRx_Type = Counter32
_TnVlanStatisticV1ReportsRx_Object = MibTableColumn
tnVlanStatisticV1ReportsRx = _TnVlanStatisticV1ReportsRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 6, 1, 1, 7),
    _TnVlanStatisticV1ReportsRx_Type()
)
tnVlanStatisticV1ReportsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVlanStatisticV1ReportsRx.setStatus("current")
_TnVlanStatisticV2ReportsRx_Type = Counter32
_TnVlanStatisticV2ReportsRx_Object = MibTableColumn
tnVlanStatisticV2ReportsRx = _TnVlanStatisticV2ReportsRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 6, 1, 1, 8),
    _TnVlanStatisticV2ReportsRx_Type()
)
tnVlanStatisticV2ReportsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVlanStatisticV2ReportsRx.setStatus("current")
_TnVlanStatisticV3ReportsRx_Type = Counter32
_TnVlanStatisticV3ReportsRx_Object = MibTableColumn
tnVlanStatisticV3ReportsRx = _TnVlanStatisticV3ReportsRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 6, 1, 1, 9),
    _TnVlanStatisticV3ReportsRx_Type()
)
tnVlanStatisticV3ReportsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVlanStatisticV3ReportsRx.setStatus("current")
_TnVlanStatisticLeavesRx_Type = Counter32
_TnVlanStatisticLeavesRx_Object = MibTableColumn
tnVlanStatisticLeavesRx = _TnVlanStatisticLeavesRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 6, 1, 1, 10),
    _TnVlanStatisticLeavesRx_Type()
)
tnVlanStatisticLeavesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVlanStatisticLeavesRx.setStatus("current")
_TnIpmcGroupInfo_ObjectIdentity = ObjectIdentity
tnIpmcGroupInfo = _TnIpmcGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 7)
)
_TnIpmcGroupTable_Object = MibTable
tnIpmcGroupTable = _TnIpmcGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tnIpmcGroupTable.setStatus("current")
_TnIpmcGroupEntry_Object = MibTableRow
tnIpmcGroupEntry = _TnIpmcGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 7, 1, 1)
)
tnIpmcGroupEntry.setIndexNames(
    (0, "TN-IPMC-SNOOPING-MIB", "tnIpmcSnoopingType"),
    (0, "TN-IPMC-SNOOPING-MIB", "tnIpmcGroupVlanIndex"),
    (0, "TN-IPMC-SNOOPING-MIB", "tnIpmcGroupAddress"),
)
if mibBuilder.loadTexts:
    tnIpmcGroupEntry.setStatus("current")
_TnIpmcGroupVlanIndex_Type = VlanId
_TnIpmcGroupVlanIndex_Object = MibTableColumn
tnIpmcGroupVlanIndex = _TnIpmcGroupVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 7, 1, 1, 1),
    _TnIpmcGroupVlanIndex_Type()
)
tnIpmcGroupVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpmcGroupVlanIndex.setStatus("current")
_TnIpmcGroupAddress_Type = InetAddress
_TnIpmcGroupAddress_Object = MibTableColumn
tnIpmcGroupAddress = _TnIpmcGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 7, 1, 1, 2),
    _TnIpmcGroupAddress_Type()
)
tnIpmcGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpmcGroupAddress.setStatus("current")
_TnIpmcGroupPortList_Type = PortList
_TnIpmcGroupPortList_Object = MibTableColumn
tnIpmcGroupPortList = _TnIpmcGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 7, 1, 1, 3),
    _TnIpmcGroupPortList_Type()
)
tnIpmcGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIpmcGroupPortList.setStatus("current")
_TnIpmcSfmInfo_ObjectIdentity = ObjectIdentity
tnIpmcSfmInfo = _TnIpmcSfmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 8)
)
_TnIpmcSfmTable_Object = MibTable
tnIpmcSfmTable = _TnIpmcSfmTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    tnIpmcSfmTable.setStatus("current")
_TnIpmcSfmEntry_Object = MibTableRow
tnIpmcSfmEntry = _TnIpmcSfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 8, 1, 1)
)
tnIpmcSfmEntry.setIndexNames(
    (0, "TN-IPMC-SNOOPING-MIB", "tnIpmcSnoopingType"),
    (0, "TN-IPMC-SNOOPING-MIB", "tnIpmcSfmVlanIndex"),
    (0, "TN-IPMC-SNOOPING-MIB", "tnIpmcSfmInetAddress"),
    (0, "TN-IPMC-SNOOPING-MIB", "tnIpmcSfmPort"),
    (0, "TN-IPMC-SNOOPING-MIB", "tnIpmcSfmSrcAddress"),
)
if mibBuilder.loadTexts:
    tnIpmcSfmEntry.setStatus("current")
_TnIpmcSfmVlanIndex_Type = VlanId
_TnIpmcSfmVlanIndex_Object = MibTableColumn
tnIpmcSfmVlanIndex = _TnIpmcSfmVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 8, 1, 1, 1),
    _TnIpmcSfmVlanIndex_Type()
)
tnIpmcSfmVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpmcSfmVlanIndex.setStatus("current")
_TnIpmcSfmInetAddress_Type = InetAddress
_TnIpmcSfmInetAddress_Object = MibTableColumn
tnIpmcSfmInetAddress = _TnIpmcSfmInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 8, 1, 1, 2),
    _TnIpmcSfmInetAddress_Type()
)
tnIpmcSfmInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpmcSfmInetAddress.setStatus("current")
_TnIpmcSfmPort_Type = InterfaceIndex
_TnIpmcSfmPort_Object = MibTableColumn
tnIpmcSfmPort = _TnIpmcSfmPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 8, 1, 1, 3),
    _TnIpmcSfmPort_Type()
)
tnIpmcSfmPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpmcSfmPort.setStatus("current")
_TnIpmcSfmSrcAddress_Type = InetAddress
_TnIpmcSfmSrcAddress_Object = MibTableColumn
tnIpmcSfmSrcAddress = _TnIpmcSfmSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 8, 1, 1, 4),
    _TnIpmcSfmSrcAddress_Type()
)
tnIpmcSfmSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpmcSfmSrcAddress.setStatus("current")


class _TnIpmcSfmMode_Type(Integer32):
    """Custom type tnIpmcSfmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_TnIpmcSfmMode_Type.__name__ = "Integer32"
_TnIpmcSfmMode_Object = MibTableColumn
tnIpmcSfmMode = _TnIpmcSfmMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 8, 1, 1, 5),
    _TnIpmcSfmMode_Type()
)
tnIpmcSfmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIpmcSfmMode.setStatus("current")


class _TnIpmcSfmSrcType_Type(Integer32):
    """Custom type tnIpmcSfmSrcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_TnIpmcSfmSrcType_Type.__name__ = "Integer32"
_TnIpmcSfmSrcType_Object = MibTableColumn
tnIpmcSfmSrcType = _TnIpmcSfmSrcType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 8, 1, 1, 6),
    _TnIpmcSfmSrcType_Type()
)
tnIpmcSfmSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIpmcSfmSrcType.setStatus("current")
_TnIpmcSfmHardFilter_Type = TruthValue
_TnIpmcSfmHardFilter_Object = MibTableColumn
tnIpmcSfmHardFilter = _TnIpmcSfmHardFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 2, 1, 8, 1, 1, 7),
    _TnIpmcSfmHardFilter_Type()
)
tnIpmcSfmHardFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIpmcSfmHardFilter.setStatus("current")
_TnIpmcSnoopingMibConformance_ObjectIdentity = ObjectIdentity
tnIpmcSnoopingMibConformance = _TnIpmcSnoopingMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 115, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-IPMC-SNOOPING-MIB",
    **{"TnIpmcType": TnIpmcType,
       "TnIpmcVersion": TnIpmcVersion,
       "tnIpmcSnoopingMib": tnIpmcSnoopingMib,
       "tnIpmcSnoopingMibNotifications": tnIpmcSnoopingMibNotifications,
       "tnIpmcSnoopingMibObjects": tnIpmcSnoopingMibObjects,
       "tnIpmcSnoopingMgmt": tnIpmcSnoopingMgmt,
       "tnSystemCfgInfo": tnSystemCfgInfo,
       "tnSystemCfgTable": tnSystemCfgTable,
       "tnSystemCfgEntry": tnSystemCfgEntry,
       "tnIpmcSnoopingType": tnIpmcSnoopingType,
       "tnIpmcSnoopingEnabled": tnIpmcSnoopingEnabled,
       "tnIpmcSnoopingFloodingEnabled": tnIpmcSnoopingFloodingEnabled,
       "tnIpmcSnoopingLeaveProxyEnabled": tnIpmcSnoopingLeaveProxyEnabled,
       "tnIpmcSnoopingProxyEnabled": tnIpmcSnoopingProxyEnabled,
       "tnIpmcSnoopingSsmRange": tnIpmcSnoopingSsmRange,
       "tnIpmcSnoopingSsmRangePrefix": tnIpmcSnoopingSsmRangePrefix,
       "tnIpmcSnoopingStatisticClear": tnIpmcSnoopingStatisticClear,
       "tnPortCfgInfo": tnPortCfgInfo,
       "tnPortCfgTable": tnPortCfgTable,
       "tnPortCfgEntry": tnPortCfgEntry,
       "tnPortRoutePortEnabled": tnPortRoutePortEnabled,
       "tnPortFastLeaveEnabled": tnPortFastLeaveEnabled,
       "tnPortThrottling": tnPortThrottling,
       "tnVlanCfgInfo": tnVlanCfgInfo,
       "tnVlanCfgTable": tnVlanCfgTable,
       "tnVlanCfgEntry": tnVlanCfgEntry,
       "tnVlanIndex": tnVlanIndex,
       "tnVlanIpmcSnoopingEnabled": tnVlanIpmcSnoopingEnabled,
       "tnVlanIpmcQuerierEnabled": tnVlanIpmcQuerierEnabled,
       "tnVlanIpmcCompatibility": tnVlanIpmcCompatibility,
       "tnVlanIpmcSnoopingRV": tnVlanIpmcSnoopingRV,
       "tnVlanIpmcSnoopingQI": tnVlanIpmcSnoopingQI,
       "tnVlanIpmcSnoopingQRI": tnVlanIpmcSnoopingQRI,
       "tnVlanIpmcSnoopingLLQI": tnVlanIpmcSnoopingLLQI,
       "tnVlanIpmcSnoopingURI": tnVlanIpmcSnoopingURI,
       "tnVlanIpmcRowStatus": tnVlanIpmcRowStatus,
       "tnPortFilterCfgInfo": tnPortFilterCfgInfo,
       "tnPortFilterCfgTable": tnPortFilterCfgTable,
       "tnPortFilterCfgEntry": tnPortFilterCfgEntry,
       "tnPortFilterIfIndex": tnPortFilterIfIndex,
       "tnPortFilterIpmcIp": tnPortFilterIpmcIp,
       "tnPortFilterRowStatus": tnPortFilterRowStatus,
       "tnPortStatusInfo": tnPortStatusInfo,
       "tnPortStatusTable": tnPortStatusTable,
       "tnPortStatusEntry": tnPortStatusEntry,
       "tnPortStatusRouteEnabled": tnPortStatusRouteEnabled,
       "tnVlanStatisticInfo": tnVlanStatisticInfo,
       "tnVlanStatisticTable": tnVlanStatisticTable,
       "tnVlanStatisticEntry": tnVlanStatisticEntry,
       "tnVlanStatisticVlanID": tnVlanStatisticVlanID,
       "tnVlanStatisticQuerierVersion": tnVlanStatisticQuerierVersion,
       "tnVlanStatisticHostVersion": tnVlanStatisticHostVersion,
       "tnVlanStatisticQuerierState": tnVlanStatisticQuerierState,
       "tnVlanStatisticQuerierTx": tnVlanStatisticQuerierTx,
       "tnVlanStatisticQuerierRx": tnVlanStatisticQuerierRx,
       "tnVlanStatisticV1ReportsRx": tnVlanStatisticV1ReportsRx,
       "tnVlanStatisticV2ReportsRx": tnVlanStatisticV2ReportsRx,
       "tnVlanStatisticV3ReportsRx": tnVlanStatisticV3ReportsRx,
       "tnVlanStatisticLeavesRx": tnVlanStatisticLeavesRx,
       "tnIpmcGroupInfo": tnIpmcGroupInfo,
       "tnIpmcGroupTable": tnIpmcGroupTable,
       "tnIpmcGroupEntry": tnIpmcGroupEntry,
       "tnIpmcGroupVlanIndex": tnIpmcGroupVlanIndex,
       "tnIpmcGroupAddress": tnIpmcGroupAddress,
       "tnIpmcGroupPortList": tnIpmcGroupPortList,
       "tnIpmcSfmInfo": tnIpmcSfmInfo,
       "tnIpmcSfmTable": tnIpmcSfmTable,
       "tnIpmcSfmEntry": tnIpmcSfmEntry,
       "tnIpmcSfmVlanIndex": tnIpmcSfmVlanIndex,
       "tnIpmcSfmInetAddress": tnIpmcSfmInetAddress,
       "tnIpmcSfmPort": tnIpmcSfmPort,
       "tnIpmcSfmSrcAddress": tnIpmcSfmSrcAddress,
       "tnIpmcSfmMode": tnIpmcSfmMode,
       "tnIpmcSfmSrcType": tnIpmcSfmSrcType,
       "tnIpmcSfmHardFilter": tnIpmcSfmHardFilter,
       "tnIpmcSnoopingMibConformance": tnIpmcSnoopingMibConformance}
)
