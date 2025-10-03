# SNMP MIB module (ENDACE-INVMGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\endace\ENDACE-INVMGR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:57 2025
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

(endace,) = mibBuilder.importSymbols(
    "ENDACE-MIB",
    "endace")

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

invmgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 15)
)
if mibBuilder.loadTexts:
    invmgrMIB.setRevisions(
        ("2021-07-21 02:57",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_InvmgrNotifications_ObjectIdentity = ObjectIdentity
invmgrNotifications = _InvmgrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 15, 0)
)
_InvmgrObjects_ObjectIdentity = ObjectIdentity
invmgrObjects = _InvmgrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 15, 1)
)
_InvmgrApplStateTable_Object = MibTable
invmgrApplStateTable = _InvmgrApplStateTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 15, 1, 1)
)
if mibBuilder.loadTexts:
    invmgrApplStateTable.setStatus("current")
_InvmgrApplStateEntry_Object = MibTableRow
invmgrApplStateEntry = _InvmgrApplStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 15, 1, 1, 1)
)
invmgrApplStateEntry.setIndexNames(
    (0, "ENDACE-INVMGR-MIB", "invmgrApplStateIndex"),
)
if mibBuilder.loadTexts:
    invmgrApplStateEntry.setStatus("current")


class _InvmgrApplStateIndex_Type(Integer32):
    """Custom type invmgrApplStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_InvmgrApplStateIndex_Type.__name__ = "Integer32"
_InvmgrApplStateIndex_Object = MibTableColumn
invmgrApplStateIndex = _InvmgrApplStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 15, 1, 1, 1, 1),
    _InvmgrApplStateIndex_Type()
)
invmgrApplStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    invmgrApplStateIndex.setStatus("current")
_InvmgrApplStateName_Type = DisplayString
_InvmgrApplStateName_Object = MibTableColumn
invmgrApplStateName = _InvmgrApplStateName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 15, 1, 1, 1, 2),
    _InvmgrApplStateName_Type()
)
invmgrApplStateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invmgrApplStateName.setStatus("current")
_InvmgrApplStateConnected_Type = TruthValue
_InvmgrApplStateConnected_Object = MibTableColumn
invmgrApplStateConnected = _InvmgrApplStateConnected_Object(
    (1, 3, 6, 1, 4, 1, 18418, 15, 1, 1, 1, 3),
    _InvmgrApplStateConnected_Type()
)
invmgrApplStateConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invmgrApplStateConnected.setStatus("current")
_InvmgrApplStateOK_Type = TruthValue
_InvmgrApplStateOK_Object = MibTableColumn
invmgrApplStateOK = _InvmgrApplStateOK_Object(
    (1, 3, 6, 1, 4, 1, 18418, 15, 1, 1, 1, 4),
    _InvmgrApplStateOK_Type()
)
invmgrApplStateOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invmgrApplStateOK.setStatus("current")
_InvmgrApplConfigTable_Object = MibTable
invmgrApplConfigTable = _InvmgrApplConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 15, 1, 2)
)
if mibBuilder.loadTexts:
    invmgrApplConfigTable.setStatus("current")
_InvmgrApplConfigEntry_Object = MibTableRow
invmgrApplConfigEntry = _InvmgrApplConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 15, 1, 2, 1)
)
invmgrApplConfigEntry.setIndexNames(
    (0, "ENDACE-INVMGR-MIB", "invmgrApplConfigIndex"),
)
if mibBuilder.loadTexts:
    invmgrApplConfigEntry.setStatus("current")


class _InvmgrApplConfigIndex_Type(Integer32):
    """Custom type invmgrApplConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_InvmgrApplConfigIndex_Type.__name__ = "Integer32"
_InvmgrApplConfigIndex_Object = MibTableColumn
invmgrApplConfigIndex = _InvmgrApplConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 15, 1, 2, 1, 1),
    _InvmgrApplConfigIndex_Type()
)
invmgrApplConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    invmgrApplConfigIndex.setStatus("current")
_InvmgrApplConfigName_Type = DisplayString
_InvmgrApplConfigName_Object = MibTableColumn
invmgrApplConfigName = _InvmgrApplConfigName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 15, 1, 2, 1, 2),
    _InvmgrApplConfigName_Type()
)
invmgrApplConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invmgrApplConfigName.setStatus("current")
_InvmgrApplConfigEnabled_Type = TruthValue
_InvmgrApplConfigEnabled_Object = MibTableColumn
invmgrApplConfigEnabled = _InvmgrApplConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 18418, 15, 1, 2, 1, 3),
    _InvmgrApplConfigEnabled_Type()
)
invmgrApplConfigEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invmgrApplConfigEnabled.setStatus("current")
_InvmgrConformance_ObjectIdentity = ObjectIdentity
invmgrConformance = _InvmgrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 15, 2)
)
_InvmgrCompliances_ObjectIdentity = ObjectIdentity
invmgrCompliances = _InvmgrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 15, 2, 1)
)
_InvmgrGroups_ObjectIdentity = ObjectIdentity
invmgrGroups = _InvmgrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 15, 2, 2)
)

# Managed Objects groups

invmgrBasicObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 15, 2, 2, 1)
)
invmgrBasicObjects.setObjects(
      *(("ENDACE-INVMGR-MIB", "invmgrApplConfigEnabled"),
        ("ENDACE-INVMGR-MIB", "invmgrApplConfigName"),
        ("ENDACE-INVMGR-MIB", "invmgrApplStateConnected"),
        ("ENDACE-INVMGR-MIB", "invmgrApplStateName"),
        ("ENDACE-INVMGR-MIB", "invmgrApplStateOK"))
)
if mibBuilder.loadTexts:
    invmgrBasicObjects.setStatus("current")


# Notification objects

invmgrConnectionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 15, 0, 1)
)
invmgrConnectionChanged.setObjects(
      *(("ENDACE-INVMGR-MIB", "invmgrApplStateName"),
        ("ENDACE-INVMGR-MIB", "invmgrApplStateConnected"))
)
if mibBuilder.loadTexts:
    invmgrConnectionChanged.setStatus(
        "current"
    )


# Notifications groups

invmgrBasicEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 15, 2, 2, 2)
)
invmgrBasicEvents.setObjects(
    ("ENDACE-INVMGR-MIB", "invmgrConnectionChanged")
)
if mibBuilder.loadTexts:
    invmgrBasicEvents.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

invmgrMandatory = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18418, 15, 2, 1, 1)
)
invmgrMandatory.setObjects(
      *(("ENDACE-INVMGR-MIB", "invmgrBasicEvents"),
        ("ENDACE-INVMGR-MIB", "invmgrBasicObjects"))
)
if mibBuilder.loadTexts:
    invmgrMandatory.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENDACE-INVMGR-MIB",
    **{"invmgrMIB": invmgrMIB,
       "invmgrNotifications": invmgrNotifications,
       "invmgrConnectionChanged": invmgrConnectionChanged,
       "invmgrObjects": invmgrObjects,
       "invmgrApplStateTable": invmgrApplStateTable,
       "invmgrApplStateEntry": invmgrApplStateEntry,
       "invmgrApplStateIndex": invmgrApplStateIndex,
       "invmgrApplStateName": invmgrApplStateName,
       "invmgrApplStateConnected": invmgrApplStateConnected,
       "invmgrApplStateOK": invmgrApplStateOK,
       "invmgrApplConfigTable": invmgrApplConfigTable,
       "invmgrApplConfigEntry": invmgrApplConfigEntry,
       "invmgrApplConfigIndex": invmgrApplConfigIndex,
       "invmgrApplConfigName": invmgrApplConfigName,
       "invmgrApplConfigEnabled": invmgrApplConfigEnabled,
       "invmgrConformance": invmgrConformance,
       "invmgrCompliances": invmgrCompliances,
       "invmgrMandatory": invmgrMandatory,
       "invmgrGroups": invmgrGroups,
       "invmgrBasicObjects": invmgrBasicObjects,
       "invmgrBasicEvents": invmgrBasicEvents}
)
