# SNMP MIB module (DLINKSW-L2FDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-L2FDB-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:25 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(PortList,
 VlanId,
 dot1qFdbId,
 dot1qStaticUnicastAddress) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId",
    "dot1qFdbId",
    "dot1qStaticUnicastAddress")

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


# MODULE-IDENTITY

dlinkSwL2FdbMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 3)
)
if mibBuilder.loadTexts:
    dlinkSwL2FdbMIB.setRevisions(
        ("2012-12-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DL2FdbMIBNotifications_ObjectIdentity = ObjectIdentity
dL2FdbMIBNotifications = _DL2FdbMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 0)
)
_DL2FdbMIBObjects_ObjectIdentity = ObjectIdentity
dL2FdbMIBObjects = _DL2FdbMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1)
)
_DL2FdbGblCtrl_ObjectIdentity = ObjectIdentity
dL2FdbGblCtrl = _DL2FdbGblCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 1)
)
_DL2FdbClearCtrl_ObjectIdentity = ObjectIdentity
dL2FdbClearCtrl = _DL2FdbClearCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 1, 1)
)
_DL2FdbClearMacAddrByMacAddr_Type = MacAddress
_DL2FdbClearMacAddrByMacAddr_Object = MibScalar
dL2FdbClearMacAddrByMacAddr = _DL2FdbClearMacAddrByMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 1, 1, 1),
    _DL2FdbClearMacAddrByMacAddr_Type()
)
dL2FdbClearMacAddrByMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dL2FdbClearMacAddrByMacAddr.setStatus("current")
_DL2FdbClearMacAddrByIf_Type = InterfaceIndexOrZero
_DL2FdbClearMacAddrByIf_Object = MibScalar
dL2FdbClearMacAddrByIf = _DL2FdbClearMacAddrByIf_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 1, 1, 2),
    _DL2FdbClearMacAddrByIf_Type()
)
dL2FdbClearMacAddrByIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dL2FdbClearMacAddrByIf.setStatus("current")


class _DL2FdbClearAllMacAddr_Type(Integer32):
    """Custom type dL2FdbClearAllMacAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DL2FdbClearAllMacAddr_Type.__name__ = "Integer32"
_DL2FdbClearAllMacAddr_Object = MibScalar
dL2FdbClearAllMacAddr = _DL2FdbClearAllMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 1, 1, 3),
    _DL2FdbClearAllMacAddr_Type()
)
dL2FdbClearAllMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dL2FdbClearAllMacAddr.setStatus("current")


class _DL2FdbAgingTime_Type(Unsigned32):
    """Custom type dL2FdbAgingTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 1000000),
    )


_DL2FdbAgingTime_Type.__name__ = "Unsigned32"
_DL2FdbAgingTime_Object = MibScalar
dL2FdbAgingTime = _DL2FdbAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 1, 2),
    _DL2FdbAgingTime_Type()
)
dL2FdbAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dL2FdbAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    dL2FdbAgingTime.setUnits("second")


class _DL2FdbMacChangeEnabled_Type(TruthValue):
    """Custom type dL2FdbMacChangeEnabled based on TruthValue"""
    defaultValue = 2


_DL2FdbMacChangeEnabled_Type.__name__ = "TruthValue"
_DL2FdbMacChangeEnabled_Object = MibScalar
dL2FdbMacChangeEnabled = _DL2FdbMacChangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 1, 3),
    _DL2FdbMacChangeEnabled_Type()
)
dL2FdbMacChangeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dL2FdbMacChangeEnabled.setStatus("current")


class _DL2FdbMacChangeNotifInterval_Type(Unsigned32):
    """Custom type dL2FdbMacChangeNotifInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DL2FdbMacChangeNotifInterval_Type.__name__ = "Unsigned32"
_DL2FdbMacChangeNotifInterval_Object = MibScalar
dL2FdbMacChangeNotifInterval = _DL2FdbMacChangeNotifInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 1, 4),
    _DL2FdbMacChangeNotifInterval_Type()
)
dL2FdbMacChangeNotifInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dL2FdbMacChangeNotifInterval.setStatus("current")
if mibBuilder.loadTexts:
    dL2FdbMacChangeNotifInterval.setUnits("second")


class _DL2FdbMacChangeNotifyEnabled_Type(TruthValue):
    """Custom type dL2FdbMacChangeNotifyEnabled based on TruthValue"""
    defaultValue = 2


_DL2FdbMacChangeNotifyEnabled_Type.__name__ = "TruthValue"
_DL2FdbMacChangeNotifyEnabled_Object = MibScalar
dL2FdbMacChangeNotifyEnabled = _DL2FdbMacChangeNotifyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 1, 5),
    _DL2FdbMacChangeNotifyEnabled_Type()
)
dL2FdbMacChangeNotifyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dL2FdbMacChangeNotifyEnabled.setStatus("current")


class _DL2FdbMacChangeHistorySize_Type(Unsigned32):
    """Custom type dL2FdbMacChangeHistorySize based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_DL2FdbMacChangeHistorySize_Type.__name__ = "Unsigned32"
_DL2FdbMacChangeHistorySize_Object = MibScalar
dL2FdbMacChangeHistorySize = _DL2FdbMacChangeHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 1, 6),
    _DL2FdbMacChangeHistorySize_Type()
)
dL2FdbMacChangeHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dL2FdbMacChangeHistorySize.setStatus("current")


class _DL2FdbDestHitEnabled_Type(TruthValue):
    """Custom type dL2FdbDestHitEnabled based on TruthValue"""
    defaultValue = 2


_DL2FdbDestHitEnabled_Type.__name__ = "TruthValue"
_DL2FdbDestHitEnabled_Object = MibScalar
dL2FdbDestHitEnabled = _DL2FdbDestHitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 1, 7),
    _DL2FdbDestHitEnabled_Type()
)
dL2FdbDestHitEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dL2FdbDestHitEnabled.setStatus("current")
_DL2FdbStaticUnicastTable_Object = MibTable
dL2FdbStaticUnicastTable = _DL2FdbStaticUnicastTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 2)
)
if mibBuilder.loadTexts:
    dL2FdbStaticUnicastTable.setStatus("current")
_DL2FdbStaticUnicastEntry_Object = MibTableRow
dL2FdbStaticUnicastEntry = _DL2FdbStaticUnicastEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 2, 1)
)
dL2FdbStaticUnicastEntry.setIndexNames(
    (0, "DLINKSW-L2FDB-MIB", "dL2FdbStaticUnicastVlanID"),
    (0, "DLINKSW-L2FDB-MIB", "dL2FdbStaticUnicastMacAddr"),
)
if mibBuilder.loadTexts:
    dL2FdbStaticUnicastEntry.setStatus("current")
_DL2FdbStaticUnicastVlanID_Type = VlanId
_DL2FdbStaticUnicastVlanID_Object = MibTableColumn
dL2FdbStaticUnicastVlanID = _DL2FdbStaticUnicastVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 2, 1, 1),
    _DL2FdbStaticUnicastVlanID_Type()
)
dL2FdbStaticUnicastVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dL2FdbStaticUnicastVlanID.setStatus("current")
_DL2FdbStaticUnicastMacAddr_Type = MacAddress
_DL2FdbStaticUnicastMacAddr_Object = MibTableColumn
dL2FdbStaticUnicastMacAddr = _DL2FdbStaticUnicastMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 2, 1, 2),
    _DL2FdbStaticUnicastMacAddr_Type()
)
dL2FdbStaticUnicastMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dL2FdbStaticUnicastMacAddr.setStatus("current")


class _DL2FdbStaticUnicastType_Type(Integer32):
    """Custom type dL2FdbStaticUnicastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("self", 1),
          ("permanent", 2),
          ("permanentDrop", 3))
    )


_DL2FdbStaticUnicastType_Type.__name__ = "Integer32"
_DL2FdbStaticUnicastType_Object = MibTableColumn
dL2FdbStaticUnicastType = _DL2FdbStaticUnicastType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 2, 1, 3),
    _DL2FdbStaticUnicastType_Type()
)
dL2FdbStaticUnicastType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dL2FdbStaticUnicastType.setStatus("current")
_DL2FdbStaticUnicastPortNum_Type = Integer32
_DL2FdbStaticUnicastPortNum_Object = MibTableColumn
dL2FdbStaticUnicastPortNum = _DL2FdbStaticUnicastPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 2, 1, 4),
    _DL2FdbStaticUnicastPortNum_Type()
)
dL2FdbStaticUnicastPortNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dL2FdbStaticUnicastPortNum.setStatus("current")
_DL2FdbStaticUnicastRowStatus_Type = RowStatus
_DL2FdbStaticUnicastRowStatus_Object = MibTableColumn
dL2FdbStaticUnicastRowStatus = _DL2FdbStaticUnicastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 2, 1, 5),
    _DL2FdbStaticUnicastRowStatus_Type()
)
dL2FdbStaticUnicastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dL2FdbStaticUnicastRowStatus.setStatus("current")
_DL2FdbIfCtrlTable_Object = MibTable
dL2FdbIfCtrlTable = _DL2FdbIfCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 3)
)
if mibBuilder.loadTexts:
    dL2FdbIfCtrlTable.setStatus("current")
_DL2FdbIfCtrlEntry_Object = MibTableRow
dL2FdbIfCtrlEntry = _DL2FdbIfCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 3, 1)
)
dL2FdbIfCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dL2FdbIfCtrlEntry.setStatus("current")


class _DL2FdbIfCtrlNotifyEnable_Type(Bits):
    """Custom type dL2FdbIfCtrlNotifyEnable based on Bits"""
    namedValues = NamedValues(
        *(("added", 0),
          ("removed", 1))
    )

_DL2FdbIfCtrlNotifyEnable_Type.__name__ = "Bits"
_DL2FdbIfCtrlNotifyEnable_Object = MibTableColumn
dL2FdbIfCtrlNotifyEnable = _DL2FdbIfCtrlNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 3, 1, 1),
    _DL2FdbIfCtrlNotifyEnable_Type()
)
dL2FdbIfCtrlNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dL2FdbIfCtrlNotifyEnable.setStatus("current")
_DL2FdbIfMacLearningEnabled_Type = TruthValue
_DL2FdbIfMacLearningEnabled_Object = MibTableColumn
dL2FdbIfMacLearningEnabled = _DL2FdbIfMacLearningEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 3, 1, 2),
    _DL2FdbIfMacLearningEnabled_Type()
)
dL2FdbIfMacLearningEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dL2FdbIfMacLearningEnabled.setStatus("current")
_DL2FdbMulticastFilterModeTable_Object = MibTable
dL2FdbMulticastFilterModeTable = _DL2FdbMulticastFilterModeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 4)
)
if mibBuilder.loadTexts:
    dL2FdbMulticastFilterModeTable.setStatus("current")
_DL2FdbMulticastFilterModeEntry_Object = MibTableRow
dL2FdbMulticastFilterModeEntry = _DL2FdbMulticastFilterModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 4, 1)
)
dL2FdbMulticastFilterModeEntry.setIndexNames(
    (0, "DLINKSW-L2FDB-MIB", "dL2FdbMcastFilterModeIfIndex"),
)
if mibBuilder.loadTexts:
    dL2FdbMulticastFilterModeEntry.setStatus("current")
_DL2FdbMcastFilterModeIfIndex_Type = InterfaceIndex
_DL2FdbMcastFilterModeIfIndex_Object = MibTableColumn
dL2FdbMcastFilterModeIfIndex = _DL2FdbMcastFilterModeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 4, 1, 1),
    _DL2FdbMcastFilterModeIfIndex_Type()
)
dL2FdbMcastFilterModeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dL2FdbMcastFilterModeIfIndex.setStatus("current")


class _DL2FdbMcastFilterMode_Type(Integer32):
    """Custom type dL2FdbMcastFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forwardAll", 1),
          ("forwardUnregistered", 2),
          ("filterUnregistered", 3))
    )


_DL2FdbMcastFilterMode_Type.__name__ = "Integer32"
_DL2FdbMcastFilterMode_Object = MibTableColumn
dL2FdbMcastFilterMode = _DL2FdbMcastFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 4, 1, 2),
    _DL2FdbMcastFilterMode_Type()
)
dL2FdbMcastFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dL2FdbMcastFilterMode.setStatus("current")
_DL2FdbMacChangeHistoryTable_Object = MibTable
dL2FdbMacChangeHistoryTable = _DL2FdbMacChangeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 5)
)
if mibBuilder.loadTexts:
    dL2FdbMacChangeHistoryTable.setStatus("current")
_DL2FdbMacChangeHistoryEntry_Object = MibTableRow
dL2FdbMacChangeHistoryEntry = _DL2FdbMacChangeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 5, 1)
)
dL2FdbMacChangeHistoryEntry.setIndexNames(
    (0, "DLINKSW-L2FDB-MIB", "dL2FdbMacChangeHistoryIndex"),
)
if mibBuilder.loadTexts:
    dL2FdbMacChangeHistoryEntry.setStatus("current")


class _DL2FdbMacChangeHistoryIndex_Type(Unsigned32):
    """Custom type dL2FdbMacChangeHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_DL2FdbMacChangeHistoryIndex_Type.__name__ = "Unsigned32"
_DL2FdbMacChangeHistoryIndex_Object = MibTableColumn
dL2FdbMacChangeHistoryIndex = _DL2FdbMacChangeHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 5, 1, 1),
    _DL2FdbMacChangeHistoryIndex_Type()
)
dL2FdbMacChangeHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dL2FdbMacChangeHistoryIndex.setStatus("current")


class _DL2FdbMacChangeHistoryOp_Type(Integer32):
    """Custom type dL2FdbMacChangeHistoryOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("added", 1),
          ("removed", 2))
    )


_DL2FdbMacChangeHistoryOp_Type.__name__ = "Integer32"
_DL2FdbMacChangeHistoryOp_Object = MibTableColumn
dL2FdbMacChangeHistoryOp = _DL2FdbMacChangeHistoryOp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 5, 1, 2),
    _DL2FdbMacChangeHistoryOp_Type()
)
dL2FdbMacChangeHistoryOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dL2FdbMacChangeHistoryOp.setStatus("current")
_DL2FdbMacChangeHistoryVlanID_Type = VlanId
_DL2FdbMacChangeHistoryVlanID_Object = MibTableColumn
dL2FdbMacChangeHistoryVlanID = _DL2FdbMacChangeHistoryVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 5, 1, 3),
    _DL2FdbMacChangeHistoryVlanID_Type()
)
dL2FdbMacChangeHistoryVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dL2FdbMacChangeHistoryVlanID.setStatus("current")
_DL2FdbMacChangeHistoryMacAddr_Type = MacAddress
_DL2FdbMacChangeHistoryMacAddr_Object = MibTableColumn
dL2FdbMacChangeHistoryMacAddr = _DL2FdbMacChangeHistoryMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 5, 1, 4),
    _DL2FdbMacChangeHistoryMacAddr_Type()
)
dL2FdbMacChangeHistoryMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dL2FdbMacChangeHistoryMacAddr.setStatus("current")
_DL2FdbMacChangeHistoryPortNum_Type = Integer32
_DL2FdbMacChangeHistoryPortNum_Object = MibTableColumn
dL2FdbMacChangeHistoryPortNum = _DL2FdbMacChangeHistoryPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 5, 1, 5),
    _DL2FdbMacChangeHistoryPortNum_Type()
)
dL2FdbMacChangeHistoryPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dL2FdbMacChangeHistoryPortNum.setStatus("current")
_DL2FdbNotifyInfo_ObjectIdentity = ObjectIdentity
dL2FdbNotifyInfo = _DL2FdbNotifyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 6)
)


class _DL2FdbMacChangeNotifyInfo_Type(OctetString):
    """Custom type dL2FdbMacChangeNotifyInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_DL2FdbMacChangeNotifyInfo_Type.__name__ = "OctetString"
_DL2FdbMacChangeNotifyInfo_Object = MibScalar
dL2FdbMacChangeNotifyInfo = _DL2FdbMacChangeNotifyInfo_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 1, 6, 1),
    _DL2FdbMacChangeNotifyInfo_Type()
)
dL2FdbMacChangeNotifyInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dL2FdbMacChangeNotifyInfo.setStatus("current")
_DL2FdbMIBConformance_ObjectIdentity = ObjectIdentity
dL2FdbMIBConformance = _DL2FdbMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 2)
)
_DL2FdbCompliances_ObjectIdentity = ObjectIdentity
dL2FdbCompliances = _DL2FdbCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 2, 1)
)
_DL2FdbGroups_ObjectIdentity = ObjectIdentity
dL2FdbGroups = _DL2FdbGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 2, 2)
)

# Managed Objects groups

dL2FdbGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 2, 2, 1)
)
dL2FdbGlobalGroup.setObjects(
      *(("DLINKSW-L2FDB-MIB", "dL2FdbClearMacAddrByMacAddr"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbClearMacAddrByIf"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbClearAllMacAddr"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbAgingTime"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbDestHitEnabled"))
)
if mibBuilder.loadTexts:
    dL2FdbGlobalGroup.setStatus("current")

dL2FdbMacAddrTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 2, 2, 2)
)
dL2FdbMacAddrTableGroup.setObjects(
      *(("DLINKSW-L2FDB-MIB", "dL2FdbStaticUnicastType"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbStaticUnicastPortNum"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbStaticUnicastRowStatus"))
)
if mibBuilder.loadTexts:
    dL2FdbMacAddrTableGroup.setStatus("current")

dL2FdbInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 2, 2, 3)
)
dL2FdbInterfaceGroup.setObjects(
    ("DLINKSW-L2FDB-MIB", "dL2FdbIfMacLearningEnabled")
)
if mibBuilder.loadTexts:
    dL2FdbInterfaceGroup.setStatus("current")

dL2FdbMacChangeNotifyCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 2, 2, 4)
)
dL2FdbMacChangeNotifyCfgGroup.setObjects(
      *(("DLINKSW-L2FDB-MIB", "dL2FdbMacChangeEnabled"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbMacChangeNotifInterval"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbMacChangeNotifyEnabled"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbMacChangeHistorySize"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbMacChangeNotifyInfo"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbIfCtrlNotifyEnable"))
)
if mibBuilder.loadTexts:
    dL2FdbMacChangeNotifyCfgGroup.setStatus("current")

dL2FdbMcastFilterModeCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 2, 2, 5)
)
dL2FdbMcastFilterModeCfgGroup.setObjects(
    ("DLINKSW-L2FDB-MIB", "dL2FdbMcastFilterMode")
)
if mibBuilder.loadTexts:
    dL2FdbMcastFilterModeCfgGroup.setStatus("current")

dL2FdbMacChangeNotifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 2, 2, 6)
)
dL2FdbMacChangeNotifyGroup.setObjects(
      *(("DLINKSW-L2FDB-MIB", "dL2FdbMacChangeHistoryOp"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbMacChangeHistoryVlanID"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbMacChangeHistoryMacAddr"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbMacChangeHistoryPortNum"))
)
if mibBuilder.loadTexts:
    dL2FdbMacChangeNotifyGroup.setStatus("current")


# Notification objects

dL2FdbMacNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 0, 1)
)
dL2FdbMacNotification.setObjects(
    ("DLINKSW-L2FDB-MIB", "dL2FdbMacChangeNotifyInfo")
)
if mibBuilder.loadTexts:
    dL2FdbMacNotification.setStatus(
        "current"
    )


# Notifications groups

dL2FdbMacChgNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 2, 2, 7)
)
dL2FdbMacChgNotificationGroup.setObjects(
    ("DLINKSW-L2FDB-MIB", "dL2FdbMacNotification")
)
if mibBuilder.loadTexts:
    dL2FdbMacChgNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dL2FdbCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 3, 2, 1, 1)
)
dL2FdbCompliance.setObjects(
      *(("DLINKSW-L2FDB-MIB", "dL2FdbGlobalGroup"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbMacAddrTableGroup"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbInterfaceGroup"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbMcastFilterModeCfgGroup"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbMacChangeNotifyCfgGroup"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbMacChangeNotifyGroup"),
        ("DLINKSW-L2FDB-MIB", "dL2FdbMacChgNotificationGroup"))
)
if mibBuilder.loadTexts:
    dL2FdbCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-L2FDB-MIB",
    **{"dlinkSwL2FdbMIB": dlinkSwL2FdbMIB,
       "dL2FdbMIBNotifications": dL2FdbMIBNotifications,
       "dL2FdbMacNotification": dL2FdbMacNotification,
       "dL2FdbMIBObjects": dL2FdbMIBObjects,
       "dL2FdbGblCtrl": dL2FdbGblCtrl,
       "dL2FdbClearCtrl": dL2FdbClearCtrl,
       "dL2FdbClearMacAddrByMacAddr": dL2FdbClearMacAddrByMacAddr,
       "dL2FdbClearMacAddrByIf": dL2FdbClearMacAddrByIf,
       "dL2FdbClearAllMacAddr": dL2FdbClearAllMacAddr,
       "dL2FdbAgingTime": dL2FdbAgingTime,
       "dL2FdbMacChangeEnabled": dL2FdbMacChangeEnabled,
       "dL2FdbMacChangeNotifInterval": dL2FdbMacChangeNotifInterval,
       "dL2FdbMacChangeNotifyEnabled": dL2FdbMacChangeNotifyEnabled,
       "dL2FdbMacChangeHistorySize": dL2FdbMacChangeHistorySize,
       "dL2FdbDestHitEnabled": dL2FdbDestHitEnabled,
       "dL2FdbStaticUnicastTable": dL2FdbStaticUnicastTable,
       "dL2FdbStaticUnicastEntry": dL2FdbStaticUnicastEntry,
       "dL2FdbStaticUnicastVlanID": dL2FdbStaticUnicastVlanID,
       "dL2FdbStaticUnicastMacAddr": dL2FdbStaticUnicastMacAddr,
       "dL2FdbStaticUnicastType": dL2FdbStaticUnicastType,
       "dL2FdbStaticUnicastPortNum": dL2FdbStaticUnicastPortNum,
       "dL2FdbStaticUnicastRowStatus": dL2FdbStaticUnicastRowStatus,
       "dL2FdbIfCtrlTable": dL2FdbIfCtrlTable,
       "dL2FdbIfCtrlEntry": dL2FdbIfCtrlEntry,
       "dL2FdbIfCtrlNotifyEnable": dL2FdbIfCtrlNotifyEnable,
       "dL2FdbIfMacLearningEnabled": dL2FdbIfMacLearningEnabled,
       "dL2FdbMulticastFilterModeTable": dL2FdbMulticastFilterModeTable,
       "dL2FdbMulticastFilterModeEntry": dL2FdbMulticastFilterModeEntry,
       "dL2FdbMcastFilterModeIfIndex": dL2FdbMcastFilterModeIfIndex,
       "dL2FdbMcastFilterMode": dL2FdbMcastFilterMode,
       "dL2FdbMacChangeHistoryTable": dL2FdbMacChangeHistoryTable,
       "dL2FdbMacChangeHistoryEntry": dL2FdbMacChangeHistoryEntry,
       "dL2FdbMacChangeHistoryIndex": dL2FdbMacChangeHistoryIndex,
       "dL2FdbMacChangeHistoryOp": dL2FdbMacChangeHistoryOp,
       "dL2FdbMacChangeHistoryVlanID": dL2FdbMacChangeHistoryVlanID,
       "dL2FdbMacChangeHistoryMacAddr": dL2FdbMacChangeHistoryMacAddr,
       "dL2FdbMacChangeHistoryPortNum": dL2FdbMacChangeHistoryPortNum,
       "dL2FdbNotifyInfo": dL2FdbNotifyInfo,
       "dL2FdbMacChangeNotifyInfo": dL2FdbMacChangeNotifyInfo,
       "dL2FdbMIBConformance": dL2FdbMIBConformance,
       "dL2FdbCompliances": dL2FdbCompliances,
       "dL2FdbCompliance": dL2FdbCompliance,
       "dL2FdbGroups": dL2FdbGroups,
       "dL2FdbGlobalGroup": dL2FdbGlobalGroup,
       "dL2FdbMacAddrTableGroup": dL2FdbMacAddrTableGroup,
       "dL2FdbInterfaceGroup": dL2FdbInterfaceGroup,
       "dL2FdbMacChangeNotifyCfgGroup": dL2FdbMacChangeNotifyCfgGroup,
       "dL2FdbMcastFilterModeCfgGroup": dL2FdbMcastFilterModeCfgGroup,
       "dL2FdbMacChangeNotifyGroup": dL2FdbMacChangeNotifyGroup,
       "dL2FdbMacChgNotificationGroup": dL2FdbMacChgNotificationGroup}
)
