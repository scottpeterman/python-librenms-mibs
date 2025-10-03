# SNMP MIB module (NSCRTV-EPON-VLAN-MGM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fs\NSCRTV-EPON-VLAN-MGM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:00 2025
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

(AutoNegotiationTechAbility,
 EponAlarmCode,
 EponAlarmInstance,
 EponCardIndex,
 EponDeviceIndex,
 EponPortIndex,
 EponSeverityType,
 EponStats15MinRecordType,
 EponStats24HourRecordType,
 EponStatsThresholdType,
 TAddress,
 vlanManagementObjects) = mibBuilder.importSymbols(
    "NSCRTV-EPONEOC-EPON-MIB",
    "AutoNegotiationTechAbility",
    "EponAlarmCode",
    "EponAlarmInstance",
    "EponCardIndex",
    "EponDeviceIndex",
    "EponPortIndex",
    "EponSeverityType",
    "EponStats15MinRecordType",
    "EponStats24HourRecordType",
    "EponStatsThresholdType",
    "TAddress",
    "vlanManagementObjects")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VlanGlobalInfoTable_Object = MibTable
vlanGlobalInfoTable = _VlanGlobalInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 1)
)
if mibBuilder.loadTexts:
    vlanGlobalInfoTable.setStatus("current")
_VlanGlobalInfoEntry_Object = MibTableRow
vlanGlobalInfoEntry = _VlanGlobalInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 1, 1)
)
vlanGlobalInfoEntry.setIndexNames(
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "vlanDeviceIndex"),
)
if mibBuilder.loadTexts:
    vlanGlobalInfoEntry.setStatus("current")
_VlanDeviceIndex_Type = Integer32
_VlanDeviceIndex_Object = MibTableColumn
vlanDeviceIndex = _VlanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 1, 1, 1),
    _VlanDeviceIndex_Type()
)
vlanDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanDeviceIndex.setStatus("current")
_MaxVlanId_Type = Integer32
_MaxVlanId_Object = MibTableColumn
maxVlanId = _MaxVlanId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 1, 1, 2),
    _MaxVlanId_Type()
)
maxVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxVlanId.setStatus("current")
_MaxSupportVlans_Type = Integer32
_MaxSupportVlans_Object = MibTableColumn
maxSupportVlans = _MaxSupportVlans_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 1, 1, 3),
    _MaxSupportVlans_Type()
)
maxSupportVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSupportVlans.setStatus("current")
_CreatedVlanNumber_Type = Integer32
_CreatedVlanNumber_Object = MibTableColumn
createdVlanNumber = _CreatedVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 1, 1, 4),
    _CreatedVlanNumber_Type()
)
createdVlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    createdVlanNumber.setStatus("current")
_VlanConfigGroup_ObjectIdentity = ObjectIdentity
vlanConfigGroup = _VlanConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2)
)
if mibBuilder.loadTexts:
    vlanConfigGroup.setStatus("current")
_OltVlanConfigTable_Object = MibTable
oltVlanConfigTable = _OltVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 1)
)
if mibBuilder.loadTexts:
    oltVlanConfigTable.setStatus("current")
_OltVlanConfigEntry_Object = MibTableRow
oltVlanConfigEntry = _OltVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 1, 1)
)
oltVlanConfigEntry.setIndexNames(
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "oltVlanIndex"),
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "oltVlanDeviceIndex"),
)
if mibBuilder.loadTexts:
    oltVlanConfigEntry.setStatus("current")
_OltVlanIndex_Type = Integer32
_OltVlanIndex_Object = MibTableColumn
oltVlanIndex = _OltVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 1, 1, 1),
    _OltVlanIndex_Type()
)
oltVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oltVlanIndex.setStatus("current")
_OltVlanDeviceIndex_Type = Integer32
_OltVlanDeviceIndex_Object = MibTableColumn
oltVlanDeviceIndex = _OltVlanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 1, 1, 2),
    _OltVlanDeviceIndex_Type()
)
oltVlanDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oltVlanDeviceIndex.setStatus("current")


class _OltVlanName_Type(OctetString):
    """Custom type oltVlanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_OltVlanName_Type.__name__ = "OctetString"
_OltVlanName_Object = MibTableColumn
oltVlanName = _OltVlanName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 1, 1, 3),
    _OltVlanName_Type()
)
oltVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oltVlanName.setStatus("current")
_TaggedPort_Type = OctetString
_TaggedPort_Object = MibTableColumn
taggedPort = _TaggedPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 1, 1, 4),
    _TaggedPort_Type()
)
taggedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    taggedPort.setStatus("current")
_UntaggedPort_Type = OctetString
_UntaggedPort_Object = MibTableColumn
untaggedPort = _UntaggedPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 1, 1, 5),
    _UntaggedPort_Type()
)
untaggedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    untaggedPort.setStatus("current")
_OltVlanRowStatus_Type = RowStatus
_OltVlanRowStatus_Object = MibTableColumn
oltVlanRowStatus = _OltVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 1, 1, 6),
    _OltVlanRowStatus_Type()
)
oltVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oltVlanRowStatus.setStatus("current")
_OnuVlanConfigTable_Object = MibTable
onuVlanConfigTable = _OnuVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 2)
)
if mibBuilder.loadTexts:
    onuVlanConfigTable.setStatus("current")
_OnuVlanConfigEntry_Object = MibTableRow
onuVlanConfigEntry = _OnuVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 2, 1)
)
onuVlanConfigEntry.setIndexNames(
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "onuVlanIndex"),
)
if mibBuilder.loadTexts:
    onuVlanConfigEntry.setStatus("current")
_OnuVlanIndex_Type = Integer32
_OnuVlanIndex_Object = MibTableColumn
onuVlanIndex = _OnuVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 2, 1, 1),
    _OnuVlanIndex_Type()
)
onuVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuVlanIndex.setStatus("current")


class _OnuVlanName_Type(OctetString):
    """Custom type onuVlanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_OnuVlanName_Type.__name__ = "OctetString"
_OnuVlanName_Object = MibTableColumn
onuVlanName = _OnuVlanName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 2, 1, 2),
    _OnuVlanName_Type()
)
onuVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuVlanName.setStatus("current")
_OnuVlanTaggedPort_Type = OctetString
_OnuVlanTaggedPort_Object = MibTableColumn
onuVlanTaggedPort = _OnuVlanTaggedPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 2, 1, 3),
    _OnuVlanTaggedPort_Type()
)
onuVlanTaggedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuVlanTaggedPort.setStatus("current")
_OnuVlanUntaggedPort_Type = OctetString
_OnuVlanUntaggedPort_Object = MibTableColumn
onuVlanUntaggedPort = _OnuVlanUntaggedPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 2, 1, 4),
    _OnuVlanUntaggedPort_Type()
)
onuVlanUntaggedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuVlanUntaggedPort.setStatus("current")
_OnuVlanRowStatus_Type = RowStatus
_OnuVlanRowStatus_Object = MibTableColumn
onuVlanRowStatus = _OnuVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 2, 1, 5),
    _OnuVlanRowStatus_Type()
)
onuVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuVlanRowStatus.setStatus("current")
_PortVlanGroup_ObjectIdentity = ObjectIdentity
portVlanGroup = _PortVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3)
)
if mibBuilder.loadTexts:
    portVlanGroup.setStatus("current")
_PortVlanTable_Object = MibTable
portVlanTable = _PortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1)
)
if mibBuilder.loadTexts:
    portVlanTable.setStatus("current")
_PortVlanEntry_Object = MibTableRow
portVlanEntry = _PortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1)
)
portVlanEntry.setIndexNames(
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "pvlanDeviceIndex"),
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "pvlanCardIndex"),
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "pvlanPortIndex"),
)
if mibBuilder.loadTexts:
    portVlanEntry.setStatus("current")
_PvlanDeviceIndex_Type = EponDeviceIndex
_PvlanDeviceIndex_Object = MibTableColumn
pvlanDeviceIndex = _PvlanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1, 1),
    _PvlanDeviceIndex_Type()
)
pvlanDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvlanDeviceIndex.setStatus("current")
_PvlanCardIndex_Type = EponCardIndex
_PvlanCardIndex_Object = MibTableColumn
pvlanCardIndex = _PvlanCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1, 2),
    _PvlanCardIndex_Type()
)
pvlanCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvlanCardIndex.setStatus("current")
_PvlanPortIndex_Type = EponPortIndex
_PvlanPortIndex_Object = MibTableColumn
pvlanPortIndex = _PvlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1, 3),
    _PvlanPortIndex_Type()
)
pvlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvlanPortIndex.setStatus("current")


class _VlanTagTpid_Type(OctetString):
    """Custom type vlanTagTpid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_VlanTagTpid_Type.__name__ = "OctetString"
_VlanTagTpid_Object = MibTableColumn
vlanTagTpid = _VlanTagTpid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1, 4),
    _VlanTagTpid_Type()
)
vlanTagTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTagTpid.setStatus("current")
_VlanTagCfi_Type = TruthValue
_VlanTagCfi_Object = MibTableColumn
vlanTagCfi = _VlanTagCfi_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1, 5),
    _VlanTagCfi_Type()
)
vlanTagCfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTagCfi.setStatus("current")


class _VlanTagPriority_Type(Integer32):
    """Custom type vlanTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanTagPriority_Type.__name__ = "Integer32"
_VlanTagPriority_Object = MibTableColumn
vlanTagPriority = _VlanTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1, 6),
    _VlanTagPriority_Type()
)
vlanTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTagPriority.setStatus("current")
_VlanPVid_Type = Integer32
_VlanPVid_Object = MibTableColumn
vlanPVid = _VlanPVid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1, 7),
    _VlanPVid_Type()
)
vlanPVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPVid.setStatus("current")


class _VlanMode_Type(Integer32):
    """Custom type vlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 0),
          ("tag", 1),
          ("translation", 2),
          ("aggregation", 3),
          ("trunk", 4),
          ("stacking", 5))
    )


_VlanMode_Type.__name__ = "Integer32"
_VlanMode_Object = MibTableColumn
vlanMode = _VlanMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1, 8),
    _VlanMode_Type()
)
vlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMode.setStatus("current")
_PortVlanTranslationTable_Object = MibTable
portVlanTranslationTable = _PortVlanTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 2)
)
if mibBuilder.loadTexts:
    portVlanTranslationTable.setStatus("current")
_PortVlanTranslationEntry_Object = MibTableRow
portVlanTranslationEntry = _PortVlanTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 2, 1)
)
portVlanTranslationEntry.setIndexNames(
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "pvtDeviceIndex"),
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "pvtCardIndex"),
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "pvtPortIndex"),
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "portVidIndex"),
)
if mibBuilder.loadTexts:
    portVlanTranslationEntry.setStatus("current")
_PvtDeviceIndex_Type = EponDeviceIndex
_PvtDeviceIndex_Object = MibTableColumn
pvtDeviceIndex = _PvtDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 2, 1, 1),
    _PvtDeviceIndex_Type()
)
pvtDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvtDeviceIndex.setStatus("current")
_PvtCardIndex_Type = EponCardIndex
_PvtCardIndex_Object = MibTableColumn
pvtCardIndex = _PvtCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 2, 1, 2),
    _PvtCardIndex_Type()
)
pvtCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvtCardIndex.setStatus("current")
_PvtPortIndex_Type = EponPortIndex
_PvtPortIndex_Object = MibTableColumn
pvtPortIndex = _PvtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 2, 1, 3),
    _PvtPortIndex_Type()
)
pvtPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvtPortIndex.setStatus("current")
_PortVidIndex_Type = Unsigned32
_PortVidIndex_Object = MibTableColumn
portVidIndex = _PortVidIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 2, 1, 4),
    _PortVidIndex_Type()
)
portVidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portVidIndex.setStatus("current")
_TranslationNewVid_Type = Unsigned32
_TranslationNewVid_Object = MibTableColumn
translationNewVid = _TranslationNewVid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 2, 1, 5),
    _TranslationNewVid_Type()
)
translationNewVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    translationNewVid.setStatus("current")
_TranslationRowStatus_Type = RowStatus
_TranslationRowStatus_Object = MibTableColumn
translationRowStatus = _TranslationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 2, 1, 6),
    _TranslationRowStatus_Type()
)
translationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    translationRowStatus.setStatus("current")
_PortVlanAggregationManagement_ObjectIdentity = ObjectIdentity
portVlanAggregationManagement = _PortVlanAggregationManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3)
)
if mibBuilder.loadTexts:
    portVlanAggregationManagement.setStatus("current")
_PortVlanAggregationConfigTable_Object = MibTable
portVlanAggregationConfigTable = _PortVlanAggregationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3, 1)
)
if mibBuilder.loadTexts:
    portVlanAggregationConfigTable.setStatus("current")
_PortVlanAggregationConfigEntry_Object = MibTableRow
portVlanAggregationConfigEntry = _PortVlanAggregationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3, 1, 1)
)
portVlanAggregationConfigEntry.setIndexNames(
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "pvaDeviceIndex"),
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "pvaCardIndex"),
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "pvaPortIndex"),
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "portAggregationVidIndex"),
)
if mibBuilder.loadTexts:
    portVlanAggregationConfigEntry.setStatus("current")
_PvaDeviceIndex_Type = EponDeviceIndex
_PvaDeviceIndex_Object = MibTableColumn
pvaDeviceIndex = _PvaDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3, 1, 1, 1),
    _PvaDeviceIndex_Type()
)
pvaDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvaDeviceIndex.setStatus("current")
_PvaCardIndex_Type = EponCardIndex
_PvaCardIndex_Object = MibTableColumn
pvaCardIndex = _PvaCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3, 1, 1, 2),
    _PvaCardIndex_Type()
)
pvaCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvaCardIndex.setStatus("current")
_PvaPortIndex_Type = EponPortIndex
_PvaPortIndex_Object = MibTableColumn
pvaPortIndex = _PvaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3, 1, 1, 3),
    _PvaPortIndex_Type()
)
pvaPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvaPortIndex.setStatus("current")
_PortAggregationVidIndex_Type = Unsigned32
_PortAggregationVidIndex_Object = MibTableColumn
portAggregationVidIndex = _PortAggregationVidIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3, 1, 1, 4),
    _PortAggregationVidIndex_Type()
)
portAggregationVidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portAggregationVidIndex.setStatus("current")


class _AggregationVidList_Type(OctetString):
    """Custom type aggregationVidList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_AggregationVidList_Type.__name__ = "OctetString"
_AggregationVidList_Object = MibTableColumn
aggregationVidList = _AggregationVidList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3, 1, 1, 5),
    _AggregationVidList_Type()
)
aggregationVidList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggregationVidList.setStatus("current")
_AggregationRowStatus_Type = RowStatus
_AggregationRowStatus_Object = MibTableColumn
aggregationRowStatus = _AggregationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3, 1, 1, 6),
    _AggregationRowStatus_Type()
)
aggregationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggregationRowStatus.setStatus("current")
_PortVlanTrunkTable_Object = MibTable
portVlanTrunkTable = _PortVlanTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 4)
)
if mibBuilder.loadTexts:
    portVlanTrunkTable.setStatus("current")
_PortVlanTrunkEntry_Object = MibTableRow
portVlanTrunkEntry = _PortVlanTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 4, 1)
)
portVlanTrunkEntry.setIndexNames(
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "trunkDeviceIndex"),
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "trunkCardIndex"),
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "trunkPortIndex"),
)
if mibBuilder.loadTexts:
    portVlanTrunkEntry.setStatus("current")
_TrunkDeviceIndex_Type = EponDeviceIndex
_TrunkDeviceIndex_Object = MibTableColumn
trunkDeviceIndex = _TrunkDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 4, 1, 1),
    _TrunkDeviceIndex_Type()
)
trunkDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkDeviceIndex.setStatus("current")
_TrunkCardIndex_Type = EponCardIndex
_TrunkCardIndex_Object = MibTableColumn
trunkCardIndex = _TrunkCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 4, 1, 2),
    _TrunkCardIndex_Type()
)
trunkCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkCardIndex.setStatus("current")
_TrunkPortIndex_Type = EponPortIndex
_TrunkPortIndex_Object = MibTableColumn
trunkPortIndex = _TrunkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 4, 1, 3),
    _TrunkPortIndex_Type()
)
trunkPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkPortIndex.setStatus("current")


class _TrunkVidList_Type(OctetString):
    """Custom type trunkVidList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_TrunkVidList_Type.__name__ = "OctetString"
_TrunkVidList_Object = MibTableColumn
trunkVidList = _TrunkVidList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 4, 1, 4),
    _TrunkVidList_Type()
)
trunkVidList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkVidList.setStatus("current")
_PortVlanTrunkRowStatus_Type = RowStatus
_PortVlanTrunkRowStatus_Object = MibTableColumn
portVlanTrunkRowStatus = _PortVlanTrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 4, 1, 5),
    _PortVlanTrunkRowStatus_Type()
)
portVlanTrunkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portVlanTrunkRowStatus.setStatus("current")
_QinQConfigGroup_ObjectIdentity = ObjectIdentity
qinQConfigGroup = _QinQConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4)
)
if mibBuilder.loadTexts:
    qinQConfigGroup.setStatus("current")
_PortQinQConfigTable_Object = MibTable
portQinQConfigTable = _PortQinQConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1)
)
if mibBuilder.loadTexts:
    portQinQConfigTable.setStatus("current")
_PortQinQConfigEntry_Object = MibTableRow
portQinQConfigEntry = _PortQinQConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1)
)
portQinQConfigEntry.setIndexNames(
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "pqDeviceIndex"),
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "pqCardIndex"),
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "pqPortIndex"),
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "pqStartVlanId"),
    (0, "NSCRTV-EPON-VLAN-MGM-MIB", "pqEndVlanId"),
)
if mibBuilder.loadTexts:
    portQinQConfigEntry.setStatus("current")
_PqDeviceIndex_Type = EponDeviceIndex
_PqDeviceIndex_Object = MibTableColumn
pqDeviceIndex = _PqDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 1),
    _PqDeviceIndex_Type()
)
pqDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pqDeviceIndex.setStatus("current")
_PqCardIndex_Type = EponCardIndex
_PqCardIndex_Object = MibTableColumn
pqCardIndex = _PqCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 2),
    _PqCardIndex_Type()
)
pqCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pqCardIndex.setStatus("current")
_PqPortIndex_Type = EponPortIndex
_PqPortIndex_Object = MibTableColumn
pqPortIndex = _PqPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 3),
    _PqPortIndex_Type()
)
pqPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pqPortIndex.setStatus("current")
_PqStartVlanId_Type = Integer32
_PqStartVlanId_Object = MibTableColumn
pqStartVlanId = _PqStartVlanId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 4),
    _PqStartVlanId_Type()
)
pqStartVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pqStartVlanId.setStatus("current")
_PqEndVlanId_Type = Integer32
_PqEndVlanId_Object = MibTableColumn
pqEndVlanId = _PqEndVlanId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 5),
    _PqEndVlanId_Type()
)
pqEndVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pqEndVlanId.setStatus("current")
_PqSVlanId_Type = Integer32
_PqSVlanId_Object = MibTableColumn
pqSVlanId = _PqSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 6),
    _PqSVlanId_Type()
)
pqSVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqSVlanId.setStatus("current")


class _PqSTagCosDetermine_Type(Integer32):
    """Custom type pqSTagCosDetermine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redefine", 1),
          ("copyFromCTag", 2))
    )


_PqSTagCosDetermine_Type.__name__ = "Integer32"
_PqSTagCosDetermine_Object = MibTableColumn
pqSTagCosDetermine = _PqSTagCosDetermine_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 7),
    _PqSTagCosDetermine_Type()
)
pqSTagCosDetermine.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqSTagCosDetermine.setStatus("current")


class _PqSTagCosNewValue_Type(Integer32):
    """Custom type pqSTagCosNewValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PqSTagCosNewValue_Type.__name__ = "Integer32"
_PqSTagCosNewValue_Object = MibTableColumn
pqSTagCosNewValue = _PqSTagCosNewValue_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 8),
    _PqSTagCosNewValue_Type()
)
pqSTagCosNewValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqSTagCosNewValue.setStatus("current")
_PqRowStatus_Type = RowStatus
_PqRowStatus_Object = MibTableColumn
pqRowStatus = _PqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 9),
    _PqRowStatus_Type()
)
pqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-EPON-VLAN-MGM-MIB",
    **{"vlanGlobalInfoTable": vlanGlobalInfoTable,
       "vlanGlobalInfoEntry": vlanGlobalInfoEntry,
       "vlanDeviceIndex": vlanDeviceIndex,
       "maxVlanId": maxVlanId,
       "maxSupportVlans": maxSupportVlans,
       "createdVlanNumber": createdVlanNumber,
       "vlanConfigGroup": vlanConfigGroup,
       "oltVlanConfigTable": oltVlanConfigTable,
       "oltVlanConfigEntry": oltVlanConfigEntry,
       "oltVlanIndex": oltVlanIndex,
       "oltVlanDeviceIndex": oltVlanDeviceIndex,
       "oltVlanName": oltVlanName,
       "taggedPort": taggedPort,
       "untaggedPort": untaggedPort,
       "oltVlanRowStatus": oltVlanRowStatus,
       "onuVlanConfigTable": onuVlanConfigTable,
       "onuVlanConfigEntry": onuVlanConfigEntry,
       "onuVlanIndex": onuVlanIndex,
       "onuVlanName": onuVlanName,
       "onuVlanTaggedPort": onuVlanTaggedPort,
       "onuVlanUntaggedPort": onuVlanUntaggedPort,
       "onuVlanRowStatus": onuVlanRowStatus,
       "portVlanGroup": portVlanGroup,
       "portVlanTable": portVlanTable,
       "portVlanEntry": portVlanEntry,
       "pvlanDeviceIndex": pvlanDeviceIndex,
       "pvlanCardIndex": pvlanCardIndex,
       "pvlanPortIndex": pvlanPortIndex,
       "vlanTagTpid": vlanTagTpid,
       "vlanTagCfi": vlanTagCfi,
       "vlanTagPriority": vlanTagPriority,
       "vlanPVid": vlanPVid,
       "vlanMode": vlanMode,
       "portVlanTranslationTable": portVlanTranslationTable,
       "portVlanTranslationEntry": portVlanTranslationEntry,
       "pvtDeviceIndex": pvtDeviceIndex,
       "pvtCardIndex": pvtCardIndex,
       "pvtPortIndex": pvtPortIndex,
       "portVidIndex": portVidIndex,
       "translationNewVid": translationNewVid,
       "translationRowStatus": translationRowStatus,
       "portVlanAggregationManagement": portVlanAggregationManagement,
       "portVlanAggregationConfigTable": portVlanAggregationConfigTable,
       "portVlanAggregationConfigEntry": portVlanAggregationConfigEntry,
       "pvaDeviceIndex": pvaDeviceIndex,
       "pvaCardIndex": pvaCardIndex,
       "pvaPortIndex": pvaPortIndex,
       "portAggregationVidIndex": portAggregationVidIndex,
       "aggregationVidList": aggregationVidList,
       "aggregationRowStatus": aggregationRowStatus,
       "portVlanTrunkTable": portVlanTrunkTable,
       "portVlanTrunkEntry": portVlanTrunkEntry,
       "trunkDeviceIndex": trunkDeviceIndex,
       "trunkCardIndex": trunkCardIndex,
       "trunkPortIndex": trunkPortIndex,
       "trunkVidList": trunkVidList,
       "portVlanTrunkRowStatus": portVlanTrunkRowStatus,
       "qinQConfigGroup": qinQConfigGroup,
       "portQinQConfigTable": portQinQConfigTable,
       "portQinQConfigEntry": portQinQConfigEntry,
       "pqDeviceIndex": pqDeviceIndex,
       "pqCardIndex": pqCardIndex,
       "pqPortIndex": pqPortIndex,
       "pqStartVlanId": pqStartVlanId,
       "pqEndVlanId": pqEndVlanId,
       "pqSVlanId": pqSVlanId,
       "pqSTagCosDetermine": pqSTagCosDetermine,
       "pqSTagCosNewValue": pqSTagCosNewValue,
       "pqRowStatus": pqRowStatus}
)
