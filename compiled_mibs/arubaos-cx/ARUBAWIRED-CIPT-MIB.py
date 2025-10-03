# SNMP MIB module (ARUBAWIRED-CIPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-CIPT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:04 2025
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

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

arubaWiredCiptMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12)
)
if mibBuilder.loadTexts:
    arubaWiredCiptMIB.setRevisions(
        ("2020-02-07 00:00",)
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

_ArubaWiredCiptConfig_ObjectIdentity = ObjectIdentity
arubaWiredCiptConfig = _ArubaWiredCiptConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1)
)
_ArubaWiredCiptGlobalConfig_ObjectIdentity = ObjectIdentity
arubaWiredCiptGlobalConfig = _ArubaWiredCiptGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 1)
)


class _ArubaWiredCiptEnable_Type(TruthValue):
    """Custom type arubaWiredCiptEnable based on TruthValue"""
    defaultValue = 2


_ArubaWiredCiptEnable_Type.__name__ = "TruthValue"
_ArubaWiredCiptEnable_Object = MibScalar
arubaWiredCiptEnable = _ArubaWiredCiptEnable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 1, 1),
    _ArubaWiredCiptEnable_Type()
)
arubaWiredCiptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredCiptEnable.setStatus("current")


class _ArubaWiredCiptProbeEnable_Type(TruthValue):
    """Custom type arubaWiredCiptProbeEnable based on TruthValue"""
    defaultValue = 1


_ArubaWiredCiptProbeEnable_Type.__name__ = "TruthValue"
_ArubaWiredCiptProbeEnable_Object = MibScalar
arubaWiredCiptProbeEnable = _ArubaWiredCiptProbeEnable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 1, 2),
    _ArubaWiredCiptProbeEnable_Type()
)
arubaWiredCiptProbeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredCiptProbeEnable.setStatus("current")
_ArubaWiredCiptVlanConfig_ObjectIdentity = ObjectIdentity
arubaWiredCiptVlanConfig = _ArubaWiredCiptVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 2)
)
_ArubaWiredCiptVidList_Type = VidList
_ArubaWiredCiptVidList_Object = MibScalar
arubaWiredCiptVidList = _ArubaWiredCiptVidList_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 2, 1),
    _ArubaWiredCiptVidList_Type()
)
arubaWiredCiptVidList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredCiptVidList.setStatus("current")
_ArubaWiredCiptPortConfig_ObjectIdentity = ObjectIdentity
arubaWiredCiptPortConfig = _ArubaWiredCiptPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 3)
)
_ArubaWiredCiptPortTable_Object = MibTable
arubaWiredCiptPortTable = _ArubaWiredCiptPortTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 3, 1)
)
if mibBuilder.loadTexts:
    arubaWiredCiptPortTable.setStatus("current")
_ArubaWiredCiptPortEntry_Object = MibTableRow
arubaWiredCiptPortEntry = _ArubaWiredCiptPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 3, 1, 1)
)
arubaWiredCiptPortEntry.setIndexNames(
    (0, "ARUBAWIRED-CIPT-MIB", "arubaWiredCiptPortIfIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredCiptPortEntry.setStatus("current")
_ArubaWiredCiptPortIfIndex_Type = InterfaceIndex
_ArubaWiredCiptPortIfIndex_Object = MibTableColumn
arubaWiredCiptPortIfIndex = _ArubaWiredCiptPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 3, 1, 1, 1),
    _ArubaWiredCiptPortIfIndex_Type()
)
arubaWiredCiptPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredCiptPortIfIndex.setStatus("current")


class _ArubaWiredCiptPortEnable_Type(Integer32):
    """Custom type arubaWiredCiptPortEnable based on Integer32"""
    defaultValue = 2

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
          ("enable", 1),
          ("auto", 2))
    )


_ArubaWiredCiptPortEnable_Type.__name__ = "Integer32"
_ArubaWiredCiptPortEnable_Object = MibTableColumn
arubaWiredCiptPortEnable = _ArubaWiredCiptPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 3, 1, 1, 2),
    _ArubaWiredCiptPortEnable_Type()
)
arubaWiredCiptPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredCiptPortEnable.setStatus("current")


class _ArubaWiredCiptPortUpdateInterval_Type(Unsigned32):
    """Custom type arubaWiredCiptPortUpdateInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 28800),
    )


_ArubaWiredCiptPortUpdateInterval_Type.__name__ = "Unsigned32"
_ArubaWiredCiptPortUpdateInterval_Object = MibTableColumn
arubaWiredCiptPortUpdateInterval = _ArubaWiredCiptPortUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 3, 1, 1, 3),
    _ArubaWiredCiptPortUpdateInterval_Type()
)
arubaWiredCiptPortUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredCiptPortUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredCiptPortUpdateInterval.setUnits("seconds")


class _ArubaWiredCiptPortClientLimit_Type(Unsigned32):
    """Custom type arubaWiredCiptPortClientLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_ArubaWiredCiptPortClientLimit_Type.__name__ = "Unsigned32"
_ArubaWiredCiptPortClientLimit_Object = MibTableColumn
arubaWiredCiptPortClientLimit = _ArubaWiredCiptPortClientLimit_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 1, 3, 1, 1, 4),
    _ArubaWiredCiptPortClientLimit_Type()
)
arubaWiredCiptPortClientLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredCiptPortClientLimit.setStatus("current")
_ArubaWiredCiptClients_ObjectIdentity = ObjectIdentity
arubaWiredCiptClients = _ArubaWiredCiptClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2)
)
_ArubaWiredCiptTrackedClients_ObjectIdentity = ObjectIdentity
arubaWiredCiptTrackedClients = _ArubaWiredCiptTrackedClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1)
)
_ArubaWiredCiptClientTable_Object = MibTable
arubaWiredCiptClientTable = _ArubaWiredCiptClientTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredCiptClientTable.setStatus("current")
_ArubaWiredCiptClientEntry_Object = MibTableRow
arubaWiredCiptClientEntry = _ArubaWiredCiptClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1, 1, 1)
)
arubaWiredCiptClientEntry.setIndexNames(
    (0, "ARUBAWIRED-CIPT-MIB", "arubaWiredCiptClientMacAddress"),
    (0, "ARUBAWIRED-CIPT-MIB", "arubaWiredCiptClientVlanId"),
    (0, "ARUBAWIRED-CIPT-MIB", "arubaWiredCiptClientIpIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredCiptClientEntry.setStatus("current")
_ArubaWiredCiptClientMacAddress_Type = MacAddress
_ArubaWiredCiptClientMacAddress_Object = MibTableColumn
arubaWiredCiptClientMacAddress = _ArubaWiredCiptClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1, 1, 1, 1),
    _ArubaWiredCiptClientMacAddress_Type()
)
arubaWiredCiptClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredCiptClientMacAddress.setStatus("current")
_ArubaWiredCiptClientVlanId_Type = VlanIndex
_ArubaWiredCiptClientVlanId_Object = MibTableColumn
arubaWiredCiptClientVlanId = _ArubaWiredCiptClientVlanId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1, 1, 1, 2),
    _ArubaWiredCiptClientVlanId_Type()
)
arubaWiredCiptClientVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredCiptClientVlanId.setStatus("current")


class _ArubaWiredCiptClientIpIndex_Type(Unsigned32):
    """Custom type arubaWiredCiptClientIpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ArubaWiredCiptClientIpIndex_Type.__name__ = "Unsigned32"
_ArubaWiredCiptClientIpIndex_Object = MibTableColumn
arubaWiredCiptClientIpIndex = _ArubaWiredCiptClientIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1, 1, 1, 3),
    _ArubaWiredCiptClientIpIndex_Type()
)
arubaWiredCiptClientIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredCiptClientIpIndex.setStatus("current")
_ArubaWiredCiptClientIpAddrType_Type = InetAddressType
_ArubaWiredCiptClientIpAddrType_Object = MibTableColumn
arubaWiredCiptClientIpAddrType = _ArubaWiredCiptClientIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1, 1, 1, 4),
    _ArubaWiredCiptClientIpAddrType_Type()
)
arubaWiredCiptClientIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredCiptClientIpAddrType.setStatus("current")
_ArubaWiredCiptClientIpAddress_Type = InetAddress
_ArubaWiredCiptClientIpAddress_Object = MibTableColumn
arubaWiredCiptClientIpAddress = _ArubaWiredCiptClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1, 1, 1, 5),
    _ArubaWiredCiptClientIpAddress_Type()
)
arubaWiredCiptClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredCiptClientIpAddress.setStatus("current")
_ArubaWiredCiptClientPortIfIndex_Type = InterfaceIndex
_ArubaWiredCiptClientPortIfIndex_Object = MibTableColumn
arubaWiredCiptClientPortIfIndex = _ArubaWiredCiptClientPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 2, 1, 1, 1, 6),
    _ArubaWiredCiptClientPortIfIndex_Type()
)
arubaWiredCiptClientPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredCiptClientPortIfIndex.setStatus("current")
_ArubaWiredCiptConformance_ObjectIdentity = ObjectIdentity
arubaWiredCiptConformance = _ArubaWiredCiptConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 3)
)
_ArubaWiredCiptGroups_ObjectIdentity = ObjectIdentity
arubaWiredCiptGroups = _ArubaWiredCiptGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 3, 1)
)
_ArubaWiredCiptCompliances_ObjectIdentity = ObjectIdentity
arubaWiredCiptCompliances = _ArubaWiredCiptCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 3, 2)
)

# Managed Objects groups

arubaWiredCiptConfigGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 3, 1, 1)
)
arubaWiredCiptConfigGlobalGroup.setObjects(
      *(("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptEnable"),
        ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptProbeEnable"))
)
if mibBuilder.loadTexts:
    arubaWiredCiptConfigGlobalGroup.setStatus("current")

arubaWiredCiptVlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 3, 1, 2)
)
arubaWiredCiptVlanConfigGroup.setObjects(
    ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptVidList")
)
if mibBuilder.loadTexts:
    arubaWiredCiptVlanConfigGroup.setStatus("current")

arubaWiredCiptPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 3, 1, 3)
)
arubaWiredCiptPortConfigGroup.setObjects(
      *(("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptPortEnable"),
        ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptPortUpdateInterval"),
        ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptPortClientLimit"))
)
if mibBuilder.loadTexts:
    arubaWiredCiptPortConfigGroup.setStatus("current")

arubaWiredCiptTrackedClientsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 3, 1, 4)
)
arubaWiredCiptTrackedClientsGroup.setObjects(
      *(("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptClientIpAddrType"),
        ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptClientIpAddress"),
        ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptClientPortIfIndex"))
)
if mibBuilder.loadTexts:
    arubaWiredCiptTrackedClientsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arubaWiredCiptCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12, 3, 2, 1)
)
arubaWiredCiptCompliance.setObjects(
      *(("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptConfigGlobalGroup"),
        ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptVlanConfigGroup"),
        ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptPortConfigGroup"),
        ("ARUBAWIRED-CIPT-MIB", "arubaWiredCiptTrackedClientsGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredCiptCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-CIPT-MIB",
    **{"VidList": VidList,
       "arubaWiredCiptMIB": arubaWiredCiptMIB,
       "arubaWiredCiptConfig": arubaWiredCiptConfig,
       "arubaWiredCiptGlobalConfig": arubaWiredCiptGlobalConfig,
       "arubaWiredCiptEnable": arubaWiredCiptEnable,
       "arubaWiredCiptProbeEnable": arubaWiredCiptProbeEnable,
       "arubaWiredCiptVlanConfig": arubaWiredCiptVlanConfig,
       "arubaWiredCiptVidList": arubaWiredCiptVidList,
       "arubaWiredCiptPortConfig": arubaWiredCiptPortConfig,
       "arubaWiredCiptPortTable": arubaWiredCiptPortTable,
       "arubaWiredCiptPortEntry": arubaWiredCiptPortEntry,
       "arubaWiredCiptPortIfIndex": arubaWiredCiptPortIfIndex,
       "arubaWiredCiptPortEnable": arubaWiredCiptPortEnable,
       "arubaWiredCiptPortUpdateInterval": arubaWiredCiptPortUpdateInterval,
       "arubaWiredCiptPortClientLimit": arubaWiredCiptPortClientLimit,
       "arubaWiredCiptClients": arubaWiredCiptClients,
       "arubaWiredCiptTrackedClients": arubaWiredCiptTrackedClients,
       "arubaWiredCiptClientTable": arubaWiredCiptClientTable,
       "arubaWiredCiptClientEntry": arubaWiredCiptClientEntry,
       "arubaWiredCiptClientMacAddress": arubaWiredCiptClientMacAddress,
       "arubaWiredCiptClientVlanId": arubaWiredCiptClientVlanId,
       "arubaWiredCiptClientIpIndex": arubaWiredCiptClientIpIndex,
       "arubaWiredCiptClientIpAddrType": arubaWiredCiptClientIpAddrType,
       "arubaWiredCiptClientIpAddress": arubaWiredCiptClientIpAddress,
       "arubaWiredCiptClientPortIfIndex": arubaWiredCiptClientPortIfIndex,
       "arubaWiredCiptConformance": arubaWiredCiptConformance,
       "arubaWiredCiptGroups": arubaWiredCiptGroups,
       "arubaWiredCiptConfigGlobalGroup": arubaWiredCiptConfigGlobalGroup,
       "arubaWiredCiptVlanConfigGroup": arubaWiredCiptVlanConfigGroup,
       "arubaWiredCiptPortConfigGroup": arubaWiredCiptPortConfigGroup,
       "arubaWiredCiptTrackedClientsGroup": arubaWiredCiptTrackedClientsGroup,
       "arubaWiredCiptCompliances": arubaWiredCiptCompliances,
       "arubaWiredCiptCompliance": arubaWiredCiptCompliance}
)
