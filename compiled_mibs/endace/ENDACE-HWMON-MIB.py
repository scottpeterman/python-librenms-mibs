# SNMP MIB module (ENDACE-HWMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\endace\ENDACE-HWMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:56 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hwmonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 16)
)
if mibBuilder.loadTexts:
    hwmonMIB.setRevisions(
        ("2023-06-08 02:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwmonNotifications_ObjectIdentity = ObjectIdentity
hwmonNotifications = _HwmonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 16, 0)
)
if mibBuilder.loadTexts:
    hwmonNotifications.setStatus("current")
_HwmonObjects_ObjectIdentity = ObjectIdentity
hwmonObjects = _HwmonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 16, 1)
)
if mibBuilder.loadTexts:
    hwmonObjects.setStatus("current")


class _HwmonFanRedundancy_Type(Integer32):
    """Custom type hwmonFanRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fault", 2))
    )


_HwmonFanRedundancy_Type.__name__ = "Integer32"
_HwmonFanRedundancy_Object = MibScalar
hwmonFanRedundancy = _HwmonFanRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 18418, 16, 1, 1),
    _HwmonFanRedundancy_Type()
)
hwmonFanRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwmonFanRedundancy.setStatus("current")


class _HwmonPsuRedundancy_Type(Integer32):
    """Custom type hwmonPsuRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fault", 2))
    )


_HwmonPsuRedundancy_Type.__name__ = "Integer32"
_HwmonPsuRedundancy_Object = MibScalar
hwmonPsuRedundancy = _HwmonPsuRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 18418, 16, 1, 2),
    _HwmonPsuRedundancy_Type()
)
hwmonPsuRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwmonPsuRedundancy.setStatus("current")


class _HwmonIntrusionStatus_Type(Integer32):
    """Custom type hwmonIntrusionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_HwmonIntrusionStatus_Type.__name__ = "Integer32"
_HwmonIntrusionStatus_Object = MibScalar
hwmonIntrusionStatus = _HwmonIntrusionStatus_Object(
    (1, 3, 6, 1, 4, 1, 18418, 16, 1, 3),
    _HwmonIntrusionStatus_Type()
)
hwmonIntrusionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwmonIntrusionStatus.setStatus("current")
_HwmonSystemTemp_Type = Integer32
_HwmonSystemTemp_Object = MibScalar
hwmonSystemTemp = _HwmonSystemTemp_Object(
    (1, 3, 6, 1, 4, 1, 18418, 16, 1, 4),
    _HwmonSystemTemp_Type()
)
hwmonSystemTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwmonSystemTemp.setStatus("current")
_HwmonConformance_ObjectIdentity = ObjectIdentity
hwmonConformance = _HwmonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 16, 2)
)

# Managed Objects groups

hwmonObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 16, 2, 1)
)
hwmonObjectGroup.setObjects(
      *(("ENDACE-HWMON-MIB", "hwmonFanRedundancy"),
        ("ENDACE-HWMON-MIB", "hwmonIntrusionStatus"),
        ("ENDACE-HWMON-MIB", "hwmonPsuRedundancy"),
        ("ENDACE-HWMON-MIB", "hwmonSystemTemp"))
)
if mibBuilder.loadTexts:
    hwmonObjectGroup.setStatus("current")


# Notification objects

hwmonFanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 16, 0, 1)
)
if mibBuilder.loadTexts:
    hwmonFanFault.setStatus(
        "current"
    )

hwmonFanNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 16, 0, 2)
)
if mibBuilder.loadTexts:
    hwmonFanNormal.setStatus(
        "current"
    )

hwmonPSUFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 16, 0, 3)
)
if mibBuilder.loadTexts:
    hwmonPSUFault.setStatus(
        "current"
    )

hwmonPSUNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 16, 0, 4)
)
if mibBuilder.loadTexts:
    hwmonPSUNormal.setStatus(
        "current"
    )

hwmonIntrusionAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 16, 0, 5)
)
if mibBuilder.loadTexts:
    hwmonIntrusionAlarm.setStatus(
        "current"
    )

hwmonIntrusionNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 16, 0, 6)
)
if mibBuilder.loadTexts:
    hwmonIntrusionNormal.setStatus(
        "current"
    )

hwmonSystemTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 16, 0, 7)
)
hwmonSystemTempHigh.setObjects(
    ("ENDACE-HWMON-MIB", "hwmonSystemTemp")
)
if mibBuilder.loadTexts:
    hwmonSystemTempHigh.setStatus(
        "current"
    )

hwmonSystemTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 16, 0, 8)
)
hwmonSystemTempNormal.setObjects(
    ("ENDACE-HWMON-MIB", "hwmonSystemTemp")
)
if mibBuilder.loadTexts:
    hwmonSystemTempNormal.setStatus(
        "current"
    )

hwmonSystemTempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 16, 0, 9)
)
hwmonSystemTempLow.setObjects(
    ("ENDACE-HWMON-MIB", "hwmonSystemTemp")
)
if mibBuilder.loadTexts:
    hwmonSystemTempLow.setStatus(
        "current"
    )


# Notifications groups

hwmonNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 16, 2, 2)
)
hwmonNotifyGroup.setObjects(
      *(("ENDACE-HWMON-MIB", "hwmonFanFault"),
        ("ENDACE-HWMON-MIB", "hwmonFanNormal"),
        ("ENDACE-HWMON-MIB", "hwmonIntrusionAlarm"),
        ("ENDACE-HWMON-MIB", "hwmonIntrusionNormal"),
        ("ENDACE-HWMON-MIB", "hwmonPSUFault"),
        ("ENDACE-HWMON-MIB", "hwmonPSUNormal"),
        ("ENDACE-HWMON-MIB", "hwmonSystemTempHigh"),
        ("ENDACE-HWMON-MIB", "hwmonSystemTempNormal"),
        ("ENDACE-HWMON-MIB", "hwmonSystemTempLow"))
)
if mibBuilder.loadTexts:
    hwmonNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENDACE-HWMON-MIB",
    **{"hwmonMIB": hwmonMIB,
       "hwmonNotifications": hwmonNotifications,
       "hwmonFanFault": hwmonFanFault,
       "hwmonFanNormal": hwmonFanNormal,
       "hwmonPSUFault": hwmonPSUFault,
       "hwmonPSUNormal": hwmonPSUNormal,
       "hwmonIntrusionAlarm": hwmonIntrusionAlarm,
       "hwmonIntrusionNormal": hwmonIntrusionNormal,
       "hwmonSystemTempHigh": hwmonSystemTempHigh,
       "hwmonSystemTempNormal": hwmonSystemTempNormal,
       "hwmonSystemTempLow": hwmonSystemTempLow,
       "hwmonObjects": hwmonObjects,
       "hwmonFanRedundancy": hwmonFanRedundancy,
       "hwmonPsuRedundancy": hwmonPsuRedundancy,
       "hwmonIntrusionStatus": hwmonIntrusionStatus,
       "hwmonSystemTemp": hwmonSystemTemp,
       "hwmonConformance": hwmonConformance,
       "hwmonObjectGroup": hwmonObjectGroup,
       "hwmonNotifyGroup": hwmonNotifyGroup}
)
