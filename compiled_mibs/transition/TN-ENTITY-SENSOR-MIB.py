# SNMP MIB module (TN-ENTITY-SENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-ENTITY-SENSOR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:22 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(EntitySensorValue,
 entPhySensorValue) = mibBuilder.importSymbols(
    "ENTITY-SENSOR-MIB",
    "EntitySensorValue",
    "entPhySensorValue")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnEntitySensorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6)
)
if mibBuilder.loadTexts:
    tnEntitySensorMIB.setRevisions(
        ("2009-01-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TnSensorThresholdSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("minor", 10),
          ("major", 20),
          ("critical", 30))
    )



class TnSensorThresholdRelation(TextualConvention, Integer32):
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
        *(("lessThan", 1),
          ("lessOrEqual", 2),
          ("greaterThan", 3),
          ("greaterOrEqual", 4),
          ("equalTo", 5),
          ("notEqualTo", 6))
    )



# MIB Managed Objects in the order of their OIDs

_TnEntitySensorMIBNotifications_ObjectIdentity = ObjectIdentity
tnEntitySensorMIBNotifications = _TnEntitySensorMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 0)
)
_TnEntitySensorMIBObjects_ObjectIdentity = ObjectIdentity
tnEntitySensorMIBObjects = _TnEntitySensorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1)
)
_TnEntSensorValues_ObjectIdentity = ObjectIdentity
tnEntSensorValues = _TnEntSensorValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 1)
)
_TnEntSensorExtTable_Object = MibTable
tnEntSensorExtTable = _TnEntSensorExtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnEntSensorExtTable.setStatus("current")
_TnEntSensorExtEntry_Object = MibTableRow
tnEntSensorExtEntry = _TnEntSensorExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 1, 1, 1)
)
tnEntSensorExtEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnEntSensorExtEntry.setStatus("current")
_TnEntSensorExtRelayInstalled_Type = TruthValue
_TnEntSensorExtRelayInstalled_Object = MibTableColumn
tnEntSensorExtRelayInstalled = _TnEntSensorExtRelayInstalled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 1, 1, 1, 1),
    _TnEntSensorExtRelayInstalled_Type()
)
tnEntSensorExtRelayInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEntSensorExtRelayInstalled.setStatus("current")
_TnEntSensorExtRelayEnabled_Type = TruthValue
_TnEntSensorExtRelayEnabled_Object = MibTableColumn
tnEntSensorExtRelayEnabled = _TnEntSensorExtRelayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 1, 1, 1, 2),
    _TnEntSensorExtRelayEnabled_Type()
)
tnEntSensorExtRelayEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEntSensorExtRelayEnabled.setStatus("current")


class _TnEntSensorExtModuleType_Type(Integer32):
    """Custom type tnEntSensorExtModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acModule", 1),
          ("dcModule", 2))
    )


_TnEntSensorExtModuleType_Type.__name__ = "Integer32"
_TnEntSensorExtModuleType_Object = MibTableColumn
tnEntSensorExtModuleType = _TnEntSensorExtModuleType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 1, 1, 1, 3),
    _TnEntSensorExtModuleType_Type()
)
tnEntSensorExtModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEntSensorExtModuleType.setStatus("current")


class _TnEntSensorExtOperMode_Type(Integer32):
    """Custom type tnEntSensorExtOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_TnEntSensorExtOperMode_Type.__name__ = "Integer32"
_TnEntSensorExtOperMode_Object = MibTableColumn
tnEntSensorExtOperMode = _TnEntSensorExtOperMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 1, 1, 1, 4),
    _TnEntSensorExtOperMode_Type()
)
tnEntSensorExtOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEntSensorExtOperMode.setStatus("current")
_TnEntSensorThresholds_ObjectIdentity = ObjectIdentity
tnEntSensorThresholds = _TnEntSensorThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 2)
)
_TnEntSensorThresholdTable_Object = MibTable
tnEntSensorThresholdTable = _TnEntSensorThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnEntSensorThresholdTable.setStatus("current")
_TnEntSensorThresholdEntry_Object = MibTableRow
tnEntSensorThresholdEntry = _TnEntSensorThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 2, 1, 1)
)
tnEntSensorThresholdEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TN-ENTITY-SENSOR-MIB", "tnEntSensorThresholdIndex"),
)
if mibBuilder.loadTexts:
    tnEntSensorThresholdEntry.setStatus("current")


class _TnEntSensorThresholdIndex_Type(Integer32):
    """Custom type tnEntSensorThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999999),
    )


_TnEntSensorThresholdIndex_Type.__name__ = "Integer32"
_TnEntSensorThresholdIndex_Object = MibTableColumn
tnEntSensorThresholdIndex = _TnEntSensorThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 2, 1, 1, 1),
    _TnEntSensorThresholdIndex_Type()
)
tnEntSensorThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEntSensorThresholdIndex.setStatus("current")
_TnEntSensorThresholdSeverity_Type = TnSensorThresholdSeverity
_TnEntSensorThresholdSeverity_Object = MibTableColumn
tnEntSensorThresholdSeverity = _TnEntSensorThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 2, 1, 1, 2),
    _TnEntSensorThresholdSeverity_Type()
)
tnEntSensorThresholdSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEntSensorThresholdSeverity.setStatus("current")
_TnEntSensorThresholdRelation_Type = TnSensorThresholdRelation
_TnEntSensorThresholdRelation_Object = MibTableColumn
tnEntSensorThresholdRelation = _TnEntSensorThresholdRelation_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 2, 1, 1, 3),
    _TnEntSensorThresholdRelation_Type()
)
tnEntSensorThresholdRelation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEntSensorThresholdRelation.setStatus("current")
_TnEntSensorThresholdValue_Type = EntitySensorValue
_TnEntSensorThresholdValue_Object = MibTableColumn
tnEntSensorThresholdValue = _TnEntSensorThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 2, 1, 1, 4),
    _TnEntSensorThresholdValue_Type()
)
tnEntSensorThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEntSensorThresholdValue.setStatus("current")
_TnEntSensorThresholdEvaluation_Type = TruthValue
_TnEntSensorThresholdEvaluation_Object = MibTableColumn
tnEntSensorThresholdEvaluation = _TnEntSensorThresholdEvaluation_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 2, 1, 1, 5),
    _TnEntSensorThresholdEvaluation_Type()
)
tnEntSensorThresholdEvaluation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEntSensorThresholdEvaluation.setStatus("current")
_TnEntSensorThresholdNotificationEnable_Type = TruthValue
_TnEntSensorThresholdNotificationEnable_Object = MibTableColumn
tnEntSensorThresholdNotificationEnable = _TnEntSensorThresholdNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 2, 1, 1, 6),
    _TnEntSensorThresholdNotificationEnable_Type()
)
tnEntSensorThresholdNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEntSensorThresholdNotificationEnable.setStatus("current")
_TnEntSensorGlobalObjects_ObjectIdentity = ObjectIdentity
tnEntSensorGlobalObjects = _TnEntSensorGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 3)
)
_TnEntSensorThreshNotifGlobalEnable_Type = TruthValue
_TnEntSensorThreshNotifGlobalEnable_Object = MibScalar
tnEntSensorThreshNotifGlobalEnable = _TnEntSensorThreshNotifGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 1, 3, 1),
    _TnEntSensorThreshNotifGlobalEnable_Type()
)
tnEntSensorThreshNotifGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEntSensorThreshNotifGlobalEnable.setStatus("current")
_TnEntitySensorMIBConformance_ObjectIdentity = ObjectIdentity
tnEntitySensorMIBConformance = _TnEntitySensorMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 2)
)

# Managed Objects groups


# Notification objects

tnEntSensorThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 6, 0, 1)
)
tnEntSensorThresholdNotification.setObjects(
      *(("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("TN-ENTITY-SENSOR-MIB", "tnEntSensorThresholdValue"),
        ("TN-ENTITY-SENSOR-MIB", "tnEntSensorThresholdSeverity"))
)
if mibBuilder.loadTexts:
    tnEntSensorThresholdNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-ENTITY-SENSOR-MIB",
    **{"TnSensorThresholdSeverity": TnSensorThresholdSeverity,
       "TnSensorThresholdRelation": TnSensorThresholdRelation,
       "tnEntitySensorMIB": tnEntitySensorMIB,
       "tnEntitySensorMIBNotifications": tnEntitySensorMIBNotifications,
       "tnEntSensorThresholdNotification": tnEntSensorThresholdNotification,
       "tnEntitySensorMIBObjects": tnEntitySensorMIBObjects,
       "tnEntSensorValues": tnEntSensorValues,
       "tnEntSensorExtTable": tnEntSensorExtTable,
       "tnEntSensorExtEntry": tnEntSensorExtEntry,
       "tnEntSensorExtRelayInstalled": tnEntSensorExtRelayInstalled,
       "tnEntSensorExtRelayEnabled": tnEntSensorExtRelayEnabled,
       "tnEntSensorExtModuleType": tnEntSensorExtModuleType,
       "tnEntSensorExtOperMode": tnEntSensorExtOperMode,
       "tnEntSensorThresholds": tnEntSensorThresholds,
       "tnEntSensorThresholdTable": tnEntSensorThresholdTable,
       "tnEntSensorThresholdEntry": tnEntSensorThresholdEntry,
       "tnEntSensorThresholdIndex": tnEntSensorThresholdIndex,
       "tnEntSensorThresholdSeverity": tnEntSensorThresholdSeverity,
       "tnEntSensorThresholdRelation": tnEntSensorThresholdRelation,
       "tnEntSensorThresholdValue": tnEntSensorThresholdValue,
       "tnEntSensorThresholdEvaluation": tnEntSensorThresholdEvaluation,
       "tnEntSensorThresholdNotificationEnable": tnEntSensorThresholdNotificationEnable,
       "tnEntSensorGlobalObjects": tnEntSensorGlobalObjects,
       "tnEntSensorThreshNotifGlobalEnable": tnEntSensorThreshNotifGlobalEnable,
       "tnEntitySensorMIBConformance": tnEntitySensorMIBConformance}
)
