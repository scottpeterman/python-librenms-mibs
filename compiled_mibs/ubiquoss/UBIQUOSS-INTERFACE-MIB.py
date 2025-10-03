# SNMP MIB module (UBIQUOSS-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBIQUOSS-INTERFACE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:02 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(ubiMgmt,) = mibBuilder.importSymbols(
    "UBIQUOSS-SMI",
    "ubiMgmt")

(ubiSysIndex,) = mibBuilder.importSymbols(
    "UBIQUOSS-SYSINFO-MIB",
    "ubiSysIndex")


# MODULE-IDENTITY

ubiInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UbiInterfaceMIBObjects_ObjectIdentity = ObjectIdentity
ubiInterfaceMIBObjects = _UbiInterfaceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1)
)
_UbiPortTable_Object = MibTable
ubiPortTable = _UbiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 1)
)
if mibBuilder.loadTexts:
    ubiPortTable.setStatus("current")
_UbiPortEntry_Object = MibTableRow
ubiPortEntry = _UbiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 1, 1)
)
ubiPortEntry.setIndexNames(
    (0, "UBIQUOSS-SYSINFO-MIB", "ubiSysIndex"),
    (0, "UBIQUOSS-INTERFACE-MIB", "ubiPortIndex"),
)
if mibBuilder.loadTexts:
    ubiPortEntry.setStatus("current")
_UbiPortIndex_Type = Integer32
_UbiPortIndex_Object = MibTableColumn
ubiPortIndex = _UbiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 1, 1, 1),
    _UbiPortIndex_Type()
)
ubiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiPortIndex.setStatus("current")
_UbiPortType_Type = IANAifType
_UbiPortType_Object = MibTableColumn
ubiPortType = _UbiPortType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 1, 1, 2),
    _UbiPortType_Type()
)
ubiPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiPortType.setStatus("current")


class _UbiPortOperStatus_Type(Integer32):
    """Custom type ubiPortOperStatus based on Integer32"""
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
          ("up", 1),
          ("down", 2))
    )


_UbiPortOperStatus_Type.__name__ = "Integer32"
_UbiPortOperStatus_Object = MibTableColumn
ubiPortOperStatus = _UbiPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 1, 1, 3),
    _UbiPortOperStatus_Type()
)
ubiPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiPortOperStatus.setStatus("current")


class _UbiPortAdminStatus_Type(Integer32):
    """Custom type ubiPortAdminStatus based on Integer32"""
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
          ("up", 1),
          ("down", 2))
    )


_UbiPortAdminStatus_Type.__name__ = "Integer32"
_UbiPortAdminStatus_Object = MibTableColumn
ubiPortAdminStatus = _UbiPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 1, 1, 4),
    _UbiPortAdminStatus_Type()
)
ubiPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPortAdminStatus.setStatus("current")


class _UbiPortBlockStatus_Type(Integer32):
    """Custom type ubiPortBlockStatus based on Integer32"""
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
          ("unblock", 1),
          ("block", 2))
    )


_UbiPortBlockStatus_Type.__name__ = "Integer32"
_UbiPortBlockStatus_Object = MibTableColumn
ubiPortBlockStatus = _UbiPortBlockStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 1, 1, 5),
    _UbiPortBlockStatus_Type()
)
ubiPortBlockStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPortBlockStatus.setStatus("current")


class _UbiPortEquipStatus_Type(Integer32):
    """Custom type ubiPortEquipStatus based on Integer32"""
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
        *(("none", 0),
          ("equiped", 1),
          ("notequiped", 2),
          ("gbicequip", 3))
    )


_UbiPortEquipStatus_Type.__name__ = "Integer32"
_UbiPortEquipStatus_Object = MibTableColumn
ubiPortEquipStatus = _UbiPortEquipStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 1, 1, 6),
    _UbiPortEquipStatus_Type()
)
ubiPortEquipStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiPortEquipStatus.setStatus("current")
_UbiPortUpSpeedCurrent_Type = Gauge32
_UbiPortUpSpeedCurrent_Object = MibTableColumn
ubiPortUpSpeedCurrent = _UbiPortUpSpeedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 1, 1, 7),
    _UbiPortUpSpeedCurrent_Type()
)
ubiPortUpSpeedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiPortUpSpeedCurrent.setStatus("current")
_UbiPortDownSpeedCurrent_Type = Gauge32
_UbiPortDownSpeedCurrent_Object = MibTableColumn
ubiPortDownSpeedCurrent = _UbiPortDownSpeedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 1, 1, 8),
    _UbiPortDownSpeedCurrent_Type()
)
ubiPortDownSpeedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiPortDownSpeedCurrent.setStatus("mandatory")


class _UbiPortFlowControl_Type(Integer32):
    """Custom type ubiPortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notavailable", 0),
          ("enable", 1),
          ("disable", 2))
    )


_UbiPortFlowControl_Type.__name__ = "Integer32"
_UbiPortFlowControl_Object = MibTableColumn
ubiPortFlowControl = _UbiPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 1, 1, 9),
    _UbiPortFlowControl_Type()
)
ubiPortFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiPortFlowControl.setStatus("mandatory")


class _UbiPortControl_Type(Integer32):
    """Custom type ubiPortControl based on Integer32"""
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
          ("reset", 1),
          ("loopback-test", 2))
    )


_UbiPortControl_Type.__name__ = "Integer32"
_UbiPortControl_Object = MibTableColumn
ubiPortControl = _UbiPortControl_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 1, 1, 10),
    _UbiPortControl_Type()
)
ubiPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPortControl.setStatus("mandatory")
_UbiPortTestResultTable_Object = MibTable
ubiPortTestResultTable = _UbiPortTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 2)
)
if mibBuilder.loadTexts:
    ubiPortTestResultTable.setStatus("current")
_UbiPortTestResultEntry_Object = MibTableRow
ubiPortTestResultEntry = _UbiPortTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 2, 1)
)
ubiPortTestResultEntry.setIndexNames(
    (0, "UBIQUOSS-SYSINFO-MIB", "ubiSysIndex"),
    (0, "UBIQUOSS-INTERFACE-MIB", "ubiPortIndex"),
)
if mibBuilder.loadTexts:
    ubiPortTestResultEntry.setStatus("current")
_UbiPortTestResultTx_Type = Counter32
_UbiPortTestResultTx_Object = MibTableColumn
ubiPortTestResultTx = _UbiPortTestResultTx_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 2, 1, 1),
    _UbiPortTestResultTx_Type()
)
ubiPortTestResultTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiPortTestResultTx.setStatus("current")
_UbiPortTestResultRx_Type = Counter32
_UbiPortTestResultRx_Object = MibTableColumn
ubiPortTestResultRx = _UbiPortTestResultRx_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 2, 1, 2),
    _UbiPortTestResultRx_Type()
)
ubiPortTestResultRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiPortTestResultRx.setStatus("current")
_UbiPortTestResultMinRTT_Type = Gauge32
_UbiPortTestResultMinRTT_Object = MibTableColumn
ubiPortTestResultMinRTT = _UbiPortTestResultMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 2, 1, 3),
    _UbiPortTestResultMinRTT_Type()
)
ubiPortTestResultMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiPortTestResultMinRTT.setStatus("current")
if mibBuilder.loadTexts:
    ubiPortTestResultMinRTT.setUnits("micro seconds")
_UbiPortTestResultAvgRTT_Type = Gauge32
_UbiPortTestResultAvgRTT_Object = MibTableColumn
ubiPortTestResultAvgRTT = _UbiPortTestResultAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 2, 1, 4),
    _UbiPortTestResultAvgRTT_Type()
)
ubiPortTestResultAvgRTT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPortTestResultAvgRTT.setStatus("current")
if mibBuilder.loadTexts:
    ubiPortTestResultAvgRTT.setUnits("micro seconds")
_UbiPortTestResultMaxRTT_Type = Gauge32
_UbiPortTestResultMaxRTT_Object = MibTableColumn
ubiPortTestResultMaxRTT = _UbiPortTestResultMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 2, 1, 5),
    _UbiPortTestResultMaxRTT_Type()
)
ubiPortTestResultMaxRTT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPortTestResultMaxRTT.setStatus("current")
if mibBuilder.loadTexts:
    ubiPortTestResultMaxRTT.setUnits("micro seconds")
_UbiPortTestResultTime_Type = OctetString
_UbiPortTestResultTime_Object = MibTableColumn
ubiPortTestResultTime = _UbiPortTestResultTime_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 2, 1, 6),
    _UbiPortTestResultTime_Type()
)
ubiPortTestResultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiPortTestResultTime.setStatus("current")


class _UbiPortTestResultStatus_Type(Integer32):
    """Custom type ubiPortTestResultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notavailable", 0),
          ("sucess", 1),
          ("fail", 2))
    )


_UbiPortTestResultStatus_Type.__name__ = "Integer32"
_UbiPortTestResultStatus_Object = MibTableColumn
ubiPortTestResultStatus = _UbiPortTestResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 1, 2, 1, 7),
    _UbiPortTestResultStatus_Type()
)
ubiPortTestResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiPortTestResultStatus.setStatus("current")
_UbiInterfaceMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ubiInterfaceMIBNotificationPrefix = _UbiInterfaceMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 2)
)
_UbiInterfaceMIBNotifications_ObjectIdentity = ObjectIdentity
ubiInterfaceMIBNotifications = _UbiInterfaceMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 2, 0)
)
_UbiInterfaceMIBConformance_ObjectIdentity = ObjectIdentity
ubiInterfaceMIBConformance = _UbiInterfaceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 3)
)
_UbiInterfaceMIBCompliances_ObjectIdentity = ObjectIdentity
ubiInterfaceMIBCompliances = _UbiInterfaceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 3, 1)
)
_UbiInterfaceMIBGroups_ObjectIdentity = ObjectIdentity
ubiInterfaceMIBGroups = _UbiInterfaceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 3, 2)
)

# Managed Objects groups

ubiInterfaceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 3, 2, 1)
)
ubiInterfaceMIBGroup.setObjects(
      *(("UBIQUOSS-INTERFACE-MIB", "ubiPortType"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiPortOperStatus"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiPortAdminStatus"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiPortBlockStatus"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiPortGBICStatus"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiPortUpSpeedCurrent"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiPortDownSpeedCurrent"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiPortFlowControl"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiPortControl"))
)
if mibBuilder.loadTexts:
    ubiInterfaceMIBGroup.setStatus("current")


# Notification objects

ubiPortAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 2, 0, 1)
)
ubiPortAlarmNotification.setObjects(
      *(("UBIQUOSS-INTERFACE-MIB", "ubiAlarmIndex"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmId"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmType"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmSeverity"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmPhysicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmLogicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmCurStatus"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmAuxinfo"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmDateTime"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmStatus"))
)
if mibBuilder.loadTexts:
    ubiPortAlarmNotification.setStatus(
        "current"
    )

ubiPortOperStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 2, 0, 2)
)
ubiPortOperStatusChangeNotification.setObjects(
      *(("UBIQUOSS-INTERFACE-MIB", "ubiAlarmIndex"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmId"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmType"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmSeverity"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmPhysicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmLogicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmCurStatus"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmAuxinfo"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmDateTime"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmStatus"))
)
if mibBuilder.loadTexts:
    ubiPortOperStatusChangeNotification.setStatus(
        "current"
    )

ubiPortAdminStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 2, 0, 3)
)
ubiPortAdminStatusChangeNotification.setObjects(
      *(("UBIQUOSS-INTERFACE-MIB", "ubiAlarmIndex"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmId"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmType"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmSeverity"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmPhysicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmLogicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmCurStatus"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmAuxinfo"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmDateTime"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmStatus"))
)
if mibBuilder.loadTexts:
    ubiPortAdminStatusChangeNotification.setStatus(
        "current"
    )

ubiPortBlockStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 2, 0, 4)
)
ubiPortBlockStatusChangeNotification.setObjects(
      *(("UBIQUOSS-INTERFACE-MIB", "ubiAlarmIndex"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmId"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmType"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmSeverity"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmPhysicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmLogicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmCurStatus"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmAuxinfo"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmDateTime"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmStatus"))
)
if mibBuilder.loadTexts:
    ubiPortBlockStatusChangeNotification.setStatus(
        "current"
    )

ubiPortGbicStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 2, 0, 5)
)
ubiPortGbicStatusChangeNotification.setObjects(
      *(("UBIQUOSS-INTERFACE-MIB", "ubiAlarmIndex"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmId"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmType"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmSeverity"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmPhysicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmLogicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmCurStatus"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmAuxinfo"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmDateTime"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmStatus"))
)
if mibBuilder.loadTexts:
    ubiPortGbicStatusChangeNotification.setStatus(
        "current"
    )

ubiPortSelfLoopDetectNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 2, 0, 6)
)
ubiPortSelfLoopDetectNotification.setObjects(
      *(("UBIQUOSS-INTERFACE-MIB", "ubiAlarmIndex"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmId"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmType"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmSeverity"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmPhysicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmLogicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmCurStatus"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmAuxinfo"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmDateTime"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmStatus"))
)
if mibBuilder.loadTexts:
    ubiPortSelfLoopDetectNotification.setStatus(
        "current"
    )

ubiChampConnectorStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 2, 0, 7)
)
ubiChampConnectorStatusChangeNotification.setObjects(
      *(("UBIQUOSS-INTERFACE-MIB", "ubiAlarmIndex"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmId"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmType"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmSeverity"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmPhysicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmLogicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmCurStatus"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmAuxinfo"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmDateTime"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmStatus"))
)
if mibBuilder.loadTexts:
    ubiChampConnectorStatusChangeNotification.setStatus(
        "current"
    )

ubiPortLoopBackStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 2, 0, 8)
)
ubiPortLoopBackStatusChangeNotification.setObjects(
      *(("UBIQUOSS-INTERFACE-MIB", "ubiAlarmIndex"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmId"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmType"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmSeverity"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmPhysicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmLogicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmCurStatus"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmAuxinfo"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmDateTime"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmStatus"))
)
if mibBuilder.loadTexts:
    ubiPortLoopBackStatusChangeNotification.setStatus(
        "current"
    )

ubiPortLoopBackFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 2, 0, 9)
)
ubiPortLoopBackFailNotification.setObjects(
      *(("UBIQUOSS-INTERFACE-MIB", "ubiAlarmIndex"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmId"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmType"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmSeverity"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmPhysicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmLogicalLoc"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmCurStatus"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmAuxinfo"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmDateTime"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiAlarmStatus"))
)
if mibBuilder.loadTexts:
    ubiPortLoopBackFailNotification.setStatus(
        "current"
    )


# Notifications groups

ubiInterfaceMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 3, 2, 2)
)
ubiInterfaceMIBNotifGroup.setObjects(
      *(("UBIQUOSS-INTERFACE-MIB", "ubiPortAlarmNotification"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiPortOperStatusChangeNotification"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiPortAdminStatusChangeNotification"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiPortBlockStatusChangeNotification"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiPortGbicStatusChangeNotification"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiPortSelfLoopDetectNotification"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiChampConnectorStatusChangeNotification"))
)
if mibBuilder.loadTexts:
    ubiInterfaceMIBNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ubiInterfaceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7800, 2, 102, 3, 1, 1)
)
ubiInterfaceMIBCompliance.setObjects(
      *(("UBIQUOSS-INTERFACE-MIB", "ubiInterfaceMIBGroup"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiInterfaceMIBNotifGroup"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiInterfaceMIBGroup"),
        ("UBIQUOSS-INTERFACE-MIB", "ubiInterfaceMIBNotifGroup"))
)
if mibBuilder.loadTexts:
    ubiInterfaceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBIQUOSS-INTERFACE-MIB",
    **{"ubiInterfaceMIB": ubiInterfaceMIB,
       "ubiInterfaceMIBObjects": ubiInterfaceMIBObjects,
       "ubiPortTable": ubiPortTable,
       "ubiPortEntry": ubiPortEntry,
       "ubiPortIndex": ubiPortIndex,
       "ubiPortType": ubiPortType,
       "ubiPortOperStatus": ubiPortOperStatus,
       "ubiPortAdminStatus": ubiPortAdminStatus,
       "ubiPortBlockStatus": ubiPortBlockStatus,
       "ubiPortEquipStatus": ubiPortEquipStatus,
       "ubiPortUpSpeedCurrent": ubiPortUpSpeedCurrent,
       "ubiPortDownSpeedCurrent": ubiPortDownSpeedCurrent,
       "ubiPortFlowControl": ubiPortFlowControl,
       "ubiPortControl": ubiPortControl,
       "ubiPortTestResultTable": ubiPortTestResultTable,
       "ubiPortTestResultEntry": ubiPortTestResultEntry,
       "ubiPortTestResultTx": ubiPortTestResultTx,
       "ubiPortTestResultRx": ubiPortTestResultRx,
       "ubiPortTestResultMinRTT": ubiPortTestResultMinRTT,
       "ubiPortTestResultAvgRTT": ubiPortTestResultAvgRTT,
       "ubiPortTestResultMaxRTT": ubiPortTestResultMaxRTT,
       "ubiPortTestResultTime": ubiPortTestResultTime,
       "ubiPortTestResultStatus": ubiPortTestResultStatus,
       "ubiInterfaceMIBNotificationPrefix": ubiInterfaceMIBNotificationPrefix,
       "ubiInterfaceMIBNotifications": ubiInterfaceMIBNotifications,
       "ubiPortAlarmNotification": ubiPortAlarmNotification,
       "ubiPortOperStatusChangeNotification": ubiPortOperStatusChangeNotification,
       "ubiPortAdminStatusChangeNotification": ubiPortAdminStatusChangeNotification,
       "ubiPortBlockStatusChangeNotification": ubiPortBlockStatusChangeNotification,
       "ubiPortGbicStatusChangeNotification": ubiPortGbicStatusChangeNotification,
       "ubiPortSelfLoopDetectNotification": ubiPortSelfLoopDetectNotification,
       "ubiChampConnectorStatusChangeNotification": ubiChampConnectorStatusChangeNotification,
       "ubiPortLoopBackStatusChangeNotification": ubiPortLoopBackStatusChangeNotification,
       "ubiPortLoopBackFailNotification": ubiPortLoopBackFailNotification,
       "ubiInterfaceMIBConformance": ubiInterfaceMIBConformance,
       "ubiInterfaceMIBCompliances": ubiInterfaceMIBCompliances,
       "ubiInterfaceMIBCompliance": ubiInterfaceMIBCompliance,
       "ubiInterfaceMIBGroups": ubiInterfaceMIBGroups,
       "ubiInterfaceMIBGroup": ubiInterfaceMIBGroup,
       "ubiInterfaceMIBNotifGroup": ubiInterfaceMIBNotifGroup}
)
