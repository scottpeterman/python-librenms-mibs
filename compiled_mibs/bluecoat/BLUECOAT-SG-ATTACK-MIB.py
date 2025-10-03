# SNMP MIB module (BLUECOAT-SG-ATTACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecoat\BLUECOAT-SG-ATTACK-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:37 2025
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

(blueCoatMgmt,) = mibBuilder.importSymbols(
    "BLUECOAT-MIB",
    "blueCoatMgmt")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

deviceAttackMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 3)
)
if mibBuilder.loadTexts:
    deviceAttackMIB.setRevisions(
        ("2007-11-05 03:00",
         "2002-11-06 03:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AttackStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAttack", 1),
          ("underAttack", 2))
    )



# MIB Managed Objects in the order of their OIDs

_DeviceAttackMIBObjects_ObjectIdentity = ObjectIdentity
deviceAttackMIBObjects = _DeviceAttackMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 3, 1)
)
_DeviceAttackValues_ObjectIdentity = ObjectIdentity
deviceAttackValues = _DeviceAttackValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1)
)
_DeviceAttackTable_Object = MibTable
deviceAttackTable = _DeviceAttackTable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    deviceAttackTable.setStatus("current")
_DeviceAttackEntry_Object = MibTableRow
deviceAttackEntry = _DeviceAttackEntry_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1, 1)
)
deviceAttackEntry.setIndexNames(
    (0, "BLUECOAT-SG-ATTACK-MIB", "deviceAttackIndex"),
)
if mibBuilder.loadTexts:
    deviceAttackEntry.setStatus("current")


class _DeviceAttackIndex_Type(Integer32):
    """Custom type deviceAttackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DeviceAttackIndex_Type.__name__ = "Integer32"
_DeviceAttackIndex_Object = MibTableColumn
deviceAttackIndex = _DeviceAttackIndex_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1, 1, 1),
    _DeviceAttackIndex_Type()
)
deviceAttackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceAttackIndex.setStatus("current")
_DeviceAttackName_Type = DisplayString
_DeviceAttackName_Object = MibTableColumn
deviceAttackName = _DeviceAttackName_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1, 1, 2),
    _DeviceAttackName_Type()
)
deviceAttackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAttackName.setStatus("current")
_DeviceAttackStatus_Type = AttackStatus
_DeviceAttackStatus_Object = MibTableColumn
deviceAttackStatus = _DeviceAttackStatus_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1, 1, 3),
    _DeviceAttackStatus_Type()
)
deviceAttackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAttackStatus.setStatus("current")
_DeviceAttackTime_Type = TimeStamp
_DeviceAttackTime_Object = MibTableColumn
deviceAttackTime = _DeviceAttackTime_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1, 1, 4),
    _DeviceAttackTime_Type()
)
deviceAttackTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAttackTime.setStatus("current")
if mibBuilder.loadTexts:
    deviceAttackTime.setUnits("Hundredths of seconds")
_DeviceAttackMIBNotifications_ObjectIdentity = ObjectIdentity
deviceAttackMIBNotifications = _DeviceAttackMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 3, 2)
)
_DeviceAttackMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
deviceAttackMIBNotificationsPrefix = _DeviceAttackMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 3, 2, 0)
)

# Managed Objects groups


# Notification objects

deviceAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 3, 2, 0, 1)
)
deviceAttackTrap.setObjects(
      *(("BLUECOAT-SG-ATTACK-MIB", "deviceAttackName"),
        ("BLUECOAT-SG-ATTACK-MIB", "deviceAttackStatus"))
)
if mibBuilder.loadTexts:
    deviceAttackTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUECOAT-SG-ATTACK-MIB",
    **{"AttackStatus": AttackStatus,
       "deviceAttackMIB": deviceAttackMIB,
       "deviceAttackMIBObjects": deviceAttackMIBObjects,
       "deviceAttackValues": deviceAttackValues,
       "deviceAttackTable": deviceAttackTable,
       "deviceAttackEntry": deviceAttackEntry,
       "deviceAttackIndex": deviceAttackIndex,
       "deviceAttackName": deviceAttackName,
       "deviceAttackStatus": deviceAttackStatus,
       "deviceAttackTime": deviceAttackTime,
       "deviceAttackMIBNotifications": deviceAttackMIBNotifications,
       "deviceAttackMIBNotificationsPrefix": deviceAttackMIBNotificationsPrefix,
       "deviceAttackTrap": deviceAttackTrap}
)
