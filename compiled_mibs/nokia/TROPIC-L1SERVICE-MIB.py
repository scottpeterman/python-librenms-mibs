# SNMP MIB module (TROPIC-L1SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TROPIC-L1SERVICE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:12:02 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(ipCidrRouteEntry,) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "ipCidrRouteEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(tnL1ServiceMIB,
 tnServiceModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnL1ServiceMIB",
    "tnServiceModules")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(AluWdmEnabledDisabled,
 AluWdmTypeOfNetIfOperation,
 TnApsGroupId,
 TnPerHopBehaviourType,
 TropicChannelIndexType,
 TropicPortIndexType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmEnabledDisabled",
    "AluWdmTypeOfNetIfOperation",
    "TnApsGroupId",
    "TnPerHopBehaviourType",
    "TropicChannelIndexType",
    "TropicPortIndexType")


# MODULE-IDENTITY

tnL1ServiceMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tnL1ServiceMibModule.setRevisions(
        ("2022-07-15 12:00",
         "2022-03-25 12:00",
         "2022-03-18 12:00",
         "2021-09-03 12:00",
         "2021-07-30 12:00",
         "2021-07-23 12:00",
         "2021-06-25 12:00",
         "2021-04-30 12:00",
         "2021-01-22 12:00",
         "2020-12-11 12:00",
         "2020-10-09 12:00",
         "2020-08-14 12:00",
         "2020-07-10 12:00",
         "2020-02-21 12:00",
         "2020-01-10 12:00",
         "2019-10-18 12:00",
         "2019-07-05 12:00",
         "2019-06-14 12:00",
         "2019-05-03 12:00",
         "2019-04-26 12:00",
         "2019-03-22 12:00",
         "2019-03-01 12:00",
         "2018-06-19 12:00",
         "2018-06-08 12:00",
         "2018-03-30 12:00",
         "2018-02-23 12:00",
         "2018-02-09 12:00",
         "2018-01-19 12:00",
         "2017-07-28 12:00",
         "2017-07-07 12:00",
         "2017-04-21 12:00",
         "2017-04-13 12:00",
         "2017-03-24 12:00",
         "2017-03-03 12:00",
         "2017-02-10 12:00",
         "2016-11-22 12:00",
         "2016-11-16 12:00",
         "2016-10-21 12:00",
         "2016-09-30 12:00",
         "2016-09-27 12:00",
         "2016-05-21 12:00",
         "2016-01-25 12:00",
         "2015-12-17 12:00",
         "2015-07-21 12:00",
         "2015-04-03 12:00",
         "2015-01-08 12:00",
         "2014-09-12 12:00",
         "2014-02-26 12:00",
         "2013-12-05 12:00",
         "2013-09-04 12:00",
         "2013-08-14 12:00",
         "2012-11-12 12:00",
         "2011-05-23 12:00",
         "2011-04-25 12:00",
         "2011-02-09 12:00",
         "2010-12-14 12:00",
         "2010-10-18 12:00",
         "2010-06-10 12:00",
         "2010-02-09 12:00",
         "2010-01-29 12:00",
         "2009-08-28 12:00",
         "2009-08-24 12:00",
         "2009-08-21 12:00",
         "2009-07-28 12:00",
         "2009-06-04 12:00",
         "2009-03-03 12:00",
         "2009-02-27 12:00",
         "2009-02-26 12:00",
         "2009-02-25 12:00",
         "2008-10-16 12:00",
         "2008-09-09 12:00",
         "2008-09-04 12:00",
         "2008-08-22 12:00",
         "2008-07-25 12:00",
         "2008-05-29 12:00",
         "2008-03-06 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ApsK1K2(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2



class TropicProtectionLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unprotected", 1),
          ("oneForOne", 2),
          ("onePlusOne", 3),
          ("onePlusOneOpticalSplitter", 4),
          ("onePlusOneESNCP", 5),
          ("onePlusOneOpticalSplitterG8731", 6))
    )



class TropicLinkAdminStateType(TextualConvention, Integer32):
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
        *(("enabled", 1),
          ("disabled", 2),
          ("testing", 3),
          ("locked", 4))
    )



class TropicLinkOperationalStateType(TextualConvention, Integer32):
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4))
    )



class TropicOspfAdjacencyStateType(TextualConvention, Integer32):
    status = "current"
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
        *(("down", 1),
          ("init", 2),
          ("twoWay", 3),
          ("exchangeStart", 4),
          ("exchange", 5),
          ("loading", 6),
          ("full", 7))
    )



class AluPortYcableMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("legacy", 1),
          ("standard", 2))
    )



class NokiaCNLinkOspfRoutingState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("redistribute", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TnL1ServiceConf_ObjectIdentity = ObjectIdentity
tnL1ServiceConf = _TnL1ServiceConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1)
)
_TnL1ServiceGroups_ObjectIdentity = ObjectIdentity
tnL1ServiceGroups = _TnL1ServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1)
)
_TnL1ServiceCompliances_ObjectIdentity = ObjectIdentity
tnL1ServiceCompliances = _TnL1ServiceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 2)
)
_TnL1ServiceObjs_ObjectIdentity = ObjectIdentity
tnL1ServiceObjs = _TnL1ServiceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2)
)
_TnControlNetworkLink_ObjectIdentity = ObjectIdentity
tnControlNetworkLink = _TnControlNetworkLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1)
)
_TnControlNetworkLinkTable_Object = MibTable
tnControlNetworkLinkTable = _TnControlNetworkLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnControlNetworkLinkTable.setStatus("current")
_TnControlNetworkLinkEntry_Object = MibTableRow
tnControlNetworkLinkEntry = _TnControlNetworkLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1)
)
tnControlNetworkLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnControlNetworkLinkEntry.setStatus("current")


class _TnCNLinkDescr_Type(SnmpAdminString):
    """Custom type tnCNLinkDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnCNLinkDescr_Type.__name__ = "SnmpAdminString"
_TnCNLinkDescr_Object = MibTableColumn
tnCNLinkDescr = _TnCNLinkDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 1),
    _TnCNLinkDescr_Type()
)
tnCNLinkDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDescr.setStatus("current")


class _TnCNLinkAdminStatus_Type(TropicLinkAdminStateType):
    """Custom type tnCNLinkAdminStatus based on TropicLinkAdminStateType"""
    defaultValue = 1


_TnCNLinkAdminStatus_Type.__name__ = "TropicLinkAdminStateType"
_TnCNLinkAdminStatus_Object = MibTableColumn
tnCNLinkAdminStatus = _TnCNLinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 2),
    _TnCNLinkAdminStatus_Type()
)
tnCNLinkAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkAdminStatus.setStatus("current")
_TnCNLinkOperStatus_Type = TropicLinkOperationalStateType
_TnCNLinkOperStatus_Object = MibTableColumn
tnCNLinkOperStatus = _TnCNLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 3),
    _TnCNLinkOperStatus_Type()
)
tnCNLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkOperStatus.setStatus("current")
_TnCNLinkPhysicalIfIndex_Type = InterfaceIndex
_TnCNLinkPhysicalIfIndex_Object = MibTableColumn
tnCNLinkPhysicalIfIndex = _TnCNLinkPhysicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 5),
    _TnCNLinkPhysicalIfIndex_Type()
)
tnCNLinkPhysicalIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkPhysicalIfIndex.setStatus("current")
_TnCNLinkIpAddress_Type = IpAddress
_TnCNLinkIpAddress_Object = MibTableColumn
tnCNLinkIpAddress = _TnCNLinkIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 7),
    _TnCNLinkIpAddress_Type()
)
tnCNLinkIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkIpAddress.setStatus("current")
_TnCNLinkSubnetMask_Type = IpAddress
_TnCNLinkSubnetMask_Object = MibTableColumn
tnCNLinkSubnetMask = _TnCNLinkSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 8),
    _TnCNLinkSubnetMask_Type()
)
tnCNLinkSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkSubnetMask.setStatus("current")


class _TnCNLinkHelloInterval_Type(Unsigned32):
    """Custom type tnCNLinkHelloInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnCNLinkHelloInterval_Type.__name__ = "Unsigned32"
_TnCNLinkHelloInterval_Object = MibTableColumn
tnCNLinkHelloInterval = _TnCNLinkHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 14),
    _TnCNLinkHelloInterval_Type()
)
tnCNLinkHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnCNLinkHelloInterval.setUnits("seconds")


class _TnCNLinkRtrDeadInterval_Type(Unsigned32):
    """Custom type tnCNLinkRtrDeadInterval based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnCNLinkRtrDeadInterval_Type.__name__ = "Unsigned32"
_TnCNLinkRtrDeadInterval_Object = MibTableColumn
tnCNLinkRtrDeadInterval = _TnCNLinkRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 15),
    _TnCNLinkRtrDeadInterval_Type()
)
tnCNLinkRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnCNLinkRtrDeadInterval.setUnits("seconds")
_TnCNLinkTeMetric_Type = Unsigned32
_TnCNLinkTeMetric_Object = MibTableColumn
tnCNLinkTeMetric = _TnCNLinkTeMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 22),
    _TnCNLinkTeMetric_Type()
)
tnCNLinkTeMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkTeMetric.setStatus("current")


class _TnCNLinkOspfRoutingState_Type(NokiaCNLinkOspfRoutingState):
    """Custom type tnCNLinkOspfRoutingState based on NokiaCNLinkOspfRoutingState"""
    defaultValue = 1


_TnCNLinkOspfRoutingState_Type.__name__ = "NokiaCNLinkOspfRoutingState"
_TnCNLinkOspfRoutingState_Object = MibTableColumn
tnCNLinkOspfRoutingState = _TnCNLinkOspfRoutingState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 31),
    _TnCNLinkOspfRoutingState_Type()
)
tnCNLinkOspfRoutingState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfRoutingState.setStatus("current")


class _TnCNLinkConfigIfType_Type(Integer32):
    """Custom type tnCNLinkConfigIfType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("broadcast", 2),
          ("nonBroadcastMultipleAccess", 3),
          ("pointToPoint", 4),
          ("virtual", 5),
          ("pointToMultipoint", 6))
    )


_TnCNLinkConfigIfType_Type.__name__ = "Integer32"
_TnCNLinkConfigIfType_Object = MibTableColumn
tnCNLinkConfigIfType = _TnCNLinkConfigIfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 32),
    _TnCNLinkConfigIfType_Type()
)
tnCNLinkConfigIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkConfigIfType.setStatus("current")


class _TnCNLinkConfigRtrPriority_Type(Unsigned32):
    """Custom type tnCNLinkConfigRtrPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnCNLinkConfigRtrPriority_Type.__name__ = "Unsigned32"
_TnCNLinkConfigRtrPriority_Object = MibTableColumn
tnCNLinkConfigRtrPriority = _TnCNLinkConfigRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 33),
    _TnCNLinkConfigRtrPriority_Type()
)
tnCNLinkConfigRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkConfigRtrPriority.setStatus("current")


class _TnCNLinkEquipOperStatus_Type(TropicLinkOperationalStateType):
    """Custom type tnCNLinkEquipOperStatus based on TropicLinkOperationalStateType"""
    defaultValue = 2


_TnCNLinkEquipOperStatus_Type.__name__ = "TropicLinkOperationalStateType"
_TnCNLinkEquipOperStatus_Object = MibTableColumn
tnCNLinkEquipOperStatus = _TnCNLinkEquipOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 34),
    _TnCNLinkEquipOperStatus_Type()
)
tnCNLinkEquipOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkEquipOperStatus.setStatus("current")
_TnCNLinkDhcpEnabled_Type = TruthValue
_TnCNLinkDhcpEnabled_Object = MibTableColumn
tnCNLinkDhcpEnabled = _TnCNLinkDhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 35),
    _TnCNLinkDhcpEnabled_Type()
)
tnCNLinkDhcpEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDhcpEnabled.setStatus("current")


class _TnCNLinkSpeed_Type(Integer32):
    """Custom type tnCNLinkSpeed based on Integer32"""
    defaultValue = 1

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
        *(("auto", 1),
          ("rate10Mbps", 2),
          ("rate100Mbps", 3),
          ("rate1000Mbps", 4))
    )


_TnCNLinkSpeed_Type.__name__ = "Integer32"
_TnCNLinkSpeed_Object = MibTableColumn
tnCNLinkSpeed = _TnCNLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 36),
    _TnCNLinkSpeed_Type()
)
tnCNLinkSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkSpeed.setStatus("current")


class _TnCNLinkDuplex_Type(Integer32):
    """Custom type tnCNLinkDuplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("half", 2),
          ("full", 3))
    )


_TnCNLinkDuplex_Type.__name__ = "Integer32"
_TnCNLinkDuplex_Object = MibTableColumn
tnCNLinkDuplex = _TnCNLinkDuplex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 37),
    _TnCNLinkDuplex_Type()
)
tnCNLinkDuplex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDuplex.setStatus("current")


class _TnCNLinkProxyArp_Type(TruthValue):
    """Custom type tnCNLinkProxyArp based on TruthValue"""
    defaultValue = 2


_TnCNLinkProxyArp_Type.__name__ = "TruthValue"
_TnCNLinkProxyArp_Object = MibTableColumn
tnCNLinkProxyArp = _TnCNLinkProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 38),
    _TnCNLinkProxyArp_Type()
)
tnCNLinkProxyArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkProxyArp.setStatus("current")


class _TnCNLinkDHCPServer_Type(TruthValue):
    """Custom type tnCNLinkDHCPServer based on TruthValue"""
    defaultValue = 1


_TnCNLinkDHCPServer_Type.__name__ = "TruthValue"
_TnCNLinkDHCPServer_Object = MibTableColumn
tnCNLinkDHCPServer = _TnCNLinkDHCPServer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 39),
    _TnCNLinkDHCPServer_Type()
)
tnCNLinkDHCPServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDHCPServer.setStatus("current")


class _TnCNLinkDHCPRange_Type(Unsigned32):
    """Custom type tnCNLinkDHCPRange based on Unsigned32"""
    defaultValue = 1


_TnCNLinkDHCPRange_Type.__name__ = "Unsigned32"
_TnCNLinkDHCPRange_Object = MibTableColumn
tnCNLinkDHCPRange = _TnCNLinkDHCPRange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 40),
    _TnCNLinkDHCPRange_Type()
)
tnCNLinkDHCPRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDHCPRange.setStatus("current")


class _TnCNLinkAdjState_Type(TropicOspfAdjacencyStateType):
    """Custom type tnCNLinkAdjState based on TropicOspfAdjacencyStateType"""
    defaultValue = 1


_TnCNLinkAdjState_Type.__name__ = "TropicOspfAdjacencyStateType"
_TnCNLinkAdjState_Object = MibTableColumn
tnCNLinkAdjState = _TnCNLinkAdjState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 41),
    _TnCNLinkAdjState_Type()
)
tnCNLinkAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkAdjState.setStatus("current")


class _TnCNLinkOscMode_Type(Integer32):
    """Custom type tnCNLinkOscMode based on Integer32"""
    defaultValue = 1

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
        *(("oc3stm1", 1),
          ("base100FX", 2),
          ("oneGE", 3),
          ("base100FX1", 4))
    )


_TnCNLinkOscMode_Type.__name__ = "Integer32"
_TnCNLinkOscMode_Object = MibTableColumn
tnCNLinkOscMode = _TnCNLinkOscMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 42),
    _TnCNLinkOscMode_Type()
)
tnCNLinkOscMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOscMode.setStatus("current")


class _TnCNLinkDHCPDfltGtwy_Type(TruthValue):
    """Custom type tnCNLinkDHCPDfltGtwy based on TruthValue"""
    defaultValue = 1


_TnCNLinkDHCPDfltGtwy_Type.__name__ = "TruthValue"
_TnCNLinkDHCPDfltGtwy_Object = MibTableColumn
tnCNLinkDHCPDfltGtwy = _TnCNLinkDHCPDfltGtwy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 43),
    _TnCNLinkDHCPDfltGtwy_Type()
)
tnCNLinkDHCPDfltGtwy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDHCPDfltGtwy.setStatus("current")


class _TnCNLinkCitAutoStateCtrl_Type(TruthValue):
    """Custom type tnCNLinkCitAutoStateCtrl based on TruthValue"""
    defaultValue = 2


_TnCNLinkCitAutoStateCtrl_Type.__name__ = "TruthValue"
_TnCNLinkCitAutoStateCtrl_Object = MibTableColumn
tnCNLinkCitAutoStateCtrl = _TnCNLinkCitAutoStateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 44),
    _TnCNLinkCitAutoStateCtrl_Type()
)
tnCNLinkCitAutoStateCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkCitAutoStateCtrl.setStatus("current")


class _TnCNLinkAutoStateSourceIP_Type(IpAddress):
    """Custom type tnCNLinkAutoStateSourceIP based on IpAddress"""
    defaultHexValue = "00000000"


_TnCNLinkAutoStateSourceIP_Type.__name__ = "IpAddress"
_TnCNLinkAutoStateSourceIP_Object = MibTableColumn
tnCNLinkAutoStateSourceIP = _TnCNLinkAutoStateSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 45),
    _TnCNLinkAutoStateSourceIP_Type()
)
tnCNLinkAutoStateSourceIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkAutoStateSourceIP.setStatus("current")


class _TnCNLinkSourceLossCount_Type(Unsigned32):
    """Custom type tnCNLinkSourceLossCount based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10000),
    )


_TnCNLinkSourceLossCount_Type.__name__ = "Unsigned32"
_TnCNLinkSourceLossCount_Object = MibTableColumn
tnCNLinkSourceLossCount = _TnCNLinkSourceLossCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 46),
    _TnCNLinkSourceLossCount_Type()
)
tnCNLinkSourceLossCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkSourceLossCount.setStatus("current")


class _TnCNLinkSourceIPCheckInterval_Type(Unsigned32):
    """Custom type tnCNLinkSourceIPCheckInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 7200),
    )


_TnCNLinkSourceIPCheckInterval_Type.__name__ = "Unsigned32"
_TnCNLinkSourceIPCheckInterval_Object = MibTableColumn
tnCNLinkSourceIPCheckInterval = _TnCNLinkSourceIPCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 47),
    _TnCNLinkSourceIPCheckInterval_Type()
)
tnCNLinkSourceIPCheckInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkSourceIPCheckInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnCNLinkSourceIPCheckInterval.setUnits("seconds")


class _TnCNLinkOspfAuthentType_Type(Integer32):
    """Custom type tnCNLinkOspfAuthentType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("simple", 2),
          ("md5", 3))
    )


_TnCNLinkOspfAuthentType_Type.__name__ = "Integer32"
_TnCNLinkOspfAuthentType_Object = MibTableColumn
tnCNLinkOspfAuthentType = _TnCNLinkOspfAuthentType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 48),
    _TnCNLinkOspfAuthentType_Type()
)
tnCNLinkOspfAuthentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfAuthentType.setStatus("current")


class _TnCNLinkOspfAuthKey_Type(SnmpAdminString):
    """Custom type tnCNLinkOspfAuthKey based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnCNLinkOspfAuthKey_Type.__name__ = "SnmpAdminString"
_TnCNLinkOspfAuthKey_Object = MibTableColumn
tnCNLinkOspfAuthKey = _TnCNLinkOspfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 49),
    _TnCNLinkOspfAuthKey_Type()
)
tnCNLinkOspfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfAuthKey.setStatus("current")


class _TnCNLinkOspfAuthKeyId_Type(Unsigned32):
    """Custom type tnCNLinkOspfAuthKeyId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnCNLinkOspfAuthKeyId_Type.__name__ = "Unsigned32"
_TnCNLinkOspfAuthKeyId_Object = MibTableColumn
tnCNLinkOspfAuthKeyId = _TnCNLinkOspfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 50),
    _TnCNLinkOspfAuthKeyId_Type()
)
tnCNLinkOspfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfAuthKeyId.setStatus("current")


class _TnCNLinkTdmxDcnConf_Type(Integer32):
    """Custom type tnCNLinkTdmxDcnConf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_TnCNLinkTdmxDcnConf_Type.__name__ = "Integer32"
_TnCNLinkTdmxDcnConf_Object = MibTableColumn
tnCNLinkTdmxDcnConf = _TnCNLinkTdmxDcnConf_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 51),
    _TnCNLinkTdmxDcnConf_Type()
)
tnCNLinkTdmxDcnConf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkTdmxDcnConf.setStatus("current")


class _TnCNLinkInetAddressType_Type(InetAddressType):
    """Custom type tnCNLinkInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnCNLinkInetAddressType_Type.__name__ = "InetAddressType"
_TnCNLinkInetAddressType_Object = MibTableColumn
tnCNLinkInetAddressType = _TnCNLinkInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 52),
    _TnCNLinkInetAddressType_Type()
)
tnCNLinkInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkInetAddressType.setStatus("current")


class _TnCNLinkInetAddress_Type(InetAddress):
    """Custom type tnCNLinkInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnCNLinkInetAddress_Type.__name__ = "InetAddress"
_TnCNLinkInetAddress_Object = MibTableColumn
tnCNLinkInetAddress = _TnCNLinkInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 53),
    _TnCNLinkInetAddress_Type()
)
tnCNLinkInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkInetAddress.setStatus("current")


class _TnCNLinkPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tnCNLinkPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_TnCNLinkPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TnCNLinkPrefixLength_Object = MibTableColumn
tnCNLinkPrefixLength = _TnCNLinkPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 54),
    _TnCNLinkPrefixLength_Type()
)
tnCNLinkPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkPrefixLength.setStatus("current")


class _TnCNLinkAutoStateSourceInetAddressType_Type(InetAddressType):
    """Custom type tnCNLinkAutoStateSourceInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnCNLinkAutoStateSourceInetAddressType_Type.__name__ = "InetAddressType"
_TnCNLinkAutoStateSourceInetAddressType_Object = MibTableColumn
tnCNLinkAutoStateSourceInetAddressType = _TnCNLinkAutoStateSourceInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 55),
    _TnCNLinkAutoStateSourceInetAddressType_Type()
)
tnCNLinkAutoStateSourceInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkAutoStateSourceInetAddressType.setStatus("current")


class _TnCNLinkAutoStateSourceInetAddress_Type(InetAddress):
    """Custom type tnCNLinkAutoStateSourceInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnCNLinkAutoStateSourceInetAddress_Type.__name__ = "InetAddress"
_TnCNLinkAutoStateSourceInetAddress_Object = MibTableColumn
tnCNLinkAutoStateSourceInetAddress = _TnCNLinkAutoStateSourceInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 56),
    _TnCNLinkAutoStateSourceInetAddress_Type()
)
tnCNLinkAutoStateSourceInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkAutoStateSourceInetAddress.setStatus("current")


class _TnCNLinkDhcpv6Enabled_Type(TruthValue):
    """Custom type tnCNLinkDhcpv6Enabled based on TruthValue"""
    defaultValue = 2


_TnCNLinkDhcpv6Enabled_Type.__name__ = "TruthValue"
_TnCNLinkDhcpv6Enabled_Object = MibTableColumn
tnCNLinkDhcpv6Enabled = _TnCNLinkDhcpv6Enabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 57),
    _TnCNLinkDhcpv6Enabled_Type()
)
tnCNLinkDhcpv6Enabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDhcpv6Enabled.setStatus("current")


class _TnCNLinkDHCPv6Range_Type(Unsigned32):
    """Custom type tnCNLinkDHCPv6Range based on Unsigned32"""
    defaultValue = 1


_TnCNLinkDHCPv6Range_Type.__name__ = "Unsigned32"
_TnCNLinkDHCPv6Range_Object = MibTableColumn
tnCNLinkDHCPv6Range = _TnCNLinkDHCPv6Range_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 58),
    _TnCNLinkDHCPv6Range_Type()
)
tnCNLinkDHCPv6Range.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDHCPv6Range.setStatus("current")


class _TnCNLinkDHCPClient_Type(TruthValue):
    """Custom type tnCNLinkDHCPClient based on TruthValue"""
    defaultValue = 1


_TnCNLinkDHCPClient_Type.__name__ = "TruthValue"
_TnCNLinkDHCPClient_Object = MibTableColumn
tnCNLinkDHCPClient = _TnCNLinkDHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 59),
    _TnCNLinkDHCPClient_Type()
)
tnCNLinkDHCPClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDHCPClient.setStatus("current")


class _TnCNLinkDHCPv6Client_Type(TruthValue):
    """Custom type tnCNLinkDHCPv6Client based on TruthValue"""
    defaultValue = 2


_TnCNLinkDHCPv6Client_Type.__name__ = "TruthValue"
_TnCNLinkDHCPv6Client_Object = MibTableColumn
tnCNLinkDHCPv6Client = _TnCNLinkDHCPv6Client_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 60),
    _TnCNLinkDHCPv6Client_Type()
)
tnCNLinkDHCPv6Client.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDHCPv6Client.setStatus("current")


class _TnCNLinkDHCPClientDfltGtwy_Type(TruthValue):
    """Custom type tnCNLinkDHCPClientDfltGtwy based on TruthValue"""
    defaultValue = 1


_TnCNLinkDHCPClientDfltGtwy_Type.__name__ = "TruthValue"
_TnCNLinkDHCPClientDfltGtwy_Object = MibTableColumn
tnCNLinkDHCPClientDfltGtwy = _TnCNLinkDHCPClientDfltGtwy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 61),
    _TnCNLinkDHCPClientDfltGtwy_Type()
)
tnCNLinkDHCPClientDfltGtwy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDHCPClientDfltGtwy.setStatus("current")


class _TnCNLinkEtherPortIpV6SLAAC_Type(TruthValue):
    """Custom type tnCNLinkEtherPortIpV6SLAAC based on TruthValue"""
    defaultValue = 2


_TnCNLinkEtherPortIpV6SLAAC_Type.__name__ = "TruthValue"
_TnCNLinkEtherPortIpV6SLAAC_Object = MibTableColumn
tnCNLinkEtherPortIpV6SLAAC = _TnCNLinkEtherPortIpV6SLAAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 62),
    _TnCNLinkEtherPortIpV6SLAAC_Type()
)
tnCNLinkEtherPortIpV6SLAAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkEtherPortIpV6SLAAC.setStatus("current")


class _TnCNLinkOspfRetransint_Type(Unsigned32):
    """Custom type tnCNLinkOspfRetransint based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnCNLinkOspfRetransint_Type.__name__ = "Unsigned32"
_TnCNLinkOspfRetransint_Object = MibTableColumn
tnCNLinkOspfRetransint = _TnCNLinkOspfRetransint_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 63),
    _TnCNLinkOspfRetransint_Type()
)
tnCNLinkOspfRetransint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfRetransint.setStatus("current")


class _TnCNLinkOspfv3AdjStateId_Type(TropicOspfAdjacencyStateType):
    """Custom type tnCNLinkOspfv3AdjStateId based on TropicOspfAdjacencyStateType"""
    defaultValue = 1


_TnCNLinkOspfv3AdjStateId_Type.__name__ = "TropicOspfAdjacencyStateType"
_TnCNLinkOspfv3AdjStateId_Object = MibTableColumn
tnCNLinkOspfv3AdjStateId = _TnCNLinkOspfv3AdjStateId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 64),
    _TnCNLinkOspfv3AdjStateId_Type()
)
tnCNLinkOspfv3AdjStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkOspfv3AdjStateId.setStatus("current")


class _TnCNLinkOspfNeighborRouterIp_Type(IpAddress):
    """Custom type tnCNLinkOspfNeighborRouterIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnCNLinkOspfNeighborRouterIp_Type.__name__ = "IpAddress"
_TnCNLinkOspfNeighborRouterIp_Object = MibTableColumn
tnCNLinkOspfNeighborRouterIp = _TnCNLinkOspfNeighborRouterIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 65),
    _TnCNLinkOspfNeighborRouterIp_Type()
)
tnCNLinkOspfNeighborRouterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkOspfNeighborRouterIp.setStatus("current")


class _TnCNLinkOspfv3NeighborRouterIp_Type(IpAddress):
    """Custom type tnCNLinkOspfv3NeighborRouterIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnCNLinkOspfv3NeighborRouterIp_Type.__name__ = "IpAddress"
_TnCNLinkOspfv3NeighborRouterIp_Object = MibTableColumn
tnCNLinkOspfv3NeighborRouterIp = _TnCNLinkOspfv3NeighborRouterIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 66),
    _TnCNLinkOspfv3NeighborRouterIp_Type()
)
tnCNLinkOspfv3NeighborRouterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkOspfv3NeighborRouterIp.setStatus("current")


class _TnCNLinkOspfNeighborIp_Type(IpAddress):
    """Custom type tnCNLinkOspfNeighborIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnCNLinkOspfNeighborIp_Type.__name__ = "IpAddress"
_TnCNLinkOspfNeighborIp_Object = MibTableColumn
tnCNLinkOspfNeighborIp = _TnCNLinkOspfNeighborIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 67),
    _TnCNLinkOspfNeighborIp_Type()
)
tnCNLinkOspfNeighborIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkOspfNeighborIp.setStatus("current")


class _TnCNLinkOspfv3NeighborInetAddress_Type(InetAddress):
    """Custom type tnCNLinkOspfv3NeighborInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnCNLinkOspfv3NeighborInetAddress_Type.__name__ = "InetAddress"
_TnCNLinkOspfv3NeighborInetAddress_Object = MibTableColumn
tnCNLinkOspfv3NeighborInetAddress = _TnCNLinkOspfv3NeighborInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 68),
    _TnCNLinkOspfv3NeighborInetAddress_Type()
)
tnCNLinkOspfv3NeighborInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkOspfv3NeighborInetAddress.setStatus("current")


class _TnCNLinkRole_Type(Integer32):
    """Custom type tnCNLinkRole based on Integer32"""
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
          ("oamp", 1),
          ("aux", 2))
    )


_TnCNLinkRole_Type.__name__ = "Integer32"
_TnCNLinkRole_Object = MibTableColumn
tnCNLinkRole = _TnCNLinkRole_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 69),
    _TnCNLinkRole_Type()
)
tnCNLinkRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkRole.setStatus("current")


class _TnCNLinkDHCPServerIPv6SLAAC_Type(SnmpAdminString):
    """Custom type tnCNLinkDHCPServerIPv6SLAAC based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnCNLinkDHCPServerIPv6SLAAC_Type.__name__ = "SnmpAdminString"
_TnCNLinkDHCPServerIPv6SLAAC_Object = MibTableColumn
tnCNLinkDHCPServerIPv6SLAAC = _TnCNLinkDHCPServerIPv6SLAAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 70),
    _TnCNLinkDHCPServerIPv6SLAAC_Type()
)
tnCNLinkDHCPServerIPv6SLAAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkDHCPServerIPv6SLAAC.setStatus("current")


class _TnCNLinkRouterAdvAutonomousFlag_Type(TruthValue):
    """Custom type tnCNLinkRouterAdvAutonomousFlag based on TruthValue"""
    defaultValue = 2


_TnCNLinkRouterAdvAutonomousFlag_Type.__name__ = "TruthValue"
_TnCNLinkRouterAdvAutonomousFlag_Object = MibTableColumn
tnCNLinkRouterAdvAutonomousFlag = _TnCNLinkRouterAdvAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 71),
    _TnCNLinkRouterAdvAutonomousFlag_Type()
)
tnCNLinkRouterAdvAutonomousFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkRouterAdvAutonomousFlag.setStatus("current")


class _TnCNLinkRouterAdvDefaultLifeTime_Type(Unsigned32):
    """Custom type tnCNLinkRouterAdvDefaultLifeTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
    )


_TnCNLinkRouterAdvDefaultLifeTime_Type.__name__ = "Unsigned32"
_TnCNLinkRouterAdvDefaultLifeTime_Object = MibTableColumn
tnCNLinkRouterAdvDefaultLifeTime = _TnCNLinkRouterAdvDefaultLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 72),
    _TnCNLinkRouterAdvDefaultLifeTime_Type()
)
tnCNLinkRouterAdvDefaultLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkRouterAdvDefaultLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tnCNLinkRouterAdvDefaultLifeTime.setUnits("seconds")


class _TnCNLinkRouterAdvDefaultPreference_Type(Integer32):
    """Custom type tnCNLinkRouterAdvDefaultPreference based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_TnCNLinkRouterAdvDefaultPreference_Type.__name__ = "Integer32"
_TnCNLinkRouterAdvDefaultPreference_Object = MibTableColumn
tnCNLinkRouterAdvDefaultPreference = _TnCNLinkRouterAdvDefaultPreference_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 73),
    _TnCNLinkRouterAdvDefaultPreference_Type()
)
tnCNLinkRouterAdvDefaultPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkRouterAdvDefaultPreference.setStatus("current")


class _TnCNLinkRouterAdvMaxRtrAdvInterval_Type(Unsigned32):
    """Custom type tnCNLinkRouterAdvMaxRtrAdvInterval based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1800),
    )


_TnCNLinkRouterAdvMaxRtrAdvInterval_Type.__name__ = "Unsigned32"
_TnCNLinkRouterAdvMaxRtrAdvInterval_Object = MibTableColumn
tnCNLinkRouterAdvMaxRtrAdvInterval = _TnCNLinkRouterAdvMaxRtrAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 74),
    _TnCNLinkRouterAdvMaxRtrAdvInterval_Type()
)
tnCNLinkRouterAdvMaxRtrAdvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkRouterAdvMaxRtrAdvInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnCNLinkRouterAdvMaxRtrAdvInterval.setUnits("seconds")


class _TnCNLinkRouterAdvManagedFlag_Type(TruthValue):
    """Custom type tnCNLinkRouterAdvManagedFlag based on TruthValue"""
    defaultValue = 2


_TnCNLinkRouterAdvManagedFlag_Type.__name__ = "TruthValue"
_TnCNLinkRouterAdvManagedFlag_Object = MibTableColumn
tnCNLinkRouterAdvManagedFlag = _TnCNLinkRouterAdvManagedFlag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 75),
    _TnCNLinkRouterAdvManagedFlag_Type()
)
tnCNLinkRouterAdvManagedFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkRouterAdvManagedFlag.setStatus("current")


class _TnCNLinkRouterAdvOtherConfigFlag_Type(TruthValue):
    """Custom type tnCNLinkRouterAdvOtherConfigFlag based on TruthValue"""
    defaultValue = 2


_TnCNLinkRouterAdvOtherConfigFlag_Type.__name__ = "TruthValue"
_TnCNLinkRouterAdvOtherConfigFlag_Object = MibTableColumn
tnCNLinkRouterAdvOtherConfigFlag = _TnCNLinkRouterAdvOtherConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 76),
    _TnCNLinkRouterAdvOtherConfigFlag_Type()
)
tnCNLinkRouterAdvOtherConfigFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkRouterAdvOtherConfigFlag.setStatus("current")


class _TnCNLinkRouterAdvPreferredLifeTime_Type(Unsigned32):
    """Custom type tnCNLinkRouterAdvPreferredLifeTime based on Unsigned32"""
    defaultValue = 14400


_TnCNLinkRouterAdvPreferredLifeTime_Type.__name__ = "Unsigned32"
_TnCNLinkRouterAdvPreferredLifeTime_Object = MibTableColumn
tnCNLinkRouterAdvPreferredLifeTime = _TnCNLinkRouterAdvPreferredLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 77),
    _TnCNLinkRouterAdvPreferredLifeTime_Type()
)
tnCNLinkRouterAdvPreferredLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkRouterAdvPreferredLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tnCNLinkRouterAdvPreferredLifeTime.setUnits("seconds")


class _TnCNLinkRouterAdvSendAdvertState_Type(TruthValue):
    """Custom type tnCNLinkRouterAdvSendAdvertState based on TruthValue"""
    defaultValue = 2


_TnCNLinkRouterAdvSendAdvertState_Type.__name__ = "TruthValue"
_TnCNLinkRouterAdvSendAdvertState_Object = MibTableColumn
tnCNLinkRouterAdvSendAdvertState = _TnCNLinkRouterAdvSendAdvertState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 78),
    _TnCNLinkRouterAdvSendAdvertState_Type()
)
tnCNLinkRouterAdvSendAdvertState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkRouterAdvSendAdvertState.setStatus("current")


class _TnCNLinkRouterAdvValidLifeTime_Type(Unsigned32):
    """Custom type tnCNLinkRouterAdvValidLifeTime based on Unsigned32"""
    defaultValue = 86400


_TnCNLinkRouterAdvValidLifeTime_Type.__name__ = "Unsigned32"
_TnCNLinkRouterAdvValidLifeTime_Object = MibTableColumn
tnCNLinkRouterAdvValidLifeTime = _TnCNLinkRouterAdvValidLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 79),
    _TnCNLinkRouterAdvValidLifeTime_Type()
)
tnCNLinkRouterAdvValidLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkRouterAdvValidLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tnCNLinkRouterAdvValidLifeTime.setUnits("seconds")


class _TnCNLinkAutoStateType_Type(Integer32):
    """Custom type tnCNLinkAutoStateType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("neInitiated", 1),
          ("nmsInitiated", 2))
    )


_TnCNLinkAutoStateType_Type.__name__ = "Integer32"
_TnCNLinkAutoStateType_Object = MibTableColumn
tnCNLinkAutoStateType = _TnCNLinkAutoStateType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 80),
    _TnCNLinkAutoStateType_Type()
)
tnCNLinkAutoStateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkAutoStateType.setStatus("current")


class _TnCNLinkAutoStateStatus_Type(Integer32):
    """Custom type tnCNLinkAutoStateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notConnected", 2),
          ("notApplicable", 3))
    )


_TnCNLinkAutoStateStatus_Type.__name__ = "Integer32"
_TnCNLinkAutoStateStatus_Object = MibTableColumn
tnCNLinkAutoStateStatus = _TnCNLinkAutoStateStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 81),
    _TnCNLinkAutoStateStatus_Type()
)
tnCNLinkAutoStateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkAutoStateStatus.setStatus("current")


class _TnCNLinkOspfv3HelloInterval_Type(Unsigned32):
    """Custom type tnCNLinkOspfv3HelloInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnCNLinkOspfv3HelloInterval_Type.__name__ = "Unsigned32"
_TnCNLinkOspfv3HelloInterval_Object = MibTableColumn
tnCNLinkOspfv3HelloInterval = _TnCNLinkOspfv3HelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 82),
    _TnCNLinkOspfv3HelloInterval_Type()
)
tnCNLinkOspfv3HelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfv3HelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnCNLinkOspfv3HelloInterval.setUnits("seconds")
_TnCNLinkOspfv3TeMetric_Type = Unsigned32
_TnCNLinkOspfv3TeMetric_Object = MibTableColumn
tnCNLinkOspfv3TeMetric = _TnCNLinkOspfv3TeMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 83),
    _TnCNLinkOspfv3TeMetric_Type()
)
tnCNLinkOspfv3TeMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfv3TeMetric.setStatus("current")


class _TnCNLinkOspfv3Retransint_Type(Unsigned32):
    """Custom type tnCNLinkOspfv3Retransint based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnCNLinkOspfv3Retransint_Type.__name__ = "Unsigned32"
_TnCNLinkOspfv3Retransint_Object = MibTableColumn
tnCNLinkOspfv3Retransint = _TnCNLinkOspfv3Retransint_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 84),
    _TnCNLinkOspfv3Retransint_Type()
)
tnCNLinkOspfv3Retransint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfv3Retransint.setStatus("current")


class _TnCNLinkOspfv3RtrDeadInterval_Type(Unsigned32):
    """Custom type tnCNLinkOspfv3RtrDeadInterval based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnCNLinkOspfv3RtrDeadInterval_Type.__name__ = "Unsigned32"
_TnCNLinkOspfv3RtrDeadInterval_Object = MibTableColumn
tnCNLinkOspfv3RtrDeadInterval = _TnCNLinkOspfv3RtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 85),
    _TnCNLinkOspfv3RtrDeadInterval_Type()
)
tnCNLinkOspfv3RtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfv3RtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnCNLinkOspfv3RtrDeadInterval.setUnits("seconds")


class _TnCNLinkOspfv3ConfigRtrPriority_Type(Unsigned32):
    """Custom type tnCNLinkOspfv3ConfigRtrPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnCNLinkOspfv3ConfigRtrPriority_Type.__name__ = "Unsigned32"
_TnCNLinkOspfv3ConfigRtrPriority_Object = MibTableColumn
tnCNLinkOspfv3ConfigRtrPriority = _TnCNLinkOspfv3ConfigRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 86),
    _TnCNLinkOspfv3ConfigRtrPriority_Type()
)
tnCNLinkOspfv3ConfigRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfv3ConfigRtrPriority.setStatus("current")


class _TnCNLinkOspfv3RoutingState_Type(NokiaCNLinkOspfRoutingState):
    """Custom type tnCNLinkOspfv3RoutingState based on NokiaCNLinkOspfRoutingState"""
    defaultValue = 1


_TnCNLinkOspfv3RoutingState_Type.__name__ = "NokiaCNLinkOspfRoutingState"
_TnCNLinkOspfv3RoutingState_Object = MibTableColumn
tnCNLinkOspfv3RoutingState = _TnCNLinkOspfv3RoutingState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 87),
    _TnCNLinkOspfv3RoutingState_Type()
)
tnCNLinkOspfv3RoutingState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfv3RoutingState.setStatus("current")


class _TnCNLinkOspfOscRoutingState_Type(NokiaCNLinkOspfRoutingState):
    """Custom type tnCNLinkOspfOscRoutingState based on NokiaCNLinkOspfRoutingState"""
    defaultValue = 2


_TnCNLinkOspfOscRoutingState_Type.__name__ = "NokiaCNLinkOspfRoutingState"
_TnCNLinkOspfOscRoutingState_Object = MibTableColumn
tnCNLinkOspfOscRoutingState = _TnCNLinkOspfOscRoutingState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 88),
    _TnCNLinkOspfOscRoutingState_Type()
)
tnCNLinkOspfOscRoutingState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfOscRoutingState.setStatus("current")


class _TnCNLinkOspfv6OscRoutingState_Type(NokiaCNLinkOspfRoutingState):
    """Custom type tnCNLinkOspfv6OscRoutingState based on NokiaCNLinkOspfRoutingState"""
    defaultValue = 1


_TnCNLinkOspfv6OscRoutingState_Type.__name__ = "NokiaCNLinkOspfRoutingState"
_TnCNLinkOspfv6OscRoutingState_Object = MibTableColumn
tnCNLinkOspfv6OscRoutingState = _TnCNLinkOspfv6OscRoutingState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 89),
    _TnCNLinkOspfv6OscRoutingState_Type()
)
tnCNLinkOspfv6OscRoutingState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkOspfv6OscRoutingState.setStatus("current")


class _TnCNLinkDHCPBootFileName_Type(OctetString):
    """Custom type tnCNLinkDHCPBootFileName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnCNLinkDHCPBootFileName_Type.__name__ = "OctetString"
_TnCNLinkDHCPBootFileName_Object = MibTableColumn
tnCNLinkDHCPBootFileName = _TnCNLinkDHCPBootFileName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 90),
    _TnCNLinkDHCPBootFileName_Type()
)
tnCNLinkDHCPBootFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDHCPBootFileName.setStatus("current")


class _TnCNLinkDHCPClassName_Type(OctetString):
    """Custom type tnCNLinkDHCPClassName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnCNLinkDHCPClassName_Type.__name__ = "OctetString"
_TnCNLinkDHCPClassName_Object = MibTableColumn
tnCNLinkDHCPClassName = _TnCNLinkDHCPClassName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 1, 1, 91),
    _TnCNLinkDHCPClassName_Type()
)
tnCNLinkDHCPClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCNLinkDHCPClassName.setStatus("current")
_TnCNLinkViaChannelTable_Object = MibTable
tnCNLinkViaChannelTable = _TnCNLinkViaChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnCNLinkViaChannelTable.setStatus("current")
_TnCNLinkViaChannelEntry_Object = MibTableRow
tnCNLinkViaChannelEntry = _TnCNLinkViaChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 2, 1)
)
tnCNLinkViaChannelEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-L1SERVICE-MIB", "tnPortIndex"),
    (0, "TROPIC-L1SERVICE-MIB", "tnChannelIndex"),
)
if mibBuilder.loadTexts:
    tnCNLinkViaChannelEntry.setStatus("current")
_TnPortIndex_Type = TropicPortIndexType
_TnPortIndex_Object = MibTableColumn
tnPortIndex = _TnPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 2, 1, 1),
    _TnPortIndex_Type()
)
tnPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPortIndex.setStatus("current")
_TnChannelIndex_Type = TropicChannelIndexType
_TnChannelIndex_Object = MibTableColumn
tnChannelIndex = _TnChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 2, 1, 2),
    _TnChannelIndex_Type()
)
tnChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnChannelIndex.setStatus("current")
_TnCNLinkViaChannelIfIndex_Type = InterfaceIndex
_TnCNLinkViaChannelIfIndex_Object = MibTableColumn
tnCNLinkViaChannelIfIndex = _TnCNLinkViaChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 1, 2, 1, 3),
    _TnCNLinkViaChannelIfIndex_Type()
)
tnCNLinkViaChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNLinkViaChannelIfIndex.setStatus("current")
_TnDataNetworkLink_ObjectIdentity = ObjectIdentity
tnDataNetworkLink = _TnDataNetworkLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 2)
)
_TnL1TrafficParamTable_Object = MibTable
tnL1TrafficParamTable = _TnL1TrafficParamTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    tnL1TrafficParamTable.setStatus("current")
_TnL1TrafficParamEntry_Object = MibTableRow
tnL1TrafficParamEntry = _TnL1TrafficParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 2, 3, 1)
)
tnL1TrafficParamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-L1SERVICE-MIB", "tnL1TrafficParamPerHopBehaviour"),
)
if mibBuilder.loadTexts:
    tnL1TrafficParamEntry.setStatus("current")
_TnL1TrafficParamPerHopBehaviour_Type = TnPerHopBehaviourType
_TnL1TrafficParamPerHopBehaviour_Object = MibTableColumn
tnL1TrafficParamPerHopBehaviour = _TnL1TrafficParamPerHopBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 2, 3, 1, 1),
    _TnL1TrafficParamPerHopBehaviour_Type()
)
tnL1TrafficParamPerHopBehaviour.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnL1TrafficParamPerHopBehaviour.setStatus("current")
_TnL1TrafficParamBookingFactor_Type = Unsigned32
_TnL1TrafficParamBookingFactor_Object = MibTableColumn
tnL1TrafficParamBookingFactor = _TnL1TrafficParamBookingFactor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 2, 3, 1, 2),
    _TnL1TrafficParamBookingFactor_Type()
)
tnL1TrafficParamBookingFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnL1TrafficParamBookingFactor.setStatus("current")
if mibBuilder.loadTexts:
    tnL1TrafficParamBookingFactor.setUnits("percentage")
_TnL1TrafficParamMaximumLoad_Type = Unsigned32
_TnL1TrafficParamMaximumLoad_Object = MibTableColumn
tnL1TrafficParamMaximumLoad = _TnL1TrafficParamMaximumLoad_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 2, 3, 1, 3),
    _TnL1TrafficParamMaximumLoad_Type()
)
tnL1TrafficParamMaximumLoad.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnL1TrafficParamMaximumLoad.setStatus("current")
if mibBuilder.loadTexts:
    tnL1TrafficParamMaximumLoad.setUnits("percentage")
_TnL1TrafficParamPMF_Type = Unsigned32
_TnL1TrafficParamPMF_Object = MibTableColumn
tnL1TrafficParamPMF = _TnL1TrafficParamPMF_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 2, 3, 1, 4),
    _TnL1TrafficParamPMF_Type()
)
tnL1TrafficParamPMF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnL1TrafficParamPMF.setStatus("current")
if mibBuilder.loadTexts:
    tnL1TrafficParamPMF.setUnits("percentage")
_TnL1TrafficParamAvailableBandwidth_Type = Unsigned32
_TnL1TrafficParamAvailableBandwidth_Object = MibTableColumn
tnL1TrafficParamAvailableBandwidth = _TnL1TrafficParamAvailableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 2, 3, 1, 5),
    _TnL1TrafficParamAvailableBandwidth_Type()
)
tnL1TrafficParamAvailableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnL1TrafficParamAvailableBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    tnL1TrafficParamAvailableBandwidth.setUnits("Mb/s")
_TnIpRoute_ObjectIdentity = ObjectIdentity
tnIpRoute = _TnIpRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4)
)
_TnIpStaticRouteTable_Object = MibTable
tnIpStaticRouteTable = _TnIpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tnIpStaticRouteTable.setStatus("deprecated")
_TnIpStaticRouteEntry_Object = MibTableRow
tnIpStaticRouteEntry = _TnIpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1, 1)
)
tnIpStaticRouteEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnIpStaticRouteDest"),
    (0, "TROPIC-L1SERVICE-MIB", "tnIpStaticRouteMask"),
    (0, "TROPIC-L1SERVICE-MIB", "tnIpStaticRouteTos"),
    (0, "TROPIC-L1SERVICE-MIB", "tnIpStaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    tnIpStaticRouteEntry.setStatus("deprecated")
_TnIpStaticRouteDest_Type = IpAddress
_TnIpStaticRouteDest_Object = MibTableColumn
tnIpStaticRouteDest = _TnIpStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1, 1, 1),
    _TnIpStaticRouteDest_Type()
)
tnIpStaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpStaticRouteDest.setStatus("deprecated")
_TnIpStaticRouteMask_Type = IpAddress
_TnIpStaticRouteMask_Object = MibTableColumn
tnIpStaticRouteMask = _TnIpStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1, 1, 2),
    _TnIpStaticRouteMask_Type()
)
tnIpStaticRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpStaticRouteMask.setStatus("deprecated")
_TnIpStaticRouteTos_Type = Integer32
_TnIpStaticRouteTos_Object = MibTableColumn
tnIpStaticRouteTos = _TnIpStaticRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1, 1, 3),
    _TnIpStaticRouteTos_Type()
)
tnIpStaticRouteTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpStaticRouteTos.setStatus("deprecated")
_TnIpStaticRouteNextHop_Type = Unsigned32
_TnIpStaticRouteNextHop_Object = MibTableColumn
tnIpStaticRouteNextHop = _TnIpStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1, 1, 4),
    _TnIpStaticRouteNextHop_Type()
)
tnIpStaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpStaticRouteNextHop.setStatus("deprecated")


class _TnIpStaticRouteMetric_Type(Integer32):
    """Custom type tnIpStaticRouteMetric based on Integer32"""
    defaultValue = -1


_TnIpStaticRouteMetric_Type.__name__ = "Integer32"
_TnIpStaticRouteMetric_Object = MibTableColumn
tnIpStaticRouteMetric = _TnIpStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1, 1, 6),
    _TnIpStaticRouteMetric_Type()
)
tnIpStaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpStaticRouteMetric.setStatus("deprecated")


class _TnIpStaticRouteWithRedistribution_Type(TruthValue):
    """Custom type tnIpStaticRouteWithRedistribution based on TruthValue"""
    defaultValue = 2


_TnIpStaticRouteWithRedistribution_Type.__name__ = "TruthValue"
_TnIpStaticRouteWithRedistribution_Object = MibTableColumn
tnIpStaticRouteWithRedistribution = _TnIpStaticRouteWithRedistribution_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1, 1, 7),
    _TnIpStaticRouteWithRedistribution_Type()
)
tnIpStaticRouteWithRedistribution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpStaticRouteWithRedistribution.setStatus("deprecated")
_TnIpStaticRouteRowStatus_Type = RowStatus
_TnIpStaticRouteRowStatus_Object = MibTableColumn
tnIpStaticRouteRowStatus = _TnIpStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 1, 1, 8),
    _TnIpStaticRouteRowStatus_Type()
)
tnIpStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpStaticRouteRowStatus.setStatus("deprecated")
_TnIpCidrRouteTable_Object = MibTable
tnIpCidrRouteTable = _TnIpCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    tnIpCidrRouteTable.setStatus("current")
_TnIpCidrRouteEntry_Object = MibTableRow
tnIpCidrRouteEntry = _TnIpCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    tnIpCidrRouteEntry.setStatus("current")


class _TnIpCidrRouteWithRedistribution_Type(TruthValue):
    """Custom type tnIpCidrRouteWithRedistribution based on TruthValue"""
    defaultValue = 2


_TnIpCidrRouteWithRedistribution_Type.__name__ = "TruthValue"
_TnIpCidrRouteWithRedistribution_Object = MibTableColumn
tnIpCidrRouteWithRedistribution = _TnIpCidrRouteWithRedistribution_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 2, 1, 1),
    _TnIpCidrRouteWithRedistribution_Type()
)
tnIpCidrRouteWithRedistribution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpCidrRouteWithRedistribution.setStatus("current")
_TnIpRouteGlobal_ObjectIdentity = ObjectIdentity
tnIpRouteGlobal = _TnIpRouteGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3)
)


class _TnIpStaticRouteRedistributeMetricType_Type(Unsigned32):
    """Custom type tnIpStaticRouteRedistributeMetricType based on Unsigned32"""
    defaultValue = 2


_TnIpStaticRouteRedistributeMetricType_Type.__name__ = "Unsigned32"
_TnIpStaticRouteRedistributeMetricType_Object = MibScalar
tnIpStaticRouteRedistributeMetricType = _TnIpStaticRouteRedistributeMetricType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 1),
    _TnIpStaticRouteRedistributeMetricType_Type()
)
tnIpStaticRouteRedistributeMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpStaticRouteRedistributeMetricType.setStatus("current")


class _TnIpStaticRouteRedistributeMetric_Type(Unsigned32):
    """Custom type tnIpStaticRouteRedistributeMetric based on Unsigned32"""
    defaultValue = 20


_TnIpStaticRouteRedistributeMetric_Type.__name__ = "Unsigned32"
_TnIpStaticRouteRedistributeMetric_Object = MibScalar
tnIpStaticRouteRedistributeMetric = _TnIpStaticRouteRedistributeMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 2),
    _TnIpStaticRouteRedistributeMetric_Type()
)
tnIpStaticRouteRedistributeMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpStaticRouteRedistributeMetric.setStatus("current")


class _TnIpDefaultRouteRedistributeMetricType_Type(Unsigned32):
    """Custom type tnIpDefaultRouteRedistributeMetricType based on Unsigned32"""
    defaultValue = 2


_TnIpDefaultRouteRedistributeMetricType_Type.__name__ = "Unsigned32"
_TnIpDefaultRouteRedistributeMetricType_Object = MibScalar
tnIpDefaultRouteRedistributeMetricType = _TnIpDefaultRouteRedistributeMetricType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 3),
    _TnIpDefaultRouteRedistributeMetricType_Type()
)
tnIpDefaultRouteRedistributeMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpDefaultRouteRedistributeMetricType.setStatus("current")


class _TnIpDefaultRouteRedistributeMetric_Type(Unsigned32):
    """Custom type tnIpDefaultRouteRedistributeMetric based on Unsigned32"""
    defaultValue = 10


_TnIpDefaultRouteRedistributeMetric_Type.__name__ = "Unsigned32"
_TnIpDefaultRouteRedistributeMetric_Object = MibScalar
tnIpDefaultRouteRedistributeMetric = _TnIpDefaultRouteRedistributeMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 4),
    _TnIpDefaultRouteRedistributeMetric_Type()
)
tnIpDefaultRouteRedistributeMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpDefaultRouteRedistributeMetric.setStatus("current")


class _TnIpOspfAreaNumberPPPId_Type(Integer32):
    """Custom type tnIpOspfAreaNumberPPPId based on Integer32"""
    defaultValue = 0


_TnIpOspfAreaNumberPPPId_Type.__name__ = "Integer32"
_TnIpOspfAreaNumberPPPId_Object = MibScalar
tnIpOspfAreaNumberPPPId = _TnIpOspfAreaNumberPPPId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 5),
    _TnIpOspfAreaNumberPPPId_Type()
)
tnIpOspfAreaNumberPPPId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpOspfAreaNumberPPPId.setStatus("current")


class _TnIpOspfRouterId_Type(IpAddress):
    """Custom type tnIpOspfRouterId based on IpAddress"""
    defaultHexValue = "AC100101"


_TnIpOspfRouterId_Type.__name__ = "IpAddress"
_TnIpOspfRouterId_Object = MibScalar
tnIpOspfRouterId = _TnIpOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 6),
    _TnIpOspfRouterId_Type()
)
tnIpOspfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpOspfRouterId.setStatus("current")


class _TnIpDefaultRouteRedistributeBgpToOspfMetricType_Type(Unsigned32):
    """Custom type tnIpDefaultRouteRedistributeBgpToOspfMetricType based on Unsigned32"""
    defaultValue = 2


_TnIpDefaultRouteRedistributeBgpToOspfMetricType_Type.__name__ = "Unsigned32"
_TnIpDefaultRouteRedistributeBgpToOspfMetricType_Object = MibScalar
tnIpDefaultRouteRedistributeBgpToOspfMetricType = _TnIpDefaultRouteRedistributeBgpToOspfMetricType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 7),
    _TnIpDefaultRouteRedistributeBgpToOspfMetricType_Type()
)
tnIpDefaultRouteRedistributeBgpToOspfMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpDefaultRouteRedistributeBgpToOspfMetricType.setStatus("current")


class _TnIpDefaultRouteRedistributeBgpToOspfMetric_Type(Unsigned32):
    """Custom type tnIpDefaultRouteRedistributeBgpToOspfMetric based on Unsigned32"""
    defaultValue = 10


_TnIpDefaultRouteRedistributeBgpToOspfMetric_Type.__name__ = "Unsigned32"
_TnIpDefaultRouteRedistributeBgpToOspfMetric_Object = MibScalar
tnIpDefaultRouteRedistributeBgpToOspfMetric = _TnIpDefaultRouteRedistributeBgpToOspfMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 8),
    _TnIpDefaultRouteRedistributeBgpToOspfMetric_Type()
)
tnIpDefaultRouteRedistributeBgpToOspfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpDefaultRouteRedistributeBgpToOspfMetric.setStatus("current")


class _TnIpDefaultRouteRedistributeBgpToOspfMode_Type(Integer32):
    """Custom type tnIpDefaultRouteRedistributeBgpToOspfMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("useMetric", 2),
          ("useBgpMed", 3))
    )


_TnIpDefaultRouteRedistributeBgpToOspfMode_Type.__name__ = "Integer32"
_TnIpDefaultRouteRedistributeBgpToOspfMode_Object = MibScalar
tnIpDefaultRouteRedistributeBgpToOspfMode = _TnIpDefaultRouteRedistributeBgpToOspfMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 9),
    _TnIpDefaultRouteRedistributeBgpToOspfMode_Type()
)
tnIpDefaultRouteRedistributeBgpToOspfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpDefaultRouteRedistributeBgpToOspfMode.setStatus("current")


class _TnIpDefaultRouteRedistributeKernelToOspfMetricType_Type(Unsigned32):
    """Custom type tnIpDefaultRouteRedistributeKernelToOspfMetricType based on Unsigned32"""
    defaultValue = 2


_TnIpDefaultRouteRedistributeKernelToOspfMetricType_Type.__name__ = "Unsigned32"
_TnIpDefaultRouteRedistributeKernelToOspfMetricType_Object = MibScalar
tnIpDefaultRouteRedistributeKernelToOspfMetricType = _TnIpDefaultRouteRedistributeKernelToOspfMetricType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 10),
    _TnIpDefaultRouteRedistributeKernelToOspfMetricType_Type()
)
tnIpDefaultRouteRedistributeKernelToOspfMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpDefaultRouteRedistributeKernelToOspfMetricType.setStatus("current")


class _TnIpDefaultRouteRedistributeKernelToOspfMetric_Type(Unsigned32):
    """Custom type tnIpDefaultRouteRedistributeKernelToOspfMetric based on Unsigned32"""
    defaultValue = 10


_TnIpDefaultRouteRedistributeKernelToOspfMetric_Type.__name__ = "Unsigned32"
_TnIpDefaultRouteRedistributeKernelToOspfMetric_Object = MibScalar
tnIpDefaultRouteRedistributeKernelToOspfMetric = _TnIpDefaultRouteRedistributeKernelToOspfMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 11),
    _TnIpDefaultRouteRedistributeKernelToOspfMetric_Type()
)
tnIpDefaultRouteRedistributeKernelToOspfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpDefaultRouteRedistributeKernelToOspfMetric.setStatus("current")


class _TnIpDefaultRouteRedistributeKernelToOspfStatus_Type(TruthValue):
    """Custom type tnIpDefaultRouteRedistributeKernelToOspfStatus based on TruthValue"""
    defaultValue = 2


_TnIpDefaultRouteRedistributeKernelToOspfStatus_Type.__name__ = "TruthValue"
_TnIpDefaultRouteRedistributeKernelToOspfStatus_Object = MibScalar
tnIpDefaultRouteRedistributeKernelToOspfStatus = _TnIpDefaultRouteRedistributeKernelToOspfStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 12),
    _TnIpDefaultRouteRedistributeKernelToOspfStatus_Type()
)
tnIpDefaultRouteRedistributeKernelToOspfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpDefaultRouteRedistributeKernelToOspfStatus.setStatus("current")


class _TnIpStaticRouteRedistributeBgpMetric_Type(Unsigned32):
    """Custom type tnIpStaticRouteRedistributeBgpMetric based on Unsigned32"""
    defaultValue = 1


_TnIpStaticRouteRedistributeBgpMetric_Type.__name__ = "Unsigned32"
_TnIpStaticRouteRedistributeBgpMetric_Object = MibScalar
tnIpStaticRouteRedistributeBgpMetric = _TnIpStaticRouteRedistributeBgpMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 13),
    _TnIpStaticRouteRedistributeBgpMetric_Type()
)
tnIpStaticRouteRedistributeBgpMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpStaticRouteRedistributeBgpMetric.setStatus("current")


class _TnIpOspfV3AreaNumberPPPId_Type(Integer32):
    """Custom type tnIpOspfV3AreaNumberPPPId based on Integer32"""
    defaultValue = 0


_TnIpOspfV3AreaNumberPPPId_Type.__name__ = "Integer32"
_TnIpOspfV3AreaNumberPPPId_Object = MibScalar
tnIpOspfV3AreaNumberPPPId = _TnIpOspfV3AreaNumberPPPId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 14),
    _TnIpOspfV3AreaNumberPPPId_Type()
)
tnIpOspfV3AreaNumberPPPId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpOspfV3AreaNumberPPPId.setStatus("current")


class _TnIpDefaultRouteRedistributeOspfToBgpMode_Type(Integer32):
    """Custom type tnIpDefaultRouteRedistributeOspfToBgpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("useOspfMetric", 2),
          ("userDefined", 3))
    )


_TnIpDefaultRouteRedistributeOspfToBgpMode_Type.__name__ = "Integer32"
_TnIpDefaultRouteRedistributeOspfToBgpMode_Object = MibScalar
tnIpDefaultRouteRedistributeOspfToBgpMode = _TnIpDefaultRouteRedistributeOspfToBgpMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 15),
    _TnIpDefaultRouteRedistributeOspfToBgpMode_Type()
)
tnIpDefaultRouteRedistributeOspfToBgpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpDefaultRouteRedistributeOspfToBgpMode.setStatus("current")
_TnIpDefaultRouteRedistributeOspfToBgpMetric_Type = Unsigned32
_TnIpDefaultRouteRedistributeOspfToBgpMetric_Object = MibScalar
tnIpDefaultRouteRedistributeOspfToBgpMetric = _TnIpDefaultRouteRedistributeOspfToBgpMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 3, 16),
    _TnIpDefaultRouteRedistributeOspfToBgpMetric_Type()
)
tnIpDefaultRouteRedistributeOspfToBgpMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpDefaultRouteRedistributeOspfToBgpMetric.setStatus("current")
_TnIpNonDefaultRouteOspfToBgpCommTagTable_Object = MibTable
tnIpNonDefaultRouteOspfToBgpCommTagTable = _TnIpNonDefaultRouteOspfToBgpCommTagTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 4)
)
if mibBuilder.loadTexts:
    tnIpNonDefaultRouteOspfToBgpCommTagTable.setStatus("current")
_TnIpNonDefaultRouteOspfToBgpCommTagEntry_Object = MibTableRow
tnIpNonDefaultRouteOspfToBgpCommTagEntry = _TnIpNonDefaultRouteOspfToBgpCommTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 4, 1)
)
tnIpNonDefaultRouteOspfToBgpCommTagEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnIpNonDefaultRouteOspfToBgpCommTagIndex"),
)
if mibBuilder.loadTexts:
    tnIpNonDefaultRouteOspfToBgpCommTagEntry.setStatus("current")
_TnIpNonDefaultRouteOspfToBgpCommTagIndex_Type = Unsigned32
_TnIpNonDefaultRouteOspfToBgpCommTagIndex_Object = MibTableColumn
tnIpNonDefaultRouteOspfToBgpCommTagIndex = _TnIpNonDefaultRouteOspfToBgpCommTagIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 4, 1, 1),
    _TnIpNonDefaultRouteOspfToBgpCommTagIndex_Type()
)
tnIpNonDefaultRouteOspfToBgpCommTagIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpNonDefaultRouteOspfToBgpCommTagIndex.setStatus("current")
_TnIpNonDefaultRouteOspfToBgpCommTagRowStatus_Type = RowStatus
_TnIpNonDefaultRouteOspfToBgpCommTagRowStatus_Object = MibTableColumn
tnIpNonDefaultRouteOspfToBgpCommTagRowStatus = _TnIpNonDefaultRouteOspfToBgpCommTagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 4, 1, 2),
    _TnIpNonDefaultRouteOspfToBgpCommTagRowStatus_Type()
)
tnIpNonDefaultRouteOspfToBgpCommTagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpNonDefaultRouteOspfToBgpCommTagRowStatus.setStatus("current")


class _TnIpNonDefaultRouteOspfToBgpCommTag_Type(SnmpAdminString):
    """Custom type tnIpNonDefaultRouteOspfToBgpCommTag based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnIpNonDefaultRouteOspfToBgpCommTag_Type.__name__ = "SnmpAdminString"
_TnIpNonDefaultRouteOspfToBgpCommTag_Object = MibTableColumn
tnIpNonDefaultRouteOspfToBgpCommTag = _TnIpNonDefaultRouteOspfToBgpCommTag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 4, 1, 3),
    _TnIpNonDefaultRouteOspfToBgpCommTag_Type()
)
tnIpNonDefaultRouteOspfToBgpCommTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpNonDefaultRouteOspfToBgpCommTag.setStatus("current")
_TnIpNonDefaultRedistBgpToOspfRuleTable_Object = MibTable
tnIpNonDefaultRedistBgpToOspfRuleTable = _TnIpNonDefaultRedistBgpToOspfRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 5)
)
if mibBuilder.loadTexts:
    tnIpNonDefaultRedistBgpToOspfRuleTable.setStatus("current")
_TnIpNonDefaultRedistBgpToOspfRuleEntry_Object = MibTableRow
tnIpNonDefaultRedistBgpToOspfRuleEntry = _TnIpNonDefaultRedistBgpToOspfRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 5, 1)
)
tnIpNonDefaultRedistBgpToOspfRuleEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnIpNonDefaultRedistBgpToOspfRuleIndex"),
)
if mibBuilder.loadTexts:
    tnIpNonDefaultRedistBgpToOspfRuleEntry.setStatus("current")
_TnIpNonDefaultRedistBgpToOspfRuleIndex_Type = OctetString
_TnIpNonDefaultRedistBgpToOspfRuleIndex_Object = MibTableColumn
tnIpNonDefaultRedistBgpToOspfRuleIndex = _TnIpNonDefaultRedistBgpToOspfRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 5, 1, 1),
    _TnIpNonDefaultRedistBgpToOspfRuleIndex_Type()
)
tnIpNonDefaultRedistBgpToOspfRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpNonDefaultRedistBgpToOspfRuleIndex.setStatus("current")
_TnIpNonDefaultRedistBgpToOspfRuleRowStatus_Type = RowStatus
_TnIpNonDefaultRedistBgpToOspfRuleRowStatus_Object = MibTableColumn
tnIpNonDefaultRedistBgpToOspfRuleRowStatus = _TnIpNonDefaultRedistBgpToOspfRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 5, 1, 2),
    _TnIpNonDefaultRedistBgpToOspfRuleRowStatus_Type()
)
tnIpNonDefaultRedistBgpToOspfRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpNonDefaultRedistBgpToOspfRuleRowStatus.setStatus("current")
_TnIpNonDefaultRedistBgpToOspfRuleOspfTag_Type = Unsigned32
_TnIpNonDefaultRedistBgpToOspfRuleOspfTag_Object = MibTableColumn
tnIpNonDefaultRedistBgpToOspfRuleOspfTag = _TnIpNonDefaultRedistBgpToOspfRuleOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 5, 1, 3),
    _TnIpNonDefaultRedistBgpToOspfRuleOspfTag_Type()
)
tnIpNonDefaultRedistBgpToOspfRuleOspfTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpNonDefaultRedistBgpToOspfRuleOspfTag.setStatus("current")


class _TnIpNonDefaultRedistBgpToOspfRuleMode_Type(Integer32):
    """Custom type tnIpNonDefaultRedistBgpToOspfRuleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useBgpMed", 1),
          ("userDefined", 2))
    )


_TnIpNonDefaultRedistBgpToOspfRuleMode_Type.__name__ = "Integer32"
_TnIpNonDefaultRedistBgpToOspfRuleMode_Object = MibTableColumn
tnIpNonDefaultRedistBgpToOspfRuleMode = _TnIpNonDefaultRedistBgpToOspfRuleMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 5, 1, 4),
    _TnIpNonDefaultRedistBgpToOspfRuleMode_Type()
)
tnIpNonDefaultRedistBgpToOspfRuleMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpNonDefaultRedistBgpToOspfRuleMode.setStatus("current")
_TnIpNonDefaultRedistBgpToOspfRuleMetric_Type = Unsigned32
_TnIpNonDefaultRedistBgpToOspfRuleMetric_Object = MibTableColumn
tnIpNonDefaultRedistBgpToOspfRuleMetric = _TnIpNonDefaultRedistBgpToOspfRuleMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 5, 1, 5),
    _TnIpNonDefaultRedistBgpToOspfRuleMetric_Type()
)
tnIpNonDefaultRedistBgpToOspfRuleMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpNonDefaultRedistBgpToOspfRuleMetric.setStatus("current")
_TnIpNonDefaultRedistBgpToOspfRuleMetricType_Type = Unsigned32
_TnIpNonDefaultRedistBgpToOspfRuleMetricType_Object = MibTableColumn
tnIpNonDefaultRedistBgpToOspfRuleMetricType = _TnIpNonDefaultRedistBgpToOspfRuleMetricType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 4, 5, 1, 6),
    _TnIpNonDefaultRedistBgpToOspfRuleMetricType_Type()
)
tnIpNonDefaultRedistBgpToOspfRuleMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpNonDefaultRedistBgpToOspfRuleMetricType.setStatus("current")
_TnSharedRiskGroupObjs_ObjectIdentity = ObjectIdentity
tnSharedRiskGroupObjs = _TnSharedRiskGroupObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 5)
)
_TnL1NetworkLink_ObjectIdentity = ObjectIdentity
tnL1NetworkLink = _TnL1NetworkLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 5, 1)
)
_TnL1Hop_ObjectIdentity = ObjectIdentity
tnL1Hop = _TnL1Hop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 5, 2)
)
_TnL1Fiber_ObjectIdentity = ObjectIdentity
tnL1Fiber = _TnL1Fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 5, 3)
)
_TnL1Conduit_ObjectIdentity = ObjectIdentity
tnL1Conduit = _TnL1Conduit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 5, 4)
)
_TnL1Protection_ObjectIdentity = ObjectIdentity
tnL1Protection = _TnL1Protection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6)
)
_TnApsGroupTable_Object = MibTable
tnApsGroupTable = _TnApsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    tnApsGroupTable.setStatus("current")
_TnApsGroupEntry_Object = MibTableRow
tnApsGroupEntry = _TnApsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1)
)
tnApsGroupEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnApsGroupId"),
)
if mibBuilder.loadTexts:
    tnApsGroupEntry.setStatus("current")
_TnApsGroupId_Type = TnApsGroupId
_TnApsGroupId_Object = MibTableColumn
tnApsGroupId = _TnApsGroupId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 1),
    _TnApsGroupId_Type()
)
tnApsGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnApsGroupId.setStatus("current")
_TnApsGroupRowStatus_Type = RowStatus
_TnApsGroupRowStatus_Object = MibTableColumn
tnApsGroupRowStatus = _TnApsGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 2),
    _TnApsGroupRowStatus_Type()
)
tnApsGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupRowStatus.setStatus("current")


class _TnApsGroupDescr_Type(SnmpAdminString):
    """Custom type tnApsGroupDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnApsGroupDescr_Type.__name__ = "SnmpAdminString"
_TnApsGroupDescr_Object = MibTableColumn
tnApsGroupDescr = _TnApsGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 3),
    _TnApsGroupDescr_Type()
)
tnApsGroupDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupDescr.setStatus("current")


class _TnApsGroupMode_Type(TropicProtectionLevel):
    """Custom type tnApsGroupMode based on TropicProtectionLevel"""
    defaultValue = 4


_TnApsGroupMode_Type.__name__ = "TropicProtectionLevel"
_TnApsGroupMode_Object = MibTableColumn
tnApsGroupMode = _TnApsGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 4),
    _TnApsGroupMode_Type()
)
tnApsGroupMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupMode.setStatus("current")


class _TnApsGroupRevert_Type(Integer32):
    """Custom type tnApsGroupRevert based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 1),
          ("revertive", 2))
    )


_TnApsGroupRevert_Type.__name__ = "Integer32"
_TnApsGroupRevert_Object = MibTableColumn
tnApsGroupRevert = _TnApsGroupRevert_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 5),
    _TnApsGroupRevert_Type()
)
tnApsGroupRevert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupRevert.setStatus("current")


class _TnApsGroupDirection_Type(Integer32):
    """Custom type tnApsGroupDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unidirectional", 1),
          ("bidirectional", 2),
          ("uniwoaps", 3))
    )


_TnApsGroupDirection_Type.__name__ = "Integer32"
_TnApsGroupDirection_Object = MibTableColumn
tnApsGroupDirection = _TnApsGroupDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 6),
    _TnApsGroupDirection_Type()
)
tnApsGroupDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupDirection.setStatus("current")


class _TnApsGroupExtraTraffic_Type(AluWdmEnabledDisabled):
    """Custom type tnApsGroupExtraTraffic based on AluWdmEnabledDisabled"""
    defaultValue = 2


_TnApsGroupExtraTraffic_Type.__name__ = "AluWdmEnabledDisabled"
_TnApsGroupExtraTraffic_Object = MibTableColumn
tnApsGroupExtraTraffic = _TnApsGroupExtraTraffic_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 7),
    _TnApsGroupExtraTraffic_Type()
)
tnApsGroupExtraTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupExtraTraffic.setStatus("current")


class _TnApsGroupWaitToRestore_Type(Unsigned32):
    """Custom type tnApsGroupWaitToRestore based on Unsigned32"""
    defaultValue = 5


_TnApsGroupWaitToRestore_Type.__name__ = "Unsigned32"
_TnApsGroupWaitToRestore_Object = MibTableColumn
tnApsGroupWaitToRestore = _TnApsGroupWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 8),
    _TnApsGroupWaitToRestore_Type()
)
tnApsGroupWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupWaitToRestore.setStatus("current")
if mibBuilder.loadTexts:
    tnApsGroupWaitToRestore.setUnits("minutes")
_TnApsGroupK1K2Rcv_Type = ApsK1K2
_TnApsGroupK1K2Rcv_Object = MibTableColumn
tnApsGroupK1K2Rcv = _TnApsGroupK1K2Rcv_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 9),
    _TnApsGroupK1K2Rcv_Type()
)
tnApsGroupK1K2Rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsGroupK1K2Rcv.setStatus("current")
_TnApsGroupK1K2Trans_Type = ApsK1K2
_TnApsGroupK1K2Trans_Object = MibTableColumn
tnApsGroupK1K2Trans = _TnApsGroupK1K2Trans_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 10),
    _TnApsGroupK1K2Trans_Type()
)
tnApsGroupK1K2Trans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsGroupK1K2Trans.setStatus("current")


class _TnApsGroupCurrentStatus_Type(Bits):
    """Custom type tnApsGroupCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("modeMismatch", 0),
          ("channelMismatch", 1),
          ("psbf", 2),
          ("feplf", 3),
          ("extraTraffic", 4))
    )

_TnApsGroupCurrentStatus_Type.__name__ = "Bits"
_TnApsGroupCurrentStatus_Object = MibTableColumn
tnApsGroupCurrentStatus = _TnApsGroupCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 11),
    _TnApsGroupCurrentStatus_Type()
)
tnApsGroupCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsGroupCurrentStatus.setStatus("current")


class _TnApsGroupModeMismatches_Type(Counter32):
    """Custom type tnApsGroupModeMismatches based on Counter32"""
    defaultValue = 0


_TnApsGroupModeMismatches_Type.__name__ = "Counter32"
_TnApsGroupModeMismatches_Object = MibTableColumn
tnApsGroupModeMismatches = _TnApsGroupModeMismatches_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 12),
    _TnApsGroupModeMismatches_Type()
)
tnApsGroupModeMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsGroupModeMismatches.setStatus("current")


class _TnApsGroupChannelMismatches_Type(Counter32):
    """Custom type tnApsGroupChannelMismatches based on Counter32"""
    defaultValue = 0


_TnApsGroupChannelMismatches_Type.__name__ = "Counter32"
_TnApsGroupChannelMismatches_Object = MibTableColumn
tnApsGroupChannelMismatches = _TnApsGroupChannelMismatches_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 13),
    _TnApsGroupChannelMismatches_Type()
)
tnApsGroupChannelMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsGroupChannelMismatches.setStatus("current")


class _TnApsGroupPSBFs_Type(Counter32):
    """Custom type tnApsGroupPSBFs based on Counter32"""
    defaultValue = 0


_TnApsGroupPSBFs_Type.__name__ = "Counter32"
_TnApsGroupPSBFs_Object = MibTableColumn
tnApsGroupPSBFs = _TnApsGroupPSBFs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 14),
    _TnApsGroupPSBFs_Type()
)
tnApsGroupPSBFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsGroupPSBFs.setStatus("current")


class _TnApsGroupFEPLFs_Type(Counter32):
    """Custom type tnApsGroupFEPLFs based on Counter32"""
    defaultValue = 0


_TnApsGroupFEPLFs_Type.__name__ = "Counter32"
_TnApsGroupFEPLFs_Object = MibTableColumn
tnApsGroupFEPLFs = _TnApsGroupFEPLFs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 15),
    _TnApsGroupFEPLFs_Type()
)
tnApsGroupFEPLFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsGroupFEPLFs.setStatus("current")
_TnApsGroupSwitchedIfIndex_Type = InterfaceIndex
_TnApsGroupSwitchedIfIndex_Object = MibTableColumn
tnApsGroupSwitchedIfIndex = _TnApsGroupSwitchedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 16),
    _TnApsGroupSwitchedIfIndex_Type()
)
tnApsGroupSwitchedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsGroupSwitchedIfIndex.setStatus("current")
_TnApsGroupMembers_Type = SnmpAdminString
_TnApsGroupMembers_Object = MibTableColumn
tnApsGroupMembers = _TnApsGroupMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 17),
    _TnApsGroupMembers_Type()
)
tnApsGroupMembers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupMembers.setStatus("current")


class _TnApsGroupSdEnable_Type(TruthValue):
    """Custom type tnApsGroupSdEnable based on TruthValue"""
    defaultValue = 2


_TnApsGroupSdEnable_Type.__name__ = "TruthValue"
_TnApsGroupSdEnable_Object = MibTableColumn
tnApsGroupSdEnable = _TnApsGroupSdEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 18),
    _TnApsGroupSdEnable_Type()
)
tnApsGroupSdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsGroupSdEnable.setStatus("current")


class _TnApsHoldOffTimer_Type(Unsigned32):
    """Custom type tnApsHoldOffTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TnApsHoldOffTimer_Type.__name__ = "Unsigned32"
_TnApsHoldOffTimer_Object = MibTableColumn
tnApsHoldOffTimer = _TnApsHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 1, 1, 19),
    _TnApsHoldOffTimer_Type()
)
tnApsHoldOffTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsHoldOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    tnApsHoldOffTimer.setUnits("milli-seconds")
_TnApsMemberTable_Object = MibTable
tnApsMemberTable = _TnApsMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    tnApsMemberTable.setStatus("current")
_TnApsMemberEntry_Object = MibTableRow
tnApsMemberEntry = _TnApsMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 2, 1)
)
tnApsMemberEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnApsGroupId"),
    (0, "TROPIC-L1SERVICE-MIB", "tnApsMemberIfIndex"),
)
if mibBuilder.loadTexts:
    tnApsMemberEntry.setStatus("current")
_TnApsMemberIfIndex_Type = InterfaceIndex
_TnApsMemberIfIndex_Object = MibTableColumn
tnApsMemberIfIndex = _TnApsMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 2, 1, 1),
    _TnApsMemberIfIndex_Type()
)
tnApsMemberIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnApsMemberIfIndex.setStatus("current")
_TnApsMemberRowStatus_Type = RowStatus
_TnApsMemberRowStatus_Object = MibTableColumn
tnApsMemberRowStatus = _TnApsMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 2, 1, 2),
    _TnApsMemberRowStatus_Type()
)
tnApsMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsMemberRowStatus.setStatus("current")


class _TnApsMemberConfigNumber_Type(Integer32):
    """Custom type tnApsMemberConfigNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_TnApsMemberConfigNumber_Type.__name__ = "Integer32"
_TnApsMemberConfigNumber_Object = MibTableColumn
tnApsMemberConfigNumber = _TnApsMemberConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 2, 1, 3),
    _TnApsMemberConfigNumber_Type()
)
tnApsMemberConfigNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsMemberConfigNumber.setStatus("current")


class _TnApsMemberSwitch_Type(Integer32):
    """Custom type tnApsMemberSwitch based on Integer32"""
    defaultValue = 1

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
        *(("noCmd", 1),
          ("clear", 2),
          ("lockoutOfProtection", 3),
          ("forcedSwitchWorkToProtect", 4),
          ("forcedSwitchProtectToWork", 5),
          ("manualSwitchWorkToProtect", 6),
          ("manualSwitchProtectToWork", 7),
          ("exercise", 8))
    )


_TnApsMemberSwitch_Type.__name__ = "Integer32"
_TnApsMemberSwitch_Object = MibTableColumn
tnApsMemberSwitch = _TnApsMemberSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 2, 1, 5),
    _TnApsMemberSwitch_Type()
)
tnApsMemberSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnApsMemberSwitch.setStatus("current")


class _TnApsMemberCurrentStatus_Type(Bits):
    """Custom type tnApsMemberCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("lockedOut", 0),
          ("sd", 1),
          ("sf", 2),
          ("switched", 3),
          ("txActive", 4),
          ("txStandby", 5),
          ("rxActive", 6),
          ("rxStandby", 7))
    )

_TnApsMemberCurrentStatus_Type.__name__ = "Bits"
_TnApsMemberCurrentStatus_Object = MibTableColumn
tnApsMemberCurrentStatus = _TnApsMemberCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 2, 1, 7),
    _TnApsMemberCurrentStatus_Type()
)
tnApsMemberCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnApsMemberCurrentStatus.setStatus("current")
_TnPackApsGroupTable_Object = MibTable
tnPackApsGroupTable = _TnPackApsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    tnPackApsGroupTable.setStatus("current")
_TnPackApsGroupEntry_Object = MibTableRow
tnPackApsGroupEntry = _TnPackApsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3, 1)
)
tnPackApsGroupEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnPackApsGroupID"),
)
if mibBuilder.loadTexts:
    tnPackApsGroupEntry.setStatus("current")
_TnPackApsGroupID_Type = Unsigned32
_TnPackApsGroupID_Object = MibTableColumn
tnPackApsGroupID = _TnPackApsGroupID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3, 1, 1),
    _TnPackApsGroupID_Type()
)
tnPackApsGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPackApsGroupID.setStatus("current")
_TnPackApsGroupRowStatus_Type = RowStatus
_TnPackApsGroupRowStatus_Object = MibTableColumn
tnPackApsGroupRowStatus = _TnPackApsGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3, 1, 2),
    _TnPackApsGroupRowStatus_Type()
)
tnPackApsGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPackApsGroupRowStatus.setStatus("current")
_TnPackApsGroupWorkIfIndex_Type = Integer32
_TnPackApsGroupWorkIfIndex_Object = MibTableColumn
tnPackApsGroupWorkIfIndex = _TnPackApsGroupWorkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3, 1, 3),
    _TnPackApsGroupWorkIfIndex_Type()
)
tnPackApsGroupWorkIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPackApsGroupWorkIfIndex.setStatus("current")
_TnPackApsGroupProtIfIndex_Type = Integer32
_TnPackApsGroupProtIfIndex_Object = MibTableColumn
tnPackApsGroupProtIfIndex = _TnPackApsGroupProtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3, 1, 4),
    _TnPackApsGroupProtIfIndex_Type()
)
tnPackApsGroupProtIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPackApsGroupProtIfIndex.setStatus("current")


class _TnPackApsGroupDescr_Type(SnmpAdminString):
    """Custom type tnPackApsGroupDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TnPackApsGroupDescr_Type.__name__ = "SnmpAdminString"
_TnPackApsGroupDescr_Object = MibTableColumn
tnPackApsGroupDescr = _TnPackApsGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3, 1, 5),
    _TnPackApsGroupDescr_Type()
)
tnPackApsGroupDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPackApsGroupDescr.setStatus("current")


class _TnPackApsGroupRevert_Type(Integer32):
    """Custom type tnPackApsGroupRevert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 1),
          ("revertive", 2))
    )


_TnPackApsGroupRevert_Type.__name__ = "Integer32"
_TnPackApsGroupRevert_Object = MibTableColumn
tnPackApsGroupRevert = _TnPackApsGroupRevert_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3, 1, 6),
    _TnPackApsGroupRevert_Type()
)
tnPackApsGroupRevert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPackApsGroupRevert.setStatus("current")


class _TnPackApsGroupDirection_Type(Integer32):
    """Custom type tnPackApsGroupDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unidirectional", 1),
          ("bidirectional", 2))
    )


_TnPackApsGroupDirection_Type.__name__ = "Integer32"
_TnPackApsGroupDirection_Object = MibTableColumn
tnPackApsGroupDirection = _TnPackApsGroupDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3, 1, 7),
    _TnPackApsGroupDirection_Type()
)
tnPackApsGroupDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPackApsGroupDirection.setStatus("current")


class _TnPackApsGroupWaitToRestore_Type(Unsigned32):
    """Custom type tnPackApsGroupWaitToRestore based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TnPackApsGroupWaitToRestore_Type.__name__ = "Unsigned32"
_TnPackApsGroupWaitToRestore_Object = MibTableColumn
tnPackApsGroupWaitToRestore = _TnPackApsGroupWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3, 1, 8),
    _TnPackApsGroupWaitToRestore_Type()
)
tnPackApsGroupWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPackApsGroupWaitToRestore.setStatus("current")


class _TnPackApsGroupHoldOffTimer_Type(Unsigned32):
    """Custom type tnPackApsGroupHoldOffTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TnPackApsGroupHoldOffTimer_Type.__name__ = "Unsigned32"
_TnPackApsGroupHoldOffTimer_Object = MibTableColumn
tnPackApsGroupHoldOffTimer = _TnPackApsGroupHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3, 1, 9),
    _TnPackApsGroupHoldOffTimer_Type()
)
tnPackApsGroupHoldOffTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPackApsGroupHoldOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    tnPackApsGroupHoldOffTimer.setUnits("milli-seconds")


class _TnPackApsGroupSwitchCmd_Type(Integer32):
    """Custom type tnPackApsGroupSwitchCmd based on Integer32"""
    defaultValue = 1

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
        *(("noCmd", 1),
          ("clear", 2),
          ("lockoutOfProtection", 3),
          ("forcedSwitchWorkToProtect", 4),
          ("forcedSwitchProtectToWork", 5),
          ("manualSwitchWorkToProtect", 6),
          ("manualSwitchProtectToWork", 7))
    )


_TnPackApsGroupSwitchCmd_Type.__name__ = "Integer32"
_TnPackApsGroupSwitchCmd_Object = MibTableColumn
tnPackApsGroupSwitchCmd = _TnPackApsGroupSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3, 1, 10),
    _TnPackApsGroupSwitchCmd_Type()
)
tnPackApsGroupSwitchCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPackApsGroupSwitchCmd.setStatus("current")


class _TnPackApsGroupActSide_Type(Integer32):
    """Custom type tnPackApsGroupActSide based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("working", 1),
          ("protection", 2))
    )


_TnPackApsGroupActSide_Type.__name__ = "Integer32"
_TnPackApsGroupActSide_Object = MibTableColumn
tnPackApsGroupActSide = _TnPackApsGroupActSide_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3, 1, 11),
    _TnPackApsGroupActSide_Type()
)
tnPackApsGroupActSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPackApsGroupActSide.setStatus("current")


class _TnPackApsGroupCurrentStatus_Type(Integer32):
    """Custom type tnPackApsGroupCurrentStatus based on Integer32"""
    defaultValue = 8

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
        *(("lockoutNe", 1),
          ("frcdNe", 2),
          ("sfNe", 3),
          ("sdNe", 4),
          ("manNe", 5),
          ("wtrNe", 6),
          ("dnr", 7),
          ("nr", 8),
          ("lockoutFe", 9),
          ("frcdFe", 10),
          ("sfFe", 11),
          ("sdFe", 12),
          ("manFe", 13),
          ("wtrFe", 14),
          ("exerNe", 15),
          ("exerFe", 16))
    )


_TnPackApsGroupCurrentStatus_Type.__name__ = "Integer32"
_TnPackApsGroupCurrentStatus_Object = MibTableColumn
tnPackApsGroupCurrentStatus = _TnPackApsGroupCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3, 1, 12),
    _TnPackApsGroupCurrentStatus_Type()
)
tnPackApsGroupCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPackApsGroupCurrentStatus.setStatus("current")


class _TnPackApsGroupWorkStatus_Type(Integer32):
    """Custom type tnPackApsGroupWorkStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sf", 1),
          ("sd", 2),
          ("none", 3))
    )


_TnPackApsGroupWorkStatus_Type.__name__ = "Integer32"
_TnPackApsGroupWorkStatus_Object = MibTableColumn
tnPackApsGroupWorkStatus = _TnPackApsGroupWorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3, 1, 13),
    _TnPackApsGroupWorkStatus_Type()
)
tnPackApsGroupWorkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPackApsGroupWorkStatus.setStatus("current")


class _TnPackApsGroupProtStatus_Type(Integer32):
    """Custom type tnPackApsGroupProtStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sf", 1),
          ("sd", 2),
          ("none", 3))
    )


_TnPackApsGroupProtStatus_Type.__name__ = "Integer32"
_TnPackApsGroupProtStatus_Object = MibTableColumn
tnPackApsGroupProtStatus = _TnPackApsGroupProtStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3, 1, 14),
    _TnPackApsGroupProtStatus_Type()
)
tnPackApsGroupProtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPackApsGroupProtStatus.setStatus("current")


class _TnPackApsGroupPortFailEnable_Type(TruthValue):
    """Custom type tnPackApsGroupPortFailEnable based on TruthValue"""
    defaultValue = 2


_TnPackApsGroupPortFailEnable_Type.__name__ = "TruthValue"
_TnPackApsGroupPortFailEnable_Object = MibTableColumn
tnPackApsGroupPortFailEnable = _TnPackApsGroupPortFailEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 6, 3, 1, 15),
    _TnPackApsGroupPortFailEnable_Type()
)
tnPackApsGroupPortFailEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPackApsGroupPortFailEnable.setStatus("current")
_TnIpTunnel_ObjectIdentity = ObjectIdentity
tnIpTunnel = _TnIpTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 7)
)
_TnControlNetworkMap_ObjectIdentity = ObjectIdentity
tnControlNetworkMap = _TnControlNetworkMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 8)
)
_TnControlNetworkMapTable_Object = MibTable
tnControlNetworkMapTable = _TnControlNetworkMapTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    tnControlNetworkMapTable.setStatus("current")
_TnControlNetworkMapEntry_Object = MibTableRow
tnControlNetworkMapEntry = _TnControlNetworkMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 8, 1, 1)
)
tnControlNetworkMapEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnCNMapTableIndex"),
)
if mibBuilder.loadTexts:
    tnControlNetworkMapEntry.setStatus("current")
_TnCNMapTableIndex_Type = Unsigned32
_TnCNMapTableIndex_Object = MibTableColumn
tnCNMapTableIndex = _TnCNMapTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 8, 1, 1, 1),
    _TnCNMapTableIndex_Type()
)
tnCNMapTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCNMapTableIndex.setStatus("current")
_TnCNMapIpAddress_Type = IpAddress
_TnCNMapIpAddress_Object = MibTableColumn
tnCNMapIpAddress = _TnCNMapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 8, 1, 1, 2),
    _TnCNMapIpAddress_Type()
)
tnCNMapIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNMapIpAddress.setStatus("current")


class _TnCNMapNeName_Type(OctetString):
    """Custom type tnCNMapNeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 81),
    )


_TnCNMapNeName_Type.__name__ = "OctetString"
_TnCNMapNeName_Object = MibTableColumn
tnCNMapNeName = _TnCNMapNeName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 8, 1, 1, 3),
    _TnCNMapNeName_Type()
)
tnCNMapNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNMapNeName.setStatus("current")


class _TnCNMapSoftwareRelease_Type(OctetString):
    """Custom type tnCNMapSoftwareRelease based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 81),
    )


_TnCNMapSoftwareRelease_Type.__name__ = "OctetString"
_TnCNMapSoftwareRelease_Object = MibTableColumn
tnCNMapSoftwareRelease = _TnCNMapSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 8, 1, 1, 4),
    _TnCNMapSoftwareRelease_Type()
)
tnCNMapSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNMapSoftwareRelease.setStatus("current")


class _TnCNMapIpv6InetAddress_Type(SnmpAdminString):
    """Custom type tnCNMapIpv6InetAddress based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnCNMapIpv6InetAddress_Type.__name__ = "SnmpAdminString"
_TnCNMapIpv6InetAddress_Object = MibTableColumn
tnCNMapIpv6InetAddress = _TnCNMapIpv6InetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 8, 1, 1, 5),
    _TnCNMapIpv6InetAddress_Type()
)
tnCNMapIpv6InetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNMapIpv6InetAddress.setStatus("current")


class _TnCNMapIpv4Address_Type(IpAddress):
    """Custom type tnCNMapIpv4Address based on IpAddress"""
    defaultHexValue = "00000000"


_TnCNMapIpv4Address_Type.__name__ = "IpAddress"
_TnCNMapIpv4Address_Object = MibTableColumn
tnCNMapIpv4Address = _TnCNMapIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 8, 1, 1, 6),
    _TnCNMapIpv4Address_Type()
)
tnCNMapIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCNMapIpv4Address.setStatus("current")
_TnNetworkInterface_ObjectIdentity = ObjectIdentity
tnNetworkInterface = _TnNetworkInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9)
)
_TnNetIfTable_Object = MibTable
tnNetIfTable = _TnNetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    tnNetIfTable.setStatus("current")
_TnNetIfEntry_Object = MibTableRow
tnNetIfEntry = _TnNetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1)
)
tnNetIfEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnNetIfIndex"),
)
if mibBuilder.loadTexts:
    tnNetIfEntry.setStatus("current")


class _TnNetIfIndex_Type(Unsigned32):
    """Custom type tnNetIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_TnNetIfIndex_Type.__name__ = "Unsigned32"
_TnNetIfIndex_Object = MibTableColumn
tnNetIfIndex = _TnNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 1),
    _TnNetIfIndex_Type()
)
tnNetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNetIfIndex.setStatus("current")
_TnNetIfTypeOfOperation_Type = AluWdmTypeOfNetIfOperation
_TnNetIfTypeOfOperation_Object = MibTableColumn
tnNetIfTypeOfOperation = _TnNetIfTypeOfOperation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 2),
    _TnNetIfTypeOfOperation_Type()
)
tnNetIfTypeOfOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfTypeOfOperation.setStatus("current")


class _TnNetIfStatus_Type(Integer32):
    """Custom type tnNetIfStatus based on Integer32"""
    defaultValue = 2

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


_TnNetIfStatus_Type.__name__ = "Integer32"
_TnNetIfStatus_Object = MibTableColumn
tnNetIfStatus = _TnNetIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 3),
    _TnNetIfStatus_Type()
)
tnNetIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfStatus.setStatus("current")


class _TnNetIfPacketType_Type(Integer32):
    """Custom type tnNetIfPacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("std", 1),
          ("non-std", 2))
    )


_TnNetIfPacketType_Type.__name__ = "Integer32"
_TnNetIfPacketType_Object = MibTableColumn
tnNetIfPacketType = _TnNetIfPacketType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 4),
    _TnNetIfPacketType_Type()
)
tnNetIfPacketType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfPacketType.setStatus("current")


class _TnNetIfMtu_Type(Integer32):
    """Custom type tnNetIfMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 1500),
    )


_TnNetIfMtu_Type.__name__ = "Integer32"
_TnNetIfMtu_Object = MibTableColumn
tnNetIfMtu = _TnNetIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 5),
    _TnNetIfMtu_Type()
)
tnNetIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfMtu.setStatus("current")


class _TnNetIfHelloInterval_Type(Unsigned32):
    """Custom type tnNetIfHelloInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnNetIfHelloInterval_Type.__name__ = "Unsigned32"
_TnNetIfHelloInterval_Object = MibTableColumn
tnNetIfHelloInterval = _TnNetIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 6),
    _TnNetIfHelloInterval_Type()
)
tnNetIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnNetIfHelloInterval.setUnits("seconds")


class _TnNetIfRtrDeadInterval_Type(Unsigned32):
    """Custom type tnNetIfRtrDeadInterval based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnNetIfRtrDeadInterval_Type.__name__ = "Unsigned32"
_TnNetIfRtrDeadInterval_Object = MibTableColumn
tnNetIfRtrDeadInterval = _TnNetIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 7),
    _TnNetIfRtrDeadInterval_Type()
)
tnNetIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnNetIfRtrDeadInterval.setUnits("seconds")


class _TnNetIfMetric_Type(Unsigned32):
    """Custom type tnNetIfMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnNetIfMetric_Type.__name__ = "Unsigned32"
_TnNetIfMetric_Object = MibTableColumn
tnNetIfMetric = _TnNetIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 8),
    _TnNetIfMetric_Type()
)
tnNetIfMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfMetric.setStatus("current")


class _TnNetIfOspfAuthentType_Type(Integer32):
    """Custom type tnNetIfOspfAuthentType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("simple", 2),
          ("md5", 3))
    )


_TnNetIfOspfAuthentType_Type.__name__ = "Integer32"
_TnNetIfOspfAuthentType_Object = MibTableColumn
tnNetIfOspfAuthentType = _TnNetIfOspfAuthentType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 9),
    _TnNetIfOspfAuthentType_Type()
)
tnNetIfOspfAuthentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfOspfAuthentType.setStatus("current")


class _TnNetIfOspfAuthKey_Type(OctetString):
    """Custom type tnNetIfOspfAuthKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnNetIfOspfAuthKey_Type.__name__ = "OctetString"
_TnNetIfOspfAuthKey_Object = MibTableColumn
tnNetIfOspfAuthKey = _TnNetIfOspfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 10),
    _TnNetIfOspfAuthKey_Type()
)
tnNetIfOspfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfOspfAuthKey.setStatus("current")


class _TnNetIfOspfAuthKeyId_Type(Unsigned32):
    """Custom type tnNetIfOspfAuthKeyId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnNetIfOspfAuthKeyId_Type.__name__ = "Unsigned32"
_TnNetIfOspfAuthKeyId_Object = MibTableColumn
tnNetIfOspfAuthKeyId = _TnNetIfOspfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 11),
    _TnNetIfOspfAuthKeyId_Type()
)
tnNetIfOspfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfOspfAuthKeyId.setStatus("current")


class _TnNetIfCnLinkAdjState_Type(TropicOspfAdjacencyStateType):
    """Custom type tnNetIfCnLinkAdjState based on TropicOspfAdjacencyStateType"""
    defaultValue = 1


_TnNetIfCnLinkAdjState_Type.__name__ = "TropicOspfAdjacencyStateType"
_TnNetIfCnLinkAdjState_Object = MibTableColumn
tnNetIfCnLinkAdjState = _TnNetIfCnLinkAdjState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 12),
    _TnNetIfCnLinkAdjState_Type()
)
tnNetIfCnLinkAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetIfCnLinkAdjState.setStatus("current")


class _TnNetIfMtuNeg_Type(Integer32):
    """Custom type tnNetIfMtuNeg based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1500),
    )


_TnNetIfMtuNeg_Type.__name__ = "Integer32"
_TnNetIfMtuNeg_Object = MibTableColumn
tnNetIfMtuNeg = _TnNetIfMtuNeg_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 13),
    _TnNetIfMtuNeg_Type()
)
tnNetIfMtuNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetIfMtuNeg.setStatus("current")


class _TnNetIfOSPFAreaNumberId_Type(Integer32):
    """Custom type tnNetIfOSPFAreaNumberId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TnNetIfOSPFAreaNumberId_Type.__name__ = "Integer32"
_TnNetIfOSPFAreaNumberId_Object = MibTableColumn
tnNetIfOSPFAreaNumberId = _TnNetIfOSPFAreaNumberId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 14),
    _TnNetIfOSPFAreaNumberId_Type()
)
tnNetIfOSPFAreaNumberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfOSPFAreaNumberId.setStatus("current")


class _TnNetIfOspfRetransint_Type(Unsigned32):
    """Custom type tnNetIfOspfRetransint based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnNetIfOspfRetransint_Type.__name__ = "Unsigned32"
_TnNetIfOspfRetransint_Object = MibTableColumn
tnNetIfOspfRetransint = _TnNetIfOspfRetransint_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 15),
    _TnNetIfOspfRetransint_Type()
)
tnNetIfOspfRetransint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfOspfRetransint.setStatus("current")


class _TnNetIfOspfv3AdjStateId_Type(TropicOspfAdjacencyStateType):
    """Custom type tnNetIfOspfv3AdjStateId based on TropicOspfAdjacencyStateType"""
    defaultValue = 1


_TnNetIfOspfv3AdjStateId_Type.__name__ = "TropicOspfAdjacencyStateType"
_TnNetIfOspfv3AdjStateId_Object = MibTableColumn
tnNetIfOspfv3AdjStateId = _TnNetIfOspfv3AdjStateId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 16),
    _TnNetIfOspfv3AdjStateId_Type()
)
tnNetIfOspfv3AdjStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetIfOspfv3AdjStateId.setStatus("current")


class _TnNetIfOspfNeighborRouterIp_Type(IpAddress):
    """Custom type tnNetIfOspfNeighborRouterIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnNetIfOspfNeighborRouterIp_Type.__name__ = "IpAddress"
_TnNetIfOspfNeighborRouterIp_Object = MibTableColumn
tnNetIfOspfNeighborRouterIp = _TnNetIfOspfNeighborRouterIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 17),
    _TnNetIfOspfNeighborRouterIp_Type()
)
tnNetIfOspfNeighborRouterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetIfOspfNeighborRouterIp.setStatus("current")


class _TnNetIfOspfv3NeighborRouterIp_Type(IpAddress):
    """Custom type tnNetIfOspfv3NeighborRouterIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnNetIfOspfv3NeighborRouterIp_Type.__name__ = "IpAddress"
_TnNetIfOspfv3NeighborRouterIp_Object = MibTableColumn
tnNetIfOspfv3NeighborRouterIp = _TnNetIfOspfv3NeighborRouterIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 18),
    _TnNetIfOspfv3NeighborRouterIp_Type()
)
tnNetIfOspfv3NeighborRouterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetIfOspfv3NeighborRouterIp.setStatus("current")


class _TnNetIfOspfNeighborIp_Type(IpAddress):
    """Custom type tnNetIfOspfNeighborIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnNetIfOspfNeighborIp_Type.__name__ = "IpAddress"
_TnNetIfOspfNeighborIp_Object = MibTableColumn
tnNetIfOspfNeighborIp = _TnNetIfOspfNeighborIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 19),
    _TnNetIfOspfNeighborIp_Type()
)
tnNetIfOspfNeighborIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetIfOspfNeighborIp.setStatus("current")


class _TnNetIfOspfv3NeighborInetAddress_Type(InetAddress):
    """Custom type tnNetIfOspfv3NeighborInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnNetIfOspfv3NeighborInetAddress_Type.__name__ = "InetAddress"
_TnNetIfOspfv3NeighborInetAddress_Object = MibTableColumn
tnNetIfOspfv3NeighborInetAddress = _TnNetIfOspfv3NeighborInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 20),
    _TnNetIfOspfv3NeighborInetAddress_Type()
)
tnNetIfOspfv3NeighborInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetIfOspfv3NeighborInetAddress.setStatus("current")


class _TnNetIfIPv6LinkLocalInetAddress_Type(InetAddress):
    """Custom type tnNetIfIPv6LinkLocalInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnNetIfIPv6LinkLocalInetAddress_Type.__name__ = "InetAddress"
_TnNetIfIPv6LinkLocalInetAddress_Object = MibTableColumn
tnNetIfIPv6LinkLocalInetAddress = _TnNetIfIPv6LinkLocalInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 21),
    _TnNetIfIPv6LinkLocalInetAddress_Type()
)
tnNetIfIPv6LinkLocalInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNetIfIPv6LinkLocalInetAddress.setStatus("current")


class _TnNetIfLcpEchoInterval_Type(Unsigned32):
    """Custom type tnNetIfLcpEchoInterval based on Unsigned32"""
    defaultValue = 3


_TnNetIfLcpEchoInterval_Type.__name__ = "Unsigned32"
_TnNetIfLcpEchoInterval_Object = MibTableColumn
tnNetIfLcpEchoInterval = _TnNetIfLcpEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 22),
    _TnNetIfLcpEchoInterval_Type()
)
tnNetIfLcpEchoInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfLcpEchoInterval.setStatus("current")


class _TnNetIfLcpEchoFailure_Type(Unsigned32):
    """Custom type tnNetIfLcpEchoFailure based on Unsigned32"""
    defaultValue = 20


_TnNetIfLcpEchoFailure_Type.__name__ = "Unsigned32"
_TnNetIfLcpEchoFailure_Object = MibTableColumn
tnNetIfLcpEchoFailure = _TnNetIfLcpEchoFailure_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 23),
    _TnNetIfLcpEchoFailure_Type()
)
tnNetIfLcpEchoFailure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfLcpEchoFailure.setStatus("current")


class _TnNetIfOspfStatus_Type(Integer32):
    """Custom type tnNetIfOspfStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("redistribute", 3))
    )


_TnNetIfOspfStatus_Type.__name__ = "Integer32"
_TnNetIfOspfStatus_Object = MibTableColumn
tnNetIfOspfStatus = _TnNetIfOspfStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 24),
    _TnNetIfOspfStatus_Type()
)
tnNetIfOspfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfOspfStatus.setStatus("current")


class _TnNetIfOspfv3AreaNumberId_Type(Integer32):
    """Custom type tnNetIfOspfv3AreaNumberId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TnNetIfOspfv3AreaNumberId_Type.__name__ = "Integer32"
_TnNetIfOspfv3AreaNumberId_Object = MibTableColumn
tnNetIfOspfv3AreaNumberId = _TnNetIfOspfv3AreaNumberId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 25),
    _TnNetIfOspfv3AreaNumberId_Type()
)
tnNetIfOspfv3AreaNumberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfOspfv3AreaNumberId.setStatus("current")


class _TnNetIfOspfv3HelloInterval_Type(Unsigned32):
    """Custom type tnNetIfOspfv3HelloInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnNetIfOspfv3HelloInterval_Type.__name__ = "Unsigned32"
_TnNetIfOspfv3HelloInterval_Object = MibTableColumn
tnNetIfOspfv3HelloInterval = _TnNetIfOspfv3HelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 26),
    _TnNetIfOspfv3HelloInterval_Type()
)
tnNetIfOspfv3HelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfOspfv3HelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnNetIfOspfv3HelloInterval.setUnits("seconds")


class _TnNetIfOspfv3Metric_Type(Unsigned32):
    """Custom type tnNetIfOspfv3Metric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnNetIfOspfv3Metric_Type.__name__ = "Unsigned32"
_TnNetIfOspfv3Metric_Object = MibTableColumn
tnNetIfOspfv3Metric = _TnNetIfOspfv3Metric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 27),
    _TnNetIfOspfv3Metric_Type()
)
tnNetIfOspfv3Metric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfOspfv3Metric.setStatus("current")


class _TnNetIfOspfv3Retransint_Type(Unsigned32):
    """Custom type tnNetIfOspfv3Retransint based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnNetIfOspfv3Retransint_Type.__name__ = "Unsigned32"
_TnNetIfOspfv3Retransint_Object = MibTableColumn
tnNetIfOspfv3Retransint = _TnNetIfOspfv3Retransint_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 28),
    _TnNetIfOspfv3Retransint_Type()
)
tnNetIfOspfv3Retransint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfOspfv3Retransint.setStatus("current")


class _TnNetIfOspfv3RtrDeadInterval_Type(Unsigned32):
    """Custom type tnNetIfOspfv3RtrDeadInterval based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnNetIfOspfv3RtrDeadInterval_Type.__name__ = "Unsigned32"
_TnNetIfOspfv3RtrDeadInterval_Object = MibTableColumn
tnNetIfOspfv3RtrDeadInterval = _TnNetIfOspfv3RtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 29),
    _TnNetIfOspfv3RtrDeadInterval_Type()
)
tnNetIfOspfv3RtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfOspfv3RtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnNetIfOspfv3RtrDeadInterval.setUnits("seconds")


class _TnNetIfOspfv3ConfigRtrPriority_Type(Unsigned32):
    """Custom type tnNetIfOspfv3ConfigRtrPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnNetIfOspfv3ConfigRtrPriority_Type.__name__ = "Unsigned32"
_TnNetIfOspfv3ConfigRtrPriority_Object = MibTableColumn
tnNetIfOspfv3ConfigRtrPriority = _TnNetIfOspfv3ConfigRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 30),
    _TnNetIfOspfv3ConfigRtrPriority_Type()
)
tnNetIfOspfv3ConfigRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfOspfv3ConfigRtrPriority.setStatus("current")


class _TnNetIfOspfv3Status_Type(Integer32):
    """Custom type tnNetIfOspfv3Status based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("redistribute", 3))
    )


_TnNetIfOspfv3Status_Type.__name__ = "Integer32"
_TnNetIfOspfv3Status_Object = MibTableColumn
tnNetIfOspfv3Status = _TnNetIfOspfv3Status_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 1, 1, 31),
    _TnNetIfOspfv3Status_Type()
)
tnNetIfOspfv3Status.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfOspfv3Status.setStatus("current")
_TnNetIfFacilityTable_Object = MibTable
tnNetIfFacilityTable = _TnNetIfFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    tnNetIfFacilityTable.setStatus("current")
_TnNetIfFacilityEntry_Object = MibTableRow
tnNetIfFacilityEntry = _TnNetIfFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 2, 1)
)
tnNetIfFacilityEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnNetIfIndex"),
    (0, "TROPIC-L1SERVICE-MIB", "tnNetIfFacilityIfIndex"),
    (0, "TROPIC-L1SERVICE-MIB", "tnNetIfFacilityIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnNetIfFacilityEntry.setStatus("current")
_TnNetIfFacilityIfIndex_Type = Unsigned32
_TnNetIfFacilityIfIndex_Object = MibTableColumn
tnNetIfFacilityIfIndex = _TnNetIfFacilityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 2, 1, 1),
    _TnNetIfFacilityIfIndex_Type()
)
tnNetIfFacilityIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNetIfFacilityIfIndex.setStatus("current")
_TnNetIfFacilityIfIndexLo_Type = Unsigned32
_TnNetIfFacilityIfIndexLo_Object = MibTableColumn
tnNetIfFacilityIfIndexLo = _TnNetIfFacilityIfIndexLo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 2, 1, 2),
    _TnNetIfFacilityIfIndexLo_Type()
)
tnNetIfFacilityIfIndexLo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNetIfFacilityIfIndexLo.setStatus("current")
_TnNetIfFacilityTypeOfOperation_Type = AluWdmTypeOfNetIfOperation
_TnNetIfFacilityTypeOfOperation_Object = MibTableColumn
tnNetIfFacilityTypeOfOperation = _TnNetIfFacilityTypeOfOperation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 2, 1, 3),
    _TnNetIfFacilityTypeOfOperation_Type()
)
tnNetIfFacilityTypeOfOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfFacilityTypeOfOperation.setStatus("current")


class _TnNetIfFacilityEccChanType_Type(Integer32):
    """Custom type tnNetIfFacilityEccChanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gcc0", 1),
          ("gcc1", 2),
          ("gcc2", 3))
    )


_TnNetIfFacilityEccChanType_Type.__name__ = "Integer32"
_TnNetIfFacilityEccChanType_Object = MibTableColumn
tnNetIfFacilityEccChanType = _TnNetIfFacilityEccChanType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 9, 2, 1, 4),
    _TnNetIfFacilityEccChanType_Type()
)
tnNetIfFacilityEccChanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNetIfFacilityEccChanType.setStatus("current")
_TnStaticRoute_ObjectIdentity = ObjectIdentity
tnStaticRoute = _TnStaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 10)
)
_TnStaticRouteTable_Object = MibTable
tnStaticRouteTable = _TnStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    tnStaticRouteTable.setStatus("current")
_TnStaticRouteEntry_Object = MibTableRow
tnStaticRouteEntry = _TnStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 10, 1, 1)
)
tnStaticRouteEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnStaticRouteIdentifier"),
    (0, "TROPIC-L1SERVICE-MIB", "tnStaticRouteDestInetAddressType"),
    (0, "TROPIC-L1SERVICE-MIB", "tnStaticRouteDestInetAddress"),
    (0, "TROPIC-L1SERVICE-MIB", "tnStaticRouteMaskPrefix"),
    (0, "TROPIC-L1SERVICE-MIB", "tnStaticRouteTos"),
    (0, "TROPIC-L1SERVICE-MIB", "tnStaticRouteNextHopType"),
    (0, "TROPIC-L1SERVICE-MIB", "tnStaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    tnStaticRouteEntry.setStatus("current")
_TnStaticRouteDestInetAddressType_Type = InetAddressType
_TnStaticRouteDestInetAddressType_Object = MibTableColumn
tnStaticRouteDestInetAddressType = _TnStaticRouteDestInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 10, 1, 1, 1),
    _TnStaticRouteDestInetAddressType_Type()
)
tnStaticRouteDestInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStaticRouteDestInetAddressType.setStatus("current")
_TnStaticRouteDestInetAddress_Type = InetAddress
_TnStaticRouteDestInetAddress_Object = MibTableColumn
tnStaticRouteDestInetAddress = _TnStaticRouteDestInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 10, 1, 1, 2),
    _TnStaticRouteDestInetAddress_Type()
)
tnStaticRouteDestInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStaticRouteDestInetAddress.setStatus("current")
_TnStaticRouteMaskPrefix_Type = Unsigned32
_TnStaticRouteMaskPrefix_Object = MibTableColumn
tnStaticRouteMaskPrefix = _TnStaticRouteMaskPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 10, 1, 1, 3),
    _TnStaticRouteMaskPrefix_Type()
)
tnStaticRouteMaskPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStaticRouteMaskPrefix.setStatus("current")
_TnStaticRouteTos_Type = Integer32
_TnStaticRouteTos_Object = MibTableColumn
tnStaticRouteTos = _TnStaticRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 10, 1, 1, 4),
    _TnStaticRouteTos_Type()
)
tnStaticRouteTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStaticRouteTos.setStatus("current")


class _TnStaticRouteNextHopType_Type(Integer32):
    """Custom type tnStaticRouteNextHopType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("netIf", 3),
          ("ifIndex", 4))
    )


_TnStaticRouteNextHopType_Type.__name__ = "Integer32"
_TnStaticRouteNextHopType_Object = MibTableColumn
tnStaticRouteNextHopType = _TnStaticRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 10, 1, 1, 5),
    _TnStaticRouteNextHopType_Type()
)
tnStaticRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStaticRouteNextHopType.setStatus("current")
_TnStaticRouteNextHop_Type = OctetString
_TnStaticRouteNextHop_Object = MibTableColumn
tnStaticRouteNextHop = _TnStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 10, 1, 1, 6),
    _TnStaticRouteNextHop_Type()
)
tnStaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStaticRouteNextHop.setStatus("current")


class _TnStaticRouteMetric_Type(Integer32):
    """Custom type tnStaticRouteMetric based on Integer32"""
    defaultValue = -1


_TnStaticRouteMetric_Type.__name__ = "Integer32"
_TnStaticRouteMetric_Object = MibTableColumn
tnStaticRouteMetric = _TnStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 10, 1, 1, 7),
    _TnStaticRouteMetric_Type()
)
tnStaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStaticRouteMetric.setStatus("current")


class _TnStaticRouteWithRedistribution_Type(TruthValue):
    """Custom type tnStaticRouteWithRedistribution based on TruthValue"""
    defaultValue = 2


_TnStaticRouteWithRedistribution_Type.__name__ = "TruthValue"
_TnStaticRouteWithRedistribution_Object = MibTableColumn
tnStaticRouteWithRedistribution = _TnStaticRouteWithRedistribution_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 10, 1, 1, 8),
    _TnStaticRouteWithRedistribution_Type()
)
tnStaticRouteWithRedistribution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStaticRouteWithRedistribution.setStatus("current")
_TnStaticRouteRowStatus_Type = RowStatus
_TnStaticRouteRowStatus_Object = MibTableColumn
tnStaticRouteRowStatus = _TnStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 10, 1, 1, 9),
    _TnStaticRouteRowStatus_Type()
)
tnStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStaticRouteRowStatus.setStatus("current")
_TnStaticRouteIdentifier_Type = Integer32
_TnStaticRouteIdentifier_Object = MibTableColumn
tnStaticRouteIdentifier = _TnStaticRouteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 10, 1, 1, 10),
    _TnStaticRouteIdentifier_Type()
)
tnStaticRouteIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStaticRouteIdentifier.setStatus("current")
_TnStaticRouteWithBgpDistribution_Type = TruthValue
_TnStaticRouteWithBgpDistribution_Object = MibTableColumn
tnStaticRouteWithBgpDistribution = _TnStaticRouteWithBgpDistribution_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 10, 1, 1, 11),
    _TnStaticRouteWithBgpDistribution_Type()
)
tnStaticRouteWithBgpDistribution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnStaticRouteWithBgpDistribution.setStatus("current")
_TnEthernetInterface_ObjectIdentity = ObjectIdentity
tnEthernetInterface = _TnEthernetInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11)
)
_TnEthIfTable_Object = MibTable
tnEthIfTable = _TnEthIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1)
)
if mibBuilder.loadTexts:
    tnEthIfTable.setStatus("current")
_TnEthIfEntry_Object = MibTableRow
tnEthIfEntry = _TnEthIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1)
)
tnEthIfEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnEthIfIndex"),
)
if mibBuilder.loadTexts:
    tnEthIfEntry.setStatus("current")


class _TnEthIfIndex_Type(Unsigned32):
    """Custom type tnEthIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TnEthIfIndex_Type.__name__ = "Unsigned32"
_TnEthIfIndex_Object = MibTableColumn
tnEthIfIndex = _TnEthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 1),
    _TnEthIfIndex_Type()
)
tnEthIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthIfIndex.setStatus("current")
_TnEthIfTypeOfOperation_Type = AluWdmTypeOfNetIfOperation
_TnEthIfTypeOfOperation_Object = MibTableColumn
tnEthIfTypeOfOperation = _TnEthIfTypeOfOperation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 2),
    _TnEthIfTypeOfOperation_Type()
)
tnEthIfTypeOfOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfTypeOfOperation.setStatus("current")


class _TnEthIfStatus_Type(Integer32):
    """Custom type tnEthIfStatus based on Integer32"""
    defaultValue = 2

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


_TnEthIfStatus_Type.__name__ = "Integer32"
_TnEthIfStatus_Object = MibTableColumn
tnEthIfStatus = _TnEthIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 3),
    _TnEthIfStatus_Type()
)
tnEthIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfStatus.setStatus("current")


class _TnEthIfHelloInterval_Type(Unsigned32):
    """Custom type tnEthIfHelloInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnEthIfHelloInterval_Type.__name__ = "Unsigned32"
_TnEthIfHelloInterval_Object = MibTableColumn
tnEthIfHelloInterval = _TnEthIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 4),
    _TnEthIfHelloInterval_Type()
)
tnEthIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnEthIfHelloInterval.setUnits("seconds")


class _TnEthIfRtrDeadInterval_Type(Unsigned32):
    """Custom type tnEthIfRtrDeadInterval based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnEthIfRtrDeadInterval_Type.__name__ = "Unsigned32"
_TnEthIfRtrDeadInterval_Object = MibTableColumn
tnEthIfRtrDeadInterval = _TnEthIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 5),
    _TnEthIfRtrDeadInterval_Type()
)
tnEthIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnEthIfRtrDeadInterval.setUnits("seconds")


class _TnEthIfMetric_Type(Unsigned32):
    """Custom type tnEthIfMetric based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnEthIfMetric_Type.__name__ = "Unsigned32"
_TnEthIfMetric_Object = MibTableColumn
tnEthIfMetric = _TnEthIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 6),
    _TnEthIfMetric_Type()
)
tnEthIfMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfMetric.setStatus("current")


class _TnEthIfOspfAuthentType_Type(Integer32):
    """Custom type tnEthIfOspfAuthentType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("simple", 2),
          ("md5", 3))
    )


_TnEthIfOspfAuthentType_Type.__name__ = "Integer32"
_TnEthIfOspfAuthentType_Object = MibTableColumn
tnEthIfOspfAuthentType = _TnEthIfOspfAuthentType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 7),
    _TnEthIfOspfAuthentType_Type()
)
tnEthIfOspfAuthentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfOspfAuthentType.setStatus("current")


class _TnEthIfOspfAuthKey_Type(OctetString):
    """Custom type tnEthIfOspfAuthKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnEthIfOspfAuthKey_Type.__name__ = "OctetString"
_TnEthIfOspfAuthKey_Object = MibTableColumn
tnEthIfOspfAuthKey = _TnEthIfOspfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 8),
    _TnEthIfOspfAuthKey_Type()
)
tnEthIfOspfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfOspfAuthKey.setStatus("current")


class _TnEthIfOspfAuthKeyId_Type(Unsigned32):
    """Custom type tnEthIfOspfAuthKeyId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnEthIfOspfAuthKeyId_Type.__name__ = "Unsigned32"
_TnEthIfOspfAuthKeyId_Object = MibTableColumn
tnEthIfOspfAuthKeyId = _TnEthIfOspfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 9),
    _TnEthIfOspfAuthKeyId_Type()
)
tnEthIfOspfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfOspfAuthKeyId.setStatus("current")


class _TnEthIfOSPFAreaNumberId_Type(Integer32):
    """Custom type tnEthIfOSPFAreaNumberId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TnEthIfOSPFAreaNumberId_Type.__name__ = "Integer32"
_TnEthIfOSPFAreaNumberId_Object = MibTableColumn
tnEthIfOSPFAreaNumberId = _TnEthIfOSPFAreaNumberId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 10),
    _TnEthIfOSPFAreaNumberId_Type()
)
tnEthIfOSPFAreaNumberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfOSPFAreaNumberId.setStatus("current")


class _TnEthIfProxyArp_Type(Integer32):
    """Custom type tnEthIfProxyArp based on Integer32"""
    defaultValue = 2

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


_TnEthIfProxyArp_Type.__name__ = "Integer32"
_TnEthIfProxyArp_Object = MibTableColumn
tnEthIfProxyArp = _TnEthIfProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 11),
    _TnEthIfProxyArp_Type()
)
tnEthIfProxyArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfProxyArp.setStatus("current")


class _TnEthIfOspfRouteState_Type(Integer32):
    """Custom type tnEthIfOspfRouteState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noDynamicRouting", 1),
          ("redistribute", 2),
          ("oSPF", 3))
    )


_TnEthIfOspfRouteState_Type.__name__ = "Integer32"
_TnEthIfOspfRouteState_Object = MibTableColumn
tnEthIfOspfRouteState = _TnEthIfOspfRouteState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 12),
    _TnEthIfOspfRouteState_Type()
)
tnEthIfOspfRouteState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfOspfRouteState.setStatus("current")


class _TnEthIfDhcpEnabled_Type(TruthValue):
    """Custom type tnEthIfDhcpEnabled based on TruthValue"""
    defaultValue = 2


_TnEthIfDhcpEnabled_Type.__name__ = "TruthValue"
_TnEthIfDhcpEnabled_Object = MibTableColumn
tnEthIfDhcpEnabled = _TnEthIfDhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 13),
    _TnEthIfDhcpEnabled_Type()
)
tnEthIfDhcpEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfDhcpEnabled.setStatus("current")


class _TnEthIfDHCPRange_Type(Unsigned32):
    """Custom type tnEthIfDHCPRange based on Unsigned32"""
    defaultValue = 1


_TnEthIfDHCPRange_Type.__name__ = "Unsigned32"
_TnEthIfDHCPRange_Object = MibTableColumn
tnEthIfDHCPRange = _TnEthIfDHCPRange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 14),
    _TnEthIfDHCPRange_Type()
)
tnEthIfDHCPRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfDHCPRange.setStatus("current")


class _TnEthIfDHCPDfltGtwy_Type(TruthValue):
    """Custom type tnEthIfDHCPDfltGtwy based on TruthValue"""
    defaultValue = 1


_TnEthIfDHCPDfltGtwy_Type.__name__ = "TruthValue"
_TnEthIfDHCPDfltGtwy_Object = MibTableColumn
tnEthIfDHCPDfltGtwy = _TnEthIfDHCPDfltGtwy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 15),
    _TnEthIfDHCPDfltGtwy_Type()
)
tnEthIfDHCPDfltGtwy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfDHCPDfltGtwy.setStatus("current")


class _TnEthIfDhcpv6Enabled_Type(TruthValue):
    """Custom type tnEthIfDhcpv6Enabled based on TruthValue"""
    defaultValue = 2


_TnEthIfDhcpv6Enabled_Type.__name__ = "TruthValue"
_TnEthIfDhcpv6Enabled_Object = MibTableColumn
tnEthIfDhcpv6Enabled = _TnEthIfDhcpv6Enabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 16),
    _TnEthIfDhcpv6Enabled_Type()
)
tnEthIfDhcpv6Enabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfDhcpv6Enabled.setStatus("current")


class _TnEthIfDHCPv6Range_Type(Unsigned32):
    """Custom type tnEthIfDHCPv6Range based on Unsigned32"""
    defaultValue = 1


_TnEthIfDHCPv6Range_Type.__name__ = "Unsigned32"
_TnEthIfDHCPv6Range_Object = MibTableColumn
tnEthIfDHCPv6Range = _TnEthIfDHCPv6Range_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 17),
    _TnEthIfDHCPv6Range_Type()
)
tnEthIfDHCPv6Range.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfDHCPv6Range.setStatus("current")


class _TnEthIfDHCPClient_Type(TruthValue):
    """Custom type tnEthIfDHCPClient based on TruthValue"""
    defaultValue = 2


_TnEthIfDHCPClient_Type.__name__ = "TruthValue"
_TnEthIfDHCPClient_Object = MibTableColumn
tnEthIfDHCPClient = _TnEthIfDHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 18),
    _TnEthIfDHCPClient_Type()
)
tnEthIfDHCPClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfDHCPClient.setStatus("current")


class _TnEthIfDHCPClientDfltGtwy_Type(TruthValue):
    """Custom type tnEthIfDHCPClientDfltGtwy based on TruthValue"""
    defaultValue = 2


_TnEthIfDHCPClientDfltGtwy_Type.__name__ = "TruthValue"
_TnEthIfDHCPClientDfltGtwy_Object = MibTableColumn
tnEthIfDHCPClientDfltGtwy = _TnEthIfDHCPClientDfltGtwy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 19),
    _TnEthIfDHCPClientDfltGtwy_Type()
)
tnEthIfDHCPClientDfltGtwy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfDHCPClientDfltGtwy.setStatus("current")


class _TnEthIfIpV6SLAAC_Type(TruthValue):
    """Custom type tnEthIfIpV6SLAAC based on TruthValue"""
    defaultValue = 2


_TnEthIfIpV6SLAAC_Type.__name__ = "TruthValue"
_TnEthIfIpV6SLAAC_Object = MibTableColumn
tnEthIfIpV6SLAAC = _TnEthIfIpV6SLAAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 20),
    _TnEthIfIpV6SLAAC_Type()
)
tnEthIfIpV6SLAAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfIpV6SLAAC.setStatus("current")
_TnEthIfIpAddress_Type = IpAddress
_TnEthIfIpAddress_Object = MibTableColumn
tnEthIfIpAddress = _TnEthIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 21),
    _TnEthIfIpAddress_Type()
)
tnEthIfIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfIpAddress.setStatus("current")
_TnEthIfSubnetMask_Type = IpAddress
_TnEthIfSubnetMask_Object = MibTableColumn
tnEthIfSubnetMask = _TnEthIfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 22),
    _TnEthIfSubnetMask_Type()
)
tnEthIfSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfSubnetMask.setStatus("current")


class _TnEthIfInetAddressType_Type(InetAddressType):
    """Custom type tnEthIfInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnEthIfInetAddressType_Type.__name__ = "InetAddressType"
_TnEthIfInetAddressType_Object = MibTableColumn
tnEthIfInetAddressType = _TnEthIfInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 23),
    _TnEthIfInetAddressType_Type()
)
tnEthIfInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfInetAddressType.setStatus("current")


class _TnEthIfInetAddress_Type(InetAddress):
    """Custom type tnEthIfInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnEthIfInetAddress_Type.__name__ = "InetAddress"
_TnEthIfInetAddress_Object = MibTableColumn
tnEthIfInetAddress = _TnEthIfInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 24),
    _TnEthIfInetAddress_Type()
)
tnEthIfInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfInetAddress.setStatus("current")


class _TnEthIfPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tnEthIfPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_TnEthIfPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TnEthIfPrefixLength_Object = MibTableColumn
tnEthIfPrefixLength = _TnEthIfPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 25),
    _TnEthIfPrefixLength_Type()
)
tnEthIfPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfPrefixLength.setStatus("current")


class _TnEthIfDescription_Type(SnmpAdminString):
    """Custom type tnEthIfDescription based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnEthIfDescription_Type.__name__ = "SnmpAdminString"
_TnEthIfDescription_Object = MibTableColumn
tnEthIfDescription = _TnEthIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 26),
    _TnEthIfDescription_Type()
)
tnEthIfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfDescription.setStatus("current")


class _TnEthIfOspfAdjStateId_Type(Integer32):
    """Custom type tnEthIfOspfAdjStateId based on Integer32"""
    defaultValue = 1

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
        *(("down", 1),
          ("init", 2),
          ("twoWay", 3),
          ("exchangeStart", 4),
          ("exchange", 5),
          ("loading", 6),
          ("full", 7))
    )


_TnEthIfOspfAdjStateId_Type.__name__ = "Integer32"
_TnEthIfOspfAdjStateId_Object = MibTableColumn
tnEthIfOspfAdjStateId = _TnEthIfOspfAdjStateId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 27),
    _TnEthIfOspfAdjStateId_Type()
)
tnEthIfOspfAdjStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthIfOspfAdjStateId.setStatus("current")


class _TnEthIfOspfDrPriorityId_Type(Integer32):
    """Custom type tnEthIfOspfDrPriorityId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnEthIfOspfDrPriorityId_Type.__name__ = "Integer32"
_TnEthIfOspfDrPriorityId_Object = MibTableColumn
tnEthIfOspfDrPriorityId = _TnEthIfOspfDrPriorityId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 28),
    _TnEthIfOspfDrPriorityId_Type()
)
tnEthIfOspfDrPriorityId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfOspfDrPriorityId.setStatus("current")


class _TnEthIfOspfRetransint_Type(Unsigned32):
    """Custom type tnEthIfOspfRetransint based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnEthIfOspfRetransint_Type.__name__ = "Unsigned32"
_TnEthIfOspfRetransint_Object = MibTableColumn
tnEthIfOspfRetransint = _TnEthIfOspfRetransint_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 29),
    _TnEthIfOspfRetransint_Type()
)
tnEthIfOspfRetransint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfOspfRetransint.setStatus("current")


class _TnEthIfOspfv3AdjStateId_Type(TropicOspfAdjacencyStateType):
    """Custom type tnEthIfOspfv3AdjStateId based on TropicOspfAdjacencyStateType"""
    defaultValue = 1


_TnEthIfOspfv3AdjStateId_Type.__name__ = "TropicOspfAdjacencyStateType"
_TnEthIfOspfv3AdjStateId_Object = MibTableColumn
tnEthIfOspfv3AdjStateId = _TnEthIfOspfv3AdjStateId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 30),
    _TnEthIfOspfv3AdjStateId_Type()
)
tnEthIfOspfv3AdjStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthIfOspfv3AdjStateId.setStatus("current")
_TnEthIfOperStatus_Type = TropicLinkOperationalStateType
_TnEthIfOperStatus_Object = MibTableColumn
tnEthIfOperStatus = _TnEthIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 31),
    _TnEthIfOperStatus_Type()
)
tnEthIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthIfOperStatus.setStatus("current")


class _TnEthIfAlmProfName_Type(OctetString):
    """Custom type tnEthIfAlmProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_TnEthIfAlmProfName_Type.__name__ = "OctetString"
_TnEthIfAlmProfName_Object = MibTableColumn
tnEthIfAlmProfName = _TnEthIfAlmProfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 32),
    _TnEthIfAlmProfName_Type()
)
tnEthIfAlmProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfAlmProfName.setStatus("current")


class _TnEthIfDHCPServerIPv6SLAAC_Type(SnmpAdminString):
    """Custom type tnEthIfDHCPServerIPv6SLAAC based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnEthIfDHCPServerIPv6SLAAC_Type.__name__ = "SnmpAdminString"
_TnEthIfDHCPServerIPv6SLAAC_Object = MibTableColumn
tnEthIfDHCPServerIPv6SLAAC = _TnEthIfDHCPServerIPv6SLAAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 33),
    _TnEthIfDHCPServerIPv6SLAAC_Type()
)
tnEthIfDHCPServerIPv6SLAAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthIfDHCPServerIPv6SLAAC.setStatus("current")


class _TnEthIfRouterAdvAutonomousFlag_Type(TruthValue):
    """Custom type tnEthIfRouterAdvAutonomousFlag based on TruthValue"""
    defaultValue = 2


_TnEthIfRouterAdvAutonomousFlag_Type.__name__ = "TruthValue"
_TnEthIfRouterAdvAutonomousFlag_Object = MibTableColumn
tnEthIfRouterAdvAutonomousFlag = _TnEthIfRouterAdvAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 34),
    _TnEthIfRouterAdvAutonomousFlag_Type()
)
tnEthIfRouterAdvAutonomousFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfRouterAdvAutonomousFlag.setStatus("current")


class _TnEthIfRouterAdvDefaultLifeTime_Type(Unsigned32):
    """Custom type tnEthIfRouterAdvDefaultLifeTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
    )


_TnEthIfRouterAdvDefaultLifeTime_Type.__name__ = "Unsigned32"
_TnEthIfRouterAdvDefaultLifeTime_Object = MibTableColumn
tnEthIfRouterAdvDefaultLifeTime = _TnEthIfRouterAdvDefaultLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 35),
    _TnEthIfRouterAdvDefaultLifeTime_Type()
)
tnEthIfRouterAdvDefaultLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfRouterAdvDefaultLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tnEthIfRouterAdvDefaultLifeTime.setUnits("seconds")


class _TnEthIfRouterAdvDefaultPreference_Type(Integer32):
    """Custom type tnEthIfRouterAdvDefaultPreference based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_TnEthIfRouterAdvDefaultPreference_Type.__name__ = "Integer32"
_TnEthIfRouterAdvDefaultPreference_Object = MibTableColumn
tnEthIfRouterAdvDefaultPreference = _TnEthIfRouterAdvDefaultPreference_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 36),
    _TnEthIfRouterAdvDefaultPreference_Type()
)
tnEthIfRouterAdvDefaultPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfRouterAdvDefaultPreference.setStatus("current")


class _TnEthIfRouterAdvMaxRtrAdvInterval_Type(Unsigned32):
    """Custom type tnEthIfRouterAdvMaxRtrAdvInterval based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1800),
    )


_TnEthIfRouterAdvMaxRtrAdvInterval_Type.__name__ = "Unsigned32"
_TnEthIfRouterAdvMaxRtrAdvInterval_Object = MibTableColumn
tnEthIfRouterAdvMaxRtrAdvInterval = _TnEthIfRouterAdvMaxRtrAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 37),
    _TnEthIfRouterAdvMaxRtrAdvInterval_Type()
)
tnEthIfRouterAdvMaxRtrAdvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfRouterAdvMaxRtrAdvInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnEthIfRouterAdvMaxRtrAdvInterval.setUnits("seconds")


class _TnEthIfRouterAdvManagedFlag_Type(TruthValue):
    """Custom type tnEthIfRouterAdvManagedFlag based on TruthValue"""
    defaultValue = 2


_TnEthIfRouterAdvManagedFlag_Type.__name__ = "TruthValue"
_TnEthIfRouterAdvManagedFlag_Object = MibTableColumn
tnEthIfRouterAdvManagedFlag = _TnEthIfRouterAdvManagedFlag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 38),
    _TnEthIfRouterAdvManagedFlag_Type()
)
tnEthIfRouterAdvManagedFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfRouterAdvManagedFlag.setStatus("current")


class _TnEthIfRouterAdvOtherConfigFlag_Type(TruthValue):
    """Custom type tnEthIfRouterAdvOtherConfigFlag based on TruthValue"""
    defaultValue = 2


_TnEthIfRouterAdvOtherConfigFlag_Type.__name__ = "TruthValue"
_TnEthIfRouterAdvOtherConfigFlag_Object = MibTableColumn
tnEthIfRouterAdvOtherConfigFlag = _TnEthIfRouterAdvOtherConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 39),
    _TnEthIfRouterAdvOtherConfigFlag_Type()
)
tnEthIfRouterAdvOtherConfigFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfRouterAdvOtherConfigFlag.setStatus("current")


class _TnEthIfRouterAdvPreferredLifeTime_Type(Unsigned32):
    """Custom type tnEthIfRouterAdvPreferredLifeTime based on Unsigned32"""
    defaultValue = 14400


_TnEthIfRouterAdvPreferredLifeTime_Type.__name__ = "Unsigned32"
_TnEthIfRouterAdvPreferredLifeTime_Object = MibTableColumn
tnEthIfRouterAdvPreferredLifeTime = _TnEthIfRouterAdvPreferredLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 40),
    _TnEthIfRouterAdvPreferredLifeTime_Type()
)
tnEthIfRouterAdvPreferredLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfRouterAdvPreferredLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tnEthIfRouterAdvPreferredLifeTime.setUnits("seconds")


class _TnEthIfRouterAdvSendAdvertState_Type(TruthValue):
    """Custom type tnEthIfRouterAdvSendAdvertState based on TruthValue"""
    defaultValue = 2


_TnEthIfRouterAdvSendAdvertState_Type.__name__ = "TruthValue"
_TnEthIfRouterAdvSendAdvertState_Object = MibTableColumn
tnEthIfRouterAdvSendAdvertState = _TnEthIfRouterAdvSendAdvertState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 41),
    _TnEthIfRouterAdvSendAdvertState_Type()
)
tnEthIfRouterAdvSendAdvertState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfRouterAdvSendAdvertState.setStatus("current")


class _TnEthIfRouterAdvValidLifeTime_Type(Unsigned32):
    """Custom type tnEthIfRouterAdvValidLifeTime based on Unsigned32"""
    defaultValue = 86400


_TnEthIfRouterAdvValidLifeTime_Type.__name__ = "Unsigned32"
_TnEthIfRouterAdvValidLifeTime_Object = MibTableColumn
tnEthIfRouterAdvValidLifeTime = _TnEthIfRouterAdvValidLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 42),
    _TnEthIfRouterAdvValidLifeTime_Type()
)
tnEthIfRouterAdvValidLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfRouterAdvValidLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tnEthIfRouterAdvValidLifeTime.setUnits("seconds")


class _TnEthIfOspfv3AreaNumberId_Type(Integer32):
    """Custom type tnEthIfOspfv3AreaNumberId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TnEthIfOspfv3AreaNumberId_Type.__name__ = "Integer32"
_TnEthIfOspfv3AreaNumberId_Object = MibTableColumn
tnEthIfOspfv3AreaNumberId = _TnEthIfOspfv3AreaNumberId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 43),
    _TnEthIfOspfv3AreaNumberId_Type()
)
tnEthIfOspfv3AreaNumberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfOspfv3AreaNumberId.setStatus("current")


class _TnEthIfOspfv3HelloInterval_Type(Unsigned32):
    """Custom type tnEthIfOspfv3HelloInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnEthIfOspfv3HelloInterval_Type.__name__ = "Unsigned32"
_TnEthIfOspfv3HelloInterval_Object = MibTableColumn
tnEthIfOspfv3HelloInterval = _TnEthIfOspfv3HelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 44),
    _TnEthIfOspfv3HelloInterval_Type()
)
tnEthIfOspfv3HelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfOspfv3HelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnEthIfOspfv3HelloInterval.setUnits("seconds")


class _TnEthIfOspfv3Metric_Type(Unsigned32):
    """Custom type tnEthIfOspfv3Metric based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnEthIfOspfv3Metric_Type.__name__ = "Unsigned32"
_TnEthIfOspfv3Metric_Object = MibTableColumn
tnEthIfOspfv3Metric = _TnEthIfOspfv3Metric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 45),
    _TnEthIfOspfv3Metric_Type()
)
tnEthIfOspfv3Metric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfOspfv3Metric.setStatus("current")


class _TnEthIfOspfv3Retransint_Type(Unsigned32):
    """Custom type tnEthIfOspfv3Retransint based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnEthIfOspfv3Retransint_Type.__name__ = "Unsigned32"
_TnEthIfOspfv3Retransint_Object = MibTableColumn
tnEthIfOspfv3Retransint = _TnEthIfOspfv3Retransint_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 46),
    _TnEthIfOspfv3Retransint_Type()
)
tnEthIfOspfv3Retransint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfOspfv3Retransint.setStatus("current")


class _TnEthIfOspfv3RtrDeadInterval_Type(Unsigned32):
    """Custom type tnEthIfOspfv3RtrDeadInterval based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnEthIfOspfv3RtrDeadInterval_Type.__name__ = "Unsigned32"
_TnEthIfOspfv3RtrDeadInterval_Object = MibTableColumn
tnEthIfOspfv3RtrDeadInterval = _TnEthIfOspfv3RtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 47),
    _TnEthIfOspfv3RtrDeadInterval_Type()
)
tnEthIfOspfv3RtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfOspfv3RtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnEthIfOspfv3RtrDeadInterval.setUnits("seconds")


class _TnEthIfOspfv3DrPriorityId_Type(Integer32):
    """Custom type tnEthIfOspfv3DrPriorityId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnEthIfOspfv3DrPriorityId_Type.__name__ = "Integer32"
_TnEthIfOspfv3DrPriorityId_Object = MibTableColumn
tnEthIfOspfv3DrPriorityId = _TnEthIfOspfv3DrPriorityId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 48),
    _TnEthIfOspfv3DrPriorityId_Type()
)
tnEthIfOspfv3DrPriorityId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfOspfv3DrPriorityId.setStatus("current")


class _TnEthIfOspfv3RouteState_Type(Integer32):
    """Custom type tnEthIfOspfv3RouteState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noDynamicRouting", 1),
          ("redistribute", 2),
          ("oSPF", 3))
    )


_TnEthIfOspfv3RouteState_Type.__name__ = "Integer32"
_TnEthIfOspfv3RouteState_Object = MibTableColumn
tnEthIfOspfv3RouteState = _TnEthIfOspfv3RouteState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 1, 1, 49),
    _TnEthIfOspfv3RouteState_Type()
)
tnEthIfOspfv3RouteState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfOspfv3RouteState.setStatus("current")
_TnEthIfInterfaceTable_Object = MibTable
tnEthIfInterfaceTable = _TnEthIfInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 2)
)
if mibBuilder.loadTexts:
    tnEthIfInterfaceTable.setStatus("current")
_TnEthIfInterfaceEntry_Object = MibTableRow
tnEthIfInterfaceEntry = _TnEthIfInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 2, 1)
)
tnEthIfInterfaceEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnEthIfIndex"),
    (0, "TROPIC-L1SERVICE-MIB", "tnEthIfInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    tnEthIfInterfaceEntry.setStatus("current")
_TnEthIfInterfaceIfIndex_Type = Unsigned32
_TnEthIfInterfaceIfIndex_Object = MibTableColumn
tnEthIfInterfaceIfIndex = _TnEthIfInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 2, 1, 1),
    _TnEthIfInterfaceIfIndex_Type()
)
tnEthIfInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthIfInterfaceIfIndex.setStatus("current")


class _TnEthIfInterfaceVlanId_Type(Unsigned32):
    """Custom type tnEthIfInterfaceVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_TnEthIfInterfaceVlanId_Type.__name__ = "Unsigned32"
_TnEthIfInterfaceVlanId_Object = MibTableColumn
tnEthIfInterfaceVlanId = _TnEthIfInterfaceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 2, 1, 2),
    _TnEthIfInterfaceVlanId_Type()
)
tnEthIfInterfaceVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfInterfaceVlanId.setStatus("current")
_TnEthIfInterfaceTypeOfOperation_Type = AluWdmTypeOfNetIfOperation
_TnEthIfInterfaceTypeOfOperation_Object = MibTableColumn
tnEthIfInterfaceTypeOfOperation = _TnEthIfInterfaceTypeOfOperation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 11, 2, 1, 3),
    _TnEthIfInterfaceTypeOfOperation_Type()
)
tnEthIfInterfaceTypeOfOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthIfInterfaceTypeOfOperation.setStatus("current")
_TnDhcpRelay_ObjectIdentity = ObjectIdentity
tnDhcpRelay = _TnDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 12)
)
_TnDhcpRelayRecordTable_Object = MibTable
tnDhcpRelayRecordTable = _TnDhcpRelayRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    tnDhcpRelayRecordTable.setStatus("current")
_TnDhcpRelayRecordEntry_Object = MibTableRow
tnDhcpRelayRecordEntry = _TnDhcpRelayRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 12, 1, 1)
)
tnDhcpRelayRecordEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnDhcpRelayRecordIndex1"),
    (0, "TROPIC-L1SERVICE-MIB", "tnDhcpRelayRecordIndex2"),
    (0, "TROPIC-L1SERVICE-MIB", "tnDhcpRelayRecordInetAddressType"),
    (0, "TROPIC-L1SERVICE-MIB", "tnDhcpRelayRecordInetAddress"),
)
if mibBuilder.loadTexts:
    tnDhcpRelayRecordEntry.setStatus("current")
_TnDhcpRelayRecordIndex1_Type = Integer32
_TnDhcpRelayRecordIndex1_Object = MibTableColumn
tnDhcpRelayRecordIndex1 = _TnDhcpRelayRecordIndex1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 12, 1, 1, 1),
    _TnDhcpRelayRecordIndex1_Type()
)
tnDhcpRelayRecordIndex1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpRelayRecordIndex1.setStatus("current")
_TnDhcpRelayRecordIndex2_Type = Integer32
_TnDhcpRelayRecordIndex2_Object = MibTableColumn
tnDhcpRelayRecordIndex2 = _TnDhcpRelayRecordIndex2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 12, 1, 1, 2),
    _TnDhcpRelayRecordIndex2_Type()
)
tnDhcpRelayRecordIndex2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpRelayRecordIndex2.setStatus("current")
_TnDhcpRelayRecordInetAddressType_Type = InetAddressType
_TnDhcpRelayRecordInetAddressType_Object = MibTableColumn
tnDhcpRelayRecordInetAddressType = _TnDhcpRelayRecordInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 12, 1, 1, 3),
    _TnDhcpRelayRecordInetAddressType_Type()
)
tnDhcpRelayRecordInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpRelayRecordInetAddressType.setStatus("current")
_TnDhcpRelayRecordInetAddress_Type = InetAddress
_TnDhcpRelayRecordInetAddress_Object = MibTableColumn
tnDhcpRelayRecordInetAddress = _TnDhcpRelayRecordInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 12, 1, 1, 4),
    _TnDhcpRelayRecordInetAddress_Type()
)
tnDhcpRelayRecordInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpRelayRecordInetAddress.setStatus("current")
_TnDhcpRelayRecordRowStatus_Type = RowStatus
_TnDhcpRelayRecordRowStatus_Object = MibTableColumn
tnDhcpRelayRecordRowStatus = _TnDhcpRelayRecordRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 12, 1, 1, 5),
    _TnDhcpRelayRecordRowStatus_Type()
)
tnDhcpRelayRecordRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDhcpRelayRecordRowStatus.setStatus("current")


class _TnDhcpRelayRecordRailIdDescr_Type(SnmpAdminString):
    """Custom type tnDhcpRelayRecordRailIdDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnDhcpRelayRecordRailIdDescr_Type.__name__ = "SnmpAdminString"
_TnDhcpRelayRecordRailIdDescr_Object = MibTableColumn
tnDhcpRelayRecordRailIdDescr = _TnDhcpRelayRecordRailIdDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 12, 1, 1, 6),
    _TnDhcpRelayRecordRailIdDescr_Type()
)
tnDhcpRelayRecordRailIdDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDhcpRelayRecordRailIdDescr.setStatus("current")
_TnDhcpServer_ObjectIdentity = ObjectIdentity
tnDhcpServer = _TnDhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 13)
)
_TnDhcpServerTable_Object = MibTable
tnDhcpServerTable = _TnDhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    tnDhcpServerTable.setStatus("current")
_TnDhcpServerEntry_Object = MibTableRow
tnDhcpServerEntry = _TnDhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 13, 1, 1)
)
tnDhcpServerEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnDhcpServerInetAddressType"),
    (0, "TROPIC-L1SERVICE-MIB", "tnDhcpServerInetAddress"),
)
if mibBuilder.loadTexts:
    tnDhcpServerEntry.setStatus("current")
_TnDhcpServerInetAddressType_Type = InetAddressType
_TnDhcpServerInetAddressType_Object = MibTableColumn
tnDhcpServerInetAddressType = _TnDhcpServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 13, 1, 1, 1),
    _TnDhcpServerInetAddressType_Type()
)
tnDhcpServerInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpServerInetAddressType.setStatus("current")
_TnDhcpServerInetAddress_Type = InetAddress
_TnDhcpServerInetAddress_Object = MibTableColumn
tnDhcpServerInetAddress = _TnDhcpServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 13, 1, 1, 2),
    _TnDhcpServerInetAddress_Type()
)
tnDhcpServerInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpServerInetAddress.setStatus("current")


class _TnDhcpServerSerialno_Type(OctetString):
    """Custom type tnDhcpServerSerialno based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDhcpServerSerialno_Type.__name__ = "OctetString"
_TnDhcpServerSerialno_Object = MibTableColumn
tnDhcpServerSerialno = _TnDhcpServerSerialno_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 13, 1, 1, 3),
    _TnDhcpServerSerialno_Type()
)
tnDhcpServerSerialno.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDhcpServerSerialno.setStatus("current")
_TnDhcpServerMacAddress_Type = MacAddress
_TnDhcpServerMacAddress_Object = MibTableColumn
tnDhcpServerMacAddress = _TnDhcpServerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 13, 1, 1, 4),
    _TnDhcpServerMacAddress_Type()
)
tnDhcpServerMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDhcpServerMacAddress.setStatus("current")
_TnDhcpServerPort_Type = Integer32
_TnDhcpServerPort_Object = MibTableColumn
tnDhcpServerPort = _TnDhcpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 13, 1, 1, 5),
    _TnDhcpServerPort_Type()
)
tnDhcpServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerPort.setStatus("current")
_TnDhcpServerRowStatus_Type = RowStatus
_TnDhcpServerRowStatus_Object = MibTableColumn
tnDhcpServerRowStatus = _TnDhcpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 2, 13, 1, 1, 6),
    _TnDhcpServerRowStatus_Type()
)
tnDhcpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDhcpServerRowStatus.setStatus("current")
ipCidrRouteEntry.registerAugmentions(
    ("TROPIC-L1SERVICE-MIB",
     "tnIpCidrRouteEntry")
)
tnIpCidrRouteEntry.setIndexNames(*ipCidrRouteEntry.getIndexNames())

# Managed Objects groups

tnControlNetworkLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 1)
)
tnControlNetworkLinkGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnCNLinkDescr"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkAdminStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOperStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkPhysicalIfIndex"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkIpAddress"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkSubnetMask"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkHelloInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkRtrDeadInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkTeMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfRoutingState"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkConfigIfType"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkConfigRtrPriority"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkEquipOperStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDhcpEnabled"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkSpeed"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDuplex"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkProxyArp"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDHCPServer"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDHCPRange"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkAdjState"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOscMode"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDHCPDfltGtwy"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkCitAutoStateCtrl"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkAutoStateSourceIP"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkSourceLossCount"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkSourceIPCheckInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfAuthentType"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfAuthKey"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfAuthKeyId"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkTdmxDcnConf"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkInetAddressType"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkInetAddress"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkPrefixLength"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkAutoStateSourceInetAddressType"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkAutoStateSourceInetAddress"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDhcpv6Enabled"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDHCPv6Range"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDHCPClient"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDHCPv6Client"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDHCPClientDfltGtwy"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkEtherPortIpV6SLAAC"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfRetransint"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfv3AdjStateId"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfNeighborRouterIp"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfv3NeighborRouterIp"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfNeighborIp"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfv3NeighborInetAddress"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkRole"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDHCPServerIPv6SLAAC"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkRouterAdvAutonomousFlag"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkRouterAdvDefaultLifeTime"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkRouterAdvDefaultPreference"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkRouterAdvMaxRtrAdvInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkRouterAdvManagedFlag"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkRouterAdvOtherConfigFlag"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkRouterAdvPreferredLifeTime"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkRouterAdvSendAdvertState"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkRouterAdvValidLifeTime"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkAutoStateType"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkAutoStateStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfv3HelloInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfv3TeMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfv3Retransint"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfv3RtrDeadInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfv3ConfigRtrPriority"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfv3RoutingState"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfOscRoutingState"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkOspfv6OscRoutingState"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDHCPBootFileName"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkDHCPClassName"))
)
if mibBuilder.loadTexts:
    tnControlNetworkLinkGroup.setStatus("current")

tnCNLinkViaChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 2)
)
tnCNLinkViaChannelGroup.setObjects(
    ("TROPIC-L1SERVICE-MIB", "tnCNLinkViaChannelIfIndex")
)
if mibBuilder.loadTexts:
    tnCNLinkViaChannelGroup.setStatus("current")

tnIpStaticRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 3)
)
tnIpStaticRouteGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnIpStaticRouteMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnIpStaticRouteWithRedistribution"),
        ("TROPIC-L1SERVICE-MIB", "tnIpStaticRouteRowStatus"))
)
if mibBuilder.loadTexts:
    tnIpStaticRouteGroup.setStatus("deprecated")

tnIpCidrRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 4)
)
tnIpCidrRouteGroup.setObjects(
    ("TROPIC-L1SERVICE-MIB", "tnIpCidrRouteWithRedistribution")
)
if mibBuilder.loadTexts:
    tnIpCidrRouteGroup.setStatus("current")

tnL1TrafficParmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 5)
)
tnL1TrafficParmGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnL1TrafficParamBookingFactor"),
        ("TROPIC-L1SERVICE-MIB", "tnL1TrafficParamMaximumLoad"),
        ("TROPIC-L1SERVICE-MIB", "tnL1TrafficParamPMF"),
        ("TROPIC-L1SERVICE-MIB", "tnL1TrafficParamAvailableBandwidth"))
)
if mibBuilder.loadTexts:
    tnL1TrafficParmGroup.setStatus("current")

tnIpRouteGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 6)
)
tnIpRouteGlobalGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnIpStaticRouteRedistributeMetricType"),
        ("TROPIC-L1SERVICE-MIB", "tnIpStaticRouteRedistributeMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnIpDefaultRouteRedistributeMetricType"),
        ("TROPIC-L1SERVICE-MIB", "tnIpDefaultRouteRedistributeMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnIpOspfAreaNumberPPPId"),
        ("TROPIC-L1SERVICE-MIB", "tnIpOspfRouterId"),
        ("TROPIC-L1SERVICE-MIB", "tnIpDefaultRouteRedistributeBgpToOspfMetricType"),
        ("TROPIC-L1SERVICE-MIB", "tnIpDefaultRouteRedistributeBgpToOspfMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnIpDefaultRouteRedistributeBgpToOspfMode"),
        ("TROPIC-L1SERVICE-MIB", "tnIpDefaultRouteRedistributeKernelToOspfMetricType"),
        ("TROPIC-L1SERVICE-MIB", "tnIpDefaultRouteRedistributeKernelToOspfMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnIpDefaultRouteRedistributeKernelToOspfStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnIpStaticRouteRedistributeBgpMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnIpOspfV3AreaNumberPPPId"),
        ("TROPIC-L1SERVICE-MIB", "tnIpDefaultRouteRedistributeOspfToBgpMode"),
        ("TROPIC-L1SERVICE-MIB", "tnIpDefaultRouteRedistributeOspfToBgpMetric"))
)
if mibBuilder.loadTexts:
    tnIpRouteGlobalGroup.setStatus("current")

tnStaticRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 7)
)
tnStaticRouteGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnStaticRouteMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnStaticRouteWithRedistribution"),
        ("TROPIC-L1SERVICE-MIB", "tnStaticRouteRowStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnStaticRouteIdentifier"),
        ("TROPIC-L1SERVICE-MIB", "tnStaticRouteWithBgpDistribution"))
)
if mibBuilder.loadTexts:
    tnStaticRouteGroup.setStatus("current")

tnIpNonDefaultRouteOspfToBgpCommTagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 8)
)
tnIpNonDefaultRouteOspfToBgpCommTagGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnIpNonDefaultRouteOspfToBgpCommTagRowStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnIpNonDefaultRouteOspfToBgpCommTag"))
)
if mibBuilder.loadTexts:
    tnIpNonDefaultRouteOspfToBgpCommTagGroup.setStatus("current")

tnIpNonDefaultRedistBgpToOspfRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 9)
)
tnIpNonDefaultRedistBgpToOspfRuleGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnIpNonDefaultRedistBgpToOspfRuleRowStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnIpNonDefaultRedistBgpToOspfRuleOspfTag"),
        ("TROPIC-L1SERVICE-MIB", "tnIpNonDefaultRedistBgpToOspfRuleMode"),
        ("TROPIC-L1SERVICE-MIB", "tnIpNonDefaultRedistBgpToOspfRuleMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnIpNonDefaultRedistBgpToOspfRuleMetricType"))
)
if mibBuilder.loadTexts:
    tnIpNonDefaultRedistBgpToOspfRuleGroup.setStatus("current")

tnApsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 10)
)
tnApsGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnApsGroupRowStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupDescr"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupMode"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupRevert"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupDirection"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupExtraTraffic"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupWaitToRestore"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupK1K2Rcv"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupK1K2Trans"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupCurrentStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupModeMismatches"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupChannelMismatches"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupPSBFs"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupFEPLFs"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupSwitchedIfIndex"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupMembers"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroupSdEnable"),
        ("TROPIC-L1SERVICE-MIB", "tnApsHoldOffTimer"))
)
if mibBuilder.loadTexts:
    tnApsGroup.setStatus("current")

tnApsMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 11)
)
tnApsMemberGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnApsMemberRowStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnApsMemberConfigNumber"),
        ("TROPIC-L1SERVICE-MIB", "tnApsMemberSwitch"),
        ("TROPIC-L1SERVICE-MIB", "tnApsMemberCurrentStatus"))
)
if mibBuilder.loadTexts:
    tnApsMemberGroup.setStatus("current")

tnControlNetworkMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 13)
)
tnControlNetworkMapGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnCNMapIpAddress"),
        ("TROPIC-L1SERVICE-MIB", "tnCNMapNeName"),
        ("TROPIC-L1SERVICE-MIB", "tnCNMapSoftwareRelease"),
        ("TROPIC-L1SERVICE-MIB", "tnCNMapIpv6InetAddress"),
        ("TROPIC-L1SERVICE-MIB", "tnCNMapIpv4Address"))
)
if mibBuilder.loadTexts:
    tnControlNetworkMapGroup.setStatus("current")

tnNetIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 14)
)
tnNetIfGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnNetIfTypeOfOperation"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfPacketType"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfMtu"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfHelloInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfRtrDeadInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfAuthentType"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfAuthKey"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfAuthKeyId"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfCnLinkAdjState"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfMtuNeg"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOSPFAreaNumberId"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfRetransint"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfv3AdjStateId"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfNeighborRouterIp"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfv3NeighborRouterIp"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfNeighborIp"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfv3NeighborInetAddress"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfIPv6LinkLocalInetAddress"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfLcpEchoInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfLcpEchoFailure"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfv3AreaNumberId"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfv3HelloInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfv3Metric"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfv3Retransint"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfv3RtrDeadInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfv3ConfigRtrPriority"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfOspfv3Status"))
)
if mibBuilder.loadTexts:
    tnNetIfGroup.setStatus("current")

tnNetIfFacilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 15)
)
tnNetIfFacilityGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnNetIfFacilityTypeOfOperation"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfFacilityEccChanType"))
)
if mibBuilder.loadTexts:
    tnNetIfFacilityGroup.setStatus("current")

tnPackApsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 16)
)
tnPackApsGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnPackApsGroupRowStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnPackApsGroupWorkIfIndex"),
        ("TROPIC-L1SERVICE-MIB", "tnPackApsGroupProtIfIndex"),
        ("TROPIC-L1SERVICE-MIB", "tnPackApsGroupDescr"),
        ("TROPIC-L1SERVICE-MIB", "tnPackApsGroupRevert"),
        ("TROPIC-L1SERVICE-MIB", "tnPackApsGroupDirection"),
        ("TROPIC-L1SERVICE-MIB", "tnPackApsGroupWaitToRestore"),
        ("TROPIC-L1SERVICE-MIB", "tnPackApsGroupHoldOffTimer"),
        ("TROPIC-L1SERVICE-MIB", "tnPackApsGroupSwitchCmd"),
        ("TROPIC-L1SERVICE-MIB", "tnPackApsGroupActSide"),
        ("TROPIC-L1SERVICE-MIB", "tnPackApsGroupCurrentStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnPackApsGroupWorkStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnPackApsGroupProtStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnPackApsGroupPortFailEnable"))
)
if mibBuilder.loadTexts:
    tnPackApsGroup.setStatus("current")

tnEthIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 17)
)
tnEthIfGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnEthIfTypeOfOperation"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfHelloInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfRtrDeadInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfMetric"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOspfAuthentType"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOspfAuthKey"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOspfAuthKeyId"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOSPFAreaNumberId"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfProxyArp"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOspfRouteState"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfDhcpEnabled"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfDHCPRange"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfDHCPDfltGtwy"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfDhcpv6Enabled"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfDHCPv6Range"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfDHCPClient"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfDHCPClientDfltGtwy"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfIpV6SLAAC"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfIpAddress"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfSubnetMask"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfInetAddressType"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfInetAddress"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfPrefixLength"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfDescription"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOspfAdjStateId"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOspfDrPriorityId"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOspfRetransint"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOspfv3AdjStateId"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOperStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfAlmProfName"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfDHCPServerIPv6SLAAC"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfRouterAdvAutonomousFlag"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfRouterAdvDefaultLifeTime"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfRouterAdvDefaultPreference"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfRouterAdvMaxRtrAdvInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfRouterAdvManagedFlag"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfRouterAdvOtherConfigFlag"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfRouterAdvPreferredLifeTime"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfRouterAdvSendAdvertState"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfRouterAdvValidLifeTime"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOspfv3AreaNumberId"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOspfv3HelloInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOspfv3Metric"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOspfv3Retransint"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOspfv3RtrDeadInterval"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOspfv3DrPriorityId"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfOspfv3RouteState"))
)
if mibBuilder.loadTexts:
    tnEthIfGroup.setStatus("current")

tnEthIfInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 18)
)
tnEthIfInterfaceGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnEthIfInterfaceVlanId"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfInterfaceTypeOfOperation"))
)
if mibBuilder.loadTexts:
    tnEthIfInterfaceGroup.setStatus("current")

tnDhcpRelayRecordGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 19)
)
tnDhcpRelayRecordGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnDhcpRelayRecordRowStatus"),
        ("TROPIC-L1SERVICE-MIB", "tnDhcpRelayRecordRailIdDescr"))
)
if mibBuilder.loadTexts:
    tnDhcpRelayRecordGroup.setStatus("current")

tnDhcpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 1, 20)
)
tnDhcpServerGroup.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnDhcpServerSerialno"),
        ("TROPIC-L1SERVICE-MIB", "tnDhcpServerMacAddress"),
        ("TROPIC-L1SERVICE-MIB", "tnDhcpServerPort"),
        ("TROPIC-L1SERVICE-MIB", "tnDhcpServerRowStatus"))
)
if mibBuilder.loadTexts:
    tnDhcpServerGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnL1ServiceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1, 1, 2, 1)
)
tnL1ServiceCompliance.setObjects(
      *(("TROPIC-L1SERVICE-MIB", "tnControlNetworkLinkGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnCNLinkViaChannelGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnIpStaticRouteGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnIpCidrRouteGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnL1TrafficParmGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnIpRouteGlobalGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnApsGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnApsMemberGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnControlNetworkMapGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnNetIfFacilityGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnPackApsGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnStaticRouteGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnEthIfInterfaceGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnDhcpRelayRecordGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnDhcpServerGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnIpNonDefaultRouteOspfToBgpCommTagGroup"),
        ("TROPIC-L1SERVICE-MIB", "tnIpNonDefaultRedistBgpToOspfRuleGroup"))
)
if mibBuilder.loadTexts:
    tnL1ServiceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-L1SERVICE-MIB",
    **{"ApsK1K2": ApsK1K2,
       "TropicProtectionLevel": TropicProtectionLevel,
       "TropicLinkAdminStateType": TropicLinkAdminStateType,
       "TropicLinkOperationalStateType": TropicLinkOperationalStateType,
       "TropicOspfAdjacencyStateType": TropicOspfAdjacencyStateType,
       "AluPortYcableMode": AluPortYcableMode,
       "NokiaCNLinkOspfRoutingState": NokiaCNLinkOspfRoutingState,
       "tnL1ServiceMibModule": tnL1ServiceMibModule,
       "tnL1ServiceConf": tnL1ServiceConf,
       "tnL1ServiceGroups": tnL1ServiceGroups,
       "tnControlNetworkLinkGroup": tnControlNetworkLinkGroup,
       "tnCNLinkViaChannelGroup": tnCNLinkViaChannelGroup,
       "tnIpStaticRouteGroup": tnIpStaticRouteGroup,
       "tnIpCidrRouteGroup": tnIpCidrRouteGroup,
       "tnL1TrafficParmGroup": tnL1TrafficParmGroup,
       "tnIpRouteGlobalGroup": tnIpRouteGlobalGroup,
       "tnStaticRouteGroup": tnStaticRouteGroup,
       "tnIpNonDefaultRouteOspfToBgpCommTagGroup": tnIpNonDefaultRouteOspfToBgpCommTagGroup,
       "tnIpNonDefaultRedistBgpToOspfRuleGroup": tnIpNonDefaultRedistBgpToOspfRuleGroup,
       "tnApsGroup": tnApsGroup,
       "tnApsMemberGroup": tnApsMemberGroup,
       "tnControlNetworkMapGroup": tnControlNetworkMapGroup,
       "tnNetIfGroup": tnNetIfGroup,
       "tnNetIfFacilityGroup": tnNetIfFacilityGroup,
       "tnPackApsGroup": tnPackApsGroup,
       "tnEthIfGroup": tnEthIfGroup,
       "tnEthIfInterfaceGroup": tnEthIfInterfaceGroup,
       "tnDhcpRelayRecordGroup": tnDhcpRelayRecordGroup,
       "tnDhcpServerGroup": tnDhcpServerGroup,
       "tnL1ServiceCompliances": tnL1ServiceCompliances,
       "tnL1ServiceCompliance": tnL1ServiceCompliance,
       "tnL1ServiceObjs": tnL1ServiceObjs,
       "tnControlNetworkLink": tnControlNetworkLink,
       "tnControlNetworkLinkTable": tnControlNetworkLinkTable,
       "tnControlNetworkLinkEntry": tnControlNetworkLinkEntry,
       "tnCNLinkDescr": tnCNLinkDescr,
       "tnCNLinkAdminStatus": tnCNLinkAdminStatus,
       "tnCNLinkOperStatus": tnCNLinkOperStatus,
       "tnCNLinkPhysicalIfIndex": tnCNLinkPhysicalIfIndex,
       "tnCNLinkIpAddress": tnCNLinkIpAddress,
       "tnCNLinkSubnetMask": tnCNLinkSubnetMask,
       "tnCNLinkHelloInterval": tnCNLinkHelloInterval,
       "tnCNLinkRtrDeadInterval": tnCNLinkRtrDeadInterval,
       "tnCNLinkTeMetric": tnCNLinkTeMetric,
       "tnCNLinkOspfRoutingState": tnCNLinkOspfRoutingState,
       "tnCNLinkConfigIfType": tnCNLinkConfigIfType,
       "tnCNLinkConfigRtrPriority": tnCNLinkConfigRtrPriority,
       "tnCNLinkEquipOperStatus": tnCNLinkEquipOperStatus,
       "tnCNLinkDhcpEnabled": tnCNLinkDhcpEnabled,
       "tnCNLinkSpeed": tnCNLinkSpeed,
       "tnCNLinkDuplex": tnCNLinkDuplex,
       "tnCNLinkProxyArp": tnCNLinkProxyArp,
       "tnCNLinkDHCPServer": tnCNLinkDHCPServer,
       "tnCNLinkDHCPRange": tnCNLinkDHCPRange,
       "tnCNLinkAdjState": tnCNLinkAdjState,
       "tnCNLinkOscMode": tnCNLinkOscMode,
       "tnCNLinkDHCPDfltGtwy": tnCNLinkDHCPDfltGtwy,
       "tnCNLinkCitAutoStateCtrl": tnCNLinkCitAutoStateCtrl,
       "tnCNLinkAutoStateSourceIP": tnCNLinkAutoStateSourceIP,
       "tnCNLinkSourceLossCount": tnCNLinkSourceLossCount,
       "tnCNLinkSourceIPCheckInterval": tnCNLinkSourceIPCheckInterval,
       "tnCNLinkOspfAuthentType": tnCNLinkOspfAuthentType,
       "tnCNLinkOspfAuthKey": tnCNLinkOspfAuthKey,
       "tnCNLinkOspfAuthKeyId": tnCNLinkOspfAuthKeyId,
       "tnCNLinkTdmxDcnConf": tnCNLinkTdmxDcnConf,
       "tnCNLinkInetAddressType": tnCNLinkInetAddressType,
       "tnCNLinkInetAddress": tnCNLinkInetAddress,
       "tnCNLinkPrefixLength": tnCNLinkPrefixLength,
       "tnCNLinkAutoStateSourceInetAddressType": tnCNLinkAutoStateSourceInetAddressType,
       "tnCNLinkAutoStateSourceInetAddress": tnCNLinkAutoStateSourceInetAddress,
       "tnCNLinkDhcpv6Enabled": tnCNLinkDhcpv6Enabled,
       "tnCNLinkDHCPv6Range": tnCNLinkDHCPv6Range,
       "tnCNLinkDHCPClient": tnCNLinkDHCPClient,
       "tnCNLinkDHCPv6Client": tnCNLinkDHCPv6Client,
       "tnCNLinkDHCPClientDfltGtwy": tnCNLinkDHCPClientDfltGtwy,
       "tnCNLinkEtherPortIpV6SLAAC": tnCNLinkEtherPortIpV6SLAAC,
       "tnCNLinkOspfRetransint": tnCNLinkOspfRetransint,
       "tnCNLinkOspfv3AdjStateId": tnCNLinkOspfv3AdjStateId,
       "tnCNLinkOspfNeighborRouterIp": tnCNLinkOspfNeighborRouterIp,
       "tnCNLinkOspfv3NeighborRouterIp": tnCNLinkOspfv3NeighborRouterIp,
       "tnCNLinkOspfNeighborIp": tnCNLinkOspfNeighborIp,
       "tnCNLinkOspfv3NeighborInetAddress": tnCNLinkOspfv3NeighborInetAddress,
       "tnCNLinkRole": tnCNLinkRole,
       "tnCNLinkDHCPServerIPv6SLAAC": tnCNLinkDHCPServerIPv6SLAAC,
       "tnCNLinkRouterAdvAutonomousFlag": tnCNLinkRouterAdvAutonomousFlag,
       "tnCNLinkRouterAdvDefaultLifeTime": tnCNLinkRouterAdvDefaultLifeTime,
       "tnCNLinkRouterAdvDefaultPreference": tnCNLinkRouterAdvDefaultPreference,
       "tnCNLinkRouterAdvMaxRtrAdvInterval": tnCNLinkRouterAdvMaxRtrAdvInterval,
       "tnCNLinkRouterAdvManagedFlag": tnCNLinkRouterAdvManagedFlag,
       "tnCNLinkRouterAdvOtherConfigFlag": tnCNLinkRouterAdvOtherConfigFlag,
       "tnCNLinkRouterAdvPreferredLifeTime": tnCNLinkRouterAdvPreferredLifeTime,
       "tnCNLinkRouterAdvSendAdvertState": tnCNLinkRouterAdvSendAdvertState,
       "tnCNLinkRouterAdvValidLifeTime": tnCNLinkRouterAdvValidLifeTime,
       "tnCNLinkAutoStateType": tnCNLinkAutoStateType,
       "tnCNLinkAutoStateStatus": tnCNLinkAutoStateStatus,
       "tnCNLinkOspfv3HelloInterval": tnCNLinkOspfv3HelloInterval,
       "tnCNLinkOspfv3TeMetric": tnCNLinkOspfv3TeMetric,
       "tnCNLinkOspfv3Retransint": tnCNLinkOspfv3Retransint,
       "tnCNLinkOspfv3RtrDeadInterval": tnCNLinkOspfv3RtrDeadInterval,
       "tnCNLinkOspfv3ConfigRtrPriority": tnCNLinkOspfv3ConfigRtrPriority,
       "tnCNLinkOspfv3RoutingState": tnCNLinkOspfv3RoutingState,
       "tnCNLinkOspfOscRoutingState": tnCNLinkOspfOscRoutingState,
       "tnCNLinkOspfv6OscRoutingState": tnCNLinkOspfv6OscRoutingState,
       "tnCNLinkDHCPBootFileName": tnCNLinkDHCPBootFileName,
       "tnCNLinkDHCPClassName": tnCNLinkDHCPClassName,
       "tnCNLinkViaChannelTable": tnCNLinkViaChannelTable,
       "tnCNLinkViaChannelEntry": tnCNLinkViaChannelEntry,
       "tnPortIndex": tnPortIndex,
       "tnChannelIndex": tnChannelIndex,
       "tnCNLinkViaChannelIfIndex": tnCNLinkViaChannelIfIndex,
       "tnDataNetworkLink": tnDataNetworkLink,
       "tnL1TrafficParamTable": tnL1TrafficParamTable,
       "tnL1TrafficParamEntry": tnL1TrafficParamEntry,
       "tnL1TrafficParamPerHopBehaviour": tnL1TrafficParamPerHopBehaviour,
       "tnL1TrafficParamBookingFactor": tnL1TrafficParamBookingFactor,
       "tnL1TrafficParamMaximumLoad": tnL1TrafficParamMaximumLoad,
       "tnL1TrafficParamPMF": tnL1TrafficParamPMF,
       "tnL1TrafficParamAvailableBandwidth": tnL1TrafficParamAvailableBandwidth,
       "tnIpRoute": tnIpRoute,
       "tnIpStaticRouteTable": tnIpStaticRouteTable,
       "tnIpStaticRouteEntry": tnIpStaticRouteEntry,
       "tnIpStaticRouteDest": tnIpStaticRouteDest,
       "tnIpStaticRouteMask": tnIpStaticRouteMask,
       "tnIpStaticRouteTos": tnIpStaticRouteTos,
       "tnIpStaticRouteNextHop": tnIpStaticRouteNextHop,
       "tnIpStaticRouteMetric": tnIpStaticRouteMetric,
       "tnIpStaticRouteWithRedistribution": tnIpStaticRouteWithRedistribution,
       "tnIpStaticRouteRowStatus": tnIpStaticRouteRowStatus,
       "tnIpCidrRouteTable": tnIpCidrRouteTable,
       "tnIpCidrRouteEntry": tnIpCidrRouteEntry,
       "tnIpCidrRouteWithRedistribution": tnIpCidrRouteWithRedistribution,
       "tnIpRouteGlobal": tnIpRouteGlobal,
       "tnIpStaticRouteRedistributeMetricType": tnIpStaticRouteRedistributeMetricType,
       "tnIpStaticRouteRedistributeMetric": tnIpStaticRouteRedistributeMetric,
       "tnIpDefaultRouteRedistributeMetricType": tnIpDefaultRouteRedistributeMetricType,
       "tnIpDefaultRouteRedistributeMetric": tnIpDefaultRouteRedistributeMetric,
       "tnIpOspfAreaNumberPPPId": tnIpOspfAreaNumberPPPId,
       "tnIpOspfRouterId": tnIpOspfRouterId,
       "tnIpDefaultRouteRedistributeBgpToOspfMetricType": tnIpDefaultRouteRedistributeBgpToOspfMetricType,
       "tnIpDefaultRouteRedistributeBgpToOspfMetric": tnIpDefaultRouteRedistributeBgpToOspfMetric,
       "tnIpDefaultRouteRedistributeBgpToOspfMode": tnIpDefaultRouteRedistributeBgpToOspfMode,
       "tnIpDefaultRouteRedistributeKernelToOspfMetricType": tnIpDefaultRouteRedistributeKernelToOspfMetricType,
       "tnIpDefaultRouteRedistributeKernelToOspfMetric": tnIpDefaultRouteRedistributeKernelToOspfMetric,
       "tnIpDefaultRouteRedistributeKernelToOspfStatus": tnIpDefaultRouteRedistributeKernelToOspfStatus,
       "tnIpStaticRouteRedistributeBgpMetric": tnIpStaticRouteRedistributeBgpMetric,
       "tnIpOspfV3AreaNumberPPPId": tnIpOspfV3AreaNumberPPPId,
       "tnIpDefaultRouteRedistributeOspfToBgpMode": tnIpDefaultRouteRedistributeOspfToBgpMode,
       "tnIpDefaultRouteRedistributeOspfToBgpMetric": tnIpDefaultRouteRedistributeOspfToBgpMetric,
       "tnIpNonDefaultRouteOspfToBgpCommTagTable": tnIpNonDefaultRouteOspfToBgpCommTagTable,
       "tnIpNonDefaultRouteOspfToBgpCommTagEntry": tnIpNonDefaultRouteOspfToBgpCommTagEntry,
       "tnIpNonDefaultRouteOspfToBgpCommTagIndex": tnIpNonDefaultRouteOspfToBgpCommTagIndex,
       "tnIpNonDefaultRouteOspfToBgpCommTagRowStatus": tnIpNonDefaultRouteOspfToBgpCommTagRowStatus,
       "tnIpNonDefaultRouteOspfToBgpCommTag": tnIpNonDefaultRouteOspfToBgpCommTag,
       "tnIpNonDefaultRedistBgpToOspfRuleTable": tnIpNonDefaultRedistBgpToOspfRuleTable,
       "tnIpNonDefaultRedistBgpToOspfRuleEntry": tnIpNonDefaultRedistBgpToOspfRuleEntry,
       "tnIpNonDefaultRedistBgpToOspfRuleIndex": tnIpNonDefaultRedistBgpToOspfRuleIndex,
       "tnIpNonDefaultRedistBgpToOspfRuleRowStatus": tnIpNonDefaultRedistBgpToOspfRuleRowStatus,
       "tnIpNonDefaultRedistBgpToOspfRuleOspfTag": tnIpNonDefaultRedistBgpToOspfRuleOspfTag,
       "tnIpNonDefaultRedistBgpToOspfRuleMode": tnIpNonDefaultRedistBgpToOspfRuleMode,
       "tnIpNonDefaultRedistBgpToOspfRuleMetric": tnIpNonDefaultRedistBgpToOspfRuleMetric,
       "tnIpNonDefaultRedistBgpToOspfRuleMetricType": tnIpNonDefaultRedistBgpToOspfRuleMetricType,
       "tnSharedRiskGroupObjs": tnSharedRiskGroupObjs,
       "tnL1NetworkLink": tnL1NetworkLink,
       "tnL1Hop": tnL1Hop,
       "tnL1Fiber": tnL1Fiber,
       "tnL1Conduit": tnL1Conduit,
       "tnL1Protection": tnL1Protection,
       "tnApsGroupTable": tnApsGroupTable,
       "tnApsGroupEntry": tnApsGroupEntry,
       "tnApsGroupId": tnApsGroupId,
       "tnApsGroupRowStatus": tnApsGroupRowStatus,
       "tnApsGroupDescr": tnApsGroupDescr,
       "tnApsGroupMode": tnApsGroupMode,
       "tnApsGroupRevert": tnApsGroupRevert,
       "tnApsGroupDirection": tnApsGroupDirection,
       "tnApsGroupExtraTraffic": tnApsGroupExtraTraffic,
       "tnApsGroupWaitToRestore": tnApsGroupWaitToRestore,
       "tnApsGroupK1K2Rcv": tnApsGroupK1K2Rcv,
       "tnApsGroupK1K2Trans": tnApsGroupK1K2Trans,
       "tnApsGroupCurrentStatus": tnApsGroupCurrentStatus,
       "tnApsGroupModeMismatches": tnApsGroupModeMismatches,
       "tnApsGroupChannelMismatches": tnApsGroupChannelMismatches,
       "tnApsGroupPSBFs": tnApsGroupPSBFs,
       "tnApsGroupFEPLFs": tnApsGroupFEPLFs,
       "tnApsGroupSwitchedIfIndex": tnApsGroupSwitchedIfIndex,
       "tnApsGroupMembers": tnApsGroupMembers,
       "tnApsGroupSdEnable": tnApsGroupSdEnable,
       "tnApsHoldOffTimer": tnApsHoldOffTimer,
       "tnApsMemberTable": tnApsMemberTable,
       "tnApsMemberEntry": tnApsMemberEntry,
       "tnApsMemberIfIndex": tnApsMemberIfIndex,
       "tnApsMemberRowStatus": tnApsMemberRowStatus,
       "tnApsMemberConfigNumber": tnApsMemberConfigNumber,
       "tnApsMemberSwitch": tnApsMemberSwitch,
       "tnApsMemberCurrentStatus": tnApsMemberCurrentStatus,
       "tnPackApsGroupTable": tnPackApsGroupTable,
       "tnPackApsGroupEntry": tnPackApsGroupEntry,
       "tnPackApsGroupID": tnPackApsGroupID,
       "tnPackApsGroupRowStatus": tnPackApsGroupRowStatus,
       "tnPackApsGroupWorkIfIndex": tnPackApsGroupWorkIfIndex,
       "tnPackApsGroupProtIfIndex": tnPackApsGroupProtIfIndex,
       "tnPackApsGroupDescr": tnPackApsGroupDescr,
       "tnPackApsGroupRevert": tnPackApsGroupRevert,
       "tnPackApsGroupDirection": tnPackApsGroupDirection,
       "tnPackApsGroupWaitToRestore": tnPackApsGroupWaitToRestore,
       "tnPackApsGroupHoldOffTimer": tnPackApsGroupHoldOffTimer,
       "tnPackApsGroupSwitchCmd": tnPackApsGroupSwitchCmd,
       "tnPackApsGroupActSide": tnPackApsGroupActSide,
       "tnPackApsGroupCurrentStatus": tnPackApsGroupCurrentStatus,
       "tnPackApsGroupWorkStatus": tnPackApsGroupWorkStatus,
       "tnPackApsGroupProtStatus": tnPackApsGroupProtStatus,
       "tnPackApsGroupPortFailEnable": tnPackApsGroupPortFailEnable,
       "tnIpTunnel": tnIpTunnel,
       "tnControlNetworkMap": tnControlNetworkMap,
       "tnControlNetworkMapTable": tnControlNetworkMapTable,
       "tnControlNetworkMapEntry": tnControlNetworkMapEntry,
       "tnCNMapTableIndex": tnCNMapTableIndex,
       "tnCNMapIpAddress": tnCNMapIpAddress,
       "tnCNMapNeName": tnCNMapNeName,
       "tnCNMapSoftwareRelease": tnCNMapSoftwareRelease,
       "tnCNMapIpv6InetAddress": tnCNMapIpv6InetAddress,
       "tnCNMapIpv4Address": tnCNMapIpv4Address,
       "tnNetworkInterface": tnNetworkInterface,
       "tnNetIfTable": tnNetIfTable,
       "tnNetIfEntry": tnNetIfEntry,
       "tnNetIfIndex": tnNetIfIndex,
       "tnNetIfTypeOfOperation": tnNetIfTypeOfOperation,
       "tnNetIfStatus": tnNetIfStatus,
       "tnNetIfPacketType": tnNetIfPacketType,
       "tnNetIfMtu": tnNetIfMtu,
       "tnNetIfHelloInterval": tnNetIfHelloInterval,
       "tnNetIfRtrDeadInterval": tnNetIfRtrDeadInterval,
       "tnNetIfMetric": tnNetIfMetric,
       "tnNetIfOspfAuthentType": tnNetIfOspfAuthentType,
       "tnNetIfOspfAuthKey": tnNetIfOspfAuthKey,
       "tnNetIfOspfAuthKeyId": tnNetIfOspfAuthKeyId,
       "tnNetIfCnLinkAdjState": tnNetIfCnLinkAdjState,
       "tnNetIfMtuNeg": tnNetIfMtuNeg,
       "tnNetIfOSPFAreaNumberId": tnNetIfOSPFAreaNumberId,
       "tnNetIfOspfRetransint": tnNetIfOspfRetransint,
       "tnNetIfOspfv3AdjStateId": tnNetIfOspfv3AdjStateId,
       "tnNetIfOspfNeighborRouterIp": tnNetIfOspfNeighborRouterIp,
       "tnNetIfOspfv3NeighborRouterIp": tnNetIfOspfv3NeighborRouterIp,
       "tnNetIfOspfNeighborIp": tnNetIfOspfNeighborIp,
       "tnNetIfOspfv3NeighborInetAddress": tnNetIfOspfv3NeighborInetAddress,
       "tnNetIfIPv6LinkLocalInetAddress": tnNetIfIPv6LinkLocalInetAddress,
       "tnNetIfLcpEchoInterval": tnNetIfLcpEchoInterval,
       "tnNetIfLcpEchoFailure": tnNetIfLcpEchoFailure,
       "tnNetIfOspfStatus": tnNetIfOspfStatus,
       "tnNetIfOspfv3AreaNumberId": tnNetIfOspfv3AreaNumberId,
       "tnNetIfOspfv3HelloInterval": tnNetIfOspfv3HelloInterval,
       "tnNetIfOspfv3Metric": tnNetIfOspfv3Metric,
       "tnNetIfOspfv3Retransint": tnNetIfOspfv3Retransint,
       "tnNetIfOspfv3RtrDeadInterval": tnNetIfOspfv3RtrDeadInterval,
       "tnNetIfOspfv3ConfigRtrPriority": tnNetIfOspfv3ConfigRtrPriority,
       "tnNetIfOspfv3Status": tnNetIfOspfv3Status,
       "tnNetIfFacilityTable": tnNetIfFacilityTable,
       "tnNetIfFacilityEntry": tnNetIfFacilityEntry,
       "tnNetIfFacilityIfIndex": tnNetIfFacilityIfIndex,
       "tnNetIfFacilityIfIndexLo": tnNetIfFacilityIfIndexLo,
       "tnNetIfFacilityTypeOfOperation": tnNetIfFacilityTypeOfOperation,
       "tnNetIfFacilityEccChanType": tnNetIfFacilityEccChanType,
       "tnStaticRoute": tnStaticRoute,
       "tnStaticRouteTable": tnStaticRouteTable,
       "tnStaticRouteEntry": tnStaticRouteEntry,
       "tnStaticRouteDestInetAddressType": tnStaticRouteDestInetAddressType,
       "tnStaticRouteDestInetAddress": tnStaticRouteDestInetAddress,
       "tnStaticRouteMaskPrefix": tnStaticRouteMaskPrefix,
       "tnStaticRouteTos": tnStaticRouteTos,
       "tnStaticRouteNextHopType": tnStaticRouteNextHopType,
       "tnStaticRouteNextHop": tnStaticRouteNextHop,
       "tnStaticRouteMetric": tnStaticRouteMetric,
       "tnStaticRouteWithRedistribution": tnStaticRouteWithRedistribution,
       "tnStaticRouteRowStatus": tnStaticRouteRowStatus,
       "tnStaticRouteIdentifier": tnStaticRouteIdentifier,
       "tnStaticRouteWithBgpDistribution": tnStaticRouteWithBgpDistribution,
       "tnEthernetInterface": tnEthernetInterface,
       "tnEthIfTable": tnEthIfTable,
       "tnEthIfEntry": tnEthIfEntry,
       "tnEthIfIndex": tnEthIfIndex,
       "tnEthIfTypeOfOperation": tnEthIfTypeOfOperation,
       "tnEthIfStatus": tnEthIfStatus,
       "tnEthIfHelloInterval": tnEthIfHelloInterval,
       "tnEthIfRtrDeadInterval": tnEthIfRtrDeadInterval,
       "tnEthIfMetric": tnEthIfMetric,
       "tnEthIfOspfAuthentType": tnEthIfOspfAuthentType,
       "tnEthIfOspfAuthKey": tnEthIfOspfAuthKey,
       "tnEthIfOspfAuthKeyId": tnEthIfOspfAuthKeyId,
       "tnEthIfOSPFAreaNumberId": tnEthIfOSPFAreaNumberId,
       "tnEthIfProxyArp": tnEthIfProxyArp,
       "tnEthIfOspfRouteState": tnEthIfOspfRouteState,
       "tnEthIfDhcpEnabled": tnEthIfDhcpEnabled,
       "tnEthIfDHCPRange": tnEthIfDHCPRange,
       "tnEthIfDHCPDfltGtwy": tnEthIfDHCPDfltGtwy,
       "tnEthIfDhcpv6Enabled": tnEthIfDhcpv6Enabled,
       "tnEthIfDHCPv6Range": tnEthIfDHCPv6Range,
       "tnEthIfDHCPClient": tnEthIfDHCPClient,
       "tnEthIfDHCPClientDfltGtwy": tnEthIfDHCPClientDfltGtwy,
       "tnEthIfIpV6SLAAC": tnEthIfIpV6SLAAC,
       "tnEthIfIpAddress": tnEthIfIpAddress,
       "tnEthIfSubnetMask": tnEthIfSubnetMask,
       "tnEthIfInetAddressType": tnEthIfInetAddressType,
       "tnEthIfInetAddress": tnEthIfInetAddress,
       "tnEthIfPrefixLength": tnEthIfPrefixLength,
       "tnEthIfDescription": tnEthIfDescription,
       "tnEthIfOspfAdjStateId": tnEthIfOspfAdjStateId,
       "tnEthIfOspfDrPriorityId": tnEthIfOspfDrPriorityId,
       "tnEthIfOspfRetransint": tnEthIfOspfRetransint,
       "tnEthIfOspfv3AdjStateId": tnEthIfOspfv3AdjStateId,
       "tnEthIfOperStatus": tnEthIfOperStatus,
       "tnEthIfAlmProfName": tnEthIfAlmProfName,
       "tnEthIfDHCPServerIPv6SLAAC": tnEthIfDHCPServerIPv6SLAAC,
       "tnEthIfRouterAdvAutonomousFlag": tnEthIfRouterAdvAutonomousFlag,
       "tnEthIfRouterAdvDefaultLifeTime": tnEthIfRouterAdvDefaultLifeTime,
       "tnEthIfRouterAdvDefaultPreference": tnEthIfRouterAdvDefaultPreference,
       "tnEthIfRouterAdvMaxRtrAdvInterval": tnEthIfRouterAdvMaxRtrAdvInterval,
       "tnEthIfRouterAdvManagedFlag": tnEthIfRouterAdvManagedFlag,
       "tnEthIfRouterAdvOtherConfigFlag": tnEthIfRouterAdvOtherConfigFlag,
       "tnEthIfRouterAdvPreferredLifeTime": tnEthIfRouterAdvPreferredLifeTime,
       "tnEthIfRouterAdvSendAdvertState": tnEthIfRouterAdvSendAdvertState,
       "tnEthIfRouterAdvValidLifeTime": tnEthIfRouterAdvValidLifeTime,
       "tnEthIfOspfv3AreaNumberId": tnEthIfOspfv3AreaNumberId,
       "tnEthIfOspfv3HelloInterval": tnEthIfOspfv3HelloInterval,
       "tnEthIfOspfv3Metric": tnEthIfOspfv3Metric,
       "tnEthIfOspfv3Retransint": tnEthIfOspfv3Retransint,
       "tnEthIfOspfv3RtrDeadInterval": tnEthIfOspfv3RtrDeadInterval,
       "tnEthIfOspfv3DrPriorityId": tnEthIfOspfv3DrPriorityId,
       "tnEthIfOspfv3RouteState": tnEthIfOspfv3RouteState,
       "tnEthIfInterfaceTable": tnEthIfInterfaceTable,
       "tnEthIfInterfaceEntry": tnEthIfInterfaceEntry,
       "tnEthIfInterfaceIfIndex": tnEthIfInterfaceIfIndex,
       "tnEthIfInterfaceVlanId": tnEthIfInterfaceVlanId,
       "tnEthIfInterfaceTypeOfOperation": tnEthIfInterfaceTypeOfOperation,
       "tnDhcpRelay": tnDhcpRelay,
       "tnDhcpRelayRecordTable": tnDhcpRelayRecordTable,
       "tnDhcpRelayRecordEntry": tnDhcpRelayRecordEntry,
       "tnDhcpRelayRecordIndex1": tnDhcpRelayRecordIndex1,
       "tnDhcpRelayRecordIndex2": tnDhcpRelayRecordIndex2,
       "tnDhcpRelayRecordInetAddressType": tnDhcpRelayRecordInetAddressType,
       "tnDhcpRelayRecordInetAddress": tnDhcpRelayRecordInetAddress,
       "tnDhcpRelayRecordRowStatus": tnDhcpRelayRecordRowStatus,
       "tnDhcpRelayRecordRailIdDescr": tnDhcpRelayRecordRailIdDescr,
       "tnDhcpServer": tnDhcpServer,
       "tnDhcpServerTable": tnDhcpServerTable,
       "tnDhcpServerEntry": tnDhcpServerEntry,
       "tnDhcpServerInetAddressType": tnDhcpServerInetAddressType,
       "tnDhcpServerInetAddress": tnDhcpServerInetAddress,
       "tnDhcpServerSerialno": tnDhcpServerSerialno,
       "tnDhcpServerMacAddress": tnDhcpServerMacAddress,
       "tnDhcpServerPort": tnDhcpServerPort,
       "tnDhcpServerRowStatus": tnDhcpServerRowStatus}
)
