# SNMP MIB module (NSCRTV-EPON-SNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fs\NSCRTV-EPON-SNI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:46:56 2025
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
 sniObjects) = mibBuilder.importSymbols(
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
    "sniObjects")

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

_SniAttributeTable_Object = MibTable
sniAttributeTable = _SniAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sniAttributeTable.setStatus("current")
_SniAttributeEntry_Object = MibTableRow
sniAttributeEntry = _SniAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1)
)
sniAttributeEntry.setIndexNames(
    (0, "NSCRTV-EPON-SNI-MIB", "sniAttributeDeviceIndex"),
    (0, "NSCRTV-EPON-SNI-MIB", "sniAttributeCardIndex"),
    (0, "NSCRTV-EPON-SNI-MIB", "sniAttributePortIndex"),
)
if mibBuilder.loadTexts:
    sniAttributeEntry.setStatus("current")
_SniAttributeDeviceIndex_Type = Integer32
_SniAttributeDeviceIndex_Object = MibTableColumn
sniAttributeDeviceIndex = _SniAttributeDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 1),
    _SniAttributeDeviceIndex_Type()
)
sniAttributeDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniAttributeDeviceIndex.setStatus("current")
_SniAttributeCardIndex_Type = EponCardIndex
_SniAttributeCardIndex_Object = MibTableColumn
sniAttributeCardIndex = _SniAttributeCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 2),
    _SniAttributeCardIndex_Type()
)
sniAttributeCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniAttributeCardIndex.setStatus("current")
_SniAttributePortIndex_Type = EponPortIndex
_SniAttributePortIndex_Object = MibTableColumn
sniAttributePortIndex = _SniAttributePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 3),
    _SniAttributePortIndex_Type()
)
sniAttributePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniAttributePortIndex.setStatus("current")
_SniPortName_Type = DisplayString
_SniPortName_Object = MibTableColumn
sniPortName = _SniPortName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 4),
    _SniPortName_Type()
)
sniPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniPortName.setStatus("current")


class _SniAdminStatus_Type(Integer32):
    """Custom type sniAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_SniAdminStatus_Type.__name__ = "Integer32"
_SniAdminStatus_Object = MibTableColumn
sniAdminStatus = _SniAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 5),
    _SniAdminStatus_Type()
)
sniAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniAdminStatus.setStatus("current")


class _SniOperationStatus_Type(Integer32):
    """Custom type sniOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_SniOperationStatus_Type.__name__ = "Integer32"
_SniOperationStatus_Object = MibTableColumn
sniOperationStatus = _SniOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 6),
    _SniOperationStatus_Type()
)
sniOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOperationStatus.setStatus("current")


class _SniMediaType_Type(Integer32):
    """Custom type sniMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("twistedPair", 1),
          ("fiber", 2),
          ("other", 3))
    )


_SniMediaType_Type.__name__ = "Integer32"
_SniMediaType_Object = MibTableColumn
sniMediaType = _SniMediaType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 7),
    _SniMediaType_Type()
)
sniMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMediaType.setStatus("current")


class _SniAutoNegotiationStatus_Type(Integer32):
    """Custom type sniAutoNegotiationStatus based on Integer32"""
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
        *(("auto-negotiate", 1),
          ("half-10", 2),
          ("full-10", 3),
          ("half-100", 4),
          ("full-100", 5),
          ("full-1000", 6),
          ("full-10000", 7),
          ("unknown", 8))
    )


_SniAutoNegotiationStatus_Type.__name__ = "Integer32"
_SniAutoNegotiationStatus_Object = MibTableColumn
sniAutoNegotiationStatus = _SniAutoNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 8),
    _SniAutoNegotiationStatus_Type()
)
sniAutoNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniAutoNegotiationStatus.setStatus("current")


class _SniAutoNegotiationMode_Type(Integer32):
    """Custom type sniAutoNegotiationMode based on Integer32"""
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
        *(("auto-negotiate", 1),
          ("half-10", 2),
          ("full-10", 3),
          ("half-100", 4),
          ("full-100", 5),
          ("full-1000", 6),
          ("full-10000", 7))
    )


_SniAutoNegotiationMode_Type.__name__ = "Integer32"
_SniAutoNegotiationMode_Object = MibTableColumn
sniAutoNegotiationMode = _SniAutoNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 9),
    _SniAutoNegotiationMode_Type()
)
sniAutoNegotiationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniAutoNegotiationMode.setStatus("current")
_SniPerfStats15minuteEnable_Type = TruthValue
_SniPerfStats15minuteEnable_Object = MibTableColumn
sniPerfStats15minuteEnable = _SniPerfStats15minuteEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 10),
    _SniPerfStats15minuteEnable_Type()
)
sniPerfStats15minuteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniPerfStats15minuteEnable.setStatus("current")
_SniPerfStats24hourEnable_Type = TruthValue
_SniPerfStats24hourEnable_Object = MibTableColumn
sniPerfStats24hourEnable = _SniPerfStats24hourEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 11),
    _SniPerfStats24hourEnable_Type()
)
sniPerfStats24hourEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniPerfStats24hourEnable.setStatus("current")
_SniLastStatusChangeTime_Type = TimeTicks
_SniLastStatusChangeTime_Object = MibTableColumn
sniLastStatusChangeTime = _SniLastStatusChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 12),
    _SniLastStatusChangeTime_Type()
)
sniLastStatusChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLastStatusChangeTime.setStatus("current")
_SniMacAddrLearnMaxNum_Type = Integer32
_SniMacAddrLearnMaxNum_Object = MibTableColumn
sniMacAddrLearnMaxNum = _SniMacAddrLearnMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 13),
    _SniMacAddrLearnMaxNum_Type()
)
sniMacAddrLearnMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniMacAddrLearnMaxNum.setStatus("current")
_SniIsolationEnable_Type = TruthValue
_SniIsolationEnable_Object = MibTableColumn
sniIsolationEnable = _SniIsolationEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 14),
    _SniIsolationEnable_Type()
)
sniIsolationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniIsolationEnable.setStatus("current")
_SniTrunkManagement_ObjectIdentity = ObjectIdentity
sniTrunkManagement = _SniTrunkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    sniTrunkManagement.setStatus("current")
_SniTrunkGroupConfigTable_Object = MibTable
sniTrunkGroupConfigTable = _SniTrunkGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sniTrunkGroupConfigTable.setStatus("current")
_SniTrunkGroupConfigEntry_Object = MibTableRow
sniTrunkGroupConfigEntry = _SniTrunkGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 1, 1)
)
sniTrunkGroupConfigEntry.setIndexNames(
    (0, "NSCRTV-EPON-SNI-MIB", "sniTrunkGroupConfigIndex"),
)
if mibBuilder.loadTexts:
    sniTrunkGroupConfigEntry.setStatus("current")
_SniTrunkGroupConfigIndex_Type = Integer32
_SniTrunkGroupConfigIndex_Object = MibTableColumn
sniTrunkGroupConfigIndex = _SniTrunkGroupConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 1, 1, 1),
    _SniTrunkGroupConfigIndex_Type()
)
sniTrunkGroupConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniTrunkGroupConfigIndex.setStatus("current")
_SniTrunkGroupConfigName_Type = DisplayString
_SniTrunkGroupConfigName_Object = MibTableColumn
sniTrunkGroupConfigName = _SniTrunkGroupConfigName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 1, 1, 2),
    _SniTrunkGroupConfigName_Type()
)
sniTrunkGroupConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniTrunkGroupConfigName.setStatus("current")
_SniTrunkGroupConfigMember_Type = OctetString
_SniTrunkGroupConfigMember_Object = MibTableColumn
sniTrunkGroupConfigMember = _SniTrunkGroupConfigMember_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 1, 1, 3),
    _SniTrunkGroupConfigMember_Type()
)
sniTrunkGroupConfigMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniTrunkGroupConfigMember.setStatus("current")


class _SniTrunkGroupConfigPolicy_Type(Integer32):
    """Custom type sniTrunkGroupConfigPolicy based on Integer32"""
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
        *(("srcMac", 1),
          ("destMac", 2),
          ("srcMacNDestMac", 3),
          ("srcIp", 4),
          ("destIp", 5),
          ("srcIpNDestIp", 6))
    )


_SniTrunkGroupConfigPolicy_Type.__name__ = "Integer32"
_SniTrunkGroupConfigPolicy_Object = MibTableColumn
sniTrunkGroupConfigPolicy = _SniTrunkGroupConfigPolicy_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 1, 1, 4),
    _SniTrunkGroupConfigPolicy_Type()
)
sniTrunkGroupConfigPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniTrunkGroupConfigPolicy.setStatus("current")
_SniTrunkGroupConfigRowstatus_Type = RowStatus
_SniTrunkGroupConfigRowstatus_Object = MibTableColumn
sniTrunkGroupConfigRowstatus = _SniTrunkGroupConfigRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 1, 1, 5),
    _SniTrunkGroupConfigRowstatus_Type()
)
sniTrunkGroupConfigRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniTrunkGroupConfigRowstatus.setStatus("current")
_SniTrunkGroupTable_Object = MibTable
sniTrunkGroupTable = _SniTrunkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    sniTrunkGroupTable.setStatus("current")
_SniTrunkGroupEntry_Object = MibTableRow
sniTrunkGroupEntry = _SniTrunkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 2, 1)
)
sniTrunkGroupEntry.setIndexNames(
    (0, "NSCRTV-EPON-SNI-MIB", "sniTrunkGroupIndex"),
)
if mibBuilder.loadTexts:
    sniTrunkGroupEntry.setStatus("current")
_SniTrunkGroupIndex_Type = Integer32
_SniTrunkGroupIndex_Object = MibTableColumn
sniTrunkGroupIndex = _SniTrunkGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 2, 1, 1),
    _SniTrunkGroupIndex_Type()
)
sniTrunkGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniTrunkGroupIndex.setStatus("current")


class _SniTrunkGroupOperationStatus_Type(Integer32):
    """Custom type sniTrunkGroupOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_SniTrunkGroupOperationStatus_Type.__name__ = "Integer32"
_SniTrunkGroupOperationStatus_Object = MibTableColumn
sniTrunkGroupOperationStatus = _SniTrunkGroupOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 2, 1, 2),
    _SniTrunkGroupOperationStatus_Type()
)
sniTrunkGroupOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniTrunkGroupOperationStatus.setStatus("current")
_SniTrunkGroupActualSpeed_Type = Integer32
_SniTrunkGroupActualSpeed_Object = MibTableColumn
sniTrunkGroupActualSpeed = _SniTrunkGroupActualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 2, 1, 3),
    _SniTrunkGroupActualSpeed_Type()
)
sniTrunkGroupActualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniTrunkGroupActualSpeed.setStatus("current")
if mibBuilder.loadTexts:
    sniTrunkGroupActualSpeed.setUnits("Mbps")


class _SniTrunkGroupAdminStatus_Type(Integer32):
    """Custom type sniTrunkGroupAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_SniTrunkGroupAdminStatus_Type.__name__ = "Integer32"
_SniTrunkGroupAdminStatus_Object = MibTableColumn
sniTrunkGroupAdminStatus = _SniTrunkGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 2, 1, 4),
    _SniTrunkGroupAdminStatus_Type()
)
sniTrunkGroupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniTrunkGroupAdminStatus.setStatus("current")
_SniMirrorTable_Object = MibTable
sniMirrorTable = _SniMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 3)
)
if mibBuilder.loadTexts:
    sniMirrorTable.setStatus("current")
_SniMirrorEntry_Object = MibTableRow
sniMirrorEntry = _SniMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 3, 1)
)
sniMirrorEntry.setIndexNames(
    (0, "NSCRTV-EPON-SNI-MIB", "sniMirrorGroupIndex"),
)
if mibBuilder.loadTexts:
    sniMirrorEntry.setStatus("current")
_SniMirrorGroupIndex_Type = Integer32
_SniMirrorGroupIndex_Object = MibTableColumn
sniMirrorGroupIndex = _SniMirrorGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 3, 1, 1),
    _SniMirrorGroupIndex_Type()
)
sniMirrorGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniMirrorGroupIndex.setStatus("current")
_SniMirrorGroupName_Type = DisplayString
_SniMirrorGroupName_Object = MibTableColumn
sniMirrorGroupName = _SniMirrorGroupName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 3, 1, 2),
    _SniMirrorGroupName_Type()
)
sniMirrorGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMirrorGroupName.setStatus("current")
_SniMirrorGroupDstPortList_Type = OctetString
_SniMirrorGroupDstPortList_Object = MibTableColumn
sniMirrorGroupDstPortList = _SniMirrorGroupDstPortList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 3, 1, 3),
    _SniMirrorGroupDstPortList_Type()
)
sniMirrorGroupDstPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMirrorGroupDstPortList.setStatus("current")
_SniMirrorGroupSrcInPortList_Type = OctetString
_SniMirrorGroupSrcInPortList_Object = MibTableColumn
sniMirrorGroupSrcInPortList = _SniMirrorGroupSrcInPortList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 3, 1, 4),
    _SniMirrorGroupSrcInPortList_Type()
)
sniMirrorGroupSrcInPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMirrorGroupSrcInPortList.setStatus("current")
_SniMirrorGroupSrcOutPortList_Type = OctetString
_SniMirrorGroupSrcOutPortList_Object = MibTableColumn
sniMirrorGroupSrcOutPortList = _SniMirrorGroupSrcOutPortList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 3, 1, 5),
    _SniMirrorGroupSrcOutPortList_Type()
)
sniMirrorGroupSrcOutPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMirrorGroupSrcOutPortList.setStatus("current")
_SniMirrorGroupRowstatus_Type = RowStatus
_SniMirrorGroupRowstatus_Object = MibTableColumn
sniMirrorGroupRowstatus = _SniMirrorGroupRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 3, 1, 6),
    _SniMirrorGroupRowstatus_Type()
)
sniMirrorGroupRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMirrorGroupRowstatus.setStatus("current")
_SniMacAddressManagement_ObjectIdentity = ObjectIdentity
sniMacAddressManagement = _SniMacAddressManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4)
)
if mibBuilder.loadTexts:
    sniMacAddressManagement.setStatus("current")
_SniMacAddressManagementTable_Object = MibTable
sniMacAddressManagementTable = _SniMacAddressManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    sniMacAddressManagementTable.setStatus("current")
_SniMacAddressManagementEntry_Object = MibTableRow
sniMacAddressManagementEntry = _SniMacAddressManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 1, 1)
)
sniMacAddressManagementEntry.setIndexNames(
    (0, "NSCRTV-EPON-SNI-MIB", "sniMacAddressManagementDeviceIndex"),
)
if mibBuilder.loadTexts:
    sniMacAddressManagementEntry.setStatus("current")
_SniMacAddressManagementDeviceIndex_Type = Integer32
_SniMacAddressManagementDeviceIndex_Object = MibTableColumn
sniMacAddressManagementDeviceIndex = _SniMacAddressManagementDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 1, 1, 1),
    _SniMacAddressManagementDeviceIndex_Type()
)
sniMacAddressManagementDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniMacAddressManagementDeviceIndex.setStatus("current")
_SniMacAddrTableAgingTime_Type = Integer32
_SniMacAddrTableAgingTime_Object = MibTableColumn
sniMacAddrTableAgingTime = _SniMacAddrTableAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 1, 1, 2),
    _SniMacAddrTableAgingTime_Type()
)
sniMacAddrTableAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniMacAddrTableAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    sniMacAddrTableAgingTime.setUnits("Seconds")


class _SniMacAddrTableClear_Type(Integer32):
    """Custom type sniMacAddrTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("allDynamic", 1)
    )


_SniMacAddrTableClear_Type.__name__ = "Integer32"
_SniMacAddrTableClear_Object = MibTableColumn
sniMacAddrTableClear = _SniMacAddrTableClear_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 1, 1, 3),
    _SniMacAddrTableClear_Type()
)
sniMacAddrTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniMacAddrTableClear.setStatus("current")
_SniMacAddressTable_Object = MibTable
sniMacAddressTable = _SniMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 2)
)
if mibBuilder.loadTexts:
    sniMacAddressTable.setStatus("current")
_SniMacAddressEntry_Object = MibTableRow
sniMacAddressEntry = _SniMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 2, 1)
)
sniMacAddressEntry.setIndexNames(
    (0, "NSCRTV-EPON-SNI-MIB", "sniMacAddrIndex"),
    (0, "NSCRTV-EPON-SNI-MIB", "sniMacAddrVlanIdIndex"),
)
if mibBuilder.loadTexts:
    sniMacAddressEntry.setStatus("current")
_SniMacAddrIndex_Type = MacAddress
_SniMacAddrIndex_Object = MibTableColumn
sniMacAddrIndex = _SniMacAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 2, 1, 1),
    _SniMacAddrIndex_Type()
)
sniMacAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniMacAddrIndex.setStatus("current")
_SniMacAddrVlanIdIndex_Type = Integer32
_SniMacAddrVlanIdIndex_Object = MibTableColumn
sniMacAddrVlanIdIndex = _SniMacAddrVlanIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 2, 1, 2),
    _SniMacAddrVlanIdIndex_Type()
)
sniMacAddrVlanIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniMacAddrVlanIdIndex.setStatus("current")


class _SniMacAddrType_Type(Integer32):
    """Custom type sniMacAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2),
          ("other", 3))
    )


_SniMacAddrType_Type.__name__ = "Integer32"
_SniMacAddrType_Object = MibTableColumn
sniMacAddrType = _SniMacAddrType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 2, 1, 3),
    _SniMacAddrType_Type()
)
sniMacAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMacAddrType.setStatus("current")
_SniMacAddrPortId_Type = EponDeviceIndex
_SniMacAddrPortId_Object = MibTableColumn
sniMacAddrPortId = _SniMacAddrPortId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 2, 1, 4),
    _SniMacAddrPortId_Type()
)
sniMacAddrPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMacAddrPortId.setStatus("current")
_SniMacAddrRowStatus_Type = RowStatus
_SniMacAddrRowStatus_Object = MibTableColumn
sniMacAddrRowStatus = _SniMacAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 2, 1, 5),
    _SniMacAddrRowStatus_Type()
)
sniMacAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMacAddrRowStatus.setStatus("current")
_SniBroadcastStormSuppressionTable_Object = MibTable
sniBroadcastStormSuppressionTable = _SniBroadcastStormSuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5)
)
if mibBuilder.loadTexts:
    sniBroadcastStormSuppressionTable.setStatus("current")
_SniBroadcastStormSuppressionEntry_Object = MibTableRow
sniBroadcastStormSuppressionEntry = _SniBroadcastStormSuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1)
)
sniBroadcastStormSuppressionEntry.setIndexNames(
    (0, "NSCRTV-EPON-SNI-MIB", "sniBroadcastStormSuppressionDeviceIndex"),
    (0, "NSCRTV-EPON-SNI-MIB", "sniBroadcastStormSuppressionCardIndex"),
    (0, "NSCRTV-EPON-SNI-MIB", "sniBroadcastStormSuppressionPortIndex"),
)
if mibBuilder.loadTexts:
    sniBroadcastStormSuppressionEntry.setStatus("current")
_SniBroadcastStormSuppressionDeviceIndex_Type = Integer32
_SniBroadcastStormSuppressionDeviceIndex_Object = MibTableColumn
sniBroadcastStormSuppressionDeviceIndex = _SniBroadcastStormSuppressionDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 1),
    _SniBroadcastStormSuppressionDeviceIndex_Type()
)
sniBroadcastStormSuppressionDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniBroadcastStormSuppressionDeviceIndex.setStatus("current")
_SniBroadcastStormSuppressionCardIndex_Type = EponCardIndex
_SniBroadcastStormSuppressionCardIndex_Object = MibTableColumn
sniBroadcastStormSuppressionCardIndex = _SniBroadcastStormSuppressionCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 2),
    _SniBroadcastStormSuppressionCardIndex_Type()
)
sniBroadcastStormSuppressionCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniBroadcastStormSuppressionCardIndex.setStatus("current")
_SniBroadcastStormSuppressionPortIndex_Type = EponPortIndex
_SniBroadcastStormSuppressionPortIndex_Object = MibTableColumn
sniBroadcastStormSuppressionPortIndex = _SniBroadcastStormSuppressionPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 3),
    _SniBroadcastStormSuppressionPortIndex_Type()
)
sniBroadcastStormSuppressionPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniBroadcastStormSuppressionPortIndex.setStatus("current")
_SniUnicastStormEnable_Type = TruthValue
_SniUnicastStormEnable_Object = MibTableColumn
sniUnicastStormEnable = _SniUnicastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 4),
    _SniUnicastStormEnable_Type()
)
sniUnicastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniUnicastStormEnable.setStatus("current")
_SniUnicastStormInPacketRate_Type = Integer32
_SniUnicastStormInPacketRate_Object = MibTableColumn
sniUnicastStormInPacketRate = _SniUnicastStormInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 5),
    _SniUnicastStormInPacketRate_Type()
)
sniUnicastStormInPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniUnicastStormInPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    sniUnicastStormInPacketRate.setUnits("pps")
_SniUnicastStormOutPacketRate_Type = Integer32
_SniUnicastStormOutPacketRate_Object = MibTableColumn
sniUnicastStormOutPacketRate = _SniUnicastStormOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 6),
    _SniUnicastStormOutPacketRate_Type()
)
sniUnicastStormOutPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniUnicastStormOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    sniUnicastStormOutPacketRate.setUnits("pps")
_SniMulticastStormEnable_Type = TruthValue
_SniMulticastStormEnable_Object = MibTableColumn
sniMulticastStormEnable = _SniMulticastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 7),
    _SniMulticastStormEnable_Type()
)
sniMulticastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniMulticastStormEnable.setStatus("current")
_SniMulticastStormInPacketRate_Type = Integer32
_SniMulticastStormInPacketRate_Object = MibTableColumn
sniMulticastStormInPacketRate = _SniMulticastStormInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 8),
    _SniMulticastStormInPacketRate_Type()
)
sniMulticastStormInPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniMulticastStormInPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    sniMulticastStormInPacketRate.setUnits("pps")
_SniMulticastStormOutPacketRate_Type = Integer32
_SniMulticastStormOutPacketRate_Object = MibTableColumn
sniMulticastStormOutPacketRate = _SniMulticastStormOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 9),
    _SniMulticastStormOutPacketRate_Type()
)
sniMulticastStormOutPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniMulticastStormOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    sniMulticastStormOutPacketRate.setUnits("pps")
_SniBroadcastStormEnable_Type = TruthValue
_SniBroadcastStormEnable_Object = MibTableColumn
sniBroadcastStormEnable = _SniBroadcastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 10),
    _SniBroadcastStormEnable_Type()
)
sniBroadcastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniBroadcastStormEnable.setStatus("current")
_SniBroadcastStormInPacketRate_Type = Integer32
_SniBroadcastStormInPacketRate_Object = MibTableColumn
sniBroadcastStormInPacketRate = _SniBroadcastStormInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 11),
    _SniBroadcastStormInPacketRate_Type()
)
sniBroadcastStormInPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniBroadcastStormInPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    sniBroadcastStormInPacketRate.setUnits("pps")
_SniBroadcastStormOutPacketRate_Type = Integer32
_SniBroadcastStormOutPacketRate_Object = MibTableColumn
sniBroadcastStormOutPacketRate = _SniBroadcastStormOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 12),
    _SniBroadcastStormOutPacketRate_Type()
)
sniBroadcastStormOutPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniBroadcastStormOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    sniBroadcastStormOutPacketRate.setUnits("pps")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-EPON-SNI-MIB",
    **{"sniAttributeTable": sniAttributeTable,
       "sniAttributeEntry": sniAttributeEntry,
       "sniAttributeDeviceIndex": sniAttributeDeviceIndex,
       "sniAttributeCardIndex": sniAttributeCardIndex,
       "sniAttributePortIndex": sniAttributePortIndex,
       "sniPortName": sniPortName,
       "sniAdminStatus": sniAdminStatus,
       "sniOperationStatus": sniOperationStatus,
       "sniMediaType": sniMediaType,
       "sniAutoNegotiationStatus": sniAutoNegotiationStatus,
       "sniAutoNegotiationMode": sniAutoNegotiationMode,
       "sniPerfStats15minuteEnable": sniPerfStats15minuteEnable,
       "sniPerfStats24hourEnable": sniPerfStats24hourEnable,
       "sniLastStatusChangeTime": sniLastStatusChangeTime,
       "sniMacAddrLearnMaxNum": sniMacAddrLearnMaxNum,
       "sniIsolationEnable": sniIsolationEnable,
       "sniTrunkManagement": sniTrunkManagement,
       "sniTrunkGroupConfigTable": sniTrunkGroupConfigTable,
       "sniTrunkGroupConfigEntry": sniTrunkGroupConfigEntry,
       "sniTrunkGroupConfigIndex": sniTrunkGroupConfigIndex,
       "sniTrunkGroupConfigName": sniTrunkGroupConfigName,
       "sniTrunkGroupConfigMember": sniTrunkGroupConfigMember,
       "sniTrunkGroupConfigPolicy": sniTrunkGroupConfigPolicy,
       "sniTrunkGroupConfigRowstatus": sniTrunkGroupConfigRowstatus,
       "sniTrunkGroupTable": sniTrunkGroupTable,
       "sniTrunkGroupEntry": sniTrunkGroupEntry,
       "sniTrunkGroupIndex": sniTrunkGroupIndex,
       "sniTrunkGroupOperationStatus": sniTrunkGroupOperationStatus,
       "sniTrunkGroupActualSpeed": sniTrunkGroupActualSpeed,
       "sniTrunkGroupAdminStatus": sniTrunkGroupAdminStatus,
       "sniMirrorTable": sniMirrorTable,
       "sniMirrorEntry": sniMirrorEntry,
       "sniMirrorGroupIndex": sniMirrorGroupIndex,
       "sniMirrorGroupName": sniMirrorGroupName,
       "sniMirrorGroupDstPortList": sniMirrorGroupDstPortList,
       "sniMirrorGroupSrcInPortList": sniMirrorGroupSrcInPortList,
       "sniMirrorGroupSrcOutPortList": sniMirrorGroupSrcOutPortList,
       "sniMirrorGroupRowstatus": sniMirrorGroupRowstatus,
       "sniMacAddressManagement": sniMacAddressManagement,
       "sniMacAddressManagementTable": sniMacAddressManagementTable,
       "sniMacAddressManagementEntry": sniMacAddressManagementEntry,
       "sniMacAddressManagementDeviceIndex": sniMacAddressManagementDeviceIndex,
       "sniMacAddrTableAgingTime": sniMacAddrTableAgingTime,
       "sniMacAddrTableClear": sniMacAddrTableClear,
       "sniMacAddressTable": sniMacAddressTable,
       "sniMacAddressEntry": sniMacAddressEntry,
       "sniMacAddrIndex": sniMacAddrIndex,
       "sniMacAddrVlanIdIndex": sniMacAddrVlanIdIndex,
       "sniMacAddrType": sniMacAddrType,
       "sniMacAddrPortId": sniMacAddrPortId,
       "sniMacAddrRowStatus": sniMacAddrRowStatus,
       "sniBroadcastStormSuppressionTable": sniBroadcastStormSuppressionTable,
       "sniBroadcastStormSuppressionEntry": sniBroadcastStormSuppressionEntry,
       "sniBroadcastStormSuppressionDeviceIndex": sniBroadcastStormSuppressionDeviceIndex,
       "sniBroadcastStormSuppressionCardIndex": sniBroadcastStormSuppressionCardIndex,
       "sniBroadcastStormSuppressionPortIndex": sniBroadcastStormSuppressionPortIndex,
       "sniUnicastStormEnable": sniUnicastStormEnable,
       "sniUnicastStormInPacketRate": sniUnicastStormInPacketRate,
       "sniUnicastStormOutPacketRate": sniUnicastStormOutPacketRate,
       "sniMulticastStormEnable": sniMulticastStormEnable,
       "sniMulticastStormInPacketRate": sniMulticastStormInPacketRate,
       "sniMulticastStormOutPacketRate": sniMulticastStormOutPacketRate,
       "sniBroadcastStormEnable": sniBroadcastStormEnable,
       "sniBroadcastStormInPacketRate": sniBroadcastStormInPacketRate,
       "sniBroadcastStormOutPacketRate": sniBroadcastStormOutPacketRate}
)
