# SNMP MIB module (CTRON-VLAN-CLASSIFY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTRON-VLAN-CLASSIFY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:01 2025
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

(ctVlanExt,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctVlanExt")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ctVlanClassify = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6)
)
if mibBuilder.loadTexts:
    ctVlanClassify.setRevisions(
        ("2002-12-19 16:31",
         "2002-03-27 20:55")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CtVlanClassifyType(TextualConvention, Integer32):
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
              34)
        )
    )
    namedValues = NamedValues(
        *(("etherType", 1),
          ("llcDsapSsap", 2),
          ("ipTypeOfService", 3),
          ("ipProtocolType", 4),
          ("ipxClassOfService", 5),
          ("ipxPacketType", 6),
          ("ipAddressSource", 7),
          ("ipAddressDestination", 8),
          ("ipAddressBilateral", 9),
          ("ipxNetworkSource", 10),
          ("ipxNetworkDestination", 11),
          ("ipxNetworkBilateral", 12),
          ("ipUdpPortSource", 13),
          ("ipUdpPortDestination", 14),
          ("ipUdpPortBilateral", 15),
          ("ipTcpPortSource", 16),
          ("ipTcpPortDestination", 17),
          ("ipTcpPortBilateral", 18),
          ("ipxSocketSource", 19),
          ("ipxSocketDestination", 20),
          ("ipxSocketBilateral", 21),
          ("macAddressSource", 22),
          ("macAddressDestination", 23),
          ("macAddressBilateral", 24),
          ("ipFragments", 25),
          ("ipUdpPortSourceRange", 26),
          ("ipUdpPortDestinationRange", 27),
          ("ipUdpPortBilateralRange", 28),
          ("ipTcpPortSourceRange", 29),
          ("ipTcpPortDestinationRange", 30),
          ("ipTcpPortBilateralRange", 31),
          ("icmpType", 32),
          ("vlanId", 33),
          ("tci", 34))
    )



class VlanIndex(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CtVlanClassifyObjects_ObjectIdentity = ObjectIdentity
ctVlanClassifyObjects = _CtVlanClassifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1)
)


class _CtVlanClassifyStatus_Type(Integer32):
    """Custom type ctVlanClassifyStatus based on Integer32"""
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


_CtVlanClassifyStatus_Type.__name__ = "Integer32"
_CtVlanClassifyStatus_Object = MibScalar
ctVlanClassifyStatus = _CtVlanClassifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 1),
    _CtVlanClassifyStatus_Type()
)
ctVlanClassifyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanClassifyStatus.setStatus("current")
_CtVlanClassifyMaxEntries_Type = Unsigned32
_CtVlanClassifyMaxEntries_Object = MibScalar
ctVlanClassifyMaxEntries = _CtVlanClassifyMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 2),
    _CtVlanClassifyMaxEntries_Type()
)
ctVlanClassifyMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanClassifyMaxEntries.setStatus("current")
_CtVlanClassifyNumEntries_Type = Unsigned32
_CtVlanClassifyNumEntries_Object = MibScalar
ctVlanClassifyNumEntries = _CtVlanClassifyNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 3),
    _CtVlanClassifyNumEntries_Type()
)
ctVlanClassifyNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanClassifyNumEntries.setStatus("current")
_CtVlanClassifyTable_Object = MibTable
ctVlanClassifyTable = _CtVlanClassifyTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4)
)
if mibBuilder.loadTexts:
    ctVlanClassifyTable.setStatus("current")
_CtVlanClassifyEntry_Object = MibTableRow
ctVlanClassifyEntry = _CtVlanClassifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4, 1)
)
ctVlanClassifyEntry.setIndexNames(
    (0, "CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyVlanIndex"),
    (0, "CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyDataMeaning"),
    (0, "CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyDataVal"),
    (0, "CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyDataMask"),
)
if mibBuilder.loadTexts:
    ctVlanClassifyEntry.setStatus("current")
_CtVlanClassifyVlanIndex_Type = VlanIndex
_CtVlanClassifyVlanIndex_Object = MibTableColumn
ctVlanClassifyVlanIndex = _CtVlanClassifyVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4, 1, 1),
    _CtVlanClassifyVlanIndex_Type()
)
ctVlanClassifyVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctVlanClassifyVlanIndex.setStatus("current")
_CtVlanClassifyDataMeaning_Type = CtVlanClassifyType
_CtVlanClassifyDataMeaning_Object = MibTableColumn
ctVlanClassifyDataMeaning = _CtVlanClassifyDataMeaning_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4, 1, 2),
    _CtVlanClassifyDataMeaning_Type()
)
ctVlanClassifyDataMeaning.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctVlanClassifyDataMeaning.setStatus("current")
_CtVlanClassifyDataVal_Type = Unsigned32
_CtVlanClassifyDataVal_Object = MibTableColumn
ctVlanClassifyDataVal = _CtVlanClassifyDataVal_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4, 1, 3),
    _CtVlanClassifyDataVal_Type()
)
ctVlanClassifyDataVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctVlanClassifyDataVal.setStatus("current")
_CtVlanClassifyDataMask_Type = Unsigned32
_CtVlanClassifyDataMask_Object = MibTableColumn
ctVlanClassifyDataMask = _CtVlanClassifyDataMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4, 1, 4),
    _CtVlanClassifyDataMask_Type()
)
ctVlanClassifyDataMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctVlanClassifyDataMask.setStatus("current")


class _CtVlanClassifyIngressList_Type(PortList):
    """Custom type ctVlanClassifyIngressList based on PortList"""
    defaultHexValue = "0000"


_CtVlanClassifyIngressList_Type.__name__ = "PortList"
_CtVlanClassifyIngressList_Object = MibTableColumn
ctVlanClassifyIngressList = _CtVlanClassifyIngressList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4, 1, 5),
    _CtVlanClassifyIngressList_Type()
)
ctVlanClassifyIngressList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctVlanClassifyIngressList.setStatus("current")
_CtVlanClassifyRowStatus_Type = RowStatus
_CtVlanClassifyRowStatus_Object = MibTableColumn
ctVlanClassifyRowStatus = _CtVlanClassifyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4, 1, 6),
    _CtVlanClassifyRowStatus_Type()
)
ctVlanClassifyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctVlanClassifyRowStatus.setStatus("current")
_CtVlanClassifyRowInfo_Type = DisplayString
_CtVlanClassifyRowInfo_Object = MibTableColumn
ctVlanClassifyRowInfo = _CtVlanClassifyRowInfo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4, 1, 7),
    _CtVlanClassifyRowInfo_Type()
)
ctVlanClassifyRowInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanClassifyRowInfo.setStatus("current")
_CtVlanClassifyAbilityTable_Object = MibTable
ctVlanClassifyAbilityTable = _CtVlanClassifyAbilityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 5)
)
if mibBuilder.loadTexts:
    ctVlanClassifyAbilityTable.setStatus("current")
_CtVlanClassifyAbilityEntry_Object = MibTableRow
ctVlanClassifyAbilityEntry = _CtVlanClassifyAbilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 5, 1)
)
ctVlanClassifyAbilityEntry.setIndexNames(
    (0, "CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyAbility"),
)
if mibBuilder.loadTexts:
    ctVlanClassifyAbilityEntry.setStatus("current")
_CtVlanClassifyAbility_Type = CtVlanClassifyType
_CtVlanClassifyAbility_Object = MibTableColumn
ctVlanClassifyAbility = _CtVlanClassifyAbility_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 5, 1, 1),
    _CtVlanClassifyAbility_Type()
)
ctVlanClassifyAbility.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctVlanClassifyAbility.setStatus("current")
_CtVlanClassifyPorts_Type = PortList
_CtVlanClassifyPorts_Object = MibTableColumn
ctVlanClassifyPorts = _CtVlanClassifyPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 5, 1, 2),
    _CtVlanClassifyPorts_Type()
)
ctVlanClassifyPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanClassifyPorts.setStatus("current")


class _CtVlanClassifyActionStatus_Type(Integer32):
    """Custom type ctVlanClassifyActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwardNoFrames", 1),
          ("forwardAllFrames", 2))
    )


_CtVlanClassifyActionStatus_Type.__name__ = "Integer32"
_CtVlanClassifyActionStatus_Object = MibTableColumn
ctVlanClassifyActionStatus = _CtVlanClassifyActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 5, 1, 3),
    _CtVlanClassifyActionStatus_Type()
)
ctVlanClassifyActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanClassifyActionStatus.setStatus("current")
_CtVlanClassifyConformance_ObjectIdentity = ObjectIdentity
ctVlanClassifyConformance = _CtVlanClassifyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 2)
)
_CtVlanClassifyGroups_ObjectIdentity = ObjectIdentity
ctVlanClassifyGroups = _CtVlanClassifyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 2, 1)
)
_CtVlanClassifyCompliances_ObjectIdentity = ObjectIdentity
ctVlanClassifyCompliances = _CtVlanClassifyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 2, 2)
)

# Managed Objects groups

ctVlanClassifyBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 2, 1, 1)
)
ctVlanClassifyBaseGroup.setObjects(
      *(("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyStatus"),
        ("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyMaxEntries"),
        ("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyNumEntries"),
        ("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyIngressList"),
        ("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyRowStatus"),
        ("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyRowInfo"),
        ("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyPorts"),
        ("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyActionStatus"))
)
if mibBuilder.loadTexts:
    ctVlanClassifyBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ctVlanClassifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 2, 2, 1)
)
ctVlanClassifyCompliance.setObjects(
    ("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyBaseGroup")
)
if mibBuilder.loadTexts:
    ctVlanClassifyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-VLAN-CLASSIFY-MIB",
    **{"CtVlanClassifyType": CtVlanClassifyType,
       "VlanIndex": VlanIndex,
       "ctVlanClassify": ctVlanClassify,
       "ctVlanClassifyObjects": ctVlanClassifyObjects,
       "ctVlanClassifyStatus": ctVlanClassifyStatus,
       "ctVlanClassifyMaxEntries": ctVlanClassifyMaxEntries,
       "ctVlanClassifyNumEntries": ctVlanClassifyNumEntries,
       "ctVlanClassifyTable": ctVlanClassifyTable,
       "ctVlanClassifyEntry": ctVlanClassifyEntry,
       "ctVlanClassifyVlanIndex": ctVlanClassifyVlanIndex,
       "ctVlanClassifyDataMeaning": ctVlanClassifyDataMeaning,
       "ctVlanClassifyDataVal": ctVlanClassifyDataVal,
       "ctVlanClassifyDataMask": ctVlanClassifyDataMask,
       "ctVlanClassifyIngressList": ctVlanClassifyIngressList,
       "ctVlanClassifyRowStatus": ctVlanClassifyRowStatus,
       "ctVlanClassifyRowInfo": ctVlanClassifyRowInfo,
       "ctVlanClassifyAbilityTable": ctVlanClassifyAbilityTable,
       "ctVlanClassifyAbilityEntry": ctVlanClassifyAbilityEntry,
       "ctVlanClassifyAbility": ctVlanClassifyAbility,
       "ctVlanClassifyPorts": ctVlanClassifyPorts,
       "ctVlanClassifyActionStatus": ctVlanClassifyActionStatus,
       "ctVlanClassifyConformance": ctVlanClassifyConformance,
       "ctVlanClassifyGroups": ctVlanClassifyGroups,
       "ctVlanClassifyBaseGroup": ctVlanClassifyBaseGroup,
       "ctVlanClassifyCompliances": ctVlanClassifyCompliances,
       "ctVlanClassifyCompliance": ctVlanClassifyCompliance}
)
