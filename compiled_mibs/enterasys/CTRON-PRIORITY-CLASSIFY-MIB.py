# SNMP MIB module (CTRON-PRIORITY-CLASSIFY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTRON-PRIORITY-CLASSIFY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:41:13 2025
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

(ctPriorityExt,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctPriorityExt")

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

ctPriClassify = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CtPriClassifyType(TextualConvention, Integer32):
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
              25)
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
          ("ipFragments", 25))
    )



class PortList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CtPriClassifyObjects_ObjectIdentity = ObjectIdentity
ctPriClassifyObjects = _CtPriClassifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1)
)


class _CtPriClassifyStatus_Type(Integer32):
    """Custom type ctPriClassifyStatus based on Integer32"""
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


_CtPriClassifyStatus_Type.__name__ = "Integer32"
_CtPriClassifyStatus_Object = MibScalar
ctPriClassifyStatus = _CtPriClassifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 1),
    _CtPriClassifyStatus_Type()
)
ctPriClassifyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPriClassifyStatus.setStatus("current")
_CtPriClassifyMaxEntries_Type = Unsigned32
_CtPriClassifyMaxEntries_Object = MibScalar
ctPriClassifyMaxEntries = _CtPriClassifyMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 2),
    _CtPriClassifyMaxEntries_Type()
)
ctPriClassifyMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriClassifyMaxEntries.setStatus("current")
_CtPriClassifyNumEntries_Type = Unsigned32
_CtPriClassifyNumEntries_Object = MibScalar
ctPriClassifyNumEntries = _CtPriClassifyNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 3),
    _CtPriClassifyNumEntries_Type()
)
ctPriClassifyNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriClassifyNumEntries.setStatus("current")
_CtPriClassifyTable_Object = MibTable
ctPriClassifyTable = _CtPriClassifyTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4)
)
if mibBuilder.loadTexts:
    ctPriClassifyTable.setStatus("current")
_CtPriClassifyEntry_Object = MibTableRow
ctPriClassifyEntry = _CtPriClassifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1)
)
ctPriClassifyEntry.setIndexNames(
    (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyPriority"),
    (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyDataMeaning"),
    (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyDataVal"),
    (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyDataMask"),
)
if mibBuilder.loadTexts:
    ctPriClassifyEntry.setStatus("current")


class _CtPriClassifyPriority_Type(Integer32):
    """Custom type ctPriClassifyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CtPriClassifyPriority_Type.__name__ = "Integer32"
_CtPriClassifyPriority_Object = MibTableColumn
ctPriClassifyPriority = _CtPriClassifyPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 1),
    _CtPriClassifyPriority_Type()
)
ctPriClassifyPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctPriClassifyPriority.setStatus("current")
_CtPriClassifyDataMeaning_Type = CtPriClassifyType
_CtPriClassifyDataMeaning_Object = MibTableColumn
ctPriClassifyDataMeaning = _CtPriClassifyDataMeaning_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 2),
    _CtPriClassifyDataMeaning_Type()
)
ctPriClassifyDataMeaning.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctPriClassifyDataMeaning.setStatus("current")
_CtPriClassifyDataVal_Type = Unsigned32
_CtPriClassifyDataVal_Object = MibTableColumn
ctPriClassifyDataVal = _CtPriClassifyDataVal_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 3),
    _CtPriClassifyDataVal_Type()
)
ctPriClassifyDataVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctPriClassifyDataVal.setStatus("current")
_CtPriClassifyDataMask_Type = Unsigned32
_CtPriClassifyDataMask_Object = MibTableColumn
ctPriClassifyDataMask = _CtPriClassifyDataMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 4),
    _CtPriClassifyDataMask_Type()
)
ctPriClassifyDataMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctPriClassifyDataMask.setStatus("current")


class _CtPriClassifyIngressList_Type(PortList):
    """Custom type ctPriClassifyIngressList based on PortList"""
    defaultHexValue = "0000"


_CtPriClassifyIngressList_Type.__name__ = "PortList"
_CtPriClassifyIngressList_Object = MibTableColumn
ctPriClassifyIngressList = _CtPriClassifyIngressList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 5),
    _CtPriClassifyIngressList_Type()
)
ctPriClassifyIngressList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctPriClassifyIngressList.setStatus("current")
_CtPriClassifyRowStatus_Type = RowStatus
_CtPriClassifyRowStatus_Object = MibTableColumn
ctPriClassifyRowStatus = _CtPriClassifyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 6),
    _CtPriClassifyRowStatus_Type()
)
ctPriClassifyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctPriClassifyRowStatus.setStatus("current")
_CtPriClassifyRowInfo_Type = DisplayString
_CtPriClassifyRowInfo_Object = MibTableColumn
ctPriClassifyRowInfo = _CtPriClassifyRowInfo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 7),
    _CtPriClassifyRowInfo_Type()
)
ctPriClassifyRowInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriClassifyRowInfo.setStatus("current")


class _CtPriClassifyTOSStatus_Type(Integer32):
    """Custom type ctPriClassifyTOSStatus based on Integer32"""
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


_CtPriClassifyTOSStatus_Type.__name__ = "Integer32"
_CtPriClassifyTOSStatus_Object = MibTableColumn
ctPriClassifyTOSStatus = _CtPriClassifyTOSStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 8),
    _CtPriClassifyTOSStatus_Type()
)
ctPriClassifyTOSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPriClassifyTOSStatus.setStatus("current")


class _CtPriClassifyTOSValue_Type(Integer32):
    """Custom type ctPriClassifyTOSValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CtPriClassifyTOSValue_Type.__name__ = "Integer32"
_CtPriClassifyTOSValue_Object = MibTableColumn
ctPriClassifyTOSValue = _CtPriClassifyTOSValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 9),
    _CtPriClassifyTOSValue_Type()
)
ctPriClassifyTOSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPriClassifyTOSValue.setStatus("current")
_CtPriClassifyAbilityTable_Object = MibTable
ctPriClassifyAbilityTable = _CtPriClassifyAbilityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5)
)
if mibBuilder.loadTexts:
    ctPriClassifyAbilityTable.setStatus("current")
_CtPriClassifyAbilityEntry_Object = MibTableRow
ctPriClassifyAbilityEntry = _CtPriClassifyAbilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5, 1)
)
ctPriClassifyAbilityEntry.setIndexNames(
    (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyAbility"),
)
if mibBuilder.loadTexts:
    ctPriClassifyAbilityEntry.setStatus("current")
_CtPriClassifyAbility_Type = CtPriClassifyType
_CtPriClassifyAbility_Object = MibTableColumn
ctPriClassifyAbility = _CtPriClassifyAbility_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5, 1, 1),
    _CtPriClassifyAbility_Type()
)
ctPriClassifyAbility.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctPriClassifyAbility.setStatus("current")
_CtPriClassifyPorts_Type = PortList
_CtPriClassifyPorts_Object = MibTableColumn
ctPriClassifyPorts = _CtPriClassifyPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5, 1, 2),
    _CtPriClassifyPorts_Type()
)
ctPriClassifyPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriClassifyPorts.setStatus("current")
_CtPriClassifyTableLastChange_Type = TimeTicks
_CtPriClassifyTableLastChange_Object = MibScalar
ctPriClassifyTableLastChange = _CtPriClassifyTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 6),
    _CtPriClassifyTableLastChange_Type()
)
ctPriClassifyTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriClassifyTableLastChange.setStatus("current")
_CtPriClassifyConformance_ObjectIdentity = ObjectIdentity
ctPriClassifyConformance = _CtPriClassifyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2)
)
_CtPriClassifyGroups_ObjectIdentity = ObjectIdentity
ctPriClassifyGroups = _CtPriClassifyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 1)
)
_CtPriClassifyCompliances_ObjectIdentity = ObjectIdentity
ctPriClassifyCompliances = _CtPriClassifyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 2)
)

# Managed Objects groups

ctPriClassifyBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 1, 1)
)
ctPriClassifyBaseGroup.setObjects(
      *(("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyStatus"),
        ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyMaxEntries"),
        ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyNumEntries"),
        ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyIngressList"),
        ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyRowStatus"),
        ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyRowInfo"),
        ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyTOSStatus"),
        ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyTOSValue"),
        ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyPorts"),
        ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyTableLastChange"))
)
if mibBuilder.loadTexts:
    ctPriClassifyBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ctPriClassifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 2, 1)
)
ctPriClassifyCompliance.setObjects(
    ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyBaseGroup")
)
if mibBuilder.loadTexts:
    ctPriClassifyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-PRIORITY-CLASSIFY-MIB",
    **{"CtPriClassifyType": CtPriClassifyType,
       "PortList": PortList,
       "ctPriClassify": ctPriClassify,
       "ctPriClassifyObjects": ctPriClassifyObjects,
       "ctPriClassifyStatus": ctPriClassifyStatus,
       "ctPriClassifyMaxEntries": ctPriClassifyMaxEntries,
       "ctPriClassifyNumEntries": ctPriClassifyNumEntries,
       "ctPriClassifyTable": ctPriClassifyTable,
       "ctPriClassifyEntry": ctPriClassifyEntry,
       "ctPriClassifyPriority": ctPriClassifyPriority,
       "ctPriClassifyDataMeaning": ctPriClassifyDataMeaning,
       "ctPriClassifyDataVal": ctPriClassifyDataVal,
       "ctPriClassifyDataMask": ctPriClassifyDataMask,
       "ctPriClassifyIngressList": ctPriClassifyIngressList,
       "ctPriClassifyRowStatus": ctPriClassifyRowStatus,
       "ctPriClassifyRowInfo": ctPriClassifyRowInfo,
       "ctPriClassifyTOSStatus": ctPriClassifyTOSStatus,
       "ctPriClassifyTOSValue": ctPriClassifyTOSValue,
       "ctPriClassifyAbilityTable": ctPriClassifyAbilityTable,
       "ctPriClassifyAbilityEntry": ctPriClassifyAbilityEntry,
       "ctPriClassifyAbility": ctPriClassifyAbility,
       "ctPriClassifyPorts": ctPriClassifyPorts,
       "ctPriClassifyTableLastChange": ctPriClassifyTableLastChange,
       "ctPriClassifyConformance": ctPriClassifyConformance,
       "ctPriClassifyGroups": ctPriClassifyGroups,
       "ctPriClassifyBaseGroup": ctPriClassifyBaseGroup,
       "ctPriClassifyCompliances": ctPriClassifyCompliances,
       "ctPriClassifyCompliance": ctPriClassifyCompliance}
)
