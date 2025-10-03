# SNMP MIB module (PRVT-DRY-CONTACTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-DRY-CONTACTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:46 2025
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

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

prvtDryContactsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 112)
)
if mibBuilder.loadTexts:
    prvtDryContactsMIB.setRevisions(
        ("2007-11-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DryContactsNotifications_ObjectIdentity = ObjectIdentity
dryContactsNotifications = _DryContactsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 112, 0)
)
_DryContactsObjects_ObjectIdentity = ObjectIdentity
dryContactsObjects = _DryContactsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 112, 1)
)
_CfgTable_Object = MibTable
cfgTable = _CfgTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 112, 1, 1)
)
if mibBuilder.loadTexts:
    cfgTable.setStatus("current")
_CfgEntry_Object = MibTableRow
cfgEntry = _CfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 112, 1, 1, 1)
)
cfgEntry.setIndexNames(
    (0, "PRVT-DRY-CONTACTS-MIB", "prvtAlarmID"),
)
if mibBuilder.loadTexts:
    cfgEntry.setStatus("current")


class _PrvtAlarmID_Type(Integer32):
    """Custom type prvtAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_PrvtAlarmID_Type.__name__ = "Integer32"
_PrvtAlarmID_Object = MibTableColumn
prvtAlarmID = _PrvtAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 112, 1, 1, 1, 1),
    _PrvtAlarmID_Type()
)
prvtAlarmID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    prvtAlarmID.setStatus("current")


class _PrvtSensorType_Type(Integer32):
    """Custom type prvtSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_PrvtSensorType_Type.__name__ = "Integer32"
_PrvtSensorType_Object = MibTableColumn
prvtSensorType = _PrvtSensorType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 112, 1, 1, 1, 2),
    _PrvtSensorType_Type()
)
prvtSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSensorType.setStatus("current")
_PrvtName_Type = OctetString
_PrvtName_Object = MibTableColumn
prvtName = _PrvtName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 112, 1, 1, 1, 3),
    _PrvtName_Type()
)
prvtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtName.setStatus("current")
_PrvtDescription_Type = OctetString
_PrvtDescription_Object = MibTableColumn
prvtDescription = _PrvtDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 112, 1, 1, 1, 4),
    _PrvtDescription_Type()
)
prvtDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtDescription.setStatus("current")


class _PrvtEnableStatus_Type(Integer32):
    """Custom type prvtEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_PrvtEnableStatus_Type.__name__ = "Integer32"
_PrvtEnableStatus_Object = MibTableColumn
prvtEnableStatus = _PrvtEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 112, 1, 1, 1, 5),
    _PrvtEnableStatus_Type()
)
prvtEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtEnableStatus.setStatus("current")


class _PrvtAlarmStatus_Type(Integer32):
    """Custom type prvtAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-alarm", 1),
          ("alarm", 2))
    )


_PrvtAlarmStatus_Type.__name__ = "Integer32"
_PrvtAlarmStatus_Object = MibTableColumn
prvtAlarmStatus = _PrvtAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 112, 1, 1, 1, 6),
    _PrvtAlarmStatus_Type()
)
prvtAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtAlarmStatus.setStatus("current")


class _PrvtAlarmSeverity_Type(Integer32):
    """Custom type prvtAlarmSeverity based on Integer32"""
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
        *(("info", 1),
          ("minor", 2),
          ("major", 3),
          ("critical", 4))
    )


_PrvtAlarmSeverity_Type.__name__ = "Integer32"
_PrvtAlarmSeverity_Object = MibTableColumn
prvtAlarmSeverity = _PrvtAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 112, 1, 1, 1, 7),
    _PrvtAlarmSeverity_Type()
)
prvtAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtAlarmSeverity.setStatus("current")


class _PrvtPolarity_Type(Integer32):
    """Custom type prvtPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normally-opened", 1),
          ("normally-closed", 2))
    )


_PrvtPolarity_Type.__name__ = "Integer32"
_PrvtPolarity_Object = MibTableColumn
prvtPolarity = _PrvtPolarity_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 112, 1, 1, 1, 8),
    _PrvtPolarity_Type()
)
prvtPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtPolarity.setStatus("current")
_PrvtLastChange_Type = TimeTicks
_PrvtLastChange_Object = MibTableColumn
prvtLastChange = _PrvtLastChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 112, 1, 1, 1, 9),
    _PrvtLastChange_Type()
)
prvtLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLastChange.setStatus("current")

# Managed Objects groups


# Notification objects

stateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 112, 0, 1)
)
stateChanged.setObjects(
      *(("PRVT-DRY-CONTACTS-MIB", "prvtAlarmID"),
        ("PRVT-DRY-CONTACTS-MIB", "prvtSensorType"),
        ("PRVT-DRY-CONTACTS-MIB", "prvtName"),
        ("PRVT-DRY-CONTACTS-MIB", "prvtDescription"),
        ("PRVT-DRY-CONTACTS-MIB", "prvtAlarmStatus"),
        ("PRVT-DRY-CONTACTS-MIB", "prvtAlarmSeverity"))
)
if mibBuilder.loadTexts:
    stateChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-DRY-CONTACTS-MIB",
    **{"prvtDryContactsMIB": prvtDryContactsMIB,
       "dryContactsNotifications": dryContactsNotifications,
       "stateChanged": stateChanged,
       "dryContactsObjects": dryContactsObjects,
       "cfgTable": cfgTable,
       "cfgEntry": cfgEntry,
       "prvtAlarmID": prvtAlarmID,
       "prvtSensorType": prvtSensorType,
       "prvtName": prvtName,
       "prvtDescription": prvtDescription,
       "prvtEnableStatus": prvtEnableStatus,
       "prvtAlarmStatus": prvtAlarmStatus,
       "prvtAlarmSeverity": prvtAlarmSeverity,
       "prvtPolarity": prvtPolarity,
       "prvtLastChange": prvtLastChange}
)
