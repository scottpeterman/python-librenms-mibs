# SNMP MIB module (DLINKSW-POWER-SAVING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-POWER-SAVING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:45 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwPowerSavingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 16)
)
if mibBuilder.loadTexts:
    dlinkSwPowerSavingMIB.setRevisions(
        ("2013-01-31 00:00",
         "2013-07-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DPowerSavingMIBNotifications_ObjectIdentity = ObjectIdentity
dPowerSavingMIBNotifications = _DPowerSavingMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 0)
)
_DPowerSavingMIBObjects_ObjectIdentity = ObjectIdentity
dPowerSavingMIBObjects = _DPowerSavingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1)
)
_DPowerSavingGeneral_ObjectIdentity = ObjectIdentity
dPowerSavingGeneral = _DPowerSavingGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 1)
)


class _DpsLinkDetectionEnabled_Type(TruthValue):
    """Custom type dpsLinkDetectionEnabled based on TruthValue"""
    defaultValue = 2


_DpsLinkDetectionEnabled_Type.__name__ = "TruthValue"
_DpsLinkDetectionEnabled_Object = MibScalar
dpsLinkDetectionEnabled = _DpsLinkDetectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 1, 1),
    _DpsLinkDetectionEnabled_Type()
)
dpsLinkDetectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsLinkDetectionEnabled.setStatus("current")


class _DpsLengthDetectionEnabled_Type(TruthValue):
    """Custom type dpsLengthDetectionEnabled based on TruthValue"""
    defaultValue = 2


_DpsLengthDetectionEnabled_Type.__name__ = "TruthValue"
_DpsLengthDetectionEnabled_Object = MibScalar
dpsLengthDetectionEnabled = _DpsLengthDetectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 1, 2),
    _DpsLengthDetectionEnabled_Type()
)
dpsLengthDetectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsLengthDetectionEnabled.setStatus("current")


class _DpsHibernationEnabled_Type(TruthValue):
    """Custom type dpsHibernationEnabled based on TruthValue"""
    defaultValue = 2


_DpsHibernationEnabled_Type.__name__ = "TruthValue"
_DpsHibernationEnabled_Object = MibScalar
dpsHibernationEnabled = _DpsHibernationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 1, 3),
    _DpsHibernationEnabled_Type()
)
dpsHibernationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsHibernationEnabled.setStatus("current")


class _DpsDimLedEnabled_Type(TruthValue):
    """Custom type dpsDimLedEnabled based on TruthValue"""
    defaultValue = 2


_DpsDimLedEnabled_Type.__name__ = "TruthValue"
_DpsDimLedEnabled_Object = MibScalar
dpsDimLedEnabled = _DpsDimLedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 1, 4),
    _DpsDimLedEnabled_Type()
)
dpsDimLedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsDimLedEnabled.setStatus("current")


class _DpsLedAdminEnabled_Type(TruthValue):
    """Custom type dpsLedAdminEnabled based on TruthValue"""
    defaultValue = 1


_DpsLedAdminEnabled_Type.__name__ = "TruthValue"
_DpsLedAdminEnabled_Object = MibScalar
dpsLedAdminEnabled = _DpsLedAdminEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 1, 5),
    _DpsLedAdminEnabled_Type()
)
dpsLedAdminEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsLedAdminEnabled.setStatus("current")


class _DpsPortShutdownEnabled_Type(TruthValue):
    """Custom type dpsPortShutdownEnabled based on TruthValue"""
    defaultValue = 2


_DpsPortShutdownEnabled_Type.__name__ = "TruthValue"
_DpsPortShutdownEnabled_Object = MibScalar
dpsPortShutdownEnabled = _DpsPortShutdownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 1, 6),
    _DpsPortShutdownEnabled_Type()
)
dpsPortShutdownEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsPortShutdownEnabled.setStatus("current")
_DPowerSavingIfObjects_ObjectIdentity = ObjectIdentity
dPowerSavingIfObjects = _DPowerSavingIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 2)
)
_DpsIfEeeTable_Object = MibTable
dpsIfEeeTable = _DpsIfEeeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dpsIfEeeTable.setStatus("current")
_DpsIfEeeEntry_Object = MibTableRow
dpsIfEeeEntry = _DpsIfEeeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 2, 1, 1)
)
dpsIfEeeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dpsIfEeeEntry.setStatus("current")


class _DpsIfEeeStatus_Type(Integer32):
    """Custom type dpsIfEeeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notAvailable", 3))
    )


_DpsIfEeeStatus_Type.__name__ = "Integer32"
_DpsIfEeeStatus_Object = MibTableColumn
dpsIfEeeStatus = _DpsIfEeeStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 2, 1, 1, 2),
    _DpsIfEeeStatus_Type()
)
dpsIfEeeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsIfEeeStatus.setStatus("current")
_DpsScheduleCtrl_ObjectIdentity = ObjectIdentity
dpsScheduleCtrl = _DpsScheduleCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 3)
)


class _DpsHibernationTimeRange_Type(DisplayString):
    """Custom type dpsHibernationTimeRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DpsHibernationTimeRange_Type.__name__ = "DisplayString"
_DpsHibernationTimeRange_Object = MibScalar
dpsHibernationTimeRange = _DpsHibernationTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 3, 1),
    _DpsHibernationTimeRange_Type()
)
dpsHibernationTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsHibernationTimeRange.setStatus("current")


class _DpsDimLedTimeRange_Type(DisplayString):
    """Custom type dpsDimLedTimeRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DpsDimLedTimeRange_Type.__name__ = "DisplayString"
_DpsDimLedTimeRange_Object = MibScalar
dpsDimLedTimeRange = _DpsDimLedTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 3, 2),
    _DpsDimLedTimeRange_Type()
)
dpsDimLedTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsDimLedTimeRange.setStatus("current")
_DpsPortShutdownScheduleTable_Object = MibTable
dpsPortShutdownScheduleTable = _DpsPortShutdownScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dpsPortShutdownScheduleTable.setStatus("current")
_DpsPortShutdownScheduleEntry_Object = MibTableRow
dpsPortShutdownScheduleEntry = _DpsPortShutdownScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 3, 3, 1)
)
dpsPortShutdownScheduleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dpsPortShutdownScheduleEntry.setStatus("current")


class _DpsPortShutdownTimeRange_Type(DisplayString):
    """Custom type dpsPortShutdownTimeRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DpsPortShutdownTimeRange_Type.__name__ = "DisplayString"
_DpsPortShutdownTimeRange_Object = MibTableColumn
dpsPortShutdownTimeRange = _DpsPortShutdownTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 1, 3, 3, 1, 1),
    _DpsPortShutdownTimeRange_Type()
)
dpsPortShutdownTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsPortShutdownTimeRange.setStatus("current")
_DPowerSavingMIBConformance_ObjectIdentity = ObjectIdentity
dPowerSavingMIBConformance = _DPowerSavingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 2)
)
_DpsMIBCompliances_ObjectIdentity = ObjectIdentity
dpsMIBCompliances = _DpsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 2, 1)
)
_DpsMIBGroups_ObjectIdentity = ObjectIdentity
dpsMIBGroups = _DpsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 2, 2)
)

# Managed Objects groups

dpsLinkCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 2, 2, 1)
)
dpsLinkCfgGroup.setObjects(
    ("DLINKSW-POWER-SAVING-MIB", "dpsLinkDetectionEnabled")
)
if mibBuilder.loadTexts:
    dpsLinkCfgGroup.setStatus("current")

dpsLenCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 2, 2, 2)
)
dpsLenCfgGroup.setObjects(
    ("DLINKSW-POWER-SAVING-MIB", "dpsLengthDetectionEnabled")
)
if mibBuilder.loadTexts:
    dpsLenCfgGroup.setStatus("current")

dpsHiberCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 2, 2, 3)
)
dpsHiberCfgGroup.setObjects(
      *(("DLINKSW-POWER-SAVING-MIB", "dpsHibernationEnabled"),
        ("DLINKSW-POWER-SAVING-MIB", "dpsHibernationTimeRange"))
)
if mibBuilder.loadTexts:
    dpsHiberCfgGroup.setStatus("current")

dpsDimLedCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 2, 2, 4)
)
dpsDimLedCfgGroup.setObjects(
      *(("DLINKSW-POWER-SAVING-MIB", "dpsDimLedEnabled"),
        ("DLINKSW-POWER-SAVING-MIB", "dpsLedAdminEnabled"),
        ("DLINKSW-POWER-SAVING-MIB", "dpsDimLedTimeRange"))
)
if mibBuilder.loadTexts:
    dpsDimLedCfgGroup.setStatus("current")

dpsShutdownCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 2, 2, 5)
)
dpsShutdownCfgGroup.setObjects(
      *(("DLINKSW-POWER-SAVING-MIB", "dpsPortShutdownEnabled"),
        ("DLINKSW-POWER-SAVING-MIB", "dpsPortShutdownTimeRange"))
)
if mibBuilder.loadTexts:
    dpsShutdownCfgGroup.setStatus("current")

dpsIfEeeCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 2, 2, 6)
)
dpsIfEeeCfgGroup.setObjects(
    ("DLINKSW-POWER-SAVING-MIB", "dpsIfEeeStatus")
)
if mibBuilder.loadTexts:
    dpsIfEeeCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 16, 2, 1, 1)
)
dpsMIBCompliance.setObjects(
      *(("DLINKSW-POWER-SAVING-MIB", "dpsLinkCfgGroup"),
        ("DLINKSW-POWER-SAVING-MIB", "dpsLenCfgGroup"),
        ("DLINKSW-POWER-SAVING-MIB", "dpsHiberCfgGroup"),
        ("DLINKSW-POWER-SAVING-MIB", "dpsDimLedCfgGroup"),
        ("DLINKSW-POWER-SAVING-MIB", "dpsShutdownCfgGroup"),
        ("DLINKSW-POWER-SAVING-MIB", "dpsIfEeeCfgGroup"))
)
if mibBuilder.loadTexts:
    dpsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-POWER-SAVING-MIB",
    **{"dlinkSwPowerSavingMIB": dlinkSwPowerSavingMIB,
       "dPowerSavingMIBNotifications": dPowerSavingMIBNotifications,
       "dPowerSavingMIBObjects": dPowerSavingMIBObjects,
       "dPowerSavingGeneral": dPowerSavingGeneral,
       "dpsLinkDetectionEnabled": dpsLinkDetectionEnabled,
       "dpsLengthDetectionEnabled": dpsLengthDetectionEnabled,
       "dpsHibernationEnabled": dpsHibernationEnabled,
       "dpsDimLedEnabled": dpsDimLedEnabled,
       "dpsLedAdminEnabled": dpsLedAdminEnabled,
       "dpsPortShutdownEnabled": dpsPortShutdownEnabled,
       "dPowerSavingIfObjects": dPowerSavingIfObjects,
       "dpsIfEeeTable": dpsIfEeeTable,
       "dpsIfEeeEntry": dpsIfEeeEntry,
       "dpsIfEeeStatus": dpsIfEeeStatus,
       "dpsScheduleCtrl": dpsScheduleCtrl,
       "dpsHibernationTimeRange": dpsHibernationTimeRange,
       "dpsDimLedTimeRange": dpsDimLedTimeRange,
       "dpsPortShutdownScheduleTable": dpsPortShutdownScheduleTable,
       "dpsPortShutdownScheduleEntry": dpsPortShutdownScheduleEntry,
       "dpsPortShutdownTimeRange": dpsPortShutdownTimeRange,
       "dPowerSavingMIBConformance": dPowerSavingMIBConformance,
       "dpsMIBCompliances": dpsMIBCompliances,
       "dpsMIBCompliance": dpsMIBCompliance,
       "dpsMIBGroups": dpsMIBGroups,
       "dpsLinkCfgGroup": dpsLinkCfgGroup,
       "dpsLenCfgGroup": dpsLenCfgGroup,
       "dpsHiberCfgGroup": dpsHiberCfgGroup,
       "dpsDimLedCfgGroup": dpsDimLedCfgGroup,
       "dpsShutdownCfgGroup": dpsShutdownCfgGroup,
       "dpsIfEeeCfgGroup": dpsIfEeeCfgGroup}
)
