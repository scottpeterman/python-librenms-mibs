# SNMP MIB module (UBIQUOSS-MAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBIQUOSS-MAC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:04 2025
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeTicks) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeTicks")

(ubiPortIndex,) = mibBuilder.importSymbols(
    "UBIQUOSS-INTERFACE-MIB",
    "ubiPortIndex")

(ubiSysIndex,) = mibBuilder.importSymbols(
    "UBIQUOSS-SYSINFO-MIB",
    "ubiSysIndex")

(ubiMgmt,) = mibBuilder.importSymbols(
    "UBQS-SMI",
    "ubiMgmt")


# MODULE-IDENTITY

ubiMacMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UbiMacMIBObjects_ObjectIdentity = ObjectIdentity
ubiMacMIBObjects = _UbiMacMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1)
)
_UbiSysMacTable_Object = MibTable
ubiSysMacTable = _UbiSysMacTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 1)
)
if mibBuilder.loadTexts:
    ubiSysMacTable.setStatus("current")
_UbiSysMacEntry_Object = MibTableRow
ubiSysMacEntry = _UbiSysMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 1, 1)
)
ubiSysMacEntry.setIndexNames(
    (0, "UBIQUOSS-SYSINFO-MIB", "ubiSysIndex"),
)
if mibBuilder.loadTexts:
    ubiSysMacEntry.setStatus("current")
_UbiSysMacMaxCnt_Type = Integer32
_UbiSysMacMaxCnt_Object = MibTableColumn
ubiSysMacMaxCnt = _UbiSysMacMaxCnt_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 1, 1, 1),
    _UbiSysMacMaxCnt_Type()
)
ubiSysMacMaxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysMacMaxCnt.setStatus("current")
_UbiSysMacCurrentCnt_Type = Integer32
_UbiSysMacCurrentCnt_Object = MibTableColumn
ubiSysMacCurrentCnt = _UbiSysMacCurrentCnt_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 1, 1, 2),
    _UbiSysMacCurrentCnt_Type()
)
ubiSysMacCurrentCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysMacCurrentCnt.setStatus("current")
_UbiSysMacRisingThreshold_Type = Integer32
_UbiSysMacRisingThreshold_Object = MibTableColumn
ubiSysMacRisingThreshold = _UbiSysMacRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 1, 1, 3),
    _UbiSysMacRisingThreshold_Type()
)
ubiSysMacRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSysMacRisingThreshold.setStatus("current")
_UbiSysMacFallingThreshold_Type = Integer32
_UbiSysMacFallingThreshold_Object = MibTableColumn
ubiSysMacFallingThreshold = _UbiSysMacFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 1, 1, 4),
    _UbiSysMacFallingThreshold_Type()
)
ubiSysMacFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSysMacFallingThreshold.setStatus("current")
_UbiSysMacAgingTime_Type = TimeTicks
_UbiSysMacAgingTime_Object = MibTableColumn
ubiSysMacAgingTime = _UbiSysMacAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 1, 1, 5),
    _UbiSysMacAgingTime_Type()
)
ubiSysMacAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSysMacAgingTime.setStatus("current")
_UbiPortMacLimitTable_Object = MibTable
ubiPortMacLimitTable = _UbiPortMacLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 2)
)
if mibBuilder.loadTexts:
    ubiPortMacLimitTable.setStatus("current")
_UbiPortMacLimitEntry_Object = MibTableRow
ubiPortMacLimitEntry = _UbiPortMacLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 2, 1)
)
ubiPortMacLimitEntry.setIndexNames(
    (0, "UBIQUOSS-SYSINFO-MIB", "ubiSysIndex"),
    (0, "UBIQUOSS-INTERFACE-MIB", "ubiPortIndex"),
)
if mibBuilder.loadTexts:
    ubiPortMacLimitEntry.setStatus("current")
_UbiPortMacMaxCnt_Type = Integer32
_UbiPortMacMaxCnt_Object = MibTableColumn
ubiPortMacMaxCnt = _UbiPortMacMaxCnt_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 2, 1, 1),
    _UbiPortMacMaxCnt_Type()
)
ubiPortMacMaxCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPortMacMaxCnt.setStatus("current")
_UbiPortMacLimitCnt_Type = Integer32
_UbiPortMacLimitCnt_Object = MibTableColumn
ubiPortMacLimitCnt = _UbiPortMacLimitCnt_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 2, 1, 2),
    _UbiPortMacLimitCnt_Type()
)
ubiPortMacLimitCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPortMacLimitCnt.setStatus("current")
_UbiPortMacCurrentCnt_Type = Integer32
_UbiPortMacCurrentCnt_Object = MibTableColumn
ubiPortMacCurrentCnt = _UbiPortMacCurrentCnt_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 2, 1, 3),
    _UbiPortMacCurrentCnt_Type()
)
ubiPortMacCurrentCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiPortMacCurrentCnt.setStatus("current")
_UbiPortMacAgingTime_Type = TimeTicks
_UbiPortMacAgingTime_Object = MibTableColumn
ubiPortMacAgingTime = _UbiPortMacAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 2, 1, 4),
    _UbiPortMacAgingTime_Type()
)
ubiPortMacAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPortMacAgingTime.setStatus("current")
_UbiPortMacAddrTable_Object = MibTable
ubiPortMacAddrTable = _UbiPortMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 3)
)
if mibBuilder.loadTexts:
    ubiPortMacAddrTable.setStatus("current")
_UbiPortMacAddrEntry_Object = MibTableRow
ubiPortMacAddrEntry = _UbiPortMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 3, 1)
)
ubiPortMacAddrEntry.setIndexNames(
    (0, "UBIQUOSS-SYSINFO-MIB", "ubiSysIndex"),
    (0, "UBIQUOSS-INTERFACE-MIB", "ubiPortIndex"),
    (0, "UBIQUOSS-MAC-MIB", "ubiPortMacAddrSequence"),
)
if mibBuilder.loadTexts:
    ubiPortMacAddrEntry.setStatus("current")
_UbiPortMacAddrSequence_Type = Integer32
_UbiPortMacAddrSequence_Object = MibTableColumn
ubiPortMacAddrSequence = _UbiPortMacAddrSequence_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 3, 1, 1),
    _UbiPortMacAddrSequence_Type()
)
ubiPortMacAddrSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiPortMacAddrSequence.setStatus("current")
_UbiPortMacAddress_Type = PhysAddress
_UbiPortMacAddress_Object = MibTableColumn
ubiPortMacAddress = _UbiPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 3, 1, 2),
    _UbiPortMacAddress_Type()
)
ubiPortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiPortMacAddress.setStatus("current")
_UbiPortRecentMacAddrTable_Object = MibTable
ubiPortRecentMacAddrTable = _UbiPortRecentMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 4)
)
if mibBuilder.loadTexts:
    ubiPortRecentMacAddrTable.setStatus("current")
_UbiPortRecentMacAddrEntry_Object = MibTableRow
ubiPortRecentMacAddrEntry = _UbiPortRecentMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 4, 1)
)
ubiPortRecentMacAddrEntry.setIndexNames(
    (0, "UBIQUOSS-SYSINFO-MIB", "ubiSysIndex"),
    (0, "UBIQUOSS-INTERFACE-MIB", "ubiPortIndex"),
    (0, "UBIQUOSS-MAC-MIB", "ubiPortRecentMacAddrSequence"),
)
if mibBuilder.loadTexts:
    ubiPortRecentMacAddrEntry.setStatus("current")
_UbiPortRecentMacAddrSequence_Type = Integer32
_UbiPortRecentMacAddrSequence_Object = MibTableColumn
ubiPortRecentMacAddrSequence = _UbiPortRecentMacAddrSequence_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 4, 1, 1),
    _UbiPortRecentMacAddrSequence_Type()
)
ubiPortRecentMacAddrSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiPortRecentMacAddrSequence.setStatus("current")
_UbiPortRecentMacAddress_Type = PhysAddress
_UbiPortRecentMacAddress_Object = MibTableColumn
ubiPortRecentMacAddress = _UbiPortRecentMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 4, 1, 2),
    _UbiPortRecentMacAddress_Type()
)
ubiPortRecentMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiPortRecentMacAddress.setStatus("current")
_UbiBaseFdbTable_Object = MibTable
ubiBaseFdbTable = _UbiBaseFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 5)
)
if mibBuilder.loadTexts:
    ubiBaseFdbTable.setStatus("current")
_UbiBaseFdbEntry_Object = MibTableRow
ubiBaseFdbEntry = _UbiBaseFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 5, 1)
)
ubiBaseFdbEntry.setIndexNames(
    (0, "UBIQUOSS-SYSINFO-MIB", "ubiSysIndex"),
    (0, "UBIQUOSS-MAC-MIB", "ubiBaseFdbVlanId"),
    (0, "UBIQUOSS-INTERFACE-MIB", "ubiPortIndex"),
    (0, "UBIQUOSS-MAC-MIB", "ubiBaseFdbMacAddress"),
)
if mibBuilder.loadTexts:
    ubiBaseFdbEntry.setStatus("current")


class _UbiBaseFdbVlanId_Type(Integer32):
    """Custom type ubiBaseFdbVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_UbiBaseFdbVlanId_Type.__name__ = "Integer32"
_UbiBaseFdbVlanId_Object = MibTableColumn
ubiBaseFdbVlanId = _UbiBaseFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 5, 1, 1),
    _UbiBaseFdbVlanId_Type()
)
ubiBaseFdbVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiBaseFdbVlanId.setStatus("current")
_UbiBaseFdbMacAddress_Type = MacAddress
_UbiBaseFdbMacAddress_Object = MibTableColumn
ubiBaseFdbMacAddress = _UbiBaseFdbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 5, 1, 2),
    _UbiBaseFdbMacAddress_Type()
)
ubiBaseFdbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiBaseFdbMacAddress.setStatus("current")


class _UbiBaseFdbStaticStatus_Type(Integer32):
    """Custom type ubiBaseFdbStaticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_UbiBaseFdbStaticStatus_Type.__name__ = "Integer32"
_UbiBaseFdbStaticStatus_Object = MibTableColumn
ubiBaseFdbStaticStatus = _UbiBaseFdbStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 5, 1, 3),
    _UbiBaseFdbStaticStatus_Type()
)
ubiBaseFdbStaticStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiBaseFdbStaticStatus.setStatus("current")


class _UbiBaseFdbSrcTrafficClass_Type(Integer32):
    """Custom type ubiBaseFdbSrcTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_UbiBaseFdbSrcTrafficClass_Type.__name__ = "Integer32"
_UbiBaseFdbSrcTrafficClass_Object = MibTableColumn
ubiBaseFdbSrcTrafficClass = _UbiBaseFdbSrcTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 5, 1, 4),
    _UbiBaseFdbSrcTrafficClass_Type()
)
ubiBaseFdbSrcTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiBaseFdbSrcTrafficClass.setStatus("current")


class _UbiBaseFdbDstTrafficClass_Type(Integer32):
    """Custom type ubiBaseFdbDstTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_UbiBaseFdbDstTrafficClass_Type.__name__ = "Integer32"
_UbiBaseFdbDstTrafficClass_Object = MibTableColumn
ubiBaseFdbDstTrafficClass = _UbiBaseFdbDstTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 5, 1, 5),
    _UbiBaseFdbDstTrafficClass_Type()
)
ubiBaseFdbDstTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiBaseFdbDstTrafficClass.setStatus("current")


class _UbiBaseFdbSrcCommand_Type(Integer32):
    """Custom type ubiBaseFdbSrcCommand based on Integer32"""
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
        *(("forward", 1),
          ("drop", 2),
          ("trap", 3),
          ("control", 4))
    )


_UbiBaseFdbSrcCommand_Type.__name__ = "Integer32"
_UbiBaseFdbSrcCommand_Object = MibTableColumn
ubiBaseFdbSrcCommand = _UbiBaseFdbSrcCommand_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 5, 1, 6),
    _UbiBaseFdbSrcCommand_Type()
)
ubiBaseFdbSrcCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiBaseFdbSrcCommand.setStatus("current")


class _UbiBaseFdbDstCommand_Type(Integer32):
    """Custom type ubiBaseFdbDstCommand based on Integer32"""
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
        *(("forward", 1),
          ("drop", 2),
          ("trap", 3),
          ("control", 4))
    )


_UbiBaseFdbDstCommand_Type.__name__ = "Integer32"
_UbiBaseFdbDstCommand_Object = MibTableColumn
ubiBaseFdbDstCommand = _UbiBaseFdbDstCommand_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 5, 1, 7),
    _UbiBaseFdbDstCommand_Type()
)
ubiBaseFdbDstCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiBaseFdbDstCommand.setStatus("current")


class _UbiBaseFdbTrafficType_Type(Integer32):
    """Custom type ubiBaseFdbTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )


_UbiBaseFdbTrafficType_Type.__name__ = "Integer32"
_UbiBaseFdbTrafficType_Object = MibTableColumn
ubiBaseFdbTrafficType = _UbiBaseFdbTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 5, 1, 8),
    _UbiBaseFdbTrafficType_Type()
)
ubiBaseFdbTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiBaseFdbTrafficType.setStatus("current")


class _UbiBaseFdbGateway_Type(Integer32):
    """Custom type ubiBaseFdbGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Notgateway", 1),
          ("gateway", 2))
    )


_UbiBaseFdbGateway_Type.__name__ = "Integer32"
_UbiBaseFdbGateway_Object = MibTableColumn
ubiBaseFdbGateway = _UbiBaseFdbGateway_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 5, 1, 9),
    _UbiBaseFdbGateway_Type()
)
ubiBaseFdbGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiBaseFdbGateway.setStatus("current")
_UbiBaseFdbRowStatus_Type = RowStatus
_UbiBaseFdbRowStatus_Object = MibTableColumn
ubiBaseFdbRowStatus = _UbiBaseFdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 1, 5, 1, 10),
    _UbiBaseFdbRowStatus_Type()
)
ubiBaseFdbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiBaseFdbRowStatus.setStatus("current")
_UbiMacMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ubiMacMIBNotificationPrefix = _UbiMacMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 2)
)
_UbiMacMIBNotifications_ObjectIdentity = ObjectIdentity
ubiMacMIBNotifications = _UbiMacMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 2, 0)
)
_UbiMacMIBConformance_ObjectIdentity = ObjectIdentity
ubiMacMIBConformance = _UbiMacMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 3)
)
_UbiMacMIBCompliances_ObjectIdentity = ObjectIdentity
ubiMacMIBCompliances = _UbiMacMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 3, 1)
)
_UbiMacMIBGroups_ObjectIdentity = ObjectIdentity
ubiMacMIBGroups = _UbiMacMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 3, 2)
)

# Managed Objects groups

ubiMacMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 3, 2, 1)
)
ubiMacMIBGroup.setObjects(
      *(("UBIQUOSS-MAC-MIB", "ubiSysMacMaxCnt"),
        ("UBIQUOSS-MAC-MIB", "ubiSysMacCurrentCnt"),
        ("UBIQUOSS-MAC-MIB", "ubiSysMacRisingThreshold"),
        ("UBIQUOSS-MAC-MIB", "ubiSysMacFallingThreshold"),
        ("UBIQUOSS-MAC-MIB", "ubiPortMacCurrentCnt"),
        ("UBIQUOSS-MAC-MIB", "ubiPortMacAddress"),
        ("UBIQUOSS-MAC-MIB", "ubiPortRecentMacAddress"))
)
if mibBuilder.loadTexts:
    ubiMacMIBGroup.setStatus("current")


# Notification objects

ubiSysMacThresholdAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 2, 0, 1)
)
ubiSysMacThresholdAlarmNotification.setObjects(
      *(("UBIQUOSS-MAC-MIB", "ubiAlarmIndex"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmId"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmType"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmSeverity"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmPhysicalLoc"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmLogicalLoc"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmCurStatus"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmAuxinfo"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmDateTime"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmStatus"))
)
if mibBuilder.loadTexts:
    ubiSysMacThresholdAlarmNotification.setStatus(
        "current"
    )

ubiSysMacRisingThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 2, 0, 2)
)
ubiSysMacRisingThresholdNotification.setObjects(
      *(("UBIQUOSS-MAC-MIB", "ubiAlarmIndex"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmId"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmType"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmSeverity"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmPhysicalLoc"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmLogicalLoc"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmCurStatus"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmAuxinfo"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmDateTime"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmStatus"))
)
if mibBuilder.loadTexts:
    ubiSysMacRisingThresholdNotification.setStatus(
        "current"
    )

ubiSysMacFallingThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 2, 0, 3)
)
ubiSysMacFallingThresholdNotification.setObjects(
      *(("UBIQUOSS-MAC-MIB", "ubiAlarmIndex"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmId"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmType"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmSeverity"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmPhysicalLoc"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmLogicalLoc"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmCurStatus"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmAuxinfo"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmDateTime"),
        ("UBIQUOSS-MAC-MIB", "ubiAlarmStatus"))
)
if mibBuilder.loadTexts:
    ubiSysMacFallingThresholdNotification.setStatus(
        "current"
    )


# Notifications groups

ubiMacMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 3, 2, 2)
)
ubiMacMIBNotifGroup.setObjects(
      *(("UBIQUOSS-MAC-MIB", "ubiSysMacThresholdAlarmNotification"),
        ("UBIQUOSS-MAC-MIB", "ubiSysMacRisingThresholdNotification"),
        ("UBIQUOSS-MAC-MIB", "ubiSysMacFallingThresholdNotification"))
)
if mibBuilder.loadTexts:
    ubiMacMIBNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ubiMacMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7800, 2, 201, 3, 1, 1)
)
ubiMacMIBCompliance.setObjects(
      *(("UBIQUOSS-MAC-MIB", "ubiMacMIBGroup"),
        ("UBIQUOSS-MAC-MIB", "ubiMacMIBNotifGroup"),
        ("UBIQUOSS-MAC-MIB", "ubiMacMIBGroup"),
        ("UBIQUOSS-MAC-MIB", "ubiMacMIBNotifGroup"))
)
if mibBuilder.loadTexts:
    ubiMacMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBIQUOSS-MAC-MIB",
    **{"ubiMacMIB": ubiMacMIB,
       "ubiMacMIBObjects": ubiMacMIBObjects,
       "ubiSysMacTable": ubiSysMacTable,
       "ubiSysMacEntry": ubiSysMacEntry,
       "ubiSysMacMaxCnt": ubiSysMacMaxCnt,
       "ubiSysMacCurrentCnt": ubiSysMacCurrentCnt,
       "ubiSysMacRisingThreshold": ubiSysMacRisingThreshold,
       "ubiSysMacFallingThreshold": ubiSysMacFallingThreshold,
       "ubiSysMacAgingTime": ubiSysMacAgingTime,
       "ubiPortMacLimitTable": ubiPortMacLimitTable,
       "ubiPortMacLimitEntry": ubiPortMacLimitEntry,
       "ubiPortMacMaxCnt": ubiPortMacMaxCnt,
       "ubiPortMacLimitCnt": ubiPortMacLimitCnt,
       "ubiPortMacCurrentCnt": ubiPortMacCurrentCnt,
       "ubiPortMacAgingTime": ubiPortMacAgingTime,
       "ubiPortMacAddrTable": ubiPortMacAddrTable,
       "ubiPortMacAddrEntry": ubiPortMacAddrEntry,
       "ubiPortMacAddrSequence": ubiPortMacAddrSequence,
       "ubiPortMacAddress": ubiPortMacAddress,
       "ubiPortRecentMacAddrTable": ubiPortRecentMacAddrTable,
       "ubiPortRecentMacAddrEntry": ubiPortRecentMacAddrEntry,
       "ubiPortRecentMacAddrSequence": ubiPortRecentMacAddrSequence,
       "ubiPortRecentMacAddress": ubiPortRecentMacAddress,
       "ubiBaseFdbTable": ubiBaseFdbTable,
       "ubiBaseFdbEntry": ubiBaseFdbEntry,
       "ubiBaseFdbVlanId": ubiBaseFdbVlanId,
       "ubiBaseFdbMacAddress": ubiBaseFdbMacAddress,
       "ubiBaseFdbStaticStatus": ubiBaseFdbStaticStatus,
       "ubiBaseFdbSrcTrafficClass": ubiBaseFdbSrcTrafficClass,
       "ubiBaseFdbDstTrafficClass": ubiBaseFdbDstTrafficClass,
       "ubiBaseFdbSrcCommand": ubiBaseFdbSrcCommand,
       "ubiBaseFdbDstCommand": ubiBaseFdbDstCommand,
       "ubiBaseFdbTrafficType": ubiBaseFdbTrafficType,
       "ubiBaseFdbGateway": ubiBaseFdbGateway,
       "ubiBaseFdbRowStatus": ubiBaseFdbRowStatus,
       "ubiMacMIBNotificationPrefix": ubiMacMIBNotificationPrefix,
       "ubiMacMIBNotifications": ubiMacMIBNotifications,
       "ubiSysMacThresholdAlarmNotification": ubiSysMacThresholdAlarmNotification,
       "ubiSysMacRisingThresholdNotification": ubiSysMacRisingThresholdNotification,
       "ubiSysMacFallingThresholdNotification": ubiSysMacFallingThresholdNotification,
       "ubiMacMIBConformance": ubiMacMIBConformance,
       "ubiMacMIBCompliances": ubiMacMIBCompliances,
       "ubiMacMIBCompliance": ubiMacMIBCompliance,
       "ubiMacMIBGroups": ubiMacMIBGroups,
       "ubiMacMIBGroup": ubiMacMIBGroup,
       "ubiMacMIBNotifGroup": ubiMacMIBNotifGroup}
)
