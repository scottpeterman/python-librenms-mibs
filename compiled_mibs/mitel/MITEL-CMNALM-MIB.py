# SNMP MIB module (MITEL-CMNALM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mitel\MITEL-CMNALM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:42 2025
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

(mitelConfCompliances,
 mitelConfGroups,
 mitelIdentification,
 mitelPropCommon) = mibBuilder.importSymbols(
    "MITEL-MIB",
    "mitelConfCompliances",
    "mitelConfGroups",
    "mitelIdentification",
    "mitelPropCommon")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mitelCmnAlarms = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1)
)
if mibBuilder.loadTexts:
    mitelCmnAlarms.setRevisions(
        ("2014-02-11 12:00",
         "2005-02-21 21:34",
         "2004-02-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ItuPerceivedSeverity(TextualConvention, Integer32):
    status = "current"
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
        *(("cleared", 1),
          ("indeterminate", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )



class MitelCmnAlarmThresholdType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("percentage", 1),
          ("absoluteValue", 2),
          ("indeterminate", 3))
    )



# MIB Managed Objects in the order of their OIDs

_MitelCmnAlmObjects_ObjectIdentity = ObjectIdentity
mitelCmnAlmObjects = _MitelCmnAlmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1)
)
if mibBuilder.loadTexts:
    mitelCmnAlmObjects.setStatus("current")
_MitelAlmSystem_ObjectIdentity = ObjectIdentity
mitelAlmSystem = _MitelAlmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mitelAlmSystem.setStatus("current")
_MitelAlmSysSeverity_Type = ItuPerceivedSeverity
_MitelAlmSysSeverity_Object = MibScalar
mitelAlmSysSeverity = _MitelAlmSysSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 1, 1),
    _MitelAlmSysSeverity_Type()
)
mitelAlmSysSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAlmSysSeverity.setStatus("current")
_MitelAlmSysSeverityDetectTime_Type = DateAndTime
_MitelAlmSysSeverityDetectTime_Object = MibScalar
mitelAlmSysSeverityDetectTime = _MitelAlmSysSeverityDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 1, 2),
    _MitelAlmSysSeverityDetectTime_Type()
)
mitelAlmSysSeverityDetectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAlmSysSeverityDetectTime.setStatus("current")
_MitelAlmSysSeverityDescr_Type = DisplayString
_MitelAlmSysSeverityDescr_Object = MibScalar
mitelAlmSysSeverityDescr = _MitelAlmSysSeverityDescr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 1, 3),
    _MitelAlmSysSeverityDescr_Type()
)
mitelAlmSysSeverityDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAlmSysSeverityDescr.setStatus("current")
_MitelAlmActiveTable_Object = MibTable
mitelAlmActiveTable = _MitelAlmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mitelAlmActiveTable.setStatus("current")
_MitelAlmActiveTableEntry_Object = MibTableRow
mitelAlmActiveTableEntry = _MitelAlmActiveTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1)
)
mitelAlmActiveTableEntry.setIndexNames(
    (0, "MITEL-CMNALM-MIB", "mitelAlmActiveTblIndex"),
)
if mibBuilder.loadTexts:
    mitelAlmActiveTableEntry.setStatus("current")
_MitelAlmActiveTblIndex_Type = ObjectIdentifier
_MitelAlmActiveTblIndex_Object = MibTableColumn
mitelAlmActiveTblIndex = _MitelAlmActiveTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 1),
    _MitelAlmActiveTblIndex_Type()
)
mitelAlmActiveTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAlmActiveTblIndex.setStatus("current")
_MitelAlmActiveTblClass_Type = DisplayString
_MitelAlmActiveTblClass_Object = MibTableColumn
mitelAlmActiveTblClass = _MitelAlmActiveTblClass_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 2),
    _MitelAlmActiveTblClass_Type()
)
mitelAlmActiveTblClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAlmActiveTblClass.setStatus("current")
_MitelAlmActiveTblType_Type = DisplayString
_MitelAlmActiveTblType_Object = MibTableColumn
mitelAlmActiveTblType = _MitelAlmActiveTblType_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 3),
    _MitelAlmActiveTblType_Type()
)
mitelAlmActiveTblType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAlmActiveTblType.setStatus("current")
_MitelAlmActiveTblTypeName_Type = DisplayString
_MitelAlmActiveTblTypeName_Object = MibTableColumn
mitelAlmActiveTblTypeName = _MitelAlmActiveTblTypeName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 4),
    _MitelAlmActiveTblTypeName_Type()
)
mitelAlmActiveTblTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAlmActiveTblTypeName.setStatus("current")
_MitelAlmActiveTblSeverity_Type = ItuPerceivedSeverity
_MitelAlmActiveTblSeverity_Object = MibTableColumn
mitelAlmActiveTblSeverity = _MitelAlmActiveTblSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 5),
    _MitelAlmActiveTblSeverity_Type()
)
mitelAlmActiveTblSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAlmActiveTblSeverity.setStatus("current")
_MitelAlmActiveTblSeverityDetectTime_Type = DateAndTime
_MitelAlmActiveTblSeverityDetectTime_Object = MibTableColumn
mitelAlmActiveTblSeverityDetectTime = _MitelAlmActiveTblSeverityDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 6),
    _MitelAlmActiveTblSeverityDetectTime_Type()
)
mitelAlmActiveTblSeverityDetectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAlmActiveTblSeverityDetectTime.setStatus("current")
_MitelAlmActiveTblThresholdType_Type = MitelCmnAlarmThresholdType
_MitelAlmActiveTblThresholdType_Object = MibTableColumn
mitelAlmActiveTblThresholdType = _MitelAlmActiveTblThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 7),
    _MitelAlmActiveTblThresholdType_Type()
)
mitelAlmActiveTblThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAlmActiveTblThresholdType.setStatus("current")
_MitelAlmActiveTblThresholdValue_Type = Integer32
_MitelAlmActiveTblThresholdValue_Object = MibTableColumn
mitelAlmActiveTblThresholdValue = _MitelAlmActiveTblThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 8),
    _MitelAlmActiveTblThresholdValue_Type()
)
mitelAlmActiveTblThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAlmActiveTblThresholdValue.setStatus("current")
_MitelAlmActiveTblDescr_Type = DisplayString
_MitelAlmActiveTblDescr_Object = MibTableColumn
mitelAlmActiveTblDescr = _MitelAlmActiveTblDescr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 9),
    _MitelAlmActiveTblDescr_Type()
)
mitelAlmActiveTblDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAlmActiveTblDescr.setStatus("current")
_MitelCmnAlmNotifications_ObjectIdentity = ObjectIdentity
mitelCmnAlmNotifications = _MitelCmnAlmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 2)
)
if mibBuilder.loadTexts:
    mitelCmnAlmNotifications.setStatus("current")
_MitelCmnAlmConformance_ObjectIdentity = ObjectIdentity
mitelCmnAlmConformance = _MitelCmnAlmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 3)
)
if mibBuilder.loadTexts:
    mitelCmnAlmConformance.setStatus("current")

# Managed Objects groups


# Notification objects

mitelNotifActiveAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 2, 1)
)
mitelNotifActiveAlarm.setObjects(
      *(("MITEL-CMNALM-MIB", "mitelAlmSysSeverity"),
        ("MITEL-CMNALM-MIB", "mitelAlmSysSeverityDetectTime"),
        ("MITEL-CMNALM-MIB", "mitelAlmActiveTblIndex"),
        ("MITEL-CMNALM-MIB", "mitelAlmActiveTblClass"),
        ("MITEL-CMNALM-MIB", "mitelAlmActiveTblType"),
        ("MITEL-CMNALM-MIB", "mitelAlmActiveTblTypeName"),
        ("MITEL-CMNALM-MIB", "mitelAlmActiveTblSeverity"),
        ("MITEL-CMNALM-MIB", "mitelAlmActiveTblThresholdType"),
        ("MITEL-CMNALM-MIB", "mitelAlmActiveTblThresholdValue"))
)
if mibBuilder.loadTexts:
    mitelNotifActiveAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-CMNALM-MIB",
    **{"ItuPerceivedSeverity": ItuPerceivedSeverity,
       "MitelCmnAlarmThresholdType": MitelCmnAlarmThresholdType,
       "mitelCmnAlarms": mitelCmnAlarms,
       "mitelCmnAlmObjects": mitelCmnAlmObjects,
       "mitelAlmSystem": mitelAlmSystem,
       "mitelAlmSysSeverity": mitelAlmSysSeverity,
       "mitelAlmSysSeverityDetectTime": mitelAlmSysSeverityDetectTime,
       "mitelAlmSysSeverityDescr": mitelAlmSysSeverityDescr,
       "mitelAlmActiveTable": mitelAlmActiveTable,
       "mitelAlmActiveTableEntry": mitelAlmActiveTableEntry,
       "mitelAlmActiveTblIndex": mitelAlmActiveTblIndex,
       "mitelAlmActiveTblClass": mitelAlmActiveTblClass,
       "mitelAlmActiveTblType": mitelAlmActiveTblType,
       "mitelAlmActiveTblTypeName": mitelAlmActiveTblTypeName,
       "mitelAlmActiveTblSeverity": mitelAlmActiveTblSeverity,
       "mitelAlmActiveTblSeverityDetectTime": mitelAlmActiveTblSeverityDetectTime,
       "mitelAlmActiveTblThresholdType": mitelAlmActiveTblThresholdType,
       "mitelAlmActiveTblThresholdValue": mitelAlmActiveTblThresholdValue,
       "mitelAlmActiveTblDescr": mitelAlmActiveTblDescr,
       "mitelCmnAlmNotifications": mitelCmnAlmNotifications,
       "mitelNotifActiveAlarm": mitelNotifActiveAlarm,
       "mitelCmnAlmConformance": mitelCmnAlmConformance}
)
